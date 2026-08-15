"""Deterministic, local-only context packaging and verification."""

from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatchcase
import hashlib
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import shutil
import tempfile
import tomllib
from typing import Any
from uuid import uuid4


DEFAULT_EXCLUDE_PATTERNS = (
    ".git/**",
    ".opencntx/**",
    ".env*",
    "**/.env*",
    "**/*.key",
    "**/*.pem",
)
PACKAGE_DIRECTORY = Path(".opencntx") / "latest"
MANIFEST_VERSION = 1


class OpenCntxError(Exception):
    """A short, user-facing OPENCNTX error."""


@dataclass(frozen=True)
class ContextConfig:
    goal: str
    include: tuple[str, ...]
    required: tuple[str, ...]
    exclude: tuple[str, ...]
    max_files: int
    max_bytes: int


@dataclass(frozen=True)
class Selection:
    files: tuple[tuple[str, Path], ...]
    excluded: tuple[dict[str, str], ...]
    ignored: tuple[dict[str, str], ...]


@dataclass(frozen=True)
class Source:
    path: str
    content: bytes
    text: str
    sha256: str

    @property
    def byte_count(self) -> int:
        return len(self.content)


@dataclass(frozen=True)
class VerifyReport:
    unchanged: tuple[str, ...]
    changed: tuple[str, ...]
    missing: tuple[str, ...]
    unexpected: tuple[str, ...]
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not (
            self.changed
            or self.missing
            or self.unexpected
            or self.errors
        )


