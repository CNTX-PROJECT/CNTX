# CNTX Architecture

## Reading guide

[The core architecture contract](core-contract.md) is the accepted normative conceptual architecture baseline for CNTX. It specifies public-core concepts and constraints, not an executable architecture. [ADR-0001](adr/0001-public-core-boundaries.md) records the accepted decision that establishes the public-core boundary. [The contract identity and versioning contract](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) are accepted additions: ARCH-001 remains the accepted core baseline, ARCH-002 is an accepted extension of that baseline, and [the artifact-contract and schema-layering contract](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) are the accepted ARCH-003 extension of that baseline. [The Common Artifact Envelope schema boundary](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) are the accepted ARCH-004 conceptual boundary for future common-envelope schema work; they do not alter existing artifact contracts or authorize executable schema work. [The Common Artifact Envelope representation boundary](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) are the accepted ARCH-005 documentation-only refinement that identifies future representation obligations and decision order without selecting fields, schema technology, serialization, validation, or implementation. [The Common Artifact Envelope schema identity and initial version policy](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) are the **Accepted**, documentation-only ARCH-006 allocation of one technology-neutral logical identity and the `1.0.0` initial accepted version target; they create no concrete Schema Identifier, executable schema, active Schema Version, schema-language choice, serialization, validation, runtime, or implementation. [The Common Artifact Envelope schema language and dialect](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) are the **Accepted**, documentation-only ARCH-007 selection of JSON Schema Draft 2020-12 with its standard vocabulary profile; they create no executable schema, concrete `$id`, composition or packaging model, artifact Serialization Binding, validator, runtime, or implementation. [The Common Artifact Envelope schema composition and packaging](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) are the **Accepted**, documentation-only ARCH-008 selection of one canonical root resource, internal `$defs`, static exact-version references, standalone canonical resources, derived identity-preserving bundles, and offline-first resolution; they create no executable schema, concrete `$id`, active Schema Version, artifact Serialization Binding, validator, runtime, or implementation. [The Common Artifact Envelope executable schema definition](common-artifact-envelope-executable-schema.md) and [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md) are the **Accepted** ARCH-009 binding of the one logical Common Artifact Envelope identity to JSON Schema Draft 2020-12 Schema Version `1.0.0`, with a closed six-property envelope, nine canonical Artifact Type tokens, coupled identity/version pins, optional provenance references, and optional digest evidence. Acceptance and schema validity do not define artifact-specific payload or relationships, select an artifact Serialization Binding, or provide authority, a validator, resolver, runtime, product, release, or deployment. The [`adr/`](adr/) directory is the location for architecture decision records. Accepted architecture governs the artifact-specific contracts listed in the [contract index](../contracts/README.md). CONTRACT-001, the Project Charter artifact contract, remains **Accepted** and is a binding, subordinate artifact-specific contract governed by ARCH-001, ARCH-002, and ARCH-003. CONTRACT-002, the Workstream artifact contract, remains **Accepted** and is a binding, subordinate artifact-specific contract governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001. CONTRACT-003, the [Task Contract artifact contract](../contracts/task-contract-artifact-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, accepted CONTRACT-001, and accepted CONTRACT-002. It does not alter or redefine accepted architecture, Project Charter, or Workstream. Only a separately approved change to the applicable higher architecture documents can alter that architecture.

CONTRACT-004, the [Context Packet artifact contract](../contracts/context-packet-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, and CONTRACT-003. It does not alter or redefine accepted architecture, Project Charter, Workstream, or Task Contract.

CONTRACT-005, the [Execution Result artifact contract](../contracts/execution-result-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, CONTRACT-003, and CONTRACT-004. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, or Context Packet.

CONTRACT-006, the [Evidence Bundle artifact contract](../contracts/evidence-bundle-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-005. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, or Execution Result.

CONTRACT-007, the [Review Record artifact contract](../contracts/review-record-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, or Evidence Bundle.

CONTRACT-008, the [Decision Record artifact contract](../contracts/decision-record-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-007. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, Evidence Bundle, or Review Record.

CONTRACT-009, the [State Snapshot artifact contract](../contracts/state-snapshot-contract.md), is **Accepted**, documentation-only, binding, and subordinate to accepted ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-008. It specializes State Snapshot semantics only and does not alter accepted architecture, any accepted artifact contract, or final human authority. CONTRACT-001 through CONTRACT-009 are **Accepted**.

This architecture documentation is read with the repository [README](../../README.md), [agent instructions](../../AGENTS.md), [governance](../../GOVERNANCE.md), and [security policy](../../SECURITY.md). The README describes the project and its current status. `AGENTS.md` sets execution constraints and source precedence. `GOVERNANCE.md` assigns decision authority and approval. Normative architecture states what the public core requires conceptually; governance assigns who may approve it; implementation is future conforming work; and non-binding discussion is neither an approved decision nor an authority source.

No executable runtime, selector, retrieval system, provider integration, validator, or product functionality is implemented here. ARCH-009 introduces one Accepted executable Common Artifact Envelope Schema Resource only; it is not an artifact-specific schema, a complete artifact definition, a Serialization Binding, or an implementation.

The [Artifact-Specific Schema Family and Canonical Artifact Container Boundary](artifact-specific-schema-family-container-boundary.md) and [ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md) are **Accepted**, documentation-only architecture. They allocate nine technology-neutral artifact-specific logical Schema Identities and inactive `1.0.0` targets, select one closed full-artifact root with mandatory `envelope` and `payload`, and pin the envelope location to the exact Accepted Common Artifact Envelope Schema Version `1.0.0`. They create no executable artifact-specific schema or payload, concrete artifact-specific `$id`, active Schema Version, binding, validator, runtime, implementation, release, or deployment; their acceptance authorizes no follow-on phase.

The [Canonical Contract Definition Identity, Initial Version, and Source Binding](contract-definition-identity-version-binding.md) and [ADR-0011](adr/0011-contract-definition-identity-version-binding.md) are **Accepted**, documentation-only architecture. They allocate exactly nine stable Contract Definition Identifiers, independent initial Contract Definition Version `1.0.0` values, and exact Accepted-source bindings for CONTRACT-001 through CONTRACT-009. The nine integrated identifier/version/source-binding pairs are Accepted and active. They change no accepted contract meaning, create no executable artifact-specific schema, binding, resolver, validator, runtime, implementation, release, or deployment, and authorize no follow-on phase.

The [Project Charter Executable Schema Definition](project-charter-executable-schema.md) and [ADR-0012](adr/0012-project-charter-executable-schema.md) are **Accepted** under issue #48 and Owner acceptance comment `5210242651`. They bind the logical Project Charter Artifact Schema Identity to a concrete Draft 2020-12 `$id` and Schema Version `1.0.0`, apply the exact Accepted Common Artifact Envelope at mandatory `/envelope`, constrain the exact Project Charter Artifact Type and governing-definition pins, and define a closed CONTRACT-001 payload with synthetic validation evidence. Governed integration to `main` activates that exact Schema Version. Acceptance and schema validity grant no contract conformance, approval, authority, release, deployment, or follow-on schema authority.

The [Workstream Executable Schema Definition](workstream-executable-schema.md)
and [ADR-0013](adr/0013-workstream-executable-schema.md) are **Accepted** under
issue #52 and Owner acceptance comment `5215029431`. They define one Draft
2020-12 resource with the exact
Accepted Common Artifact Envelope at mandatory `/envelope`, exact Workstream
Artifact Type and governing-definition pins, an opaque governing Project
Charter Artifact Instance/Revision pin, and a closed twelve-property
CONTRACT-002 payload. The resource contains no Project Charter schema `$ref`.
Governed integration to `main` activates that exact Schema Version. Acceptance,
schema validity, or repository presence grants no contract conformance,
approval, authority, release, deployment, merge permission, or Task Contract
schema authority.

The [Task Contract Executable Schema Definition](task-contract-executable-schema.md)
and [ADR-0014](adr/0014-task-contract-executable-schema.md) are **Accepted**
under issue #54 and Owner acceptance comment `5215700352`. They define one
Draft 2020-12 Task Contract Schema Version
`1.0.0` with the exact Accepted Common Artifact Envelope at mandatory
`/envelope`, exact Task Contract Artifact Type and governing-definition pins,
separate opaque governing Project Charter and Workstream Artifact
Instance/Revision pins, and a closed eleven-property CONTRACT-003 payload. It
contains no Project Charter, Workstream, peer Task Contract, or downstream
artifact schema `$ref`, permission language, approval mechanism, workflow, or
runtime. Governed integration to `main` activates that exact Schema Version.
Acceptance, schema validity, or repository presence grants no contract
conformance, task authority, integration authority, release, deployment,
merge permission, Context Packet schema authority, or follow-on authority.

The [Context Packet Executable Schema Definition](context-packet-executable-schema.md)
and [ADR-0015](adr/0015-context-packet-executable-schema.md) are **Accepted**
under issue #56 and Owner acceptance comment `5216466742`. They define one
Draft 2020-12 Context Packet Schema Version `1.0.0` with the exact Accepted
Common Artifact Envelope at
mandatory `/envelope`, exact Context Packet Artifact Type and governing
definition pins, one opaque governing Task Contract Artifact Instance/Revision
pin, and a closed thirteen-property CONTRACT-004 payload. The resource contains
no Project Charter, Workstream, Task Contract, peer, Execution Result, or
downstream schema `$ref` and no executable selection, retrieval, ranking,
access, disclosure, transformation, prompt, workflow, or runtime mechanism.
Governed integration to `main` activates that exact Schema Version.
Acceptance, schema validity, or repository presence grants no contract
conformance, task authority, source access, retrieval or disclosure permission,
merge permission, release, deployment, Execution Result schema authority, or
follow-on authority.

The [Execution Result Executable Schema Definition](execution-result-executable-schema.md)
and [ADR-0016](adr/0016-execution-result-executable-schema.md) are **Accepted**
under issue #58 and Owner acceptance comment `5217275706`. They define one
Draft 2020-12 Execution Result Schema Version `1.0.0` that composes the exact
Accepted Common Artifact Envelope with a closed fourteen-property CONTRACT-005
payload, one opaque governing Task Contract pin, and explicit opaque Context
Packet pin declarations. It contains no artifact-specific schema `$ref`.
Output, actions, side effects, resources, provenance, checks, criteria
assessments, assumptions, limitations, failures, deviations, stops,
escalations, security/privacy, and evidence/review/decision/lifecycle
traceability remain evidentiary declarations. Governed integration to `main`
activates that exact Schema Version. Acceptance, schema validity, or repository
presence grants no correctness, completion, conformance, integration authority,
release, deployment, merge permission, Evidence Bundle schema authority, or
follow-on authority.

The [Evidence Bundle Executable Schema Definition](evidence-bundle-executable-schema.md)
and [ADR-0017](adr/0017-evidence-bundle-executable-schema.md) are **Accepted**
under issue #60 and Owner acceptance comment `5217888146`. They define one
Accepted Draft 2020-12 Evidence Bundle Schema Version `1.0.0` that composes the
exact Accepted Common Artifact Envelope with a
closed fifteen-property CONTRACT-006 payload, one opaque governing Task
Contract pin, exact reviewable-subject declarations, explicit opaque artifact
relationships, Evidence Items, claim traceability, and bounded provenance,
quality, limitation, security/privacy, and lifecycle declarations. It contains
no artifact-specific schema `$ref` and implements no collection, retrieval,
scoring, verification, access, disclosure, approval, acceptance, workflow,
release, deployment, or merge mechanism. Creation, validation, review, schema
validity, or repository presence grants no contract conformance, source truth,
relevance, sufficiency, correctness, acceptance, integration, release,
deployment, merge permission, Review Record schema authority, or follow-on
authority. Governed integration to `main` activates the exact Schema Version.

The [Review Record Executable Schema Definition](review-record-executable-schema.md)
and [ADR-0018](adr/0018-review-record-executable-schema.md) are **Proposed**
under issue #62. They define one inactive Draft 2020-12 Review Record Schema
Version `1.0.0` candidate that composes the exact Accepted Common Artifact
Envelope with a closed sixteen-property CONTRACT-007 payload. Review Authority
and Execution Authority remain separate opaque pins; exact reviewable subjects,
nine artifact-relationship categories, findings, evidence use, uncertainty,
dissent, recommendations, peer reviews, correction, security/privacy, and
lifecycle values remain bounded Evidentiary declarations. The candidate
contains no artifact-specific schema `$ref` and implements no reviewer identity
or specialty system, review, retrieval, scoring, severity, confidence, verdict,
approval, voting, synthesis, decision, workflow, runtime, access, disclosure,
retention, release, deployment, or merge mechanism. Creation, validation,
review, schema validity, or repository presence grants no contract conformance,
specialist authority, review quality, recommendation authority, acceptance,
integration, release, deployment, merge permission, Decision Record schema
authority, or follow-on authority. It remains inactive pending separate
exact-head EIGENAAR / Final Authority acceptance and governed integration.

## Document status

- **Proposed** — submitted for review and not yet an accepted repository decision.
- **Accepted** — approved under repository governance and adopted as a binding architecture decision or baseline.
- **Superseded** — replaced by a later accepted decision that identifies the replacement.
- **Deprecated** — retained for reference but discouraged for new use; it is not necessarily replaced.

## Future changes

Future architecture changes MUST start with an approved issue or task contract, identify their intended scope and affected documents, and receive the authority and review required by [governance](../../GOVERNANCE.md). An accepted architecture decision record MUST accompany a consequential architecture change when the core contract requires one. Until then, discussion and proposed documents do not alter accepted architecture.
