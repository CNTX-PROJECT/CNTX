# ADR-0005: Common Artifact Envelope representation boundary

## Status

Accepted.

This ADR records the accepted, documentation-only architecture decision approved under issue #34. Owner / Final Authority acceptance of the exact reviewed candidate head is recorded in issue comment `5207587298`. On merge and publication to `main`, ADR-0005 becomes an accepted repository decision under repository governance.

## Context

Accepted ARCH-004 classifies Common Artifact Envelope concepts as universal, conditional, artifact-specific, or explicitly outside common-envelope ownership. It deliberately does not decide whether or how the owned concepts are represented.

Before selecting schema identity, schema language, executable structure, or serialization, CNTX needs an independently reviewable boundary for what a future common definition must be capable of expressing. Without that boundary, a later schema could make conditional concepts universal, omit required common capabilities, conflate identity with version, absorb artifact-specific payload, encode authority in metadata, or hide unresolved design decisions inside technology choices.

## Decision

CNTX adopts [the Common Artifact Envelope Representation Boundary](../common-artifact-envelope-representation-boundary.md) as ARCH-005 with these constraints:

1. A representation obligation requires the future common definition to preserve an accepted concept without choosing its lexical or executable form.
2. The common definition provides universal capability for Artifact Type, Artifact Instance Identifier, Artifact Revision, governing Contract Definition Identifier and Version, and provenance-reference mechanics.
3. Schema identity/version, digest evidence, extension/profile declarations, and authoritative-source reference mechanics activate only under their accepted conditions.
4. Artifact/revision, contract-identifier/version, schema-identifier/version, provenance target/pin, and digest subject/method context remain semantically coupled but conceptually distinct.
5. Not-applicable, not-asserted, unresolved, and known information must not be collapsed when the distinction affects provenance or conformance; their encoding remains deferred.
6. The common envelope and artifact-specific payload remain independently reviewable definitions. Shared mechanics cannot absorb artifact-specific relationship meaning or content responsibility.
7. Authority, approval, trust, classification, lifecycle, Document Status, Implementation Version, contract conformance, schema validity, and integration authority remain outside common-envelope ownership.
8. Schema identity/versioning, schema language/dialect, executable definitions, bindings, and validation remain separate later decisions in an explicit dependency order.

This decision does not select field names, types, nesting, requiredness, cardinality, identifiers, syntax, schema language or dialect, serialization, packaging, validation, or runtime technology.

## Consequences

- A future executable common definition will have a stable checklist of semantic capabilities and activation conditions.
- Conditional metadata cannot silently become universally required merely because it has a common representation.
- Identity, revision, version, provenance, and digest concepts can be reviewed together without being conflated.
- Artifact-specific schemas retain their payload and relationship semantics while reusing governed common mechanics.
- Schema-language selection cannot smuggle in unresolved authority, privacy, composition, or presence decisions.
- Later executable and validation work still requires separate authority, evidence, and review.

## Rejected alternatives

### Jump directly to an executable schema

Rejected because a language or dialect would turn unresolved representation obligations into implicit technology-driven decisions.

### Choose concrete field names and types in this decision

Rejected because lexical structure, types, nesting, cardinality, and validation belong to later schema decisions and require their own evidence.

### Require every common capability in every Artifact Instance

Rejected because definition capability and instance activation are distinct. Conditional concepts remain conditional, and artifact-specific contracts retain their requirements.

### Put artifact payload and relationship meaning in the common envelope

Rejected because that would erase bounded artifact responsibilities and create a monolithic global structure.

### Encode authority, approval, status, or conformance in envelope metadata

Rejected because accepted architecture keeps these meanings outside common-envelope ownership; metadata and successful validation cannot grant them.

### Treat the combined Architect/Implementer review as final approval

Rejected because issue #34 permits transparent operational role combination but preserves sole human final authority and the exact-head decision gate.

## Follow-up decisions

The next candidate decision should address schema identity and initial version policy for the Common Artifact Envelope as a separate, documentation-only task. Later decisions may address schema language and dialect, composition and packaging, an executable common definition, artifact-specific schemas, Serialization Bindings, and validation evidence.

No follow-up task, identifier, version, schema technology, implementation, merge, release, or deployment is authorized by this ADR.
