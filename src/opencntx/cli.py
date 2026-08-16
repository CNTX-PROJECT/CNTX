"""Command-line interface for OPENCNTX."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
import os
from pathlib import Path
import sys

from .core import (
    OpenCntxError,
    format_verify_report,
    pack_project,
    verify_package,
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
        help="initialiseer lokale projectopslag of capture één bestand veilig",
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
