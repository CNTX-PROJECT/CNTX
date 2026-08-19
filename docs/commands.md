# Command reference

[Start here](start-here.md) · [How it works](how-it-works.md) · [Workspace](workspace.md) · [Commands](commands.md) · [Security](security.md) · [All docs](README.md)

This navigation table preserves the 42 documented CLI paths: four orientation
help routes and all 38 executable routes from the real parser. It does not invent options or grant
permission to run a workflow step. Use the exact nested `--help` output for
required arguments and repeatable options.

| # | Command path | Purpose |
|---:|---|---|
| 1 | `opencntx --help` | show top-level orientation without changing a project |
| 2 | `opencntx workspace --help` | show workspace command groups |
| 3 | `opencntx workspace media --help` | show media routes |
| 4 | `opencntx workspace task --help` | show task lifecycle routes |
| 5 | `opencntx init` | create a readable core configuration |
| 6 | `opencntx pack` | build one bounded core context package |
| 7 | `opencntx verify` | verify a core package and its source drift |
| 8 | `opencntx workspace init` | create a new local project workspace |
| 9 | `opencntx workspace capture` | store one supplied source byte-for-byte |
| 10 | `opencntx workspace control refresh` | refresh the derived current-roadmap snapshot |
| 11 | `opencntx workspace chapter create` | create one new draft chapter with source pins |
| 12 | `opencntx workspace catalog rebuild` | rebuild the derived local catalog and index |
| 13 | `opencntx workspace media register` | register supplied derived UTF-8 text |
| 14 | `opencntx workspace media review` | record review of one exact derived text object |
| 15 | `opencntx workspace media promote` | capture accepted derived text with provenance |
| 16 | `opencntx workspace media status` | report current derivation state read-only |
| 17 | `opencntx workspace media verify` | verify source, record, review, and text bindings |
| 18 | `opencntx workspace media remove` | remove exact active derived bytes with a tombstone |
| 19 | `opencntx workspace playbook register` | register a proposed playbook revision |
| 20 | `opencntx workspace playbook approve` | approve one exact playbook definition |
| 21 | `opencntx workspace playbook status` | report playbook state read-only |
| 22 | `opencntx workspace playbook verify` | verify playbook records and definition digests |
| 23 | `opencntx workspace role register` | register a proposed role revision |
| 24 | `opencntx workspace role approve` | approve one exact role definition |
| 25 | `opencntx workspace role status` | report role state read-only |
| 26 | `opencntx workspace role verify` | verify role records and definition digests |
| 27 | `opencntx workspace executor prepare` | bind task, context, playbook, and role |
| 28 | `opencntx workspace executor status` | report executor package state read-only |
| 29 | `opencntx workspace executor verify` | verify assignment and permission bindings |
| 30 | `opencntx workspace context build` | build one deterministic task-bound package |
| 31 | `opencntx workspace context verify` | verify live task and context bindings read-only |
| 32 | `opencntx workspace task propose` | append one exact task proposal |
| 33 | `opencntx workspace task approve` | append exact OWNER proposal approval |
| 34 | `opencntx workspace task begin` | move one approved task into execution |
| 35 | `opencntx workspace task submit-result` | append one result and evidence binding |
| 36 | `opencntx workspace task review-result` | append an ARCHITECT review |
| 37 | `opencntx workspace task accept-result` | append the exact OWNER result decision |
| 38 | `opencntx workspace task close` | close an accepted task |
| 39 | `opencntx workspace task status` | report current task state read-only |
| 40 | `opencntx workspace task record-attempt` | append one stable failure signature |
| 41 | `opencntx workspace task cancel` | terminate a task explicitly as cancelled |
| 42 | `opencntx workspace task supersede` | terminate a task in favor of a named successor |

## Core pack options

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

## Compact current roadmap control

Refresh a supported marked current block with:

```powershell
opencntx workspace control refresh --root my-project
```

The snapshot is derived. It does not edit, interpret, approve, or synchronize
the official roadmap.

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
- [Workspace](workspace.md)
- [OWNER flow](owner-flow.md)
- [Troubleshooting](troubleshooting.md)

[Documentation home](README.md)
