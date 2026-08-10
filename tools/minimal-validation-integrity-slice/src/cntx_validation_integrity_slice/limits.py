"""Exact initial Gate E2 resource ceilings and bounded counters."""

from __future__ import annotations

from dataclasses import dataclass


class LimitExceeded(ValueError):
    """Raised when an affected operation reaches a declared ceiling."""


@dataclass(frozen=True)
class ResourceLimits:
    schema_resources: int = 10
    manifests: int = 10
    cases: int = 203
    operations_per_case: int = 64
    operations_total: int = 1_024
    rules: int = 13
    subject_records: int = 256
    individual_json_bytes: int = 4 * 1024 * 1024
    total_json_bytes: int = 64 * 1024 * 1024
    json_depth: int = 128
    json_nodes: int = 1_000_000
    ref_occurrences: int = 4_096
    graph_nodes: int = 10
    graph_edges: int = 4_096
    expansion_depth: int = 64
    expansions: int = 8_192
    rule_results: int = 4_096
    diagnostics: int = 10_000
    diagnostic_bytes: int = 16 * 1024 * 1024
    warnings_and_limitations: int = 10_000
    warnings_and_limitations_bytes: int = 16 * 1024 * 1024
    individual_output_bytes: int = 16 * 1024 * 1024
    retained_output_bytes: int = 128 * 1024 * 1024
    temporary_storage_bytes: int = 256 * 1024 * 1024
    worker_concurrency: int = 1
    worker_processes: int = 1
    worker_threads: int = 1
    handles: int = 128
    wall_seconds: int = 300
    cpu_seconds: int = 300
    process_memory_bytes: int = 1024 * 1024 * 1024
    repeated_executions: int = 2


DEFAULT_LIMITS = ResourceLimits()


def require_at_most(label: str, actual: int, maximum: int) -> None:
    if actual > maximum:
        raise LimitExceeded(f"{label}={actual} exceeds ceiling {maximum}")


def require_exact(label: str, actual: int, expected: int) -> None:
    if actual != expected:
        raise LimitExceeded(f"{label}={actual} does not equal required {expected}")
