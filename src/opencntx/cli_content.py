"""Content command parsers and dispatch for OPENCNTX."""

from __future__ import annotations

import argparse
from pathlib import Path

from .catalog import create_chapter, rebuild_catalog
from .media import (
    DECISIONS,
    KINDS,
    PRODUCER_CLASSES,
    MediaMutationResult,
    format_media_verify_report,
    media_status,
    promote_derivation,
    register_derivation,
    remove_derivation,
    review_derivation,
    verify_media,
)
from .navigator import (
    build_context_package,
    format_context_verify_report,
    verify_context_package,
)


def register_chapter_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "chapter",
        help="create a safe chapter template that is not yet approved",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_chapter_command",
        required=True,
    )
    create = subparsers.add_parser(
        "create",
        help="create one new DRAFT chapter without overwriting anything",
    )
    create.add_argument(
        "chapter_id",
        help="stable chapter ID, for example CH-ELECTRICITY",
    )
    create.add_argument("--title", required=True, help="short readable chapter title")
    create.add_argument(
        "--scope",
        default="UNKNOWN - to be determined by OWNER and ARCHITECT.",
        help="short boundary of the subject",
    )
    create.add_argument(
        "--source",
        action="append",
        default=[],
        help="existing exact source ID; repeatable",
    )
    create.add_argument(
        "--depends-on",
        action="append",
        default=[],
        help="existing chapter ID; repeatable",
    )
    create.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )


def register_catalog_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "catalog",
        help="rebuild the human index and local SQLite catalog",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_catalog_command",
        required=True,
    )
    rebuild = subparsers.add_parser(
        "rebuild",
        help="rebuild the catalog and index from official workspace files",
    )
    rebuild.add_argument(
        "--root",
        default=".",
        help="project workspace; default: current directory",
    )


def register_media_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "media",
        help="register and verify text safely derived from media",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_media_command",
        required=True,
    )
    _register_media_mutations(subparsers)
    _register_media_queries(subparsers)


