# CNTX Decision Record Executable Schema Definition (ARCH-019)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed executable-schema architecture decision governed by
[issue #64](https://github.com/CNTX-PROJECT/CNTX/issues/64) and recorded by
[ADR-0019](adr/0019-decision-record-executable-schema.md).

The exact [Schema Resource](../../schemas/decision-record/1.0.0/schema.json)
and [synthetic test evidence](../../tests/schemas/decision-record/1.0.0/cases.json)
are candidates only. Creation, repository presence, validation, and transparent
non-independent review do not accept or activate Decision Record Schema Version
`1.0.0`. Only a separate attributable EIGENAAR / Final Authority acceptance and
separately governed integration can do so.

This proposal remains subordinate to Accepted architecture, Accepted
[CONTRACT-008](../contracts/decision-record-contract.md), repository governance,
and final human authority. It modifies no Accepted source and creates no
Decision Record Artifact Instance, decision authority, decision-maker identity,
approval, execution, acceptance, integration, release, deployment, publication,
or merge authority.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Decision Record
Artifact** identity, an inactive `1.0.0` target, a closed `envelope`/`payload`
root, and the exact Common Artifact Envelope dependency. Accepted
[ARCH-011](contract-definition-identity-version-binding.md) allocates the
Decision Record Contract Definition Identifier and Version. CONTRACT-008
controls Decision Record meaning, attributable decision provenance, and final
human authority.

ARCH-019 proposes one Draft 2020-12 Schema Resource that specializes only the
common-envelope constants, represents authority and all artifact relationships
through opaque exact Artifact Instance Identifier/Revision pins, and translates
only CONTRACT-008 responsibilities into a closed payload.

The resource does not allocate authority or identity, prove approval, retrieve
or interpret a source, reason about alternatives, calculate an outcome, resolve
a conflict, execute a decision, change state, or create a downstream effect.

## Proposed schema identity

| Dimension | Proposed value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Decision Record Artifact |
| Artifact token | `decision-record` |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0` |
| Candidate Schema Version | `1.0.0`, inactive |
| Canonical repository path | `schemas/decision-record/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/decision-record` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Proposed under issue #64 |

Creation, validation, review, or repository presence does not grant acceptance
or activation. No acceptance comment exists for this candidate.

## Root and common-envelope specialization

The Schema Resource evaluates one complete artifact with a closed root that
requires exactly:

1. `envelope`; and
2. `payload`.

The `envelope` composes the exact Accepted Common Artifact Envelope through one
static external reference and constrains these five values:

- Artifact Type: `decision-record`;
- Contract Definition Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/decision-record`;
- Contract Definition Version: `1.0.0`;
- Schema Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0`; and
- Schema Version: `1.0.0`.

The common resource remains independently Accepted and unchanged. All other
schema references are fragment-local. No Project Charter, Workstream, Task
Contract, Context Packet, Execution Result, Evidence Bundle, Review Record, peer
Decision Record, State Snapshot, or other artifact-specific schema is
referenced.

## Closed seventeen-property payload

The payload requires exactly these seventeen direct responsibilities:

| Property | Structural responsibility | Explicit non-effect |
| --- | --- | --- |
| `decisionAuthorityAndDecisionMaker` | One exact opaque Decision Authority pin, an opaque human decision-maker reference, non-empty authority scope, limitations, and explicit decision/preparation/review/publication/administration/execution authority boundaries. | No authority or identity allocation, resolution, credentialing, delegation, verification, amendment, or expansion. |
| `approvedRevisionAndApprovalProvenance` | Exact Decision Record pin represented as the approved revision, attributable approval references, governing-authority traceability, approval statement, and effective conditions. | No proof of self-pin equality, attribution, authority, valid approval, effectiveness, authenticity, or signature. |
| `decisionBoundaryQuestionAndOutcome` | Local decision reference, one coherent boundary, question, opaque disposition, outcome statement, and excluded or separately approvable decisions. | No universal outcome taxonomy, reasoning engine, bundled unrelated decision, or automatic effect. |
| `rationaleDecisionBasisTradeoffsAlternativesConstraintsAndRisks` | Rationale, basis references, tradeoffs, alternatives, constraints, and risks. | No scoring, confidence, ranking, weighting, optimization, recommendation generation, or truth proof. |
| `governingSourcesAndWorkBoundaryTraceability` | Non-empty closed governing-source entries plus Project Charter, Workstream, and Task Contract boundary declarations. | No retrieval, resolution, embedding, schema coupling, applicability proof, or authority transfer. |
| `artifactRelationships` | Nine exact specified-or-none opaque artifact-pin categories. | No schema reference, retrieval, referential-integrity check, lifecycle mutation, or relationship verification. |
| `evidenceReviewRecommendationsUncertaintyDissentAndHandling` | Separate evidence, review, recommendation, uncertainty, dissent, unresolved-question, and handling declarations plus an explicit input-is-not-approval statement. | No review, evidence evaluation, recommendation adoption, voting, consensus, approval, or decision. |
| `authorshipReviewApprovalDecisionEffectivePublicationAndImplementationTiming` | Seven separately named specified-or-none opaque temporal coordinates. | No date-time grammar, timestamp, clock, chronology, causal order, temporal truth, or scheduler. |
| `scopeConditionsAndTemporalApplicability` | Applicable and excluded scope, conditions, prerequisites, temporal applicability, affected audiences/environments, and non-generalization limits. | No inferred applicability, permission, transition, enforcement, or generalization. |
| `consequencesPermittedNextActionsConstraintsDependenciesAndObligations` | Consequences, permitted next actions, constraints, dependencies, obligations, and unresolved consequences. | No permission grant, execution, workflow, state change, or fulfillment proof. |
| `acceptanceIntegrationReleaseDeploymentPublicationMergeAndExecutionBoundary` | Seven specified-or-none consequential-action categories, with intended relation, exact separate-authority pin, conditions/limits, and non-automatic-effect statement. | No acceptance, integration, release, deployment, publication, merge, execution, or authorization. |
| `amendmentCorrectionRevocationAndSupersession` | Four specified-or-none exact peer Decision Record relation categories with scope, reason, affected boundary, and historical preservation. | No automatic amendment, correction, revocation, supersession, deletion, overwrite, or lifecycle transition. |
| `peerDecisionDependenciesConflictsAndAuthorizedResolution` | Specified-or-none exact peer-decision dependencies, conflicts, unresolved conflicts, and authorized-resolution references. | No latest-wins, automatic resolution, ranking, voting, majority, consensus, precedence, or conflict engine. |
| `rolesDelegationAccountabilityAndTechnicalAccessBoundary` | Authors, reviewers, evidence providers, operators, accountable decision maker, delegation-source pins, role overlap, and technical-access boundaries. | No identity or role allocation, authentication, credentialing, assignment, delegation execution, access grant, or authority inference. |
| `externalRecordAndPublicationTraceability` | Five exact specified-or-none categories for ADRs, issues, comments, pull requests, and commits. | No network retrieval, existence proof, publication, merge, update, or authority effect. |
| `securityPrivacyAccessDisclosureAndRestrictedBasis` | Security, privacy, access, confidentiality, restricted basis, disclosure, redaction-information-loss, and residual-risk declarations. | No permission, access, disclosure, redaction, sanitization, encryption, retention, archival, disposal, or enforcement mechanism. |
| `lifecycleHistoricalProvenanceAndFollowOnAuthority` | Lifecycle narrative, prior/later revision traceability, historical preservation, follow-on authority pins, non-automatic effects, and actions requiring separate authority. | No revision sequencing, state machine, workflow, transition, execution, implementation, or automatic follow-on authority. |

Every defined object is closed. Unknown payload and nested properties are
invalid. Required ordinary arrays are non-empty and unique by JSON value.
Ordinary strings require at least one non-whitespace character.

## Decision authority and approval provenance

`decisionAuthorityAndDecisionMaker.decisionAuthority` is one exact opaque
Artifact Instance Identifier/Revision pin. It records the approved source that
purports to authorize the bounded decision; it does not allocate, retrieve,
resolve, interpret, amend, broaden, or validate that authority.

The opaque decision-maker reference identifies no person through this schema
and creates no credential, role, delegation, identity assurance, or authority.
The six authority-separation statements prevent preparation, review,
publication, administration, or execution access from silently becoming
decision authority.

`approvedRevisionAndApprovalProvenance.approvedDecisionRecord` records the
Decision Record pin represented as approved. JSON Schema cannot compare it to
the common envelope pin, establish that the referenced approval exists, prove
attribution or human intent, verify authority, or make the approval effective.
Conflicting, missing, ambiguous, restricted, or unverifiable provenance
requires external governed handling and cannot be inferred away.

## Bounded decision, basis, and inputs

One local reference keeps the question, coherent boundary, opaque outcome
disposition, and outcome statement together. Excluded or separately approvable
decisions remain explicit. The schema supplies no approved vocabulary for
outcomes, status, verdict, pass/fail, severity, confidence, score, grade,
priority, weight, threshold, or implementation state.

Rationale, basis, tradeoffs, alternatives, constraints, and risks remain
separate declarative sets. Evidence, Review Records, recommendations,
uncertainty, dissent, unresolved questions, and handling remain input. Their
presence, absence, number, apparent agreement, or schema validity does not make
or approve the decision.

## Governing sources and artifact relationships

Each governing-source entry preserves a local reference, opaque source kind and
identifier, specified-or-none opaque revision, applicability statements, and
limitations. Project Charter, Workstream, and Task Contract boundaries remain
separate declarations.

`artifactRelationships` requires exactly nine categories:

1. Project Charters;
2. Workstreams;
3. Task Contracts;
4. Context Packets;
5. Execution Results;
6. Evidence Bundles;
7. Review Records;
8. peer Decision Records; and
9. State Snapshots.

Every category is an exclusive specified-or-none artifact-pin declaration. No
category embeds an artifact or references its artifact-specific schema.

## Timing, scope, consequences, and downstream actions

Authorship, review, approval, decision, effective, publication, and
implementation timing are seven independent opaque coordinates. The schema
does not define lexical formats, time zones, clocks, chronology, ordering,
causality, validity periods, or automatic activation.

Scope, exclusions, conditions, prerequisites, applicability, audiences,
environments, and non-generalization limits remain declarations. Consequences,
next actions, constraints, dependencies, obligations, and unresolved
consequences describe possible effects without granting permission or
performing work.

Acceptance, integration, release, deployment, publication, merge, and execution
are separate categories. A specified category requires an intended relation,
an exact separate-authority pin, conditions and limits, and a non-automatic-
effect statement. A Decision Record cannot authorize itself or replace the
separate authority for any listed action.

## Change, conflict, and historical preservation

Amendment, correction, revocation, and supersession remain separate exact peer
Decision Record relations. Each relation preserves its reason, scope, affected
boundary, and historical record. Nothing is silently overwritten or removed.

Dependencies, conflicts, unresolved conflicts, and authorized resolutions also
remain separate. The schema defines no latest-wins rule, hierarchy, priority,
vote, majority, consensus, ranking, conflict solver, or automatic precedence.
An authorized-resolution reference is provenance, not proof that the authority
exists or that the conflict was validly resolved.

## Roles, external records, security, privacy, and lifecycle

Role and technical-access declarations neither identify nor authorize anyone.
Technical access is not decision authority. Delegation is represented only by
opaque exact pins or assessed absence and is neither created nor validated.

ADRs, issues, comments, pull requests, and commits are opaque external records.
The schema does not retrieve, resolve, create, edit, publish, merge, or verify
them. Security, privacy, restricted-basis, disclosure, redaction-information-
loss, and residual-risk values are declarations only and implement no control.

Lifecycle narrative and revision traceability preserve history without a state
model. Follow-on authority references do not authorize follow-on work. Every
remaining consequential action continues to require its own attributable
authority and governed lifecycle.

## Declaration sets and explicit absence

Ordinary statement categories use one reusable mutually exclusive shape:

- `specified`: a closed object with `disposition: specified` and required
  non-empty unique non-blank `items`;
- `none`: a closed object with only `disposition: none`.

Opaque-value categories, artifact-pin categories, downstream-boundary
categories, peer-decision relations, and external-record categories use the
same exclusive dispositions with their own closed value or item schemas.

`none` means only assessed absence for this Artifact Revision. It does not mean
unknown, irrelevant, complete, correct, sufficient, safe, conflict-free,
authorized, approved, accepted, implemented, inaccessible, or permanently
absent.

## Lexical, collection, and reference assertions

A shared assertion requires ordinary strings to contain at least one
non-whitespace character. It performs no trimming, normalization, identity
allocation, canonicalization, or executable grammar. Required arrays are
non-empty and unique by JSON value. Array ordering assigns no chronology,
priority, authority, decision, acceptance, or workflow order.

The canonical document is one Schema Resource with one root `$schema`, one root
`$id`, fragment-local `#/$defs/` references, and exactly one external Common
Artifact Envelope `$ref`. It has no nested resource, anchor, dynamic reference,
custom vocabulary, `format`, `default`, Hyper-Schema behavior, artifact-specific
schema dependency, or public subschema API.

## Synthetic validation evidence

The non-normative test manifest defines exactly twenty ordered public-safe
cases: three valid and seventeen invalid.

The valid cases cover:

1. a minimal bounded affirmative decision with separated authority, approved-
   revision provenance, all nine relationship categories, separated timing and
   scope, and no downstream effect, change, or conflict;
2. a qualified conditional decision pinned to an Execution Result and informed
   by exact Evidence Bundle and Review Record pins, with tradeoffs, uncertainty,
   dissent, conditions, consequences, and separately authorized integration;
3. an amendment and supersession case with peer-decision conflict and
   resolution traceability, restricted basis and redaction information loss,
   distinct timing, downstream boundaries, and preserved history.

The invalid cases reject missing roots or mandatory responsibilities; unknown
properties; wrong common-envelope constants; blank or incomplete authority;
malformed approval provenance; bundled decisions; missing relationship
categories; empty rationale, source, or declaration sets; collapsed timing;
input represented as approval; malformed peer relations and latest-wins rules;
automatic downstream effects and execution engines; missing security/privacy
responsibilities; and composite null, duplicate, embedded-artifact, score,
confidence, priority, voting, majority, consensus, signature-as-approval,
workflow, runtime, and implementation shapes.

Fixtures are synthetic and non-normative. Expected validity is evidence about
structure under this exact candidate and the locally registered exact Common
Artifact Envelope resource only.

## Conformance and authority boundary

Schema validity establishes only that one JSON value satisfies this exact
candidate under the explicitly registered Common Artifact Envelope resource.
It does not establish contract conformance, source existence, source truth,
authority, human identity, approval, attribution, authenticity, integrity,
correctness, completeness, safety, privacy, outcome quality, legal effect,
implementation, acceptance, integration, release, deployment, publication,
merge, execution, or follow-on permission.

The candidate is non-self-approving. Tests, validation, review count, apparent
consensus, repository presence, Draft PR state, or tool output cannot replace
separate attributable EIGENAAR / Final Authority acceptance.

## Security and privacy boundary

The resource and fixtures contain synthetic public-safe values only. No secret,
credential, personal data, private path, production configuration, restricted
content, provider-specific assumption, product behavior, or private
implementation is introduced.

Access, confidentiality, restricted basis, disclosure, and redaction loss are
recorded as declarations. The schema grants no permission and implements no
access control, disclosure control, redaction, sanitization, encryption,
signature, verification, timestamp, trust store, retention, archival, disposal,
or chain-of-custody mechanism.

## Rejected alternatives

Rejected: open or flat roots; copied, moving, or dynamic common references;
embedded or artifact-schema-referenced governing, evidence, review, peer,
state, or downstream artifacts; implicit authority or self-approval; merged
decision, preparation, review, publication, administration, and execution
authority; bundled decisions; universal outcomes, statuses, verdicts,
pass/fail states, severity, confidence, scores, grades, priorities, weights,
thresholds, signatures-as-approval, voting, majority, consensus, ranking,
latest-wins, or implementation taxonomies; automatic retrieval, reasoning,
recommendation, decision, approval, conflict resolution, state transition,
integration, publication, release, deployment, merge, execution, workflow, or
runtime behavior; network-dependent resolution; null or fabricated absence;
canonical JSON assumptions; and schema validity as acceptance.

## Validation requirements

The governed candidate requires strict duplicate-free JSON and UTF-8 checks,
official Draft 2020-12 schema checking, isolated `jsonschema 4.25.1`, exact
offline registration of the Common Artifact Envelope, required missing-resource
failure, all twenty expected fixture outcomes, exact root/constants/seventeen-
property payload, authority-separation, self-pin, relationship, timing,
downstream, change, external-record, declaration, closure, lexical, collection,
and reference-graph assertions, thirty-two protected-blob checks, link and
privacy/security scans, exact eight-path scope, exact one-commit state, GitHub
read-back, and one transparent non-independent exact-head COMMENT review.

## Activation gate and continuing stop

ARCH-019 remains Proposed. The approved creation workflow stops after the
transparent non-independent exact-head COMMENT review. A separate attributable
EIGENAAR / Final Authority acceptance is required before any status promotion,
promotion commit, Ready-for-review transition, merge, issue closure, activation,
or branch cleanup may be considered.

No inference from upstream acceptance, a passing schema, the candidate commit,
the Draft PR, or the review can cross that gate.

## Deferred and unauthorized scope

Deferred and unauthorized: Decision Record Artifact Instances; Artifact
Instance Identifier generation or Artifact Revision sequencing; authority,
decision-maker, identity, credential, delegation, approval, signature,
verification, trust, timestamp, digest, encoding, canonicalization, encryption,
retrieval, resolver, registry, catalog, cache, bundler, network access,
reasoning, recommendation, scoring, voting, consensus, conflict resolution,
state, lifecycle, workflow, integration, publication, release, deployment,
merge, execution, access-control, disclosure, redaction, sanitization,
retention, archival, disposal, or chain-of-custody mechanisms; State Snapshot
or later artifact-specific executable schemas; artifact Serialization Binding;
canonical artifact JSON; Extension Module/Profile mechanisms; validator or
validation-output implementations; conformance tooling; code generation;
migration; templates; forms; checklists; rubrics; prompts; APIs; CLIs; engines;
schedulers; orchestrators; runtime-, provider-, or product work; private or
reference implementation; release; tag; hosted publication; or deployment.

## Authoritative sources

- [Issue #64](https://github.com/CNTX-PROJECT/CNTX/issues/64)
- [CONTRACT-008 Decision Record](../contracts/decision-record-contract.md)
- [Artifact-specific schema family and container boundary](artifact-specific-schema-family-container-boundary.md)
- [Contract Definition identity/version binding](contract-definition-identity-version-binding.md)
- [Common Artifact Envelope Schema Version 1.0.0](../../schemas/common-artifact-envelope/1.0.0/schema.json)
- [ADR-0019](adr/0019-decision-record-executable-schema.md)
- [Proposed Decision Record Schema Version 1.0.0](../../schemas/decision-record/1.0.0/schema.json)
- [Non-normative synthetic cases](../../tests/schemas/decision-record/1.0.0/cases.json)
