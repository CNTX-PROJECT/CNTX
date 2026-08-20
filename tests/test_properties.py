from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

try:
    from hypothesis import HealthCheck, given, settings
    from hypothesis import strategies as st
except ImportError:
    HYPOTHESIS_AVAILABLE = False

    def given(*_args: object, **_kwargs: object):
        return lambda function: function

    class _MissingStrategies:
        def __getattr__(self, _name: str):
            return lambda *_args, **_kwargs: None

    st = _MissingStrategies()
    HealthCheck = settings = None
else:
    HYPOTHESIS_AVAILABLE = True


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "src"
if str(SOURCE_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(SOURCE_ROOT))

from opencntx.attempts import AttemptError, normalize_target
from opencntx.core import OpenCntxError, _matches_pattern, _normalize_relative_path
from opencntx.integrity import (
    IntegrityError,
    _write_new,
    safe_managed_path,
    write_new_bytes,
)
from opencntx.lifecycle import LifecycleError, _read_json
from opencntx.primitives import pretty_json_bytes, sha256_bytes

if settings is not None:
    settings.register_profile(
        "opencntx-ci",
        max_examples=50,
        derandomize=True,
        database=None,
        deadline=None,
        suppress_health_check=(HealthCheck.too_slow,),
    )
    settings.load_profile("opencntx-ci")


@unittest.skipUnless(HYPOTHESIS_AVAILABLE, "Hypothesis is an explicit quality dependency")
class PropertyTests(unittest.TestCase):
    @given(
        st.lists(
            st.from_regex(r"[A-Za-z0-9_-]{1,12}", fullmatch=True),
            min_size=1,
            max_size=5,
        )
    )
    def test_safe_relative_paths_remain_contained(self, parts: list[str]) -> None:
        relative = "/".join(parts)
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            root.joinpath(*parts[:-1]).mkdir(parents=True, exist_ok=True)
            result = safe_managed_path(root, relative)
            self.assertEqual(root.resolve() / relative, result)
            self.assertTrue(result.is_relative_to(root.resolve()))

    @given(
        st.sampled_from(
            ("", ".", "..", "../outside", "/absolute", "C:/absolute", "safe/../outside")
        )
    )
    def test_unsafe_managed_paths_fail_closed(self, relative: str) -> None:
        with (
            tempfile.TemporaryDirectory() as temporary_directory,
            self.assertRaises(IntegrityError),
        ):
            safe_managed_path(Path(temporary_directory), relative)

    def test_dot_managed_path_fails_closed_without_index_error(self) -> None:
        with (
            tempfile.TemporaryDirectory() as temporary_directory,
            self.assertRaises(IntegrityError),
        ):
            safe_managed_path(Path(temporary_directory), ".")

    def test_shared_new_file_writer_preserves_bytes_and_reports_parent_sync(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "exact.bin"
            result = write_new_bytes(target, b"exact\x00bytes", sync_parent=True)
            self.assertEqual(b"exact\x00bytes", target.read_bytes())
            self.assertIn(result, {"SYNCED", "UNSUPPORTED"})

    def test_transaction_writer_translates_existing_target_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory) / "existing.bin"
            target.write_bytes(b"keep")
            with self.assertRaises(IntegrityError) as caught:
                _write_new(target, b"replacement")
            self.assertEqual("transaction_write_failed", caught.exception.code)
            self.assertEqual(b"keep", target.read_bytes())

    def test_lifecycle_json_reader_rejects_non_object_and_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            cases = {
                "array.json": (b"[]", "lifecycle_record_invalid"),
                "duplicate.json": (b'{"key":1,"key":2}', "lifecycle_record_invalid"),
            }
            for name, (content, expected_code) in cases.items():
                with self.subTest(name=name):
                    path = root / name
                    path.write_bytes(content)
                    with self.assertRaises(LifecycleError) as caught:
                        _read_json(path, label="property fixture")
                    self.assertEqual(expected_code, caught.exception.code)

    @given(
        st.lists(
            st.from_regex(r"[A-Za-z0-9_.-]{1,16}", fullmatch=True),
            min_size=1,
            max_size=5,
        )
    )
    def test_attempt_targets_and_core_paths_are_idempotent(self, parts: list[str]) -> None:
        relative = "/".join(parts)
        try:
            normalized_target = normalize_target(relative)
            normalized_path = _normalize_relative_path(relative, "path")
        except (AttemptError, OpenCntxError):
            return
        self.assertEqual(normalized_target, normalize_target(normalized_target))
        self.assertEqual(normalized_path, _normalize_relative_path(normalized_path, "path"))

    @given(
        st.from_regex(r"[A-Za-z0-9_-]{1,10}/[A-Za-z0-9_.-]{1,10}", fullmatch=True),
        st.sampled_from(("**/*", "**/*.py", "*", "src/**", "README.md")),
    )
    def test_pattern_matching_is_deterministic(self, relative: str, pattern: str) -> None:
        self.assertEqual(
            _matches_pattern(relative, pattern),
            _matches_pattern(relative, pattern),
        )

    @given(
        st.dictionaries(
            st.from_regex(r"[a-z][a-z0-9_]{0,12}", fullmatch=True),
            st.one_of(st.none(), st.booleans(), st.integers(-1000, 1000), st.text(max_size=20)),
            max_size=12,
        )
    )
    def test_manifest_like_json_is_canonical_and_digest_stable(
        self, value: dict[str, object]
    ) -> None:
        first = pretty_json_bytes(value)
        second = pretty_json_bytes(dict(reversed(tuple(value.items()))))
        self.assertEqual(first, second)
        self.assertEqual(value, json.loads(first))
        self.assertEqual(sha256_bytes(first), sha256_bytes(second))


if __name__ == "__main__":
    unittest.main()
