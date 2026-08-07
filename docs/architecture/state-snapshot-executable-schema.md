# CNTX State Snapshot Executable Schema Definition (ARCH-020)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed executable-schema architecture candidate governed
by [issue #66](https://github.com/CNTX-PROJECT/CNTX/issues/66) and recorded by
[ADR-0020](adr/0020-state-snapshot-executable-schema.md).

The candidate [Schema Resource](../../schemas/state-snapshot/1.0.0/schema.json)
and [synthetic test evidence](../../tests/schemas/state-snapshot/1.0.0/cases.json)
are Proposed and inactive. Creation, validation, publication in a Draft pull
request, and a transparent non-independent review grant no acceptance or
activation. Only separate attributable EIGENAAR / Final Authority acceptance
of the exact reviewed head may authorize a status-only promotion; that later
phase is not authorized by this document or issue.

This candidate remains subordinate to Accepted architecture, Accepted
[CONTRACT-009](../contracts/state-snapshot-contract.md), repository governance,
controlling sources, and final human authority. It modifies no Accepted source
and creates no State Snapshot Artifact Instance, authority, evidence, approval,
decision, task authorization, integration, release, deployment, publication,
merge permission, or follow-on authority.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / State Snapshot
Artifact** identity, an inactive `1.0.0` target, a closed `envelope`/`payload`
root, and the exact Common Artifact Envelope dependency. Accepted
[ARCH-011](contract-definition-identity-version-binding.md) allocates the
State Snapshot Contract Definition Identifier and Version. CONTRACT-009
controls State Snapshot meaning, Derived classification, controlling-source
precedence, uncertainty preservation, temporal distinctions, historical
provenance, bounded handoff, and final human authority.

Proposed ARCH-020 binds one Draft 2020-12 Schema Resource that specializes only
the common-envelope constants, represents sources and artifact relationships
through opaque identifiers and exact revisions or explicit pinning
limitations, and translates only CONTRACT-009 responsibilities into a closed
payload.

The resource does not allocate authority or identity, prove a source claim,
retrieve or interpret a source, calculate freshness, decide precedence,
resolve conflict, update state, synchronize repositories, authorize
continuation, or create a consequential effect.

## Proposed schema identity

| Dimension | Proposed value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / State Snapshot Artifact |
| Artifact token | `state-snapshot` |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0` |
| Schema Version | `1.0.0`, inactive |
| Canonical repository path | `schemas/state-snapshot/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/state-snapshot` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Proposed under issue #66; exact-head acceptance pending |

Repository presence, `$id`, validation, review, or apparent recency does not
activate the resource. The canonical `$id` identifies the candidate resource
but does not promise hosting, registry publication, network retrieval, or
resolver behavior.

## Root and common-envelope specialization

The Schema Resource evaluates one complete artifact with a closed root that
requires exactly:

1. `envelope`; and
2. `payload`.

The `envelope` composes the exact Accepted Common Artifact Envelope through one
static external reference and constrains these five values:

- Artifact Type: `state-snapshot`;
- Contract Definition Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/state-snapshot`;
- Contract Definition Version: `1.0.0`;
- Schema Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0`; and
- Schema Version: `1.0.0`.

The common resource remains independently Accepted and unchanged. All other
schema references are fragment-local. No Project Charter, Workstream, Task
Contract, Context Packet, Execution Result, Evidence Bundle, Review Record,
Decision Record, peer State Snapshot, or other artifact-specific schema is
referenced.

## Closed eighteen-property payload

The payload requires exactly these eighteen direct responsibilities:

| Property | Structural responsibility | Explicit non-effect |
| --- | --- | --- |
| `derivationAuthorityClassificationAndNonAuthority` | Opaque authorized-derivation reference, exact `Derived` classification, scope, limits, and explicit non-authoritative/non-evidentiary boundaries. | No authority, role, identity, credential, approval, decision, or task-authority allocation or proof. |
| `orientationPurposeScopeAudienceAndExclusions` | Bounded purpose, scope, audiences, exclusions, non-self-contained boundary, and source-consultation requirement. | No replacement of controlling sources or permission to copy unrelated/private history. |
| `governingContextControllingSourcesAndPrecedence` | Governing context, controlling-source references, precedence, final-human-authority, source-controls-on-conflict, and visible-conflict boundaries. | No new controlling source, silent conflict resolution, or automatic precedence engine. |
| `sourceIdentityRevisionDigestAndPinningLimitations` | Non-empty sources with identity, applicability, provenance, exact revision or exclusive pinning limitation, and optional opaque digest reference. | No retrieval, digest method, authenticity, correctness, authority, or approval proof. |
| `derivationProvenanceDependenciesAndTemporalCoordinates` | Derivation provenance, source/dependency references, and six distinct opaque temporal coordinates. | No timestamp grammar, clock, ordering, causality, recency, or expiry calculation. |
| `freshnessStalenessAndKnownValidThrough` | Assessments using exactly four CONTRACT-009 freshness tokens with basis, limitations, and non-proof. | No universal status vocabulary, truth proof, or currentness calculation. |
| `relevanceSelectionMinimizationAndMaterialContext` | Relevance basis, minimum selected context, exclusions, non-duplication, and explicit preservation of uncertainty, dependencies, conflicts, omissions, incomplete work, stops, and gaps. | No automatic selection, retrieval, ranking, summarization, redaction, or minimization. |
| `reportedStateClaimsAndOrientationBoundary` | Non-empty reported-state entries with subject, statement, scope, source traceability, limitations, and orientation-not-proof. | No completion, correctness, conformance, currentness, verification, approval, or integration proof. |
| `completionCorrectnessConformanceAndVerificationBoundary` | Five separate specified-or-none claim categories for completion, correctness, conformance, currentness, and verification. | No collapsed status, proof, certification, scoring, or self-approval. |
| `evidenceReviewDecisionAndIntegrationTraceability` | Separate Execution Result, Evidence Bundle, Review Record, Decision Record, and integration-reporting declarations. | No evidence creation, review replacement, decision authority, approval, or integration proof. |
| `artifactRelationships` | Nine required specified-or-none opaque Artifact Instance Identifier/Revision categories. | No embedded artifact, artifact-specific schema reference, retrieval, or referential-integrity proof. |
| `uncertaintyLimitationsOmissionsAndVerificationGaps` | Separate missing, unavailable, unpinned, omission, conflict, verification-gap, and other-limitation declarations with reason and effect. | No fabricated absence, silent resolution, completeness claim, or negative proof. |
| `incompleteWorkStoppedConditionsUnresolvedDecisionsAndRemainingActions` | Four separate specified-or-none categories preserving incomplete work, stops, unresolved decisions, and remaining actions. | No continuation, permission, workflow, or task authority. |
| `snapshotIdentityRevisionAndHistoricalProvenance` | Exact represented snapshot pin, derivation/revision narratives, prior/later pins, and historical-preservation boundary. | No identifier generation, revision sequencing, self-pin comparison, overwrite, or deletion. |
| `peerSnapshotDependenciesReplacementCorrectionSupersessionAndConflicts` | Five exact peer-snapshot relation categories with scope, reason, affected boundary, history, and non-automatic effect. | No latest-wins, silent replacement, automatic merge, mutation, or conflict resolution. |
| `handoffRecipientsContinuationNeedsAndAuthorityBoundary` | Handoff scope, recipients, accessibility, continuation needs, required separate authority, and non-conversation-copy boundary. | No Task Contract, source access, retrieval, disclosure, or continuation authority. |
| `securityPrivacyAccessDisclosureAndRestrictedContext` | Security, privacy, access, confidentiality, restricted-source, exclusion, disclosure, redaction-information-loss, and residual-risk declarations. | No control, permission, enforcement, encryption, redaction, sanitization, retention, or disposal mechanism. |
| `conceptualLifecycleNonAutomaticEffectsAndFollowOnAuthority` | Conceptual `integration → compact state update`, trigger context, non-proof, history, follow-on authority references, and separately authorized actions. | No integration, state, synchronization, transition, workflow, automatic handoff, scheduler, orchestrator, or runtime. |

Every schema-defined object is closed. Unknown payload and nested properties
are invalid. Required ordinary arrays are non-empty and unique by JSON value.
Ordinary required strings contain at least one non-whitespace character.

## Source identity, pinning, and controlling authority

Every source entry has a local reference, opaque source kind and identity,
applicability, provenance, limitations, and exactly one of:

- `exact-revision` with one opaque exact revision; or
- `limitation` with an explicit pinning limitation and uncertainty effect.

An optional opaque content-digest reference assists traceability only. The
schema defines no digest algorithm, encoding, canonicalization, signature,
timestamp, authenticity, correctness, or trust effect.

Source precedence remains declarative. If the snapshot conflicts with a
controlling source, the controlling source governs and the conflict remains
visible. Schema validity cannot determine which external source is authentic,
applicable, current, complete, or controlling.

## Temporal and freshness separation

State applicability, derivation, source, observation, publication, and
known-valid-through context are six independent opaque coordinates. They are
not date-time fields and define no ordering, chronology, clock, expiry, or
currentness algorithm.

Freshness assessments use only:

- `known-current`;
- `possibly-stale`;
- `demonstrably-stale`; or
- `unknown-freshness`.

These tokens are local to the State Snapshot contract. They do not create an
artifact lifecycle or universal status taxonomy. Recent derivation, later
publication, or lack of a newer snapshot proves no currentness.

## Reported state, claims, and traceability

Reported state is orientation, not evidence or proof. Completion, correctness,
conformance, currentness, and verification claims remain five separate
specified-or-none categories. Execution Results, Evidence Bundles, Review
Records, Decision Records, and integration reporting also remain separate.

Their presence, apparent agreement, number, public visibility, or schema
validity does not prove a claim, approve a decision, establish integration, or
create authority. No pass/fail, verdict, severity, confidence, score, grade,
priority, threshold, or implementation-status taxonomy is defined.

## Artifact and peer-snapshot relationships

`artifactRelationships` requires exactly nine categories:

1. Project Charters;
2. Workstreams;
3. Task Contracts;
4. Context Packets;
5. Execution Results;
6. Evidence Bundles;
7. Review Records;
8. Decision Records; and
9. peer State Snapshots.

Each is an exclusive specified-or-none opaque exact-pin declaration. No
artifact is embedded and no artifact-specific schema is referenced.

Peer-snapshot dependency, replacement, correction, supersession, and conflict
are five separate exact relation categories. Each specified relation preserves
the peer pin, scope, reason, affected boundary, history, and non-automatic
effect. No implicit recency, latest-wins, deletion, overwrite, silent merge, or
automatic conflict-resolution rule applies.

## Uncertainty, stops, handoff, and lifecycle

Missing, unavailable, and unpinned sources, omissions, conflicts, verification
gaps, and other material limitations remain explicit. Silence is neither a
resolution nor proof of absence. Incomplete work, stopped conditions,
unresolved decisions, and remaining actions remain separate declarations.

A handoff records bounded recipients, source accessibility or limitations,
continuation needs, and separately required authority. It is not a Task
Contract and cannot authorize retrieval, access, disclosure, or continuation.

The accepted conceptual lifecycle relation is represented exactly as
`integration → compact state update`. It neither proves integration nor
implements a state update. Historical sources and snapshot revisions remain
preserved; follow-on actions retain their own authority gates.

## Security and privacy

Fixtures are synthetic and public-safe. Public snapshots must not expose
secrets, credentials, personal data, production configuration, private paths,
restricted source material, private project data, private implementation
logic, or sensitive operational details.

Security, privacy, access, confidentiality, disclosure, restricted-source,
redaction-information-loss, and residual-risk fields are declarations only.
The schema implements no access control, disclosure control, encryption,
redaction, sanitization, retention, archival, disposal, or verification.

## Test evidence

The [test manifest](../../tests/schemas/state-snapshot/1.0.0/cases.json)
contains exactly twenty ordered public-safe synthetic cases: three valid and
seventeen invalid. It mechanically deep-copies one base instance and applies
declared `add`, `remove`, or `replace` operations using RFC 6901 JSON Pointers.
That fixture representation is non-normative test evidence, not an artifact
Serialization Binding, patch protocol, migration, validator, or runtime.

The valid cases cover:

1. fully pinned bounded orientation after reported integration;
2. partial and stopped state with an explicit unpinned-source limitation,
   uncertainty, evidence/review/decision traceability, gaps, stops, and
   separate continuation authority; and
3. correction and supersession with exact peer pins, stale assessments,
   historical preservation, restricted-source omission, information loss, and
   bounded continuation.

The invalid cases reject missing or unknown roots; wrong envelope constants;
missing mandatory responsibilities; authoritative/self-approving
classification; malformed source precedence or pinning; collapsed temporal or
freshness semantics; empty relevant context; malformed claims, inputs,
relationships, limitations, stops, and peer relations; latest-wins; null,
blank, duplicate, embedded, unknown, runtime, retrieval, synchronization, and
implementation shapes.

Expected aggregate: `20/20`, exactly three valid and seventeen invalid.

## Validation and conformance boundary

Validation requires strict duplicate-free JSON, UTF-8 checks, official Draft
2020-12 schema checking, isolated `jsonschema 4.25.1`, exact offline
registration of Common Artifact Envelope Schema Version `1.0.0`, a required
missing-resource failure, all twenty expected fixture outcomes, exact
root/constants/eighteen-property payload and structural assertions, the exact
reference graph, protected-blob checks, link and privacy/security scans, exact
eight-path scope, exact one-commit candidate state, GitHub read-back, and one
transparent non-independent exact-head COMMENT review.

Schema validity proves structure only. It proves no source identity, source
truth, provenance, applicability, freshness, absence, completeness,
correctness, conformance, verification, evidence, review, decision, approval,
acceptance, integration, authority, security, privacy, release, deployment,
publication, merge permission, or follow-on authority.

## Deferred scope and continuing authority boundary

Deferred and unauthorized: Artifact Instances; identifier generation; revision
sequencing; authority, role, identity, credential, delegation, approval,
signature, verification, trust, timestamp, digest, encoding, canonicalization,
encryption, retrieval, resolver, registry, catalog, cache, bundler, network,
selection, search, ranking, RAG, embedding, summarization, transformation,
freshness calculation, conflict resolution, latest-wins, state,
synchronization, lifecycle, workflow, automatic handoff, access, disclosure,
redaction, sanitization, retention, archival, disposal, and chain-of-custody
mechanisms; Serialization Binding; canonical artifact JSON; Extension
Module/Profile mechanisms; validator/output implementations; conformance
tooling; migration; templates; prompts; API; CLI; runtime; private or reference
implementation; provider; product; release; tag; hosted publication; and
deployment.

The candidate authorizes no Ready transition, Accepted promotion, merge, issue
closure, or public branch cleanup. After one exact-head review, the workflow
must stop for separate attributable EIGENAAR / Final Authority acceptance.

## References

- [CONTRACT-009 State Snapshot](../contracts/state-snapshot-contract.md)
- [Artifact-specific schema family and container boundary](artifact-specific-schema-family-container-boundary.md)
- [Contract Definition identity/version binding](contract-definition-identity-version-binding.md)
- [Common Artifact Envelope Schema Version 1.0.0](../../schemas/common-artifact-envelope/1.0.0/schema.json)
- [Proposed State Snapshot Schema Version 1.0.0](../../schemas/state-snapshot/1.0.0/schema.json)
- [Non-normative synthetic cases](../../tests/schemas/state-snapshot/1.0.0/cases.json)
- [ADR-0020](adr/0020-state-snapshot-executable-schema.md)
- [Issue #66](https://github.com/CNTX-PROJECT/CNTX/issues/66)
