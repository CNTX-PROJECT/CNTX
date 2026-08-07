# CNTX Execution Result Executable Schema Definition (ARCH-016)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed executable-schema architecture candidate governed
by [issue #58](https://github.com/CNTX-PROJECT/CNTX/issues/58) and recorded by
[ADR-0016](adr/0016-execution-result-executable-schema.md). Owner / Final
Authority creation authority is recorded in issue comment `5216946200`.

The accompanying [Schema Resource](../../schemas/execution-result/1.0.0/schema.json)
and [synthetic test evidence](../../tests/schemas/execution-result/1.0.0/cases.json)
are Proposed and inactive. Candidate creation, validation, Draft publication,
or transparent non-independent review grants no acceptance. Separate Owner /
Final Authority acceptance of the exact reviewed candidate is required before
any status promotion or integration.

This candidate remains subordinate to Accepted architecture, Accepted
[CONTRACT-005](../contracts/execution-result-contract.md), repository
governance, and final human authority. It modifies no Accepted source and
creates no Execution Result Artifact Instance, task authority, correctness or
completion decision, acceptance, integration, release, deployment, or merge
authority.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Execution Result
Artifact** identity, an inactive `1.0.0` target, a closed
`envelope`/`payload` root, and the exact Common Artifact Envelope dependency.
Accepted [ARCH-011](contract-definition-identity-version-binding.md) allocates
the Execution Result Contract Definition Identifier and Version. CONTRACT-005
controls Execution Result meaning and authority boundaries.

Proposed ARCH-016 binds one Draft 2020-12 Schema Resource that specializes
only the common-envelope constants, represents the governing Task Contract
through one opaque Artifact Instance/Revision pin, represents used Context
Packets through an explicit opaque-pin declaration, and translates only
CONTRACT-005 responsibilities into a closed payload.

This is structural evaluation, not semantic proof. Validity cannot establish
that work was authorized, performed, correct, complete, contract-conformant,
accepted, integrated, released, deployed, or permitted to merge.

## Governing traceability

| Governing source | Constraint preserved |
| --- | --- |
| [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), and [ARCH-003](artifact-contract-schema-architecture.md) | Final human authority, separate identity/version dimensions, layering, evidence limits, and public/private separation remain unchanged. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) and the [Accepted common schema](../../schemas/common-artifact-envelope/1.0.0/schema.json) | The complete common envelope remains independently governed and is referenced once at its exact root identity. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) | The Execution Result logical identity, independent version line, closed artifact root, payload ownership, and rollout order remain controlling. |
| [ARCH-011](contract-definition-identity-version-binding.md) | The exact Execution Result Contract Definition Identifier `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/execution-result` and Version `1.0.0` are used. |
| [ARCH-012](project-charter-executable-schema.md), [ARCH-013](workstream-executable-schema.md), [ARCH-014](task-contract-executable-schema.md), and [ARCH-015](context-packet-executable-schema.md) | Accepted resources remain unchanged and are not referenced by this schema. |
| [CONTRACT-005](../contracts/execution-result-contract.md) | Only Accepted governing-pin, output, action/side-effect, resource, provenance, validation/check, criteria-assessment, uncertainty, limitation/failure/deviation, stop/escalation, unperformed-work, security/privacy, and traceability responsibilities become structure. |
| [Issue #58](https://github.com/CNTX-PROJECT/CNTX/issues/58) | Exact baseline, eight-path scope, validation, transparent review, stop gate, and prohibited actions remain binding. |

## Exact resource identity and version

| Dimension | Proposed value |
| --- | --- |
| Logical Schema Identity | CNTX Public Core Schema Family / Execution Result Artifact |
| Schema language | JSON Schema |
| Dialect | Draft 2020-12 |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/execution-result/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Proposed under issue #58 |

The `$id` is the stable identity of this proposed exact Schema Version. Its
HTTPS form neither requires nor authorizes network access. It is not a branch,
tag, release, resolver mapping, registry entry, hosted-publication guarantee,
Serialization Binding, trust marker, or authority source.

Schema Version, Contract Definition Version, Artifact Instance Identifier,
Artifact Revision, Document Status, approval state, Content Digest, Provenance
Reference, implementation, release, and deployment remain distinct.

## Complete artifact root

The resource evaluates one complete Execution Result Artifact Instance in the
JSON-compatible instance model. The root is closed and has exactly two
required direct members: `envelope` and `payload`. It cannot be flattened,
opened, extended by an unknown root property, or used to treat either member
alone as a complete Execution Result.

## Common Artifact Envelope specialization

`/envelope` uses exactly one static external reference:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

A local overlay constrains only these constants:

| Envelope coordinate | Exact constant |
| --- | --- |
| `artifactType` | `execution-result` |
| `governingContract.identifier` | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/execution-result` |
| `governingContract.version` | `1.0.0` |
| `governingSchema.identifier` | `https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0` |
| `governingSchema.version` | `1.0.0` |

The overlay does not copy, weaken, open, or redefine the common resource. The
common schema retains ownership of artifact identity, governing coordinates,
provenance references, digest evidence, lexical assertions, and envelope
closure.

## Governing Task Contract and Context Packet boundary

`governingTaskContract` is mandatory and contains exactly two required
non-blank opaque strings: `artifactInstanceIdentifier` and
`artifactRevision`. The schema does not allocate either value, retrieve or
resolve the Task Contract, embed or validate it, or prove existence,
applicability, approval, currency, completeness, or authority.

`contextPacketsUsed` explicitly declares either one or more unique closed
Context Packet Artifact Instance/Revision pins or assessed `none`. The schema
does not retrieve, resolve, embed, or validate a Context Packet and proves no
relevance, sufficiency, minimality, correctness, freshness, accessibility,
authority, or disclosure permission.

The resource contains no `$ref` to Project Charter, Workstream, Task Contract,
Context Packet, peer Execution Result, Evidence Bundle, Review Record, Decision
Record, State Snapshot, or any other artifact-specific schema.

## Closed payload model

The payload contains exactly fourteen required direct properties:

| Property | Structural responsibility | Explicit non-meaning |
| --- | --- | --- |
| `governingTaskContract` | Opaque governing Task Contract Artifact Instance/Revision pin. | No retrieval, embedded contract, schema dependency, approval, or authority proof. |
| `contextPacketsUsed` | Explicit specified opaque Context Packet pins or assessed absence. | No retrieval, relevance/sufficiency proof, source authority, or schema dependency. |
| `claimedOutput` | Bounded summary, output claims, and produced-resource declarations. | No correctness, completeness, acceptance, integration, release, deployment, or merge proof. |
| `actionsAndSideEffects` | Performed-action, side-effect, and action-limitation declarations. | No action execution, effect discovery, complete observation, or mutation authority. |
| `accessedAndChangedResources` | Accessed, changed, and resource-limitation declarations. | No path language, access grant, repository semantics, mutation, or exhaustive inventory. |
| `provenanceAndRevisionContext` | Provenance entries, revision context, representation treatments, uncertainty/limitations, and claim traceability. | No retrieval, authenticity, fidelity, canonicalization, or provenance-truth proof. |
| `validationAndCheckClaims` | Assessed absence or bounded check claims with claimed outcomes and limitations. | No validator implementation/output contract, final determination, approval, or automation. |
| `acceptanceCriteriaAssessment` | Non-empty bounded criteria claims with evidence and limitations. | No exhaustive criteria mapping, correctness, satisfaction decision, or acceptance. |
| `assumptionsDependenciesAndUncertainty` | Assumption, dependency, uncertainty, conflict, missing-context, and apparent-authority-conflict declarations. | No automatic resolution or fallback authority. |
| `limitationsFailuresAndDeviations` | Limitation, failure, deviation, rationale, and unresolved-impact declarations. | No Task Contract amendment, deviation permission, or consequence resolution. |
| `stopsAndEscalations` | Stop, escalation, and unresolved-condition declarations. | No notification, queue, state, approval, scheduler, workflow, or orchestrator. |
| `unperformedWork` | Deliberately unperformed work and reason/consequence declarations. | No completeness proof, backlog, task transfer, or follow-on authority. |
| `securityPrivacyAndDisclosure` | Security/privacy observations, restricted references, disclosure limits, and residual risks. | No access control, disclosure permission, redaction, encryption, enforcement, or adequacy proof. |
| `evidenceReviewDecisionAndLifecycleTraceability` | Opaque evidence, review, decision, peer-result, supersession/retention, and lifecycle-context declarations. | No embedded downstream artifact, approval, lifecycle vocabulary, state machine, workflow, or final authority. |

Every defined object is closed. Unknown payload and nested properties are
invalid. Required ordinary arrays are non-empty and unique by JSON value.
Ordinary strings are non-blank.

## Provenance-entry model

`provenanceEntries` is required, non-empty, and unique by JSON value. Each
closed entry requires exactly:

1. `sourceReference`;
2. `sourceType`;
3. `revisionOrVersionContext`;
4. `contentTreatments`; and
5. `resultingUncertaintyAndLimitations`.

Source references are opaque and have no URI, repository, path, registry,
resolver, retrieval, access, authenticity, or authority semantics.

`contentTreatments` is non-empty and unique, with only `direct`, `summarized`,
`extracted`, `transformed`, and `unavailable`. Tokens describe representation
only and activate no algorithm or permission.

## Check and acceptance-criteria claims

A specified check claim contains exactly `checkReference`, `claimedOutcome`,
and `evidenceAndLimitations`. Claimed outcomes are limited to `passed`,
`failed`, `inconclusive`, and `not-performed`.

Every acceptance-criteria assessment contains exactly `criterionReference`,
`claimedAssessment`, and `evidenceAndLimitations`. Claimed assessments are
limited to `satisfied`, `not-satisfied`, `partially-satisfied`, and
`not-assessed`.

These tokens are evidentiary claims, not approval states, validator-output
standards, final determinations, lifecycle states, or automation triggers.
Schema validity cannot establish that every governing criterion was included
or interpreted correctly.

## Declaration sets and explicit absence

One internal statement declaration-set shape is reused wherever a category may
be empty but must be assessed:

- `specified`: a closed object with `disposition: specified` and required
  non-empty unique non-blank `items`;
- `none`: a closed object with only `disposition: none`.

Artifact-pin and check-claim declarations use the same mutually exclusive
dispositions with their own closed item schemas.

`none` means only assessed for this Artifact Revision with no item declared.
It does not mean unknown, irrelevant, approved, complete, correct, satisfied,
successful, safe, risk-free, authorized, inaccessible, or permanently absent.

## Lexical, collection, and reference assertions

A shared assertion requires ordinary strings to contain at least one
non-whitespace character. It performs no trimming or Unicode normalization and
assigns no executable grammar. Required arrays are non-empty and unique by JSON
value; ordering assigns no chronology, priority, authority, execution,
retrieval, review, decision, acceptance, or workflow order.

The canonical document is one Schema Resource with one root `$schema`, one
root `$id`, internal fragment-local `#/$defs/` references, and exactly one
external common-envelope `$ref`. It has no nested resource, anchor, dynamic
reference, custom vocabulary, `format`, `default`, Hyper-Schema behavior,
artifact-specific schema dependency, or public subschema API.

## Evidentiary and non-self-approving boundary

An Execution Result records bounded claims about output and limitations. It
cannot modify, broaden, replace, or reinterpret its governing Task Contract;
replace authoritative Project Charter, Workstream, Task Contract, or Context
Packet sources; or silently transfer claims, context, or authority between
tasks.

Completion, criteria satisfaction, tests, validation, review, schema validity,
or a conformance claim are evidence for an applicable authorized human
decision, not that decision. Existence, possession, storage, receipt, schema
validity, digest evidence, or implementer capability grants no authority.

## Conformance and validation boundary

Conformance to this schema means only that one instance satisfies the
structural assertions of the exact Schema Version under the required common
resource mapping. It proves no CONTRACT-005 semantic conformance, source or
claim truth, correctness, completeness, authorization, acceptance-criteria
satisfaction, acceptance, integration, release, deployment, or merge
permission.

Processors must receive the exact common resource locally. The canonical
identifier is not permission for automatic network retrieval. Validation
failure without the registered common resource is required evidence that the
dependency is explicit rather than silently fetched.

## Synthetic test evidence

The [test manifest](../../tests/schemas/execution-result/1.0.0/cases.json)
contains exactly twenty ordered public-safe synthetic cases: three valid and
seventeen invalid. Coverage includes the root, common-envelope constants,
opaque Task Contract and Context Packet pins, all fourteen responsibilities,
provenance/treatment rules, check and criteria claims, declarations, lexical
and collection rules, closure, and forbidden executable or embedded-artifact
shapes.

Fixtures are non-normative structural evidence. They are not canonical
Execution Results, Approved Task Contracts, Context Packets, actual execution
evidence, acceptance determinations, templates, forms, prompts, workflows,
Serialization Bindings, conformance claims, reference implementations,
releases, or deployments.

## Security and privacy

The schema can record security, privacy, disclosure, and residual-risk claims
but cannot determine whether they are adequate or followed. Public fixtures
use only synthetic content. Secrets, credentials, personal data, production
configuration, private paths, restricted content, and private implementation
details remain outside this public resource.

## Consequences and tradeoffs

- A complete Execution Result becomes structurally evaluable only after separate
  acceptance and integration.
- All fourteen CONTRACT-005 responsibility groups are explicit and closed.
- Opaque artifact and source references preserve technology neutrality but
  require semantic human review.
- Explicit absence avoids fabricated placeholders but is more verbose.
- Claimed check and criteria vocabularies support bounded evidence without
  creating approval or validator-output protocols.
- Static schema composition supports offline deterministic validation while
  requiring callers to supply the common resource.
- Structural rigor cannot prove correctness, completeness, authority,
  acceptance, integration, release, deployment, or merge permission.

## Rejected alternatives

Rejected alternatives include an open or flat root; copied or dynamic common
schema content; embedded or schema-referenced governing, context, peer,
evidence, review, decision, state, or downstream artifacts; unrestricted logs;
automatic execution, resource discovery, validation, criteria satisfaction,
approval, conflict resolution, evidence/review/decision creation, state
machines, workflows, runtime/provider fields, unknown properties, null or
fabricated `N/A`, mandatory network resolution, canonical JSON assumptions,
and validation or review as acceptance.

## Deferred and explicitly unauthorized scope

This candidate defines no Artifact Instance, identifier generation, revision
sequencing, artifact-specific schema dependency, execution or mutation,
resource access, validator implementation/output contract, criteria engine,
approval/acceptance mechanism, lifecycle or workflow, digest method,
canonicalization, signature, verification, trust store, Serialization Binding,
canonical JSON, resolver, registry, cache, bundler, network access,
conformance tool, code generator, migration, template, form, prompt, API, CLI,
scheduler, orchestrator, runtime, implementation, product, release, tag,
hosted publication, or deployment.

## Continuing gate

Candidate creation, validation, Draft publication, and exact-head COMMENT
review do not grant acceptance. Separate Owner / Final Authority acceptance of
the exact reviewed head is required before status promotion, Ready transition,
merge, completion, issue closure, activation, or public branch cleanup.

No Evidence Bundle or other follow-on Schema Resource is automatically
authorized by this candidate.
