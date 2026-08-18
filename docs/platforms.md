# Platforms and CI

OPENCNTX requires Python 3.11 or newer and has no runtime dependencies.

## Supported Python versions

- Python 3.11
- Python 3.12
- Python 3.13

## Fully tested operating systems

- Windows
- Ubuntu Linux

The code may work elsewhere, but the project does not claim live CI proof for
an operating system outside this matrix.

## Active CI matrix

Status label: `CI_ACTIVE`

Every pull request and push to `main` runs six jobs:

| Operating system | Python 3.11 | Python 3.12 | Python 3.13 |
|---|:---:|:---:|:---:|
| Ubuntu | ✓ | ✓ | ✓ |
| Windows | ✓ | ✓ | ✓ |

Each job:

1. checks out the exact commit;
2. sets up the selected Python version;
3. runs the complete test suite with `ResourceWarning` treated as an error;
4. builds exactly one wheel;
5. installs that wheel without dependencies;
6. verifies package version and `opencntx --help`.

## What counts as proof

Only a completed successful live run on the exact candidate or main commit is
green CI evidence. A workflow file, local run, or empty check list is not live
CI proof.

The `main` ruleset requires the exact six matrix check names and strict current
commit status.

## Run tests locally

```powershell
$env:PYTHONDONTWRITEBYTECODE="1"
python -W error::ResourceWarning -m unittest discover -s tests
python tools/render_brand.py --check
```

Ubuntu:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 tools/render_brand.py --check
```

## Related pages

- [Installation](installation.md)
- [Troubleshooting](troubleshooting.md)
- [Public roadmap](roadmap.md)
- [Contribution guide](../CONTRIBUTING.md)

[Documentation home](README.md)
