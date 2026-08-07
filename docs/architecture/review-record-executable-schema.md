# CNTX Review Record Executable Schema Definition (ARCH-018)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted executable-schema architecture decision governed by
[issue #62](https://github.com/CNTX-PROJECT/CNTX/issues/62) and recorded by
[ADR-0018](adr/0018-review-record-executable-schema.md).

EIGENAAR / Final Authority acceptance of the exact reviewed candidate is
recorded in issue comment `5218629573`. The exact reviewed
[Schema Resource](../../schemas/review-record/1.0.0/schema.json) and
[synthetic test evidence](../../tests/schemas/review-record/1.0.0/cases.json)
are Accepted in that revision. Governed integration to `main` activates
Review Record Schema Version `1.0.0`. The transparent non-independent review
was Evidentiary only and did not grant acceptance.

This decision remains subordinate to Accepted architecture, Accepted
[CONTRACT-007](../contracts/review-record-contract.md), repository governance,
and final human authority. It modifies no Accepted source and creates no Review
Record Artifact Instance, review authority, specialist qualification, review
outcome, decision, acceptance, integration, release, deployment, or merge
authority.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Review Record
Artifact** identity, an inactive `1.0.0` target, a closed
`envelope`/`payload` root, and the exact Common Artifact Envelope dependency.
Accepted [ARCH-011](contract-definition-identity-version-binding.md) allocates
the Review Record Contract Definition Identifier and Version. CONTRACT-007
controls Review Record meaning, its Evidentiary classification, Specialist
Reviewer authorship, and its non-authoritative decision boundary.

Accepted ARCH-018 binds one Draft 2020-12 Schema Resource that specializes only the
common-envelope constants, represents review and execution authority through
separate opaque Artifact Instance/Revision pin declarations, represents all
other artifact relationships through explicit opaque pins, and translates only
CONTRACT-007 responsibilities into a closed payload.

The resource does not perform a review, determine reviewer qualification,
resolve a subject or evidence item, classify a finding, calculate confidence
or severity, issue a verdict, make a recommendation, synthesize peer reviews,
or record a consequential decision.

## Accepted schema identity

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Review Record Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/review-record/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/review-record` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #62 and EIGENAAR acceptance comment `5218629573` |

Creation, repository presence, validation, and review did not grant acceptance
or activation. Exact-head acceptance is recorded in issue comment
`5218629573`; governed integration to `main` activates this exact version.

## Root and common-envelope specialization

The Schema Resource evaluates one complete artifact with a closed root that
requires exactly:

1. `envelope`; and
2. `payload`.

The `envelope` composes the exact Accepted Common Artifact Envelope through
one static external reference and constrains these five values:

- Artifact Type: `review-record`;
- Contract Definition Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/review-record`;
- Contract Definition Version: `1.0.0`;
- Schema Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0`; and
- Schema Version: `1.0.0`.

The common resource remains independently Accepted and unchanged. All other
schema references are fragment-local. No Project Charter, Workstream, Task
Contract, Context Packet, Execution Result, Evidence Bundle, peer Review Record,
Decision Record, State Snapshot, or later artifact-specific schema is
referenced.

## Closed sixteen-property payload

The payload requires exactly these sixteen direct responsibilities:

| Property | Structural responsibility | Explicit non-effect |
| --- | --- | --- |
| `reviewAuthoritySpecialtyAndReviewer` | Exact opaque Review Authority pin, reviewer reference, non-empty declared specialties, role-overlap/prior-involvement declaration, authority scope, and authority limits. | No identity allocation, specialty taxonomy, credentialing, accreditation, assignment, rank, or independence certification. |
| `executionAuthorityTraceability` | Explicit specified non-empty opaque execution-authority pins or assessed none, separate from Review Authority. | No authority inference, delegation encoding, amendment, transition, or retroactive authorization. |
| `reviewableSubjects` | Non-empty exact subject references with opaque kind, Artifact Instance Identifier/Revision pins, bounded claims, scope, and criteria. | No retrieval, resolution, embedding, type interpretation, claim assessment, or subject mutation. |
| `artifactRelationships` | Nine explicit specified-or-none opaque-pin categories. | No schema coupling, relationship verification, authority transfer, or lifecycle effect. |
| `scopeCriteriaCoverageDepthAndUnreviewedAreas` | Separate scope, criteria, coverage, depth, unreviewed-area, and boundary declarations. | No completeness, quality, sufficiency, or approval proof. |
| `observationsInterpretationsFindingsAndRationale` | Non-empty findings with local reference, subject traceability, and distinct observation, interpretation, finding statement, and rationale. | No verdict, severity, confidence, score, grade, weight, threshold, or approval state. |
| `evidenceUseAndFindingTraceability` | Non-empty finding mappings to subjects, supporting, qualifying, contradictory, missing, and unavailable evidence, methods, and limitations. | No evidence retrieval, evidentiary weight, corroboration, conflict resolution, sufficiency calculation, or truth proof. |
| `methodsChecksToolsConditionsAndAssumptions` | Separate method, check, tool, condition, assumption, and limitation declarations. | No executable procedure, validation engine, toolchain, workflow, or runtime. |
| `uncertaintyLimitationsDissentAndUnresolvedQuestions` | Explicit uncertainty, limitation, dissent, and unresolved-question declarations. | No automatic resolution, confidence calculation, safe conclusion, or decision. |
| `recommendationsAndDecisionBoundary` | Explicit non-empty bounded recommendations or assessed none. | No approval, rejection, acceptance, integration, release, deployment, merge, or other consequential decision. |
| `independenceConflictsPriorInvolvementAndDependencies` | Independence limitations, conflicts, prior involvement, and material dependencies. | No proof or certification of independence, qualification, or authority. |
| `adverseContradictoryMissingUnavailableExcludedAndRedactedInformation` | Separate adverse, contradictory, missing, unavailable, excluded, and redacted information plus its review effect. | No filtering, access, disclosure, redaction, restoration, or conflict-resolution mechanism. |
| `peerReviewsConflictingReviewsAndSynthesis` | Opaque peer-review references plus agreement, difference, bounded synthesis, and remaining dissent. | No silent merge, voting, majority, consensus, ranking, weighting, or automatic synthesis. |
| `correctionSupplementationReassessmentAndHistoricalTraceability` | Correction, supplementation, reassessment, reasons, affected conclusions, later evidence, and history. | No revision sequencing, silent overwrite, retroactive availability, or lifecycle mutation. |
| `securityPrivacyAccessDisclosureAndRetention` | Security, privacy, access, disclosure, retention, redaction-loss, and residual-risk declarations. | No permission grant, access control, disclosure, retention, archival, disposal, redaction, encryption, or enforcement. |
| `escalationStopAndLifecycleTraceability` | Escalation, stop, lifecycle limits, follow-up, and historical traceability. | No escalation engine, workflow execution, state transition, scheduler, or orchestration. |

Every defined object is closed. Unknown payload and nested properties are
invalid. Required ordinary arrays are non-empty and unique by JSON value.
Ordinary strings require at least one non-whitespace character.

## Authority separation

`reviewAuthoritySpecialtyAndReviewer.reviewAuthority` is one exact opaque
Artifact Instance Identifier/Revision pin. It records the approved source that
authorizes this bounded review; it does not allocate, validate, amend, replace,
or transition that authority.

`executionAuthorityTraceability` separately records one or more opaque
execution-authority pins or assessed absence. Review Authority does not replace
or broaden Execution Authority. Execution Authority does not automatically
authorize specialist review. Missing, conflicting, ambiguous, privacy-sensitive,
or security-sensitive authority requires stop or escalation rather than
inference.

## Reviewable subjects and artifact relationships

`reviewableSubjects` is required, non-empty, and unique by JSON value. Each
closed entry requires exactly:

1. `subjectReference`;
2. `subjectKind`;
3. `artifactInstanceIdentifier`;
4. `artifactRevision`;
5. `boundedClaimReferences`;
6. `reviewScope`; and
7. `reviewCriteria`.

Subject kinds, identifiers, revisions, claims, scope, and criteria remain
opaque or declarative. The schema performs no retrieval, resolution,
referential-integrity check, content validation, or authorization.

`artifactRelationships` requires exactly nine categories:

1. Project Charters;
2. Workstreams;
3. Task Contracts;
4. Context Packets;
5. Execution Results;
6. Evidence Bundles;
7. peer Review Records;
8. Decision Records; and
9. State Snapshots.

Every category is an exclusive specified-or-none artifact-pin declaration. No
category embeds an artifact or references its artifact-specific schema.

## Findings and evidence traceability

Every finding keeps observation, interpretation, finding statement, subject
references, and supporting rationale structurally separate. This separation
prevents one untyped value from silently combining fact, analysis, conclusion,
and reasoning.

Every evidence-use mapping preserves the related finding, subject, supporting,
qualifying, contradictory, missing, and unavailable evidence references,
methods, and limitations. The schema does not establish that a reference
exists, resolves, is authentic, was lawfully obtained, supports or contradicts
a finding, is independent, or is complete, sufficient, correct, current, safe,
or accepted.

## Recommendations and final human authority

A recommendation uses an exclusive specified-or-none declaration. Every
specified recommendation is tied to one or more finding references and keeps
its statement, conditions, and limitations explicit.

A recommendation remains specialist Evidentiary input. It is not approval,
rejection, acceptance, integration, release, deployment, merge, or another
consequential decision. Review count, majority, apparent consensus, reviewer
title, schema validity, test success, or tool output grants no decision
authority. Final consequential authority remains human or explicitly
human-governed.

## Peer review, correction, and history

Peer Review Record pins remain independent artifacts. Agreement and
disagreement remain explicit; a bounded synthesis cannot erase source reviews,
specialty limits, conflicts, uncertainty, dissent, or unreviewed scope.

Correction, supplementation, reassessment, later evidence, and affected
conclusions remain historically distinguishable. The schema does not define
Artifact Revision sequencing, supersession rules, freshness logic, or a
lifecycle transition. Later evidence is not represented as having been
available to an earlier reviewer.

## Declaration sets and explicit absence

Statement categories use one reusable mutually exclusive shape:

- `specified`: a closed object with `disposition: specified` and required
  non-empty unique non-blank `items`;
- `none`: a closed object with only `disposition: none`.

Artifact-pin and recommendation categories use the same dispositions with
their own closed item schemas.

`none` means only assessed absence for this Artifact Revision. It does not
mean unknown, irrelevant, complete, correct, sufficient, independent, safe,
risk-free, accepted, approved, inaccessible, or permanently absent.

## Lexical, collection, and reference assertions

A shared assertion requires ordinary strings to contain at least one
non-whitespace character. It performs no trimming, normalization, identifier
allocation, or executable grammar. Required arrays are non-empty and unique by
JSON value. Array ordering assigns no chronology, priority, authority, review,
decision, acceptance, or workflow order.

The canonical document is one Schema Resource with one root `$schema`, one
root `$id`, internal fragment-local `#/$defs/` references, and exactly one
external Common Artifact Envelope `$ref`. It has no nested resource, anchor,
dynamic reference, custom vocabulary, `format`, `default`, Hyper-Schema
behavior, artifact-specific schema dependency, or public subschema API.

## Synthetic validation evidence

The non-normative test manifest defines exactly twenty ordered public-safe
cases: three valid and seventeen invalid.

The valid cases cover:

1. a minimal inconclusive single-subject review with no recommendation;
2. a review of opaque Execution Result and Evidence Bundle pins with supporting
   and adverse findings, evidence traceability, methods, and a bounded
   recommendation; and
3. peer comparison with disagreement, dissent, role overlap, redaction loss,
   later evidence, correction, reassessment, and historical traceability.

The invalid cases cover missing or unknown roots, wrong envelope constants,
missing or malformed authority, subjects, relationships, findings, evidence
traceability, recommendations, mandatory payload responsibilities, and a
composite prohibited implementation/decision shape.

Expected validity is structural evidence only. It proves no contract
conformance, reviewer competence, review quality, subject truth, evidence
authenticity, finding correctness, recommendation quality, approval,
acceptance, integration, release, deployment, or merge permission.

## Conformance and validation boundary

Conformance to this schema means only that one instance satisfies this exact
Accepted Schema Resource under the exact locally registered Common Artifact
Envelope resource. The schema does not evaluate full CONTRACT-007 conformance,
authority validity, specialty appropriateness, referential integrity,
provenance, authenticity, evidence relevance, independence, completeness,
coverage, reproducibility, sufficiency, correctness, security, privacy,
decision validity, or final human approval.

A schema-valid Review Record remains Evidentiary and non-self-approving.
Validation failure proves only that the tested instance does not satisfy this
schema; it does not itself create an authorized rejection, rollback, stop,
transition, or remediation order.

## Security and privacy boundary

The schema records security, privacy, access, disclosure, retention, and
redaction-loss declarations but implements none of their mechanisms. Technical
access or possession is not authority to review, retain, transform, disclose,
publish, or redistribute material.

Public instances and fixtures must not expose secrets, credentials, personal
data, production configuration, private paths, restricted content, or private
implementation details. Redaction and exclusion remain visible with their
material information loss and limitations.

## Deferred and unauthorized scope

ARCH-018 does not authorize:

- changes to CONTRACT-007 or prior Accepted architecture;
- a Review Record Artifact Instance or revision mechanism;
- reviewer identity allocation, specialty taxonomy, accreditation,
  credentialing, assignment, ranking, or independence certification;
- governing, subject, evidence, peer-review, decision, or state retrieval,
  resolution, embedding, or artifact-to-artifact schema references;
- review execution, evidence collection, finding generation/classification,
  recommendation generation, automatic synthesis, corroboration, conflict
  resolution, voting, majority, consensus, ranking, or routing;
- outcome, verdict, pass/fail, severity, confidence, score, grade, weight,
  threshold, rubric, checklist, quality-gate, approval, rejection, or decision
  taxonomies or engines;
- digest, canonicalization, signature, verification, encryption, timestamp,
  trust, custody, redaction, sanitization, or retention mechanisms;
- Artifact Serialization Binding or canonical artifact JSON;
- Extension Module or Profile mechanisms;
- validator implementation, validation-output contract, resolver, registry,
  catalog, cache, bundler, or automatic network access;
- Decision Record or a later executable artifact-specific schema;
- conformance tooling, code generation, migration, template, form, checklist,
  rubric, prompt, API, CLI, workflow, engine, scheduler, orchestrator, runtime,
  provider, product, private implementation, reference implementation,
  release, tag, hosted publication, or deployment; or
- any later architecture, schema, implementation, release, publication, or
  deployment without its own separately attributable authority.

## Activation and continuing authority boundary

EIGENAAR / Final Authority acceptance of the exact reviewed candidate is
recorded in issue comment `5218629573`. Governed integration to `main`
activates exactly Review Record Schema Version `1.0.0`. Acceptance and
activation grant no Decision Record or later schema authority and no artifact
instance, binding, validator, resolver, runtime, implementation, product,
release, publication, or deployment authority.
