# CNTX Epistemic Provenance and Freshness Extension Module JSON Representation Boundary (ARCH-040)

## Status and authority

**Document Status: Accepted.**

This documentation-only decision is Accepted under [issue
#139](https://github.com/CNTX-PROJECT/CNTX/issues/139) and attributable EIGENAAR
/ Final Authority issue-contract acceptance comment
[5259097128](https://github.com/CNTX-PROJECT/CNTX/issues/139#issuecomment-5259097128).
Exact-head acceptance is recorded in comment
[5259328712](https://github.com/CNTX-PROJECT/CNTX/issues/139#issuecomment-5259328712)
on candidate commit `60d815ed9545c5ab16a4531df9a83cc00ed65340` and tree
`4671ec2dac4df5029dddaaa5876375ba2b7b749d`, prepared directly from public
baseline commit
`67e04ad50d9563b7942c4f402841417391a72ac4` and tree
`89b7a2610d43684d6e48fc8455ad2480d0055ab7`.

The preceding Proposed status, issue-contract acceptance, candidate
preparation, branch or repository presence, validation, review, Draft state,
mergeability, URL availability, parsing, or implementation recognition did not
accept, allocate, activate, integrate, release, or authorize ARCH-040 or any
representation. Exact-head acceptance establishes Accepted status only.
Status promotion, Ready state, review, branch or repository presence, and
mergeability do not integrate or activate the decision; later separately
governed integration is required.

## Purpose and decision boundary

Accepted ARCH-038 defines logical responsibilities for epistemic provenance
and freshness but deliberately creates no JSON property, member, token, object
shape, payload, media type, Serialization Binding, schema, rule,
implementation, or execution. A later executable Definition Schema Resource
cannot reliably validate a representation that has not first been explicitly
bounded.

ARCH-040 therefore defines exactly one JSON-compatible instance-data model
for one bounded declaration about one exact source subject under the Accepted
Epistemic Provenance and Freshness Extension Module Definition. It defines:

1. one closed thirteen-member root model;
2. exact lower-camel-case property ownership;
3. closed serialized tokens for the six ARCH-038 source categories, eight
   information conditions, and four existing ARCH-024 outcomes;
4. exact-pinned definition, declaration, source, claim, provenance, temporal,
   digest, policy, clock/reference, derivation, condition, evaluation,
   limitation, and authority responsibilities;
5. explicit absence and fail-closed representation rules;
6. duplicate, ordering, extension, unknown-member, and opaque-identifier
   boundaries;
7. strict separation from Core Artifact Instances, activation declarations,
   schemas, rules, implementations, evidence instances, and final authority;
   and
8. the dependency-first handoff to a later separately governed Module
   Definition Schema Resource and synthetic case set.

This decision selects JSON-compatible names and shapes only. It does not define
JSON text serialization, canonical bytes, a media type, a Serialization
Binding, a Schema Identifier or Version, a canonical `$id`, a Schema Resource,
schema assertions, testcases, fixed expected results, validation, processing,
or execution.

## Exact decision basis

This decision is subordinate to and changes none of:

- ARCH-001 through ARCH-039 and ADR-0001 through ADR-0039;
- especially ARCH-024 and ARCH-028 through ARCH-038 for separate outcomes,
  Definition identity/version, activation, composition, resources, validation,
  tooling, the exact Module Definition, and final-human authority;
- CONTRACT-001 through CONTRACT-009;
- all ten Accepted Core Schema Resources and their exact Schema Versions
  `1.0.0`;
- Core Artifact JSON Serialization Binding Version `1.0.0`;
- all ten historical Test Manifests and the exact `203/38/165`, `957/948/9`,
  and `9/1` inventories;
- all thirteen Accepted Cross-Record Integrity Rules;
- the Accepted Tool and Implementation identities and Version `1.0.0` pins;
- Package E and bounded practice evidence and limitations;
- Accepted ARCH-039 and its exact Context Packet Profile Subjects and
  narrowing-only boundary;
- immutable prerelease `0.1.0-prealpha.1`, its tag, Release, verification, and
  completion history; and
- repository governance, settings, ruleset, security/privacy, public/private,
  adverse/restricted-evidence, non-aggregation, non-execution, and
  final-human-authority boundaries.

Representation under this decision cannot broaden, repair, override, weaken,
reinterpret, or replace an Accepted source. If this document and an Accepted
source could be read differently, the Accepted source controls and the
affected representation claim is blocked.

## Exact representation subject

The representation subject is one bounded declaration record about one exact
source subject under exactly this governing Definition key:

| Dimension | Exact value |
| --- | --- |
| Definition category | `CNTX Extension Module Definition` |
| Definition local name | `epistemic-provenance-freshness` |
| Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness` |
| Definition Version | `1.0.0` |
| Representation scope | One declaration record, one exact primary source subject, zero or more explicitly bounded claims and evaluations |
| Document status | Accepted |

The governing Definition Identifier is opaque and version independent. Its
HTTPS shape grants no dereferencing, retrieval, network, redirect, registry,
catalog, cache, trust, support, or authority. Definition Version remains a
separate exact pin.

ARCH-040 allocates no separate Representation Identifier or Representation
Version. The root model is the Accepted representation boundary for the exact
Definition key above. A later decision may determine whether an independent
Serialization Binding identity/version is necessary after a concrete Schema
Resource exists; this decision does not reserve one.

The represented declaration record is not:

- the Extension Module Definition or a Definition instance;
- an Extension Module instance or activation declaration;
- a Governing Definition Declaration or Governing Declaration Set;
- a Definition Package, bundle, registry entry, catalog entry, or cache entry;
- a CNTX Artifact Type or Artifact Instance;
- an Evidence Bundle, Validation Execution Record, Review Record, or Decision
  Record;
- a policy, rule, schema, validation output, or conformance claim; or
- an approval, certification, release, support, or deployment record.

## JSON-compatible model and naming rules

The logical instance-data model uses JSON-compatible values: object, array,
string, number, boolean, and null. This document does not define JSON text
bytes, member ordering, whitespace, escaping, Unicode normalization, numeric
lexical form, duplicate-member parser behavior, or a media type. Those remain
Serialization Binding or schema/implementation concerns where applicable.

Property names defined here use lower camel case and are case-sensitive. Token
values defined here use lowercase ASCII kebab case and are case-sensitive.
Opaque identifiers, revisions, source values, policy coordinates, digest
values, time values, references, and role identifiers preserve their supplied
case and meaning; processors MUST NOT case-fold, trim, normalize, repair,
coerce, infer, or substitute them.

The root is closed to exactly these thirteen properties:

1. `governingDefinition`;
2. `declaration`;
3. `source`;
4. `claims`;
5. `provenance`;
6. `temporal`;
7. `integrity`;
8. `policies`;
9. `derivation`;
10. `conditions`;
11. `evaluations`;
12. `limitations`; and
13. `authority`.

No root extension property, namespace escape, wildcard member, vendor member,
implementation metadata member, or unknown-member preservation bag is
permitted. A later Definition Version may add an explicitly governed
capability; the current representation does not create an open extension
surface.

## Root requiredness and conditional applicability

Every representation contains all thirteen root properties. Conditional
applicability is represented inside the responsible property through an exact
condition declaration; it is never represented by silently omitting a root
dimension.

This fixed root presence has three purposes:

1. Assessed None remains distinguishable from Missing.
2. Not Assessed remains distinguishable from Assessed None.
3. A processor cannot infer a favorable state from property absence.

Root presence does not require every subordinate value to be favorable or
available. It requires the responsible role to make the applicable condition
visible. A later schema may make particular subordinate values conditional on
the declared condition but MUST NOT replace an unfavorable condition with a
default value.

## Common condition wrapper

Every condition-bearing dimension uses the same logical wrapper
responsibilities:

| Property | Responsibility |
| --- | --- |
| `condition` | Exactly one closed information-condition token. |
| `value` | The dimension-specific value; present only where the condition and governing meaning permit it. |
| `explanation` | A bounded explanation of the exact condition, scope, uncertainty, conflict, restriction, or absence. |
| `evidenceRefs` | Zero or more opaque exact references to separately governed evidence; references grant no retrieval or access. |
| `responsibleRoles` | One or more attributable role references responsible for the declaration or assessment. |

The wrapper itself is closed. It creates no generic evidence object, authority
system, status score, confidence number, severity, recommendation, or
processor instruction.

For `specified`, the exact dimension-specific value is present and the
explanation states its bounded scope where necessary. For every other
condition, the explanation is required and the value is absent unless
minimum public-safe metadata is expressly necessary to identify a conflict,
restriction, or unverifiable subject without disclosing restricted content.

`restricted` never contains the restricted material merely to satisfy this
representation. `conflicting` preserves each material alternative through
explicit bounded references or public-safe declarations; it does not select a
winner. `unverifiable` records why reliable determination is unavailable; it
is not a favorable or unfavorable evaluation outcome.

## Closed source-category tokens

The six exact serialized source-category tokens are:

| Token | Exact ARCH-038 meaning |
| --- | --- |
| `governing-source` | An exact source whose Accepted authority governs the bounded requirement or decision in the declared context. |
| `observation-source` | An exact source directly observed or retrieved without automatic authority, authenticity, completeness, or currentness. |
| `evidence-source` | An exact source supplied to support or challenge one bounded claim with scope, provenance, limitations, and adverse information. |
| `derived-source` | Material produced from exact upstream sources through an explicitly described finite derivation chain. |
| `human-assertion-source` | An attributable human statement with identity, role, time, scope, and evidence boundary visible. |
| `model-recollection-source` | Visible non-governing model recollection that may be stale, incomplete, or wrong. |

A source may carry more than one token only when every role and claim boundary
is separately declared. Array order creates no precedence. Tokens are unique
within the source declaration.

Restricted, inaccessible, conflicting, missing, and unverifiable are not
source categories. An unknown or unsupported supplied category is not mapped
to a seventh category or accepted as an extension token. Its exact supplied
value is retained only as public-safe adverse input in the applicable
condition explanation, and every dependent favorable claim is blocked.

## `governingDefinition`

`governingDefinition` is a closed object responsible only for:

- `identifier`: the exact Definition Identifier above;
- `version`: exact Definition Version `1.0.0`; and
- `sourceRevision`: an exact immutable revision pin for the authoritative
  Accepted Definition source used by the declaring context.

The source revision does not replace the Definition Version. The Identifier
does not replace source revision. Neither creates retrieval, authenticity,
acceptance, activation, support, or authority. A wrong, missing, ambiguous, or
conflicting pin blocks every dependent successful claim.

## `declaration`

`declaration` is a closed object responsible for:

- `identifier`: one stable opaque identifier for this logical declaration
  record across revisions;
- `revision`: the exact declaration revision represented;
- `producingRole`: one attributable role reference;
- `governingContext`: an opaque exact context identifier/revision pin or an
  explicit unfavorable condition; and
- `supersedes`: zero or more exact prior declaration identifier/revision pins,
  without rewriting prior content.

The declaration identifier is not a CNTX Artifact Instance Identifier unless a
later separately Accepted binding says so. Revision order, storage, mutation,
concurrency, signing, hashing, and retrieval are not defined here. A new
revision does not silently correct or erase the old revision.

The declaration's production coordinate is owned only by
`temporal.recordProductionTime`; it is not duplicated under `declaration`.

## `source`

`source` is a closed object responsible for one exact primary source subject:

- `categories`: one or more unique recognized source-category tokens, or an
  explicit blocking condition for unknown/unsupported supplied input;
- `identity`: an exact opaque source identity or a condition wrapper explaining
  why a reliable exact identity cannot be established;
- `revision`: an exact opaque source revision/version or a condition wrapper
  explaining why a reliable pin cannot be established;
- `locations`: zero or more source/supply locations as provenance only;
- `availability`: a condition wrapper separate from identity, authenticity,
  completeness, applicability, and authority;
- `roles`: one or more bounded claim-role declarations; and
- `subjectBoundary`: the exact material subject boundary used by dependent
  claims.

Location is not identity, availability is not authenticity, and a mutable URL,
branch, alias, `latest`, `current`, filename, search result, cache item,
repository position, installation, or prior use is not an exact revision pin.

For a material source, missing or unreliable identity/revision remains visible
and blocks dependent favorable claims. The representation does not invent a
replacement identity or downgrade exactness to best effort.

## `claims`

`claims` is a closed array of zero or more bounded claim objects. Every claim
object is responsible for:

- one opaque stable `identifier` within the declaration scope;
- `subject`: an exact reference to the represented source subject or exact
  bounded sub-subject;
- `dimensions`: one or more exact epistemic-dimension tokens applicable to the
  claim;
- `statement`: the bounded declared proposition without asserting truth;
- `roles`: claimant and other attributable role references;
- `governingSources`: exact source identity/revision pins relevant to the
  claim;
- `scope`: inclusions, exclusions, applicability, and non-claims; and
- `evidenceRefs`: zero or more opaque exact evidence references.

The permitted dimension tokens preserve ARCH-038 separation:

`source-category`, `source-identity`, `source-revision`,
`source-availability`, `provenance`, `authenticity`, `integrity`,
`source-publication-revision-time`, `observation-retrieval-time`,
`record-production-time`, `valid-through-time`, `freshness`, `applicability`,
`clock-reference-provenance`, `derivation`, `validation`, and `evidence`.

Token order creates no ranking. A claim about one dimension never implies an
outcome in another. The statement is a declaration, not proof, evidence,
review, approval, or authority.

## `provenance`

`provenance` is a closed object with separate condition-wrapped
responsibilities for:

- `origin`;
- `custody`;
- `acquisition`;
- `observation`;
- `supply`;
- `transformation`; and
- `responsibleRoles`.

Each responsibility preserves exact identities/revisions where applicable,
time and reference provenance, sequence where material, access/disclosure
conditions, uncertainty, limitations, adverse information, and public-safe
restricted metadata.

Provenance does not establish truth, authenticity, integrity, freshness,
applicability, completeness, correctness, permission, acceptance, or
authority. A location, signature, repository, account, role label, or chain of
custody does not acquire an unrepresented favorable meaning.

## `temporal`

`temporal` is a closed object with exactly four separate condition-wrapped
coordinates:

1. `sourcePublicationRevisionTime`;
2. `observationRetrievalTime`;
3. `recordProductionTime`; and
4. `validThroughTime`.

Every specified coordinate carries:

- `value`: the supplied temporal value;
- `reference`: the exact clock/reference identity and revision where
  available;
- `offset`: explicit timezone or offset information where applicable;
- `precision`: represented precision;
- `uncertainty`: known resolution, uncertainty, skew, conversion, or
  synchronization limitation;
- `source`: exact source/provenance for the coordinate; and
- `responsibleRole`: the attributable declaring or observing role.

This decision creates no timestamp lexical syntax, calendar profile, default
timezone, duration, tolerance, threshold, clock service, synchronization
mechanism, or time comparison algorithm. A later schema must separately select
any syntax it can enforce without changing these meanings.

No coordinate is inferred from another. File metadata, commit time, HTTP
header, cache time, model statement, evaluator local clock, or record
production time cannot silently stand for another coordinate. A timestamp
without reference provenance and exact applicable policy evaluation proves no
freshness or currentness.

`temporal.recordProductionTime` is the sole structural owner of the
declaration's production coordinate. Other properties may reference its exact
meaning but must not repeat a divergent value.

## `integrity`

`integrity` is a closed object whose `digestClaims` property contains zero or
more separately bounded digest-claim objects. Each digest claim is responsible
for:

- `algorithm`: one exact opaque algorithm identity, with no default;
- `value`: the exact supplied digest value;
- `subjectBoundary`: the precise subject bytes or separately governed
  canonicalization reference;
- `sourceRevision`: exact source revision/version and acquisition context;
- `verificationProcedure`: an exact opaque procedure identity/revision or
  explicit condition;
- `observationTime`: an exact reference to the applicable temporal coordinate;
- `responsibleRole`: the attributable observing/verifying role;
- `condition`: the applicable information condition;
- `outcomeRef`: an exact reference to a separate evaluation where one exists;
- `evidenceRefs`; and
- `limitations`, failures, and adverse/restricted information.

This decision selects no digest algorithm, encoding, canonicalization,
signature, certificate, trust store, attestation, verification
implementation, or comparison behavior. A bare algorithm or value is
insufficient. A match supports only the exact bounded integrity claim and
proves no authenticity, semantic correctness, safety, trust, freshness,
authority, or fitness.

## `policies`

`policies` is a closed object with separate condition-wrapped
`freshnessPolicy` and `applicabilityPolicy` responsibilities. Every specified
policy pin carries:

- exact `identifier` and `version` as separate values;
- `authoritativeSource` and exact source revision;
- declared `taskClass` and/or `sourceClass` applicability coordinates;
- `temporalInputs` naming the exact coordinates used;
- `assessmentReferenceTime` and clock/reference provenance;
- an opaque exact `conditionBoundary` or comparison responsibility from the
  authoritative policy source;
- claimant/evaluator roles, evidence references, limitations, adverse and
  restricted information; and
- exact evaluation reference where separately present.

This representation creates no policy identity/version, task/source-class
vocabulary, threshold, duration, tolerance, grace period, comparison rule,
score, grade, traffic light, or quality gate. It carries only exact supplied
pins and bounded declarations.

No ambient, product-selected, provider-selected, implementation-preferred,
newest, `latest`, cached, or fallback policy is permitted. Missing or ambiguous
applicable policy keeps dependent freshness outcomes Unverifiable or Not
Evaluated; it can never be repaired to Satisfied.

## `derivation`

`derivation` is a condition-wrapped closed object. It is `specified` whenever
`derived-source` is one of the source categories and then carries:

- `upstreamSources`: a non-empty finite set of exact source
  identity/revision/category pins and access conditions;
- `transformations`: a finite sequence of exact transformation
  identity/revision pins, responsible roles, and material declared parameters;
- `relationships`: exact input/output relationships and transformation order;
- `omissions`: filtering, redaction, aggregation, interpretation, loss, and
  other material changes;
- `uncertainty`: propagated and introduced uncertainty;
- `integrityRefs`: applicable digest-claim references;
- `conditions`: adverse, conflicting, restricted, missing, unsupported, and
  unverifiable conditions; and
- `claimRefs`, `evidenceRefs`, `limitations`, and authority.

For a non-derived primary source, the responsible role uses `assessed-none` or
another exact condition supported by its bounded scope; the property is not
silently omitted.

The derivation must be finite, closed, caller-supplied, frozen, and acyclic for
one consequential assessment. This representation creates no transformation
vocabulary, operation semantics, processor, graph engine, execution order,
canonical operation identity, or proof that a transformation preserved
meaning, authenticity, integrity, completeness, freshness, or applicability.

## `conditions`

`conditions` is a closed array of dimension- and subject-bound condition
declarations. The exact condition tokens are:

| Token | Meaning |
| --- | --- |
| `specified` | Applicable information is explicitly declared for the exact frozen context. |
| `assessed-none` | The responsible role assessed the dimension and declared that no item exists or applies under the stated scope. |
| `not-assessed` | The dimension was not examined; no positive or negative conclusion exists. |
| `missing` | Information required by the governing context is absent. |
| `inaccessible` | Expected or identified information cannot be accessed under available mechanism or authority. |
| `conflicting` | Material declarations, sources, revisions, times, policies, or evidence cannot be reconciled. |
| `restricted` | Information exists or may exist but access or disclosure is bounded by governing authority. |
| `unverifiable` | Context, provenance, evidence, capability, precision, or access is insufficient for reliable determination. |

Each item names its exact dimension, subject, condition, explanation,
responsible roles, relevant public-safe references, limitations, and dependent
claim/evaluation effects. Array order creates no severity, precedence, or
resolution order. Duplicate items with the same dimension and subject must be
identical or are conflicting.

Assessed None is not Missing. Not Assessed is not Assessed None. Inaccessible
is not absent. Restricted is not favorable or adverse proof. Unverifiable is
not Not Satisfied. None may be collapsed into generic unknown, warning, pass,
or failure.

## `evaluations`

`evaluations` is a closed array of zero or more separate dimension-level
evaluation declarations. The only outcome tokens are the existing ARCH-024
values:

1. `satisfied`;
2. `not-satisfied`;
3. `unverifiable`; and
4. `not-evaluated`.

Every evaluation item names:

- exact `identifier` within the declaration;
- `dimension` and exact `subject`;
- `claimRef` where applicable;
- exact governing source identity/revision pins;
- policy identity/version and applicability where applicable;
- evidence references and evaluator context;
- observation/reference time and clock provenance;
- one outcome;
- diagnostics as bounded declarations, not a portable severity vocabulary;
- limitations, failures, adverse and restricted information;
- claimant, evaluator, reviewer where applicable, and governing authority; and
- non-execution or blocked prerequisites.

The array has no aggregate outcome property. No member, array order, count,
majority, score, weighting, ranking, or processor result may derive an
aggregate pass/fail, valid result, traffic light, grade, badge, threshold,
quality gate, recommendation, approval, certification, release fitness,
deployment fitness, or consequential authority.

Schema validity of the representation, if separately introduced later, is not
an evaluation outcome under this property and proves none of the represented
epistemic outcomes.

## `limitations`

`limitations` is a closed object responsible for separate non-empty arrays or
explicit Assessed None declarations for:

- `scopeLimitations`;
- `methodLimitations`;
- `evidenceLimitations`;
- `accessLimitations`;
- `securityPrivacyLimitations`;
- `resourceLimitations`;
- `adverseInformation`;
- `restrictedInformationMetadata`; and
- `unknownUnsupportedOrNonExecuted`.

Limitations are not warnings that a processor may discard. They are part of
the bounded meaning and must remain associated with affected subjects, claims,
conditions, and evaluations. Restricted metadata is minimum public-safe
orientation only and never substitutes for the protected information.

No limitation item creates a portable severity, confidence, risk score,
remediation instruction, access permission, disclosure permission, security
claim, privacy claim, legal conclusion, or acceptance decision.

## `authority`

`authority` is a closed object responsible for attributable role references
for:

- `declaringRoles`;
- `supplyingRoles`;
- `evaluatingRoles`;
- `reviewingRoles` where present;
- `governingRoles`; and
- `finalHumanAuthorityRole`.

Every role reference carries an opaque identity, role label, bounded scope,
and attribution/provenance reference. This decision creates no person,
account, organization, credential, authentication, authorization, access-
control, signature, delegation, voting, approval, or identity-verification
system.

The semantic invariant `automaticAuthority: false` remains fixed but is not a
serialized property. Its absence as a property cannot be interpreted as true,
false, configurable, unknown, or default. Technical output never becomes
self-acceptance, merge permission, release approval, deployment approval, or
final-human authority.

## Reference and identity boundary

Internal references between declaration-owned claims, conditions,
evaluations, digest claims, sources, temporal coordinates, and derivation items
are opaque local identifiers whose uniqueness and resolution scope are the
containing declaration. They create no external retrieval instruction or
global identity.

External source, policy, evidence, Definition, schema, role, or context
references remain opaque exact pins. A URI-shaped value grants no network
access, redirect following, catalog lookup, registry lookup, trust, or
authority. Relative-path interpretation, filesystem access, environment
resolution, and ambient discovery are prohibited.

A later schema may enforce local uniqueness and referential consistency within
one declaration but cannot prove that an externally referenced subject exists,
is accessible, authentic, Accepted, trustworthy, current, supported, or
authorized.

## Ordering, duplicates, and set meaning

Object member order carries no meaning. Array order carries meaning only for
`derivation.transformations` and exact input/output relationships where the
source declaration says sequence is material. All other arrays are unordered
logical sets or bags whose duplicate policy is explicitly defined:

- categories, identifiers, pins, references, roles, and exact condition/
  evaluation keys are duplicate-free;
- repeated identical limitation statements are non-conforming redundancy;
- non-identical declarations for the same exact subject/dimension/key are
  conflicting and remain visible; and
- insertion, document, lexical, package, or evaluation order creates no
  precedence or conflict resolution.

This document defines logical uniqueness, not byte-level canonicalization,
stable sorting, hash input, signature input, or deterministic reserialization.

## Absence, null, empty, and unknown handling

Absence, JSON `null`, empty string, empty object, empty array, Assessed None,
Not Assessed, Missing, Inaccessible, Restricted, Conflicting, and Unverifiable
are distinct.

This representation uses explicit condition declarations for semantic
absence. JSON `null` carries no automatic semantic absence meaning and is not
permitted as a convenience substitute for a required condition. Empty strings
do not satisfy identifiers, revisions, tokens, explanations, references,
times, digest values, policy pins, or role values. Empty arrays are permitted
only where zero items is the exact declared meaning and any required
Assessed None condition is separately explicit.

An unknown property or token is not ignored, stored as an extension, mapped to
a known value, or accepted by fallback. The exact supplied unknown value may be
retained as adverse public-safe input only in a bounded condition explanation.
Every dependent favorable claim remains blocked.

## Core sovereignty and placement boundary

The representation is separate from all existing Core Artifact JSON. It adds
no property to:

- Common Artifact Envelope Schema Version `1.0.0`;
- any of the nine artifact-specific Schema Versions `1.0.0`;
- any Accepted Artifact Contract Definition;
- Core Artifact JSON Serialization Binding Version `1.0.0`;
- a Context Packet or another Artifact Instance; or
- the existing ten-schema Tool/Implementation supported set.

The representation has no repository JSON instance path and no placement in a
Context Packet. A future Profile representation must separately define any
Context Packet-specific selection, narrowing, attachment, activation, or
declaration relationship after this Module representation is Accepted and
integrated.

Core validity remains a prerequisite. This representation cannot make
Core-invalid input valid, repair missing Core information, override a Core
contract, change an Artifact Type, or add authority to a Core record.

## Activation, composition, and conflict boundary

Representation presence activates nothing. A future consequential use still
requires an exact separately Accepted declaration/activation representation
and one closed frozen governing context under ARCH-030 and ARCH-031.

The represented Module has no Required or Optional Extension Module Definition
dependency and no Profile Subject. Another Extension Module may compose only
under separately Accepted exact dependency and declaration inputs, with
non-conflicting order-independent meanings. There is no precedence,
latest-wins, specificity, fallback, repair, or automatic conflict resolution.

ARCH-039 and any later Profile representation may only select or narrow
capabilities already present in exact pinned Accepted subjects. A Profile
cannot invent a Module property, weaken a condition, repair Core, convert
unfavorable information to favorable evidence, or override this Module
representation.

## Security, privacy, and resource boundary

Every represented source, reference, declaration, policy pin, time value,
digest value, derivation, role, limitation, and evidence reference is
untrusted. The representation must not contain credentials, secrets, tokens,
private keys, production configuration, unnecessary personal data, or
restricted content merely to make a record structurally complete.

Public records carry only authorized public-safe metadata for restricted
information. That metadata must not reveal the protected information through
filenames, paths, identifiers, query strings, error text, timing detail, role
detail, hashes of guessable content, or derivation descriptions.

This decision selects no maximum size, array count, string length, nesting
depth, derivation depth, time limit, memory limit, recursion limit, expansion
limit, redaction algorithm, sanitization mechanism, access control,
encryption, digest, signature, sandbox, process isolation, or network control.
A later schema and implementation must separately bound resources and preserve
non-execution when reliable complete processing is not possible.

The representation proves no source authenticity, integrity, freshness,
applicability, confidentiality, access authorization, privacy compliance,
security, legal status, safety, trust, or absence of risk.

## Lifecycle and change boundary

Accepted ARCH-040 consumes no separate representation identity/version.
Acceptance and status promotion activate or integrate nothing. If later
integrated through separately governed authority, it establishes only this
exact representation boundary against ARCH-038 Definition Version `1.0.0`.

A correction fixes documentary error without silently changing represented
meaning. A normative property, token, requiredness, condition, structure,
reference, or semantic change requires a separately governed compatibility and
version decision. Accepted historical content, cases, evidence, and authority
records remain immutable and are never rewritten in place.

Repository presence, parser acceptance, schema validity, implementation
support, popularity, or product use cannot select a representation version or
grant currentness, compatibility, support, or authority.

## Dependency-first Schema Resource handoff

After and only after attributable exact-head acceptance, governed integration,
completion, synchronization, and authorized cleanup of ARCH-040, the resulting
public `main` may be reassessed read-only for one concrete Module Definition
Schema Resource task.

That later task must separately decide:

1. one Definition Schema Identifier in the correct ARCH-031 family;
2. one initial Schema Version independent of Definition Version;
3. one version-qualified absolute HTTPS canonical `$id`;
4. one repository schema path and immutable standalone JSON Schema Draft
   2020-12 resource;
5. exact assertions against this representation and ARCH-038 only;
6. exact static-reference and resource-graph behavior;
7. synthetic expected-valid and expected-invalid cases for every material
   assertion family and relevant blocked/unsupported condition;
8. fixed expected results before any evaluator execution;
9. isolated validation that does not silently expand the Accepted ten-schema
   Tool/Implementation supported set; and
10. non-aggregation, limitations, adverse/restricted evidence, non-execution,
    and final-human authority.

This handoff authorizes none of those choices and reserves no Schema
Identifier, Version, `$id`, path, file, assertion, case, expected result,
validator capability, or later ARCH number.

## Consequences and limitations

Positive consequences:

- the ARCH-038 logical responsibilities receive one inspectable closed
  JSON-compatible shape before schema design;
- source categories, identities/revisions, provenance, temporal coordinates,
  policies, digests, clock/reference context, derivations, conditions,
  evaluations, limitations, and authority remain separate;
- semantic absence and unfavorable conditions cannot be hidden through missing
  properties or null/default values;
- Core Artifact JSON and Context Packet Schema Version `1.0.0` remain
  untouched;
- a later schema can be designed against an explicit target rather than
  inventing representation through assertions; and
- technical outcomes retain no aggregate or automatic authority.

Costs and limitations:

- the root and subordinate structures are intentionally explicit and may be
  verbose;
- callers must preserve exact pins, provenance, conditions, limitations, and
  attributable roles instead of relying on ambient context;
- concrete time syntax, policy vocabularies, digest methods, resource limits,
  schema constraints, bindings, and implementations remain unresolved;
- a structurally complete representation may still contain false, stale,
  incomplete, conflicting, restricted, or unverifiable declarations;
- preparation and review are non-independent;
- no implementation or adversarial execution evidence exists; and
- one bounded representation cannot prove completeness or suitability for all
  domains, sources, tasks, policies, security/privacy contexts, products, or
  deployments.

## Alternatives not selected

### Create the executable schema immediately

Not selected because ARCH-038 creates no target representation and explicitly
requires concrete representation and schemas/cases through separate gates. A
schema must not invent the data model it claims merely to validate.

### Add provenance/freshness properties directly to Context Packet

Not selected because ARCH-038 is an additive reusable Module and ARCH-039 is a
separate narrowing-only Profile. Existing Context Packet Contract and Schema
Version `1.0.0` remain immutable. Placement and attachment require later
Profile representation and activation decisions.

### Use an open extension object

Not selected because ambient vendor fields, namespaces, unknown members, and
fallback processing undermine closed supply, exact meaning, fail-closed
behavior, and deterministic review.

### Collapse condition and outcome into one status

Not selected because Specified/Missing/Restricted/Unverifiable conditions and
Satisfied/Not Satisfied/Unverifiable/Not Evaluated evaluation outcomes answer
different questions and carry different evidence and claim effects.

### Store only a timestamp and URL

Not selected because a URL is not exact identity/revision and a timestamp
without coordinate meaning, reference provenance, exact policy, applicability,
evidence, and evaluation proves no freshness.

### Select SHA-256 and RFC 3339 as implicit defaults

Not selected because ARCH-038 deliberately selects no digest algorithm,
timestamp syntax, calendar profile, canonicalization, or default timezone.
Those choices require later exact scope and compatibility analysis.

### Let model recollection fill missing values

Not selected because model recollection is explicitly non-governing and may be
stale, incomplete, or wrong. It remains a visible source category and cannot
repair a missing exact governing source or favorable claim.

## Protected predecessors and historical integrity

ARCH-001 through ARCH-039, ADR-0001 through ADR-0039, CONTRACT-001 through
CONTRACT-009, all existing identities and versions, ten Accepted Schema
Resources, twenty historical schema/test JSON files, five practice JSON files,
exact `203/38/165`, `957/948/9`, and `9/1` inventories, thirteen integrity
rules, Tool/Implementation contracts, Package E/practice evidence, immutable
release objects, settings, ruleset, H2.4, limitations, adverse/restricted
evidence, and historical authority records remain unchanged.

The current decision adds documentation only. It changes no JSON, schema,
test, fixture, expected result, rule, Python, dependency, runner, invocation,
workflow, CI, setting, tag, Release, evidence instance, or historical source.

## Explicit non-decisions and non-execution

Accepted status creates no Representation Identifier/Version, Serialization
Binding, Definition Schema Identifier, Schema Version, `$id`,
Schema Resource, schema file, assertion, Test Manifest, testcase, fixed
expected result, fixture, policy identity/version, task/source-class
vocabulary, threshold, duration, digest algorithm, canonicalization, clock
service, rule, diagnostic vocabulary, Tool/Implementation identity/version,
dependency, Python, code, runner, execution, validation output, Portable
Conformance Evidence, evidence instance, workflow, CI, release, publication,
support, certification, hosting, or deployment.

It performs no retrieval, network access, source resolution, policy
evaluation, time comparison, digest verification, transformation, validation,
test execution, evidence production, review decision, release action, or
deployment.

## Final-human authority and stopgate

The fixed semantic assertion `automaticAuthority: false` remains controlling.
No declaration, representation, parser result, later schema result, condition,
evaluation, evidence reference, review, score, majority, consensus, tool,
implementation, or model becomes final authority.

Exact-head acceptance is recorded in comment `5259328712`. Status promotion,
Ready-for-review, transparent non-independent COMMENT review, and final
read-only verification do not integrate or activate ARCH-040. Merge,
integration, issue closure, branch cleanup, Module Schema Resource work,
Profile representation, implementation, release, publication, support,
certification, hosting, deployment, and every later Phase 4A3 subphase require
new separate attributable EIGENAAR / Final Authority authority.

## References

- [Core architecture contract](core-contract.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Extension Module and Profile Identity and Version Policy](extension-module-profile-identity-version-policy.md)
- [Extension Module and Profile Dependency, Activation, Composition and Conflict Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [Extension Module and Profile Schema Resource, Packaging and Declaration Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [Extension Module and Profile Executable Schema and Validation/Conformance Boundary](extension-module-profile-executable-schema-validation-conformance-boundary.md)
- [Extension Module and Profile Tooling and Implementation Boundary](extension-module-profile-tooling-implementation-boundary.md)
- [Epistemic Provenance and Freshness Extension Module Definition](epistemic-provenance-freshness-extension-module-definition.md)
- [Context Packet Epistemic Provenance and Freshness Profile Definition](context-packet-epistemic-provenance-freshness-profile-definition.md)
- [ADR-0040](adr/0040-epistemic-provenance-freshness-extension-module-json-representation-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
