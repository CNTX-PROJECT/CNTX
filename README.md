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

The architecture index now also exposes the **Accepted** [Task Contract
Executable Schema Definition](docs/architecture/task-contract-executable-schema.md)
with [ADR-0014](docs/architecture/adr/0014-task-contract-executable-schema.md),
the Accepted [Task Contract Schema Version `1.0.0`](schemas/task-contract/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/task-contract/1.0.0/cases.json).
ARCH-014 composes the exact Accepted Common Artifact Envelope with a closed
eleven-property CONTRACT-003 payload, exact Task Contract Artifact Type and
governing-definition pins, and separate opaque governing Project Charter and
Workstream Artifact Instance/Revision pins without either artifact-specific
schema `$ref`. Scope, actions, resources, authority, context, evidence,
decisions, and lifecycle remain declarative. Governed integration to `main`
activates the exact Schema Version. Acceptance, schema validity, or repository
presence grants no contract conformance, task authority, permission
enforcement, integration authority, release, deployment, implementation,
merge permission, Context Packet schema authority, or follow-on authority.

The architecture index now also exposes the **Accepted** [Context
Packet Executable Schema Definition](docs/architecture/context-packet-executable-schema.md)
with [ADR-0015](docs/architecture/adr/0015-context-packet-executable-schema.md),
the Accepted [Context Packet Schema Version `1.0.0`](schemas/context-packet/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/context-packet/1.0.0/cases.json).
ARCH-015 composes the exact Accepted Common Artifact Envelope with a closed
thirteen-property CONTRACT-004 payload, exact Context Packet Artifact Type and
governing-definition pins, and one opaque governing Task Contract Artifact
Instance/Revision pin without any artifact-specific schema `$ref`. Source
references, representation treatments, relevance, freshness, access,
sufficiency, minimization, stop, and lifecycle information remain declarative.
The resource provides no automatic selection, retrieval, ranking, RAG,
disclosure, transformation, prompt, workflow, or runtime behavior. Governed
integration to `main` activates the exact Schema Version. Acceptance, schema
validity, or repository presence grants no contract conformance, task
authority, source access, retrieval or disclosure permission, merge permission,
release, deployment, Execution Result schema authority, or follow-on authority.

The architecture index now also exposes the **Accepted** [Execution Result
Executable Schema Definition](docs/architecture/execution-result-executable-schema.md)
with [ADR-0016](docs/architecture/adr/0016-execution-result-executable-schema.md),
the Accepted [Execution Result Schema Version `1.0.0`](schemas/execution-result/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/execution-result/1.0.0/cases.json).
ARCH-016 composes the exact Accepted Common Artifact Envelope with a closed
fourteen-property CONTRACT-005 payload, one opaque governing Task Contract
pin, and explicit opaque Context Packet pin declarations without any
artifact-specific schema `$ref`. Output, action, resource, provenance, check,
criteria, limitation, stop, security/privacy, and traceability values remain
bounded evidentiary claims. Governed integration to `main` activates the exact
Schema Version. Acceptance, schema validity, or repository presence grants no
correctness, completion, contract conformance, integration authority, release,
deployment, merge permission, Evidence Bundle schema authority, or follow-on
authority.

The architecture index now also exposes the **Accepted** [Evidence Bundle
Executable Schema Definition](docs/architecture/evidence-bundle-executable-schema.md)
with [ADR-0017](docs/architecture/adr/0017-evidence-bundle-executable-schema.md),
the Accepted [Evidence Bundle Schema Version `1.0.0`](schemas/evidence-bundle/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/evidence-bundle/1.0.0/cases.json).
ARCH-017 composes the exact Accepted Common Artifact Envelope with a closed
fifteen-property CONTRACT-006 payload, one opaque governing Task Contract pin,
exact reviewable-subject declarations, explicit opaque artifact relationships,
Evidence Items, claim traceability, and bounded provenance, quality,
limitation, security/privacy, and lifecycle declarations without any
artifact-specific schema `$ref`. The accepted resource implements no collection,
retrieval, scoring, verification, access, disclosure, approval, acceptance,
workflow, release, deployment, or merge mechanism. Creation, validation,
review, schema validity, or repository presence grants no contract conformance,
source truth, relevance, sufficiency, correctness, acceptance, integration,
release, deployment, merge permission, Review Record schema authority, or
follow-on authority. Governed integration to `main` activates the exact Schema
Version; acceptance and activation authorize no Review Record schema or other
follow-on work.

