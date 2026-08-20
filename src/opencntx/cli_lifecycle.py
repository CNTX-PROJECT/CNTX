"""Lifecycle command parser and dispatch for OPENCNTX."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .lifecycle import (
    TRUST_PROFILES,
    apply_cleanup,
    apply_migration,
    format_cleanup_plan,
    format_lifecycle_status,
    format_migration_plan,
    lifecycle_status,
    plan_cleanup,
    plan_migration,
    restore_cleanup,
    write_plan,
)
from .workspace import WorkspaceError


def register_lifecycle_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Register the workspace lifecycle family."""
    parser = workspace_subparsers.add_parser(
        "lifecycle",
        help="audit local trust, storage, cleanup, schemas, and migration",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_lifecycle_command",
        required=True,
    )
    status = subparsers.add_parser(
        "status",
        help="show read-only trust, privacy, permission, and storage evidence",
    )
    status.add_argument(
        "--trust-profile",
        choices=TRUST_PROFILES,
        default="single-user-local",
    )
    status.add_argument("--json", action="store_true")
    status.add_argument("--root", default=".")

    migrate = subparsers.add_parser(
        "migrate",
        help="preview or apply exact registration of unchanged compatible v1 records",
    )
    mode = migrate.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    migrate.add_argument("--plan")
    migrate.add_argument("--plan-sha256")
    migrate.add_argument("--json", action="store_true")
    migrate.add_argument("--root", default=".")

    cleanup = subparsers.add_parser(
        "cleanup",
        help="preview or apply explicit allowlisted cleanup with an external checkpoint",
    )
    cleanup.add_argument("--target", action="append", default=[])
    cleanup.add_argument("--checkpoint")
    cleanup.add_argument("--write-plan")
    cleanup.add_argument("--apply", action="store_true")
    cleanup.add_argument("--plan")
    cleanup.add_argument("--plan-sha256")
    cleanup.add_argument("--root", default=".")

    restore = subparsers.add_parser(
        "restore",
        help="restore exact bytes from one verified external lifecycle checkpoint",
    )
    restore.add_argument("--checkpoint", required=True)
    restore.add_argument("--checkpoint-sha256", required=True)
    restore.add_argument("--root", default=".")


def _dispatch_status(args: argparse.Namespace, root: Path) -> int:
    report = lifecycle_status(root, args.trust_profile)
    if args.json:
        print(json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(format_lifecycle_status(report))
    return 0


def _dispatch_migrate(args: argparse.Namespace, root: Path) -> int:
    if args.dry_run:
        plan = plan_migration(root)
        if args.json:
            print(json.dumps(plan, ensure_ascii=True, indent=2, sort_keys=True))
        else:
            print(format_migration_plan(plan))
        return 0
    if not args.plan or not args.plan_sha256:
        raise WorkspaceError(
            "Migration apply requires --plan and --plan-sha256.",
            code="lifecycle_plan_required",
        )
    result = apply_migration(root, Path(args.plan), args.plan_sha256)
    print(f"Lifecycle migration: {result['status']}")
    print(f"Plan-SHA-256: {result['plan_sha256']}")
    return 0


def _dispatch_cleanup(args: argparse.Namespace, root: Path) -> int:
    if args.apply:
        invalid = (
            args.target
            or args.checkpoint
            or args.write_plan
            or not args.plan
            or not args.plan_sha256
        )
        if invalid:
            raise WorkspaceError(
                "Cleanup apply requires only --plan and --plan-sha256.",
                code="lifecycle_plan_required",
            )
        result = apply_cleanup(root, Path(args.plan), args.plan_sha256)
        print(f"Lifecycle cleanup: {result['status']}")
        print(f"Checkpoint: {result['checkpoint']}")
        print(f"Checkpoint-SHA-256: {result['checkpoint_sha256']}")
        print(f"Directory flush: {result['directory_flush']}")
        return 0

    if not args.target or not args.checkpoint or args.plan or args.plan_sha256:
        raise WorkspaceError(
            "Cleanup preview requires --target and --checkpoint.",
            code="lifecycle_cleanup_target_invalid",
        )
    plan = plan_cleanup(root, args.target, Path(args.checkpoint))
    if args.write_plan:
        write_plan(Path(args.write_plan), plan, workspace_root=root)
    print(format_cleanup_plan(plan))
    return 0


def dispatch_lifecycle(args: argparse.Namespace) -> int:
    """Dispatch one lifecycle command."""
    root = Path(args.root)
    command = args.workspace_lifecycle_command
    if command == "status":
        return _dispatch_status(args, root)
    if command == "migrate":
        return _dispatch_migrate(args, root)
    if command == "cleanup":
        return _dispatch_cleanup(args, root)
    if command == "restore":
        result = restore_cleanup(root, Path(args.checkpoint), args.checkpoint_sha256)
        print(f"Lifecycle restore: {result['status']}")
        print(f"Targets: {result['target_count']}")
        print(f"Checkpoint-SHA-256: {result['checkpoint_sha256']}")
        return 0
    return 2
