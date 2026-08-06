# CNTX Common Artifact Envelope Schema Boundary (ARCH-004)

## Status and authority

Status: **Accepted**.

This document is an accepted, documentation-only architecture boundary integrated under issue #32 and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md). It is binding only within its exact semantic-ownership scope. It refines but does not alter or redefine [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), [ARCH-003](artifact-contract-schema-architecture.md), any accepted artifact contract, or final human authority.

This decision defines semantic ownership boundaries for a future Common Artifact Envelope. It does not define or authorize concrete fields, names, requiredness, types, nesting, cardinality, identifiers, timestamps, digests, schema language or dialect, serialization, packaging, publication, validation, or runtime behavior.

## Purpose

ARCH-003 places a conceptual Common Artifact Envelope between identity/version/provenance semantics and artifact-specific contracts. Before CNTX can consider an executable common schema, the public core needs one reviewable answer to two questions:

1. Which accepted concepts belong to the common envelope boundary, conditionally belong there, remain owned by artifact-specific contracts, or stay explicitly outside envelope semantics?
2. Which part of a source relationship is common reference and provenance mechanics, and which part remains artifact-specific relationship meaning?

This decision answers only those boundary questions. Classification here assigns semantic ownership; it does not decide whether or how a concept is represented in any future schema.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Canonical artifact responsibilities, classifications, lifecycle boundaries, human final authority, minimal context, evidence discipline, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Artifact, contract, and schema identities and versions remain distinct; status is not version; identifiers, digests, and provenance do not grant authority, trust, or approval. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | The Common Artifact Envelope remains Layer 3, subordinate to Layers 1 and 2 and above artifact-specific contracts; lower layers may specialize but not redefine higher layers. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Each canonical artifact keeps its accepted responsibility, classification, relationship semantics, authority limits, and artifact-specific content. |
| Issues #30, #31, and #32 | Schema work remains core-first and documentation-only; Layer 5 and executable or serialization decisions remain deferred; issue #32 is the bounded authority for this decision. |

## Ownership classification

The four categories below are mutually exclusive statements of semantic ownership. “Universal” means that the concept has one common meaning across Artifact Instances; it does not silently establish presence, requiredness, representation, or validation rules.

| Boundary category | Concepts | Ownership rule |
| --- | --- | --- |
| **Universal envelope** | Artifact Type; Artifact Instance Identifier; Artifact Revision; governing Contract Definition Identifier and Contract Definition Version; provenance-reference capability | The future common definition owns the cross-artifact meaning and separation of these concepts. It does not decide their concrete representation or make the referenced source authoritative. |
| **Conditional envelope** | Schema Identifier and Schema Version when an executable schema exists; optional content-digest evidence; declared extensions or profiles when applicable; generic identity and pinning mechanics for an authoritative-source reference when an artifact contract requires that relationship | The future common definition may own the shared meaning only when the stated condition applies. This decision does not decide presence, requiredness, representation, extension mechanics, or Layer 5 behavior. |
| **Artifact-specific** | Relationship role and purpose; relationship direction, multiplicity, sufficiency, freshness, replacement, or conflict semantics; artifact payload and responsibility; task scope; context selection; execution claims; evidence claims; review findings; decision rationale; approval evidence; declared state | The applicable accepted artifact contract owns the meaning and constraints. A future envelope may provide common reference mechanics but cannot generalize or override these semantics. |
| **Explicitly outside common-envelope ownership** | Authority; approval; trust; canonical artifact classification; artifact lifecycle; Document Status; Implementation Version; contract conformance; schema validity | These concepts remain governed by architecture, governance, artifact contracts, document control, or later separately accepted decisions. Envelope metadata, identifiers, versions, references, digests, or validation results cannot create or imply them. |

Transport, storage, provider, domain, private-implementation, execution, orchestration, and product concerns are also outside this decision. Their exclusion does not assign them to a later layer or authorize later work.

## Common references and artifact-specific relationships

A future Common Artifact Envelope may provide shared identity, revision pinning, and provenance-reference semantics. Those mechanics answer only which artifact, contract, schema, revision, or authoritative source is being referenced and, where applicable, which evidence supports content integrity.

The applicable artifact contract continues to answer why the relationship exists, which role the referenced artifact plays, whether it governs or merely informs, what freshness or conflict rules apply, and what authority limits hold. Therefore:

- a reference to an authoritative source does not transfer that source's authority to the referencing artifact;
- an embedded or derived copy does not replace the pinned authoritative source;
- a digest can support integrity evidence but not approval, trust, status, or conformance;
- a schema reference can identify an applicable schema but cannot establish contract conformance or acceptance; and
- provenance can establish lineage without deciding the semantic sufficiency of the relationship.

## Contract-by-contract cross-check