def _deduplicate(values: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def _normalize_pattern(value: str, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise OpenCntxError(f"{label} bevat een leeg of ongeldig patroon.")
    pattern = value.strip().replace("\\", "/")
    while "//" in pattern:
        pattern = pattern.replace("//", "/")
    while pattern.startswith("./"):
        pattern = pattern[2:]
    if not pattern or "\x00" in pattern:
        raise OpenCntxError(f"{label} bevat een leeg of ongeldig patroon.")
    if PurePosixPath(pattern).is_absolute() or PureWindowsPath(pattern).is_absolute():
        raise OpenCntxError(f"{label} mag geen absoluut pad bevatten: {value}")
    if ".." in PurePosixPath(pattern).parts:
        raise OpenCntxError(f"{label} mag de projectroot niet verlaten: {value}")
    return pattern


def _normalize_relative_path(value: str, label: str) -> str:
    path = _normalize_pattern(value, label)
    if any(character in path for character in "*?["):
        raise OpenCntxError(f"{label} bevat geen letterlijk relatief pad: {value}")
    return path


def _string_list(
    table: dict[str, Any],
    key: str,
    *,
    allow_empty: bool,
) -> tuple[str, ...]:
    value = table.get(key)
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise OpenCntxError(f"context.{key} moet een lijst met paden zijn.")
    if not allow_empty and not value:
        raise OpenCntxError(f"context.{key} mag niet leeg zijn.")
    return tuple(_normalize_pattern(item, f"context.{key}") for item in value)


def _positive_integer(table: dict[str, Any], key: str) -> int:
    value = table.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise OpenCntxError(f"context.{key} moet een positief geheel getal zijn.")
    return value


def _config_from_tables(
    task: dict[str, Any],
    context: dict[str, Any],
    *,
    add_default_excludes: bool,
) -> ContextConfig:
    goal = task.get("goal")
    if not isinstance(goal, str) or not goal.strip():
        raise OpenCntxError("task.goal moet een niet-lege tekst zijn.")

    include = _deduplicate(list(_string_list(context, "include", allow_empty=False)))
    required = _deduplicate(list(_string_list(context, "required", allow_empty=True)))
    configured_exclude = list(_string_list(context, "exclude", allow_empty=True))
    excludes = (
        list(DEFAULT_EXCLUDE_PATTERNS) + configured_exclude
        if add_default_excludes
        else configured_exclude
    )
    exclude = _deduplicate(
        [_normalize_pattern(item, "context.exclude") for item in excludes]
    )
    return ContextConfig(
        goal=goal.strip(),
        include=include,
        required=required,
        exclude=exclude,
        max_files=_positive_integer(context, "max_files"),
        max_bytes=_positive_integer(context, "max_bytes"),
    )


def load_config(project_root: Path) -> ContextConfig:
    """Read and strictly validate ``opencntx.toml`` in a project root."""
    root = project_root.resolve(strict=True)
    config_path = root / "opencntx.toml"
    try:
        resolved_config = config_path.resolve(strict=True)
    except FileNotFoundError as exc:
        raise OpenCntxError("opencntx.toml ontbreekt; voer eerst 'opencntx init' uit.") from exc
    if not resolved_config.is_relative_to(root):
        raise OpenCntxError("opencntx.toml mag de projectroot niet verlaten.")
    try:
        with resolved_config.open("rb") as config_file:
            data = tomllib.load(config_file)
    except tomllib.TOMLDecodeError as exc:
        raise OpenCntxError(f"opencntx.toml bevat ongeldige TOML: {exc}") from exc
    except OSError as exc:
        raise OpenCntxError(f"opencntx.toml kan niet worden gelezen: {exc}") from exc

    if not isinstance(data, dict):
        raise OpenCntxError("opencntx.toml heeft geen geldige tabelstructuur.")
    unknown_root = set(data) - {"task", "context"}
    if unknown_root:
        raise OpenCntxError(f"Onbekende TOML-sectie of sleutel: {sorted(unknown_root)[0]}")
    task = data.get("task")
    context = data.get("context")
    if not isinstance(task, dict) or not isinstance(context, dict):
        raise OpenCntxError("opencntx.toml vereist de tabellen [task] en [context].")
    unknown_task = set(task) - {"goal"}
    unknown_context = set(context) - {
        "include",
        "required",
        "exclude",
        "max_files",
        "max_bytes",
    }
    if unknown_task or unknown_context:
        unknown = sorted(unknown_task | unknown_context)[0]
        raise OpenCntxError(f"Onbekende configuratiesleutel: {unknown}")
    return _config_from_tables(task, context, add_default_excludes=True)


def _matches_pattern(relative_path: str, pattern: str) -> bool:
    if fnmatchcase(relative_path, pattern):
        return True
    if pattern.endswith("/**") and relative_path == pattern[:-3].rstrip("/"):
        return True
    if pattern.startswith("**/") and fnmatchcase(relative_path, pattern[3:]):
        return True
    if "/" not in pattern:
        return any(fnmatchcase(part, pattern) for part in PurePosixPath(relative_path).parts)
    return False


def _matching_exclusion(relative_path: str, patterns: tuple[str, ...]) -> str | None:
    return next(
        (pattern for pattern in patterns if _matches_pattern(relative_path, pattern)),
        None,
    )


def _expand(root: Path, pattern: str) -> list[Path]:
    try:
        return sorted(root.glob(pattern), key=lambda path: path.relative_to(root).as_posix())
    except (OSError, ValueError) as exc:
        raise OpenCntxError(
            f"Include-patroon kan niet worden uitgebreid: {pattern}: {exc}"
        ) from exc


def discover_sources(
    project_root: Path,
    config: ContextConfig,
    *,
    enforce_required: bool,
) -> Selection:
    """Expand includes deterministically and exclude paths before reading bytes."""
    root = project_root.resolve(strict=True)
    selected: dict[str, Path] = {}
    excluded: dict[tuple[str, str], dict[str, str]] = {}
    ignored: dict[tuple[str, str], dict[str, str]] = {}

    for pattern in config.include:
        matches = _expand(root, pattern)
        if not matches:
            ignored[(pattern, "geen overeenkomst")] = {
                "pattern": pattern,
                "reason": "include-patroon vond geen pad",
            }
        for candidate in matches:
            try:
                relative_path = candidate.relative_to(root).as_posix()
            except ValueError as exc:
                raise OpenCntxError(f"Pad verlaat de projectroot: {candidate}") from exc
            exclusion = _matching_exclusion(relative_path, config.exclude)
            if exclusion is not None:
                if relative_path == ".opencntx" or relative_path.startswith(".opencntx/"):
                    continue
                excluded[(relative_path, exclusion)] = {
                    "path": relative_path,
                    "pattern": exclusion,
                    "reason": "uitgesloten vóór lezen",
                }
                continue
            try:
                resolved = candidate.resolve(strict=True)
            except OSError as exc:
                raise OpenCntxError(
                    f"Bronpad is ontbrekend of ontoegankelijk: {relative_path}: {exc}"
                ) from exc
            if not resolved.is_relative_to(root):
                raise OpenCntxError(f"Bronpad verlaat via symlink de projectroot: {relative_path}")
            if resolved.is_dir():
                ignored[(relative_path, "map")] = {
                    "path": relative_path,
                    "reason": "map is geen tekstbron",
                }
                continue
            if not resolved.is_file():
                ignored[(relative_path, "geen bestand")] = {
                    "path": relative_path,
                    "reason": "pad is geen regulier bestand",
                }
                continue
            selected[relative_path] = resolved

    ordered_files = tuple(sorted(selected.items()))
    if enforce_required:
        selected_paths = tuple(path for path, _ in ordered_files)
        for pattern in config.required:
            if not any(_matches_pattern(path, pattern) for path in selected_paths):
                raise OpenCntxError(
                    f"Verplicht patroon levert geen opgenomen bestand op: {pattern}"
                )
    return Selection(
        files=ordered_files,
        excluded=tuple(excluded[key] for key in sorted(excluded)),
        ignored=tuple(ignored[key] for key in sorted(ignored)),
    )


def _read_source(
    project_root: Path,
    relative_path: str,
    *,
    byte_limit: int | None = None,
) -> Source:
    root = project_root.resolve(strict=True)
    safe_path = _normalize_relative_path(relative_path, "bronpad")
    logical_path = root.joinpath(*PurePosixPath(safe_path).parts)
    try:
        resolved = logical_path.resolve(strict=True)
    except OSError as exc:
        raise OpenCntxError(f"Bron is ontbrekend of ontoegankelijk: {safe_path}: {exc}") from exc
    if not resolved.is_relative_to(root):
        raise OpenCntxError(f"Bron verlaat via symlink de projectroot: {safe_path}")
    try:
        declared_size = resolved.stat().st_size
        if byte_limit is not None and declared_size > byte_limit:
            raise OpenCntxError(
                f"Bytebudget overschreden vóór lezen door: {safe_path}. "
                "Verklein context.include, sluit het bestand uit of verhoog max_bytes."
            )
        content = resolved.read_bytes()
        if byte_limit is not None and len(content) > byte_limit:
            raise OpenCntxError(
                f"Bytebudget overschreden tijdens lezen door: {safe_path}. "
                "Verklein context.include, sluit het bestand uit of verhoog max_bytes."
            )
    except OpenCntxError:
        raise
    except OSError as exc:
        raise OpenCntxError(f"Bron kan niet worden gelezen: {safe_path}: {exc}") from exc
    if b"\x00" in content or any(
        byte < 32 and byte not in (9, 10, 13) for byte in content
    ):
        raise OpenCntxError(f"Binaire bron wordt geweigerd: {safe_path}")
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise OpenCntxError(f"Bron is geen geldige UTF-8-tekst: {safe_path}") from exc
    return Source(
        path=safe_path,
        content=content,
        text=text,
        sha256=hashlib.sha256(content).hexdigest(),
    )


def read_sources(
    project_root: Path,
    selection: Selection,
    config: ContextConfig,
) -> tuple[Source, ...]:
    if not selection.files:
        raise OpenCntxError("Geen tekstbronnen geselecteerd; pas context.include aan.")
    if len(selection.files) > config.max_files:
        raise OpenCntxError(
            f"Bestandsbudget overschreden: {len(selection.files)} > {config.max_files}. "
            "Verklein context.include of verhoog max_files."
        )
    sources: list[Source] = []
    total_bytes = 0
    for relative_path, _ in selection.files:
        source = _read_source(
            project_root,
            relative_path,
            byte_limit=config.max_bytes - total_bytes,
        )
        total_bytes += source.byte_count
        if total_bytes > config.max_bytes:
            raise OpenCntxError(
                f"Bytebudget overschreden: {total_bytes} > {config.max_bytes}. "
                "Verklein context.include, sluit grote bestanden uit of verhoog max_bytes."
            )
        sources.append(source)
    return tuple(sources)


def _markdown_fence(text: str) -> str:
    longest = max((len(match.group(0)) for match in re.finditer(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def render_context(goal: str, sources: tuple[Source, ...]) -> str:
    lines = [
        "# OPENCNTX Context Package",
        "",
        "## Taak",
        "",
        goal,
        "",
        "## Bronnen",
    ]
    for source in sources:
        fence = _markdown_fence(source.text)
        lines.extend(
            [
                "",
                f"### `{source.path}`",
                "",
                f"- Bytes: {source.byte_count}",
                f"- SHA-256: `{source.sha256}`",
                "",
                f"{fence}text",
                source.text,
                fence,
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _manifest(
    config: ContextConfig,
    selection: Selection,
    sources: tuple[Source, ...],
    context_bytes: bytes,
) -> dict[str, Any]:
    return {
        "format": "opencntx-manifest",
        "format_version": MANIFEST_VERSION,
        "task": {"goal": config.goal},
        "selection": {
            "include": list(config.include),
            "required": list(config.required),
            "exclude": list(config.exclude),
            "max_files": config.max_files,
            "max_bytes": config.max_bytes,
        },
        "package": {
            "file_count": len(sources),
            "total_bytes": sum(source.byte_count for source in sources),
            "context_sha256": hashlib.sha256(context_bytes).hexdigest(),
        },
        "sources": [
            {
                "path": source.path,
                "bytes": source.byte_count,
                "sha256": source.sha256,
            }
            for source in sources
        ],
        "excluded": list(selection.excluded),
        "ignored": list(selection.ignored),
    }


def _write_file(path: Path, content: bytes) -> None:
    with path.open("xb") as output:
        output.write(content)
        output.flush()
        os.fsync(output.fileno())


def _atomic_package_write(
    project_root: Path,
    context_bytes: bytes,
    manifest_bytes: bytes,
) -> Path:
    root = project_root.resolve(strict=True)
    output_parent = root / ".opencntx"
    if output_parent.is_symlink():
        raise OpenCntxError(".opencntx mag geen symlink zijn.")
    try:
        output_parent.mkdir(exist_ok=True)
        resolved_parent = output_parent.resolve(strict=True)
    except OSError as exc:
        raise OpenCntxError(f"Uitvoermap kan niet worden gemaakt: {exc}") from exc
    if not resolved_parent.is_relative_to(root) or not resolved_parent.is_dir():
        raise OpenCntxError("Uitvoermap moet binnen de projectroot liggen.")

    latest = output_parent / "latest"
    if latest.is_symlink():
        raise OpenCntxError(".opencntx/latest mag geen symlink zijn.")
    temporary = Path(tempfile.mkdtemp(prefix=".building-", dir=output_parent))
    backup: Path | None = None
    try:
        _write_file(temporary / "CONTEXT.md", context_bytes)
        _write_file(temporary / "manifest.json", manifest_bytes)
        if latest.exists():
            if not latest.is_dir():
                raise OpenCntxError(".opencntx/latest is geen pakketmap.")
            backup = output_parent / f".previous-{uuid4().hex}"
            os.replace(latest, backup)
        try:
            os.replace(temporary, latest)
        except OSError:
            if backup is not None and backup.exists() and not latest.exists():
                os.replace(backup, latest)
            raise
        if backup is not None:
            shutil.rmtree(backup, ignore_errors=True)
        return latest
    except OpenCntxError:
        raise
    except OSError as exc:
        raise OpenCntxError(f"Pakket kon niet atomair worden geschreven: {exc}") from exc
    finally:
        if temporary.exists():
            shutil.rmtree(temporary, ignore_errors=True)


def pack_project(project_root: Path) -> tuple[Path, dict[str, Any]]:
    """Build the complete package in memory, then atomically publish it."""
    root = project_root.resolve(strict=True)
    config = load_config(root)
    selection = discover_sources(root, config, enforce_required=True)
    sources = read_sources(root, selection, config)
    context_bytes = render_context(config.goal, sources).encode("utf-8")
    manifest = _manifest(config, selection, sources, context_bytes)
    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    package_path = _atomic_package_write(root, context_bytes, manifest_bytes)
    return package_path, manifest


def _load_manifest(package_path: Path) -> tuple[Path, Path, dict[str, Any], ContextConfig]:
    try:
        package = package_path.resolve(strict=True)
    except OSError as exc:
        raise OpenCntxError(f"Pakketmap ontbreekt of is ontoegankelijk: {package_path}") from exc
    if not package.is_dir() or package.parent.name != ".opencntx":
        raise OpenCntxError("Pakketmap moet direct onder .opencntx staan.")
    root = package.parent.parent.resolve(strict=True)
    manifest_path = package / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise OpenCntxError("manifest.json ontbreekt in het pakket.") from exc
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise OpenCntxError(f"manifest.json is ongeldig of onleesbaar: {exc}") from exc
    if not isinstance(manifest, dict):
        raise OpenCntxError("manifest.json heeft geen geldige objectstructuur.")
    if (
        manifest.get("format") != "opencntx-manifest"
        or manifest.get("format_version") != MANIFEST_VERSION
    ):
        raise OpenCntxError("manifest.json gebruikt een onbekend formaat of versie.")
    task = manifest.get("task")
    selection = manifest.get("selection")
    if not isinstance(task, dict) or not isinstance(selection, dict):
        raise OpenCntxError("manifest.json mist taak- of selectiegegevens.")
    config = _config_from_tables(task, selection, add_default_excludes=False)
    return root, package, manifest, config


def _expected_sources(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    source_list = manifest.get("sources")
    if not isinstance(source_list, list):
        raise OpenCntxError("manifest.json mist een geldige bronnenlijst.")
    expected: dict[str, dict[str, Any]] = {}
    for item in source_list:
        if not isinstance(item, dict):
            raise OpenCntxError("manifest.json bevat een ongeldige bronregistratie.")
        path = _normalize_relative_path(item.get("path"), "manifest-bronpad")
        byte_count = item.get("bytes")
        digest = item.get("sha256")
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
            or not isinstance(digest, str)
            or re.fullmatch(r"[0-9a-f]{64}", digest) is None
        ):
            raise OpenCntxError(f"manifest.json bevat ongeldige metadata voor: {path}")
        if path in expected:
            raise OpenCntxError(f"manifest.json bevat een dubbel bronpad: {path}")
        expected[path] = item
    return expected


def verify_package(package_path: Path) -> VerifyReport:
    """Compare a package with current sources without writing any file."""
    root, package, manifest, config = _load_manifest(package_path)
    expected = _expected_sources(manifest)
    errors: list[str] = []

    package_info = manifest.get("package")
    if not isinstance(package_info, dict):
        raise OpenCntxError("manifest.json mist geldige pakketmetadata.")
    expected_context_hash = package_info.get("context_sha256")
    if (
        isinstance(package_info.get("file_count"), bool)
        or package_info.get("file_count") != len(expected)
        or isinstance(package_info.get("total_bytes"), bool)
        or package_info.get("total_bytes")
        != sum(item["bytes"] for item in expected.values())
        or not isinstance(expected_context_hash, str)
        or re.fullmatch(r"[0-9a-f]{64}", expected_context_hash) is None
    ):
        errors.append("manifest.json bevat intern inconsistente pakketmetadata")
    try:
        context_bytes = (package / "CONTEXT.md").read_bytes()
        actual_context_hash = hashlib.sha256(context_bytes).hexdigest()
        if expected_context_hash != actual_context_hash:
            errors.append("CONTEXT.md wijkt af van de manifest-hash")
    except OSError as exc:
        errors.append(f"CONTEXT.md kan niet volledig worden gecontroleerd: {exc}")

    selection: Selection | None
    try:
        selection = discover_sources(root, config, enforce_required=False)
        current_paths = {path for path, _ in selection.files}
    except OpenCntxError as exc:
        selection = None
        current_paths = {
            path
            for path in expected
            if root.joinpath(*PurePosixPath(path).parts).exists()
        }
        errors.append(f"Bronselectie is onvolledig: {exc}")

    expected_paths = set(expected)
    missing = sorted(expected_paths - current_paths)
    unexpected = sorted(current_paths - expected_paths)
    changed: list[str] = []
    unchanged: list[str] = []
    current_sources: dict[str, Source] = {}
    total_bytes = 0
    for path in sorted(current_paths):
        try:
            source = _read_source(
                root,
                path,
                byte_limit=max(config.max_bytes - total_bytes, 0),
            )
            current_sources[path] = source
            total_bytes += source.byte_count
        except OpenCntxError as exc:
            errors.append(str(exc))
            if path in expected_paths:
                changed.append(path)

    if len(current_paths) > config.max_files:
        errors.append(
            f"Bestandsbudget is nu overschreden: {len(current_paths)} > {config.max_files}"
        )
    if total_bytes > config.max_bytes:
        errors.append(f"Bytebudget is nu overschreden: {total_bytes} > {config.max_bytes}")

    for path in sorted(expected_paths & current_paths):
        source = current_sources.get(path)
        if source is None:
            continue
        record = expected[path]
        if source.byte_count != record["bytes"] or source.sha256 != record["sha256"]:
            changed.append(path)
        else:
            unchanged.append(path)

    return VerifyReport(
        unchanged=tuple(sorted(set(unchanged))),
        changed=tuple(sorted(set(changed))),
        missing=tuple(missing),
        unexpected=tuple(unexpected),
        errors=tuple(sorted(set(errors))),
    )


def format_verify_report(report: VerifyReport) -> str:
    """Render every required drift category, including empty ones."""
    lines: list[str] = []
    for label, paths in (
        ("unchanged", report.unchanged),
        ("changed", report.changed),
        ("missing", report.missing),
        ("unexpected", report.unexpected),
    ):
        lines.append(f"{label} ({len(paths)}):")
        lines.extend(f"  {path}" for path in paths)
    lines.append(f"errors ({len(report.errors)}):")
    lines.extend(f"  {error}" for error in report.errors)
    lines.append("resultaat: OK" if report.ok else "resultaat: DRIFT OF ONVOLLEDIG")
    return "\n".join(lines)
