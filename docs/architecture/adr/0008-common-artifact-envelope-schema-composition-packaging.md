# ADR-0008: Common Artifact Envelope schema composition and packaging

## Status

Proposed.

This ADR records the proposed, documentation-only architecture decision prepared under issue #40. It does not become an accepted repository decision unless the human Owner / Final Authority accepts the exact reviewed candidate revision and the result is integrated under repository governance.

## Context

Accepted ARCH-005 requires source layout, composition, resolution, packaging, and publication boundaries before an executable Common Artifact Envelope definition. Accepted ARCH-006 allocates one technology-neutral logical identity and a conditional `1.0.0` target. Accepted ARCH-007 selects JSON Schema Draft 2020-12, its default vocabulary profile, `$schema`, and `$id` as the future resource-identity mechanism while deferring the resource topology and concrete identity binding.

JSON Schema permits standalone resources, embedded resources, internal `$defs`, static and dynamic references, and Compound Schema Documents. CNTX needs a narrower initial model that preserves independent review, exact version pins, layer direction, offline determinism, and the difference between canonical resources and distribution copies.

## Decision

CNTX proposes [the Common Artifact Envelope Schema Composition and Packaging](../common-artifact-envelope-schema-composition-packaging.md) as ARCH-008 with these constraints:

1. Each accepted Common Artifact Envelope Schema Version has exactly one canonical root Schema Resource and one standalone canonical document.
2. The future root declares the ARCH-007 dialect and receives one version-qualified canonical `$id`; ARCH-008 assigns no concrete value and activates no Schema Version.
3. The future `$id` is a normalized absolute HTTPS URI without a fragment, controlled through an Owner-governed public namespace, and includes the exact `MAJOR.MINOR.PATCH` version without `latest` behavior.
4. The canonical root contains no nested `$id` and therefore no embedded Schema Resources.
5. Internal reusable subschemas live only under root `$defs`, inherit the root dialect and identity scope, and receive no independent identity, version, status, or governance lifecycle.
6. Internal composition uses static fragment-only `$ref`; cross-resource JSON Pointers based on enclosing document layout are prohibited.
7. No public `$anchor` surface and no `$dynamicRef` or `$dynamicAnchor` mechanism are selected for the initial Common Artifact Envelope.
8. The common root has no mandatory external Schema Resource dependency.
9. Future artifact-specific resources may depend through static `$ref` on the exact versioned common root, must preserve their own contracts and identities, and must not copy or redefine common semantics.
10. Schema-resource dependencies follow accepted layer direction and remain acyclic.
11. Canonical authoring and publication use separately reviewable standalone resources with `application/schema+json`.
12. A Compound Schema Document may later be generated only as a derived offline/transport bundle from already accepted resources.
13. A bundle embeds referenced resources under root `$defs` using unique non-normative keys, preserves every `$id`, explicitly preserves every `$schema`, leaves `$ref` values unchanged, and preserves evaluation and canonical-reference behavior.
14. A bundle does not create a new logical identity, Schema Version, Document Status, authority, acceptance, or conformance result.
15. Processors preload or are supplied the exact resource set by canonical URI; automatic network retrieval is disabled by default and an unresolved required reference fails closed as unresolved.
16. Accepted versioned resources are immutable. Retrieval coordinates and mirrors remain separate from canonical identity, and unversioned aliases are human-discovery aids only.
17. Identity, resolution, bundling, publication, schema validity, and validation grant no contract conformance, approval, authority, trust, acceptance, release, deployment, or access permission.

## Consequences

Positive consequences:

- the common definition remains one reviewable Layer 3 resource;
- internal reuse does not create hidden module identities;
- exact version-pinned dependencies make provenance and compatibility visible;
- artifact-specific definitions remain independent while reusing common meaning;
- immutable canonical standalone sources remain separate from generated, non-byte-identical distribution layout;
- bundles can support offline use without rewriting identities or references; and
- network, substitution, and moving-alias risks are excluded by default.

Tradeoffs:

- the initial model exposes no dynamic extension or public subschema API;
- later consumers must explicitly provision exact resources;
- derived bundles require traceable, identity-aware generation and equivalence evidence; and
- concrete URI, file, manifest, resolver, validator, and executable choices remain later work.

## Rejected alternatives

### One monolithic common-plus-artifact schema

Rejected because it would erase artifact-specific ownership and independent versioning.

### Multiple embedded resources in the canonical common source

Rejected because nested `$id` values would multiply resource identities before independent governance needs are established.

### Publicly reference internal `$defs` layout

Rejected because internal organization must not silently become a compatibility API.

### Dynamic references as the initial extension mechanism

Rejected because no recursive dynamic-extension need is established and Layer 5 remains separately governed.

### Copy the common envelope into artifact-specific schemas

Rejected because copies drift and can redefine common meaning.

### Make the Compound Schema Document canonical

Rejected because transport layout must not control identity, ownership, or review.

### Rewrite references or fully dereference during bundling

Rejected because those transformations can change behavior, annotations, canonical locations, and provenance.

### Automatically fetch HTTPS references

Rejected because an identifier is not network or access authorization.

### Use an unversioned or latest identity

Rejected because consequential dependencies require an exact immutable Schema Version pin.

### Assign a concrete `$id` or executable file now

Rejected because this phase is documentation-only and no executable resource exists to bind or review.

### Treat the combined Architect/Implementer review as final approval

Rejected because the transparent combined role is not independent and cannot replace the human Owner / Final Authority.

## Follow-up decisions

Only after ARCH-008 is accepted and integrated may the executable Common Artifact Envelope definition become a separately authorized candidate task. That later work must bind a concrete versioned `$id`, create and review the exact executable content, define its repository/publication coordinates, and prove conformance to ARCH-004 through ARCH-008 without treating schema validity as approval.

No follow-up task, executable schema, concrete field, concrete `$id`, active Schema Version, concrete `$defs` or `$ref`, artifact Serialization Binding, dynamic-reference mechanism, resolver, validator, bundler, implementation, merge, release, or deployment is authorized by this ADR.
