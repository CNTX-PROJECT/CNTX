from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from dataclasses import asdict
from pathlib import Path

from cntx_validation_integrity_slice import (
    IMPLEMENTATION_IDENTITY,
    IMPLEMENTATION_VERSION,
    TOOL_IDENTITY,
    TOOL_VERSION,
)
from cntx_validation_integrity_slice.integrity import RULE_NAMES, RULE_PREFIX
from cntx_validation_integrity_slice.limits import DEFAULT_LIMITS
from cntx_validation_integrity_slice.manifests import EXPECTED_MANIFEST_PATHS
from cntx_validation_integrity_slice.presentation import human_summary, json_bytes
from cntx_validation_integrity_slice.resources import SCHEMA_IDENTITIES
from cntx_validation_integrity_slice.runner import (
    EXPECTED_OPERATIONS,
    EXPECTED_PHASE_APPLICABILITY,
    run_candidate,
)


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _prepare_input(repository_root: Path, input_root: Path) -> dict:
    schemas = []
    manifests = []
    for slug, identity in sorted(SCHEMA_IDENTITIES.items()):
        schema_relative = f"schemas/{slug}/1.0.0/schema.json"
        manifest_relative = EXPECTED_MANIFEST_PATHS[identity]
        for relative in (schema_relative, manifest_relative):
            target = input_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repository_root / relative, target)
        schemas.append({
            "identity": identity,
            "version": "1.0.0",
            "path": schema_relative,
            "sha256": _digest(input_root / schema_relative),
        })
        manifests.append({
            "key": f"manifest:{slug}",
            "schemaIdentity": identity,
            "version": "1.0.0",
            "path": manifest_relative,
            "sha256": _digest(input_root / manifest_relative),
            "construction": "operation-based" if slug == "state-snapshot" else "direct",
        })
    lock = repository_root / "tools/minimal-validation-integrity-slice/requirements-1.0.1.lock"
    copied_lock = input_root / "dependency/requirements.lock"
    copied_lock.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(lock, copied_lock)
    return {
        "invocation": {"identifier": "synthetic-reproduction", "revision": "fixture-1"},
        "tool": {"identity": TOOL_IDENTITY, "version": TOOL_VERSION},
        "implementation": {"identity": IMPLEMENTATION_IDENTITY, "version": IMPLEMENTATION_VERSION},
        "implementationSource": {"repository": "CNTX-PROJECT/CNTX", "commit": "a" * 40, "tree": "b" * 40},
        "validationSubject": {"repository": "CNTX-PROJECT/CNTX", "commit": "c" * 40, "tree": "d" * 40},
        "governingContext": {"status": "synthetic-test-fixture", "frozen": True},
        "evaluatorContext": {"status": "synthetic-test-fixture", "offlineFirst": True},
        "dependencyLock": {"path": "dependency/requirements.lock", "sha256": _digest(copied_lock)},
        "configuration": {"dialect": "draft-2020-12", "formatAssertion": False, "repair": False},
        "environment": {"runtime": "CPython", "version": "3.13.14", "status": "synthetic-test-fixture"},
        "schemas": schemas,
        "manifests": manifests,
        "rules": [
            {"identity": RULE_PREFIX + name, "version": "1.0.0"}
            for name in reversed(RULE_NAMES)
        ],
        "subjectRecords": [],
        "resourceLimits": asdict(DEFAULT_LIMITS),
        "output": {"machinePath": "result.json", "summaryPath": "summary.txt"},
        "executionWindow": {"start": "caller-supplied-fixture", "end": "caller-supplied-fixture"},
        "evidenceItems": [],
        "reproductionProcedures": [{"step": "execute same frozen synthetic fixture twice"}],
        "expectedInventory": {
            "schemaResources": 10, "manifests": 10, "directManifests": 9,
            "operationBasedManifests": 1, "cases": 203,
            "expectedValid": 38, "expectedInvalid": 165, "rules": 13,
        },
        "requestedOperations": EXPECTED_OPERATIONS,
        "phaseApplicability": EXPECTED_PHASE_APPLICABILITY,
        "adverseEvidence": [],
        "restrictedEvidence": [],
        "retentionAndCleanup": {"retention": "temporary", "cleanup": "TemporaryDirectory"},
        "claimBoundary": {"claim": "synthetic bounded implementation test only"},
        "roles": {
            "requester": "synthetic-requester", "executor": "synthetic-executor",
            "reviewer": "synthetic-reviewer", "decisionMaker": "synthetic-decision-maker",
            "acceptor": "synthetic-acceptor", "finalAuthority": "synthetic-final-authority",
        },
        "network": {"automaticAccess": False, "state": "prohibited"},
        "automaticAuthority": False,
    }


class DeterministicPresentationTests(unittest.TestCase):
    def test_json_serialization_is_byte_stable_for_same_value(self) -> None:
        first = {"z": [2, 1], "a": {"b": True}, "automaticAuthority": False}
        second = {"automaticAuthority": False, "a": {"b": True}, "z": [2, 1]}
        self.assertEqual(json_bytes(first), json_bytes(second))

    def test_summary_preserves_separate_counts_and_non_authority(self) -> None:
        output = {
            "caseObservations": [{"comparison": "matched"}, {"comparison": "mismatched"}],
            "integrityEvaluationRecord": {"ruleResults": [
                {"outcome": "satisfied"}, {"outcome": "not-evaluated"},
            ]},
            "validationExecutionRecord": {"phaseResults": [{"outcome": "satisfied"}]},
            "diagnostics": [{"identifier": "D-1"}],
            "warnings": [],
            "limitations": [{"identifier": "L-1"}],
            "adverseEvidence": [],
            "restrictedEvidence": [],
            "blockedConditions": [],
            "nonExecution": [],
        }
        summary = human_summary(output)
        self.assertIn("matched=1", summary)
        self.assertIn("mismatched=1", summary)
        self.assertIn("not-evaluated=1", summary)
        self.assertIn("automaticAuthority=false", summary)
        self.assertNotIn("PASS", summary)

    def test_two_full_frozen_runs_have_equal_declared_output(self) -> None:
        repository_root = Path(__file__).resolve().parents[3]
        with tempfile.TemporaryDirectory() as directory:
            temporary_root = Path(directory)
            input_root = temporary_root / "input"
            first_output = temporary_root / "output-one"
            second_output = temporary_root / "output-two"
            input_root.mkdir()
            first_output.mkdir()
            second_output.mkdir()
            invocation = _prepare_input(repository_root, input_root)
            (input_root / "invocation.json").write_bytes(json_bytes(invocation))
            first = run_candidate(input_root, first_output, "invocation.json")
            second = run_candidate(input_root, second_output, "invocation.json")
            self.assertEqual(first["machineSha256"], second["machineSha256"])
            self.assertEqual(first["summarySha256"], second["summarySha256"])
            self.assertEqual(
                (first_output / "result.json").read_bytes(),
                (second_output / "result.json").read_bytes(),
            )
            result = json.loads((first_output / "result.json").read_text(encoding="utf-8"))
            self.assertEqual(result["inventoryObservations"]["cases"], 203)
            self.assertEqual(len(result["caseObservations"]), 203)
            self.assertEqual(len(result["integrityEvaluationRecord"]["ruleResults"]), 13)
            self.assertIs(result["automaticAuthority"], False)


if __name__ == "__main__":
    unittest.main()
