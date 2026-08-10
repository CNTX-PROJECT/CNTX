"""Historical direct and operation-based Test Manifest construction."""

from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .limits import DEFAULT_LIMITS, ResourceLimits, require_at_most, require_exact
from .path_safety import resolve_beneath
from .resources import SCHEMA_IDENTITIES, sha256_file
from .strict_json import load_strict

EXPECTED_MANIFEST_PATHS = {
    identity: f"tests/schemas/{slug}/1.0.0/cases.json"
    for slug, identity in SCHEMA_IDENTITIES.items()
}


class ManifestError(ValueError):
    """A manifest recognition or construction failure."""


@dataclass(frozen=True)
class ConstructedCase:
    manifest_key: str
    case_key: str
    supplied_order: int
    construction_form: str
    schema_identity: str
    expected_validity: bool
    instance: Any | None
    construction_error: str | None = None


def _tokens(pointer: str) -> list[str]:
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ManifestError("operation path is not an RFC 6901 JSON Pointer")
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]


def _parent(root: Any, tokens: list[str]) -> tuple[Any, str]:
    if not tokens:
        return None, ""
    current = root
    for token in tokens[:-1]:
        if isinstance(current, dict) and token in current:
            current = current[token]
        elif isinstance(current, list) and token.isdigit() and int(token) < len(current):
            current = current[int(token)]
        else:
            raise ManifestError("operation path does not resolve")
    return current, tokens[-1]


def _apply(root: Any, operation: dict[str, Any]) -> Any:
    if set(operation) not in ({"op", "path"}, {"op", "path", "value"}):
        raise ManifestError("operation has unknown or missing members")
    op = operation.get("op")
    if op not in {"add", "remove", "replace"}:
        raise ManifestError("unknown operation")
    if op in {"add", "replace"} and "value" not in operation:
        raise ManifestError("operation value missing")
    tokens = _tokens(operation.get("path", ""))
    if not tokens:
        if op == "remove":
            raise ManifestError("root removal is unsupported")
        return copy.deepcopy(operation["value"])
    parent, token = _parent(root, tokens)
    if isinstance(parent, dict):
        exists = token in parent
        if op in {"remove", "replace"} and not exists:
            raise ManifestError("operation target is missing")
        if op == "remove":
            del parent[token]
        else:
            parent[token] = copy.deepcopy(operation["value"])
        return root
    if isinstance(parent, list):
        if op == "add" and token == "-":
            parent.append(copy.deepcopy(operation["value"]))
            return root
        if not token.isdigit():
            raise ManifestError("array index is not a non-negative integer")
        index = int(token)
        if op == "add":
            if index > len(parent):
                raise ManifestError("array insertion index is out of range")
            parent.insert(index, copy.deepcopy(operation["value"]))
        elif index >= len(parent):
            raise ManifestError("array target index is out of range")
        elif op == "remove":
            del parent[index]
        else:
            parent[index] = copy.deepcopy(operation["value"])
        return root
    raise ManifestError("operation parent is not a container")


def load_and_construct(
    declarations: list[dict[str, Any]],
    input_root: Path,
    limits: ResourceLimits = DEFAULT_LIMITS,
) -> tuple[list[ConstructedCase], dict[str, int]]:
    require_exact("Test Manifests", len(declarations), limits.manifests)
    supplied = [item.get("schemaIdentity") for item in declarations]
    if len(set(supplied)) != len(supplied):
        raise ManifestError("duplicate manifest Schema Identity")
    if set(supplied) != set(EXPECTED_MANIFEST_PATHS):
        raise ManifestError("missing, additional, or unsupported manifest")

    constructed: list[ConstructedCase] = []
    direct_count = operation_count = expected_valid = expected_invalid = total_ops = 0
    for declaration in sorted(declarations, key=lambda item: item["schemaIdentity"]):
        if set(declaration) != {"key", "schemaIdentity", "version", "path", "sha256", "construction"}:
            raise ManifestError("manifest declaration has unknown or missing members")
        identity = declaration["schemaIdentity"]
        expected_path = EXPECTED_MANIFEST_PATHS[identity]
        if declaration["path"] != expected_path or declaration["version"] != "1.0.0":
            raise ManifestError("manifest path or version mismatch")
        path = resolve_beneath(input_root, declaration["path"], must_exist=True)
        if sha256_file(path) != declaration["sha256"]:
            raise ManifestError("manifest digest mismatch")
        document = load_strict(path, limits)
        if not isinstance(document, dict) or document.get("schemaId") != identity:
            raise ManifestError("manifest schemaId mismatch")
        cases = document.get("cases")
        if not isinstance(cases, list):
            raise ManifestError("manifest cases missing")
        form = declaration["construction"]
        actual_form = "operation-based" if "baseInstance" in document else "direct"
        if form != actual_form:
            raise ManifestError("manifest construction form mismatch")
        direct_count += form == "direct"
        operation_count += form == "operation-based"
        seen: set[str] = set()
        for order, case in enumerate(cases):
            if not isinstance(case, dict) or not isinstance(case.get("name"), str):
                raise ManifestError("case key missing or malformed")
            key = case["name"]
            if key in seen:
                raise ManifestError("duplicate case key")
            seen.add(key)
            expected = case.get("valid")
            if not isinstance(expected, bool):
                raise ManifestError("expected-validity declaration missing")
            expected_valid += expected
            expected_invalid += not expected
            error: str | None = None
            instance: Any | None
            if form == "direct":
                if "instance" not in case:
                    error, instance = "direct instance missing", None
                else:
                    instance = copy.deepcopy(case["instance"])
            else:
                operations = case.get("operations")
                if not isinstance(operations, list):
                    error, instance = "operations missing", None
                else:
                    require_at_most("operations in one case", len(operations), limits.operations_per_case)
                    total_ops += len(operations)
                    require_at_most("operations across cases", total_ops, limits.operations_total)
                    instance = copy.deepcopy(document.get("baseInstance"))
                    try:
                        for operation in operations:
                            if not isinstance(operation, dict):
                                raise ManifestError("operation is not an object")
                            instance = _apply(instance, operation)
                    except ManifestError as exception:
                        error, instance = str(exception), None
            constructed.append(
                ConstructedCase(
                    declaration["key"], key, order, form, identity,
                    expected, instance, error,
                )
            )

    require_exact("cases", len(constructed), limits.cases)
    require_exact("expected-valid cases", expected_valid, 38)
    require_exact("expected-invalid cases", expected_invalid, 165)
    require_exact("direct manifests", direct_count, 9)
    require_exact("operation-based manifests", operation_count, 1)
    return constructed, {
        "manifests": len(declarations),
        "directManifests": direct_count,
        "operationBasedManifests": operation_count,
        "cases": len(constructed),
        "expectedValid": expected_valid,
        "expectedInvalid": expected_invalid,
        "operations": total_ops,
    }
