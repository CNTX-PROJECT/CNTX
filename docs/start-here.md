# Start here

[Start here](start-here.md) · [How it works](how-it-works.md) · [Workspace](workspace.md) · [Commands](commands.md) · [Security](security.md) · [All docs](README.md)

This page covers installation and your first useful result in one continuous
path. Start with a small test project that contains only files you are allowed
to read and share.

## 1. Check the requirements

You need:

- Python 3.11, 3.12, or 3.13;
- Git;
- Windows or Ubuntu for a fully tested path.

Other operating systems may work, but the live CI matrix does not prove them.
OPENCNTX needs no account, API key, database, cloud service, or AI provider.

## 2. Install the Alpha release

The current Alpha release is `v0.2.0`. OPENCNTX is not published on PyPI.

### Windows

Open PowerShell:

```powershell
git clone --branch v0.2.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
opencntx --help
```

If `python` is not found, install a supported Python version and make sure its
launcher is available in PowerShell. Do not use unofficial installers.

### Ubuntu

Open a terminal:

```bash
git clone --branch v0.2.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python3 -m pip install .
opencntx --help
```

Use a virtual environment when the system Python blocks local installation:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
opencntx --help
```

## 3. Confirm the installed version

```powershell
python -c "import opencntx; print(opencntx.__version__)"
```

The Alpha release prints `0.2.0`.

## 4. Open a small project

Leave the OPENCNTX source directory and open the project whose files you want
to package:

```powershell
cd path\to\your-project
```

## 5. Create the configuration

```powershell
opencntx init
```

This creates `opencntx.toml` and refuses to overwrite an existing one.

Set one narrow goal and review every pattern:

```toml
[task]
goal = "Explain why this small Python test fails"

[context]
include = ["README.md", "src/**/*.py", "tests/**/*.py"]
required = ["README.md"]
exclude = [".git/**", ".env*", "**/*.key", "**/*.pem"]
max_files = 25
max_bytes = 100000
```

## 6. Build the package

```powershell
opencntx pack
```

Successful output appears under `.opencntx/latest/`:

- `CONTEXT.md` contains the selected text;
- `manifest.json` records paths, sizes, and SHA-256 hashes.

## 7. Inspect every included byte

Open `.opencntx/latest/CONTEXT.md`. Confirm that:

- every file helps with the stated task;
- no password, token, personal data, or private material is present;
- the package is small enough to review;
- the goal is still correct.

## 8. Verify before use

```powershell
opencntx verify .opencntx/latest
```

Exit code `0` means the package and recorded source bytes still match. It does
not prove that the text is correct, safe, complete, or approved. A non-zero
result requires inspection.

## 9. Share only by choice

OPENCNTX never uploads the package. If you choose to use it with an AI tool,
you provide `CONTEXT.md` or selected contents yourself.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/docs/core-flow-dark.svg">
  <img src="../assets/docs/core-flow.svg" alt="Initialize, pack, inspect, verify, and only then decide whether to share">
</picture>

## 10. Create a workspace when the project grows

The basic package flow is enough for one bounded task. For a longer project:

```powershell
opencntx workspace init my-project
opencntx workspace control refresh --root my-project
opencntx workspace capture README.md --root my-project --origin OWNER
```

Read [Workspace](workspace.md) before adding chapters, tasks, playbooks, roles,
or executor packages.

## Upgrade or remove OPENCNTX

For an upgrade, clone the next approved tag into a fresh directory and install
it there. Replacing files in an old clone is not a clean-upgrade proof.

To remove the package from the active Python environment:

```powershell
python -m pip uninstall opencntx
```

This does not remove your projects, workspaces, or context packages. Delete
those separately only after reviewing the exact target.

## If something fails

Use [Troubleshooting](troubleshooting.md) for installation, path, budget,
digest, stale-chapter, context, and task errors. Use [Support](../SUPPORT.md)
for ordinary questions and reproducible bugs.

## Next pages

- [How it works](how-it-works.md) — understand the full mental model.
- [Core commands](core.md) — learn exact `init`, `pack`, and `verify` behavior.
- [Context packages](context-packets.md) — understand budgets and drift.
- [Security](security.md) — understand the local trust boundary.
