# Troubleshooting

[Start here](start-here.md) · [How it works](how-it-works.md) · [Workspace](workspace.md) · [Commands](commands.md) · [Security](security.md) · [All docs](README.md)

Start with the smallest failing command. Read its complete output and keep the
first stable error message.

## `opencntx` is not found

Verify the installation environment:

```powershell
python -c "import opencntx; print(opencntx.__version__)"
python -m pip show opencntx
```

Activate the virtual environment where you installed the package, or reinstall
from the approved tag using [Start here](start-here.md).

## `init` refuses to continue

An `opencntx.toml` probably already exists. OPENCNTX does not overwrite it.
Open and review the existing file instead of deleting it automatically.

## `pack` reports a missing required file

Check the path relative to the project root and the `required` list. File name
case can matter on Linux.

## A budget is exceeded

Do not increase the budget automatically. Narrow the task, remove unrelated
include patterns, or add a deliberate exclusion. The package must fit as a
complete set.

## A file is rejected as binary or invalid UTF-8

The core accepts local UTF-8 text only. Convert the file outside OPENCNTX after
review, or use the media registration flow for already produced UTF-8 text.
OPENCNTX does not perform extraction itself.

## `verify` reports changed or missing sources

The package no longer matches the current project files. Decide whether the
old snapshot is still correct. If not, inspect the changed sources and rebuild
the package.

## A workspace command reports a wrong digest

Do not copy a digest from an older revision. Run the relevant read-only status
or verify command, inspect the current official record, and use the exact value
required by the next approved step.

## A chapter is `STALE` or `INCOMPLETE`

Check its source pins and dependencies. Create or accept the required revision,
then rebuild the catalog. Do not edit the SQLite database directly.

## Context cannot be built

Confirm that:

- the task is exactly `IN_EXECUTION`;
- required chapters are current and accepted;
- the catalog reflects the latest official files;
- source privacy is allowed;
- control and task digests match;
- the byte budget is sufficient for the complete selected set.

## A task becomes `BLOCKED`

Three equal failure signatures reached the anti-deadloop limit. Stop. Preserve
the evidence and ask the OWNER for a new decision. Do not create an automatic
retry loop.

## Need more help?

Use [Support](../SUPPORT.md) for ordinary questions and reproducible bugs. Use
GitHub's private vulnerability route for security issues.

[Documentation home](README.md)
