<div align="center">

# OPENCNTX

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/opencntx-wordmark-dark.svg">
  <img src="assets/brand/opencntx-wordmark-light.svg" width="640" alt="OPENCNTX — OPEN in purple, CNTX in black or white">
</picture>

**Small context. Clear evidence. Any model.**

[Start here](docs/start-here.md) · [How it works](docs/how-it-works.md) · [Advanced / Alpha workspace](docs/workspace.md) · [Commands](docs/commands.md) · [Security](docs/security.md) · [All docs](docs/README.md)

</div>

OPENCNTX is a small local command-line tool. It turns only the files you choose
into a reviewable context package for one AI task. Paths, sizes, and SHA-256
hashes show what was included and whether those bytes changed later.

It works without an account, API key, cloud service, or built-in AI model. You
may use the reviewed text files with any AI tool that accepts text or files.
OPENCNTX never sends them for you.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/docs/opencntx-overview-dark.svg">
  <img src="assets/docs/opencntx-overview.svg" alt="Select local files, review and verify a small context package, then decide whether to share it">
</picture>

## Start in four steps

OPENCNTX requires Python 3.11 or newer. The current Alpha release is `v0.2.0`.

### 1. Install the Alpha release

With `pipx` and Git already installed, one pinned command creates an isolated
tool environment:

```powershell
pipx install "git+https://github.com/CNTX-PROJECT/OPENCNTX.git@v0.2.0"
opencntx --version
opencntx --help
```

The source-checkout route remains available:

```powershell
git clone --branch v0.2.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
opencntx --version
opencntx --help
```

For contributor work on the current source:

```powershell
git clone --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

### 2. Create a configuration

Run this inside the project that contains the files you want to use:

```powershell
opencntx init
```

Open `opencntx.toml`. Set one clear goal and review the allowed file patterns
before continuing.

### 3. Preview, build, and inspect the package

```powershell
opencntx pack --preview
opencntx pack
```

Preview shows selected, required, excluded, and ignored paths, budgets, and
safe secret-signal metadata without writing a package. Then read
`.opencntx/latest/CONTEXT.md` yourself. Remove anything that does not belong in
the task.

### 4. Verify the exact bytes

```powershell
opencntx verify
```

A successful check proves that the recorded files still match. It does not
prove that the content is true, complete, safe, or approved.

The complete beginner route—including Windows, Ubuntu, removal, and common
errors—is on [Start here](docs/start-here.md). An explicit package path remains
available as `opencntx verify PATH`. Build and checksum details for contributors
are on [Release artifacts](docs/release-artifacts.md).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/docs/core-flow-dark.svg">
  <img src="assets/docs/core-flow.svg" alt="Initialize, preview and pack, inspect, verify, and only then decide whether to share">
</picture>

## Advanced / Alpha workspace

The core route above is complete; workspace concepts are not required for a
first context package. Longer projects can optionally use the existing Alpha
workspace for supplied sources, chapters, tasks, playbooks, roles, derived
text, and bounded executor packages. It remains advanced and may change within
the public Alpha contract.

Read [Advanced / Alpha workspace](docs/workspace.md) only when that extra
structure is useful. No workspace command starts an AI, agent, shell process,
OCR tool, transcription service, or external sync.

## Safety in one minute

- OPENCNTX reads only selected local UTF-8 text inside the project boundary.
- Known credential paths are excluded before reading. A small local scanner
  blocks narrow high-confidence signals and warns on broader signals, but it
  cannot prove that output is secret-free. Inspect every output file.
- Privacy labels classify content. They do not encrypt it or control access.
- A non-zero exit code means the requested operation was not fully proven.
- A hash proves byte identity, not truth, safety, completeness, or approval.
- Sharing is always your separate decision.

Read [Security in plain language](docs/security.md) first. The root
[Security Policy](SECURITY.md) is the canonical technical boundary. Report a
possible vulnerability privately through GitHub's **Report a vulnerability**
route, never in a public issue.

## Project status

| Item | Current public state |
|---|---|
| Release | [`v0.2.0`](https://github.com/CNTX-PROJECT/OPENCNTX/releases/tag/v0.2.0) |
| Package version | `0.2.0` |
| Python | 3.11, 3.12, and 3.13 |
| Tested systems | Windows and Ubuntu |
| CI | `CI_ACTIVE`, six required matrix jobs |
| Runtime dependencies | none |
| License | [Apache-2.0](LICENSE) |

OPENCNTX is not published on PyPI, and the existing `v0.2.0` release has no
wheel or sdist assets. Current-main builds are unpublished candidates because
`main` contains changes after that tag. See [Release artifacts](docs/release-artifacts.md)
for the exact boundary.

Only a successful live CI run on the exact commit proves those six jobs. See
the [changelog](CHANGELOG.md), [support routes](SUPPORT.md), and
[contribution guide](CONTRIBUTING.md) for project-specific details.
