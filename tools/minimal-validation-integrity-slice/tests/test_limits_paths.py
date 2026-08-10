from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from cntx_validation_integrity_slice.limits import LimitExceeded, require_at_most, require_exact
from cntx_validation_integrity_slice.path_safety import UnsafePath, resolve_beneath
from cntx_validation_integrity_slice.runner import _network_guard


class LimitAndPathTests(unittest.TestCase):
    def test_limit_helpers_fail_closed(self) -> None:
        require_at_most("x", 1, 1)
        require_exact("x", 1, 1)
        with self.assertRaises(LimitExceeded):
            require_at_most("x", 2, 1)
        with self.assertRaises(LimitExceeded):
            require_exact("x", 2, 1)

    def test_resolves_role_relative_path_beneath_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "safe.json"
            target.write_text("{}", encoding="utf-8")
            self.assertEqual(resolve_beneath(root, "safe.json", must_exist=True), target.resolve())

    def test_rejects_parent_absolute_and_stream_syntax(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rejected = ("../outside", str(root.resolve()), "file:stream")
            for value in rejected:
                with self.subTest(value=value), self.assertRaises(UnsafePath):
                    resolve_beneath(root, value, must_exist=False)

    @unittest.skipUnless(os.name == "nt", "Windows case-boundary test")
    def test_rejects_case_normalization_ambiguity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Exact.json").write_text("{}", encoding="utf-8")
            with self.assertRaises(UnsafePath):
                resolve_beneath(root, "exact.json", must_exist=True)

    def test_network_audit_event_is_rejected_without_contacting_network(self) -> None:
        with self.assertRaises(PermissionError):
            _network_guard("socket.connect", ())

    def test_rejects_symbolic_link_component_when_supported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target"
            target.mkdir()
            link = root / "link"
            try:
                link.symlink_to(target, target_is_directory=True)
            except OSError:
                self.skipTest("symbolic links unavailable in this environment")
            with self.assertRaises(UnsafePath):
                resolve_beneath(root, "link/file.json", must_exist=False)


if __name__ == "__main__":
    unittest.main()