| Accepted contract | Artifact-specific ownership preserved |
| --- | --- |
| [CONTRACT-001 — Project Charter](../contracts/project-charter-contract.md) | Enduring project intent, approved scope and constraints, authority basis, and downstream governance relationships remain Project Charter semantics. |
| [CONTRACT-002 — Workstream](../contracts/workstream-contract.md) | Coordination scope, declared workstream state, and the meaning of relationships to Project Charter and Task Contracts remain Workstream semantics. |
| [CONTRACT-003 — Task Contract](../contracts/task-contract-artifact-contract.md) | Bounded scope, permissions, prohibitions, governing authority, completion evidence, and task relationships remain Task Contract semantics. |
| [CONTRACT-004 — Context Packet](../contracts/context-packet-contract.md) | Context selection, minimum relevance, freshness, lineage, conflicts, and the non-authoritative nature of the packet remain Context Packet semantics. |
| [CONTRACT-005 — Execution Result](../contracts/execution-result-contract.md) | Task-governed result claims, performed work, limitations, and incomplete work remain Execution Result semantics. |
| [CONTRACT-006 — Evidence Bundle](../contracts/evidence-bundle-contract.md) | Claims, evidence quality, integrity, sufficiency, and contradiction handling remain Evidence Bundle semantics. |
| [CONTRACT-007 — Review Record](../contracts/review-record-contract.md) | Review subject, specialist scope, findings, recommendation, dissent, and uncertainty remain Review Record semantics. |
| [CONTRACT-008 — Decision Record](../contracts/decision-record-contract.md) | Decision authority, rationale, effective scope, approval, amendment, and conflict resolution remain Decision Record semantics. |
| [CONTRACT-009 — State Snapshot](../contracts/state-snapshot-contract.md) | Snapshot scope, source interpretation, temporal meaning, freshness, staleness, replacement, and derived status remain State Snapshot semantics. |

This cross-check does not add a concept to any accepted contract and does not change an artifact's Authoritative, Evidentiary, or Derived classification.

## Schema-family boundary

Under this accepted boundary, the Common Artifact Envelope is to remain one independently reviewable common definition in the future Schema Family. Artifact-specific definitions may depend on that common definition while preserving their own accepted contract semantics. They may not replace it with incompatible common metadata, and the common definition may not absorb artifact-specific payload or relationship meaning.

This boundary prevents both a hidden global schema and nine divergent redefinitions of common identity, version, and provenance concepts. It does not decide schema composition, resolution, extension, packaging, publication, or validation mechanisms.

## Preconditions for any later executable-schema decision

No decision about schema language or dialect, executable envelope structure, schema identity or version assignment, packaging, publication, or validation is authorized by this decision. Before any such decision is proposed:

1. this accepted boundary, its exact integrated revision, and its governing ARCH-001 through ARCH-003 baseline must be identified;
2. the later task must define an explicit allowlist and preserve the four ownership categories and nine contract boundaries;
3. schema identity/versioning and language/dialect choices must be presented as separate, reviewable decisions rather than embedded assumptions;
4. security and privacy analysis must confirm that public definitions cannot require secrets, credentials, personal data, production configuration, or private implementation context; and
5. the later task must retain the distinction between schema validity, contract conformance, review, approval, integration, and human authority.

Layer 5 extension/profile mechanisms remain deferred. No later phase is implied, scheduled, or authorized merely because these preconditions are documented.

## Security and privacy boundary

The envelope boundary is public and domain-agnostic. A future definition must be capable of referring to an authoritative source without copying restricted source content. Identifiers, provenance references, and digests must not be treated as permission to expose secrets, credentials, personal data, private paths, production configuration, provider-specific material, or private implementation details.

This decision contains no private project context and establishes no discovery, registry, negotiation, retrieval, transport, storage, access-control, or runtime mechanism. Security or privacy questions that require such mechanics need a separate private assessment and an explicitly authorized public decision boundary.

## Acceptance record and continuing gate

Issue #32 and its corrective Owner / Final Authority direction record the issue-specific acceptance and integration authority for this exact boundary. That direction explicitly records that no independent review occurred and does not change general CNTX governance or role separation.

Accepted status establishes only this conceptual boundary. It does not authorize a later schema phase. Review completion, a passing check, mergeability, or the existence of this document cannot authorize concrete schema or implementation work; every later consequential phase still requires its own attributable authority.

## Deferred and prohibited by this decision

The following remain outside the present decision: concrete fields or examples; field names or aliases; requiredness; types; nesting; cardinality; identifier syntax; timestamps; digest algorithms; schema language or dialect; JSON or YAML schemas; serialization bindings; templates; payloads; fixtures; validators; conformance tooling; registries; discovery or negotiation; extension resolution; profiles; selectors; engines; workflows; APIs; CLIs; runtimes; provider integrations; private implementations; and reference-implementation work.
