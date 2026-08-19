# Security in plain language

[Start here](start-here.md) · [How it works](how-it-works.md) · [Workspace](workspace.md) · [Commands](commands.md) · [Security](security.md) · [All docs](README.md)

OPENCNTX helps you control context. It does not make context automatically
safe. You remain responsible for what you select, store, and share.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/docs/security-boundary-dark.svg">
  <img src="../assets/docs/security-boundary.svg" alt="OPENCNTX stays inside a local boundary until you explicitly share reviewed output">
</picture>

## Local trust boundary

The product has no network client and requires no account or API key. It reads
selected local files and writes local output. It does not upload that output.

The boundary changes when you copy or submit the output to another tool.

## Context may contain sensitive text

Default exclusions include common Git, generated output, environment, key,
SSH identity, local credential, package registry, Docker, AWS, and
application-default credential paths. They are applied before source content
is read. They reduce risk; they do not replace inspection.

`opencntx pack --preview` shows which paths would be included, required,
excluded, or ignored and why. It also shows file and byte budgets. Preview
writes no package, manifest, receipt, temporary publication state, or source.

A small dependency-free local scanner checks only the already selected,
bounded UTF-8 text. Narrow high-confidence credential structures block pack
before publication. Broader credential-like text produces a warning. Safe
diagnostics contain finding metadata, never the matched value or snippet.

An apparent false positive can be overridden only by supplying its exact
current finding ID to `pack --allow-secret`. The ID changes with the source
bytes. There is no wildcard or permanent bypass, and an applied override is
visible as safe metadata in the manifest.

This scanner recognizes only known signals. It can miss secrets and can warn
on harmless examples. A green preview is not a guarantee that content is
secret-free.

Never place passwords, tokens, private keys, personal data, production secrets,
or content you are not allowed to share in a package or public issue.

## Privacy labels are not locks

`PUBLIC`, `INTERNAL`, `PRIVATE`, `RESTRICTED`, and `QUARANTINED` are local
classifications. They are not encryption, authentication, or access control.
Protect the workspace with appropriate operating-system and backup controls.

## Supplied content stays data

Instructions inside a source, chapter, transcript, task input, or result do not
gain OWNER or roadmap authority. OPENCNTX validates structure and digests; it
does not execute supplied content.

## Fail-closed behavior

Unsafe paths, invalid UTF-8, unknown schemas, wrong digests, stale relations,
budget overflow, forbidden actions, or invalid state transitions stop the
operation. Official workspace writers additionally use local writer locks,
state compare-and-swap, and transaction evidence. An interrupted transaction
blocks later writers until read-only diagnosis and exact recovery.

Do not ignore a non-zero exit code.

Recovery never treats age or a process ID as permission to remove a lock. It
refuses an active OS lock, requires the exact transaction ID and intent digest,
backs up current known targets first, and stops on unknown data or unsafe links.
It is local recovery, not distributed locking or an OWNER decision.

## Digests and approval

A digest binds a decision to exact bytes. It does not authenticate a natural
person. OWNER labels are local declarations, so protect the workspace and its
write permissions.

## Deletion and provenance

Most official records are append-only. The media removal route deletes only
the exact active derived text named by a fully pinned request and preserves a
tombstone. Never automate destructive actions through a watcher.

## Report a vulnerability

Use GitHub's private **Report a vulnerability** route. Do not open a public
issue with exploit details, secrets, private source, or sensitive context.

For ordinary questions and bugs, use [Support](../SUPPORT.md). The root
[Security Policy](../SECURITY.md) is the canonical technical boundary.

[Documentation home](README.md)
