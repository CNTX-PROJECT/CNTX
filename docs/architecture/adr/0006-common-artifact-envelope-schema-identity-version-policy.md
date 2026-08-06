# ADR-0006: Common Artifact Envelope schema identity and initial version policy

## Status

Accepted.

This ADR records the accepted, documentation-only architecture decision approved under issue #36. Owner / Final Authority acceptance of the exact reviewed candidate head is recorded in issue comment `5207779116`. On merge and publication to `main`, ADR-0006 becomes an accepted repository decision under repository governance.

## Context

Accepted ARCH-002 requires every future executable schema definition to have a stable, explicitly namespaced Schema Identifier and a distinct semantic Schema Version. Accepted ARCH-004 and ARCH-005 require one independently reviewable Common Artifact Envelope definition and place identity and initial version policy before schema language, dialect, executable structure, packaging, publication, and validation.

Without a separate identity decision, a later technology choice could silently treat a file path, URL, schema-language keyword, title, or registry location as the architecture identity. Without an initial version policy, candidate commits, repository pre-alpha status, schema acceptance, project releases, and semantic schema versions could be conflated.

No executable Common Artifact Envelope schema currently exists. The decision therefore must allocate stable logical identity and version-entry rules without pretending that executable content or an active Schema Version already exists.

## Decision

CNTX adopts [the Common Artifact Envelope Schema Identity and Initial Version Policy](../common-artifact-envelope-schema-identity-version-policy.md) as ARCH-006 with these constraints:

1. The future Common Artifact Envelope executable definition receives exactly one technology-neutral logical identity allocation: logical namespace **CNTX Public Core Schema Family** and logical local identity **Common Artifact Envelope**.
2. The allocation identifies the one future common definition governed by accepted Layer 3 boundaries. It is not a concrete lexical Schema Identifier, URI, URN, URL, path, filename, schema keyword value, registry key, or resolver address.
3. No executable Common Artifact Envelope schema and no active Schema Version are created by this decision.
4. Schema Version `1.0.0` is reserved as the initial accepted version target for the first later executable definition accepted under its own exact-revision human decision. Candidate drafting and review corrections do not consume semantic versions.
5. Repository `pre-alpha` or release status is separate from schema versioning and does not require an accepted `0.x` schema line.
6. After first schema acceptance, accepted versions are immutable and progress under the ARCH-002 `MAJOR.MINOR.PATCH` rules with a compatibility assessment, traceable provenance, applicable Decision Record, and human approval.
7. The logical schema identity remains stable across versions, including MAJOR versions. A new identity requires a separate accepted decision establishing a genuinely distinct schema responsibility; it cannot be used to evade compatibility or provenance obligations.
8. Schema identity and version remain distinct from contract identity/version, artifact identity/revision, Document Status, Implementation Version, Content Digest, provenance, location, release state, conformance, approval, and authority.
9. A later schema-language, dialect, composition, packaging, and publication decision must preserve the logical identity but will separately decide its concrete encoding and whether multiple dialect representations are one or multiple executable definitions.

This decision does not select schema language, dialect, executable structure, concrete fields, serialization, validation, registry, resolver, publication mechanism, or implementation technology.

## Consequences

- Future language and publication choices receive a stable logical identity requirement instead of defining identity incidentally.
- The first accepted executable definition has an unambiguous `1.0.0` entry target without creating a nonexistent schema or claiming premature acceptance.
- Candidate document and schema revisions remain traceable through repository provenance without artificial PATCH consumption.
- Breaking evolution can remain under the same stable logical identity with a new MAJOR version.
- Artifact-specific schemas, extensions, profiles, bindings, validators, and implementations cannot reuse the Common Artifact Envelope identity.
- Identifier, version, status, conformance, authority, release, and deployment claims remain separate.

## Rejected alternatives

### Use a file path, URL, or schema-language identity keyword now

Rejected because language, dialect, packaging, publication, and resolver behavior are later decisions. Selecting their lexical form here would embed an unauthorized technology and distribution choice.

### Assign `1.0.0` as an active Schema Version now

Rejected because there is no executable definition to version. ARCH-006 reserves an initial accepted target; it does not create executable content or schema acceptance.

### Begin with an accepted `0.x` schema because CNTX is pre-alpha

Rejected because repository maturity and future release versions are distinct from the semantic version of an accepted executable schema definition. First accepted schema meaning begins at `1.0.0` under this policy.

### Increment PATCH for each candidate or review correction

Rejected because pre-acceptance candidate revisions are provenance events, not accepted semantic-schema changes. PATCH applies only after an accepted version exists and only to non-semantic corrections.

### Allocate a new identity for each MAJOR version, dialect, or file location

Rejected because stable logical identity spans compatible and breaking versions of the same schema responsibility. Dialect equivalence still needs a separate decision, and locations are mutable coordinates rather than identity.

### Treat identity allocation as an executable schema or approval

Rejected because a logical identity and version target provide neither schema content nor conformance, trust, authority, acceptance, integration, release, or deployment.

### Treat the combined Architect/Implementer review as final approval

Rejected because issue #36 permits transparent operational role combination but preserves sole human final authority and the exact-head decision gate.

## Follow-up decisions

The next candidate decision should address schema language and dialect as a separate documentation-only task that preserves ARCH-006 if accepted. Composition and packaging must remain separately reviewable before an executable Common Artifact Envelope definition is proposed.

No follow-up task, concrete identifier encoding, schema language, dialect, executable definition, packaging, publication, validator, Layer 5 mechanism, implementation, merge, release, or deployment is authorized by this ADR.
