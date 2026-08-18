# Getting started

This guide creates one small context package in about five minutes. Start in a
test project that contains only files you are comfortable reading and sharing.

## 1. Open your project directory

```powershell
cd path\to\your-project
```

## 2. Create the configuration

```powershell
opencntx init
```

This creates `opencntx.toml` without overwriting an existing file.

## 3. Set one clear goal

Edit the file:

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

Keep the goal narrow. Include only files that can help with that goal.

## 4. Build the package

```powershell
opencntx pack
```

Successful output is written under `.opencntx/latest/`:

- `CONTEXT.md` contains the selected text;
- `manifest.json` records paths, sizes, and SHA-256 hashes.

## 5. Inspect it yourself

Open `.opencntx/latest/CONTEXT.md`. Check that:

- every included file belongs to the task;
- no password, token, personal data, or private material is present;
- the total amount of context is small enough to review;
- the task goal is still correct.

## 6. Verify before use

```powershell
opencntx verify .opencntx/latest
```

Exit code `0` means the package and its recorded local sources still match.
A non-zero result means you must inspect the reported drift or error.

## 7. Share only by choice

OPENCNTX never uploads the package. If you decide to use it with an AI tool,
you provide `CONTEXT.md` or its relevant contents yourself.

![The safe core flow is initialize, pack, inspect, verify, and then choose whether to share](../assets/docs/core-flow.svg)

## What to read next

- [Core commands](core.md) explains exact behavior and exit codes.
- [Context packages](context-packets.md) explains budgets and drift.
- [Workspace](workspace.md) starts the larger project workflow.
- [Security](security.md) explains the trust boundary.

[Documentation home](README.md)
