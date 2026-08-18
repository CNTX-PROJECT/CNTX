# Installation

Install OPENCNTX locally from its public Git tag. No account, API key, database,
or AI provider is required.

## Requirements

- Python 3.11, 3.12, or 3.13
- Git
- Windows or Ubuntu for the fully tested paths

Other operating systems may work, but they are not part of the current live CI
matrix.

## Windows

Open PowerShell and run:

```powershell
git clone --branch v0.2.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
opencntx --help
```

If `python` is not found, install a supported Python version and make sure its
launcher is available in your terminal. Do not download unofficial OPENCNTX
installers.

## Ubuntu

Open a terminal and run:

```bash
git clone --branch v0.2.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python3 -m pip install .
opencntx --help
```

Use a virtual environment when your system Python does not allow local package
installation:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
opencntx --help
```

## Verify the installed version

```powershell
python -c "import opencntx; print(opencntx.__version__)"
```

The current release prints `0.2.0`.

## Install current contributor source

Use `main` only when you intentionally want unreleased contributor work:

```powershell
git clone --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

A live tag and GitHub release are the stable publication boundary. OPENCNTX is
not published on PyPI.

## Upgrade

Clone the new approved tag into a fresh directory and install it. Do not assume
that replacing files inside an old clone proves a clean upgrade.

## Remove

If you installed OPENCNTX into a Python environment:

```powershell
python -m pip uninstall opencntx
```

Removing the package does not remove your project files, workspaces, or context
packages. Review and delete those separately only when you intend to.

## Next step

Continue with [Getting started](getting-started.md). For installation errors,
open [Troubleshooting](troubleshooting.md).

[Documentation home](README.md)
