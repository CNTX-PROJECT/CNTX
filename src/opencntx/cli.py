"""Command-line interface for OPENCNTX."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
import os
from pathlib import Path
import sys

from . import __version__
from .catalog import create_chapter, rebuild_catalog
from .core import (
    OpenCntxError,
    format_pack_preview,
    format_verify_report,
    pack_project,
    plan_project,
    verify_package,
)
from .control import refresh_control_snapshot
from .integrity import (
    IntegrityError,
    doctor_workspace,
    format_doctor_report,
    format_recovery_plan,
    recover_workspace,
)
from .navigator import (
    build_context_package,
    format_context_verify_report,
    verify_context_package,
)
from .media import (
    DECISIONS,
    KINDS,
    PRODUCER_CLASSES,
    format_media_verify_report,
    media_status,
    promote_derivation,
    register_derivation,
    remove_derivation,
    review_derivation,
    verify_media,
)
from .playbook import (
    approve_playbook,
    approve_role,
    executor_status,
    format_definition_verify_report,
    format_executor_verify_report,
    playbook_status,
    prepare_executor,
    register_playbook,
    register_role,
    role_status,
    verify_executor,
    verify_playbook,
    verify_role,
)
from .workflow import (
    accept_result,
    approve_task,
    begin_task,
    cancel_task,
    close_task,
    propose_task,
    record_attempt,
    review_result,
    submit_result,
    supersede_task,
    task_status,
)
from .workspace import (
    PRIVACY_LABELS,
    WorkspaceError,
    capture_source,
    init_workspace,
)


CONFIG_TEMPLATE = '''[task]
goal = "Describe the one concrete task"

[context]
include = ["README.md", "src/**/*.py"]
required = ["README.md"]
exclude = [".git/**", ".env*", "**/*.key", "**/*.pem"]
max_files = 25
max_bytes = 100000
'''


def build_parser() -> argparse.ArgumentParser:
    """Build the public CLI parser."""
    parser = argparse.ArgumentParser(
        prog="opencntx",
        description="Create a small, explicit, and verifiable context package for one task.",
        epilog=(
            "Core route: init, pack --preview, pack, inspect CONTEXT.md, verify. "
            "Advanced / Alpha: workspace."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "init",
        help="safely create an opencntx.toml template in the current directory",
    )
    pack_parser = subparsers.add_parser(
        "pack",
        help="atomically create CONTEXT.md and manifest.json from selected sources",
    )
    pack_parser.add_argument(
        "--preview",
        action="store_true",
        help="show the exact selection and secret decision without writing anything",
    )
    pack_parser.add_argument(
        "--allow-secret",
        action="append",
        default=[],
        metavar="FINDING_ID",
        help="override one exact current high-confidence finding; repeatable",
    )
    verify_parser = subparsers.add_parser(
        "verify",
        help="check a package for changed, missing, and unexpected sources",
    )
    verify_parser.add_argument(
        "package",
        nargs="?",
        default=".opencntx/latest",
        help="package directory; default: .opencntx/latest",
    )
    workspace_parser = subparsers.add_parser(
        "workspace",
        help="Advanced / Alpha: local storage, media, catalog, task gates, and navigation",
    )
    workspace_subparsers = workspace_parser.add_subparsers(
        dest="workspace_command",
        required=True,
    )
    workspace_init_parser = workspace_subparsers.add_parser(
        "init",
        help="safely create the fixed project workspace structure",
    )
    workspace_init_parser.add_argument(
        "project",
        nargs="?",
        default=".",
        help="project directory; default: current directory",
    )
    workspace_capture_parser = workspace_subparsers.add_parser(
        "capture",
        help="capture one regular local file without executing it",
    )
    workspace_capture_parser.add_argument("source", help="local source file")
    workspace_capture_parser.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )
    workspace_capture_parser.add_argument(
        "--privacy",
        choices=PRIVACY_LABELS,
        default="PRIVATE",
        help="privacy label; default: PRIVATE",
    )
    workspace_capture_parser.add_argument(
        "--origin",
        help="short origin on one line",
    )
    workspace_capture_parser.add_argument(
        "--supersedes",
        help="optional existing source ID superseded by this new source",
    )
    workspace_doctor_parser = workspace_subparsers.add_parser(
        "doctor",
        help="read-only diagnosis of active or incomplete writer transactions",
    )
    workspace_doctor_parser.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )
    workspace_recover_parser = workspace_subparsers.add_parser(
        "recover",
        help="preview or apply exact backup-first transaction recovery",
    )
    workspace_recover_parser.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )
    workspace_recover_parser.add_argument(
        "--transaction",
        required=True,
        help="exact transaction ID reported by workspace doctor",
    )
    workspace_recover_parser.add_argument(
        "--intent-sha256",
        required=True,
        help="exact intent SHA-256 reported by workspace doctor",
    )
    workspace_recover_parser.add_argument(
        "--apply",
        action="store_true",
        help="apply the exact recovery after a read-only preview",
    )
    workspace_control_parser = workspace_subparsers.add_parser(
        "control",
        help="manage the compact derived current roadmap control",
    )
    workspace_control_subparsers = workspace_control_parser.add_subparsers(
        dest="workspace_control_command",
        required=True,
    )
    workspace_control_refresh_parser = workspace_control_subparsers.add_parser(
        "refresh",
        help="refresh the control snapshot without changing the official roadmap",
    )
    workspace_control_refresh_parser.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )
    workspace_chapter_parser = workspace_subparsers.add_parser(
        "chapter",
        help="create a safe chapter template that is not yet approved",
    )
    workspace_chapter_subparsers = workspace_chapter_parser.add_subparsers(
        dest="workspace_chapter_command",
        required=True,
    )
    workspace_chapter_create_parser = workspace_chapter_subparsers.add_parser(
        "create",
        help="create one new DRAFT chapter without overwriting anything",
    )
    workspace_chapter_create_parser.add_argument(
        "chapter_id",
        help="stable chapter ID, for example CH-ELECTRICITY",
    )
    workspace_chapter_create_parser.add_argument(
        "--title",
        required=True,
        help="short readable chapter title",
    )
    workspace_chapter_create_parser.add_argument(
        "--scope",
        default="UNKNOWN - to be determined by OWNER and ARCHITECT.",
        help="short boundary of the subject",
    )
    workspace_chapter_create_parser.add_argument(
        "--source",
        action="append",
        default=[],
        help="existing exact source ID; repeatable",
    )
    workspace_chapter_create_parser.add_argument(
        "--depends-on",
        action="append",
        default=[],
        help="existing chapter ID; repeatable",
    )
    workspace_chapter_create_parser.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )
    workspace_catalog_parser = workspace_subparsers.add_parser(
        "catalog",
        help="rebuild the human index and local SQLite catalog",
    )
    workspace_catalog_subparsers = workspace_catalog_parser.add_subparsers(
        dest="workspace_catalog_command",
        required=True,
    )
    workspace_catalog_rebuild_parser = workspace_catalog_subparsers.add_parser(
        "rebuild",
        help="rebuild the catalog and index from official workspace files",
    )
    workspace_catalog_rebuild_parser.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )
    workspace_media_parser = workspace_subparsers.add_parser(
        "media",
        help="register and verify text safely derived from media",
    )
    workspace_media_subparsers = workspace_media_parser.add_subparsers(
        dest="workspace_media_command",
        required=True,
    )
    media_register_parser = workspace_media_subparsers.add_parser(
        "register",
        help="register supplied UTF-8 text without starting OCR, AI, or another tool",
    )
    media_register_parser.add_argument("source_id")
    media_register_parser.add_argument("--text", required=True)
    media_register_parser.add_argument("--kind", required=True, choices=KINDS)
    media_register_parser.add_argument(
        "--producer-class", required=True, choices=PRODUCER_CLASSES
    )
    media_register_parser.add_argument("--producer", required=True)
    media_register_parser.add_argument("--locator", action="append", default=[])
    media_register_parser.add_argument("--supersedes-derivation-id")
    media_register_parser.add_argument("--root", default=".")

    media_review_parser = workspace_media_subparsers.add_parser(
        "review",
        help="review one exact derivation without accepting it as fact",
    )
    media_review_parser.add_argument("source_id")
    media_review_parser.add_argument("derivation_id")
    media_review_parser.add_argument("--content-sha256", required=True)
    media_review_parser.add_argument("--decision", required=True, choices=DECISIONS)
    media_review_parser.add_argument("--finding", action="append", required=True)
    media_review_parser.add_argument("--reviewer", required=True)
    media_review_parser.add_argument("--root", default=".")

    media_promote_parser = workspace_media_subparsers.add_parser(
        "promote",
        help="deliberately promote reviewed text to a regular CAPTURED source",
    )
    media_promote_parser.add_argument("source_id")
    media_promote_parser.add_argument("derivation_id")
    media_promote_parser.add_argument("--review-digest", required=True)
    media_promote_parser.add_argument("--root", default=".")

    media_status_parser = workspace_media_subparsers.add_parser(
        "status",
        help="show whether media is unexamined, derived, reviewed, or removed",
    )
    media_status_parser.add_argument("source_id")
    media_status_parser.add_argument("derivation_id", nargs="?")
    media_status_parser.add_argument("--root", default=".")

    media_verify_parser = workspace_media_subparsers.add_parser(
        "verify",
        help="verify original, derived, and promotion bytes fully read-only",
    )
    media_verify_parser.add_argument("source_id")
    media_verify_parser.add_argument("derivation_id", nargs="?")
    media_verify_parser.add_argument("--root", default=".")

    media_remove_parser = workspace_media_subparsers.add_parser(
        "remove",
        help="remove only exactly pinned derived text and create a tombstone",
    )
    media_remove_parser.add_argument("source_id")
    media_remove_parser.add_argument("derivation_id")
    media_remove_parser.add_argument("--record-digest", required=True)
    media_remove_parser.add_argument("--content-sha256", required=True)
    media_remove_parser.add_argument("--owner", required=True)
    media_remove_parser.add_argument("--root", default=".")
    workspace_playbook_parser = workspace_subparsers.add_parser(
        "playbook",
        help="register and approve non-executing playbook revisions",
    )
    workspace_playbook_subparsers = workspace_playbook_parser.add_subparsers(
        dest="workspace_playbook_command",
        required=True,
    )
    playbook_register_parser = workspace_playbook_subparsers.add_parser(
        "register",
        help="register one immutable proposed playbook revision",
    )
    playbook_register_parser.add_argument("playbook_id")
    playbook_register_parser.add_argument("--revision", required=True, type=int)
    playbook_register_parser.add_argument("--title", required=True)
    playbook_register_parser.add_argument("--purpose", required=True)
    playbook_register_parser.add_argument("--input", action="append", required=True)
    playbook_register_parser.add_argument("--step", action="append", required=True)
    playbook_register_parser.add_argument("--stop", action="append", required=True)
    playbook_register_parser.add_argument("--evidence", action="append", required=True)
    playbook_register_parser.add_argument("--allow", action="append", required=True)
    playbook_register_parser.add_argument("--forbid", action="append", required=True)
    playbook_register_parser.add_argument("--architect", required=True)
    playbook_register_parser.add_argument("--supersedes-digest")
    playbook_register_parser.add_argument("--root", default=".")
    playbook_approve_parser = workspace_playbook_subparsers.add_parser(
        "approve",
        help="bind a local OWNER approval to one exact playbook revision",
    )
    playbook_approve_parser.add_argument("playbook_id")
    playbook_approve_parser.add_argument("--revision", required=True, type=int)
    playbook_approve_parser.add_argument("--definition-digest", required=True)
    playbook_approve_parser.add_argument("--owner", required=True)
    playbook_approve_parser.add_argument("--root", default=".")
    for command_name, help_text in (
        ("status", "show the computed playbook status without writing"),
        ("verify", "verify playbook bytes and approval fully read-only"),
    ):
        command_parser = workspace_playbook_subparsers.add_parser(
            command_name, help=help_text
        )
        command_parser.add_argument("playbook_id")
        command_parser.add_argument("--revision", required=True, type=int)
        command_parser.add_argument("--root", default=".")

    workspace_role_parser = workspace_subparsers.add_parser(
        "role",
        help="register bounded role revisions without OWNER authority",
    )
    workspace_role_subparsers = workspace_role_parser.add_subparsers(
        dest="workspace_role_command",
        required=True,
    )
    role_register_parser = workspace_role_subparsers.add_parser(
        "register",
        help="register one immutable proposed role revision",
    )
    role_register_parser.add_argument("role_id")
    role_register_parser.add_argument("--revision", required=True, type=int)
    role_register_parser.add_argument("--title", required=True)
    role_register_parser.add_argument(
        "--responsibility", action="append", required=True
    )
    role_register_parser.add_argument("--allow", action="append", required=True)
    role_register_parser.add_argument("--forbid", action="append", required=True)
    role_register_parser.add_argument("--handoff", required=True)
    role_register_parser.add_argument("--architect", required=True)
    role_register_parser.add_argument("--supersedes-digest")
    role_register_parser.add_argument("--root", default=".")
    role_approve_parser = workspace_role_subparsers.add_parser(
        "approve",
        help="bind a local OWNER approval to one exact role revision",
    )
    role_approve_parser.add_argument("role_id")
    role_approve_parser.add_argument("--revision", required=True, type=int)
    role_approve_parser.add_argument("--definition-digest", required=True)
    role_approve_parser.add_argument("--owner", required=True)
    role_approve_parser.add_argument("--root", default=".")
    for command_name, help_text in (
        ("status", "show the computed role status without writing"),
        ("verify", "verify role bytes and approval fully read-only"),
    ):
        command_parser = workspace_role_subparsers.add_parser(
            command_name, help=help_text
        )
        command_parser.add_argument("role_id")
        command_parser.add_argument("--revision", required=True, type=int)
        command_parser.add_argument("--root", default=".")

    workspace_executor_parser = workspace_subparsers.add_parser(
        "executor",
        help="create or verify one non-executing task-bound executor package",
    )
    workspace_executor_subparsers = workspace_executor_parser.add_subparsers(
        dest="workspace_executor_command",
        required=True,
    )
    executor_prepare_parser = workspace_executor_subparsers.add_parser(
        "prepare",
        help="bind task, context, playbook, and role without starting an executor",
    )
    executor_prepare_parser.add_argument("task_id")
    executor_prepare_parser.add_argument("--revision", required=True, type=int)
    executor_prepare_parser.add_argument("--proposal-digest", required=True)
    executor_prepare_parser.add_argument("--playbook-id", required=True)
    executor_prepare_parser.add_argument("--playbook-revision", required=True, type=int)
    executor_prepare_parser.add_argument("--playbook-digest", required=True)
    executor_prepare_parser.add_argument("--role-id", required=True)
    executor_prepare_parser.add_argument("--role-revision", required=True, type=int)
    executor_prepare_parser.add_argument("--role-digest", required=True)
    executor_prepare_parser.add_argument("--context-manifest-digest", required=True)
    executor_prepare_parser.add_argument("--executor", required=True)
    executor_prepare_parser.add_argument("--root", default=".")
    for command_name, help_text in (
        ("status", "show the current executor package status without writing"),
        ("verify", "verify all task, context, and definition bindings read-only"),
    ):
        command_parser = workspace_executor_subparsers.add_parser(
            command_name, help=help_text
        )
        command_parser.add_argument("task_id")
        command_parser.add_argument("executor_id")
        command_parser.add_argument("--root", default=".")
    workspace_context_parser = workspace_subparsers.add_parser(
        "context",
        help="build or verify one task-bound hot-warm-cold package",
    )
    workspace_context_subparsers = workspace_context_parser.add_subparsers(
        dest="workspace_context_command",
        required=True,
    )
    workspace_context_build_parser = workspace_context_subparsers.add_parser(
        "build",
        help="build local context for one approved task in execution",
    )
    workspace_context_build_parser.add_argument("task_id")
    workspace_context_build_parser.add_argument("--proposal-digest", required=True)
    workspace_context_build_parser.add_argument("--max-files", required=True, type=int)
    workspace_context_build_parser.add_argument("--max-bytes", required=True, type=int)
    workspace_context_build_parser.add_argument("--root", default=".")
    workspace_context_verify_parser = workspace_context_subparsers.add_parser(
        "verify",
        help="verify package bytes and the complete current task route read-only",
    )
    workspace_context_verify_parser.add_argument("task_id")
    workspace_context_verify_parser.add_argument("--proposal-digest", required=True)
    workspace_context_verify_parser.add_argument("--root", default=".")
    workspace_task_parser = workspace_subparsers.add_parser(
        "task",
        help="register one bounded task with exact OWNER gates",
    )
    workspace_task_subparsers = workspace_task_parser.add_subparsers(
        dest="workspace_task_command",
        required=True,
    )
    task_propose_parser = workspace_task_subparsers.add_parser(
        "propose",
        help="create one task proposal that waits for exact OWNER approval",
    )
    task_propose_parser.add_argument("task_id", help="task ID, for example TASK-20260816-0001")
    task_propose_parser.add_argument("--title", required=True, help="short task title")
    task_propose_parser.add_argument("--goal", required=True, help="one bounded goal")
    task_propose_parser.add_argument(
        "--done", required=True, help="exacte Definition of Done"
    )
    task_propose_parser.add_argument(
        "--executor-role", required=True, help="bounded executor role"
    )
    task_propose_parser.add_argument(
        "--input", action="append", required=True, help="official relative input path; repeatable"
    )
    task_propose_parser.add_argument(
        "--allow", action="append", required=True, help="allowed action; repeatable"
    )
    task_propose_parser.add_argument(
        "--forbid", action="append", required=True, help="forbidden action; repeatable"
    )
    task_propose_parser.add_argument(
        "--expected-output", required=True, help="expected result form"
    )
    task_propose_parser.add_argument(
        "--acceptance", action="append", required=True, help="acceptance criterion; repeatable"
    )
    task_propose_parser.add_argument(
        "--architect", required=True, help="local ARCHITECT actor statement"
    )
    task_propose_parser.add_argument("--root", default=".", help="project workspace")

    task_approve_parser = workspace_task_subparsers.add_parser(
        "approve", help="register an exact local OWNER approval"
    )
    task_approve_parser.add_argument("task_id")
    task_approve_parser.add_argument("--revision", required=True, type=int)
    task_approve_parser.add_argument("--proposal-digest", required=True)
    task_approve_parser.add_argument("--owner", required=True)
    task_approve_parser.add_argument("--root", default=".")

    task_begin_parser = workspace_task_subparsers.add_parser(
        "begin", help="register execution without starting a process or agent"
    )
    task_begin_parser.add_argument("task_id")
    task_begin_parser.add_argument("--architect", required=True)
    task_begin_parser.add_argument("--root", default=".")

    task_result_parser = workspace_task_subparsers.add_parser(
        "submit-result", help="store one result and optional evidence as bytes"
    )
    task_result_parser.add_argument("task_id")
    task_result_parser.add_argument("--result", required=True)
    task_result_parser.add_argument("--evidence", action="append", default=[])
    task_result_parser.add_argument("--limitation", action="append", default=[])
    task_result_parser.add_argument("--open-question", action="append", default=[])
    task_result_parser.add_argument("--executor", required=True)
    task_result_parser.add_argument("--root", default=".")

    task_review_parser = workspace_task_subparsers.add_parser(
        "review-result", help="bind ARCHITECT review to the exact result"
    )
    task_review_parser.add_argument("task_id")
    task_review_parser.add_argument("--result-digest", required=True)
    task_review_parser.add_argument("--outcome", required=True, choices=("PASS", "RETURN"))
    task_review_parser.add_argument("--finding", action="append", required=True)
    task_review_parser.add_argument("--architect", required=True)
    task_review_parser.add_argument("--root", default=".")

    task_accept_parser = workspace_task_subparsers.add_parser(
        "accept-result", help="register exact local OWNER acceptance or return"
    )
    task_accept_parser.add_argument("task_id")
    task_accept_parser.add_argument("--result-digest", required=True)
    task_accept_parser.add_argument("--review-digest", required=True)
    task_accept_parser.add_argument("--decision", required=True, choices=("ACCEPT", "RETURN"))
    task_accept_parser.add_argument("--owner", required=True)
    task_accept_parser.add_argument("--root", default=".")

    task_close_parser = workspace_task_subparsers.add_parser(
        "close", help="write closure evidence only after OWNER acceptance"
    )
    task_close_parser.add_argument("task_id")
    task_close_parser.add_argument("--architect", required=True)
    task_close_parser.add_argument("--root", default=".")

    task_status_parser = workspace_task_subparsers.add_parser(
        "status", help="verify record chain, inputs, artifacts, and current gate"
    )
    task_status_parser.add_argument("task_id")
    task_status_parser.add_argument("--root", default=".")

    task_attempt_parser = workspace_task_subparsers.add_parser(
        "record-attempt", help="register one manual failed attempt; never automatic"
    )
    task_attempt_parser.add_argument("task_id")
    task_attempt_parser.add_argument("--error-code", required=True)
    task_attempt_parser.add_argument("--error-signature", required=True)
    task_attempt_parser.add_argument("--new-basis", required=True)
    task_attempt_parser.add_argument("--executor", required=True)
    task_attempt_parser.add_argument("--root", default=".")

    task_cancel_parser = workspace_task_subparsers.add_parser(
        "cancel", help="end a non-terminal task with an OWNER statement"
    )
    task_cancel_parser.add_argument("task_id")
    task_cancel_parser.add_argument("--reason", required=True)
    task_cancel_parser.add_argument("--owner", required=True)
    task_cancel_parser.add_argument("--root", default=".")

    task_supersede_parser = workspace_task_subparsers.add_parser(
        "supersede", help="identify a replacement task ID with an OWNER statement"
    )
    task_supersede_parser.add_argument("task_id")
    task_supersede_parser.add_argument("--replacement-task-id", required=True)
    task_supersede_parser.add_argument("--reason", required=True)
    task_supersede_parser.add_argument("--owner", required=True)
    task_supersede_parser.add_argument("--root", default=".")
    return parser


def init_project(project_root: Path) -> int:
    """Create the initial configuration without overwriting user data."""
    destination = project_root / "opencntx.toml"
    try:
        with destination.open("x", encoding="utf-8", newline="\n") as config_file:
            config_file.write(CONFIG_TEMPLATE)
    except FileExistsError:
        print(
            f"Error: {destination.name} already exists; nothing was overwritten.",
            file=sys.stderr,
        )
        return 2
    except OSError as exc:
        print(f"Error: could not create {destination}: {exc}", file=sys.stderr)
        return 2

    print(f"Created: {destination}")
    return 0


def _print_task_result(root: Path, result: object) -> None:
    resolved_root = root.resolve(strict=True)
    task_path = result.task_path.relative_to(resolved_root).as_posix()
    print(f"{result.status}: {result.task_id} revision {result.revision}")
    print(f"Task status: {result.task_status}")
    print(f"Object digest: {result.object_digest}")
    print(f"Record digest: {result.record_digest}")
    print(f"Task card: {task_path}")
    if result.receipt_path is not None:
        receipt = result.receipt_path.relative_to(resolved_root).as_posix()
        print(f"Receipt: {receipt}")
    print(
        "Actor ID is a local statement, not cryptographic identity evidence."
    )


def _print_media_result(root: Path, result: object) -> None:
    resolved_root = root.resolve(strict=True)
    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
    print(f"{result.status}: {result.source_id} / {result.derivation_id}")
    print(f"Derived SHA-256: {result.content_sha256}")
    print(f"Record-SHA-256: {result.record_sha256}")
    if result.promoted_source_id is not None:
        print(f"Promoted source: {result.promoted_source_id}")
    print(f"Receipt: {receipt}")
    print("Derived text is not automatically fact or OWNER-approved knowledge.")


def _print_definition_result(root: Path, result: object) -> None:
    resolved_root = root.resolve(strict=True)
    definition = result.definition_path.relative_to(resolved_root).as_posix()
    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
    print(
        f"{result.status}: {result.definition_type} {result.definition_id} "
        f"revision {result.revision}"
    )
    print(f"Definition-SHA-256: {result.definition_digest}")
    print(f"Document-SHA-256: {result.document_digest}")
    print(f"Document: {definition}")
    print(f"Receipt: {receipt}")
    print("Actor ID is a local statement, not cryptographic identity evidence.")


def _print_definition_status(result: object) -> None:
    print(
        f"{result.status}: {result.definition_type} {result.definition_id} "
        f"revision {result.revision}"
    )
    if result.definition_digest is not None:
        print(f"Definition-SHA-256: {result.definition_digest}")
    if result.document_digest is not None:
        print(f"Document-SHA-256: {result.document_digest}")
    if result.approval_digest is not None:
        print(f"Approvalrecord-SHA-256: {result.approval_digest}")
    for error in result.errors:
        print(f"Error: {error}")


def _configure_console_output() -> None:
    """Escape unsupported user characters instead of crashing narrow consoles."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(errors="backslashreplace", newline="\n")


