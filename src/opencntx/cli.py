"""Command-line interface for OPENCNTX."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
import os
from pathlib import Path
import sys

from .catalog import create_chapter, rebuild_catalog
from .core import (
    OpenCntxError,
    format_verify_report,
    pack_project,
    verify_package,
)
from .navigator import (
    build_context_package,
    format_context_verify_report,
    verify_context_package,
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
goal = "Beschrijf de ene concrete taak"

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
        description=(
            "Maak een klein, expliciet en controleerbaar contextpakket voor één AI-taak."
        ),
        epilog=(
            "Bestaande kerncommando's: {init,pack,verify}. "
            "Optionele lokale opslag: workspace."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "init",
        help="maak veilig een opencntx.toml-sjabloon in de huidige map",
    )
    subparsers.add_parser(
        "pack",
        help="maak atomair CONTEXT.md en manifest.json uit de gekozen bronnen",
    )
    verify_parser = subparsers.add_parser(
        "verify",
        help="controleer een pakket op gewijzigde, ontbrekende en nieuwe bronnen",
    )
    verify_parser.add_argument("package", help="pakketmap, bijvoorbeeld .opencntx/latest")
    workspace_parser = subparsers.add_parser(
        "workspace",
        help="lokale opslag, catalogus, taakgates en begrensde contextnavigatie",
    )
    workspace_subparsers = workspace_parser.add_subparsers(
        dest="workspace_command",
        required=True,
    )
    workspace_init_parser = workspace_subparsers.add_parser(
        "init",
        help="maak veilig de vaste projectwerkruimtestructuur",
    )
    workspace_init_parser.add_argument(
        "project",
        nargs="?",
        default=".",
        help="projectmap; standaard de huidige map",
    )
    workspace_capture_parser = workspace_subparsers.add_parser(
        "capture",
        help="bewaar één regulier lokaal bestand zonder het uit te voeren",
    )
    workspace_capture_parser.add_argument("source", help="het lokale bronbestand")
    workspace_capture_parser.add_argument(
        "--root",
        default=".",
        help="projectwerkruimte; standaard de huidige map",
    )
    workspace_capture_parser.add_argument(
        "--privacy",
        choices=PRIVACY_LABELS,
        default="PRIVATE",
        help="privacylabel; standaard PRIVATE",
    )
    workspace_capture_parser.add_argument(
        "--origin",
        help="korte herkomst in één regel",
    )
    workspace_capture_parser.add_argument(
        "--supersedes",
        help="optionele bestaande source-ID die deze nieuwe bron vervangt",
    )
    workspace_chapter_parser = workspace_subparsers.add_parser(
        "chapter",
        help="maak een veilig, nog niet goedgekeurd hoofdstuksjabloon",
    )
    workspace_chapter_subparsers = workspace_chapter_parser.add_subparsers(
        dest="workspace_chapter_command",
        required=True,
    )
    workspace_chapter_create_parser = workspace_chapter_subparsers.add_parser(
        "create",
        help="maak één nieuw DRAFT-hoofdstuk zonder iets te overschrijven",
    )
    workspace_chapter_create_parser.add_argument(
        "chapter_id",
        help="stabiele hoofdstuk-ID, bijvoorbeeld CH-ELEKTRICITEIT",
    )
    workspace_chapter_create_parser.add_argument(
        "--title",
        required=True,
        help="korte leesbare hoofdstuktitel",
    )
    workspace_chapter_create_parser.add_argument(
        "--scope",
        default="UNKNOWN — door OWNER en ARCHITECT te bepalen.",
        help="korte grens van het onderwerp",
    )
    workspace_chapter_create_parser.add_argument(
        "--source",
        action="append",
        default=[],
        help="bestaande exacte source-ID; optie mag worden herhaald",
    )
    workspace_chapter_create_parser.add_argument(
        "--depends-on",
        action="append",
        default=[],
        help="bestaande hoofdstuk-ID; optie mag worden herhaald",
    )
    workspace_chapter_create_parser.add_argument(
        "--root",
        default=".",
        help="projectwerkruimte; standaard de huidige map",
    )
    workspace_catalog_parser = workspace_subparsers.add_parser(
        "catalog",
        help="herbouw de menselijke index en lokale SQLite-catalogus",
    )
    workspace_catalog_subparsers = workspace_catalog_parser.add_subparsers(
        dest="workspace_catalog_command",
        required=True,
    )
    workspace_catalog_rebuild_parser = workspace_catalog_subparsers.add_parser(
        "rebuild",
        help="herbouw catalogus en index uit officiële werkruimtebestanden",
    )
    workspace_catalog_rebuild_parser.add_argument(
        "--root",
        default=".",
        help="projectwerkruimte; standaard de huidige map",
    )
    workspace_context_parser = workspace_subparsers.add_parser(
        "context",
        help="bouw of controleer één taakgebonden heet-warm-koudpakket",
    )
    workspace_context_subparsers = workspace_context_parser.add_subparsers(
        dest="workspace_context_command",
        required=True,
    )
    workspace_context_build_parser = workspace_context_subparsers.add_parser(
        "build",
        help="maak lokaal context voor één goedgekeurde taak in uitvoering",
    )
    workspace_context_build_parser.add_argument("task_id")
    workspace_context_build_parser.add_argument("--proposal-digest", required=True)
    workspace_context_build_parser.add_argument("--max-files", required=True, type=int)
    workspace_context_build_parser.add_argument("--max-bytes", required=True, type=int)
    workspace_context_build_parser.add_argument("--root", default=".")
    workspace_context_verify_parser = workspace_context_subparsers.add_parser(
        "verify",
        help="controleer pakketbytes en de volledige actuele taakroute read-only",
    )
    workspace_context_verify_parser.add_argument("task_id")
    workspace_context_verify_parser.add_argument("--proposal-digest", required=True)
    workspace_context_verify_parser.add_argument("--root", default=".")
    workspace_task_parser = workspace_subparsers.add_parser(
        "task",
        help="registreer één begrensde taak met exacte OWNER-gates",
    )
    workspace_task_subparsers = workspace_task_parser.add_subparsers(
        dest="workspace_task_command",
        required=True,
    )
    task_propose_parser = workspace_task_subparsers.add_parser(
        "propose",
        help="maak één taakvoorstel dat exact op OWNER-goedkeuring wacht",
    )
    task_propose_parser.add_argument("task_id", help="taak-ID, bijvoorbeeld TASK-20260816-0001")
    task_propose_parser.add_argument("--title", required=True, help="korte taaktitel")
    task_propose_parser.add_argument("--goal", required=True, help="één begrensd doel")
    task_propose_parser.add_argument(
        "--done", required=True, help="exacte Definition of Done"
    )
    task_propose_parser.add_argument(
        "--executor-role", required=True, help="begrensde uitvoerderrol"
    )
    task_propose_parser.add_argument(
        "--input", action="append", required=True, help="officieel relatief inputpad; herhaalbaar"
    )
    task_propose_parser.add_argument(
        "--allow", action="append", required=True, help="toegestane actie; herhaalbaar"
    )
    task_propose_parser.add_argument(
        "--forbid", action="append", required=True, help="verboden actie; herhaalbaar"
    )
    task_propose_parser.add_argument(
        "--expected-output", required=True, help="verwachte resultaatvorm"
    )
    task_propose_parser.add_argument(
        "--acceptance", action="append", required=True, help="acceptatiecriterium; herhaalbaar"
    )
    task_propose_parser.add_argument(
        "--architect", required=True, help="lokale ARCHITECT-actorverklaring"
    )
    task_propose_parser.add_argument("--root", default=".", help="projectwerkruimte")

    task_approve_parser = workspace_task_subparsers.add_parser(
        "approve", help="registreer een exacte lokale OWNER-goedkeuring"
    )
    task_approve_parser.add_argument("task_id")
    task_approve_parser.add_argument("--revision", required=True, type=int)
    task_approve_parser.add_argument("--proposal-digest", required=True)
    task_approve_parser.add_argument("--owner", required=True)
    task_approve_parser.add_argument("--root", default=".")

    task_begin_parser = workspace_task_subparsers.add_parser(
        "begin", help="registreer uitvoering zonder een proces of agent te starten"
    )
    task_begin_parser.add_argument("task_id")
    task_begin_parser.add_argument("--architect", required=True)
    task_begin_parser.add_argument("--root", default=".")

    task_result_parser = workspace_task_subparsers.add_parser(
        "submit-result", help="bewaar één resultaat en optioneel bewijs als bytes"
    )
    task_result_parser.add_argument("task_id")
    task_result_parser.add_argument("--result", required=True)
    task_result_parser.add_argument("--evidence", action="append", default=[])
    task_result_parser.add_argument("--limitation", action="append", default=[])
    task_result_parser.add_argument("--open-question", action="append", default=[])
    task_result_parser.add_argument("--executor", required=True)
    task_result_parser.add_argument("--root", default=".")

    task_review_parser = workspace_task_subparsers.add_parser(
        "review-result", help="bind ARCHITECT-controle aan het exacte resultaat"
    )
    task_review_parser.add_argument("task_id")
    task_review_parser.add_argument("--result-digest", required=True)
    task_review_parser.add_argument("--outcome", required=True, choices=("PASS", "RETURN"))
    task_review_parser.add_argument("--finding", action="append", required=True)
    task_review_parser.add_argument("--architect", required=True)
    task_review_parser.add_argument("--root", default=".")

    task_accept_parser = workspace_task_subparsers.add_parser(
        "accept-result", help="registreer exacte lokale OWNER-aanvaarding of retour"
    )
    task_accept_parser.add_argument("task_id")
    task_accept_parser.add_argument("--result-digest", required=True)
    task_accept_parser.add_argument("--review-digest", required=True)
    task_accept_parser.add_argument("--decision", required=True, choices=("ACCEPT", "RETURN"))
    task_accept_parser.add_argument("--owner", required=True)
    task_accept_parser.add_argument("--root", default=".")

    task_close_parser = workspace_task_subparsers.add_parser(
        "close", help="schrijf alleen na OWNER-aanvaarding het afrondingsbewijs"
    )
    task_close_parser.add_argument("task_id")
    task_close_parser.add_argument("--architect", required=True)
    task_close_parser.add_argument("--root", default=".")

    task_status_parser = workspace_task_subparsers.add_parser(
        "status", help="controleer recordketen, inputs, artifacts en actuele gate"
    )
    task_status_parser.add_argument("task_id")
    task_status_parser.add_argument("--root", default=".")

    task_attempt_parser = workspace_task_subparsers.add_parser(
        "record-attempt", help="registreer één handmatige foutpoging; nooit automatisch"
    )
    task_attempt_parser.add_argument("task_id")
    task_attempt_parser.add_argument("--error-code", required=True)
    task_attempt_parser.add_argument("--error-signature", required=True)
    task_attempt_parser.add_argument("--new-basis", required=True)
    task_attempt_parser.add_argument("--executor", required=True)
    task_attempt_parser.add_argument("--root", default=".")

    task_cancel_parser = workspace_task_subparsers.add_parser(
        "cancel", help="beëindig een niet-terminale taak met een OWNER-verklaring"
    )
    task_cancel_parser.add_argument("task_id")
    task_cancel_parser.add_argument("--reason", required=True)
    task_cancel_parser.add_argument("--owner", required=True)
    task_cancel_parser.add_argument("--root", default=".")

    task_supersede_parser = workspace_task_subparsers.add_parser(
        "supersede", help="wijs met een OWNER-verklaring een vervangende taak-ID aan"
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
            f"Fout: {destination.name} bestaat al; er is niets overschreven.",
            file=sys.stderr,
        )
        return 2
    except OSError as exc:
        print(f"Fout: kon {destination} niet maken: {exc}", file=sys.stderr)
        return 2

    print(f"Gemaakt: {destination}")
    return 0


def _print_task_result(root: Path, result: object) -> None:
    resolved_root = root.resolve(strict=True)
    task_path = result.task_path.relative_to(resolved_root).as_posix()
    print(f"{result.status}: {result.task_id} revisie {result.revision}")
    print(f"Taakstatus: {result.task_status}")
    print(f"Objectdigest: {result.object_digest}")
    print(f"Recorddigest: {result.record_digest}")
    print(f"Taakkaart: {task_path}")
    if result.receipt_path is not None:
        receipt = result.receipt_path.relative_to(resolved_root).as_posix()
        print(f"Ontvangstbewijs: {receipt}")
    print(
        "Actor-ID is een lokale verklaring, geen cryptografisch identiteitsbewijs."
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Run the OPENCNTX command-line interface."""
    args = build_parser().parse_args(argv)
    if args.command == "init":
        return init_project(Path.cwd())
    try:
        if args.command == "workspace":
            if args.workspace_command == "init":
                result = init_workspace(Path(args.project))
                if result.created:
                    print(f"Gemaakt: projectwerkruimte {result.root}")
                else:
                    print(f"Bestaat al: projectwerkruimte {result.root}; niets gewijzigd.")
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
                print(f"Ontvangstbewijs: {receipt}")
                return 0
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
                    print(f"Hoofdstuk: {chapter}")
                    print("Status: DRAFT; dit verleent geen OWNER-goedkeuring.")
                    return 0
            if args.workspace_command == "catalog":
                if args.workspace_catalog_command == "rebuild":
                    root = Path(args.root)
                    result = rebuild_catalog(root)
                    resolved_root = root.resolve(strict=True)
                    receipt = result.receipt_path.relative_to(resolved_root).as_posix()
                    counts = result.freshness_counts
                    print(
                        f"{result.status}: {result.chapter_count} hoofdstukken, "
                        f"{result.source_count} bronnen"
                    )
                    print(
                        "Freshness: "
                        f"CURRENT={counts['CURRENT']}, STALE={counts['STALE']}, "
                        f"INCOMPLETE={counts['INCOMPLETE']}, "
                        f"ARCHIVED={counts['ARCHIVED']}"
                    )
                    print(f"State-digest: {result.state_digest}")
                    print(f"Ontvangstbewijs: {receipt}")
                    return 0
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
                        f"{result.status}: {result.task_id} revisie {result.revision} "
                        f"({result.file_count} bestanden, {result.total_bytes} bytes)"
                    )
                    print(f"Pakket: {package}")
                    print(f"Context-SHA-256: {result.context_digest}")
                    print(f"Manifest-SHA-256: {result.manifest_digest}")
                    print(f"Ontvangstbewijs: {receipt}")
                    print("Lokaal gebouwd; dit geeft geen toestemming voor extern delen.")
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
            package_path, manifest = pack_project(Path.cwd())
            print(
                f"Gemaakt: {package_path} "
                f"({manifest['package']['file_count']} bestanden, "
                f"{manifest['package']['total_bytes']} bytes)"
            )
            return 0
        if args.command == "verify":
            package_argument = args.package.replace("\\", os.sep)
            report = verify_package(Path(package_argument))
            print(format_verify_report(report))
            return 0 if report.ok else 1
    except (OpenCntxError, WorkspaceError) as exc:
        print(f"Fout: {exc}", file=sys.stderr)
        return 2
    return 2
