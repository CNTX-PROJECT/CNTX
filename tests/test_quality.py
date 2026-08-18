from __future__ import annotations

import os
import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
DOCS = ROOT / "docs"
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"


def _configure_windows_ci_temp_root() -> None:
    if os.name != "nt" or os.environ.get("GITHUB_ACTIONS") != "true":
        return
    runner_temp = os.environ.get("RUNNER_TEMP")
    if runner_temp is None:
        raise RuntimeError("Windows GitHub Actions requires RUNNER_TEMP")
    canonical_temp = Path(runner_temp).resolve()
    if not canonical_temp.is_dir():
        raise RuntimeError("Windows GitHub Actions RUNNER_TEMP must exist")
    tempfile.tempdir = str(canonical_temp)


_configure_windows_ci_temp_root()

GUIDES = {
    "brand.md",
    "core.md",
    "workspace.md",
    "owner-flow.md",
    "commands.md",
    "security.md",
    "platforms.md",
}

EXPECTED_ACTION_USES = {
    "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
    "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97",
}

EXPECTED_DOCUMENTED_COMMAND_PATHS = (
    "opencntx --help",
    "opencntx workspace --help",
    "opencntx workspace media --help",
    "opencntx workspace task --help",
    "opencntx init",
    "opencntx pack",
    "opencntx verify",
    "opencntx workspace init",
    "opencntx workspace capture",
    "opencntx workspace chapter create",
    "opencntx workspace catalog rebuild",
    "opencntx workspace media register",
    "opencntx workspace media review",
    "opencntx workspace media promote",
    "opencntx workspace media status",
    "opencntx workspace media verify",
    "opencntx workspace media remove",
    "opencntx workspace playbook register",
    "opencntx workspace playbook approve",
    "opencntx workspace playbook status",
    "opencntx workspace playbook verify",
    "opencntx workspace role register",
    "opencntx workspace role approve",
    "opencntx workspace role status",
    "opencntx workspace role verify",
    "opencntx workspace executor prepare",
    "opencntx workspace executor status",
    "opencntx workspace executor verify",
    "opencntx workspace context build",
    "opencntx workspace context verify",
    "opencntx workspace task propose",
    "opencntx workspace task approve",
    "opencntx workspace task begin",
    "opencntx workspace task submit-result",
    "opencntx workspace task review-result",
    "opencntx workspace task accept-result",
    "opencntx workspace task close",
    "opencntx workspace task status",
    "opencntx workspace task record-attempt",
    "opencntx workspace task cancel",
    "opencntx workspace task supersede",
)

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")
COMMAND_ROW = re.compile(r"^\|\s*\d+\s*\|\s*`([^`]+)`\s*\|", re.MULTILINE)


def _link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def _local_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    links: list[str] = []
    for match in MARKDOWN_LINK.finditer(text):
        target = _link_target(match.group(1))
        parsed = urlsplit(target)
        if parsed.scheme in {"http", "https", "mailto"} or not parsed.path:
            continue
        links.append(unquote(parsed.path))
    return links


