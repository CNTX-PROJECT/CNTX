# CNTX Validation Evidence and Reproduction Package Identity, Version, and JSON Representation (ARCH-035)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only architecture decision governed
by [issue #116](https://github.com/CNTX-PROJECT/CNTX/issues/116).
Attributable EIGENAAR / Final Authority acceptance of the exact issue/task
contract is recorded in issue comment
[`5241232823`](https://github.com/CNTX-PROJECT/CNTX/issues/116#issuecomment-5241232823).
Exact-head acceptance of reviewed candidate commit
`90d660b116288f8bb7c99152fec16022178fa8d8` and tree
`a34fe286546f84839647b203970ff908e3aec2d9` is recorded in issue comment
[`5241789812`](https://github.com/CNTX-PROJECT/CNTX/issues/116#issuecomment-5241789812)
after transparent non-independent ARCHITECT COMMENT review `4897646170`.

This candidate is prepared on public baseline commit
`e46ae6f03205d1ccff364ce2ed82847a155afb2b` and tree
`7b7dce3809205e2c6095f4f8f1509fe6c972a363`.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
express permission. These terms express requirement strength only within this
Accepted decision and grant no authority.

## Purpose and decision boundary

Accepted ARCH-034 defines one concrete Validation Execution Record identity,
version, and JSON representation. It preserves exact validation subjects,
governing and evaluator context, eight phase results, diagnostics, limitations,
claims, and human-authority boundaries. It deliberately does not define a
concrete evidence or reproduction package.

Accepted ARCH-025 defines Portable Conformance Evidence responsibilities but
creates no concrete evidence identity or representation. Accepted CONTRACT-006
defines the Evidence Bundle as a canonical Evidentiary Artifact Type, but that
artifact remains distinct from validation-layer output and reproduction
material. Accepted ARCH-033 requires concrete output and evidence identities
before any concrete Tool or Implementation contract.

This decision therefore defines exactly one concrete, non-Artifact
Validation-layer package for bounded evidence and reproduction material that
may support, qualify, contradict, or leave unverifiable one or more exact
Validation Execution Record claims.

The package records declarations and supplied material. It does not collect,
retrieve, validate, execute, reproduce, assess, review, decide, accept, certify,
release, publish, host, or deploy anything by itself.

## Governing traceability

This candidate is subordinate to all Accepted predecessors. In particular:

| Governing source | Preserved responsibility |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Bounded collaboration, evidence visibility, non-authority, and human final authority remain controlling. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Definition, representation, instance, revision, provenance, location, digest, lifecycle, acceptance, and authority remain separate. |
| [CONTRACT-006](../contracts/evidence-bundle-contract.md) | The canonical Evidence Bundle remains a distinct Evidentiary Artifact Type and is not replaced by this package. |
| [ARCH-022](core-artifact-serialization-binding.md) and [ADR-0022](adr/0022-core-artifact-serialization-binding.md) | Core Artifact JSON remains separate; this non-Artifact representation does not use the Common Artifact Envelope. |
| [ARCH-023](schema-resource-resolution-catalog-boundary.md) and [ADR-0023](adr/0023-schema-resource-resolution-catalog-boundary.md) | Exact caller-supplied resource closure, offline-first resolution, and fail-closed ambiguity remain controlling. |
| [ARCH-024](validation-and-validation-output-contract.md) and [ADR-0024](adr/0024-validation-and-validation-output-contract.md) | Validation phases, separate outcomes, diagnostics, limitations, output, and non-authority remain controlling. |
| [ARCH-025](portable-conformance-evidence-boundary.md) and [ADR-0025](adr/0025-portable-conformance-evidence-boundary.md) | Portable Conformance Evidence, claim sufficiency, portability, and independent reassessment remain separate later concerns. |
| [ARCH-033](extension-module-profile-tooling-implementation-boundary.md) and [ADR-0033](adr/0033-extension-module-profile-tooling-implementation-boundary.md) | Tool, Implementation, capability, configuration, dependency, environment, output, evidence, conformance, release, deployment, and authority remain separate. |
| [ARCH-034](validation-execution-record.md) and [ADR-0034](adr/0034-validation-execution-record.md) | The exact Validation Execution Record identity, version, phases, outcomes, references, and authority boundary remain unchanged. |

All Accepted Contract Definitions, Schema Resources, synthetic test manifests,
Core Artifact JSON Binding Version `1.0.0`, release history, settings evidence,
and historical Git/GitHub objects remain unchanged.

## Terminology

| Term | Meaning here | Does not imply |
| --- | --- | --- |
| **Evidence and Reproduction Package** | One immutable revision of a bounded validation-layer package represented under this decision. | Evidence Bundle, Portable Conformance Evidence, proof, acceptance, certification, release evidence, or authority. |
| **Package Definition** | The versioned normative meaning assigned here to the package. | Artifact Type, executable schema, Tool, Implementation, or package instance. |
| **Package Identifier** | Stable identity of one package lineage. | Definition identity, revision, location, authenticity, acceptance, or priority. |
| **Package Revision** | Exact immutable revision in one package lineage. | Recency, precedence, correction, currentness, acceptance, or replacement. |
| **Subject** | One exactly pinned object, record, source, resource, output, or other bounded item to which evidence or reproduction material relates. | Truth, applicability, acceptance, or conformance. |
| **Evidence Item** | One bounded supplied or declared evidence unit with exact local identity, source, observation, provenance, relations, and limitations. | Support, sufficiency, independence, authenticity, or correctness. |
| **Reproduction Procedure** | One ordered bounded description of inputs, preconditions, steps, observations, differences, and limits. | Instruction to execute, successful reproduction, equivalence, certification, or authority. |
| **Output Reference** | One package-local declaration of produced or supplied output bytes or location. | Canonical Validation Output, Artifact Instance, evidence sufficiency, or publication. |
| **Condition Object** | An explicit structured absence, ambiguity, conflict, restriction, unsupported state, non-assessment, or non-execution declaration. | Value, default, waiver, repair, success, or permission to continue. |

## Allocated logical identities and initial versions

Governed integration of this Accepted decision allocates and activates exactly
these pairs:

| Dimension | Exact value |
| --- | --- |
| Validation Evidence and Reproduction Package Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/definitions/validation-evidence-reproduction-package` |
| Validation Evidence and Reproduction Package Definition Version | `1.0.0` |
| Validation Evidence and Reproduction Package JSON Representation Identifier | `https://github.com/CNTX-PROJECT/CNTX/bindings/validation-evidence-reproduction-package-json` |
| Validation Evidence and Reproduction Package JSON Representation Version | `1.0.0` |

The HTTPS-shaped identifiers are identities, not retrieval authority. They do
not authorize network access, redirects, discovery, hosted content, or trust in
content returned from a similar location.

Definition Identity, Definition Version, Representation Identity,
Representation Version, Package Identifier, Package Revision, location,
provenance, digest, lifecycle, review, decision, acceptance, publication, and
authority MUST remain separate dimensions.

This candidate assigns no media type, filename, extension, repository location
for package instances, schema `$id`, Schema Version, registry, transport,
storage location, retention system, publication channel, Tool, Implementation,
runtime, dependency, or interface.

## Package classification

A Validation Evidence and Reproduction Package is a **Validation-layer
package**. It is not a new CNTX Artifact Type and MUST NOT use or extend the
closed nine-value `artifactType` enumeration in the Common Artifact Envelope.

It is not governed as a Project Charter, Workstream, Task Contract, Context
Packet, Execution Result, Evidence Bundle, Review Record, Decision Record, or
State Snapshot. It MUST NOT use the Common Artifact Envelope.

A later Evidence Bundle MAY reference an exact Package Identifier and Revision
under a separately governed representation or mapping. That reference does not
make this package an Evidence Bundle and proves no evidence relevance,
sufficiency, independence, acceptance, or authority.

## JSON document boundary

Representation Version `1.0.0` is exactly one JSON text containing exactly one
root JSON object.

The representation MUST:

- use strict UTF-8;
- contain no byte-order mark;
- contain no duplicate object member names at any depth;
- contain no comments, non-JSON values, or trailing non-whitespace bytes;
- preserve supplied strings and numbers without coercion, repair, defaulting,
  normalization, substitution, or silent fallback;
- use exact case-sensitive property names and tokens defined here;
- reject unknown properties in every closed object defined here; and
- treat array order as meaningful only where this decision explicitly defines
  order.

Parsing success proves only that a JSON value is available. Representation
success proves only this representation dimension. Neither proves source
existence, authenticity, evidence support, evidence sufficiency,
reproducibility, executable-schema conformance, normative-contract conformance,
Artifact Instance conformance, review, acceptance, security/privacy, release,
or deployment fitness.

## Closed root object

The root object contains exactly these twelve required properties and no
others:

| Property | Responsibility |
| --- | --- |
| `package` | Definition, representation, Package Identifier, Package Revision, lifecycle, producer, production time, and package digest. |
| `subjects` | Exact bounded subjects and supplied-representation coordinates. |
| `governingInputs` | Exact frozen governing-source, Definition, resource, authority, and claim-scope inputs. |
| `evaluatorContext` | Supplied evaluator, Tool, Implementation, runtime, dependency, configuration, capability, environment, limit, and network declarations. |
| `executionRecords` | Exact referenced Validation Execution Record coordinates and package-local aliases. |
| `evidenceItems` | Bounded direct, derived, supporting, qualifying, contradictory, missing, unavailable, restricted, or other evidence declarations. |
| `reproductionProcedures` | Ordered bounded reproduction descriptions, observations, differences, cleanup, and non-execution. |
| `outputs` | Exact supplied or produced output references, digests, provenance, and limitations. |
| `diagnostics` | Zero or more separately identified bounded package diagnostics. |
| `limitations` | Zero or more separately identified material package limitations. |
| `claimBoundary` | Exact claimed and explicitly unclaimed dimensions, exclusions, and evidence/limitation relations. |
| `authorityBoundary` | Producer, assembler, executor, reviewer, decision-maker, automatic-authority prohibition, and final-human-authority boundary. |

All twelve properties remain required even when no execution or reproduction
was attempted. Missing information MUST use an applicable explicit condition;
it MUST NOT be omitted, guessed, defaulted, fabricated, or represented as a
successful observation.

## Common scalar, timestamp, digest, and reference rules

Unless an exact token or format is defined below:

- a string MUST contain at least one non-whitespace Unicode code point;
- an identifier or reference is an opaque case-sensitive string;
- a reference MUST NOT be treated as a path, URL, retrieval instruction,
  mutable alias, or authenticity proof merely because of its spelling;
- arrays declared unique MUST contain no duplicate JSON string values;
- arrays MAY be empty only where the responsible object explicitly permits an
  assessed empty set; and
- an object is closed and contains exactly the properties listed for it.

UTC timestamps use RFC 3339 `date-time` form with an uppercase `Z`. A timestamp
records only a supplied or observed coordinate. It proves no freshness,
ordering, authority, authenticity, or trusted-clock property.

Where Representation Version `1.0.0` requires a digest, the closed digest
object contains exactly `method`, `value`, and `coveredBytes`. `method` is
exactly `sha-256`; `value` is exactly 64 lowercase hexadecimal characters;
`coveredBytes` states the exact byte sequence or supplied object whose bytes
were digested. A digest proves no truth, authenticity, provenance, acceptance,
or authority.

## Explicit condition object

Where a property permits a condition instead of a value, the condition object
contains exactly:

- `condition`;
- `reason`; and
- `provenanceReferences`.

`condition` is exactly one of:

- `not-applicable`;
- `missing`;
- `unavailable`;
- `ambiguous`;
- `conflicting`;
- `unsupported`;
- `restricted`;
- `not-defined`;
- `not-assessed`; or
- `not-executed`.

`reason` is non-blank. `provenanceReferences` is a unique array and MAY be
empty only when the reason states why no reliable provenance is available. A
condition is not `null`, an empty placeholder, a value, a default, a waiver, a
repair, a success, or permission to continue. It MUST be linked to applicable
diagnostics, limitations, reproduction outcomes, and claim boundaries.

## `package` object

The closed `package` object contains exactly:

| Property | Requirement |
| --- | --- |
| `definitionIdentifier` | Exact proposed Package Definition Identifier. |
| `definitionVersion` | Exact token `1.0.0`. |
| `representationIdentifier` | Exact proposed JSON Representation Identifier. |
| `representationVersion` | Exact token `1.0.0`. |
| `packageIdentifier` | Stable identity of one package lineage. |
| `packageRevision` | Exact immutable revision of this package. |
| `lifecycleState` | Exactly `produced`, `corrected`, `superseded`, or `withdrawn`. |
| `previousRevision` | Exact previous Package Revision or an explicit first-revision declaration. |
| `producerReference` | Exact attributable producer reference. |
| `assemblerReference` | Exact attributable package-assembler reference. |
| `producedAt` | Required UTC timestamp. |
| `packageDigest` | Required SHA-256 digest over the exact declared package bytes, or a condition explaining why bytes are not yet available. |

`previousRevision` contains exactly `disposition` and `valueOrReason`.
`disposition` is exactly `specified` or `first-revision`. `specified` requires
the exact previous Package Revision; `first-revision` requires an explanation
that this is the first supplied revision in the lineage.

Correction, supersession, or withdrawal creates a new immutable Package
Revision. It MUST NOT overwrite, delete, or silently reinterpret an earlier
revision. Lifecycle state does not imply acceptance, currentness, precedence,
authority, or replacement outside an exact supplied lineage and governing
decision.

## `subjects` array

`subjects` is a non-empty array. Every closed subject object contains exactly:

- `subjectReference`;
- `subjectKind`;
- `identity`;
- `versionOrRevision`;
- `representationDigest`;
- `scope`;
- `exclusions`; and
- `provenanceReferences`.

`subjectReference` is package-local and unique. `subjectKind` is exactly one
of `validation-execution-record`, `raw-evaluator-output`, `governing-input`,
`schema-resource`, `reproduction-subject`, or `other`.

`identity`, `versionOrRevision`, and `representationDigest` contain exact
values or explicit conditions. `scope` is non-blank. `exclusions` is a unique
non-empty array of explicit exclusions or one assessed-absence statement.
`provenanceReferences` is non-empty unless an explicit condition proves why
reliable provenance is unavailable.

At least one subject has `subjectKind: validation-execution-record` and must
correspond to an entry in `executionRecords`. The package MUST NOT infer subject
identity or revision from a path, filename, branch, tag, registry, cache,
network location, display name, or object order.

## `governingInputs` object

The closed `governingInputs` object contains exactly:

- `contextIdentifier`;
- `contextRevision`;
- `contextDigest`;
- `frozenAt`;
- `inputs`;
- `resourceClosure`;
- `authorityReferences`;
- `claimScopeReference`;
- `provenanceReferences`; and
- `limitations`.

Each closed `inputs` entry contains exactly:

- `inputReference`;
- `dimension`;
- `disposition`;
- `identity`;
- `versionOrRevision`;
- `digestOrCondition`;
- `sourceReference`;
- `provenanceReferences`; and
- `limitations`.

`inputReference` is unique. `dimension` is exactly one of:

- `repository`;
- `architecture-source`;
- `adr-source`;
- `contract-definition`;
- `accepted-contract-source`;
- `serialization-binding`;
- `definition`;
- `schema-resource`;
- `resource-closure`;
- `activation-context`;
- `declaration-set`;
- `validation-execution-record`;
- `task-authority`; or
- `claim-scope`.

`disposition` is exactly `supplied`, `not-applicable`, `missing`, `ambiguous`,
`conflicting`, `unavailable`, `unsupported`, or `restricted`. Only `supplied`
permits positive use of the declared identity, revision, digest, source, and
provenance. Another disposition requires explicit conditions and visible
claim impact.

The closed `resourceClosure` object contains exactly `entryResourceReferences`,
`resourceReferences`, `staticReferenceEdges`, `unresolvedReferences`,
`closureDigest`, and `limitations`. Resource and edge references are unique.
The closure is caller-supplied and finite. This package neither resolves nor
retrieves it.

The governing context remains unchanged for the package revision. Any material
change to source, revision, content, provenance, resource closure, authority,
or claim scope requires a new context revision and Package Revision.

## `evaluatorContext` object

The closed `evaluatorContext` object contains exactly:

- `evaluatorReference`;
- `evaluatorClass`;
- `tool`;
- `implementation`;
- `runtime`;
- `dependencies`;
- `configuration`;
- `capabilities`;
- `unsupportedCapabilities`;
- `environment`;
- `resourceLimits`;
- `network`; and
- `provenanceReferences`.

`evaluatorClass` is exactly `human`, `model`, `tool`, `implementation`,
`pipeline`, or `other`. This token classifies a supplied declaration and
allocates no canonical role, Tool, Implementation, provider, or authority.

The closed `tool`, `implementation`, and `runtime` objects each contain exactly
`disposition`, `identity`, `version`, `configurationReference`, and
`provenanceReferences`. `disposition` is `specified` or `not-defined`.
`specified` requires exact caller-supplied identity and version. `not-defined`
requires explicit conditions and MUST NOT be replaced by product, model,
provider, language, filename, executable, package-manager, or registry guesses.

Every dependency object contains exactly `dependencyReference`, `identity`,
`version`, `source`, `digestOrCondition`, `purpose`, and
`provenanceReferences`. Dependency references are unique. Absence of a complete
dependency set is a visible limitation; it is not an empty assessed set unless
that assertion has exact provenance.

`capabilities` and `unsupportedCapabilities` are separate unique arrays.
Configuration, environment, and resource limits are caller-supplied closed
declarations. They do not prove enforcement or completeness.

The closed `network` object contains exactly `declaredMode`,
`observedNetworkUse`, `observationMethod`, `limitations`, and
`provenanceReferences`. `declaredMode` is exactly `prohibited`.
`observedNetworkUse` is exactly `none-observed`, `observed`, `unverifiable`, or
`not-assessed`. `none-observed` proves only the bounded observation method and
interval; it is not universal proof that no network activity occurred.

## `executionRecords` array

`executionRecords` is non-empty. Every closed entry contains exactly:

- `executionRecordReference`;
- `definitionIdentifier`;
- `definitionVersion`;
- `representationIdentifier`;
- `representationVersion`;
- `recordIdentifier`;
- `recordRevision`;
- `recordDigest`;
- `locationOrCondition`;
- `phaseOutcomeSummary`;
- `provenanceReferences`; and
- `limitations`.

`executionRecordReference` is package-local and unique. The Definition and
Representation identifiers and versions MUST match exact supplied values; use
of the ARCH-034 `1.0.0` pair is explicit rather than inferred.

`phaseOutcomeSummary` contains exactly eight entries in ARCH-034 order. Every
entry contains exactly `phase`, `outcome`, and `recordPhaseReference` and uses
the exact ARCH-034 phase and outcome tokens. The summary is a supplied index;
it cannot replace or silently correct the referenced Validation Execution
Record. A mismatch is adverse evidence and a package diagnostic.

## `evidenceItems` array

Every closed evidence-item object contains exactly:

- `evidenceReference`;
- `category`;
- `relationship`;
- `subjectReferences`;
- `executionRecordReferences`;
- `phaseReferences`;
- `claimReferences`;
- `sourceReference`;
- `sourceRevisionOrCondition`;
- `sourceDigestOrCondition`;
- `observationContext`;
- `expectedObservation`;
- `actualObservation`;
- `transformation`;
- `integrity`;
- `uncertainty`;
- `limitationReferences`;
- `restrictedContent`;
- `provenanceReferences`; and
- `observedAtOrCondition`.

`evidenceReference` is package-local and unique. `category` is exactly one of:

- `direct-observation`;
- `measurement`;
- `log`;
- `validation-output`;
- `state-observation`;
- `provenance-record`;
- `human-attestation`;
- `external-reference`;
- `derived-analysis`;
- `contradictory-evidence`;
- `missing-evidence`;
- `unavailable-evidence`;
- `restricted-evidence`; or
- `other`.

`relationship` is exactly `supporting`, `qualifying`, `contradicting`,
`missing`, `unavailable`, `restricted`, or `not-assessed`. It is a declared
relationship, not proof of relevance or sufficiency.

`subjectReferences` is non-empty. The other relation arrays MAY be empty only
when the item's category and explicit conditions explain why. Every package-
local reference must resolve under the local integrity rules below.

`expectedObservation` and `actualObservation` remain separate. An absent actual
observation uses a condition such as `not-executed`, `unavailable`, or
`restricted`; it MUST NOT copy the expected observation or present expectation
as observation.

The closed `transformation` object identifies whether material was direct,
copied, extracted, summarized, transformed, redacted, aggregated, or derived;
the exact input references; method statement; output digest or condition;
known loss; and provenance. Transformation cannot create independent
corroboration or direct evidence.

The closed `integrity` object records supplied digest/signature/timestamp
claims or explicit conditions and limitations. It proves no truth,
authenticity, authority, or acceptance.

The closed `restrictedContent` object records classification, copied-content
disposition, access-authority reference or condition, minimization/redaction
statement, disclosure limit, retention/cleanup statement, and limitations.
Restricted content SHOULD be referenced rather than copied when safe review is
possible without disclosure.

## `reproductionProcedures` array

Every closed reproduction-procedure object contains exactly:

- `procedureReference`;
- `subjectReferences`;
- `executionRecordReferences`;
- `claimReferences`;
- `inputReferences`;
- `evaluatorContextReference`;
- `preconditions`;
- `steps`;
- `attemptState`;
- `outcome`;
- `deviations`;
- `outputReferences`;
- `evidenceReferences`;
- `diagnosticReferences`;
- `limitationReferences`;
- `cleanupObservation`; and
- `provenanceReferences`.

`procedureReference` is package-local and unique. `steps` is a non-empty
ordered array. Each closed step contains exactly:

- `stepReference`;
- `sequence`;
- `actionDescription`;
- `inputReferences`;
- `preconditions`;
- `expectedObservation`;
- `actualObservation`;
- `outcome`;
- `deviations`;
- `outputReferences`;
- `evidenceReferences`;
- `diagnosticReferences`;
- `limitationReferences`; and
- `startedAtOrCondition`; and
- `endedAtOrCondition`.

Step references are unique within the package. `sequence` starts at one and is
contiguous within the procedure. Array order MUST match `sequence`.

Step and procedure `outcome` are exactly `satisfied`, `not-satisfied`,
`unverifiable`, or `not-evaluated`. These outcomes state only the bounded
reproduction observation under the supplied context. They are not validation
phase outcomes, universal pass/fail, conformance, equivalence, approval, or
authority.

`attemptState` is exactly `not-attempted`, `attempted`, `completed`, `blocked`,
or `unverifiable`. `not-attempted` requires step outcomes `not-evaluated` and
explicit non-execution reasons. `blocked` and `unverifiable` remain visible and
cannot be rewritten as failure or success.

Every deviation object identifies exact expected and observed context,
category, reason, affected steps/claims, evidence, and limitations.
Substitution, coercion, defaulting, repair, fallback, retry, dependency change,
configuration change, capability change, environment change, limit change, or
network change MUST be recorded as a deviation; none is silent.

A reproduction description is not execution authority. A reproduced result is
new evidence. It does not retroactively replace, correct, approve, certify, or
strengthen the original record or evidence without a separately assessed claim.

## `outputs` array

Every closed output object contains exactly:

- `outputReference`;
- `category`;
- `producerReference`;
- `executionRecordReferences`;
- `procedureReferences`;
- `locationOrCondition`;
- `mediaTypeOrCondition`;
- `digestOrCondition`;
- `producedAtOrCondition`;
- `evidenceReferences`;
- `limitationReferences`; and
- `provenanceReferences`.

`outputReference` is package-local and unique. `category` is exactly
`raw-evaluator-output`, `diagnostic-output`, `log-output`,
`reproduction-output`, `summary-output`, or `other`.

An output entry records supplied material or a condition. It is not canonical
Validation Output, Portable Conformance Evidence, an Evidence Bundle, an
Artifact Instance, certification, release evidence, publication, or authority.

## `diagnostics` array

Every closed diagnostic object contains exactly:

- `diagnosticReference`;
- `category`;
- `subjectReferences`;
- `executionRecordReferences`;
- `procedureReferences`;
- `stepReferences`;
- `requirementReferenceOrCondition`;
- `message`;
- `evidenceReferences`;
- `limitationReferences`; and
- `restrictedContentDisposition`.

`diagnosticReference` is package-local and unique. `category` is exactly one
of `input-mismatch`, `revision-mismatch`, `digest-mismatch`,
`resource-closure-mismatch`, `reference-integrity-failure`,
`expected-actual-difference`, `unsupported-capability`, `warning`,
`resource-blocked`, `security-privacy-ambiguity`, `restricted-evidence`,
`adverse-evidence`, `non-execution`, or `other`.

Message text is bounded presentation and is not a portable stable error
vocabulary, severity, exit code, waiver, remediation, or authority.

## `limitations` array

Every closed limitation object contains exactly:

- `limitationReference`;
- `category`;
- `statement`;
- `affectedSubjectReferences`;
- `affectedExecutionRecordReferences`;
- `affectedProcedureReferences`;
- `affectedClaimReferences`;
- `evidenceReferences`;
- `disposition`; and
- `provenanceReferences`.

`limitationReference` is package-local and unique. `category` is exactly
`input`, `source`, `provenance`, `integrity`, `authenticity`, `freshness`,
`coverage`, `independence`, `reproducibility`, `transformation`, `capability`,
`configuration`, `dependency`, `environment`, `resource`, `evidence`,
`security-privacy`, `disclosure`, `retention-cleanup`,
`non-machine-verifiable`, or `other`.

`disposition` is exactly `material`, `restricted`, `unresolved`, or
`assessed-non-material`. An assessed-non-material limitation remains visible
and attributable. It is not permission to omit the item or upgrade a claim.

## `claimBoundary` object

The closed `claimBoundary` object contains exactly:

- `claims`;
- `explicitNonClaims`;
- `scope`;
- `exclusions`;
- `claimantReference`;
- `assessmentState`; and
- `provenanceReferences`.

Every closed claim object contains exactly:

- `claimReference`;
- `dimension`;
- `statement`;
- `subjectReferences`;
- `executionRecordReferences`;
- `procedureReferences`;
- `supportingEvidenceReferences`;
- `qualifyingEvidenceReferences`;
- `contradictingEvidenceReferences`;
- `missingEvidenceReferences`;
- `limitationReferences`;
- `disposition`; and
- `reason`.

`claimReference` is package-local and unique. `dimension` is exactly
`input-integrity`, `source-provenance`, `resource-closure`,
`execution-observation`, `output-integrity`, `evidence-support`,
`evidence-contradiction`, `reproducibility`, `reproduction-difference`, or
`other`.

`disposition` is exactly `bounded-claim`, `qualified`, `contradicted`,
`unverifiable`, or `not-assessed`. It is not a final sufficiency verdict or
decision. A claim MUST NOT be `bounded-claim` when material contradictory,
missing, restricted, unresolved, or unverifiable evidence required by that
claim remains applicable.

`assessmentState` is exactly `not-reviewed`, `comment-reviewed`,
`independently-reviewed`, or `review-unverifiable`. Review state does not
approve a claim or package.

No aggregate `valid`, `pass`, `fail`, traffic light, score, grade, badge,
threshold, quality gate, ranking, recommendation, approval, certification,
release fitness, deployment fitness, or universal evidence-sufficiency
property is permitted.

## `authorityBoundary` object

The closed `authorityBoundary` object contains exactly:

- `producerReference`;
- `assemblerReference`;
- `executorReferences`;
- `reviewerReferences`;
- `decisionMakerReferences`;
- `finalAuthorityReferences`;
- `reviewStatus`;
- `decisionStatus`;
- `automaticAuthority`;
- `authorizedEffects`; and
- `prohibitedAutomaticEffects`.

`reviewStatus` is exactly `not-reviewed`, `comment-reviewed`,
`independently-reviewed`, or `review-unverifiable`. `decisionStatus` is exactly
`no-decision`, `decision-pending`, `decided`, or `decision-unverifiable`.

`automaticAuthority` MUST be exactly `false`. `authorizedEffects` contains
only exact effects attributable to a separately supplied governing decision or
an explicit assessed-empty statement. `prohibitedAutomaticEffects` MUST list
at least approval, acceptance, integration, merge, issue closure, correction,
withdrawal, deprecation, supersession, certification, release, publication,
support, hosting, and deployment.

Production, assembly, schema validity, digest match, evidence reference,
reproduction, output, review, or repository presence grants no authority to
perform any prohibited effect.

## Referential integrity within one package

Representation Version `1.0.0` requires package-local referential integrity:

- every `subjectReference` resolves to exactly one `subjects` entry;
- every `executionRecordReference` resolves to exactly one
  `executionRecords` entry;
- every `evidenceReference` resolves to exactly one `evidenceItems` entry;
- every `procedureReference` resolves to exactly one
  `reproductionProcedures` entry;
- every `stepReference` resolves to exactly one step;
- every `outputReference` resolves to exactly one `outputs` entry;
- every `diagnosticReference` resolves to exactly one `diagnostics` entry;
- every `limitationReference` resolves to exactly one `limitations` entry;
- every `claimReference` resolves to exactly one claim; and
- every `inputReference` resolves to exactly one governing input or exact
  reproduction input declaration.

All package-local identifiers are globally unique within their own reference
kind. Duplicate or dangling local references make the representation
nonconforming. A reference of one kind MUST NOT resolve through another kind.

External source, authority, Definition, Schema Resource, Artifact, Tool,
Implementation, runtime, dependency, and record references remain opaque exact
pins unless their objects are supplied under a later separately Accepted
closure contract. Package-local integrity proves no external existence,
authenticity, support, contradiction, relevance, sufficiency, or trust.

General cross-record relationship evaluation, self-acceptance rules, review-
independence rules, and other normative integrity rules remain Package C work.

## Output, evidence, review, decision, and artifact separation

This package remains separate from:

- a Validation Execution Record;
- raw evaluator output;
- canonical Validation Output, if later defined;
- Portable Conformance Evidence;
- the CONTRACT-006 Evidence Bundle;
- the CONTRACT-007 Review Record;
- the CONTRACT-008 Decision Record;
- certification evidence;
- release evidence;
- support, compatibility, interoperability, security/privacy, hosting, or
  deployment evidence; and
- every other Artifact Instance.

It is not any of those records without a later separate Accepted identity,
version, schema, binding, provenance, lifecycle, and Artifact Instance
contract. Copying, embedding, referencing, hashing, signing, timestamping,
publishing, or reviewing material does not change this separation.

## Closed, offline-first, deterministic processing boundary

Any later producer or consumer MUST operate only on the exact caller-supplied,
closed, frozen, bounded context and package revision. It MUST NOT:

- discover or retrieve governing or evidence material automatically;
- follow redirects or treat network content as authority;
- rely on hidden caches, ambient files, environment variables, registries, or
  mutable aliases;
- interpret `latest`, newest-wins, popularity, majority, consensus, score, or
  ranking as meaning or precedence;
- silently substitute, coerce, default, repair, normalize, retry, or fall back;
- silently downgrade capability, dependency, configuration, environment,
  resource, security, privacy, or evidence requirements; or
- omit adverse, contradictory, missing, restricted, or non-executed material.

Deterministic ordering is limited to explicitly ordered arrays and exact local
reference resolution. No implementation algorithm, canonical JSON, global
sorting rule, scheduler, retry policy, or execution engine is created here.

## Security, privacy, resource, and disclosure boundary

Untrusted inputs and all copied or referenced material remain bounded. A future
producer or consumer must declare and enforce, under its own separately
accepted contract, applicable limits for:

- document, package, resource, reference, target, result, evidence-item,
  procedure, step, output, diagnostic, and claim counts and sizes;
- graph depth/breadth, recursion, composition, reference expansion, repeated
  evaluation, regex, and general evaluation cost;
- memory, CPU, wall time, concurrency, process/thread, file descriptor, output,
  diagnostic, logging, and temporary storage; and
- minimization, least privilege, redaction, access, disclosure, retention,
  cleanup, and restricted evidence.

Public packages MUST NOT contain credentials, tokens, secrets, personal data,
private project context, production configuration, private paths, hostnames,
restricted source material, or exploitable private details. Technical access
does not grant collection, copying, retention, disclosure, or publication
authority.

This candidate creates no concrete limit, threshold, algorithm, sandbox,
process model, access-control system, log format, cleanup mechanism, retention
policy, encryption, signing, transport, storage, or disclosure mechanism.

## Versioning and compatibility

Definition Version and Representation Version evolve independently under
Accepted identity/version policy.

- a compatible additive clarification that does not change valid package
  meaning MAY support a later MINOR version;
- an incompatible required property, token, closure, or semantic change
  requires a new MAJOR version;
- editorial correction without normative change may support PATCH treatment
  only under a separately accepted version decision; and
- Accepted Version `1.0.0`, if activated, remains immutable.

No mutable alias, registry preference, publication date, provider behavior,
reference implementation, or implementation default may select a governing
version.

## Lifecycle and dependency-first next work

Governed integration of this Accepted decision activates only the exact Package
Definition and JSON Representation identity/version pairs allocated here. It
does not create a package instance or authorize Package C, D, or E.

The next work remains dependency-first and separately governed:

1. Package C — test-manifest and initial cross-record integrity-rule contract;
2. Package D — concrete Tool and Implementation identity, version, capability,
   configuration, dependency, and interface contracts;
3. Package E — implementation, cases, bounded evidence, review, and
   attributable decision; and
4. any later release, publication, support, certification, hosting, or
   deployment.

No next package starts automatically from acceptance, integration, repository
presence, roadmap position, issue state, package production, evidence, or
reproduction.

## Consequences and limitations

Positive consequences:

- exact evidence and reproduction packages receive stable identities and one
  concrete representation target;
- expected and actual observations remain separate;
- direct, derived, supporting, qualifying, contradictory, missing,
  unavailable, and restricted evidence remain distinguishable;
- evaluator, Tool, Implementation, runtime, dependency, configuration,
  capability, environment, limits, and network declarations remain visible;
- reproduction steps, deviations, outputs, cleanup, diagnostics, limitations,
  and non-execution remain traceable;
- local dangling or duplicate references are prohibited; and
- later integrity, Tool/Implementation, runner, and evidence work receives a
  stable dependency without automatic authority.

Costs and limitations:

- the representation is intentionally detailed;
- package production requires explicit caller-supplied context and provenance;
- no executable schema, validator, resolver, runner, Tool, Implementation,
  interface, storage, or transport exists;
- external source existence, authenticity, referential integrity, evidence
  relevance, sufficiency, independence, and trust remain unproven;
- timestamps, digests, identities, observations, and declarations remain
  claims requiring evidence;
- package-local integrity is not general cross-record integrity;
- reproduction descriptions may remain unexecuted or unverifiable; and
- interoperability and broader conformance remain unproven.

## Protected predecessors and immutable history

This candidate changes none of the following:

- ARCH-001 through ARCH-034 and ADR-0001 through ADR-0034;
- CONTRACT-001 through CONTRACT-009;
- the ten Accepted Schema Versions `1.0.0`;
- all ten existing synthetic test manifests and the exact `203/38/165` case
  inventory;
- Core Artifact JSON Binding Version `1.0.0`;
- Accepted resolution, validation/output, Portable Conformance Evidence,
  readiness, assessment, remediation, decision, release, verification,
  completion, maintenance, and Extension Module/Profile sources;
- Release Version `0.1.0-prealpha.1`, tag `v0.1.0-prealpha.1`, its exact tag
  target and release-subject tree, and immutable GitHub Release objects;
- issue #80, issue #108, issue #114, PR #109, PR #115, or any historical issue,
  comment, review, commit, tree, tag, release, ruleset, or setting evidence; or
- public/private and final-human-authority boundaries.

## Explicit non-decisions

This candidate creates no tenth Artifact Type, Common Artifact Envelope change,
artifact contract, Artifact Instance, Validation Execution Record revision,
canonical Validation Output, Portable Conformance Evidence, Evidence Bundle,
Review Record, Decision Record, certification evidence, release evidence,
support evidence, or deployment evidence.

It creates no executable schema, schema `$id`, Schema Version, assertion, test
manifest, test case, cross-record integrity rule, validator, resolver, runner,
suite, reference implementation, Tool Identity/Version, Implementation
Identity/Version, runtime, dependency, environment, configuration, capability,
interface, CLI, API, workflow, CI, product, hosted service, registry, storage,
transport, or publication system.

It performs no dependency installation, schema/test execution, evidence
collection, reproduction, network access, security scan, specialist
security/privacy/legal review, correction, reassessment, release, publication,
support, certification, hosting, deployment, Ready-for-review transition,
merge, issue closure, or branch cleanup.

Package C, D, and E remain unauthorized and separately governed.

## Final-human authority

EIGENAAR / Final Authority remains the sole final human authority. Package
producer, assembler, executor, evaluator, Tool, Implementation, reviewer,
decision-maker, and final authority remain separate attributable dimensions.

Missing, ambiguous, conflicting, unavailable, unsupported, restricted, or
unverifiable authority remains visible and fail closed. A package cannot create
or launder authority through evidence, reproduction, review, publication, or
technical access.

## Lifecycle and final human authority

This Accepted decision did not approve itself. Attributable EIGENAAR / Final
Authority acceptance of the exact reviewed candidate is recorded in issue
comment `5241789812`. Repository presence, validation, and transparent
non-independent ARCHITECT review did not grant that acceptance.

Governed integration activates only the exact Package Definition and
Representation identity/version pairs and boundaries defined here. Acceptance
and integration do not create a package instance or authorize Package C, D, E,
an executable schema, dependency, Tool, Implementation, runner, workflow,
release, support, hosting, or deployment.
