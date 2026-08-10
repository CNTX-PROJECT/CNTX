from __future__ import annotations

import copy
import unittest

from cntx_validation_integrity_slice.integrity import RULE_NAMES, evaluate_rules


def record(key: str, kind: str = "task-contract") -> dict:
    return {
        "key": key,
        "kind": kind,
        "identity": f"identity:{key}",
        "version": "1.0.0",
        "revision": "r1",
        "sha256": "a" * 64,
        "provenance": {"source": "synthetic-test"},
        "accessibility": "accessible",
        "content": {"key": key},
        "references": [],
        "roles": {"producer": "p", "executor": "e", "declaredOverlaps": []},
        "links": {},
        "automaticAuthority": False,
    }


class IntegrityTests(unittest.TestCase):
    def test_empty_set_retains_thirteen_not_evaluated_results(self) -> None:
        results = evaluate_rules([])
        self.assertEqual(len(results), 13)
        self.assertEqual({item.outcome for item in results}, {"not-evaluated"})

    def test_every_rule_identity_is_present_once(self) -> None:
        results = evaluate_rules([record("one")])
        self.assertEqual(len(results), len(RULE_NAMES))
        self.assertEqual(len({item.rule_identity for item in results}), len(RULE_NAMES))

    def test_dangling_and_duplicate_references_are_visible(self) -> None:
        first = record("same")
        second = record("same")
        first["references"] = [{"targetKey": "missing"}]
        results = evaluate_rules([first, second])
        by_name = {item.rule_identity.rsplit("/", 1)[-1]: item for item in results}
        self.assertEqual(by_name["record-key-unique"].outcome, "not-satisfied")
        self.assertEqual(by_name["reference-resolves-exactly-once"].outcome, "not-satisfied")

    def test_conflicting_same_identity_revision_is_visible(self) -> None:
        first = record("one")
        second = copy.deepcopy(first)
        second["key"] = "two"
        second["content"] = {"different": True}
        results = evaluate_rules([first, second])
        target = next(item for item in results if item.rule_identity.endswith("identity-revision-content-consistent"))
        self.assertEqual(target.outcome, "not-satisfied")

    def test_role_independence_and_authority_adversaries(self) -> None:
        review = record("review", "review-record")
        review["roles"] = {"reviewer": "same", "executor": "same", "declaredOverlaps": ["same"]}
        review["independence"] = {
            "required": True,
            "declaration": "non-independent",
            "sourceKey": "review-policy",
            "sourceRevision": "r1",
        }
        review["automaticAuthority"] = True
        decision = record("decision", "decision-record")
        decision["roles"] = {"acceptor": "same", "producer": "same", "executor": "other", "declaredOverlaps": ["same"]}
        results = evaluate_rules([review, decision])
        by_name = {item.rule_identity.rsplit("/", 1)[-1]: item for item in results}
        self.assertEqual(by_name["self-review-prohibited"].outcome, "not-satisfied")
        self.assertEqual(by_name["self-acceptance-prohibited"].outcome, "not-satisfied")
        self.assertEqual(by_name["automatic-authority-false"].outcome, "not-satisfied")

    def test_restricted_target_remains_unverifiable_not_missing(self) -> None:
        source = record("source")
        target = record("target")
        target["content"] = None
        target["accessibility"] = "restricted"
        source["references"] = [{"targetKey": "target", "targetRevision": "r1"}]
        results = evaluate_rules([source, target])
        by_name = {item.rule_identity.rsplit("/", 1)[-1]: item for item in results}
        self.assertEqual(by_name["supplied-record-exists"].outcome, "unverifiable")
        self.assertEqual(by_name["reference-resolves-exactly-once"].outcome, "unverifiable")

    def test_transparent_non_independent_review_is_not_self_review_when_independence_not_required(self) -> None:
        review = record("review", "review-record")
        review["roles"] = {"reviewer": "same", "executor": "same", "declaredOverlaps": ["same"]}
        review["independence"] = {
            "required": False,
            "declaration": "non-independent",
            "sourceKey": "review-policy",
            "sourceRevision": "r1",
        }
        results = evaluate_rules([review])
        target = next(item for item in results if item.rule_identity.endswith("self-review-prohibited"))
        self.assertEqual(target.outcome, "satisfied")


if __name__ == "__main__":
    unittest.main()
