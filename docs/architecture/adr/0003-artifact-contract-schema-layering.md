# ADR-0003: Artifact Contract and Schema Layering

## Status

**Proposed.** This decision requires final human approval under [GOVERNANCE.md](../../../GOVERNANCE.md) before it can become accepted.

## Context

The accepted [core architecture contract](../core-contract.md) establishes CNTX public-core boundaries, and the accepted [contract identity and versioning contract](../contract-identity-versioning.md) establishes the identity, revision, versioning, compatibility, and provenance baseline. Before defining individual artifact contracts or executable schemas, CNTX needs an unambiguous conceptual architecture for common envelope semantics, artifact-specific contracts, extensions, profiles, bindings, validation, conformance, and implementations. This remains documentation-only work and must preserve bounded context, traceability, public/private boundaries, and final human authority.

## Decision

CNTX separates normative contracts, Common Artifact Envelope semantics, artifact-specific contracts, executable schemas, Serialization Bindings, Extension Modules and Profiles, validators, Conformance Claims, and implementations. Lower layers MUST conform to higher accepted layers and MUST NOT redefine their semantics. The layer order is:

1. accepted governance and core architecture;
2. accepted identity/versioning and provenance semantics;
3. common artifact-envelope semantics;
4. artifact-specific normative contracts;
5. optional extension modules and profiles;
6. executable schemas;
7. serialization bindings;
8. validators and conformance tooling;
9. runtime or product implementations.

CNTX defines a Common Artifact Envelope conceptually without selecting fields or syntax. Every canonical artifact MUST have one bounded artifact-specific normative contract before an executable schema is introduced. The canonical nine-artifact dependency direction remains Project Charter to Workstream and Task Contract; Workstream to Task Contract; Task Contract to Context Packet and Execution Result; Context Packet to Execution Result; Execution Result to Evidence Bundle and Review Record; Evidence Bundle to Review Record and Decision Record; Review Record to Decision Record; Project Charter to Decision Record; and Decision Record to State Snapshot. Derived and evidentiary artifacts MUST NOT replace authoritative sources.

Extensions and Profiles are explicit, namespaced, non-overriding layers. CNTX distinguishes contract, schema, instance, binding, and implementation conformance. Schema validity does not establish approval or full contract conformance. Exact schema language, fields, serialization, validation, migration, and runtime technology remain deferred. CNTX remains provider-, model-, runtime-, transport-, storage-, serialization-, schema-language-, and domain-independent.

## Consequences

Future schema proposals must begin with a reviewable, bounded normative artifact contract and show upward conformance to accepted semantics. Schema and binding work cannot become the source of authority or alter accepted meaning. Validators and evidence can support a Conformance Claim but cannot approve, authorize, or merge work. The organization preserves independently reviewable artifact boundaries and prevents accumulation of unrelated context in a global artifact structure.

## Rejected alternatives

- One monolithic global schema for every artifact and context, because it erases bounded artifact and context-isolation boundaries.
- Starting with executable schemas before normative artifact contracts, because machine-checkable structure cannot define accepted semantic authority.
- Treating generated code or implementation models as the authority source, because mutable implementations cannot replace accepted contracts or schemas.
- Embedding complete authoritative source content into every downstream artifact, because it risks stale, private, and unbounded copied context.
- Allowing extensions to override core semantics implicitly, because this would weaken stable authority, provenance, privacy, lifecycle, and mandatory requirements.
- Equating schema validity with approval or full contract conformance, because validation alone is evidentiary and does not assess all semantic, governance, or approval conditions.

## Follow-up decisions

Future accepted decisions may address concrete fields and requiredness, schema language, serialization formats and syntax, envelope names, relationship cardinalities and embedding, validators and error reporting, unknown-field and extension behavior, namespace and registry governance, profile negotiation, packaging and distribution, migration and compatibility rules, conformance fixtures, code generation, and runtime APIs, storage, transport, or orchestration. They MUST NOT preselect technologies or providers without an approved decision.
