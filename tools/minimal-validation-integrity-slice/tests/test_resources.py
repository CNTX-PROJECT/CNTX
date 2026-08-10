from __future__ import annotations

import unittest

from cntx_validation_integrity_slice.resources import _pointer_exists


class ResourceTests(unittest.TestCase):
    def test_pointer_resolution(self) -> None:
        document = {"$defs": {"a/b": {"~key": ["value"]}}}
        self.assertTrue(_pointer_exists(document, "#/$defs/a~1b/~0key/0"))
        self.assertFalse(_pointer_exists(document, "#/$defs/missing"))
        self.assertFalse(_pointer_exists(document, "#not-a-pointer"))

    def test_supported_resource_inventory_is_exact(self) -> None:
        from cntx_validation_integrity_slice.resources import SCHEMA_IDENTITIES

        self.assertEqual(len(SCHEMA_IDENTITIES), 10)
        self.assertEqual(len(set(SCHEMA_IDENTITIES.values())), 10)
        self.assertTrue(all(identity.endswith("/1.0.0") for identity in SCHEMA_IDENTITIES.values()))


if __name__ == "__main__":
    unittest.main()
