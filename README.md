# CNTX

CNTX is an open-source framework for intelligent task delegation, context isolation, compact project and workstream state, and verifiable collaboration between people and specialized AI agents.

## Mission

Complex work needs clear boundaries: tasks should be decomposed, each participant should receive only the minimal context needed, and decisions should be supported by explicit contracts and evidence. CNTX exists to provide a public foundation for those practices while preserving human authority for approval and final decisions.

CNTX is model-, vendor-, runtime-, and domain-agnostic. It does not prescribe a specific AI provider, execution environment, industry, or private implementation.

## Principles

- Decompose work into small, explicit tasks.
- Use minimal context and isolate context between workstreams.
- State contracts, assumptions, evidence, approvals, and handoffs clearly.
- Keep people in authority for consequential decisions and merges.
- Treat security, privacy, and scope boundaries as first-class constraints.

## Project status and roadmap

CNTX is in an early foundation phase. The repository has an accepted public governance and collaboration foundation. Its first conceptual architecture contract is accepted in the [architecture documentation](docs/architecture/README.md); it does not claim implemented runtime or product functionality.

The [artifact-contract index](docs/contracts/README.md) includes nine accepted, binding subordinate artifact-specific contracts: Project Charter, Workstream, Task Contract, Context Packet, Execution Result, Evidence Bundle, Review Record, Decision Record, and State Snapshot. None introduces an executable schema, template, validator, state engine, synchronization engine, workflow, runtime, or product functionality. No canonical artifact contract remains listed as future work; the accepted status does not authorize a follow-on phase. CNTX remains a public core that is model-, vendor-, runtime-, and domain-agnostic and remains independent of private reference implementations.

The high-level roadmap is to define public concepts and documentation, invite review under the project governance, and only then consider scoped, approved implementation work. Private reference implementations may exist later outside this public repository.

## Participate

- Read [Contributing](CONTRIBUTING.md) before proposing non-trivial work.
- See [Governance](GOVERNANCE.md) for authority, decisions, and review.
- Follow [Security](SECURITY.md) for responsible disclosure.
- Coding agents must follow [AGENTS.md](AGENTS.md).

## Public-repository boundary

Private project data, secrets, credentials, personal data, production configurations, and production automation do not belong in this public repository. Do not submit them in commits, pull requests, issues, or discussion.
