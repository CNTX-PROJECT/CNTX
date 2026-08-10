"""Closed internal observation models for the candidate implementation."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

Outcome = Literal["satisfied", "not-satisfied", "unverifiable", "not-evaluated"]


@dataclass(frozen=True)
class Diagnostic:
    identifier: str
    category: str
    phase: str
    subject_key: str
    explanation: str
    related_references: tuple[str, ...] = ()
    disclosure: str = "public-safe"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CaseObservation:
    manifest_key: str
    case_key: str
    supplied_order: int
    construction_form: str
    construction_outcome: Outcome
    schema_identity: str
    expected_validity: bool
    actual_validity: bool | None
    comparison: str
    diagnostics: tuple[Diagnostic, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["diagnostics"] = [item.to_dict() for item in self.diagnostics]
        return value


@dataclass(frozen=True)
class RuleObservation:
    rule_identity: str
    rule_version: str
    subject_keys: tuple[str, ...]
    applicable: bool
    outcome: Outcome
    evidence_references: tuple[str, ...] = ()
    diagnostics: tuple[Diagnostic, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["diagnostics"] = [item.to_dict() for item in self.diagnostics]
        return value


@dataclass
class RunObservations:
    phases: list[dict[str, Any]] = field(default_factory=list)
    cases: list[CaseObservation] = field(default_factory=list)
    rules: list[RuleObservation] = field(default_factory=list)
    diagnostics: list[Diagnostic] = field(default_factory=list)
    warnings: list[dict[str, Any]] = field(default_factory=list)
    limitations: list[dict[str, Any]] = field(default_factory=list)
    blocked_conditions: list[dict[str, Any]] = field(default_factory=list)
    non_execution: list[dict[str, Any]] = field(default_factory=list)
