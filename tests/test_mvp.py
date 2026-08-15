from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from opencntx.core import OpenCntxError, pack_project


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPOSITORY_ROOT / "src"


def run_cli(*arguments: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    existing_pythonpath = environment.get("PYTHONPATH")
    environment["PYTHONPATH"] = os.pathsep.join(
        part for part in (str(SOURCE_ROOT), existing_pythonpath) if part
    )
    return subprocess.run(
        [sys.executable, "-m", "opencntx", *arguments],
        cwd=cwd,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )


def toml_array(values: list[str]) -> str:
    return "[" + ", ".join(json.dumps(value, ensure_ascii=False) for value in values) + "]"


def write_config(
    root: Path,
    *,
    include: list[str],
    required: list[str] | None = None,
    exclude: list[str] | None = None,
    max_files: int = 25,
    max_bytes: int = 100_000,
) -> None:
    content = "\n".join(
        [
            "[task]",
            'goal = "Test één concrete taak"',
            "",
            "[context]",
            f"include = {toml_array(include)}",
            f"required = {toml_array(required or [])}",
            f"exclude = {toml_array(exclude or [])}",
            f"max_files = {max_files}",
            f"max_bytes = {max_bytes}",
            "",
        ]
    )
    (root / "opencntx.toml").write_text(content, encoding="utf-8", newline="\n")


class MvpTests(unittest.TestCase):
    def test_01_happy_minimal_flow(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "README.md").write_text("# Demo\n", encoding="utf-8")
            (root / "src").mkdir()
            (root / "src" / "app.py").write_text("VALUE = 1\n", encoding="utf-8")

            init_result = run_cli("init", cwd=root)
            pack_result = run_cli("pack", cwd=root)
            verify_result = run_cli("verify", ".opencntx/latest", cwd=root)

            self.assertEqual(init_result.returncode, 0, init_result.stderr)
            self.assertEqual(pack_result.returncode, 0, pack_result.stderr)
            self.assertEqual(verify_result.returncode, 0, verify_result.stderr)
            package = root / ".opencntx" / "latest"
            self.assertEqual(
                sorted(path.name for path in package.iterdir()),
                ["CONTEXT.md", "manifest.json"],
            )
            manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(
                [source["path"] for source in manifest["sources"]],
                ["README.md", "src/app.py"],
            )
            self.assertIn("unchanged (2):", verify_result.stdout)
            self.assertIn("changed (0):", verify_result.stdout)
            self.assertIn("missing (0):", verify_result.stdout)
            self.assertIn("unexpected (0):", verify_result.stdout)
            self.assertIn("resultaat: OK", verify_result.stdout)

    def test_02_repeated_pack_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "a.txt").write_text("dezelfde bytes\n", encoding="utf-8")
            write_config(root, include=["**/*"], required=["a.txt"])

            first = run_cli("pack", cwd=root)
            first_context = (root / ".opencntx/latest/CONTEXT.md").read_bytes()
            first_manifest = (root / ".opencntx/latest/manifest.json").read_bytes()
            second = run_cli("pack", cwd=root)

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(
                (root / ".opencntx/latest/CONTEXT.md").read_bytes(),
                first_context,
            )
            self.assertEqual(
                (root / ".opencntx/latest/manifest.json").read_bytes(),
                first_manifest,
            )

    def test_03_budget_overflow_leaves_no_partial_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "large.txt").write_text("te groot", encoding="utf-8")
            write_config(root, include=["large.txt"], max_bytes=3)

            result = run_cli("pack", cwd=root)

            self.assertEqual(result.returncode, 2)
            self.assertIn("Bytebudget overschreden", result.stderr)
            self.assertFalse((root / ".opencntx/latest").exists())
            self.assertEqual(list((root / ".opencntx").glob(".building-*")), [])

        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "one.txt").write_text("een", encoding="utf-8")
            (root / "two.txt").write_text("twee", encoding="utf-8")
            write_config(root, include=["*.txt"], max_files=1)

            result = run_cli("pack", cwd=root)

            self.assertEqual(result.returncode, 2)
            self.assertIn("Bestandsbudget overschreden", result.stderr)
            self.assertFalse((root / ".opencntx/latest").exists())

    def test_04_missing_required_file_is_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "optional.txt").write_text("optioneel", encoding="utf-8")
            write_config(
                root,
                include=["*.txt"],
                required=["required.txt"],
            )

            result = run_cli("pack", cwd=root)

            self.assertEqual(result.returncode, 2)
            self.assertIn("Verplicht patroon", result.stderr)
            self.assertIn("required.txt", result.stderr)

    def test_05_exclusions_and_sensitive_defaults_apply_before_reading(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "notes.txt").write_text("publiek", encoding="utf-8")
            (root / ".env").write_text("DEMO_SECRET=not-real", encoding="utf-8")
            (root / "secret.pem").write_bytes(b"\x00binary-secret")
            (root / "private.key").write_bytes(b"\x00binary-key")
            write_config(
                root,
                include=["notes.txt", ".env", "secret.pem", "private.key", "missing*.md"],
                required=["notes.txt"],
            )

            result = run_cli("pack", cwd=root)

            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads(
                (root / ".opencntx/latest/manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual([item["path"] for item in manifest["sources"]], ["notes.txt"])
            self.assertEqual(
                {item["path"] for item in manifest["excluded"]},
                {".env", "private.key", "secret.pem"},
            )
            self.assertTrue(
                any(item.get("pattern") == "missing*.md" for item in manifest["ignored"])
            )
            context = (root / ".opencntx/latest/CONTEXT.md").read_text(encoding="utf-8")
            self.assertNotIn("not-real", context)

    def test_06_binary_and_unreadable_files_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "binary.bin").write_bytes(b"text\x00binary")
            write_config(root, include=["binary.bin"])

            binary_result = run_cli("pack", cwd=root)

            self.assertEqual(binary_result.returncode, 2)
            self.assertIn("Binaire bron", binary_result.stderr)

        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "blocked.txt").write_text("tekst", encoding="utf-8")
            write_config(root, include=["blocked.txt"])
            with patch.object(Path, "read_bytes", side_effect=PermissionError("geen toegang")):
                with self.assertRaisesRegex(OpenCntxError, "kan niet worden gelezen"):
                    pack_project(root)

    def test_07_path_traversal_and_symlink_escape_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            parent = Path(temporary_directory)
            root = parent / "project"
            root.mkdir()
            outside = parent / "outside.txt"
            outside.write_text("buiten", encoding="utf-8")
            write_config(root, include=["../outside.txt"])

            traversal_result = run_cli("pack", cwd=root)

            self.assertEqual(traversal_result.returncode, 2)
            self.assertIn("projectroot niet verlaten", traversal_result.stderr)

            write_config(root, include=["link.txt"])
            link = root / "link.txt"
            try:
                link.symlink_to(outside)
            except OSError:
                return
            symlink_result = run_cli("pack", cwd=root)
            self.assertEqual(symlink_result.returncode, 2)
            self.assertIn("symlink de projectroot", symlink_result.stderr)

    def test_08_verify_reports_all_drift_categories(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for name in ("a.txt", "b.txt", "stable.txt"):
                (root / name).write_text(f"origineel {name}\n", encoding="utf-8")
            write_config(root, include=["*.txt"], required=["a.txt"])
            pack_result = run_cli("pack", cwd=root)
            self.assertEqual(pack_result.returncode, 0, pack_result.stderr)

            (root / "a.txt").write_text("gewijzigd\n", encoding="utf-8")
            (root / "b.txt").unlink()
            (root / "new.txt").write_text("nieuw\n", encoding="utf-8")
            verify_result = run_cli("verify", ".opencntx/latest", cwd=root)

            self.assertEqual(verify_result.returncode, 1)
            self.assertRegex(verify_result.stdout, r"(?s)unchanged \(1\):.*stable\.txt")
            self.assertRegex(verify_result.stdout, r"(?s)changed \(1\):.*a\.txt")
            self.assertRegex(verify_result.stdout, r"(?s)missing \(1\):.*b\.txt")
            self.assertRegex(verify_result.stdout, r"(?s)unexpected \(1\):.*new\.txt")
            self.assertIn("resultaat: DRIFT OF ONVOLLEDIG", verify_result.stdout)

    def test_09_windows_style_paths_work(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            folder = root / "folder"
            folder.mkdir()
            (folder / "note.txt").write_text("Windows-pad", encoding="utf-8")
            write_config(
                root,
                include=[r"folder\*.txt"],
                required=[r"folder\note.txt"],
            )

            pack_result = run_cli("pack", cwd=root)
            verify_result = run_cli("verify", r".opencntx\latest", cwd=root)

            self.assertEqual(pack_result.returncode, 0, pack_result.stderr)
            self.assertEqual(verify_result.returncode, 0, verify_result.stderr)
            self.assertIn("folder/note.txt", verify_result.stdout)

    def test_10_pack_and_verify_never_mutate_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source_path = root / "source.txt"
            source_path.write_bytes(b"ongewijzigde bron\n")
            write_config(root, include=["source.txt"], required=["source.txt"])
            before_bytes = source_path.read_bytes()
            before_mtime = source_path.stat().st_mtime_ns

            pack_result = run_cli("pack", cwd=root)
            verify_result = run_cli("verify", ".opencntx/latest", cwd=root)

            self.assertEqual(pack_result.returncode, 0, pack_result.stderr)
            self.assertEqual(verify_result.returncode, 0, verify_result.stderr)
            self.assertEqual(source_path.read_bytes(), before_bytes)
            self.assertEqual(source_path.stat().st_mtime_ns, before_mtime)

    def test_invalid_toml_is_a_short_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "opencntx.toml").write_text("[task\n", encoding="utf-8")

            result = run_cli("pack", cwd=root)

            self.assertEqual(result.returncode, 2)
            self.assertIn("ongeldige TOML", result.stderr)

    def test_tampered_context_makes_verify_nonzero_without_rewriting_it(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "source.txt").write_text("bron", encoding="utf-8")
            write_config(root, include=["source.txt"])
            self.assertEqual(run_cli("pack", cwd=root).returncode, 0)
            context_path = root / ".opencntx/latest/CONTEXT.md"
            context_path.write_text("gemanipuleerd", encoding="utf-8")
            before = context_path.read_bytes()

            result = run_cli("verify", ".opencntx/latest", cwd=root)

            self.assertEqual(result.returncode, 1)
            self.assertIn("CONTEXT.md wijkt af", result.stdout)
            self.assertEqual(context_path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
