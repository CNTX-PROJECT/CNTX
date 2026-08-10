"""Closed Schema Resource registration, closure checks, and evaluation."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .limits import DEFAULT_LIMITS, ResourceLimits, require_at_most, require_exact
from .path_safety import resolve_beneath
from .strict_json import load_strict

SCHEMA_IDENTITIES = {
    "common-artifact-envelope": "https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0",
    "project-charter": "https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0",
    "workstream": "https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0",
    "task-contract": "https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0",
    "context-packet": "https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0",
    "execution-result": "https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0",
    "evidence-bundle": "https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0",
    "review-record": "https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0",
    "decision-record": "https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0",
    "state-snapshot": "https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0",
}


class ResourceError(ValueError):
    """A closed-resource or static-reference failure."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _walk_refs(value: Any) -> Iterable[str]:
    stack = [value]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            ref = current.get("$ref")
            if isinstance(ref, str):
                yield ref
            stack.extend(current.values())
        elif isinstance(current, list):
            stack.extend(current)


def _pointer_exists(document: Any, fragment: str) -> bool:
    if fragment in {"", "#"}:
        return True
    if not fragment.startswith("#/"):
        return False
    current = document
    for raw in fragment[2:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and token in current:
            current = current[token]
        elif isinstance(current, list) and token.isdigit() and int(token) < len(current):
            current = current[int(token)]
        else:
            return False
    return True


@dataclass(frozen=True)
class ResourceSet:
    documents: dict[str, dict[str, Any]]
    paths: dict[str, Path]
    digests: dict[str, str]
    reference_count: int

    def check_schemas(self) -> list[dict[str, str]]:
        from jsonschema import Draft202012Validator

        observations: list[dict[str, str]] = []
        for identity in sorted(self.documents):
            Draft202012Validator.check_schema(self.documents[identity])
            observations.append({"schemaIdentity": identity, "outcome": "satisfied"})
        return observations

    def evaluate(self, identity: str, instance: Any) -> tuple[bool, list[str]]:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource

        if identity not in self.documents:
            raise ResourceError(f"unsupported Schema Resource: {identity}")
        registry = Registry().with_resources(
            (key, Resource.from_contents(document))
            for key, document in sorted(self.documents.items())
        )
        validator = Draft202012Validator(self.documents[identity], registry=registry)
        errors = sorted(
            validator.iter_errors(instance),
            key=lambda item: (tuple(str(part) for part in item.absolute_path), item.message),
        )
        diagnostics = [
            f"/{'/'.join(str(part) for part in error.absolute_path)}: {error.message}"
            for error in errors
        ]
        return not errors, diagnostics


def load_resource_set(
    declarations: list[dict[str, Any]],
    input_root: Path,
    limits: ResourceLimits = DEFAULT_LIMITS,
) -> ResourceSet:
    require_exact("Schema Resources", len(declarations), limits.schema_resources)
    expected = set(SCHEMA_IDENTITIES.values())
    supplied = [item.get("identity") for item in declarations]
    if len(set(supplied)) != len(supplied):
        raise ResourceError("duplicate Schema Resource identity")
    if set(supplied) != expected:
        raise ResourceError("missing, additional, or unsupported Schema Resource identity")

    documents: dict[str, dict[str, Any]] = {}
    paths: dict[str, Path] = {}
    digests: dict[str, str] = {}
    for item in declarations:
        if set(item) != {"identity", "version", "path", "sha256"}:
            raise ResourceError("Schema Resource declaration has unknown or missing members")
        identity = item["identity"]
        if item["version"] != "1.0.0":
            raise ResourceError(f"unsupported Schema Resource version for {identity}")
        path = resolve_beneath(input_root, item["path"], must_exist=True)
        digest = sha256_file(path)
        if digest != item["sha256"]:
            raise ResourceError(f"Schema Resource digest mismatch for {identity}")
        document = load_strict(path, limits)
        if not isinstance(document, dict) or document.get("$id") != identity:
            raise ResourceError(f"Schema Resource $id mismatch for {identity}")
        documents[identity] = document
        paths[identity] = path
        digests[identity] = digest

    references: list[tuple[str, str]] = []
    for identity, document in documents.items():
        references.extend((identity, ref) for ref in _walk_refs(document))
    require_at_most("static $ref occurrences", len(references), limits.ref_occurrences)
    require_at_most("resource graph edges", len(references), limits.graph_edges)
    require_at_most("resource graph nodes", len(documents), limits.graph_nodes)
    require_at_most("static reference expansions", len(references), limits.expansions)

    adjacency: dict[str, set[str]] = {identity: set() for identity in documents}
    for owner, ref in references:
        if ref.startswith("#"):
            target_identity, fragment = owner, ref
        else:
            target_identity, marker, suffix = ref.partition("#")
            fragment = f"#{suffix}" if marker else ""
        target = documents.get(target_identity)
        if target is None:
            raise ResourceError(f"unregistered static reference: {ref}")
        if fragment and not _pointer_exists(target, fragment):
            raise ResourceError(f"unresolved static reference fragment: {ref}")
        adjacency[owner].add(target_identity)

    traversed_paths = 0

    def assess_depth(identity: str, path: tuple[str, ...]) -> None:
        nonlocal traversed_paths
        traversed_paths += 1
        require_at_most("static reference traversal steps", traversed_paths, limits.expansions)
        require_at_most("static reference expansion depth", len(path), limits.expansion_depth)
        for target_identity in sorted(adjacency[identity]):
            if target_identity not in path:
                assess_depth(target_identity, path + (target_identity,))

    for identity in sorted(documents):
        assess_depth(identity, (identity,))

    return ResourceSet(documents, paths, digests, len(references))