def main(argv: Sequence[str] | None = None) -> int:
    """Run the OPENCNTX command-line interface."""
    _configure_console_output()
    args = build_parser().parse_args(argv)
    if args.command == "init":
        return init_project(Path.cwd())
    try:
        if args.command == "workspace":
            if args.workspace_command == "init":
                result = init_workspace(Path(args.project))
                if result.created:
                    print(f"Created: project workspace {result.root}")
                else:
                    print(f"Already exists: project workspace {result.root}; nothing changed.")
                return 0
            if args.workspace_command == "capture":
                root = Path(args.root)
                result = capture_source(
                    root,
                    Path(args.source),
                    privacy=args.privacy,
                    origin=args.origin,
                    supersedes=args.supersedes,
                )
                resolved_root = root.resolve(strict=True)
                receipt = result.receipt_path.relative_to(resolved_root).as_posix()
                print(
                    f"{result.status}: {result.source_id} "
                    f"({result.byte_count} bytes, SHA-256 {result.sha256})"
                )
                print(f"Receipt: {receipt}")
                return 0
            if args.workspace_command == "doctor":
                report = doctor_workspace(Path(args.root))
                print(format_doctor_report(report))
                return 0 if report.ok else 1
            if args.workspace_command == "recover":
                plan = recover_workspace(
                    Path(args.root),
                    args.transaction,
                    args.intent_sha256,
                    apply=args.apply,
                )
                print(format_recovery_plan(plan, applied=args.apply))
                return 0
            if args.workspace_command == "control":
                if args.workspace_control_command == "refresh":
                    root = Path(args.root)
                    result = refresh_control_snapshot(root)
                    resolved_root = root.resolve(strict=True)
                    assert result.receipt_path is not None
                    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
                    print(f"{result.status}: {result.mode}")
                    print(f"Roadmap-SHA-256: {result.roadmap_sha256}")
                    if result.block_sha256 is not None:
                        print(
                            f"Control block: {result.block_bytes} bytes, "
                            f"SHA-256 {result.block_sha256}"
                        )
                    if result.snapshot_sha256 is not None:
                        print(f"Snapshot-SHA-256: {result.snapshot_sha256}")
                    if result.snapshot_path is not None:
                        snapshot = result.snapshot_path.relative_to(resolved_root).as_posix()
                        print(f"Snapshot: {snapshot}")
                    print(f"Receipt: {receipt}")
                    print("Derived evidence; this grants no OWNER authority.")
                    return 0
                return 2
            if args.workspace_command == "chapter":
                if args.workspace_chapter_command == "create":
                    root = Path(args.root)
                    result = create_chapter(
                        root,
                        args.chapter_id,
                        title=args.title,
                        scope=args.scope,
                        source_ids=args.source,
                        dependency_ids=args.depends_on,
                    )
                    resolved_root = root.resolve(strict=True)
                    chapter = result.chapter_path.relative_to(resolved_root).as_posix()
                    print(f"{result.status}: {result.chapter_id}")
                    print(f"Chapter: {chapter}")
                    print("Status: DRAFT; this grants no OWNER approval.")
                    return 0
            if args.workspace_command == "catalog":
                if args.workspace_catalog_command == "rebuild":
                    root = Path(args.root)
                    result = rebuild_catalog(root)
                    resolved_root = root.resolve(strict=True)
                    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
                    counts = result.freshness_counts
                    print(
                        f"{result.status}: {result.chapter_count} chapters, "
                        f"{result.source_count} sources"
                    )
                    print(
                        "Freshness: "
                        f"CURRENT={counts['CURRENT']}, STALE={counts['STALE']}, "
                        f"INCOMPLETE={counts['INCOMPLETE']}, "
                        f"ARCHIVED={counts['ARCHIVED']}"
                    )
                    print(f"State-digest: {result.state_digest}")
                    print(f"Receipt: {receipt}")
                    return 0
            if args.workspace_command == "media":
                root = Path(args.root)
                if args.workspace_media_command == "register":
                    result = register_derivation(
                        root,
                        args.source_id,
                        Path(args.text),
                        kind=args.kind,
                        producer_class=args.producer_class,
                        producer=args.producer,
                        locators=args.locator,
                        supersedes_derivation_id=args.supersedes_derivation_id,
                    )
                    _print_media_result(root, result)
                    return 0
                if args.workspace_media_command == "review":
                    result = review_derivation(
                        root,
                        args.source_id,
                        args.derivation_id,
                        content_sha256=args.content_sha256,
                        decision=args.decision,
                        findings=args.finding,
                        reviewer=args.reviewer,
                    )
                    _print_media_result(root, result)
                    return 0
                if args.workspace_media_command == "promote":
                    result = promote_derivation(
                        root,
                        args.source_id,
                        args.derivation_id,
                        review_digest=args.review_digest,
                    )
                    _print_media_result(root, result)
                    return 0
                if args.workspace_media_command == "status":
                    entries = media_status(root, args.source_id, args.derivation_id)
                    for entry in entries:
                        identity = entry.derivation_id or entry.source_id
                        print(f"{entry.status}: {identity}")
                        print(entry.statement)
                        if entry.content_sha256 is not None:
                            print(f"Derived SHA-256: {entry.content_sha256}")
                        if entry.record_sha256 is not None:
                            print(f"Record-SHA-256: {entry.record_sha256}")
                        if entry.review_sha256 is not None:
                            print(f"Review-SHA-256: {entry.review_sha256}")
                        if entry.promoted_source_id is not None:
                            print(f"Promoted source: {entry.promoted_source_id}")
                    return 0
                if args.workspace_media_command == "verify":
                    report = verify_media(root, args.source_id, args.derivation_id)
                    print(format_media_verify_report(report))
                    return 0 if report.ok else 1
                if args.workspace_media_command == "remove":
                    result = remove_derivation(
                        root,
                        args.source_id,
                        args.derivation_id,
                        record_digest=args.record_digest,
                        content_sha256=args.content_sha256,
                        owner=args.owner,
                    )
                    _print_media_result(root, result)
                    return 0
                return 2
            if args.workspace_command == "playbook":
                root = Path(args.root)
                if args.workspace_playbook_command == "register":
                    result = register_playbook(
                        root,
                        args.playbook_id,
                        revision=args.revision,
                        title=args.title,
                        purpose=args.purpose,
                        inputs=args.input,
                        steps=args.step,
                        stop_conditions=args.stop,
                        evidence_requirements=args.evidence,
                        allowed_actions=args.allow,
                        forbidden_actions=args.forbid,
                        architect=args.architect,
                        supersedes_digest=args.supersedes_digest,
                    )
                    _print_definition_result(root, result)
                    return 0
                if args.workspace_playbook_command == "approve":
                    result = approve_playbook(
                        root,
                        args.playbook_id,
                        revision=args.revision,
                        definition_digest=args.definition_digest,
                        owner=args.owner,
                    )
                    _print_definition_result(root, result)
                    return 0
                if args.workspace_playbook_command == "status":
                    result = playbook_status(root, args.playbook_id, args.revision)
                    _print_definition_status(result)
                    return 0 if not result.errors else 1
                if args.workspace_playbook_command == "verify":
                    report = verify_playbook(root, args.playbook_id, args.revision)
                    print(format_definition_verify_report(report))
                    return 0 if report.ok else 1
                return 2
            if args.workspace_command == "role":
                root = Path(args.root)
                if args.workspace_role_command == "register":
                    result = register_role(
                        root,
                        args.role_id,
                        revision=args.revision,
                        title=args.title,
                        responsibilities=args.responsibility,
                        allowed_actions=args.allow,
                        forbidden_actions=args.forbid,
                        handoff=args.handoff,
                        architect=args.architect,
                        supersedes_digest=args.supersedes_digest,
                    )
                    _print_definition_result(root, result)
                    return 0
                if args.workspace_role_command == "approve":
                    result = approve_role(
                        root,
                        args.role_id,
                        revision=args.revision,
                        definition_digest=args.definition_digest,
                        owner=args.owner,
                    )
                    _print_definition_result(root, result)
                    return 0
                if args.workspace_role_command == "status":
                    result = role_status(root, args.role_id, args.revision)
                    _print_definition_status(result)
                    return 0 if not result.errors else 1
                if args.workspace_role_command == "verify":
                    report = verify_role(root, args.role_id, args.revision)
                    print(format_definition_verify_report(report))
                    return 0 if report.ok else 1
                return 2
            if args.workspace_command == "executor":
                root = Path(args.root)
                if args.workspace_executor_command == "prepare":
                    result = prepare_executor(
                        root,
                        args.task_id,
                        revision=args.revision,
                        proposal_digest=args.proposal_digest,
                        playbook_id=args.playbook_id,
                        playbook_revision=args.playbook_revision,
                        playbook_digest=args.playbook_digest,
                        role_id=args.role_id,
                        role_revision=args.role_revision,
                        role_digest=args.role_digest,
                        context_manifest_digest=args.context_manifest_digest,
                        executor=args.executor,
                    )
                    resolved_root = root.resolve(strict=True)
                    assignment = result.assignment_path.relative_to(resolved_root).as_posix()
                    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
                    print(f"{result.status}: {result.task_id} / {result.executor_id}")
                    print(f"Record-SHA-256: {result.record_digest}")
                    print(f"Assignment: {assignment}")
                    print(f"Receipt: {receipt}")
                    print("No person, process, tool, model, or agent was started.")
                    return 0
                if args.workspace_executor_command == "status":
                    result = executor_status(root, args.task_id, args.executor_id)
                    print(f"{result.status}: {result.task_id} / {result.executor_id}")
                    if result.record_digest is not None:
                        print(f"Record-SHA-256: {result.record_digest}")
                    for error in result.errors:
                        print(f"Error: {error}")
                    return 0 if not result.errors else 1
                if args.workspace_executor_command == "verify":
                    report = verify_executor(root, args.task_id, args.executor_id)
                    print(format_executor_verify_report(report))
                    return 0 if report.ok else 1
                return 2
            if args.workspace_command == "context":
                root = Path(args.root)
                if args.workspace_context_command == "build":
                    result = build_context_package(
                        root,
                        args.task_id,
                        proposal_digest=args.proposal_digest,
                        max_files=args.max_files,
                        max_bytes=args.max_bytes,
                    )
                    resolved_root = root.resolve(strict=True)
                    package = result.package_path.relative_to(resolved_root).as_posix()
                    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
                    print(
                        f"{result.status}: {result.task_id} revision {result.revision} "
                        f"({result.file_count} files, {result.total_bytes} bytes)"
                    )
                    print(f"Package: {package}")
                    print(f"Context-SHA-256: {result.context_digest}")
                    print(f"Manifest-SHA-256: {result.manifest_digest}")
                    print(f"Receipt: {receipt}")
                    print("Built locally; this does not grant permission for external sharing.")
                    return 0
                if args.workspace_context_command == "verify":
                    report = verify_context_package(
                        root,
                        args.task_id,
                        proposal_digest=args.proposal_digest,
                    )
                    print(format_context_verify_report(report))
                    return 0 if report.ok else 1
                return 2
            if args.workspace_command == "task":
                root = Path(args.root)
                if args.workspace_task_command == "propose":
                    result = propose_task(
                        root,
                        args.task_id,
                        title=args.title,
                        goal=args.goal,
                        definition_of_done=args.done,
                        executor_role=args.executor_role,
                        input_paths=args.input,
                        allowed_actions=args.allow,
                        forbidden_actions=args.forbid,
                        expected_output=args.expected_output,
                        acceptance_criteria=args.acceptance,
                        architect=args.architect,
                    )
                elif args.workspace_task_command == "approve":
                    result = approve_task(
                        root,
                        args.task_id,
                        revision=args.revision,
                        proposal_digest=args.proposal_digest,
                        owner=args.owner,
                    )
                elif args.workspace_task_command == "begin":
                    result = begin_task(root, args.task_id, architect=args.architect)
                elif args.workspace_task_command == "submit-result":
                    result = submit_result(
                        root,
                        args.task_id,
                        result_path=Path(args.result),
                        evidence_paths=[Path(path) for path in args.evidence],
                        limitations=args.limitation,
                        open_questions=args.open_question,
                        executor=args.executor,
                    )
                elif args.workspace_task_command == "review-result":
                    result = review_result(
                        root,
                        args.task_id,
                        result_digest=args.result_digest,
                        outcome=args.outcome,
                        findings=args.finding,
                        architect=args.architect,
                    )
                elif args.workspace_task_command == "accept-result":
                    result = accept_result(
                        root,
                        args.task_id,
                        result_digest=args.result_digest,
                        review_digest=args.review_digest,
                        decision=args.decision,
                        owner=args.owner,
                    )
                elif args.workspace_task_command == "close":
                    result = close_task(root, args.task_id, architect=args.architect)
                elif args.workspace_task_command == "status":
                    result = task_status(root, args.task_id)
                elif args.workspace_task_command == "record-attempt":
                    result = record_attempt(
                        root,
                        args.task_id,
                        error_code=args.error_code,
                        error_signature=args.error_signature,
                        new_basis=args.new_basis,
                        executor=args.executor,
                    )
                elif args.workspace_task_command == "cancel":
                    result = cancel_task(
                        root, args.task_id, reason=args.reason, owner=args.owner
                    )
                elif args.workspace_task_command == "supersede":
                    result = supersede_task(
                        root,
                        args.task_id,
                        replacement_task_id=args.replacement_task_id,
                        reason=args.reason,
                        owner=args.owner,
                    )
                else:
                    return 2
                _print_task_result(root, result)
                return 0
        if args.command == "pack":
            allowed_secret_ids = tuple(args.allow_secret)
            if args.preview:
                plan = plan_project(
                    Path.cwd(),
                    allowed_secret_ids=allowed_secret_ids,
                )
                print(format_pack_preview(plan))
                return 2 if plan.security.blocked else 0
            package_path, manifest = pack_project(
                Path.cwd(),
                allowed_secret_ids=allowed_secret_ids,
            )
            print(
                f"Created: {package_path} "
                f"({manifest['package']['file_count']} files, "
                f"{manifest['package']['total_bytes']} bytes)"
            )
            for finding in manifest["security"]["warnings"]:
                print(
                    "Secret policy warning: "
                    f"{finding['finding_id']} {finding['path']}:"
                    f"{finding['line']}:{finding['column']} "
                    f"{finding['rule_id']} {finding['confidence']}",
                    file=sys.stderr,
                )
            return 0
        if args.command == "verify":
            package_argument = args.package.replace("\\", os.sep)
            report = verify_package(Path(package_argument))
            print(format_verify_report(report))
            return 0 if report.ok else 1
    except (IntegrityError, OpenCntxError, WorkspaceError) as exc:
        detail = (
            f"operation failed ({exc.code})"
            if isinstance(exc, (IntegrityError, WorkspaceError))
            else str(exc)
        )
        print(f"Error: {detail}", file=sys.stderr)
        return 2
    return 2
