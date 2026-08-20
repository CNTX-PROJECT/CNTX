# Public roadmap

[Start here](start-here.md) · [How it works](how-it-works.md) · [Workspace](workspace.md) · [Commands](commands.md) · [Security](security.md) · [All docs](README.md)

This page reports completed public facts. It does not promise unapproved
features or expose private project records.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/docs/roadmap-dark.svg">
  <img src="../assets/docs/roadmap.svg" alt="OPENCNTX progressed from the three-command core through the workspace foundation to the current version 0.2 release">
</picture>

## Completed foundation

### Reset and small runnable core

- established the OPENCNTX project and provider-neutral boundary;
- added `init`, `pack`, and `verify`;
- proved the core flow on Windows and Ubuntu.

### Public v0.1.0

- released the deterministic three-command context package flow;
- documented explicit includes, exclusions, budgets, hashes, and drift;
- kept AI, network, cloud, GUI, and provider integrations out of scope.

### Workspace foundation

- byte-exact source capture and receipts;
- chapter revisions and replaceable local catalog;
- append-only tasks with separate OWNER gates;
- deterministic task-bound context navigation;
- safe registration of already derived UTF-8 text;
- proposed and approved playbooks and roles;
- bounded executor packages that do not start execution;
- compact current control snapshot for large roadmaps.

### Public v0.2.0

- released the complete current workspace foundation;
- activated six-job Windows and Ubuntu CI;
- added strict `main` protection and immutable release evidence;
- published security, community, documentation, and brand surfaces.

### Verifiable release preparation

- added clean, independent wheel and sdist candidate builds;
- separated byte-identical wheel proof from content-identical sdist proof;
- added exact SHA-256 and unsigned build-record verification;
- exercised install, core smoke, and uninstall on all six existing CI jobs;
- documented one pinned `pipx` route and kept publication behind a separate
  explicit decision.

### Local workspace transaction integrity

- added local single-writer workspace and task locks with exact state CAS;
- added durable transaction intent, phase, completion, and recovery evidence;
- added read-only interrupted-state diagnosis and explicit backup-first
  recovery bound to transaction ID and intent SHA-256;
- added real multiprocess conflict and forced-process-crash tests;
- centralized symlink, junction/reparse, containment, and directory-flush
  handling without adding a runtime dependency.

### Objective attempt and deadloop evidence

- replaced new free-text failure signatures with deterministic fingerprints
  from command, target, input-digest, exit-status, and error-class facts;
- bound attempts to one verified executor package, context manifest, allowed
  action, and copied local evidence;
- required digest-backed changed input or unique new evidence for a later
  attempt;
- added fixed semantic-repeat, total-attempt, cumulative-action, and
  cumulative-duration blocks with read-only status explanations;
- kept historical text attempts readable and kept execution, retry, truth
  attestation, and cryptographic identity outside the product claim.

## Current state

- Current release: `v0.2.0`
- Package version: `0.2.0`
- Maturity: Alpha
- Runtime dependencies: none
- CI: `CI_ACTIVE`
- Product focus: local, explicit, bounded, verifiable context
- Distribution: exact Git tag; no PyPI package or attached wheel/sdist assets

## Future work

No future feature is promised by this page. A next item becomes active only
after a separate bounded proposal, explicit OWNER approval, implementation,
tests, review, and merge.

Ideas are evaluated against the product boundary. AI calls, automatic agents,
cloud synchronization, OCR, transcription, embeddings, databases, GUI, MCP,
or other expansion are not implied roadmap commitments.

## Related pages

- [How it works](how-it-works.md)
- [Platforms](platforms.md)
- [Changelog](../CHANGELOG.md)
- [Contribution guide](../CONTRIBUTING.md)

[Documentation home](README.md)
