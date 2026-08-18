from __future__ import annotations

import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import tomllib
import unittest


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


class CliTests(unittest.TestCase):
    def test_package_versions_match(self) -> None:
        with (REPOSITORY_ROOT / "pyproject.toml").open("rb") as project_file:
            project_version = tomllib.load(project_file)["project"]["version"]

        package_globals = runpy.run_path(SOURCE_ROOT / "opencntx" / "__init__.py")

        self.assertEqual(project_version, "0.2.0")
        self.assertEqual(package_globals["__version__"], project_version)

    def test_help_works(self) -> None:
        result = run_cli("--help", cwd=REPOSITORY_ROOT)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("{init,pack,verify}", result.stdout)
        self.assertIn("controleerbaar contextpakket", result.stdout)

    def test_init_creates_expected_template(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project_root = Path(temporary_directory)

            result = run_cli("init", cwd=project_root)

            self.assertEqual(result.returncode, 0, result.stderr)
            config = (project_root / "opencntx.toml").read_text(encoding="utf-8")
            self.assertIn('[task]\ngoal = "Beschrijf de ene concrete taak"', config)
            self.assertIn("max_files = 25", config)
            self.assertIn("max_bytes = 100000", config)

    def test_init_never_overwrites_existing_config(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project_root = Path(temporary_directory)
            config_path = project_root / "opencntx.toml"
            config_path.write_text("bewaar mij\n", encoding="utf-8")

            result = run_cli("init", cwd=project_root)

            self.assertEqual(result.returncode, 2)
            self.assertIn("niets overschreven", result.stderr)
            self.assertEqual(config_path.read_text(encoding="utf-8"), "bewaar mij\n")


if __name__ == "__main__":
    unittest.main()
