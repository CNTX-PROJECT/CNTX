# ADR-0011: Canonical Contract Definition identity, initial version, and source binding

## Status

Accepted.

This ADR records the accepted, documentation-only decision governed by
[issue #46](https://github.com/CNTX-PROJECT/CNTX/issues/46). Owner / Final
Authority creation authority is recorded in issue comment `5209713761`. The
Owner / Final Authority separately accepted exact reviewed candidate head
`74594b39d81c79991d0a8ac5ddb15dc517905a8b` in issue comment `5209812463`.
On governed integration to `main`, the exact nine allocations become Accepted
and active.

## Context

Accepted ARCH-002 distinguishes Contract Definition Identifier and Contract
Definition Version from artifact, schema, status, implementation, digest, and
provenance dimensions. Accepted ARCH-009 represents the pair in the Common
Artifact Envelope. Accepted ARCH-010 requires an artifact-specific schema to
identify its applicable Contract Definition and exact version, prohibits the
schema task from inventing those coordinates, and makes unresolved allocation a
stop condition before Project Charter executable-schema work.

All nine canonical artifact contract definitions already exist and are
Accepted, but no concrete Contract Definition Identifiers or exact Contract
Definition Versions have been allocated. Without an exact binding, a later
schema could conflate Artifact Type, contract number, file path, repository
location, or Schema Identifier with normative Contract Definition identity.

## Decision

CNTX adopts the accepted
[Canonical Contract Definition Identity, Initial Version, and Source Binding](../contract-definition-identity-version-binding.md)
as ARCH-011 with these constraints:

1. Allocate the logical namespace **CNTX Public Core Contract Definition
   Family**.
2. Allocate exactly nine stable, version-independent HTTPS Contract Definition
   Identifiers, one for each CONTRACT-001 through CONTRACT-009, using the exact
   values in the ARCH-011 allocation table.
3. Allocate initial Contract Definition Version `1.0.0` independently to every
   definition. No family-wide lockstep version exists.
4. Bind each proposed pair to its exact canonical Accepted contract source at
   public baseline commit
   `27b022d8d83df2d60f45762579d8c5a1c8257f37`, tree
   `d9d188f279b8ff5391a15ece2e4a8147b7bc8386`.
5. Treat repository identity, commit, and path as provenance coordinates, not
   substitutes for stable Contract Definition identity or semantic version.
6. Activate the exact nine allocations only after exact-head human acceptance,
   status-only promotion, and governed integration.
7. After activation, keep each version's normative meaning immutable and apply
   ARCH-002 MAJOR, MINOR, and PATCH rules to later Accepted changes.
8. Keep identity/version, Schema identity/version, Artifact Type, Artifact
   Instance identity/revision, status, implementation, digest, provenance,
   release, and deployment distinct.
9. Treat the HTTPS values as identifiers rather than network-fetch
   instructions, resolver coordinates, authority assertions, or access grants.
10. Change none of the nine Accepted artifact contract source documents and
    create no executable schema, binding, validator, registry service, runtime,
    release, or deployment.

## Rationale

Family-wide allocation resolves the same prerequisite consistently for all
nine contracts while preserving independent responsibilities and versions.
Version-independent identifiers allow the same logical definition to evolve
through compatible and breaking semantic versions. Exact baseline source
binding prevents an unspecified mutable notion of current content from being
called `1.0.0`.

The existing publicly attributable repository namespace provides exact lexical
coordinates without introducing a private namespace or operational service.
Keeping version outside the identifier preserves ARCH-002 dimension separation
and matches the coupled `governingContract` representation already Accepted in
the Common Artifact Envelope.

## Consequences

- A future Project Charter executable schema can use an exact, governed
  Contract Definition identifier/version constant rather than inventing one.
- The remaining artifact-specific schemas can reuse the same family rules in
  dependency order.
- Each contract can evolve independently while higher-to-lower dependency
  impact remains reviewable.
- Exact prior meaning remains traceable through identifier, version, repository
  provenance, baseline commit, and source path.
- Candidate commits remain provenance events and do not consume semantic
  versions.
- Identifier syntax, version, repository hosting, and successful retrieval do
  not grant conformance, authority, trust, acceptance, release, or deployment.
- No operational resolver, registry, hosted publication service, validator, or
  implementation is supplied.

## Rejected alternatives

- **Contract number, Artifact Type, or source path as identifier** — rejected
  because each is a classification, label, or mutable coordinate rather than a
  stable explicitly namespaced Contract Definition identity.
- **Branch, tag, release, `latest`, or version-bearing identifier** — rejected
  because moving coordinates and semantic version are distinct from stable
  logical identity.
- **One family identity or lockstep family version** — rejected because the
  nine normative responsibilities and version lines remain independent.
- **A new identity for every MAJOR** — rejected because breaking evolution of
  the same responsibility changes version, not identity.
- **Initial `0.x` because CNTX is pre-alpha** — rejected because repository
  maturity and release state do not define Contract Definition Version.
- **PATCH for every candidate or review correction** — rejected because
  pre-acceptance changes are provenance events.
- **`1.0.0` without exact source binding** — rejected because an unpinned
  mutable source cannot establish the exact versioned normative meaning.
- **Mandatory digest or automatic network resolution** — rejected because
  digest, canonicalization, resolver, network, and publication mechanics remain
  separately governed.
- **Combined Architect/Implementer review as final approval** — rejected
  because the authorized review is transparently non-independent and human
  final authority remains controlling.

## Security and privacy

The allocated values and sources are intentionally public. They contain no
secrets, credentials, personal data, private project data, production
configuration, private paths, restricted sources, or private implementation
detail. Future provenance and mappings must preserve that boundary. Identifier
format, namespace appearance, discoverability, and retrieval success provide no
trust, authorization, endorsement, safety, or permission to access data.

## Validation and authority boundary

The exact candidate proved the five-path allowlist, unchanged contract and
schema sources, exact nine unique identifier/version/source mappings, valid
local links, Proposed candidate status, clean diff, baseline parentage, and
local, remote, and Draft PR head equality. Those results were evidence only.

The same operational agent prepared and reviewed the candidate under issue
#46. The review was non-independent and did not grant acceptance. The Owner /
Final Authority separately accepted the exact reviewed head in issue comment
`5209812463`. Promotion, integration, issue closure, and branch cleanup remain
separately bounded actions.

## Deferred scope

Deferred and unauthorized work includes contract-source changes; executable
artifact-specific schemas and payloads; concrete artifact-specific `$id`
values and active Schema Versions; Common Artifact Envelope changes; Artifact
Instance identifier or revision mechanics; digests, encoding, canonicalization,
signatures, verification, and trust; Serialization Bindings; extensions and
profiles; validators and validation output; resolvers, registries, catalogs,
caches, bundles, network retrieval, and hosted publication; conformance tools,
code generation, migration, APIs, CLIs, workflows, runtimes, providers,
products, private or reference implementations, releases, tags, and deployment.

## Continuing gate

This ADR is Accepted and authorizes no follow-on phase. On governed integration,
the nine exact allocations become Accepted and active. Only then may Project
Charter executable-schema work become a separately authorized candidate using
the exact allocated Project Charter Contract Definition Identifier and Version.
