# Brand guide

The OPENCNTX identity is a simple text system. It avoids a separate network or
boundary illustration in the primary mark.

## Core rule

- `OPEN` is purple.
- `CNTX` is near-black on light backgrounds.
- `CNTX` is white on dark backgrounds.
- Always write `OPENCNTX` in uppercase without a space in normal text.

## Official colors

| Use | Color |
|---|---|
| Light background | `#F7F5FB` |
| Dark background | `#0B0B0F` |
| Primary purple | `#7C3AED` |
| Light-wordmark purple | `#6D28D9` |
| Dark-wordmark purple | `#C084FC` |
| White | `#FFFFFF` |

The tested text pairs meet WCAG AA contrast for normal text.

## Official files

| File | Use |
|---|---|
| `opencntx-wordmark-light.svg` | wide mark on a light surface |
| `opencntx-wordmark-dark.svg` | wide mark on a dark surface |
| `opencntx-avatar.svg` | stacked organization avatar source |
| `opencntx-avatar-512.png` | generated avatar upload |
| `opencntx-symbol-light.svg` | compact OC mark for light surfaces |
| `opencntx-symbol-dark.svg` | compact OC mark for dark surfaces |
| `opencntx-icon-32.png` | generated small icon |
| `opencntx-icon-128.png` | generated large icon |
| `opencntx-social-preview.svg` | social preview source |
| `opencntx-social-preview-1280x640.png` | generated social preview upload |

## Clear space and size

- Keep clear space equal to at least the height of the `O` stroke around the
  wordmark.
- Do not display the horizontal wordmark below 240 pixels wide.
- Use the compact mark below that size.
- Keep the avatar square and do not crop its text.

## Do not

- change the OPEN/CNTX color relationship;
- add gradients, shadows, glow, or decorative network lines;
- stretch or rotate the mark;
- replace letters with generated image text;
- place the light variant on a dark surface or the dark variant on light;
- use unofficial colors as if they were the primary identity.

## Reproduce and verify

The official SVG files use controlled native shapes without external fonts,
scripts, images, or network references. PNG files and `SHA256SUMS` are
deterministically generated:

```powershell
$env:PYTHONDONTWRITEBYTECODE="1"
python tools/render_brand.py --write
python tools/render_brand.py --check
```

PNG checksums are byte-exact. SVG checksums use canonical LF line endings so
the same vector source verifies after a normal checkout on Windows or Linux.

Run `--write` only after consciously reviewing an official SVG change. Normal
verification uses `--check` and must not change committed files.

For contribution and support routes, see [CONTRIBUTING.md](../CONTRIBUTING.md)
and [SUPPORT.md](../SUPPORT.md).

[Documentation home](README.md)
