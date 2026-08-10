<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-logo-light.svg">
    <img alt="CNTX — bounded context, verifiable work, human authority" src="docs/assets/brand/cntx-logo-light.svg" width="520">
  </picture>
</p>

<p align="center"><strong>Bounded context. Verifiable work. Human authority.</strong></p>

<p align="center">
  <a href="README.md"><strong>Overview</strong></a> ·
  <a href="ROADMAP.md">Roadmap</a> ·
  <a href="docs/architecture/README.md">Architecture</a> ·
  <a href="docs/contracts/README.md">Contracts</a> ·
  <a href="docs/brand/README.md">Brand</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-status-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-status-light.svg">
    <img alt="Public Core complete · Open specification · Model and vendor agnostic · Apache-2.0" src="docs/assets/brand/cntx-status-light.svg">
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-collaboration-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-collaboration-light.png">
  <img alt="Distinct bounded context modules connect through explicit evidence paths to a central human authority" src="docs/assets/brand/cntx-collaboration-light.png">
</picture>

## What is CNTX?

CNTX is an open specification for organizing complex work between people and
specialized AI agents. It makes four things explicit:

1. **what work is allowed;**
2. **what minimum context is supplied;**
3. **what output and evidence are produced;**
4. **which human authority makes the consequential decision.**

The result is collaboration that can remain bounded, inspectable, reproducible,
and independent of any particular model, vendor, runtime, product, or domain.

## How CNTX works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-how-it-works-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-how-it-works-light.svg">
  <img alt="CNTX flow: define scope, supply context, perform bounded work, capture evidence, review, and make a human decision" src="docs/assets/brand/cntx-how-it-works-light.svg">
</picture>

| Principle | What it means |
| --- | --- |
| **Bounded** | A task has explicit scope, inputs, authority, limits, and stop conditions. |
| **Minimal** | Each participant receives only the relevant context it needs. |
| **Verifiable** | Outputs stay separate from evidence, review, and final decisions. |
| **Fail closed** | Missing, conflicting, ambiguous, unsupported, or unverifiable conditions stay visible. |
| **Human governed** | Automation never turns itself into approval or final authority. |

## The public artifact chain

CNTX defines nine canonical Artifact Types. Together they preserve intent,
context, execution claims, evidence, review, decisions, and bounded orientation
without pretending that one record proves another.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/cntx-artifact-chain-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/brand/cntx-artifact-chain-light.svg">
  <img alt="CNTX artifact chain from Project Charter and Workstream through Task Contract, Context Packet, Execution Result, Evidence Bundle, Review Record, Decision Record, and State Snapshot" src="docs/assets/brand/cntx-artifact-chain-light.svg">
</picture>

## What is available today?

| Public baseline | Included |
| --- | --- |
| Architecture | 33 Accepted architecture sources with corresponding ADRs |
| Artifact contracts | 9 Accepted contracts for the canonical Artifact Types |
| Executable schemas | 10 Accepted JSON Schema Draft 2020-12 resources at version `1.0.0` |
| Synthetic evidence | 203 cases: 38 valid and 165 invalid |
| Extension model | Accepted conceptual boundaries through ARCH-033 |
| Public release | Immutable, unsupported prerelease `0.1.0-prealpha.1` |

The initial Public-Core specification and prerelease cycle are complete. The
current baseline also includes the Accepted Extension Module and Profile
architecture through ARCH-033. See the full [status and roadmap](ROADMAP.md) for
the exact history, boundaries, and dependency-ordered future possibilities.

> [!IMPORTANT]
> CNTX currently provides a public specification foundation. It does **not**
> provide a concrete validator, resolver, runner, SDK, library, API, CLI,
> workflow, runtime, hosted service, supported release line, certification, or
> deployment. Repository presence or schema validity does not imply approval,
> correctness, conformance, security, support, or final authority.

## Start here

| If you want to… | Go to… |
| --- | --- |
| Understand the design in order | [Architecture index](docs/architecture/README.md) |
| Inspect the nine collaboration records | [Artifact-contract index](docs/contracts/README.md) |
| Explore executable JSON Schemas | [`schemas/`](schemas/) |
| Inspect positive and negative cases | [`tests/schemas/`](tests/schemas/) |
| Follow status, history, and future gates | [Roadmap](ROADMAP.md) |
| Understand release evidence | [Release index](docs/release/README.md) |
| Propose a governed change | [Contributing](CONTRIBUTING.md) and [Governance](GOVERNANCE.md) |
| Report a vulnerability | [Security](SECURITY.md) |

## Find CNTX

`AI collaboration` · `context engineering` · `task delegation` ·
`human-in-the-loop` · `evidence` · `governance` · `JSON Schema` ·
`multi-agent systems` · `vendor-neutral specification`

## Public-repository boundary

Private project data, secrets, credentials, personal data, production
configuration, and production automation do not belong in this repository.
Read [Security](SECURITY.md), [Governance](GOVERNANCE.md), and
[AGENTS.md](AGENTS.md) before contributing consequential work.

---

<p align="center">
  Apache-2.0 licensed · Public by design · Human authority preserved
</p>
