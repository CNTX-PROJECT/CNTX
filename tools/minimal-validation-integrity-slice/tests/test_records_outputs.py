from __future__ import annotations

import unittest

from cntx_validation_integrity_slice.models import RunObservations
from cntx_validation_integrity_slice.records import integrity_record, validation_record


def invocation() -> dict:
    return {
        "invocation": {"identifier": "inv-1", "revision": "r1"},
        "validationSubject": {"commit": "a" * 40, "tree": "b" * 40},
        "governingContext": {"frozen": True},
        "evaluatorContext": {"network": "prohibited"},
        "executionWindow": {"state": "not-executed-test-fixture"},
        "claimBoundary": {"claimed": ["bounded structural observation"]},
        "roles": {
            "executor": "executor", "reviewer": "reviewer",
            "decisionMaker": "owner", "finalAuthority": "owner",
        },
        "subjectRecords": [],
        "rules": [],
    }


class RecordOutputTests(unittest.TestCase):
    def test_validation_root_is_closed_ten_property_shape(self) -> None:
        value = validation_record(invocation(), RunObservations())
        self.assertEqual(set(value), {
            "record", "subject", "governingContext", "evaluatorContext",
            "executionWindow", "phaseResults", "diagnostics", "limitations",
            "claimBoundary", "authorityBoundary",
        })
        self.assertIs(value["authorityBoundary"]["automaticAuthority"], False)

    def test_integrity_root_is_closed_nine_property_shape(self) -> None:
        value = integrity_record(invocation(), RunObservations())
        self.assertEqual(set(value), {
            "evaluation", "governingContext", "suppliedRecords",
            "ruleDefinitions", "ruleResults", "diagnostics", "limitations",
            "claimBoundary", "authorityBoundary",
        })


if __name__ == "__main__":
    unittest.main()
