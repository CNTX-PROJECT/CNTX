"""Thirteen bounded cross-record integrity-rule evaluations."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from typing import Any

from .limits import DEFAULT_LIMITS, ResourceLimits, require_at_most
from .models import Diagnostic, RuleObservation

RULE_PREFIX = "https://github.com/CNTX-PROJECT/CNTX/rules/cross-record/"
RULE_NAMES = (
    "supplied-record-exists",
    "identity-version-revision-complete",
    "record-key-unique",
    "identity-revision-content-consistent",
    "reference-resolves-exactly-once",
    "task-context-execution-chain",
    "validation-record-subject-link",
    "evidence-package-execution-link",
    "role-overlap-visible",
    "review-independence-declared",
    "self-review-prohibited",
    "self-acceptance-prohibited",
    "automatic-authority-false",
)


def _diag(rule: str, subject: str, explanation: str) -> Diagnostic:
    token = hashlib.sha256(f"{rule}|{subject}|{explanation}".encode()).hexdigest()[:12]
    return Diagnostic(
        f"D-{token}", "cross-record-integrity-failure", "integrity-rules",
        subject, explanation,
    )


def _result(name: str, subjects: list[str], outcome: str, explanation: str | None = None) -> RuleObservation:
    diagnostics = () if explanation is None else (_diag(name, ",".join(subjects) or "record-set", explanation),)
    return RuleObservation(RULE_PREFIX + name, "1.0.0", tuple(subjects), True, outcome, (), diagnostics)


def _not_evaluated(name: str) -> RuleObservation:
    return RuleObservation(RULE_PREFIX + name, "1.0.0", (), False, "not-evaluated")


def _record_keys(records: list[dict[str, Any]]) -> list[str]:
    return [str(record.get("key", "<missing>")) for record in records]


def evaluate_rules(
    records: list[dict[str, Any]],
    limits: ResourceLimits = DEFAULT_LIMITS,
) -> list[RuleObservation]:
    require_at_most("caller-supplied subject records", len(records), limits.subject_records)
    if not records:
        return [_not_evaluated(name) for name in RULE_NAMES]
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("supplied record is not an object")

    keys = _record_keys(records)
    by_key: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record, key in zip(records, keys):
        by_key[key].append(record)
    results: list[RuleObservation] = []

    missing_content = [
        key for key, record in zip(keys, records)
        if record.get("content") is None and record.get("accessibility") not in {"restricted", "inaccessible"}
    ]
    unavailable_content = [
        key for key, record in zip(keys, records)
        if record.get("content") is None and record.get("accessibility") in {"restricted", "inaccessible"}
    ]
    if missing_content:
        results.append(_result(RULE_NAMES[0], missing_content, "not-satisfied", "required supplied content is missing"))
    elif unavailable_content:
        results.append(_result(RULE_NAMES[0], unavailable_content, "unverifiable", "required supplied content is restricted or inaccessible"))
    else:
        results.append(_result(RULE_NAMES[0], keys, "satisfied"))

    required = ("key", "kind", "identity", "version", "revision", "sha256", "provenance", "accessibility", "roles")
    incomplete = [key for key, record in zip(keys, records) if any(not record.get(field) for field in required)]
    results.append(_result(RULE_NAMES[1], incomplete or keys, "not-satisfied", "identity/version/revision pin is incomplete") if incomplete else _result(RULE_NAMES[1], keys, "satisfied"))

    duplicates = sorted(key for key, items in by_key.items() if len(items) != 1)
    results.append(_result(RULE_NAMES[2], duplicates or keys, "not-satisfied", "record key is not unique") if duplicates else _result(RULE_NAMES[2], keys, "satisfied"))

    coordinates: dict[tuple[Any, Any], set[str]] = defaultdict(set)
    for record in records:
        compared = {
            "content": record.get("content"),
            "sha256": record.get("sha256"),
            "provenance": record.get("provenance"),
        }
        serialized = json.dumps(compared, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        coordinates[(record.get("identity"), record.get("revision"))].add(hashlib.sha256(serialized.encode()).hexdigest())
    conflicts = [f"{identity}@{revision}" for (identity, revision), digests in coordinates.items() if len(digests) > 1]
    results.append(_result(RULE_NAMES[3], conflicts or keys, "not-satisfied", "same identity/revision has conflicting content") if conflicts else _result(RULE_NAMES[3], keys, "satisfied"))

    dangling: list[str] = []
    ambiguous: list[str] = []
    unavailable: list[str] = []
    for record in records:
        for reference in record.get("references", []):
            target = reference.get("targetKey") if isinstance(reference, dict) else None
            revision = reference.get("targetRevision") if isinstance(reference, dict) else None
            matches = [
                item for item in by_key.get(str(target), [])
                if item.get("revision") == revision
            ]
            count = len(matches)
            if count == 0:
                dangling.append(f"{record.get('key')}->{target}@{revision}")
            elif count > 1:
                ambiguous.append(f"{record.get('key')}->{target}@{revision}")
            elif matches[0].get("accessibility") in {"restricted", "inaccessible"}:
                unavailable.append(f"{record.get('key')}->{target}@{revision}")
    bad_refs = dangling + ambiguous
    if bad_refs:
        results.append(_result(RULE_NAMES[4], bad_refs, "not-satisfied", "reference does not resolve exactly once at the required revision"))
    elif unavailable:
        results.append(_result(RULE_NAMES[4], unavailable, "unverifiable", "resolved reference is restricted or inaccessible"))
    else:
        results.append(_result(RULE_NAMES[4], keys, "satisfied"))

    def linked(kind: str, fields: tuple[str, ...], rule: str) -> RuleObservation:
        applicable = [record for record in records if record.get("kind") == kind]
        if not applicable:
            return _not_evaluated(rule)
        bad = []
        for record in applicable:
            links = record.get("links", {})
            def resolves(field: str) -> bool:
                link = links.get(field) if isinstance(links, dict) else None
                if not isinstance(link, dict) or set(link) != {"targetKey", "targetRevision"}:
                    return False
                return len([
                    item for item in by_key.get(str(link["targetKey"]), [])
                    if item.get("revision") == link["targetRevision"]
                ]) == 1
            if any(not resolves(field) for field in fields):
                bad.append(str(record.get("key")))
        return _result(rule, bad or [str(item.get("key")) for item in applicable], "not-satisfied", "required chain link is missing or ambiguous") if bad else _result(rule, [str(item.get("key")) for item in applicable], "satisfied")

    results.append(linked("execution-result", ("taskContract", "contextPacket"), RULE_NAMES[5]))
    results.append(linked("validation-execution-record", ("subject",), RULE_NAMES[6]))
    results.append(linked("validation-evidence-reproduction-package", ("executionRecord",), RULE_NAMES[7]))

    role_records = [record for record in records if isinstance(record.get("roles"), dict)]
    if not role_records:
        results.append(_not_evaluated(RULE_NAMES[8]))
    else:
        bad = []
        for record in role_records:
            roles = record["roles"]
            identities = [value for key, value in roles.items() if key != "declaredOverlaps" and isinstance(value, str)]
            actual = sorted(identity for identity, count in Counter(identities).items() if count > 1)
            declared = sorted(roles.get("declaredOverlaps", []))
            if actual != declared:
                bad.append(str(record.get("key")))
        results.append(_result(RULE_NAMES[8], bad or [str(item.get("key")) for item in role_records], "not-satisfied", "role overlap declaration does not match visible overlap") if bad else _result(RULE_NAMES[8], [str(item.get("key")) for item in role_records], "satisfied"))

    reviews = [record for record in records if record.get("kind") == "review-record"]
    if not reviews:
        results.extend((_not_evaluated(RULE_NAMES[9]), _not_evaluated(RULE_NAMES[10])))
    else:
        undeclared = []
        self_reviews = []
        review_unknown = []
        for item in reviews:
            independence = item.get("independence")
            if not isinstance(independence, dict) or set(independence) != {"required", "declaration", "sourceKey", "sourceRevision"} or independence.get("declaration") not in {"independent", "non-independent"}:
                undeclared.append(str(item.get("key")))
                review_unknown.append(str(item.get("key")))
            elif independence.get("required") is True and item.get("roles", {}).get("reviewer") == item.get("roles", {}).get("executor"):
                self_reviews.append(str(item.get("key")))
        results.append(_result(RULE_NAMES[9], undeclared or [str(item.get("key")) for item in reviews], "not-satisfied", "review independence is not declared") if undeclared else _result(RULE_NAMES[9], [str(item.get("key")) for item in reviews], "satisfied"))
        if self_reviews:
            results.append(_result(RULE_NAMES[10], self_reviews, "not-satisfied", "required independent self-review is prohibited"))
        elif review_unknown:
            results.append(_result(RULE_NAMES[10], review_unknown, "unverifiable", "independent-review applicability is undeclared"))
        else:
            results.append(_result(RULE_NAMES[10], [str(item.get("key")) for item in reviews], "satisfied"))

    decisions = [record for record in records if record.get("kind") == "decision-record"]
    if not decisions:
        results.append(_not_evaluated(RULE_NAMES[11]))
    else:
        bad = [
            str(item.get("key")) for item in decisions
            if item.get("roles", {}).get("acceptor") in {
                item.get("roles", {}).get("producer"),
                item.get("roles", {}).get("executor"),
                item.get("roles", {}).get("reviewer"),
            }
        ]
        results.append(_result(RULE_NAMES[11], bad or [str(item.get("key")) for item in decisions], "not-satisfied", "self-acceptance is prohibited") if bad else _result(RULE_NAMES[11], [str(item.get("key")) for item in decisions], "satisfied"))

    authority_bad = [str(item.get("key")) for item in records if item.get("automaticAuthority") is not False]
    results.append(_result(RULE_NAMES[12], authority_bad or keys, "not-satisfied", "automaticAuthority must be exactly false") if authority_bad else _result(RULE_NAMES[12], keys, "satisfied"))

    require_at_most("integrity rules", len(results), limits.rules)
    if len(results) != limits.rules:
        raise ValueError("exact thirteen-rule evaluation was not produced")
    return sorted(results, key=lambda item: (item.rule_identity, item.subject_keys))
