"""Closed, bounded orchestration for one caller-supplied invocation."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import platform
import re
import sys
import time
import tomllib
from pathlib import Path
from typing import Any

from . import IMPLEMENTATION_IDENTITY, IMPLEMENTATION_VERSION, TOOL_IDENTITY, TOOL_VERSION
from .integrity import RULE_NAMES, RULE_PREFIX, evaluate_rules
from .limits import DEFAULT_LIMITS, ResourceLimits, require_at_most
from .manifests import load_and_construct
from .models import CaseObservation, Diagnostic, RuleObservation, RunObservations
from .path_safety import resolve_beneath
from .presentation import human_summary, json_bytes
from .records import context_pins, evidence_package, integrity_record, validation_record
from .resources import load_resource_set
from .strict_json import load_strict

INVOCATION_KEYS = {
    "invocation", "tool", "implementation", "implementationSource",
    "validationSubject", "governingContext", "evaluatorContext",
    "dependencyLock", "configuration", "environment", "schemas",
    "manifests", "rules", "subjectRecords", "resourceLimits", "output",
    "executionWindow", "evidenceItems", "reproductionProcedures",
    "expectedInventory", "requestedOperations", "phaseApplicability",
    "adverseEvidence", "restrictedEvidence", "retentionAndCleanup",
    "claimBoundary", "roles", "network", "automaticAuthority",
}

EXPECTED_OPERATIONS = [
    "schema-resource-checking",
    "test-manifest-evaluation",
    "cross-record-integrity-evaluation",
    "candidate-record-and-evidence-production",
]

EXPECTED_PHASE_APPLICABILITY = {
    "governing-input-assessment": True,
    "parsing-and-representation-assessment": True,
    "identity-and-version-assessment": True,
    "resolution-and-resource-closure-assessment": True,
    "schema-definition-assessment": True,
    "schema-evaluation-assessment": True,
    "normative-contract-assessment": True,
    "output-and-evidence-assessment": True,
}

EXPECTED_DEPENDENCY_ARTIFACTS = {
    "jsonschema": ("4.26.0", "jsonschema-4.26.0-py3-none-any.whl", 90630, "d489f15263b8d200f8387e64b4c3a75f06629559fb73deb8fdfb525f2dab50ce"),
    "attrs": ("26.1.0", "attrs-26.1.0-py3-none-any.whl", 67548, "c647aa4a12dfbad9333ca4e71fe62ddc36f4e63b2d260a37a8b83d2f043ac309"),
    "jsonschema-specifications": ("2025.9.1", "jsonschema_specifications-2025.9.1-py3-none-any.whl", 18437, "98802fee3a11ee76ecaca44429fda8a41bff98b00a0f2838151b113f210cc6fe"),
    "referencing": ("0.37.0", "referencing-0.37.0-py3-none-any.whl", 26766, "381329a9f99628c9069361716891d34ad94af76e461dcb0335825aecc7692231"),
    "rpds-py": ("2026.6.3", "rpds_py-2026.6.3-cp313-cp313-win_amd64.whl", 219454, "9250a9a0a6fd4648b3f868da8d91a4c52b5811a62df58e753d50ae4454a36f80"),
}


class InvocationError(ValueError):
    """A closed invocation failed before or during dependent processing."""


def _network_guard(event: str, _arguments: tuple[Any, ...]) -> None:
    if event.startswith("socket."):
        raise PermissionError("network access prohibited by CNTX invocation")


def install_network_guard() -> None:
    sys.addaudithook(_network_guard)


def _exact_limits(value: dict[str, Any]) -> ResourceLimits:
    expected = DEFAULT_LIMITS.__dict__
    if value != expected:
        raise InvocationError("resourceLimits must equal the exact accepted initial ceilings")
    return DEFAULT_LIMITS


def _closed_object(value: Any, keys: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        raise InvocationError(f"{label} has unknown or missing members")
    return value


def _nonblank(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InvocationError(f"{label} must be a non-blank string")
    return value


def _digest(value: Any, label: str, length: int) -> str:
    text = _nonblank(value, label)
    if re.fullmatch(rf"[0-9a-f]{{{length}}}", text) is None:
        raise InvocationError(f"{label} must be lowercase hexadecimal length {length}")
    return text


def _validate_subject_records(records: list[Any]) -> None:
    base_keys = {
        "key", "kind", "identity", "version", "revision", "sha256",
        "provenance", "accessibility", "content", "references", "roles",
        "links", "automaticAuthority",
    }
    role_keys = {
        "requester", "producer", "executor", "reviewer", "decisionMaker",
        "acceptor", "finalAuthority", "declaredOverlaps",
    }
    for index, record in enumerate(records):
        if not isinstance(record, dict) or set(record) not in (base_keys, base_keys | {"independence"}):
            raise InvocationError(f"subjectRecords[{index}] has unknown or missing members")
        for field in ("key", "kind", "identity", "version", "revision"):
            _nonblank(record[field], f"subjectRecords[{index}].{field}")
        _digest(record["sha256"], f"subjectRecords[{index}].sha256", 64)
        if not isinstance(record["provenance"], dict):
            raise InvocationError(f"subjectRecords[{index}].provenance must be an object")
        if record["accessibility"] not in {"accessible", "restricted", "inaccessible"}:
            raise InvocationError(f"subjectRecords[{index}].accessibility is unsupported")
        if record["accessibility"] != "accessible" and record["content"] is not None:
            raise InvocationError(f"subjectRecords[{index}] may not copy restricted or inaccessible content")
        if not isinstance(record["references"], list):
            raise InvocationError(f"subjectRecords[{index}].references must be an array")
        for reference in record["references"]:
            if not isinstance(reference, dict) or set(reference) != {"relation", "targetKey", "targetRevision"}:
                raise InvocationError(f"subjectRecords[{index}] reference is malformed")
            for field in ("relation", "targetKey", "targetRevision"):
                _nonblank(reference[field], f"subjectRecords[{index}] reference {field}")
        roles = record["roles"]
        if not isinstance(roles, dict) or not set(roles).issubset(role_keys) or "declaredOverlaps" not in roles:
            raise InvocationError(f"subjectRecords[{index}].roles is malformed")
        if not isinstance(roles["declaredOverlaps"], list) or any(
            not isinstance(item, str) or not item for item in roles["declaredOverlaps"]
        ):
            raise InvocationError(f"subjectRecords[{index}].declaredOverlaps is malformed")
        for role, identity in roles.items():
            if role != "declaredOverlaps":
                _nonblank(identity, f"subjectRecords[{index}] role {role}")
        if not isinstance(record["links"], dict):
            raise InvocationError(f"subjectRecords[{index}].links must be an object")
        for relation, link in record["links"].items():
            _nonblank(relation, f"subjectRecords[{index}] link relation")
            if not isinstance(link, dict) or set(link) != {"targetKey", "targetRevision"}:
                raise InvocationError(f"subjectRecords[{index}] link is malformed")
            _nonblank(link["targetKey"], f"subjectRecords[{index}] link targetKey")
            _nonblank(link["targetRevision"], f"subjectRecords[{index}] link targetRevision")
        if not isinstance(record["automaticAuthority"], bool):
            raise InvocationError(f"subjectRecords[{index}].automaticAuthority must be boolean")
        if "independence" in record:
            independence = _closed_object(
                record["independence"],
                {"required", "declaration", "sourceKey", "sourceRevision"},
                f"subjectRecords[{index}].independence",
            )
            if type(independence["required"]) is not bool or independence["declaration"] not in {"independent", "non-independent"}:
                raise InvocationError(f"subjectRecords[{index}].independence is malformed")
            _nonblank(independence["sourceKey"], f"subjectRecords[{index}] independence sourceKey")
            _nonblank(independence["sourceRevision"], f"subjectRecords[{index}] independence sourceRevision")


def _validate_invocation(value: Any) -> tuple[dict[str, Any], ResourceLimits]:
    if not isinstance(value, dict) or set(value) != INVOCATION_KEYS:
        raise InvocationError("invocation root has unknown or missing members")
    if value["tool"] != {"identity": TOOL_IDENTITY, "version": TOOL_VERSION}:
        raise InvocationError("Tool identity/version mismatch")
    if value["implementation"] != {
        "identity": IMPLEMENTATION_IDENTITY,
        "version": IMPLEMENTATION_VERSION,
    }:
        raise InvocationError("Implementation identity/version mismatch")
    if value["automaticAuthority"] is not False:
        raise InvocationError("automaticAuthority must be exactly false")
    if value["network"] != {"automaticAccess": False, "state": "prohibited"}:
        raise InvocationError("network prohibition is missing or ambiguous")
    invocation_pin = _closed_object(value["invocation"], {"identifier", "revision"}, "invocation")
    _nonblank(invocation_pin["identifier"], "invocation identifier")
    _nonblank(invocation_pin["revision"], "invocation revision")
    for label in ("implementationSource", "validationSubject"):
        pin = _closed_object(value[label], {"repository", "commit", "tree"}, label)
        _nonblank(pin["repository"], f"{label} repository")
        _digest(pin["commit"], f"{label} commit", 40)
        _digest(pin["tree"], f"{label} tree", 40)
    lock_pin = _closed_object(value["dependencyLock"], {"path", "sha256"}, "dependencyLock")
    _nonblank(lock_pin["path"], "dependencyLock path")
    _digest(lock_pin["sha256"], "dependencyLock sha256", 64)
    output = _closed_object(value["output"], {"machinePath", "summaryPath"}, "output")
    _nonblank(output["machinePath"], "machine output path")
    _nonblank(output["summaryPath"], "summary output path")
    for label in (
        "governingContext", "evaluatorContext", "configuration", "environment",
        "executionWindow", "claimBoundary", "retentionAndCleanup",
    ):
        if not isinstance(value[label], dict):
            raise InvocationError(f"{label} must be an exact object")
    for label in (
        "evidenceItems", "reproductionProcedures", "adverseEvidence", "restrictedEvidence",
    ):
        if not isinstance(value[label], list):
            raise InvocationError(f"{label} must be an exact array")
    if not isinstance(value["subjectRecords"], list):
        raise InvocationError("subjectRecords must be an exact array")
    _validate_subject_records(value["subjectRecords"])
    if not isinstance(value["schemas"], list) or not isinstance(value["manifests"], list):
        raise InvocationError("schemas and manifests must be exact arrays")
    if value["expectedInventory"] != {
        "schemaResources": 10,
        "manifests": 10,
        "directManifests": 9,
        "operationBasedManifests": 1,
        "cases": 203,
        "expectedValid": 38,
        "expectedInvalid": 165,
        "rules": 13,
    }:
        raise InvocationError("expectedInventory must equal the accepted closed inventory")
    if value["requestedOperations"] != EXPECTED_OPERATIONS:
        raise InvocationError("requestedOperations must equal the closed Package E slice")
    if value["phaseApplicability"] != EXPECTED_PHASE_APPLICABILITY:
        raise InvocationError("all eight Package E phases must be explicitly applicable")
    if not isinstance(value["adverseEvidence"], list):
        raise InvocationError("adverseEvidence must be an exact array")
    if not isinstance(value["restrictedEvidence"], list):
        raise InvocationError("restrictedEvidence must be an exact array")
    if not isinstance(value["retentionAndCleanup"], dict):
        raise InvocationError("retentionAndCleanup must be an exact object")
    if not isinstance(value["roles"], dict) or set(value["roles"]) != {
        "requester", "executor", "reviewer", "decisionMaker", "acceptor", "finalAuthority"
    }:
        raise InvocationError("attributable role declarations are incomplete")
    for role, identity in value["roles"].items():
        _nonblank(identity, f"role {role}")
    rules = value["rules"]
    expected_rules = {
        (RULE_PREFIX + name, "1.0.0")
        for name in RULE_NAMES
    }
    if not isinstance(rules, list) or any(
        not isinstance(item, dict) or set(item) != {"identity", "version"}
        for item in rules
    ):
        raise InvocationError("Cross-Record Rule declarations are malformed")
    supplied_rules = [(item["identity"], item["version"]) for item in rules]
    if len(supplied_rules) != len(set(supplied_rules)) or set(supplied_rules) != expected_rules:
        raise InvocationError("Cross-Record Rule set is missing, additional, duplicate, or unsupported")
    return value, _exact_limits(value["resourceLimits"])


def _phase(identifier: str, outcome: str, references: list[str] | None = None) -> dict[str, Any]:
    return {"identifier": identifier, "outcome": outcome, "diagnosticReferences": references or []}


def _diagnostic(identifier: str, category: str, phase: str, subject: str, explanation: str) -> Diagnostic:
    return Diagnostic(identifier, category, phase, subject, explanation)


def _write_exclusive(path: Path, data: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(data)
        stream.flush()


def _check_wall(started: float, limits: ResourceLimits) -> None:
    if time.monotonic() - started > limits.wall_seconds:
        raise InvocationError("wall-time ceiling reached")


def _bounded_observation_collections(
    observations: RunObservations,
    invocation: dict[str, Any],
    limits: ResourceLimits,
) -> None:
    diagnostics = [item.to_dict() for item in observations.diagnostics]
    warning_limitations = (
        observations.warnings
        + observations.limitations
        + invocation["adverseEvidence"]
        + invocation["restrictedEvidence"]
    )


def _verify_dependency_lock(path: Path, expected_sha256: str) -> None:
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        raise InvocationError("dependency lock digest mismatch")
    try:
        lock = tomllib.loads(data.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise InvocationError("dependency lock is not strict UTF-8 TOML") from error
    if set(lock) != {
        "format", "runtime_name", "runtime_version", "implementation_identity",
        "implementation_version", "artifact",
    }:
        raise InvocationError("dependency lock root has unknown or missing members")
    if (
        lock["format"] != 1
        or lock["runtime_name"] != "CPython"
        or lock["runtime_version"] != "3.13.14"
        or lock["implementation_identity"] != IMPLEMENTATION_IDENTITY
        or lock["implementation_version"] != IMPLEMENTATION_VERSION
        or not isinstance(lock["artifact"], list)
        or len(lock["artifact"]) != 5
    ):
        raise InvocationError("dependency lock identity, runtime, or inventory mismatch")
    supplied: set[str] = set()
    for artifact in lock["artifact"]:
        if not isinstance(artifact, dict) or set(artifact) != {
            "name", "version", "filename", "python_tag", "abi_tag", "platform_tag",
            "size", "sha256", "origin",
        }:
            raise InvocationError("dependency artifact has unknown or missing members")
        name = artifact["name"]
        if name in supplied or name not in EXPECTED_DEPENDENCY_ARTIFACTS:
            raise InvocationError("dependency artifact is duplicate or unsupported")
        supplied.add(name)
        expected = EXPECTED_DEPENDENCY_ARTIFACTS[name]
        if (artifact["version"], artifact["filename"], artifact["size"], artifact["sha256"]) != expected:
            raise InvocationError(f"dependency artifact pin mismatch for {name}")
        if not isinstance(artifact["origin"], str) or not artifact["origin"].startswith("https://files.pythonhosted.org/"):
            raise InvocationError(f"dependency artifact origin mismatch for {name}")
    if supplied != set(EXPECTED_DEPENDENCY_ARTIFACTS):
        raise InvocationError("dependency artifact set is incomplete")


def _verify_runtime_and_installed_dependencies() -> None:
    if platform.python_implementation() != "CPython" or platform.python_version() != "3.13.14":
        raise InvocationError("runtime must be exact CPython 3.13.14")
    for name, expected in EXPECTED_DEPENDENCY_ARTIFACTS.items():
        try:
            actual = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError as error:
            raise InvocationError(f"required installed dependency missing: {name}") from error
        if actual != expected[0]:
            raise InvocationError(f"installed dependency version mismatch for {name}")
    require_at_most("diagnostics", len(diagnostics), limits.diagnostics)
    require_at_most(
        "diagnostic bytes",
        len(json.dumps(diagnostics, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")),
        limits.diagnostic_bytes,
    )
    require_at_most(
        "warnings and limitations",
        len(warning_limitations),
        limits.warnings_and_limitations,
    )
    require_at_most(
        "warning and limitation bytes",
        len(json.dumps(warning_limitations, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")),
        limits.warnings_and_limitations_bytes,
    )


def run_candidate(input_root: Path, output_root: Path, invocation_relative: str) -> dict[str, Any]:
    started = time.monotonic()
    install_network_guard()
    invocation_path = resolve_beneath(input_root, invocation_relative, must_exist=True)
    invocation_value = load_strict(invocation_path)
    invocation, limits = _validate_invocation(invocation_value)
    _verify_runtime_and_installed_dependencies()
    lock_path = resolve_beneath(input_root, invocation["dependencyLock"]["path"], must_exist=True)
    _verify_dependency_lock(lock_path, invocation["dependencyLock"]["sha256"])
    input_bytes = invocation_path.stat().st_size
    for declaration in invocation["schemas"] + invocation["manifests"]:
        if isinstance(declaration, dict) and isinstance(declaration.get("path"), str):
            declared_path = resolve_beneath(input_root, declaration["path"], must_exist=True)
            input_bytes += declared_path.stat().st_size
    require_at_most("total caller-supplied JSON bytes", input_bytes, limits.total_json_bytes)
    observations = RunObservations()
    observations.limitations.extend([
        {
            "identifier": "L-runtime-hard-limits",
            "statement": "Process memory, CPU time, handles, process count, and thread count require outer-environment evidence; stronger enforcement remains unverifiable until Gate E3.",
        },
        {
            "identifier": "L-network-boundary",
            "statement": "The Python audit hook rejects Python socket events; operating-system network isolation remains separately evidenced at Gate E3.",
        },
    ])

    observations.phases.append(_phase("governing-input-assessment", "satisfied"))
    resources = None
    cases = []
    inventory: dict[str, int] = {}
    try:
        resources = load_resource_set(invocation["schemas"], input_root, limits)
        cases, inventory = load_and_construct(invocation["manifests"], input_root, limits)
        observations.phases.append(_phase("parsing-and-representation-assessment", "satisfied"))
        observations.phases.append(_phase("identity-and-version-assessment", "satisfied"))
        observations.phases.append(_phase("resolution-and-resource-closure-assessment", "satisfied"))
        resources.check_schemas()
        observations.phases.append(_phase("schema-definition-assessment", "satisfied"))
    except Exception as error:
        diagnostic = _diagnostic(
            "D-resource-or-manifest-001", "processing-failure",
            "parsing-and-representation-assessment", "closed-input-set", str(error),
        )
        observations.diagnostics.append(diagnostic)
        observations.phases.extend([
            _phase("parsing-and-representation-assessment", "not-satisfied", [diagnostic.identifier]),
            _phase("identity-and-version-assessment", "not-evaluated"),
            _phase("resolution-and-resource-closure-assessment", "not-evaluated"),
            _phase("schema-definition-assessment", "not-evaluated"),
        ])
        observations.blocked_conditions.append({"phase": "schema-evaluation-assessment", "reason": str(error)})

    if resources is None:
        observations.phases.append(_phase("schema-evaluation-assessment", "not-evaluated"))
    else:
        evaluation_blocked = False
        for case in cases:
            _check_wall(started, limits)
            if case.construction_error is not None or case.instance is None:
                diagnostic = _diagnostic(
                    f"D-case-construction-{len(observations.diagnostics)+1:04d}",
                    "case-construction-failure", "schema-evaluation-assessment",
                    f"{case.manifest_key}:{case.case_key}", case.construction_error or "construction unavailable",
                )
                observations.diagnostics.append(diagnostic)
                observations.cases.append(CaseObservation(
                    case.manifest_key, case.case_key, case.supplied_order,
                    case.construction_form, "not-satisfied", case.schema_identity,
                    case.expected_validity, None, "not-evaluated", (diagnostic,),
                ))
                evaluation_blocked = True
                continue
            try:
                actual, messages = resources.evaluate(case.schema_identity, case.instance)
                diagnostics = tuple(
                    _diagnostic(
                        f"D-schema-{len(observations.diagnostics)+index+1:04d}",
                        "assertion-failure", "schema-evaluation-assessment",
                        f"{case.manifest_key}:{case.case_key}", message,
                    )
                    for index, message in enumerate(messages)
                )
                observations.diagnostics.extend(diagnostics)
                comparison = "matched" if actual == case.expected_validity else "mismatched"
                observations.cases.append(CaseObservation(
                    case.manifest_key, case.case_key, case.supplied_order,
                    case.construction_form, "satisfied", case.schema_identity,
                    case.expected_validity, actual, comparison, diagnostics,
                ))
            except Exception as error:
                diagnostic = _diagnostic(
                    f"D-evaluation-{len(observations.diagnostics)+1:04d}",
                    "processing-failure", "schema-evaluation-assessment",
                    f"{case.manifest_key}:{case.case_key}", str(error),
                )
                observations.diagnostics.append(diagnostic)
                observations.cases.append(CaseObservation(
                    case.manifest_key, case.case_key, case.supplied_order,
                    case.construction_form, "unverifiable", case.schema_identity,
                    case.expected_validity, None, "unverifiable", (diagnostic,),
                ))
                evaluation_blocked = True
        observations.phases.append(_phase(
            "schema-evaluation-assessment",
            "not-satisfied" if evaluation_blocked else "satisfied",
        ))

    try:
        observations.rules = evaluate_rules(invocation["subjectRecords"], limits)
        observations.diagnostics.extend(
            diagnostic for result in observations.rules for diagnostic in result.diagnostics
        )
        observations.phases.append(_phase("normative-contract-assessment", "satisfied"))
    except Exception as error:
        diagnostic = _diagnostic(
            "D-integrity-001", "cross-record-integrity-failure",
            "normative-contract-assessment", "supplied-record-set", str(error),
        )
        observations.diagnostics.append(diagnostic)
        observations.rules = [
            RuleObservation(RULE_PREFIX + name, "1.0.0", (), True, "not-evaluated")
            for name in RULE_NAMES
        ]
        observations.phases.append(_phase("normative-contract-assessment", "not-satisfied", [diagnostic.identifier]))

    _check_wall(started, limits)
    _bounded_observation_collections(observations, invocation, limits)
    observations.phases.append(_phase("output-and-evidence-assessment", "satisfied"))
    validation = validation_record(invocation, observations)
    integrity = integrity_record(invocation, observations)
    case_values = [item.to_dict() for item in sorted(
        observations.cases,
        key=lambda item: (item.schema_identity, item.manifest_key, item.supplied_order, item.case_key),
    )]
    provisional = {
        "validationExecutionRecord": validation,
        "caseObservations": case_values,
        "inventoryObservations": inventory,
        "integrityEvaluationRecord": integrity,
    }
    references = []
    for key, value in provisional.items():
        digest = hashlib.sha256(json_bytes(value, limits)).hexdigest()
        references.append({"reference": key, "sha256": digest, "provenance": "same invocation"})
    evidence = evidence_package(invocation, observations, references)
    output = {
        "invocation": invocation["invocation"],
        "contextPins": context_pins(invocation),
        **provisional,
        "validationEvidenceReproductionPackage": evidence,
        "diagnostics": [item.to_dict() for item in sorted(
            observations.diagnostics,
            key=lambda item: (item.phase, item.subject_key, item.category, item.identifier),
        )],
        "warnings": observations.warnings,
        "limitations": observations.limitations,
        "adverseEvidence": invocation["adverseEvidence"],
        "restrictedEvidence": invocation["restrictedEvidence"],
        "blockedConditions": observations.blocked_conditions,
        "nonExecution": observations.non_execution,
        "retentionAndCleanup": invocation["retentionAndCleanup"],
        "claimBoundary": invocation["claimBoundary"],
        "automaticAuthority": False,
    }
    machine = json_bytes(output, limits)
    summary = human_summary(output).encode("utf-8")
    require_at_most("human summary bytes", len(summary), limits.individual_output_bytes)
    require_at_most("total retained output", len(machine) + len(summary), limits.retained_output_bytes)
    machine_path = resolve_beneath(output_root, invocation["output"]["machinePath"], must_exist=False)
    summary_path = resolve_beneath(output_root, invocation["output"]["summaryPath"], must_exist=False)
    if machine_path == summary_path:
        raise InvocationError("machine and summary output paths must differ")
    if machine_path.exists() or summary_path.exists():
        raise InvocationError("output target already exists")
    if not machine_path.parent.is_dir() or not summary_path.parent.is_dir():
        raise InvocationError("output parent must already exist beneath the approved root")
    written: list[Path] = []
    try:
        _write_exclusive(machine_path, machine)
        written.append(machine_path)
        _write_exclusive(summary_path, summary)
        written.append(summary_path)
        _check_wall(started, limits)
    except Exception:
        for path in reversed(written):
            path.unlink(missing_ok=True)
        raise
    return {
        "machineOutput": invocation["output"]["machinePath"],
        "summaryOutput": invocation["output"]["summaryPath"],
        "machineSha256": hashlib.sha256(machine).hexdigest(),
        "summarySha256": hashlib.sha256(summary).hexdigest(),
        "operationalState": "completed-with-separate-observations",
        "automaticAuthority": False,
    }
