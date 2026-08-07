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

The architecture index includes the **Accepted**, documentation-only [Common Artifact Envelope schema boundary](docs/architecture/common-artifact-envelope-schema-boundary.md) with [ADR-0004](docs/architecture/adr/0004-common-artifact-envelope-schema-boundary.md). ARCH-004 classifies shared metadata ownership before any executable schema decision. Its acceptance authorizes no concrete fields, serialization, validator, Layer 5 mechanism, runtime, or follow-on implementation.

The architecture index also includes the **Accepted**, documentation-only [Common Artifact Envelope representation boundary](docs/architecture/common-artifact-envelope-representation-boundary.md) with [ADR-0005](docs/architecture/adr/0005-common-artifact-envelope-representation-boundary.md). ARCH-005 identifies what a future common definition must be capable of representing and the order of later schema-foundation decisions; it selects no fields, schema language, serialization, validator, runtime, or implementation and authorizes no follow-on phase.

The architecture index now includes the **Accepted**, documentation-only [Common Artifact Envelope schema identity and initial version policy](docs/architecture/common-artifact-envelope-schema-identity-version-policy.md) with [ADR-0006](docs/architecture/adr/0006-common-artifact-envelope-schema-identity-version-policy.md). ARCH-006 establishes one technology-neutral logical identity and reserves `1.0.0` only as the initial accepted version target for a future executable common definition. It creates no concrete Schema Identifier, executable schema, active Schema Version, schema-language or dialect choice, serialization, validator, Layer 5 mechanism, runtime, implementation, release, or deployment.

The architecture index now includes the **Accepted**, documentation-only [Common Artifact Envelope schema language and dialect](docs/architecture/common-artifact-envelope-schema-language-dialect.md) with [ADR-0007](docs/architecture/adr/0007-common-artifact-envelope-schema-language-dialect.md). ARCH-007 selects JSON Schema Draft 2020-12 and its standard vocabulary profile as a fixed processing model. It creates no executable schema, concrete `$id`, composition or packaging model, artifact Serialization Binding, validator, Layer 5 mechanism, runtime, implementation, release, or deployment; composition and packaging remain a separate later decision.

The architecture index now includes the **Accepted**, documentation-only [Common Artifact Envelope schema composition and packaging](docs/architecture/common-artifact-envelope-schema-composition-packaging.md) with [ADR-0008](docs/architecture/adr/0008-common-artifact-envelope-schema-composition-packaging.md). ARCH-008 selects one canonical root Schema Resource per version, internal `$defs`, static exact-version references, standalone canonical resources, optional identity-preserving Compound Schema Document bundles, and offline-first resolution without creating an executable schema, concrete `$id`, active Schema Version, artifact Serialization Binding, validator, runtime, implementation, release, or deployment.

The architecture index now includes the **Accepted** [Common Artifact Envelope executable schema definition](docs/architecture/common-artifact-envelope-executable-schema.md) with [ADR-0009](docs/architecture/adr/0009-common-artifact-envelope-executable-schema.md), the Accepted [`1.0.0` Schema Resource](schemas/common-artifact-envelope/1.0.0/schema.json), and its [synthetic test evidence](tests/schemas/common-artifact-envelope/1.0.0/cases.json). ARCH-009 defines a closed envelope object for the nine accepted Artifact Types, coupled artifact/contract/schema pins, optional provenance references, and optional digest evidence. Acceptance and schema validity do not authorize an artifact-specific schema or payload, select an artifact Serialization Binding, or provide a validator, resolver, runtime, product, release, or deployment.

The architecture index also contains the **Accepted**, documentation-only [Artifact-Specific Schema Family and Canonical Artifact Container Boundary](docs/architecture/artifact-specific-schema-family-container-boundary.md) with [ADR-0010](docs/architecture/adr/0010-artifact-specific-schema-family-container-boundary.md). The decision allocates nine technology-neutral artifact-specific logical Schema Identities and inactive `1.0.0` targets, selects a closed full-artifact root with mandatory `envelope` and `payload`, and fixes the exact Accepted common-envelope reference at `/envelope`. It creates no executable artifact-specific schema or payload, concrete artifact-specific `$id`, active Schema Version, binding, validator, runtime, implementation, release, or deployment; its acceptance authorizes no follow-on phase.

