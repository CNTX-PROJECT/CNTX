from __future__ import annotations

import unittest

from cntx_validation_integrity_slice.manifests import ManifestError, _apply


class ManifestConstructionTests(unittest.TestCase):
    def test_add_replace_remove_and_append(self) -> None:
        value = {"array": [1], "object": {"a": 1}}
        _apply(value, {"op": "add", "path": "/array/-", "value": 2})
        _apply(value, {"op": "replace", "path": "/object/a", "value": 3})
        _apply(value, {"op": "remove", "path": "/array/0"})
        self.assertEqual(value, {"array": [2], "object": {"a": 3}})

    def test_array_insertion_uses_json_patch_position(self) -> None:
        value = {"array": [1, 3]}
        _apply(value, {"op": "add", "path": "/array/1", "value": 2})
        self.assertEqual(value["array"], [1, 2, 3])

    def test_rejects_unknown_operation_and_invalid_paths(self) -> None:
        rejected = (
            {"op": "copy", "path": "/a"},
            {"op": "remove", "path": "/missing"},
            {"op": "add", "path": "not-a-pointer", "value": 1},
            {"op": "replace", "path": "/array/4", "value": 1},
        )
        for operation in rejected:
            with self.subTest(operation=operation), self.assertRaises(ManifestError):
                _apply({"array": []}, operation)

    def test_root_replacement_does_not_mutate_replacement_value(self) -> None:
        replacement = {"nested": []}
        result = _apply({}, {"op": "replace", "path": "", "value": replacement})
        result["nested"].append("changed")
        self.assertEqual(replacement, {"nested": []})


if __name__ == "__main__":
    unittest.main()
