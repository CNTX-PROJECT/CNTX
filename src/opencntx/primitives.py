"""Small byte-exact primitives shared by OPENCNTX domains."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def utc_now() -> datetime:
    """Return the current timezone-aware UTC time."""
    return datetime.now(UTC)


def timestamp_microseconds(value: datetime) -> str:
    """Render the established microsecond UTC timestamp representation."""
    return value.isoformat(timespec="microseconds").replace("+00:00", "Z")


def pretty_json_bytes(value: object) -> bytes:
    """Render the established UTF-8, indented, sorted JSON representation."""
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    """Return the lowercase SHA-256 digest of exact bytes."""
    return hashlib.sha256(value).hexdigest()


def read_json_object(path: Path) -> tuple[dict[str, Any], bytes]:
    """Read one UTF-8 JSON object without imposing domain error semantics."""
    content = path.read_bytes()
    value = json.loads(content)
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value, content
