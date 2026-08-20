"""Definition and executor command parsers and dispatch for OPENCNTX."""

from __future__ import annotations

import argparse
from pathlib import Path

from .playbook import (
    DefinitionMutationResult,
    DefinitionStatus,
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


def register_playbook_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "playbook",
        help="register and approve non-executing playbook revisions",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_playbook_command",
        required=True,
    )
    register = subparsers.add_parser(
        "register",
        help="register one immutable proposed playbook revision",
    )
    register.add_argument("playbook_id")
    register.add_argument("--revision", required=True, type=int)
    register.add_argument("--title", required=True)
    register.add_argument("--purpose", required=True)
    register.add_argument("--input", action="append", required=True)
    register.add_argument("--step", action="append", required=True)
    register.add_argument("--stop", action="append", required=True)
    register.add_argument("--evidence", action="append", required=True)
    register.add_argument("--allow", action="append", required=True)
    register.add_argument("--forbid", action="append", required=True)
    register.add_argument("--architect", required=True)
    register.add_argument("--supersedes-digest")
    register.add_argument("--root", default=".")

    approve = subparsers.add_parser(
        "approve",
        help="bind a local OWNER approval to one exact playbook revision",
    )
    approve.add_argument("playbook_id")
    approve.add_argument("--revision", required=True, type=int)
    approve.add_argument("--definition-digest", required=True)
    approve.add_argument("--owner", required=True)
    approve.add_argument("--root", default=".")
    _register_definition_queries(subparsers, "playbook_id", "playbook")


def _register_definition_queries(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    identifier: str,
    label: str,
) -> None:
    for command_name, help_text in (
        ("status", f"show the computed {label} status without writing"),
        ("verify", f"verify {label} bytes and approval fully read-only"),
    ):
        parser = subparsers.add_parser(command_name, help=help_text)
        parser.add_argument(identifier)
        parser.add_argument("--revision", required=True, type=int)
        parser.add_argument("--root", default=".")


def register_role_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "role",
        help="register bounded role revisions without OWNER authority",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_role_command",
        required=True,
    )
    register = subparsers.add_parser(
        "register",
        help="register one immutable proposed role revision",
    )
    register.add_argument("role_id")
    register.add_argument("--revision", required=True, type=int)
    register.add_argument("--title", required=True)
    register.add_argument("--responsibility", action="append", required=True)
    register.add_argument("--allow", action="append", required=True)
    register.add_argument("--forbid", action="append", required=True)
    register.add_argument("--handoff", required=True)
    register.add_argument("--architect", required=True)
    register.add_argument("--supersedes-digest")
    register.add_argument("--root", default=".")

    approve = subparsers.add_parser(
        "approve",
        help="bind a local OWNER approval to one exact role revision",
    )
    approve.add_argument("role_id")
    approve.add_argument("--revision", required=True, type=int)
    approve.add_argument("--definition-digest", required=True)
    approve.add_argument("--owner", required=True)
    approve.add_argument("--root", default=".")
    _register_definition_queries(subparsers, "role_id", "role")


def register_executor_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "executor",
        help="create or verify one non-executing task-bound executor package",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_executor_command",
        required=True,
    )
    prepare = subparsers.add_parser(
        "prepare",
        help="bind task, context, playbook, and role without starting an executor",
    )
    prepare.add_argument("task_id")
    prepare.add_argument("--revision", required=True, type=int)
    prepare.add_argument("--proposal-digest", required=True)
    prepare.add_argument("--playbook-id", required=True)
    prepare.add_argument("--playbook-revision", required=True, type=int)
    prepare.add_argument("--playbook-digest", required=True)
    prepare.add_argument("--role-id", required=True)
    prepare.add_argument("--role-revision", required=True, type=int)
    prepare.add_argument("--role-digest", required=True)
    prepare.add_argument("--context-manifest-digest", required=True)
    prepare.add_argument("--executor", required=True)
    prepare.add_argument("--root", default=".")
    for command_name, help_text in (
        ("status", "show the current executor package status without writing"),
        ("verify", "verify all task, context, and definition bindings read-only"),
    ):
        command = subparsers.add_parser(command_name, help=help_text)
        command.add_argument("task_id")
        command.add_argument("executor_id")
        command.add_argument("--root", default=".")


def _print_definition_result(root: Path, result: DefinitionMutationResult) -> None:
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


def _print_definition_status(result: DefinitionStatus) -> None:
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


def dispatch_playbook(args: argparse.Namespace) -> int:
    root = Path(args.root)
    command = args.workspace_playbook_command
    if command == "register":
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
    if command == "approve":
        result = approve_playbook(
            root,
            args.playbook_id,
            revision=args.revision,
            definition_digest=args.definition_digest,
            owner=args.owner,
        )
        _print_definition_result(root, result)
        return 0
    if command == "status":
        status = playbook_status(root, args.playbook_id, args.revision)
        _print_definition_status(status)
        return 0 if not status.errors else 1
    if command == "verify":
        report = verify_playbook(root, args.playbook_id, args.revision)
        print(format_definition_verify_report(report))
        return 0 if report.ok else 1
    return 2


def dispatch_role(args: argparse.Namespace) -> int:
    root = Path(args.root)
    command = args.workspace_role_command
    if command == "register":
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
    if command == "approve":
        result = approve_role(
            root,
            args.role_id,
            revision=args.revision,
            definition_digest=args.definition_digest,
            owner=args.owner,
        )
        _print_definition_result(root, result)
        return 0
    if command == "status":
        status = role_status(root, args.role_id, args.revision)
        _print_definition_status(status)
        return 0 if not status.errors else 1
    if command == "verify":
        report = verify_role(root, args.role_id, args.revision)
        print(format_definition_verify_report(report))
        return 0 if report.ok else 1
    return 2


def dispatch_executor(args: argparse.Namespace) -> int:
    root = Path(args.root)
    command = args.workspace_executor_command
    if command == "prepare":
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
    if command == "status":
        status = executor_status(root, args.task_id, args.executor_id)
        print(f"{status.status}: {status.task_id} / {status.executor_id}")
        if status.record_digest is not None:
            print(f"Record-SHA-256: {status.record_digest}")
        for error in status.errors:
            print(f"Error: {error}")
        return 0 if not status.errors else 1
    if command == "verify":
        report = verify_executor(root, args.task_id, args.executor_id)
        print(format_executor_verify_report(report))
        return 0 if report.ok else 1
    return 2
