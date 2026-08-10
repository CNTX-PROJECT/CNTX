"""Strict UTF-8 JSON parsing without repair, coercion, or duplicate members."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from .limits import DEFAULT_LIMITS, ResourceLimits, require_at_most


class StrictJsonError(ValueError):
    """A bounded strict-JSON rejection."""


def _reject_constant(value: str) -> None:
    raise StrictJsonError(f"non-JSON numeric constant rejected: {value}")


def _unique_object(pairs: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJsonError(f"duplicate object member rejected: {key!r}")
        result[key] = value
    return result


def _measure(root: Any, limits: ResourceLimits) -> tuple[int, int]:
    nodes = 0
    deepest = 0
    stack: list[tuple[Any, int]] = [(root, 1)]
    while stack:
        value, depth = stack.pop()
        nodes += 1
        deepest = max(deepest, depth)
        require_at_most("JSON nodes", nodes, limits.json_nodes)
        require_at_most("JSON depth", deepest, limits.json_depth)
        if isinstance(value, dict):
            stack.extend((item, depth + 1) for item in value.values())
        elif isinstance(value, list):
            stack.extend((item, depth + 1) for item in value)
    return nodes, deepest


def loads_strict(data: bytes, limits: ResourceLimits = DEFAULT_LIMITS) -> Any:
    require_at_most("individual JSON bytes", len(data), limits.individual_json_bytes)
    if data.startswith(b"\xef\xbb\xbf"):
        raise StrictJsonError("UTF-8 BOM rejected")
    try:
        text = data.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise StrictJsonError("invalid UTF-8 rejected") from error
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except (json.JSONDecodeError, StrictJsonError) as error:
        raise StrictJsonError(str(error)) from error
    _measure(value, limits)
    return value


def load_strict(path: Path, limits: ResourceLimits = DEFAULT_LIMITS) -> Any:
    return loads_strict(path.read_bytes(), limits)