def _register_media_mutations(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    register = subparsers.add_parser(
        "register",
        help="register supplied UTF-8 text without starting OCR, AI, or another tool",
    )
    register.add_argument("source_id")
    register.add_argument("--text", required=True)
    register.add_argument("--kind", required=True, choices=KINDS)
    register.add_argument("--producer-class", required=True, choices=PRODUCER_CLASSES)
    register.add_argument("--producer", required=True)
    register.add_argument("--locator", action="append", default=[])
    register.add_argument("--supersedes-derivation-id")
    register.add_argument("--root", default=".")

    review = subparsers.add_parser(
        "review",
        help="review one exact derivation without accepting it as fact",
    )
    review.add_argument("source_id")
    review.add_argument("derivation_id")
    review.add_argument("--content-sha256", required=True)
    review.add_argument("--decision", required=True, choices=DECISIONS)
    review.add_argument("--finding", action="append", required=True)
    review.add_argument("--reviewer", required=True)
    review.add_argument("--root", default=".")

    promote = subparsers.add_parser(
        "promote",
        help="deliberately promote reviewed text to a regular CAPTURED source",
    )
    promote.add_argument("source_id")
    promote.add_argument("derivation_id")
    promote.add_argument("--review-digest", required=True)
    promote.add_argument("--root", default=".")


def _register_media_queries(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    status = subparsers.add_parser(
        "status",
        help="show whether media is unexamined, derived, reviewed, or removed",
    )
    status.add_argument("source_id")
    status.add_argument("derivation_id", nargs="?")
    status.add_argument("--root", default=".")

    verify = subparsers.add_parser(
        "verify",
        help="verify original, derived, and promotion bytes fully read-only",
    )
    verify.add_argument("source_id")
    verify.add_argument("derivation_id", nargs="?")
    verify.add_argument("--root", default=".")

    remove = subparsers.add_parser(
        "remove",
        help="remove only exactly pinned derived text and create a tombstone",
    )
    remove.add_argument("source_id")
    remove.add_argument("derivation_id")
    remove.add_argument("--record-digest", required=True)
    remove.add_argument("--content-sha256", required=True)
    remove.add_argument("--owner", required=True)
    remove.add_argument("--root", default=".")


def register_context_commands(
    workspace_subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = workspace_subparsers.add_parser(
        "context",
        help="build or verify one task-bound hot-warm-cold package",
    )
    subparsers = parser.add_subparsers(
        dest="workspace_context_command",
        required=True,
    )
    build = subparsers.add_parser(
        "build",
        help="build local context for one approved task in execution",
    )
    build.add_argument("task_id")
    build.add_argument("--proposal-digest", required=True)
    build.add_argument("--max-files", required=True, type=int)
    build.add_argument("--max-bytes", required=True, type=int)
    build.add_argument("--root", default=".")

    verify = subparsers.add_parser(
        "verify",
        help="verify package bytes and the complete current task route read-only",
    )
    verify.add_argument("task_id")
    verify.add_argument("--proposal-digest", required=True)
    verify.add_argument("--root", default=".")


def _print_media_result(root: Path, result: MediaMutationResult) -> None:
    resolved_root = root.resolve(strict=True)
    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
    print(f"{result.status}: {result.source_id} / {result.derivation_id}")
    print(f"Derived SHA-256: {result.content_sha256}")
    print(f"Record-SHA-256: {result.record_sha256}")
    if result.promoted_source_id is not None:
        print(f"Promoted source: {result.promoted_source_id}")
    print(f"Receipt: {receipt}")
    print("Derived text is not automatically fact or OWNER-approved knowledge.")


def dispatch_chapter(args: argparse.Namespace) -> int:
    root = Path(args.root)
    result = create_chapter(
        root,
        args.chapter_id,
        title=args.title,
        scope=args.scope,
        source_ids=args.source,
        dependency_ids=args.depends_on,
    )
    chapter = result.chapter_path.relative_to(root.resolve(strict=True)).as_posix()
    print(f"{result.status}: {result.chapter_id}")
    print(f"Chapter: {chapter}")
    print("Status: DRAFT; this grants no OWNER approval.")
    return 0


def dispatch_catalog(args: argparse.Namespace) -> int:
    root = Path(args.root)
    result = rebuild_catalog(root)
    receipt = result.receipt_path.relative_to(root.resolve(strict=True)).as_posix()
    counts = result.freshness_counts
    print(f"{result.status}: {result.chapter_count} chapters, {result.source_count} sources")
    print(
        "Freshness: "
        f"CURRENT={counts['CURRENT']}, STALE={counts['STALE']}, "
        f"INCOMPLETE={counts['INCOMPLETE']}, ARCHIVED={counts['ARCHIVED']}"
    )
    print(f"State-digest: {result.state_digest}")
    print(f"Receipt: {receipt}")
    return 0


def _dispatch_media_mutation(args: argparse.Namespace, root: Path) -> int | None:
    command = args.workspace_media_command
    if command == "register":
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
    elif command == "review":
        result = review_derivation(
            root,
            args.source_id,
            args.derivation_id,
            content_sha256=args.content_sha256,
            decision=args.decision,
            findings=args.finding,
            reviewer=args.reviewer,
        )
    elif command == "promote":
        result = promote_derivation(
            root,
            args.source_id,
            args.derivation_id,
            review_digest=args.review_digest,
        )
    elif command == "remove":
        result = remove_derivation(
            root,
            args.source_id,
            args.derivation_id,
            record_digest=args.record_digest,
            content_sha256=args.content_sha256,
            owner=args.owner,
        )
    else:
        return None
    _print_media_result(root, result)
    return 0


def dispatch_media(args: argparse.Namespace) -> int:
    root = Path(args.root)
    mutation = _dispatch_media_mutation(args, root)
    if mutation is not None:
        return mutation
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
    return 2


def dispatch_context(args: argparse.Namespace) -> int:
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
