<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-logo-light.svg">
    <img alt="CNTX — bounded context, verifiable work, human authority" src="docs/assets/brand/cntx-logo-light.svg" width="500">
  </picture>
</p>

<p align="center"><strong>Give AI clear context. Keep evidence. Let people decide.</strong></p>

<p align="center">
  <a href="README.md"><strong>Overview</strong></a> ·
  <a href="ROADMAP.md">Roadmap</a> ·
  <a href="docs/architecture/README.md">Architecture</a> ·
  <a href="docs/contracts/README.md">Contracts</a> ·
  <a href="schemas/README.md">Schemas</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-collaboration-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-collaboration-light.png">
  <img alt="Bounded context modules connect through explicit evidence paths to a separate human authority" src="docs/assets/brand/cntx-collaboration-light.png">
</picture>

## Why CNTX exists

AI can forget instructions, mix unrelated context, fill gaps with guesses, or
sound more certain than its evidence allows. CNTX is an open specification for
making AI-assisted work bounded, traceable, and reviewable.

| Common problem | CNTX response | Intended benefit |
| --- | --- | --- |
| Too much or unclear context | Give each task a small, explicit context packet | Less context mixing |
| Confident output without proof | Keep claims, evidence, uncertainty, and review separate | Unsupported conclusions stay visible |
| Unclear approval | Keep consequential decisions with identified people | No automatic self-approval |

CNTX does **not** promise perfect AI. It provides a vendor-neutral structure
for collaboration between people and specialized AI agents.

## One controlled path

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-how-it-works-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-how-it-works-light.svg">
  <img alt="Define the task, supply minimum context, perform bounded work, capture evidence, review the result, and let an identified human decide" src="docs/assets/brand/cntx-how-it-works-light.svg">
</picture>

Work does not become evidence by itself. Evidence does not become approval by
itself. A tool or AI agent never becomes final authority merely by producing a
result.

## What exists today

| Public foundation | Current state |
| --- | --- |
| Architecture | 39 Accepted decisions with 39 matching ADRs |
| Collaboration records | 9 Accepted artifact contracts |
| Machine-readable structure | 10 Accepted JSON Schema Draft 2020-12 resources at version `1.0.0` |
| Synthetic examples | 203 matched cases: 38 valid and 165 invalid |
| Bounded executable slice | Local offline validation plus 13 separate cross-record rules |
| Source and freshness layer | ARCH-038 and ARCH-039 Accepted and integrated as documentation-only Definitions |
| Public release | Immutable, unsupported prerelease `0.1.0-prealpha.1` |

> [!IMPORTANT]
> CNTX is a specification foundation with one bounded local practice slice,
> not a finished software product. It provides no supported SDK, API, hosted
> service, certification, complete conformance suite, or deployment. A valid
> schema, successful execution, or satisfied rule proves no truth, approval,
> security, broader conformance, release fitness, or final authority.

## Roadmap at a glance

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-roadmap-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-roadmap-light.svg">
  <img alt="CNTX roadmap: the public specification, bounded validation slice, and source and freshness Definitions are integrated; exact schema resources are the next governed technical decision; practical pilots follow only after further proof" src="docs/assets/brand/cntx-roadmap-light.svg">
</picture>

- **Now:** the specification foundation, bounded validation/integrity slice,
  and ARCH-038/ARCH-039 documentation layer are integrated.
- **Next:** reassess exact Definition Schema Resources, assertions, cases, and
  fixed expected results. This work is not started by the roadmap.
- **Later:** task/runtime controls, multiple principals, temporary context,
  one real vertical slice, adapters, and adversarial evaluation.

There is no promised completion date. Every consequential step requires its
own governed decision. See the [full roadmap and technical history](ROADMAP.md).

## Choose your route

| You want to… | Start here |
| --- | --- |
| Understand the design | [Architecture](docs/architecture/README.md) |
| See the nine collaboration records | [Artifact contracts](docs/contracts/README.md) |
| Inspect machine-readable structure | [JSON Schemas](schemas/README.md) |
| Review positive and negative examples | [Schema tests](tests/schemas/) |
| Inspect the bounded executable slice | [Validation and integrity slice](tools/minimal-validation-integrity-slice/README.md) |
| Follow current and future work | [Roadmap](ROADMAP.md) |
| Check the historical prerelease | [Release index](docs/release/README.md) |
| Propose a safe change | [Contributing](CONTRIBUTING.md) and [Governance](GOVERNANCE.md) |
| Report a vulnerability | [Security](SECURITY.md) |

## Public boundary

Never place private project data, secrets, credentials, personal data,
production configuration, or production automation in this public repository.
Read [Security](SECURITY.md), [Governance](GOVERNANCE.md), and
[AGENTS.md](AGENTS.md) before consequential work.

---

<p align="center">
  Open specification · Model and vendor agnostic · Apache-2.0 · Human authority preserved
</p>
