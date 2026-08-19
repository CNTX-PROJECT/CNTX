# Command reference

[Start here](start-here.md) · [How it works](how-it-works.md) · [Advanced / Alpha workspace](workspace.md) · [Commands](commands.md) · [Security](security.md) · [All docs](README.md)

This navigation table documents 45 public CLI paths: five orientation and
version routes plus all 40 executable routes from the real parser. It does not invent options or grant
permission to run a workflow step. Use the exact nested `--help` output for
required arguments and repeatable options.

| # | Command path | Purpose |
|---:|---|---|
| 1 | `opencntx --help` | show top-level orientation without changing a project |
| 2 | `opencntx --version` | show the installed package version without requiring a subcommand |
| 3 | `opencntx workspace --help` | show workspace command groups |
| 4 | `opencntx workspace media --help` | show media routes |
| 5 | `opencntx workspace task --help` | show task lifecycle routes |
| 6 | `opencntx init` | create a readable core configuration |
| 7 | `opencntx pack` | build one bounded core context package |
| 8 | `opencntx verify` | verify a core package and its source drift |
| 9 | `opencntx workspace init` | create a new local project workspace |
| 10 | `opencntx workspace capture` | store one supplied source byte-for-byte |
| 11 | `opencntx workspace doctor` | diagnose active or interrupted writer transactions read-only |
| 12 | `opencntx workspace recover` | preview or apply one exact backup-first recovery |
| 13 | `opencntx workspace control refresh` | refresh the derived current-roadmap snapshot |
| 14 | `opencntx workspace chapter create` | create one new draft chapter with source pins |
| 15 | `opencntx workspace catalog rebuild` | rebuild the derived local catalog and index |
| 16 | `opencntx workspace media register` | register supplied derived UTF-8 text |
| 17 | `opencntx workspace media review` | record review of one exact derived text object |
| 18 | `opencntx workspace media promote` | capture accepted derived text with provenance |
| 19 | `opencntx workspace media status` | report current derivation state read-only |
| 20 | `opencntx workspace media verify` | verify source, record, review, and text bindings |
| 21 | `opencntx workspace media remove` | remove exact active derived bytes with a tombstone |
| 22 | `opencntx workspace playbook register` | register a proposed playbook revision |
| 23 | `opencntx workspace playbook approve` | approve one exact playbook definition |
| 24 | `opencntx workspace playbook status` | report playbook state read-only |
| 25 | `opencntx workspace playbook verify` | verify playbook records and definition digests |
| 26 | `opencntx workspace role register` | register a proposed role revision |
| 27 | `opencntx workspace role approve` | approve one exact role definition |
| 28 | `opencntx workspace role status` | report role state read-only |
| 29 | `opencntx workspace role verify` | verify role records and definition digests |
| 30 | `opencntx workspace executor prepare` | bind task, context, playbook, and role |
| 31 | `opencntx workspace executor status` | report executor package state read-only |
| 32 | `opencntx workspace executor verify` | verify assignment and permission bindings |
| 33 | `opencntx workspace context build` | build one deterministic task-bound package |
| 34 | `opencntx workspace context verify` | verify live task and context bindings read-only |
| 35 | `opencntx workspace task propose` | append one exact task proposal |
| 36 | `opencntx workspace task approve` | append exact OWNER proposal approval |
| 37 | `opencntx workspace task begin` | move one approved task into execution |
| 38 | `opencntx workspace task submit-result` | append one result and evidence binding |
| 39 | `opencntx workspace task review-result` | append an ARCHITECT review |
| 40 | `opencntx workspace task accept-result` | append the exact OWNER result decision |
| 41 | `opencntx workspace task close` | close an accepted task |
| 42 | `opencntx workspace task status` | report current task state read-only |
| 43 | `opencntx workspace task record-attempt` | append one stable failure signature |
| 44 | `opencntx workspace task cancel` | terminate a task explicitly as cancelled |
| 45 | `opencntx workspace task supersede` | terminate a task in favor of a named successor |

## Core pack options

Confirm the installed version without a subcommand:

```powershell
opencntx --version
```

Run the complete read-only selection, budget, and local secret-policy plan:

```powershell
opencntx pack --preview
```

Override only one exact current high-confidence finding reported by preview:

```powershell
opencntx pack --allow-secret FINDING_ID_FROM_PREVIEW
```

Repeat `--allow-secret` only when preview reports multiple exact findings that
you have separately reviewed. Unknown, duplicate, warning-only, or stale IDs
fail. Preview writes nothing and never grants persistent permission.

Verify the default package under the current directory:

```powershell
opencntx verify
```

This checks exactly `.opencntx/latest` and never searches upward. An explicit
`opencntx verify PATH` keeps the existing path-bound behavior.

## Public language and terminal contract

OPENCNTX uses English for fixed CLI help, errors, warnings, results, templates,
and generated headings. User-provided content and paths remain UTF-8. Fixed
tool text is ASCII-safe; when a narrow Windows console cannot represent a user
character, the CLI escapes that character instead of crashing or changing the
stored bytes.

## Advanced / Alpha: compact current roadmap control

Refresh a supported marked current block with:

```powershell
opencntx workspace control refresh --root my-project
```

The snapshot is derived. It does not edit, interpret, approve, or synchronize
the official roadmap.

## Advanced / Alpha: transaction diagnosis and recovery

Diagnose without writing, creating a lock, or repairing anything:

```powershell
opencntx workspace doctor --root my-project
```

If doctor reports `RECOVERY_REQUIRED`, copy its exact transaction ID and intent
SHA-256 into a preview:

```powershell
opencntx workspace recover --root my-project --transaction TXN-ID --intent-sha256 SHA256
```

The preview changes nothing. Apply only after inspecting the exact action:

```powershell
opencntx workspace recover --root my-project --transaction TXN-ID --intent-sha256 SHA256 --apply
```

Apply refuses an active writer, changed intent, unsafe link, unknown transaction
data, or changed target. It creates and verifies a retained local backup before
rolling the named transaction back and writes a recovery receipt.

## Find exact options

Add `--help` to the specific route, for example:

```powershell
opencntx workspace context build --help
opencntx workspace playbook register --help
```

## Exit codes

| Code | Meaning |
|---:|---|
| `0` | The requested operation completed and its checks passed |
| `1` | A read-only verification or status check found drift or invalid bindings |
| `2` | Arguments, input, configuration, paths, budgets, secret policy, or stored structure were invalid |

Treat every non-zero exit as a stop until you understand the reported result.
The core contract is explained in [Core commands](core.md#exit-codes).

## Important boundary

A documented command is not authority to approve a task, delete content,
publish a result, or bypass an OWNER gate. The active task records and exact
digests remain controlling.

## Related pages

- [Core commands](core.md)
- [Advanced / Alpha workspace](workspace.md)
- [OWNER flow](owner-flow.md)
- [Troubleshooting](troubleshooting.md)

[Documentation home](README.md)
