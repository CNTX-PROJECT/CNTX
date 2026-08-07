# CNTX Evidence Bundle Executable Schema Definition (ARCH-017)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted executable-schema architecture decision governed
by [issue #60](https://github.com/CNTX-PROJECT/CNTX/issues/60) and recorded by
[ADR-0017](adr/0017-evidence-bundle-executable-schema.md). Owner / Final
Authority acceptance of the exact reviewed candidate is recorded in issue
comment `5217888146`.

The exact reviewed [Schema Resource](../../schemas/evidence-bundle/1.0.0/schema.json) and
[synthetic test evidence](../../tests/schemas/evidence-bundle/1.0.0/cases.json)
are Accepted in the revision recorded by Owner / Final Authority acceptance
comment `5217888146`. On governed integration to `main`, Evidence Bundle Schema
Version `1.0.0` becomes active within this exact scope. The transparent
non-independent review was evidentiary only and did not grant acceptance.

This decision remains subordinate to Accepted architecture, Accepted
[CONTRACT-006](../contracts/evidence-bundle-contract.md), repository governance,
and final human authority. It modifies no Accepted source and creates no
Evidence Bundle Artifact Instance, collection or access authority, evidentiary
sufficiency decision, acceptance, integration, release, deployment, or merge
authority.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Evidence Bundle
Artifact** identity, an inactive `1.0.0` target, a closed
`envelope`/`payload` root, and the exact Common Artifact Envelope dependency.
Accepted [ARCH-011](contract-definition-identity-version-binding.md) allocates
the Evidence Bundle Contract Definition Identifier and Version. CONTRACT-006
controls Evidence Bundle meaning and authority boundaries.

Accepted ARCH-017 binds one Draft 2020-12 Schema Resource that specializes
only the common-envelope constants, represents the governing Task Contract
through one opaque Artifact Instance/Revision pin, represents every other
artifact relationship through explicit opaque-pin declarations, and
translates only CONTRACT-006 responsibilities into a closed payload.

The Evidence Bundle remains Evidentiary, bounded, and non-self-approving. It
can structurally record claims that evidence supports, qualifies,
contradicts, or insufficiently supports a bounded claim. Structural validity
cannot establish that a source exists, was authorized, is authentic or
current, supports a claim, is independent, is sufficient, or permits a
decision, acceptance, integration, release, deployment, or merge.

## Governing traceability

| Governing source | Constraint preserved |
| --- | --- |
| [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), and [ARCH-003](artifact-contract-schema-architecture.md) | Final human authority, separate identity/version dimensions, layering, evidence limits, and public/private separation remain unchanged. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) and the [Accepted common schema](../../schemas/common-artifact-envelope/1.0.0/schema.json) | The complete common envelope remains independently governed and is referenced once at its exact root identity. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) | The Evidence Bundle logical identity, independent version line, closed artifact root, payload ownership, and dependency-first rollout order remain controlling. |
| [ARCH-011](contract-definition-identity-version-binding.md) | The exact Evidence Bundle Contract Definition Identifier `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/evidence-bundle` and Version `1.0.0` are used. |
| [ARCH-012](project-charter-executable-schema.md), [ARCH-013](workstream-executable-schema.md), [ARCH-014](task-contract-executable-schema.md), [ARCH-015](context-packet-executable-schema.md), and [ARCH-016](execution-result-executable-schema.md) | Accepted resources remain unchanged and are not referenced by this schema. |
| [CONTRACT-006](../contracts/evidence-bundle-contract.md) | Only Accepted governing-pin, reviewable-subject, artifact-relationship, evidence-item, claim-traceability, relevance/scope/minimization, provenance/collection/observation, derivation/transformation/loss, check/assumption/condition/dependency, integrity/authenticity/freshness/validity, completeness/coverage/independence/reproducibility, contradictory/adverse/missing/unavailable/excluded, uncertainty/limitation/bias/gap, security/privacy/access/disclosure/retention, and review/decision/lifecycle-traceability responsibilities become structure. |
| [Issue #60](https://github.com/CNTX-PROJECT/CNTX/issues/60) | Exact baseline, eight-path scope, validation, transparent review, stop gate, and prohibited actions remain binding. |

## Exact resource identity and version

| Dimension | Accepted value |
| --- | --- |
| Logical Schema Identity | CNTX Public Core Schema Family / Evidence Bundle Artifact |
| Schema language | JSON Schema |
| Dialect | Draft 2020-12 |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/evidence-bundle/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #60 and Owner acceptance comment `5217888146` |

The `$id` is the stable identity of this exact Schema Version. Its
HTTPS form neither requires nor authorizes network access. It is not a branch,
tag, release, resolver mapping, registry entry, hosted-publication guarantee,
Serialization Binding, trust marker, or authority source.

Schema Version, Contract Definition Version, Artifact Instance Identifier,
Artifact Revision, source or subject revision, Document Status, approval
state, Content Digest, Provenance Reference, evidence freshness or validity,
implementation, release, and deployment remain distinct.

## Complete artifact root

The resource evaluates one complete Evidence Bundle Artifact Instance in the
JSON-compatible instance model. The root is closed and has exactly two
required direct members: `envelope` and `payload`. It cannot be flattened,
opened, extended by an unknown root property, or used to treat either member
alone as a complete Evidence Bundle.

## Common Artifact Envelope specialization

`/envelope` uses exactly one static external reference:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

A local overlay constrains only these constants:

| Envelope coordinate | Exact constant |
| --- | --- |
| `artifactType` | `evidence-bundle` |
| `governingContract.identifier` | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/evidence-bundle` |
| `governingContract.version` | `1.0.0` |
| `governingSchema.identifier` | `https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0` |
| `governingSchema.version` | `1.0.0` |

The overlay does not copy, weaken, open, or redefine the common resource. The
common schema retains ownership of artifact identity, governing coordinates,
provenance references, digest evidence, lexical assertions, and envelope
closure.

## Governing Task Contract and artifact-relationship boundary

`governingTaskContract` is mandatory and contains exactly two required
non-blank opaque strings: `artifactInstanceIdentifier` and
`artifactRevision`. The schema does not allocate either value, retrieve or
resolve the Task Contract, embed or validate it, or prove existence,
applicability, approval, currency, completeness, or authority.

`artifactRelationships` explicitly declares specified opaque pins or assessed
absence for Project Charters, Workstreams, Context Packets, Execution Results,
peer Evidence Bundles, Review Records, Decision Records, and State Snapshots.
No relationship transfers authority, proves relevance, retrieves a resource,
or creates a schema dependency.

The resource contains no `$ref` to Project Charter, Workstream, Task Contract,
Context Packet, Execution Result, peer Evidence Bundle, Review Record, Decision
Record, State Snapshot, or any other artifact-specific schema.

## Closed payload model

The payload contains exactly fifteen required direct properties:

| Property | Structural responsibility | Explicit non-meaning |
| --- | --- | --- |
| `governingTaskContract` | Opaque governing Task Contract Artifact Instance/Revision pin. | No retrieval, embedded contract, schema dependency, approval, or authority proof. |
| `reviewableSubjects` | Non-empty exact subject/revision and bounded-claim declarations. | No subject-type interpretation, retrieval, claim truth, relevance, or acceptance proof. |
| `artifactRelationships` | Specified-or-none opaque pins for the eight related artifact categories. | No artifact embedding, reference resolution, schema dependency, authority transfer, or lifecycle effect. |
| `evidenceItems` | Specified closed evidence-item declarations or assessed absence. | No collection, access, retrieval, verification, scoring, weighting, or sufficiency proof. |
| `claimEvidenceTraceability` | Non-empty bounded mappings to supporting, qualifying, contradictory, and missing evidence declarations. | No referential-integrity, support, contradiction, relevance, truth, or sufficiency proof. |
| `relevanceScopeAndMinimization` | Scope, relevance, inclusion, exclusion, minimization, and least-disclosure declarations. | No automatic selection, ranking, omission authority, disclosure permission, or completeness proof. |
| `provenanceCollectionAndObservationContext` | Assembly provenance, authority context, revisions, conditions, environment, and gaps. | No collection authority, source authenticity, chain of custody, or environment capture mechanism. |
| `derivationTransformationAndInformationLoss` | Inputs, transformations, summaries, extracts, normalizations, conversions, aggregations, redactions, and loss declarations. | No transformation, summarization, extraction, normalization, conversion, aggregation, redaction, or sanitization algorithm. |
| `checksAssumptionsConditionsAndDependencies` | Check/output, assumption, condition, environment, method, tool, and dependency declarations. | No validator, tool execution, standardized validation output, or automated check. |
| `integrityAuthenticityFreshnessAndValidity` | Integrity, authenticity, freshness, validity, and custody-context claims. | No digest, canonicalization, signature, verification, timestamp, trust store, or custody mechanism. |
| `completenessCoverageIndependenceAndReproducibility` | Separate bounded quality and sufficiency claims. | No score, confidence, grade, threshold, proof, independent corroboration, or approval. |
| `contradictoryAdverseMissingUnavailableAndExcludedEvidence` | Explicit contradictory, adverse, missing, unavailable, inaccessible, excluded, and unresolved-conflict declarations. | No favorable-evidence filter, automatic exclusion, deduplication, corroboration, or conflict resolution. |
| `uncertaintyLimitationsBiasAndUnresolvedGaps` | Explicit uncertainty, limitation, bias, transformation-loss, and unresolved-gap declarations. | No automatic resolution, fallback authority, or safe/sufficient conclusion. |
| `securityPrivacyAccessDisclosureAndRetention` | Security/privacy observations and access, collection-authority, disclosure, redaction, restricted-handling, and residual-risk limitations. | No permission, access control, disclosure, redaction, retention, archival, disposal, encryption, or enforcement mechanism. |
| `reviewDecisionAndLifecycleTraceability` | Opaque review/decision references and decision-input, correction, supplementation, supersession, withdrawal, staleness, retention, archival, disposal, and history declarations. | No review, decision, approval, correction, state transition, lifecycle action, workflow, or final authority. |

Every defined object is closed. Unknown payload and nested properties are
invalid. Required ordinary arrays are non-empty and unique by JSON value.
Ordinary strings are non-blank.

## Reviewable-subject model

`reviewableSubjects` is required, non-empty, and unique by JSON value. Each
closed entry requires exactly:

1. `subjectReference`;
2. `subjectIdentifier`;
3. `subjectRevision`;
4. `boundedClaimReferences`; and
5. `subjectScopeAndContext`.

Subject and claim references are opaque. The schema defines no subject-type
enumeration and performs no artifact retrieval, type identification,
relationship validation, or claim assessment.

## Evidence-item model

`evidenceItems` uses an exclusive specified-or-none declaration. Each
specified closed item requires exactly:

1. `evidenceItemReference`;
2. `claimReferences`;
3. `sourceReference`;
4. `sourceRevisionContext`;
5. `observationCollectionAndConditions`;
6. `representationTreatments`;
7. `relevanceRationale`;
8. `provenanceIntegrityAndValidityContext`;
9. `uncertaintyLimitationsAndBias`; and
10. `securityPrivacyAccessAndDisclosure`.

`representationTreatments` is non-empty and unique, with only `direct`,
`derived`, `summarized`, `transformed`, `redacted`, and `copied`. These tokens
describe representation context only. They implement no treatment, classify
no evidence quality, allocate no access or disclosure permission, and assign
no evidentiary weight.

## Claim-to-evidence traceability

`claimEvidenceTraceability` is required, non-empty, and unique by JSON value.
Each closed mapping requires exactly:

1. `claimReference`;
2. `subjectReference`;
3. `supportingEvidenceReferences`;
4. `qualifyingEvidenceReferences`;
5. `contradictoryEvidenceReferences`;
6. `missingEvidence`; and
7. `assessmentAndLimitations`.

The mapping structure does not prove that referenced items exist, are
distinct, resolve, originate from an authorized source, support or contradict
the claim, cover all material evidence, or are relevant, independent,
complete, sufficient, correct, current, authentic, or accepted.

## Declaration sets and explicit absence

One internal statement declaration-set shape is reused wherever a category may
be empty but must be assessed:

- `specified`: a closed object with `disposition: specified` and required
  non-empty unique non-blank `items`;
- `none`: a closed object with only `disposition: none`.

Artifact-pin and Evidence Item declarations use the same mutually exclusive
dispositions with their own closed item schemas.

`none` means only assessed for this Artifact Revision with no item declared.
It does not mean unknown, irrelevant, approved, complete, correct, sufficient,
safe, risk-free, authorized, inaccessible, or permanently absent.

## Lexical, collection, and reference assertions

A shared assertion requires ordinary strings to contain at least one
non-whitespace character. It performs no trimming or Unicode normalization and
assigns no executable grammar. Required arrays are non-empty and unique by
JSON value; ordering assigns no chronology, priority, authority, collection,
retrieval, review, decision, acceptance, or workflow order.

The canonical document is one Schema Resource with one root `$schema`, one
root `$id`, internal fragment-local `#/$defs/` references, and exactly one
external common-envelope `$ref`. It has no nested resource, anchor, dynamic
reference, custom vocabulary, `format`, `default`, Hyper-Schema behavior,
artifact-specific schema dependency, or public subschema API.

## Evidentiary and non-self-approving boundary

An Evidence Bundle records bounded claims about evidence and its context. It
cannot modify, broaden, replace, reinterpret, or retroactively authorize its
governing Task Contract; modify or approve its reviewable subject; replace
authoritative sources; or silently transfer claims, context, or authority
between tasks or artifacts.

Source possession, schema validity, collection success, a digest, a signature,
a timestamp, tool output, validation, review, or a conformance claim is
evidence only for its bounded source, scope, conditions, and environment. It
does not become a decision. Material contradictory, adverse, missing,
unavailable, inaccessible, redacted, or excluded evidence remains explicit.

## Conformance and validation boundary

Conformance to this schema means only that one instance satisfies the
structural assertions of the exact Schema Version under the required common
resource mapping. It proves no CONTRACT-006 semantic conformance, source or
claim truth, authenticity, integrity, relevance, independence, coverage,
completeness, reproducibility, sufficiency, correctness, authorization,
acceptance, integration, release, deployment, or merge permission.

Processors must receive the exact common resource locally. The canonical
identifier is not permission for automatic network retrieval. Validation
failure without the registered common resource is required evidence that the
dependency is explicit rather than silently fetched.

## Synthetic test evidence

The [test manifest](../../tests/schemas/evidence-bundle/1.0.0/cases.json)
contains exactly twenty ordered public-safe synthetic cases: three valid and
seventeen invalid. Coverage includes the root, common-envelope constants,
opaque Task Contract and artifact pins, all fifteen responsibilities,
reviewable subjects, Evidence Items and treatments, claim traceability,
declarations, lexical and collection rules, closure, and forbidden executable,
authority, workflow, runtime, or embedded-artifact shapes.

Fixtures are non-normative structural evidence. They are not canonical
Evidence Bundles, approved Task Contracts, actual evidence, quality or
sufficiency determinations, Review Records, Decision Records, templates,
forms, prompts, workflows, Serialization Bindings, conformance claims,
reference implementations, releases, or deployments.

## Security and privacy

The schema can record security, privacy, access, disclosure, redaction,
retention, and residual-risk claims but cannot determine whether they are
adequate or followed. Public fixtures use only synthetic content. Secrets,
credentials, personal data, production configuration, private paths,
restricted content, private source material, and private implementation
details remain outside this public resource.

## Consequences and tradeoffs

- A complete Evidence Bundle can become structurally evaluable only after
  separate acceptance and governed integration.
- All fifteen CONTRACT-006 responsibility groups are explicit and closed.
- Opaque subject, artifact, evidence, and claim references preserve technology
  neutrality but require semantic human review.
- Explicit absence avoids fabricated placeholders but is more verbose.
- Treatment tokens preserve representation distinctions without defining an
  algorithm or evidence taxonomy.
- Static schema composition supports offline deterministic validation while
  requiring callers to supply the common resource.
- Structural rigor cannot prove provenance, authenticity, relevance,
  independence, completeness, sufficiency, correctness, authority,
  acceptance, integration, release, deployment, or merge permission.

## Rejected alternatives

Rejected alternatives include an open or flat root; copied or dynamic common
schema content; embedded or schema-referenced governing, subject, context,
result, peer, review, decision, state, or downstream artifacts; unrestricted
evidence collection; universal scores, confidence scales, grades, weights, or
thresholds; automatic selection, retrieval, ranking, deduplication,
corroboration, conflict resolution, verification, redaction, retention,
decision, approval, lifecycle, workflow, or runtime behavior; network-dependent
resolution; unknown properties; null or fabricated `N/A`; canonical JSON
assumptions; and validation or review as acceptance.

## Deferred and explicitly unauthorized scope

This decision defines no Artifact Instance, identifier generation, revision
sequencing, artifact-specific schema dependency, collection, capture,
retrieval, search, ranking, scoring, deduplication, corroboration, conflict
resolution, access control, disclosure, validator implementation/output
contract, digest method, encoding, canonicalization, signature, verification,
encryption, timestamp, trust store, chain-of-custody, transformation,
summarization, extraction, normalization, conversion, aggregation, redaction,
sanitization, retention, archival, disposal, Serialization Binding, canonical
JSON, Extension Module/Profile, resolver, registry, catalog, cache, bundler,
network access, conformance tool, code generator, migration, template, form,
prompt, API, CLI, workflow, scheduler, orchestrator, runtime, implementation,
product, release, tag, hosted publication, or deployment.

## Continuing gate

The exact reviewed candidate was accepted by the Owner / Final Authority in
issue comment `5217888146`. Governed integration to `main` activates exactly
Evidence Bundle Schema Version `1.0.0`.

No Review Record or other follow-on Schema Resource is automatically
authorized by this decision.
