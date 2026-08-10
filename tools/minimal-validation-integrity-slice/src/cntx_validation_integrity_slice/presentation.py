"""Deterministic bounded JSON and non-verdict human presentation."""

from __future__ import annotations

import json
from typing import Any

from .limits import DEFAULT_LIMITS, ResourceLimits, require_at_most


def json_bytes(value: Any, limits: ResourceLimits = DEFAULT_LIMITS) -> bytes:
    data = (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    require_at_most("individual output bytes", len(data), limits.individual_output_bytes)
    return data


def human_summary(output: dict[str, Any]) -> str:
    cases = output["caseObservations"]
    rules = output["integrityEvaluationRecord"]["ruleResults"]
    phases = output["validationExecutionRecord"]["phaseResults"]
    comparisons: dict[str, int] = {}
    for item in cases:
        comparisons[item["comparison"]] = comparisons.get(item["comparison"], 0) + 1
    outcomes: dict[str, int] = {}
    for item in rules:
        outcomes[item["outcome"]] = outcomes.get(item["outcome"], 0) + 1
    phase_outcomes: dict[str, int] = {}
    for item in phases:
        phase_outcomes[item["outcome"]] = phase_outcomes.get(item["outcome"], 0) + 1
    lines = [
        "CNTX Minimal Validation and Integrity Slice — bounded observations",
        f"Cases retained: {len(cases)}",
        "Case comparisons: " + ", ".join(f"{key}={comparisons[key]}" for key in sorted(comparisons)),
        f"Rule observations retained: {len(rules)}",
        "Rule outcomes: " + ", ".join(f"{key}={outcomes[key]}" for key in sorted(outcomes)),
        "Phase outcomes: " + ", ".join(f"{key}={phase_outcomes[key]}" for key in sorted(phase_outcomes)),
        f"Diagnostics retained: {len(output['diagnostics'])}",
        f"Warnings retained: {len(output['warnings'])}",
        f"Limitations retained: {len(output['limitations'])}",
        f"Adverse-evidence items retained: {len(output['adverseEvidence'])}",
        f"Restricted-evidence references retained: {len(output['restrictedEvidence'])}",
        f"Blocked conditions retained: {len(output['blockedConditions'])}",
        f"Non-execution items retained: {len(output['nonExecution'])}",
        "No aggregate pass/fail, conformance, approval, certification, release, deployment, or authority result is produced.",
        "automaticAuthority=false",
    ]
    return "\n".join(lines) + "\n"
