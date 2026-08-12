"""Role-relative path validation for caller-approved roots."""

from __future__ import annotations

import os
from pathlib import Path, PurePath


class UnsafePath(ValueError):
    """A path escaped or ambiguously addressed an approved root."""


def _is_link_or_junction(path: Path) -> bool:
    is_junction = getattr(os.path, "isjunction", lambda _path: False)
    return path.is_symlink() or bool(is_junction(path))


def _reject_case_ambiguity(root: Path, parts: tuple[str, ...]) -> None:
    if os.name != "nt":
        return
    current = root
    for part in parts:
        if not current.exists() or not current.is_dir():
            return
        matches = [entry.name for entry in current.iterdir() if entry.name.casefold() == part.casefold()]
        if len(matches) > 1 or (matches and part not in matches):
            raise UnsafePath("case-collision or case-normalization ambiguity rejected")
        current = current / part


def _validate_relative(relative: str) -> PurePath:
    if not relative or "\x00" in relative:
        raise UnsafePath("empty or NUL-containing path")
    candidate = PurePath(relative)
    if candidate.is_absolute() or candidate.drive or candidate.anchor:
        raise UnsafePath("absolute, drive, or share path rejected")
    if any(part in {"", ".", ".."} for part in candidate.parts):
        raise UnsafePath("empty, current, or parent segment rejected")
    if any(":" in part for part in candidate.parts):
        raise UnsafePath("device or alternate-data-stream syntax rejected")
    return candidate


def resolve_beneath(root: Path, relative: str, *, must_exist: bool) -> Path:
    parts = _validate_relative(relative).parts
    canonical_root = root.resolve(strict=True)
    _reject_case_ambiguity(canonical_root, parts)
    target = canonical_root.joinpath(*parts)
    probe = target if target.exists() else target.parent
    while probe != canonical_root and not probe.exists():
        probe = probe.parent
    if probe.exists() and _is_link_or_junction(probe):
        raise UnsafePath("symbolic-link or junction boundary rejected")
    resolved = target.resolve(strict=must_exist)
    try:
        resolved.relative_to(canonical_root)
    except ValueError as error:
        raise UnsafePath("path escapes approved root") from error
    current = canonical_root
    for part in parts[:-1] if not must_exist else parts:
        current = current / part
        if current.exists() and _is_link_or_junction(current):
            raise UnsafePath("symbolic-link or junction component rejected")
    return resolved