The architecture index now also exposes the **Accepted** [Review Record
Executable Schema Definition](docs/architecture/review-record-executable-schema.md)
with [ADR-0018](docs/architecture/adr/0018-review-record-executable-schema.md),
the Accepted [Review Record Schema Version `1.0.0`](schemas/review-record/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/review-record/1.0.0/cases.json).
ARCH-018 composes the exact Accepted Common Artifact Envelope with a closed
sixteen-property CONTRACT-007 payload, separates Review Authority and Execution
Authority, and records exact reviewable subjects, nine opaque artifact
relationship categories, findings, evidence use, uncertainty, dissent,
recommendations, peer review, correction, security/privacy, escalation, stop,
and lifecycle traceability without any artifact-specific schema `$ref`. The
accepted resource implements no reviewer identity or specialty system, review,
retrieval, scoring, severity, confidence, verdict, approval, voting, synthesis,
decision, workflow, runtime, access, disclosure, retention, release,
deployment, or merge mechanism. Creation, validation, review, schema validity,
or repository presence grants no contract conformance, specialist authority,
review quality, acceptance, integration, release, deployment, merge permission,
Decision Record schema authority, or follow-on authority. Governed integration
to `main` activates the exact Schema Version under issue #62 and EIGENAAR
acceptance comment `5218629573`; acceptance and activation authorize no
Decision Record schema or other follow-on work.

The architecture index now also exposes the **Accepted** [Decision Record
Executable Schema Definition](docs/architecture/decision-record-executable-schema.md)
with [ADR-0019](docs/architecture/adr/0019-decision-record-executable-schema.md),
the Accepted [Decision Record Schema Version `1.0.0`](schemas/decision-record/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/decision-record/1.0.0/cases.json).
ARCH-019 composes the exact Accepted Common Artifact Envelope with a closed
seventeen-property CONTRACT-008 payload and preserves exact authority and
approved-revision provenance, one bounded question and outcome, basis, nine
opaque artifact relationships, inputs, timing, scope, consequences, downstream
boundaries, peer changes/conflicts, roles, external records, security/privacy,
restricted basis, lifecycle, and history without any artifact-specific schema
`$ref`. The accepted resource allocates no authority or identity, proves no approval,
makes or executes no decision, changes no state, and implements no retrieval,
reasoning, recommendation, voting, conflict-resolution, workflow, runtime,
access, disclosure, retention, acceptance, integration, release, deployment,
publication, or merge mechanism. Creation, validation, review, schema validity,
or repository presence grants no acceptance, activation, State Snapshot schema,
or follow-on authority. Governed integration to `main` activates the exact
Schema Version under issue #64 and EIGENAAR acceptance comment `5219310944`;
acceptance and activation authorize no State Snapshot schema or other follow-on
work.

The architecture index now also exposes the **Accepted** [State Snapshot
Executable Schema Definition](docs/architecture/state-snapshot-executable-schema.md)
with [ADR-0020](docs/architecture/adr/0020-state-snapshot-executable-schema.md),
the [State Snapshot Schema Version `1.0.0`](schemas/state-snapshot/1.0.0/schema.json),
and its [synthetic validation cases](tests/schemas/state-snapshot/1.0.0/cases.json).
ARCH-020 composes the exact Accepted Common Artifact Envelope with a closed
eighteen-property CONTRACT-009 payload and preserves Derived/non-authoritative
classification, controlling sources and exact revisions or pinning
limitations, provenance, temporal/freshness separation, reported state and
claims, evidence/review/decision/integration traceability, nine artifact
relationships, uncertainty, incomplete work and stops, snapshot history, five
peer relations, bounded handoff, security/privacy, and non-automatic lifecycle
effects without any artifact-specific schema `$ref`. The accepted resource
allocates no authority or identity, proves no source or claim, retrieves no content,
calculates no freshness, resolves no conflict, changes or synchronizes no state,
and implements no workflow, runtime, access, disclosure, retention,
verification, release, deployment, publication, or merge mechanism. Creation,
validation, review, schema validity, or repository presence did not grant
acceptance or activation. Exact-head acceptance is recorded in issue comment
`5219885650`; governed integration to `main` activates the exact Schema Version.
Acceptance and activation authorize no further phase automatically.

The **Accepted** [CNTX Public Core Completion Boundary and Remaining Layer
Roadmap](docs/architecture/public-core-completion-boundary-roadmap.md) with
[ADR-0021](docs/architecture/adr/0021-public-core-completion-boundary-roadmap.md)
under issue #68 and EIGENAAR acceptance comment `5220966638` records that the
contract-and-schema foundation is complete while portable
Serialization Binding, schema-resource resolution/catalog, validation output,
conformance evidence, and release-readiness remain separately governed future
decisions. The Accepted decision does not make CNTX release-ready and authorizes no
implementation, runtime, product, release, publication, deployment, or
follow-on work.

