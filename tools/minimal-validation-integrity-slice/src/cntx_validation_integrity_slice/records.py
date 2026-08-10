"""Candidate Validation-layer record construction with no authority effect."""

from __future__ import annotations

from typing import Any

from . import IMPLEMENTATION_IDENTITY, IMPLEMENTATION_VERSION, TOOL_IDENTITY, TOOL_VERSION
from .models import RunObservations

PHASES = (
    "governing-input-assessment",
    "parsing-and-representation-assessment",
    "identity-and-version-assessment",
    "resolution-and-resource-closure-assessment",
    "schema-definition-assessment",
    "schema-evaluation-assessment",
    "normative-contract-assessment",
    "output-and-evidence-assessment",
)


def _authority(invocation: dict[str, Any]) -> dict[str, Any]:
    return {
        "producer": invocation["roles"]["executor"],
        "reviewer": invocation["roles"]["reviewer"],
        "decisionMaker": invocation["roles"]["decisionMaker"],
        "finalHumanAuthority": invocation["roles"]["finalAuthority"],
        "automaticAuthority": False,
        "boundary": "Candidate output grants no review, acceptance, certification, release, deployment, or final-human decision.",
    }


def validation_record(invocation: dict[str, Any], observations: RunObservations) -> dict[str, Any]:
    return {
        "record": {
            "definition": "https://github.com/CNTX-PROJECT/CNTX/definitions/validation-execution-record",
            "definitionVersion": "1.0.0",
            "representation": "https://github.com/CNTX-PROJECT/CNTX/bindings/validation-execution-record-json",
            "representationVersion": "1.0.0",
            "identifier": invocation["invocation"]["identifier"] + ":validation-record",
            "revision": invocation["invocation"]["revision"],
            "lifecycle": "candidate",
        },
        "subject": invocation["validationSubject"],
        "governingContext": invocation["governingContext"],
        "evaluatorContext": invocation["evaluatorContext"],
        "executionWindow": invocation["executionWindow"],
        "phaseResults": observations.phases,
        "diagnostics": [item.to_dict() for item in observations.diagnostics],
        "limitations": observations.limitations,
        "claimBoundary": invocation["claimBoundary"],
        "authorityBoundary": _authority(invocation),
    }


def integrity_record(invocation: dict[str, Any], observations: RunObservations) -> dict[str, Any]:
    return {
        "evaluation": {
            "definition": "https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-evaluation-record",
            "definitionVersion": "1.0.0",
            "representation": "https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-evaluation-record-json",
            "representationVersion": "1.0.0",
            "identifier": invocation["invocation"]["identifier"] + ":integrity-record",
            "revision": invocation["invocation"]["revision"],
            "lifecycle": "candidate",
        },
        "governingContext": invocation["governingContext"],
        "suppliedRecords": invocation["subjectRecords"],
        "ruleDefinitions": invocation["rules"],
        "ruleResults": [item.to_dict() for item in observations.rules],
        "diagnostics": [item.to_dict() for item in observations.diagnostics],
        "limitations": observations.limitations,
        "claimBoundary": invocation["claimBoundary"],
        "authorityBoundary": _authority(invocation),
    }


def evidence_package(
    invocation: dict[str, Any],
    observations: RunObservations,
    output_references: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "package": {
            "definition": "https://github.com/CNTX-PROJECT/CNTX/definitions/validation-evidence-reproduction-package",
            "definitionVersion": "1.0.0",
            "representation": "https://github.com/CNTX-PROJECT/CNTX/bindings/validation-evidence-reproduction-package-json",
            "representationVersion": "1.0.0",
            "identifier": invocation["invocation"]["identifier"] + ":evidence-package",
            "revision": invocation["invocation"]["revision"],
            "lifecycle": "candidate",
        },
        "subjects": [invocation["validationSubject"]],
        "governingInputs": {
            "governingContext": invocation["governingContext"],
            "implementationSource": invocation["implementationSource"],
            "schemas": invocation["schemas"],
            "manifests": invocation["manifests"],
            "rules": invocation["rules"],
            "expectedInventory": invocation["expectedInventory"],
            "requestedOperations": invocation["requestedOperations"],
            "phaseApplicability": invocation["phaseApplicability"],
        },
        "evaluatorContext": {
            "evaluator": invocation["evaluatorContext"],
            "dependencyLock": invocation["dependencyLock"],
            "configuration": invocation["configuration"],
            "environment": invocation["environment"],
            "resourceLimits": invocation["resourceLimits"],
            "network": invocation["network"],
        },
        "executionRecords": [{"reference": invocation["invocation"]["identifier"] + ":validation-record"}],
        "evidenceItems": invocation["evidenceItems"],
        "reproductionProcedures": invocation["reproductionProcedures"],
        "outputs": output_references,
        "diagnostics": [item.to_dict() for item in observations.diagnostics],
        "limitations": observations.limitations,
        "claimBoundary": invocation["claimBoundary"],
        "authorityBoundary": _authority(invocation),
    }


def context_pins(invocation: dict[str, Any]) -> dict[str, Any]:
    return {
        "tool": {"identity": TOOL_IDENTITY, "version": TOOL_VERSION},
        "implementation": {"identity": IMPLEMENTATION_IDENTITY, "version": IMPLEMENTATION_VERSION},
        "implementationSource": invocation["implementationSource"],
        "validationSubject": invocation["validationSubject"],
        "dependencyLock": invocation["dependencyLock"],
        "configuration": invocation["configuration"],
        "environment": invocation["environment"],
        "governingContext": invocation["governingContext"],
        "schemas": invocation["schemas"],
        "manifests": invocation["manifests"],
        "rules": invocation["rules"],
        "expectedInventory": invocation["expectedInventory"],
        "requestedOperations": invocation["requestedOperations"],
        "phaseApplicability": invocation["phaseApplicability"],
        "resourceLimits": invocation["resourceLimits"],
        "network": invocation["network"],
        "roles": invocation["roles"],
        "retentionAndCleanup": invocation["retentionAndCleanup"],
    }
