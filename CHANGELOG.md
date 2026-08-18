# Changelog

All notable OPENCNTX changes are recorded here.

## Unreleased

### Changed

- Reorganized the public documentation into separate task-focused English
  pages for beginners, workspace users, project owners, and technical readers.
- Replaced the original network-style brand with a simple modern text system:
  purple `OPEN`, near-black `CNTX` on light surfaces, and white `CNTX` on dark
  surfaces.
- Added accessible diagrams for the core flow, workspace, OWNER flow, context
  selection, security boundary, and public roadmap.

No product code, command, schema, dependency, workflow, package version, or
runtime behavior changed in this documentation and brand update.

## 0.2.0 - 2026-08-18

### Added

- A local workspace storage foundation that records supplied files byte-for-
  byte with privacy label, origin, SHA-256, and receipt.
- Immutable chapter revisions and a fully rebuildable local catalog for
  sources, dependencies, freshness, and `CURRENT` state.
- Append-only task records with separate exact OWNER approval for proposal and
  result, closure only after acceptance, and a bounded anti-deadloop stop.
- A deterministic task-bound context navigator that follows only explicitly
  pinned control, task, chapter, playbook, role, and source relationships.
- An automatic compact control snapshot from one exactly marked current
  roadmap block while retaining the full roadmap digest.
- Safe registration, review, promotion, and removal of already supplied
  derived UTF-8 text without performing OCR, transcription, or AI processing.
- Proposed and exactly approved playbooks and roles, with at most one local
  executor package that does not start a person, process, tool, AI, or agent.
- Public documentation, community files, deterministic brand assets, and a
  bounded six-job CI matrix.

### Validated

- The release candidate passed exactly 159 tests on Windows and Ubuntu with
  `ResourceWarning` treated as an error.
- Six live CI matrix jobs are evidence only on the exact candidate or merge
  commit.
- A private practical test confirmed that task context remained small,
  findable, traceable, and useful, and that one deliberate failure stopped
  without retry or partial execution.

### Known limitations

- OPENCNTX performs no AI call, automatic summary, OCR, transcription,
  embedding, vector search, knowledge graph, agent start, or process execution.
- The control snapshot does not synchronize Obsidian, GitHub, or another
  external store and does not interpret the official roadmap.
- There is no cloud service, external database, watcher, GUI, MCP server, or
  PyPI publication.
- Live task context is verified while the task is `IN_EXECUTION`; after
  closure, the append-only chain, digests, result, evidence, and executor state
  form the historical completion proof.
- CI is `CI_ACTIVE` and bounded to Windows and Ubuntu with Python 3.11, 3.12,
  and 3.13. Only the live run on the exact commit counts as proof.

## 0.1.0 - 2026-08-16

The first public release of the local, provider-neutral OPENCNTX core.

### Added

- `opencntx init` for a small readable configuration template without
  overwriting an existing file.
- `opencntx pack` for deterministic selection and atomic publication of
  `CONTEXT.md` and `manifest.json`.
- `opencntx verify` for separate reporting of unchanged, changed, missing, and
  unexpected sources.
- Explicit include, required, and exclude patterns plus file and byte budgets.
- Relative source paths, byte sizes, and SHA-256 hashes in the manifest.
- Default exclusion of Git metadata, generated packages, environment paths,
  and common key files.
- Rejection of binary or unreadable input, path traversal, and symlink escape
  outside the project root.
- Local Windows and Ubuntu tests for the complete core flow.

### Known limitations

- Only local UTF-8 text files are supported.
- No PDF, Office, image, audio, or binary extraction.
- No automatic selection, summary, embedding, or ranking.
- No AI provider, agent, MCP server, GUI, cloud service, database, or hosting.
- The user must inspect the generated context package before sharing it.