The architecture index now includes the **Accepted**, documentation-only [Canonical Contract Definition Identity, Initial Version, and Source Binding](docs/architecture/contract-definition-identity-version-binding.md) with [ADR-0011](docs/architecture/adr/0011-contract-definition-identity-version-binding.md). ARCH-011 allocates nine stable Contract Definition Identifiers, independent initial `1.0.0` versions, and exact Accepted-source bindings for CONTRACT-001 through CONTRACT-009. The nine integrated identifier/version/source-binding pairs are Accepted and active. The decision changes no contract meaning, creates no executable artifact-specific schema, binding, resolver, validator, runtime, implementation, release, or deployment, and grants no follow-on authority.

The architecture index now also exposes the **Accepted** [Project Charter Executable Schema Definition](docs/architecture/project-charter-executable-schema.md) with [ADR-0012](docs/architecture/adr/0012-project-charter-executable-schema.md), the Accepted [Project Charter Schema Version `1.0.0`](schemas/project-charter/1.0.0/schema.json), and its [synthetic validation cases](tests/schemas/project-charter/1.0.0/cases.json). ARCH-012 composes the exact Accepted Common Artifact Envelope with a closed CONTRACT-001 payload and exact Project Charter Artifact Type, governing Contract, and governing Schema pins. Governed integration to `main` activates the exact Schema Version. Acceptance, schema validity, or repository presence grants no contract conformance, authority, release, deployment, implementation, or authority for the next artifact-specific schema.

The architecture index now also exposes the **Accepted** [Workstream
Executable Schema Definition](docs/architecture/workstream-executable-schema.md)
with [ADR-0013](docs/architecture/adr/0013-workstream-executable-schema.md), the
Accepted [Workstream Schema Version `1.0.0`](schemas/workstream/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/workstream/1.0.0/cases.json).
ARCH-013 composes the exact Accepted Common Artifact Envelope with a closed
twelve-property CONTRACT-002 payload, exact Workstream Artifact Type and
governing-definition pins, and an opaque governing Project Charter
Artifact Instance/Revision pin without a Project Charter schema `$ref`.
Governed integration to `main` activates the exact Schema Version. Acceptance,
schema validity, or repository presence grants no contract conformance,
approval, authority, release, deployment, implementation, merge permission,
or Task Contract schema authority.

The architecture index now also exposes the **Proposed** [Task Contract
Executable Schema Definition](docs/architecture/task-contract-executable-schema.md)
with [ADR-0014](docs/architecture/adr/0014-task-contract-executable-schema.md),
the Proposed inactive [Task Contract Schema Version `1.0.0`](schemas/task-contract/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/task-contract/1.0.0/cases.json).
ARCH-014 composes the exact Accepted Common Artifact Envelope with a closed
eleven-property CONTRACT-003 payload, exact Task Contract Artifact Type and
governing-definition pins, and separate opaque governing Project Charter and
Workstream Artifact Instance/Revision pins without either artifact-specific
schema `$ref`. Scope, actions, resources, authority, context, evidence,
decisions, and lifecycle remain declarative. Creation, validation, review,
Draft PR status, or repository presence grants no acceptance, activation,
contract conformance, task authority, permission enforcement, integration,
release, deployment, implementation, merge permission, Context Packet schema
authority, or follow-on authority.

The high-level roadmap is to define public concepts and documentation, invite review under the project governance, and only then consider scoped, approved implementation work. Private reference implementations may exist later outside this public repository.

## Participate

- Read [Contributing](CONTRIBUTING.md) before proposing non-trivial work.
- See [Governance](GOVERNANCE.md) for authority, decisions, and review.
- Follow [Security](SECURITY.md) for responsible disclosure.
- Coding agents must follow [AGENTS.md](AGENTS.md).

## Public-repository boundary

Private project data, secrets, credentials, personal data, production configurations, and production automation do not belong in this public repository. Do not submit them in commits, pull requests, issues, or discussion.