class PublicQualityTests(unittest.TestCase):
    def test_all_local_markdown_links_resolve_within_repository(self) -> None:
        markdown_files = sorted(
            path
            for path in ROOT.rglob("*.md")
            if ".git" not in path.parts and ".opencntx" not in path.parts
        )
        self.assertTrue(markdown_files)

        for markdown_file in markdown_files:
            for target in _local_links(markdown_file):
                with self.subTest(file=markdown_file, target=target):
                    self.assertFalse(target.startswith("file://"))
                    self.assertFalse(Path(target).is_absolute())
                    self.assertIsNone(WINDOWS_ABSOLUTE.match(target))
                    resolved = (markdown_file.parent / target).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.exists())

    def test_docs_index_links_every_guide(self) -> None:
        index_links = {Path(target).as_posix() for target in _local_links(DOCS / "README.md")}
        self.assertEqual(GUIDES, index_links & GUIDES)

        for guide_name in GUIDES:
            guide = DOCS / guide_name
            text = guide.read_text(encoding="utf-8")
            headings = [line for line in text.splitlines() if line.startswith("# ")]
            self.assertEqual(1, len(headings), guide_name)
            self.assertIn("README.md", _local_links(guide), guide_name)

        command_text = (DOCS / "commands.md").read_text(encoding="utf-8")
        documented_paths = tuple(COMMAND_ROW.findall(command_text))
        self.assertEqual(EXPECTED_DOCUMENTED_COMMAND_PATHS, documented_paths)
        self.assertEqual(41, len(documented_paths))

    def test_readme_is_compact_and_links_the_docs(self) -> None:
        lines = README.read_text(encoding="utf-8").splitlines()
        self.assertLessEqual(len(lines), 180)
        text = README.read_text(encoding="utf-8")
        self.assertIn('srcset="assets/brand/opencntx-wordmark-dark.svg"', text)
        self.assertIn('src="assets/brand/opencntx-wordmark-light.svg"', text)
        targets = {Path(target).as_posix() for target in _local_links(README)}
        required = {"docs/README.md"} | {f"docs/{name}" for name in GUIDES}
        self.assertTrue(required.issubset(targets))

    def test_community_and_security_routes_are_bounded(self) -> None:
        required = {
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
            "SUPPORT.md",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/ISSUE_TEMPLATE/feature_request.yml",
            ".github/ISSUE_TEMPLATE/config.yml",
            ".github/pull_request_template.md",
        }
        self.assertTrue(all((ROOT / path).is_file() for path in required))

        security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        support = (ROOT / "SUPPORT.md").read_text(encoding="utf-8")
        issue_config = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text(
            encoding="utf-8"
        )
        pull_request = (ROOT / ".github/pull_request_template.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Report a vulnerability", security)
        self.assertIn("SUPPORT.md", security)
        self.assertIn("openbaar issue", support)
        self.assertIn("blank_issues_enabled: false", issue_config)
        self.assertIn("/security/advisories/new", issue_config)
        self.assertNotIn("mailto:", issue_config)
        for phrase in (
            "Security- en privacygrenzen",
            "Nieuwe of gewijzigde dependencies",
            "Documentatie en changelog",
            "render_brand.py --check",
            "Nul automatische checks is geen groen bewijs",
        ):
            self.assertIn(phrase, pull_request)

    def test_workflow_uses_immutable_official_action_pins(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        uses = {
            line.split("uses:", 1)[1].split("#", 1)[0].strip()
            for line in text.splitlines()
            if "uses:" in line
        }
        self.assertEqual(EXPECTED_ACTION_USES, uses)
        for action in uses:
            self.assertRegex(action, r"^actions/[a-z-]+@[0-9a-f]{40}$")

    def test_workflow_permissions_and_triggers_are_bounded(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("pull_request:", text)
        self.assertIn("push:", text)
        self.assertIn("contents: read", text)
        self.assertIn("persist-credentials: false", text)
        for forbidden in (
            "pull_request_target",
            "contents: write",
            "actions: write",
            "id-token: write",
            "packages: write",
            "secrets.",
            "upload-artifact",
            "workflow_dispatch",
        ):
            self.assertNotIn(forbidden, text)

    def test_workflow_matrix_and_commands_cover_tests_build_install_smoke(self) -> None:
        text = WORKFLOW.read_text(encoding="utf-8")
        for value in (
            "ubuntu-latest",
            "windows-latest",
            '"3.11"',
            '"3.12"',
            '"3.13"',
            "PYTHONDONTWRITEBYTECODE",
            "PYTHONUTF8",
            "python -W error::ResourceWarning -m unittest discover -s tests",
            "python -m pip wheel . --no-deps --wheel-dir dist",
            '"--no-deps"',
            'subprocess.run(["opencntx", "--help"], check=True)',
        ):
            self.assertIn(value, text)

    def test_public_ci_status_is_active_and_unambiguous(self) -> None:
        status_documents = (README, CHANGELOG, DOCS / "platforms.md")
        for document in status_documents:
            with self.subTest(document=document.name):
                text = document.read_text(encoding="utf-8")
                self.assertIn("CI_ACTIVE", text)
                self.assertNotIn("CI_DEFINED_INACTIVE", text)
                self.assertIn("live", text.lower())
        if os.name == "nt" and os.environ.get("GITHUB_ACTIONS") == "true":
            self.assertEqual(
                Path(os.environ["RUNNER_TEMP"]).resolve(),
                Path(tempfile.gettempdir()).resolve(),
            )


if __name__ == "__main__":
    unittest.main()