The architecture index also exposes the **Accepted** [CNTX Core Artifact
Serialization Binding Architecture](docs/architecture/core-artifact-serialization-binding.md)
(ARCH-022)
with [ADR-0022](docs/architecture/adr/0022-core-artifact-serialization-binding.md)
under issue #70 and EIGENAAR acceptance comment `5221466569`. The
documentation-only decision defines one logical Core Artifact JSON binding
identity and initial Binding Version `1.0.0`, activated by governed integration,
RFC 8259 `application/json`, UTF-8 without BOM, duplicate-name rejection,
bounded number and Unicode handling, non-semantic object ordering and
whitespace, preserved array order, explicit absence of canonicalization,
one-artifact document boundaries, separated error layers, compatibility, and
security/privacy limits. The Accepted binding changes no Accepted contract, schema, test,
identity, or version and creates no Artifact Instance, canonical JSON,
resolver, validator, conformance tooling, implementation, release,
publication, deployment, acceptance, merge permission, or follow-on authority.

The architecture index also exposes the **Accepted** [CNTX Schema Resource
Resolution and Catalog
Boundary](docs/architecture/schema-resource-resolution-catalog-boundary.md)
(ARCH-023) with
[ADR-0023](docs/architecture/adr/0023-schema-resource-resolution-catalog-boundary.md)
under issue #72, attributable EIGENAAR creation-authority comment `5221792750`,
and EIGENAAR acceptance comment `5222126273`. The documentation-only decision
defines exact Schema Identifier/Version keys, a
frozen caller-supplied context, a non-authoritative catalog view, closed
offline-first supply, no automatic network retrieval, exact transitive
resource closure, fail-closed missing/ambiguous/conflicting/wrong-version
handling, determinism, provenance, and security/privacy boundaries. The
Accepted decision changes no Accepted contract, architecture, schema, test,
identity, version, or Core Artifact JSON Binding and creates no executable
catalog, resolver, registry, cache, bundler, validator, validation output,
conformance tool, implementation, release, publication, deployment,
acceptance, merge permission, or follow-on authority.

The architecture index also exposes the **Accepted** [CNTX Validation and
Validation Output
Contract](docs/architecture/validation-and-validation-output-contract.md)
(ARCH-024) with
[ADR-0024](docs/architecture/adr/0024-validation-and-validation-output-contract.md)
under issue #74, attributable EIGENAAR creation-authority comment `5222505304`,
and EIGENAAR acceptance comment `5222756874`. The documentation-only decision
defines a frozen validation context, six separate conformance dimensions,
logical phases and dependencies,
four conceptual outcomes, fail-closed claim rules, diagnostic and limitation
boundaries, its relationship to JSON Schema Draft 2020-12 output,
reproducibility responsibilities, and security/privacy/non-authority limits.
The Accepted decision creates no output identity, field, schema, portable
error/severity vocabulary, universal result, validator, conformance tool,
Artifact Instance, portable evidence, implementation, release, publication,
deployment, acceptance, merge permission, or follow-on authority.

The architecture index now also exposes the **Accepted** [CNTX Portable
Conformance Evidence
Boundary](docs/architecture/portable-conformance-evidence-boundary.md)
(ARCH-025) with
[ADR-0025](docs/architecture/adr/0025-portable-conformance-evidence-boundary.md)
under issue #76 and attributable EIGENAAR creation-authority comment
`5223043068`, and EIGENAAR acceptance comment `5223192303`. The
documentation-only decision defines exactly scoped,
version-bound, provenance-bearing, offline-first, independently reassessable
conformance evidence; twelve logical evidence responsibilities;
claim/evidence/requirement traceability; validation-output and Evidence Bundle
separation; fail-closed evidence gaps; six conformance-target evidence
boundaries; reproduction, conflict, security/privacy, disclosure, and non-
authority limits. It creates no evidence Artifact Instance, Conformance Claim
artifact, field, schema, manifest, package, serialization, protocol, validator,
test runner, suite, score, badge, certification, supported-version claim,
release-readiness decision, implementation, release, publication, deployment,
acceptance, merge permission, or follow-on authority.

The high-level roadmap is to define public concepts and documentation, invite review under the project governance, and only then consider scoped, approved implementation work. Private reference implementations may exist later outside this public repository.

## Participate

- Read [Contributing](CONTRIBUTING.md) before proposing non-trivial work.
- See [Governance](GOVERNANCE.md) for authority, decisions, and review.
- Follow [Security](SECURITY.md) for responsible disclosure.
- Coding agents must follow [AGENTS.md](AGENTS.md).

## Public-repository boundary

Private project data, secrets, credentials, personal data, production configurations, and production automation do not belong in this public repository. Do not submit them in commits, pull requests, issues, or discussion.
