# CNTX Context Packet Executable Schema Definition (ARCH-015)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted executable-schema architecture decision governed
by [issue #56](https://github.com/CNTX-PROJECT/CNTX/issues/56) and recorded by
[ADR-0015](adr/0015-context-packet-executable-schema.md). Owner / Final
Authority acceptance of the exact reviewed candidate is recorded in issue
comment `5216466742`.

The exact reviewed [Schema Resource](../../schemas/context-packet/1.0.0/schema.json)
and [synthetic test evidence](../../tests/schemas/context-packet/1.0.0/cases.json)
are Accepted in the revision recorded by Owner / Final Authority acceptance
comment `5216466742`. On governed integration to `main`, Context Packet Schema
Version `1.0.0` becomes active within this exact scope. The transparent
non-independent review was evidentiary only and did not grant acceptance.

This decision remains subordinate to Accepted architecture, Accepted
[CONTRACT-004](../contracts/context-packet-contract.md), repository
governance, and final human authority. It modifies no Accepted source and
creates no Context Packet Artifact Instance, task authority, source-access or
disclosure permission, retrieval behavior, validator, runtime, release, or
deployment.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Context Packet
Artifact** identity, an inactive `1.0.0` target, a closed
`envelope`/`payload` root, and the exact Common Artifact Envelope
dependency. Accepted
[ARCH-011](contract-definition-identity-version-binding.md) allocates the
Context Packet Contract Definition Identifier and Version. CONTRACT-004
controls Context Packet meaning and authority boundaries.

Accepted ARCH-015 binds one Draft 2020-12 Schema Resource that specializes only the
common-envelope constants, represents the governing Task Contract through one
opaque Artifact Instance/Revision pin, and translates only CONTRACT-004's
Accepted responsibilities into a closed payload.

This is structural evaluation, not semantic proof. Validity cannot establish
that selected context is relevant, sufficient, minimal, current, accessible,
safe to disclose, authoritative, or suitable for execution.

## Governing traceability

| Governing source | Constraint preserved |
| --- | --- |
| [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), and [ARCH-003](artifact-contract-schema-architecture.md) | Final human authority, separate identity/version dimensions, layering, evidence limits, and public/private separation remain unchanged. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) and the [Accepted common schema](../../schemas/common-artifact-envelope/1.0.0/schema.json) | The complete common envelope remains independently governed and is referenced once at its exact root identity. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) | The Context Packet logical identity, independent version line, closed artifact root, payload ownership, and rollout order remain controlling. |
| [ARCH-011](contract-definition-identity-version-binding.md) | The exact Context Packet Contract Definition Identifier `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet` and Version `1.0.0` are used. |
| [ARCH-012](project-charter-executable-schema.md), [ARCH-013](workstream-executable-schema.md), and [ARCH-014](task-contract-executable-schema.md) | Accepted resources remain unchanged and are not referenced by this schema. |
| [CONTRACT-004](../contracts/context-packet-contract.md) | Only Accepted context-selection, provenance, exclusion, freshness, uncertainty, transformation, security/privacy, sufficiency, stop, lifecycle, and traceability responsibilities become structure. |
| [Issue #56](https://github.com/CNTX-PROJECT/CNTX/issues/56) | Exact baseline, eight-path scope, validation, transparent review, stop gate, and prohibited actions remain binding. |

## Exact resource identity and version

| Dimension | Accepted value |
| --- | --- |
| Logical Schema Identity | CNTX Public Core Schema Family / Context Packet Artifact |
| Schema language | JSON Schema |
| Dialect | Draft 2020-12 |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/context-packet/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #56 and Owner acceptance comment `5216466742` |

The `$id` is the stable identity of this exact Schema Version. Its
HTTPS form neither requires nor authorizes network access. It is not a branch,
tag, release, resolver mapping, registry entry, hosted-publication guarantee,
Serialization Binding, trust marker, or authority source.

Schema Version, Contract Definition Version, Artifact Instance Identifier,
Artifact Revision, Document Status, approval state, Content Digest, Provenance
Reference, implementation, release, and deployment remain distinct.

## Complete artifact root

The resource evaluates one complete Context Packet Artifact Instance in the
JSON-compatible instance model. The root is closed and has exactly two
required direct members: `envelope` and `payload`. It cannot be flattened,
opened, extended by an unknown root property, or used to treat either member
alone as a complete Context Packet.

## Common Artifact Envelope specialization

`/envelope` uses exactly one static external reference:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

A local overlay constrains only these constants:

| Envelope coordinate | Exact constant |
| --- | --- |
| `artifactType` | `context-packet` |
| `governingContract.identifier` | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet` |
| `governingContract.version` | `1.0.0` |
| `governingSchema.identifier` | `https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0` |
| `governingSchema.version` | `1.0.0` |

The overlay does not copy, weaken, open, or redefine the common resource. The
common schema retains ownership of artifact identity, governing coordinates,
provenance references, digest evidence, lexical assertions, and envelope
closure.

## Governing Task Contract and dependency boundary

`governingTaskContract` is mandatory and contains exactly two required
non-blank opaque strings: `artifactInstanceIdentifier` and
`artifactRevision`. The schema does not allocate either value, retrieve or
resolve the Task Contract, embed it, validate it, or prove existence,
applicability, approval, currency, or authority.

The resource contains no `$ref` to Project Charter, Workstream, Task Contract,
peer Context Packet, Execution Result, or any other artifact-specific schema.
Context derived from those sources can appear only as provenance-bearing
declarative Context Packet data.

## Closed payload model

The payload contains exactly thirteen required direct properties:

| Property | Structural responsibility | Explicit non-meaning |
| --- | --- | --- |
| `governingTaskContract` | Opaque governing Task Contract Artifact Instance/Revision pin. | No retrieval, embedded contract, schema dependency, approval, or authority proof. |
| `selectionPurpose` | Task objective, packet purpose, intended use, and intended executor class. | No relevance, sufficiency, assignment, access, capability, or execution authority. |
| `applicableGoverningContext` | Assessed charter, workstream, approval, review, and decision context. | No embedded governing artifact, approval evidence, or replacement authority. |
| `selectedSources` | Non-empty provenance-bearing source entries and representation treatments. | No source selection, retrieval, ranking, access, disclosure, or transformation algorithm. |
| `exclusionsAndForbiddenContext` | Excluded, forbidden, inaccessible, omitted, and redaction-boundary declarations. | No access control, filter, retrieval block, or enforcement. |
| `provenanceAndPinning` | Provenance, pinning, derivation, and limitation declarations. | No digest algorithm, signature, trust, registry, resolver, or authenticity proof. |
| `freshnessAndApplicability` | Freshness/applicability assessments, staleness risks, and reassessment triggers. | No clock, timer, score, scheduler, automatic invalidation, or state transition. |
| `assumptionsDependenciesAndUncertainty` | Assumptions, dependencies, uncertainty, conflicts, and missing/inaccessible-source impacts. | No automatic resolution or fallback authority. |
| `transformationAndRedaction` | Summary, extraction, transformation, redaction, sanitization, and loss limits. | No algorithm or fidelity, completeness, reversibility, confidentiality, or safe-disclosure proof. |
| `securityPrivacyAndAccess` | Security, privacy, confidentiality, boundary, access, and least-disclosure constraints. | No access grant, credential, policy engine, or disclosure permission. |
| `sufficiencyAndMinimization` | Relevance evidence, sufficiency/minimization rationales, validation obligations, limitations, and specialist boundaries. | No proof of relevance, sufficiency, minimality, correctness, completeness, privacy, or security. |
| `stopAndEscalation` | Stop and escalation conditions. | No workflow, notification, queue, timer, state, scheduler, or orchestrator. |
| `lifecycleAndExecutionTraceability` | Assessed lifecycle categories and execution-traceability requirements. | No lifecycle state machine, timestamp, automation, Execution Result embedding, or execution proof. |

Every defined object is closed. Unknown payload and nested properties are
invalid. Required ordinary arrays are non-empty and unique by JSON value.
Ordinary strings are non-blank.

## Selected-source model

`selectedSources` is a required non-empty unique array. Each closed entry
requires exactly:

1. `sourceReference`;
2. `sourceType`;
3. `relevanceRationale`;
4. `revisionOrVersionContext`;
5. `includedMaterial`;
6. `contentTreatments`;
7. `authorityAndApplicabilityContext`; and
8. `knownLossAndLimitations`.

The first three values are non-blank strings. A source reference is opaque and
has no URI, repository, path, registry, resolver, retrieval, access, or
authority semantics. The four assessed categories use declaration sets.

`contentTreatments` is non-empty and unique, with only `direct`,
`summarized`, `extracted`, `redacted`, `transformed`, and
`reference-only`. These tokens describe representation only. They activate
no algorithm and grant no source-read, copy, transform, or disclosure
permission. A reference-only entry may declare `includedMaterial` as
assessed `none`.

## Declaration sets and explicit absence

One internal declaration-set shape is reused wherever a category may be empty
but must be assessed:

- `specified`: a closed object with `disposition: specified` and required
  non-empty unique non-blank `items`;
- `none`: a closed object with only `disposition: none`.

`none` means only assessed for this Artifact Revision with no item declared.
It does not mean unknown, automatically irrelevant, approved, complete, true,
sufficient, minimal, safe, risk-free, authorized, inaccessible, or
permanently absent. It is not Document Status, approval state, lifecycle
state, task progress, retrieval state, or runtime state.

## Lexical, collection, and reference assertions

A shared assertion requires ordinary strings to contain at least one
non-whitespace character. It performs no trimming or Unicode normalization and
assigns no executable grammar. Required arrays are non-empty and unique by
JSON value; ordering assigns no priority, authority, ranking, retrieval,
workflow, or approval order.

The canonical document is one Schema Resource with one root `$schema`, one
root `$id`, internal fragment-local `#/$defs/` references, and exactly one
external common-envelope `$ref`. It has no nested resource, anchor, dynamic
reference, custom vocabulary, `format`, `default`, Hyper-Schema behavior,
artifact-specific schema dependency, or public subschema API.

## Derived and non-authoritative boundary

A Context Packet is derived selection context, not a replacement for its
sources. Included text, summaries, extracts, transformations, redactions,
references, rationales, declarations, and pins remain non-authoritative unless
an applicable governing source separately establishes authority.

Completeness does not prove minimality. Minimality does not prove sufficiency.
Schema validity proves neither. Technical reachability does not grant access;
a reference does not grant disclosure; a declared constraint does not enforce
it; and a governing pin does not prove current authority.

## Conformance and validation boundary

Conformance to this schema means only that one instance satisfies the
structural assertions of the exact Schema Version under the required common
resource mapping. It proves no CONTRACT-004 semantic conformance, relevance,
sufficiency, minimality, freshness, provenance truth, source existence,
authorization, approval, privacy, security, or safe executability.

Processors must receive the exact common resource locally. The canonical
identifier is not permission for automatic network retrieval. Validation
failure without the registered common resource is required evidence that the
dependency is explicit rather than silently fetched.

## Synthetic test evidence

The [test manifest](../../tests/schemas/context-packet/1.0.0/cases.json)
contains exactly twenty ordered public-safe synthetic cases: three valid and
seventeen invalid. Coverage includes the root, common-envelope constants,
opaque Task Contract pin, all thirteen responsibilities, selected-source and
treatment rules, declarations, lexical and collection rules, closure, and
forbidden executable or embedded-artifact shapes.

Fixtures are non-normative structural evidence. They are not canonical Context
Packets, Approved Task Contracts, executable selections, retrieval results,
templates, forms, prompts, RAG payloads, access policies, Serialization
Bindings, conformance claims, reference implementations, or releases.

## Security and privacy

The schema requires explicit security, privacy, confidentiality,
public/private, access, and least-disclosure constraints but cannot determine
whether they are adequate or followed. Public fixtures use only synthetic
content. Secrets, credentials, personal data, production configuration,
private paths, restricted content, and private implementation details remain
outside this public resource.

## Consequences and tradeoffs

- A complete Context Packet becomes structurally evaluable after separate
  acceptance and integration.
- All thirteen CONTRACT-004 responsibility groups are explicit and closed.
- Opaque source references preserve technology neutrality but require semantic
  human review.
- Explicit absence avoids fabricated placeholders but is more verbose.
- Static schema composition supports offline deterministic validation while
  requiring callers to supply the common resource.
- Structural rigor cannot prove selection quality, authority, access,
  relevance, sufficiency, minimality, or safe disclosure.

## Rejected alternatives

Rejected alternatives include an open or flat root; copied or dynamic common
schema content; embedded or schema-referenced governing/downstream artifacts;
unrestricted context dumps; automatic search, ranking, retrieval, RAG,
embedding, vector storage, prompt assembly, token budgets, chunking, or
truncation; executable access/disclosure policies; automatic conflict
resolution; transformation/redaction algorithms; approval, signature, trust,
credential, freshness-engine, state-machine, workflow, runtime, and provider
fields; unknown properties; null or fabricated `N/A`; mandatory network
resolution; and validation or review as acceptance.

## Deferred and explicitly unauthorized scope

This decision defines no Artifact Instance, identifier generation, revision
sequencing, artifact-specific schema dependency, automatic source selection or
retrieval, search/ranking/RAG/embedding/vector mechanism, prompt assembly,
token handling, transformation/redaction/sanitization algorithm, access
control, disclosure mechanism, digest method, canonicalization, signature,
verification, trust store, Serialization Binding, canonical JSON, validator,
validation-output contract, resolver, registry, cache, bundler, network
access, conformance tool, code generator, migration, template, form, prompt,
API, CLI, workflow, scheduler, orchestrator, runtime, implementation, product,
release, tag, hosted publication, or deployment.

## Continuing gate

The exact reviewed candidate was accepted by the Owner / Final Authority in
issue comment `5216466742`. Governed integration to `main` activates exactly
Context Packet Schema Version `1.0.0`. No Execution Result or other follow-on
Schema Resource is automatically authorized by this decision.
