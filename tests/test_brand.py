from __future__ import annotations

import hashlib
import os
import struct
import subprocess
import sys
import unittest
import zlib
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "assets" / "brand"
RENDERER = ROOT / "tools" / "render_brand.py"

SVG_DIMENSIONS = {
    "opencntx-avatar.svg": (512, 512),
    "opencntx-social-preview.svg": (1280, 640),
    "opencntx-symbol-dark.svg": (256, 256),
    "opencntx-symbol-light.svg": (256, 256),
    "opencntx-wordmark-dark.svg": (800, 160),
    "opencntx-wordmark-light.svg": (800, 160),
}

PNG_DIMENSIONS = {
    "opencntx-avatar-512.png": (512, 512),
    "opencntx-icon-128.png": (128, 128),
    "opencntx-icon-32.png": (32, 32),
    "opencntx-social-preview-1280x640.png": (1280, 640),
}

PALETTE = {
    "#F7F5FB",
    "#0B0B0F",
    "#FFFFFF",
    "#7C3AED",
    "#A855F7",
    "#6D28D9",
    "#C084FC",
}

ALLOWED_ELEMENTS = {
    "svg",
    "g",
    "title",
    "desc",
    "rect",
    "polygon",
    "circle",
    "ellipse",
}
ALLOWED_ATTRIBUTES = {
    "svg": {"width", "height", "viewBox", "role", "aria-labelledby"},
    "g": {"id", "fill", "aria-label"},
    "title": {"id"},
    "desc": {"id"},
    "rect": {"x", "y", "width", "height", "fill"},
    "polygon": {"points", "fill"},
    "circle": {"cx", "cy", "r", "fill"},
    "ellipse": {"cx", "cy", "rx", "ry", "fill"},
}


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _luminance(color: str) -> float:
    channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        value / 12.92
        if value <= 0.04045
        else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def _contrast(first: str, second: str) -> float:
    high, low = sorted((_luminance(first), _luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def _png(path: Path):
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise AssertionError(f"not a PNG: {path.name}")
    offset = 8
    chunks = []
    payloads: dict[bytes, list[bytes]] = {}
    while offset < len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        name = data[offset + 4 : offset + 8]
        payload = data[offset + 8 : offset + 8 + length]
        chunks.append(name)
        payloads.setdefault(name, []).append(payload)
        offset += 12 + length
    header = payloads[b"IHDR"][0]
    width, height, bit_depth, color_type, compression, filtering, interlace = (
        struct.unpack(">IIBBBBB", header)
    )
    raw = zlib.decompress(b"".join(payloads[b"IDAT"]))
    return (
        chunks,
        (width, height),
        (bit_depth, color_type, compression, filtering, interlace),
        raw,
    )


class BrandTests(unittest.TestCase):
    def test_svg_profile_dimensions_and_accessibility_are_exact(self) -> None:
        forbidden = (
            b"<script",
            b"<text",
            b"<use",
            b"<image",
            b"<filter",
            b"<mask",
            b"<linearGradient",
            b"<radialGradient",
            b"<animate",
            b"<foreignObject",
            b"href=",
            b"url(",
            b"font",
            b"style=",
        )
        for name, dimensions in SVG_DIMENSIONS.items():
            with self.subTest(name=name):
                path = BRAND / name
                data = path.read_bytes()
                data.decode("utf-8", errors="strict")
                for token in forbidden:
                    self.assertNotIn(token, data)
                root = ElementTree.fromstring(data)
                self.assertEqual(str(dimensions[0]), root.attrib["width"])
                self.assertEqual(str(dimensions[1]), root.attrib["height"])
                self.assertEqual(
                    f"0 0 {dimensions[0]} {dimensions[1]}", root.attrib["viewBox"]
                )
                self.assertEqual("img", root.attrib["role"])
                self.assertEqual("title description", root.attrib["aria-labelledby"])
                self.assertEqual("title", _local_name(root[0].tag))
                self.assertEqual("title", root[0].attrib["id"])
                self.assertEqual("desc", _local_name(root[1].tag))
                self.assertEqual("description", root[1].attrib["id"])
                for element in root.iter():
                    local = _local_name(element.tag)
                    self.assertIn(local, ALLOWED_ELEMENTS)
                    self.assertTrue(
                        set(element.attrib).issubset(ALLOWED_ATTRIBUTES[local]),
                        (name, local, element.attrib),
                    )
                    fill = element.attrib.get("fill")
                    if fill:
                        self.assertIn(fill, PALETTE)

    def test_wordmark_owner_color_rule_is_exact(self) -> None:
        expected = {
            "opencntx-wordmark-light.svg": ("#6D28D9", "#0B0B0F"),
            "opencntx-wordmark-dark.svg": ("#C084FC", "#FFFFFF"),
        }
        for name, colors in expected.items():
            root = ElementTree.parse(BRAND / name).getroot()
            groups = {
                element.attrib.get("id"): element
                for element in root
                if _local_name(element.tag) == "g"
            }
            self.assertEqual("OPEN", groups["word-open"].attrib["aria-label"])
            self.assertEqual("CNTX", groups["word-cntx"].attrib["aria-label"])
            self.assertEqual(colors[0], groups["word-open"].attrib["fill"])
            self.assertEqual(colors[1], groups["word-cntx"].attrib["fill"])

    def test_primary_brand_is_simple_text_without_legacy_network_art(self) -> None:
        for name in (
            "opencntx-avatar.svg",
            "opencntx-social-preview.svg",
            "opencntx-wordmark-dark.svg",
            "opencntx-wordmark-light.svg",
        ):
            with self.subTest(name=name):
                data = (BRAND / name).read_bytes()
                for legacy in (b'id="boundary"', b'id="network"', b'id="nodes"'):
                    self.assertNotIn(legacy, data)
                self.assertIn(b'id="word-open"', data)
                self.assertIn(b'id="word-cntx"', data)

        for name in ("opencntx-avatar.svg", "opencntx-social-preview.svg"):
            root = ElementTree.parse(BRAND / name).getroot()
            groups = {
                element.attrib.get("id"): element
                for element in root
                if _local_name(element.tag) == "g"
            }
            self.assertEqual("#6D28D9", groups["word-open"].attrib["fill"])
            self.assertEqual("#0B0B0F", groups["word-cntx"].attrib["fill"])

        social = (BRAND / "opencntx-social-preview.svg").read_text(
            encoding="utf-8"
        )
        self.assertIn("SMALL CONTEXT. CLEAR EVIDENCE. ANY MODEL.", social)

    def test_text_and_graphic_contrasts_meet_the_contract(self) -> None:
        text_pairs = (
            ("#0B0B0F", "#F7F5FB"),
            ("#6D28D9", "#F7F5FB"),
            ("#FFFFFF", "#0B0B0F"),
            ("#C084FC", "#0B0B0F"),
        )
        graphic_pairs = (
            ("#7C3AED", "#F7F5FB"),
            ("#A855F7", "#0B0B0F"),
        )
        for foreground, background in text_pairs:
            self.assertGreaterEqual(_contrast(foreground, background), 4.5)
        for foreground, background in graphic_pairs:
            self.assertGreaterEqual(_contrast(foreground, background), 3.0)

    def test_png_dimensions_chunks_and_transparency_are_exact(self) -> None:
        for name, dimensions in PNG_DIMENSIONS.items():
            with self.subTest(name=name):
                chunks, actual, profile, raw = _png(BRAND / name)
                self.assertEqual([b"IHDR", b"IDAT", b"IEND"], chunks)
                self.assertEqual(dimensions, actual)
                self.assertEqual((8, 6, 0, 0, 0), profile)
                stride = dimensions[0] * 4 + 1
                self.assertEqual(stride * dimensions[1], len(raw))
                self.assertTrue(all(raw[row * stride] == 0 for row in range(dimensions[1])))
                alpha = []
                for row in range(dimensions[1]):
                    pixels = raw[row * stride + 1 : (row + 1) * stride]
                    alpha.extend(pixels[3::4])
                if "icon" in name:
                    self.assertEqual(0, min(alpha))
                    self.assertEqual(255, max(alpha))
                else:
                    self.assertEqual({255}, set(alpha))

    def test_hash_manifest_is_sorted_complete_and_current(self) -> None:
        manifest = (BRAND / "SHA256SUMS").read_bytes()
        self.assertNotIn(b"\r", manifest)
        self.assertNotIn(b"\n", manifest)
        lines = manifest.decode("ascii").split(" | ")
        parsed = [line.split("  ", 1) for line in lines]
        expected_paths = sorted(
            f"assets/brand/{name}" for name in (*SVG_DIMENSIONS, *PNG_DIMENSIONS)
        )
        self.assertEqual(expected_paths, [item[1] for item in parsed])
        for digest, relative in parsed:
            self.assertEqual(64, len(digest))
            data = (ROOT / relative).read_bytes()
            if relative.endswith(".svg"):
                data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            actual = hashlib.sha256(data).hexdigest()
            self.assertEqual(digest, actual, relative)

    def test_standard_library_renderer_reproduces_derivatives(self) -> None:
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONUTF8"] = "1"
        completed = subprocess.run(
            [sys.executable, str(RENDERER), "--check"],
            cwd=ROOT,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("BRAND_ASSETS_OK", completed.stdout.strip())


if __name__ == "__main__":
    unittest.main()
