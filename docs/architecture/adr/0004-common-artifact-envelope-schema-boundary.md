# ADR-0004: Common Artifact Envelope schema boundary

## Status

Accepted.

This ADR records the accepted documentation-only boundary decision authorized under issue #32. Acceptance does not authorize a follow-on task, concrete schema design, Layer 5 mechanisms, validation, runtime work, provider integration, or private implementation work.

## Context

ARCH-003 defines a conceptual Common Artifact Envelope at Layer 3, between accepted identity/version/provenance semantics and the nine accepted artifact-specific contracts. It deliberately defers concrete fields, requiredness, encoding, serialization, schemas, and validators.

Before an executable common definition can be considered, CNTX needs an independently reviewable boundary for shared semantic ownership. Without that boundary, a future schema could improperly absorb authority or artifact-specific meaning, or each artifact-specific schema could redefine common identity and provenance concepts differently.

## Decision

CNTX adopts [the Common Artifact Envelope Schema Boundary](../common-artifact-envelope-schema-boundary.md) as ARCH-004 with these constraints:

1. Accepted envelope-related concepts are classified as universal envelope, conditional envelope, artifact-specific, or explicitly outside common-envelope ownership.
2. The common boundary owns shared identity, version, pinning, and provenance semantics only; classification does not decide concrete representation, presence, or requiredness.
3. Common reference mechanics remain separate from relationship role, authority, direction, sufficiency, freshness, conflict, and other semantics owned by the applicable artifact contract.
4. Authority, approval, trust, canonical artifact classification, lifecycle, Document Status, Implementation Version, contract conformance, and schema validity remain outside common-envelope ownership.
5. The future Common Artifact Envelope remains one independently reviewable common definition in the Schema Family; it is neither a hidden global schema nor a container for artifact-specific payload meaning.
6. The nine accepted artifact contracts retain their existing responsibilities, classifications, relationships, authority limits, and content semantics.

This decision does not select a schema language or dialect and does not define an executable schema, concrete structure, serialization, validator, registry, packaging model, publication model, or runtime behavior.

## Consequences

- Future schema proposals will have a stable conceptual boundary against which shared and artifact-specific ownership can be reviewed.
- Common identity, version, provenance, and pinning semantics can be defined once without erasing the distinctions established by accepted artifact contracts.
- A source reference can use common mechanics while its governing meaning remains with the artifact contract.
- Envelope metadata and validation cannot be used as substitutes for authority, approval, trust, lifecycle state, artifact classification, contract conformance, or human decision.
- Later schema identity/versioning, language/dialect, executable definition, packaging, publication, and validation decisions will still require separately authorized work.
- Layer 5 extension/profile mechanisms remain deferred.

## Rejected alternatives

### Define concrete envelope fields now

Rejected because issue #32 bounded this decision to semantic ownership only. Concrete representation would collapse a later decision into an unreviewed assumption.

### Put all cross-artifact relationships in the common envelope

Rejected because the common layer may own identity and pinning mechanics, but relationship meaning and constraints differ across the nine accepted artifact contracts.

### Encode authority, approval, status, classification, or conformance as envelope ownership

Rejected because accepted architecture keeps these concepts distinct. Metadata, references, digests, versions, and schema-valid results cannot grant authority or approval.

### Let each artifact-specific schema redefine common metadata

Rejected because incompatible definitions would undermine the accepted identity/version/provenance layer and the purpose of a common envelope.

### Treat this decision as approval for executable schema work

Rejected because proposal, review, acceptance, integration, and later implementation are separate governance phases.

## Follow-up decisions

No follow-up task is authorized by this ADR. Later bounded proposals may consider schema identity and version assignment, schema language or dialect, executable common and artifact-specific definitions, packaging, publication, or validation. Each requires its own authority, scope, security/privacy assessment, evidence, and review.
