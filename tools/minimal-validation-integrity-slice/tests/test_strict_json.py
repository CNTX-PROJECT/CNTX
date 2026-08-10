from __future__ import annotations

import unittest

from cntx_validation_integrity_slice.limits import ResourceLimits
from cntx_validation_integrity_slice.strict_json import StrictJsonError, loads_strict


class StrictJsonTests(unittest.TestCase):
    def test_accepts_closed_json_value(self) -> None:
        self.assertEqual(loads_strict(b'{"a":[1,true,null]}'), {"a": [1, True, None]})

    def test_rejects_duplicate_member(self) -> None:
        with self.assertRaises(StrictJsonError):
            loads_strict(b'{"a":1,"a":2}')

    def test_rejects_bom_invalid_utf8_comments_and_trailing_bytes(self) -> None:
        rejected = (
            b"\xef\xbb\xbf{}",
            b'"\xff"',
            b'{"a":1 // comment\n}',
            b'{} trailing',
        )
        for data in rejected:
            with self.subTest(data=data), self.assertRaises(StrictJsonError):
                loads_strict(data)

    def test_rejects_nan(self) -> None:
        with self.assertRaises(StrictJsonError):
            loads_strict(b'{"value":NaN}')

    def test_enforces_bytes_depth_and_nodes(self) -> None:
        limits = ResourceLimits(individual_json_bytes=4, json_depth=2, json_nodes=3)
        with self.assertRaises(ValueError):
            loads_strict(b'{"a":1}', limits)
        with self.assertRaises(ValueError):
            loads_strict(b'[[[]]]', ResourceLimits(json_depth=2))
        with self.assertRaises(ValueError):
            loads_strict(b'[1,2,3]', ResourceLimits(json_nodes=3))


if __name__ == "__main__":
    unittest.main()
