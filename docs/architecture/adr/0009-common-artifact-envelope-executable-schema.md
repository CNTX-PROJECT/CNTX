# ADR-0009: Common Artifact Envelope executable schema definition

## Status

Accepted.

This ADR records the accepted first executable Common Artifact Envelope Schema Resource approved under issue #42. Owner / Final Authority acceptance of the exact reviewed candidate is recorded in issue comment `5208715683`. On governed integration to `main`, Schema Version `1.0.0` becomes active under repository governance.

## Context

Accepted ARCH-004 defines the common-envelope ownership boundary. ARCH-005 defines representation capability, semantic coupling, conditional activation, absence, and payload separation. ARCH-006 allocates one logical Common Artifact Envelope schema identity and reserves `1.0.0` as the first accepted target. ARCH-007 selects JSON Schema Draft 2020-12. ARCH-008 selects one standalone root resource, a version-qualified HTTPS identity, internal `$defs`, static fragment references, no dynamic/public-anchor surface, and offline-first processing.

No executable Common Artifact Envelope exists at the baseline. Without one, artifact-specific executable schemas cannot reuse a single machine-evaluable common identity and provenance boundary. The new resource must remain smaller than a full artifact definition and must not turn schema validity into normative authority.

## Decision

Adopt the following Accepted executable definition:

1. Create one standalone JSON Schema Draft 2020-12 resource at `schemas/common-artifact-envelope/1.0.0/schema.json`.
2. Bind the ARCH-006 logical identity to `$id` `https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`.
3. Use `1.0.0` as the Accepted initial Schema Version; it becomes active on governed integration.
4. Evaluate exactly one Common Artifact Envelope object, not a complete artifact or payload.
5. Define exactly six root properties: `artifactType`, `artifactInstance`, `governingContract`, `governingSchema`, optional `provenanceReferences`, and optional `contentDigests`.
6. Require Artifact Type, the coupled artifact identifier/revision pin, the coupled Contract Definition identifier/version pin, and the coupled Schema identifier/version pin.
7. Enumerate exactly the nine Accepted canonical Artifact Types using lower-kebab-case tokens.
8. Represent identifiers and Artifact Revision as non-blank opaque strings.
9. Require exact three-component, no-leading-zero `MAJOR.MINOR.PATCH` syntax for Contract Definition Version and Schema Version.
10. Support artifact, contract-definition, and schema-definition provenance targets without relationship or authority semantics.
11. Support optional subject-bound digest evidence without selecting an algorithm, encoding, canonicalization, signature, or verifier.
12. Close every object with `additionalProperties: false`; reject empty evidence arrays and incomplete or `null` placeholders.
13. Keep all reusable subschemas inside root `$defs`, with static fragment-only `$ref` values and no nested `$id` or `$schema`.
14. Use no `$anchor`, `$dynamicAnchor`, `$dynamicRef`, external reference, custom keyword, custom vocabulary, `format`, default, extension field, or profile field.
15. Commit one synthetic, non-normative positive/negative test-case manifest as review evidence, not as a validator, binding, conformance claim, or accepted Artifact Instance.
16. Preserve the distinction between schema validity, normative-contract conformance, review, acceptance, authority, release, deployment, and access permission.

## Rationale

The selected root is the smallest executable structure that implements every universal representation obligation and the activated schema pin while keeping artifact payload and relationship meaning independently governed. Closed semantic-pair objects prevent incomplete pins. A closed Artifact Type enum keeps the accepted canonical kinds lexically consistent. Generic provenance and digest evidence supports shared pinning without defining why a source matters.

Opaque strings preserve domain independence and avoid pre-empting future identifier-generation contracts. A strict `MAJOR.MINOR.PATCH` pattern implements the accepted version model without relying on `format`, coercion, or validator options. The version-qualified HTTPS `$id` provides one stable canonical resource identity while remaining distinct from retrieval and network permission.

## Consequences

Positive consequences:

- the Common Artifact Envelope becomes machine-evaluable;
- required identity and governing-definition pairs fail when incomplete;
- all nine canonical Artifact Types share one closed lexical surface;
- later artifact-specific resources can statically depend on one exact common identity;
- no external resource or automatic network access is required;
- unknown properties cannot silently expand common meaning; and
- repeatable positive and negative evidence accompanies the accepted resource.

Costs and limitations:

- this resource cannot validate any artifact-specific payload;
- it cannot determine whether an identifier, revision, version, provenance claim, or digest is true or authorized;
- closed objects require explicit versioned evolution;
- no complete artifact representation exists until artifact-specific schema work is separately accepted;
- no Extension Module or Profile can be declared through the common envelope yet; and
- no validator, resolver, serialization, runtime, release, or deployment is supplied.

## Rejected alternatives

- **One full-artifact root** — rejected because it would choose container layout and absorb artifact-specific payload.
- **Flat pins** — rejected because incomplete identifier/revision or identifier/version pairs would be easier to create.
- **URI-only identifiers** — rejected because common identifiers remain opaque and domain-independent.
- **Required provenance for every instance** — rejected because capability is universal but activation remains contract-specific.
- **Relationship roles in common references** — rejected because those semantics remain artifact-specific.
- **A selected digest algorithm** — rejected because digest mechanics and verification remain separately governed.
- **Authority, approval, lifecycle, status, or implementation fields** — rejected as outside common-envelope ownership.
- **Reserved extension/profile fields** — rejected before Layer 5 representation and mechanics decisions.
- **Open objects** — rejected because unknown fields could create unreviewed common semantics.
- **Public anchors or dynamic references** — rejected by the initial ARCH-008 composition surface.
- **Moving or unversioned identity** — rejected because accepted versions must be consequentially pinnable.
- **Validation as acceptance** — rejected because only the human Owner / Final Authority may accept the exact candidate.

## Security and privacy

The resource and synthetic test data require no secrets, credentials, personal data, private paths, production configuration, private project context, restricted source content, provider-specific requirement, or private implementation detail. References and identifiers grant no retrieval or disclosure permission. The schema cannot detect every policy-sensitive string; applicable contracts, policy, and human review remain controlling.

Automatic network retrieval, resolver security, resource limits, validator hardening, catalogs, caches, trust stores, integrity verification, and diagnostic handling are outside this decision.

## Validation and authority boundary

The accepted resource must be strictly parsed with duplicate-key rejection, checked against the official Draft 2020-12 meta-schema, and evaluated against every committed expected-valid and expected-invalid case using an isolated standards-conformant validator. Those results are evidence only.

The same operational agent prepared and reviewed the exact candidate under the transparent issue #42 arrangement. The review was non-independent and did not provide final approval; the Owner / Final Authority accepted the exact reviewed head separately in issue comment `5208715683`. `$id`, `1.0.0`, meta-schema validity, instance-test success, mergeability, or publication-shaped coordinates do not independently grant acceptance or integration authority.

## Deferred scope

Deferred and unauthorized work includes artifact-specific schemas and payloads; full artifact container and envelope placement; Contract Definition identity/version allocation; Artifact Instance Identifier generation; revision sequencing; digest algorithms and verification; Extension Module/Profile mechanics; Serialization Bindings; canonicalization; transport; storage; bundles; registries; resolvers; validators; conformance tooling; code generation; migrations; APIs; CLIs; workflows; runtimes; providers; products; private implementations; reference implementations; releases; tags; hosted publication; and deployment.

## Continuing gate

The exact-head candidate was accepted by the Owner / Final Authority in issue comment `5208715683`, authorizing only the recorded status promotion and integration sequence. No follow-on Schema Family phase is implied or authorized.
