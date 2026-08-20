"""Core command parser and dispatch for OPENCNTX."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from .core import (
    format_pack_preview,
    format_verify_report,
    pack_project,
    plan_project,
    verify_package,
)
from .lifecycle import require_disk_capacity
from .workspace import WorkspaceError

CONFIG_TEMPLATE = """[task]
goal = "Describe the one concrete task"

[context]
include = ["README.md", "src/**/*.py"]
required = ["README.md"]
exclude = [".git/**", ".env*", "**/*.key", "**/*.pem"]
max_files = 25
max_bytes = 100000
"""


def register_core_commands(
    subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    """Register the stable core command family."""
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


def init_project(project_root: Path) -> int:
    """Create the initial configuration without overwriting user data."""
    destination = project_root / "opencntx.toml"
    try:
        required_bytes = len(CONFIG_TEMPLATE.encode("utf-8")) + 4096
        require_disk_capacity(project_root, required_bytes, "core-init")
        with destination.open("x", encoding="utf-8", newline="\n") as config_file:
            config_file.write(CONFIG_TEMPLATE)
    except FileExistsError:
        print(
            f"Error: {destination.name} already exists; nothing was overwritten.",
            file=sys.stderr,
        )
        return 2
    except WorkspaceError as exc:
        print(f"Error: operation failed ({exc.code})", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Error: could not create {destination}: {exc}", file=sys.stderr)
        return 2

    print(f"Created: {destination}")
    return 0


def _dispatch_pack(args: argparse.Namespace) -> int:
    allowed_secret_ids = tuple(args.allow_secret)
    if args.preview:
        plan = plan_project(Path.cwd(), allowed_secret_ids=allowed_secret_ids)
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
    print("Built locally; this does not grant permission for external sharing.")
    for finding in manifest["security"]["warnings"]:
        print(
            "Secret policy warning: "
            f"{finding['finding_id']} {finding['path']}:"
            f"{finding['line']}:{finding['column']} "
            f"{finding['rule_id']} {finding['confidence']}",
            file=sys.stderr,
        )
    return 0


def dispatch_core(args: argparse.Namespace) -> int | None:
    """Dispatch one core command, or return None for another family."""
    if args.command == "init":
        return init_project(Path.cwd())
    if args.command == "pack":
        return _dispatch_pack(args)
    if args.command == "verify":
        package_argument = args.package.replace("\\", os.sep)
        report = verify_package(Path(package_argument))
        print(format_verify_report(report))
        return 0 if report.ok else 1
    return None
