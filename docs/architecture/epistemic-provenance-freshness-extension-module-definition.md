# CNTX Epistemic Provenance and Freshness Extension Module Definition (ARCH-038)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only Extension Module Definition
governed by [issue #128](https://github.com/CNTX-PROJECT/CNTX/issues/128) and
recorded by
[ADR-0038](adr/0038-epistemic-provenance-freshness-extension-module-definition.md).
Attributable EIGENAAR / Final Authority issue-contract acceptance is recorded
in issue comment
[5251980826](https://github.com/CNTX-PROJECT/CNTX/issues/128#issuecomment-5251980826).
Attributable EIGENAAR / Final Authority acceptance of exact candidate commit
`e6700258c584deaabf028e8d339680567ed1715f` and tree
`664f00045fc7dcfb26ff2d9cf12c5787c0524493` is recorded in exact-head issue
comment
[5252557346](https://github.com/CNTX-PROJECT/CNTX/issues/128#issuecomment-5252557346).

Candidate preparation, repository presence, validation, mergeability, and the
transparent non-independent ARCHITECT review did not grant acceptance. The
exact-head acceptance above makes the reviewed Definition Accepted. Separately
governed integration to `main` remains required to integrate this decision and,
with that acceptance, allocate and activate only the exact Definition
Identifier and Version stated below.

Status promotion, branch presence, repository presence, Ready-for-review,
review, and mergeability do not by themselves integrate this decision or
allocate or activate its Identifier or initial Definition Version. They create
no support, release, deployment, or governing-use authority.

## Purpose and decision boundary

CNTX Public Core can already declare source and temporal information in bounded
human-readable contexts, but those declarations do not by themselves establish
source authenticity, exact revision, observation provenance, policy-pinned
freshness, clock provenance, digest meaning, or currentness.

This Definition specifies exactly one additive Extension Module
responsibility: preserving explicit, independently assessable epistemic
provenance and freshness meaning for exact sources, observations, derived
context, and bounded claims.

It defines only:

1. one exact Extension Module Definition identity and initial version;
2. six closed logical source categories;
3. exact source identity and revision/version responsibilities;
4. four separate temporal coordinates;
5. digest algorithm, value, and subject-boundary responsibilities;
6. exact policy identity/version and applicability responsibilities;
7. clock/reference provenance and uncertainty/precision responsibilities;
8. derivation-chain responsibilities;
9. separate information-condition states and evaluation outcomes;
10. fail-closed unknown, unsupported, conflicting, restricted, and
    unverifiable handling; and
11. security/privacy, lifecycle, evidence, non-execution, and final-human-
    authority boundaries.

It creates no Profile, concrete property, payload shape, serialized
declaration, Schema Resource, executable schema, rule, testcase, validator,
tool, implementation, execution, evidence instance, release, publication,
support, certification, hosting, or deployment.

## Exact decision basis

This decision was first proposed on exact public baseline commit
`65a659efac05528b23a67b6a3ebfdbd337b336dd` and tree
`12b29e79b253ca6cf7b1486598b894ad0eac6e8f`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-037 and ADR-0001 through ADR-0037;
- especially ARCH-028 through ARCH-033 for Extension Module/Profile category,
  identity/version, dependency/activation/composition/conflict,
  resource/package/declaration, schema/validation/conformance, and
  tooling/implementation boundaries;
- CONTRACT-001 through CONTRACT-009;
- all ten Accepted Core Schema Versions `1.0.0` and their exact Schema
  Resources;
- all ten historical Test Manifests and their exact `203/38/165` case
  inventory;
- historical schema-reference inventory `957/948/9`;
- all thirteen Cross-Record Integrity Rules Version `1.0.0`;
- the Accepted Tool and Implementation identities and Version `1.0.0` pins;
- the completed Package E and bounded cross-record practice evidence,
  including every limitation and `automaticAuthority: false`; and
- immutable prerelease `0.1.0-prealpha.1`, tag `v0.1.0-prealpha.1`, GitHub
  Release `367290932` / `RE_kwDOTsnR984V5Go0`, ruleset `20518984`, disabled
  Actions, and current security settings.

This status promotion changes none of those sources, identities, versions,
schemas, assertions, expected results, bindings, rules, tools,
implementations, evidence, limitations, statuses, settings, or authority.

## Definition subject

| Dimension | Exact Accepted value |
| --- | --- |
| Definition category | CNTX Extension Module Definition |
| Local name | `epistemic-provenance-freshness` |
| Extension Module Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness` |
| Initial Extension Module Definition Version | `1.0.0` |
| Lifecycle status | Accepted |

The Identifier is an opaque, version-independent logical identifier. It does
not authorize dereferencing, discovery, retrieval, redirects, registry or
catalog lookup, network access, trust, support, or authority. Definition
Version is a separate exact pin.

Discussion, issue acceptance, candidate preparation, status promotion, branch
or repository presence, Ready-for-review, review, mergeability, path, filename,
URL availability, implementation recognition, or product use does not by
itself integrate the decision, allocate the Identifier, or activate Version
`1.0.0`. Exact-head acceptance comment `5252557346` plus separately governed
integration to `main` allocates and activates only this exact Identifier and
Version as the integrated Accepted Definition. Proposed and reviewed states
consume no Definition Version.

No Profile Definition Identifier, Profile Definition Version, or Profile local
name is created or reserved.

## Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
express requirement strength within this Accepted Definition. They do not
create a representation, processor, implementation, execution permission, or
consequential authority.

## Additive responsibility and Core sovereignty

Upon separately governed integration, this Accepted Definition adds only epistemic
provenance and freshness meaning. It MUST NOT:

1. modify, replace, weaken, reinterpret, repair, coerce, default, or override
   any Accepted Core source, identity, version, field, token, relationship,
   assertion, testcase, expected-validity declaration, binding, or authority;
2. make a Core-invalid representation Core-valid;
3. make any Core artifact depend implicitly on this Definition;
4. infer activation from repository, path, filename, URL, package,
   installation, implementation, cache, product, or prior execution state;
5. turn missing, adverse, conflicting, restricted, uncertain, or unverifiable
   information into proof;
6. make provenance equivalent to authenticity, a digest equivalent to trust,
   or freshness equivalent to applicability or correctness; or
7. bypass attributable final human authority.

Where this Definition and an exact pinned Core requirement materially
conflict, the dependent Extension Module evaluation MUST fail closed. This
Definition has no override precedence.

## Separate epistemic dimensions

The following dimensions MUST remain separate:

| Dimension | Bounded responsibility | Does not establish |
| --- | --- | --- |
| Source category | Classify the declared epistemic role of a source under this exact Definition Version. | Identity, authority, authenticity, or quality. |
| Source identity | Identify the intended source exactly enough for the governed claim. | Revision, accessibility, or trust. |
| Source revision/version | Pin the exact source state used. | Currentness or compatibility. |
| Source availability | State whether the source can be accessed under governing authority. | Authenticity, completeness, or applicability. |
| Provenance | Preserve origin, custody, acquisition, transformation, and responsible-role information. | Truth, acceptance, or authority by itself. |
| Authenticity | Support a bounded claim that the source is what it purports to be. | Integrity, freshness, or correctness. |
| Integrity | Support a bounded claim that exact subject material was not changed relative to an explicit mechanism. | Authenticity, semantic correctness, or trust. |
| Source publication/revision time | State when the source says it was published or revised. | Observation time or currentness. |
| Observation/retrieval time | State when the source was observed or retrieved. | Source publication time or freshness proof. |
| Record production time | State when the declaring record was produced. | Source or observation time. |
| Valid-through time | State an optional declared temporal applicability boundary. | Automatic applicability or authority. |
| Freshness policy | Identify exact criteria against which temporal information may be assessed. | A result without evaluation and evidence. |
| Applicability policy | Identify the task/source class for which an assessment is relevant. | Freshness, validity, or permission. |
| Clock/reference provenance | Identify the time reference, offset, precision, and uncertainty basis. | Clock correctness or synchronization proof. |
| Derivation | Preserve exact upstream inputs and transformations for derived material. | Source authenticity or transformation correctness. |
| Validation | Evaluate one exact requirement against one frozen context. | Acceptance, conformance in another dimension, or final authority. |
| Evidence | Support one bounded claim with provenance and limitations. | Review, approval, certification, release, or deployment. |

No dimension substitutes for or implies another. In particular, availability
is not authenticity; authenticity is not integrity; integrity is not
freshness; freshness is not applicability; applicability is not correctness;
validation is not acceptance; and implementation support is not normative
authority.

## Closed logical source categories

For Definition Version `1.0.0`, the logical source-category set is
closed to exactly these six semantic categories:

1. **Governing Source** — an exact source whose accepted authority governs the
   bounded requirement or decision in the declared context.
2. **Observation Source** — an exact source directly observed or retrieved for
   the bounded assessment, without an automatic claim of authority,
   authenticity, completeness, or currentness.
3. **Evidence Source** — an exact source supplied to support or challenge one
   bounded claim, with claim scope, provenance, limitations, and adverse
   information preserved.
4. **Derived Source** — material produced from one or more exact upstream
   sources through an explicitly described transformation and derivation
   chain.
5. **Human Assertion Source** — an attributable human statement whose
   identity, role, time, scope, and evidence boundary remain visible.
6. **Model Recollection Source** — model-produced recollection that is
   explicitly visible, non-governing, possibly stale, incomplete, or wrong,
   and never a substitute for an exact governing source.

These names define logical meaning, not serialized tokens, JSON values, fields,
types, or a portable vocabulary. A source may perform more than one role only
when each applicable category and claim boundary is explicitly declared and
independently assessed. Category order creates no precedence.

A category not defined by the exact active Definition Version is unknown. An
unknown category or unsupported category version MUST remain visible and MUST
block every dependent successful claim. It MUST NOT be mapped silently to a
known category, ignored, approximated, or handled by fallback.

Restricted is an access/disclosure condition, not a seventh source category.
Inaccessible, conflicting, missing, and unverifiable are condition states, not
source categories.

## Exact source identity and revision/version

Every source that is material to a dependent claim MUST have:

1. one declared logical source category;
2. an exact source identity appropriate to its governing context;
3. an exact source revision or version, or an explicit condition stating why
   no reliable exact revision/version can be established;
4. the authoritative or supplying source location as provenance only, without
   treating availability as authority;
5. the applicable claim scope and role;
6. acquisition or observation provenance where applicable;
7. disclosed limitations, adverse information, access restrictions, and
   uncertainty; and
8. attributable declaring and governing roles.

A mutable alias, branch name, `latest`, `current`, newest-wins selection,
unversioned URL, search result, repository position, cache entry, filename,
installation state, product setting, or prior successful use MUST NOT replace
an exact revision/version pin.

If the exact identity, revision, category, source, or provenance required for a
dependent claim is missing, ambiguous, conflicting, unknown, unsupported,
restricted beyond governing access, or unverifiable, that condition MUST
remain visible and the dependent claim MUST fail closed.

## Separate temporal coordinates

This Definition distinguishes exactly four logical temporal coordinates:

1. **Source Publication/Revision Time** — the time a source declares for its
   publication or revision.
2. **Observation/Retrieval Time** — the time the supplied source was actually
   observed or retrieved for the bounded context.
3. **Record Production Time** — the time the provenance/freshness declaration
   or containing record was produced.
4. **Valid-Through Time** — an optional declared boundary through which a
   source, statement, or assessment claims temporal applicability under an
   exact policy.

No coordinate may be inferred from another. Absence of one coordinate MUST NOT
be repaired with another. A file timestamp, commit time, HTTP header, cache
time, local clock value, model statement, or record production time MUST NOT be
treated as a different coordinate without explicit governing meaning and
evidence.

Every supplied coordinate MUST preserve its declared time reference, timezone
or offset, precision, uncertainty, clock/reference provenance, and source. A
timestamp without those boundaries proves no freshness or currentness.

Valid-Through Time is optional and grants no automatic validity, permission,
support, or currentness. Expiry, absence, conflict, or uncertainty MUST be
assessed only under an exact pinned applicability and freshness policy.

This Definition creates no timestamp syntax, calendar profile, clock service,
time synchronization mechanism, tolerance, duration, age threshold, or
default timezone.

## Digest meaning and algorithm agility

Where a digest is material to an integrity claim, the declaration MUST keep
separate:

1. exact digest algorithm identity;
2. exact digest value;
3. the precise subject bytes or separately governed canonicalization rule;
4. source revision/version and acquisition context;
5. comparison or verification procedure;
6. observation time and responsible role; and
7. outcome, limitations, failures, and adverse evidence.

There is no implicit or default digest algorithm. An algorithm name without a
value, a value without an algorithm, or either without an exact subject
boundary is insufficient. A digest match supports only the bounded integrity
claim defined by its exact mechanism and evidence. It proves no authenticity,
semantic equivalence, safety, trust, freshness, authority, or fitness.

This Definition selects no algorithm, encoding, canonicalization, signature,
attestation, trust store, certificate, or verification implementation.

## Freshness and applicability policy pins

Every consequential freshness assessment MUST identify exactly:

1. the applicable policy identity;
2. the exact policy version;
3. the declared task class or source class to which it applies;
4. the source identity/revision and source category;
5. the temporal coordinate or coordinates used;
6. the clock/reference, timezone or offset, precision, and uncertainty basis;
7. the assessment reference time and its provenance;
8. the applicable condition, tolerance, or boundary from the authoritative
   policy source;
9. the assessment outcome and diagnostics; and
10. limitations, conflicts, restricted evidence, non-execution, claimant, and
    authority.

Policy identity is not policy content. Policy version is not applicability.
Applicability is not freshness. Freshness is not authenticity, integrity,
correctness, completeness, acceptance, support, or fitness.

No default, ambient, product-selected, provider-selected, implementation-
preferred, newest, `latest`, cached, or fallback policy is permitted. If no
exact applicable policy identity/version can be established, the freshness
dimension is Unverifiable or Not Evaluated as appropriate; it MUST NOT be
reported as Satisfied.

This Definition creates no concrete policy identity, policy version, task-
class vocabulary, source-class vocabulary, duration, threshold, comparison
rule, grace period, score, grade, traffic light, or quality gate.

## Clock/reference provenance, precision, and uncertainty

Clock/reference information MUST preserve, where applicable:

- the reference or clock source identity and exact revision/version where
  available;
- the responsible observation or producing environment;
- timezone or explicit offset;
- represented precision and known resolution;
- known uncertainty, skew, synchronization limitation, or conversion;
- acquisition and transformation provenance;
- conflict or absence; and
- the exact claim for which the time value is used.

An unavailable, unknown, unsupported, conflicting, insufficiently precise, or
unverifiable time reference MUST remain explicit. It MUST NOT be replaced by
the evaluator's local clock, record creation time, file metadata, network
response time, or another convenient coordinate.

This Definition proves no clock correctness, synchronization, monotonicity,
tamper resistance, time-source authenticity, or legal timestamp status.

## Derivation chains

A Derived Source MUST preserve a finite, explicit derivation chain containing,
at least logically:

1. every exact upstream source identity and revision/version;
2. each upstream source category and applicable access condition;
3. acquisition or observation provenance and temporal coordinates;
4. each transformation identity, revision/version, responsible role, and
   declared parameters where material;
5. transformation order and exact input/output relationships;
6. digest meaning where used;
7. omissions, filtering, redaction, aggregation, interpretation, and loss;
8. uncertainty propagated or introduced;
9. adverse, conflicting, restricted, and unverifiable conditions; and
10. the bounded claim, evidence, limitations, and authority.

The chain MUST be finite, closed, caller-supplied, and frozen for one
consequential assessment. A missing material upstream source or transformation,
cycle, conflicting revision, unknown mechanism, restricted dependency, or
insufficient provenance blocks every dependent successful claim.

Derivation does not transfer governing authority from one source to another.
Summarization, copying, redaction, translation, conversion, aggregation, model
processing, or human interpretation does not automatically preserve
authenticity, integrity, completeness, freshness, applicability, or meaning.

This Definition creates no transformation vocabulary, provenance graph
serialization, canonical operation identity, processor, or execution.

## Information-condition states

The following logical condition states MUST remain distinct:

| Condition | Meaning |
| --- | --- |
| Specified | The applicable information is explicitly declared for the exact frozen context. |
| Assessed None | The responsible role explicitly assessed the dimension and recorded that no item exists or applies under the exact stated scope. |
| Not Assessed | The dimension was not examined; no positive or negative conclusion is available. |
| Missing | Information required by the governing context is absent. |
| Inaccessible | The information is expected or identified but cannot be accessed under the available mechanism or authority. |
| Conflicting | Two or more material declarations, sources, revisions, times, policies, or evidence items cannot be reconciled under the governing context. |
| Restricted | Information exists or may exist but access or disclosure is bounded by governing authority; public-safe metadata does not replace the restricted content. |
| Unverifiable | Available context, provenance, evidence, capability, precision, or access is insufficient for a reliable determination. |

These are semantic conditions, not serialized values or a portable diagnostic
vocabulary. More than one condition may be relevant only when each applies to
a different exact dimension or subject and the distinction is explicit.

Assessed None is not Missing. Not Assessed is not Assessed None. Inaccessible
is not absent. Restricted is not favorable or adverse proof. Unverifiable is
not Not Satisfied. None of these conditions may be collapsed into a generic
unknown, warning, pass, or failure.

## Evaluation outcomes and non-aggregation

Where an applicable contract performs a broader CNTX assessment, the existing
ARCH-024 outcomes remain controlling and separate:

1. `Satisfied`;
2. `Not Satisfied`;
3. `Unverifiable`; and
4. `Not Evaluated`.

Every outcome MUST name its exact dimension, subject, governing source,
identity/version pins, policy where applicable, evidence, evaluator context,
observation time, limitations, adverse/restricted information, and authority.

No source category, temporal coordinate, digest, policy pin, condition state,
or individual outcome creates an aggregate pass/fail, valid result, traffic
light, score, grade, badge, threshold, rubric, quality gate, recommendation,
approval, certification, release fitness, deployment fitness, or
consequential authority.

The fixed logical assertion `automaticAuthority: false` applies to this
Definition. It is a semantic non-authority assertion, not a JSON property or
serialized member created by this document.

## Dependencies, activation, and composition

This Accepted Definition has no Required or Optional Extension Module
Definition Dependencies and creates no Profile Subject.

Its normative basis remains the exact Accepted CNTX architecture and authority
sources identified above. That basis is not an executable Definition
dependency graph and does not make Core depend on this Definition.

Any consequential use of this Accepted Definition still requires a separately
Accepted declaration/activation representation and one
closed frozen context under ARCH-030 and ARCH-031. That context would need to
pin the exact Definition Identifier and Version, authoritative definition
source and revision, activation authority, applicable Core inputs, source and
policy material, provenance, limitations, and every unknown, unsupported,
conflicting, restricted, or blocked condition.

Repository presence, URL availability, installation, processor capability, or
Profile selection activates nothing. A later Profile may select or narrow only
capabilities already present in its exact pinned Accepted inputs. It cannot
invent, weaken, reinterpret, repair, or extend this Definition.

Composition with another exact active Extension Module is permitted only under
separately Accepted dependency and declaration inputs and only where governing
meanings are non-conflicting and order-independent. There is no precedence,
latest-wins rule, fallback, or automatic conflict resolution.

## Closed supply and fail-closed processing

Every consequential assessment under this Definition MUST be explicit,
caller-supplied, offline-first, closed, finite, frozen, and exact-pinned before
evaluation begins.

The context MUST NOT be expanded, repaired, or completed through automatic
discovery, retrieval, network access, redirects, registries, catalogs, mirrors,
caches, mutable aliases, environment state, product configuration, model
recollection, previous success, or implementation preference.

At minimum, the following remain separately visible and block every dependent
successful claim:

1. missing, ambiguous, duplicate, or conflicting source identity or revision;
2. unknown or unsupported source category or Definition Version;
3. missing authoritative source or insufficient acceptance provenance;
4. wrong or absent policy identity/version;
5. policy-applicability ambiguity;
6. missing, conflated, conflicting, or unverifiable temporal coordinates;
7. missing or insufficient clock/reference provenance, precision, or
   uncertainty;
8. digest algorithm/value/subject mismatch or insufficiency;
9. incomplete, cyclic, ambiguous, or unsupported derivation;
10. unavailable or required restricted information;
11. conflicting, adverse, insufficient, or unverifiable evidence;
12. unsupported evaluator capability or mechanism;
13. security/privacy ambiguity or disclosure conflict;
14. resource condition preventing reliable complete assessment;
15. non-executed prerequisite or blocked dependent phase; and
16. missing or ambiguous authority.

No condition may be resolved silently through load, document, package, or
lexical order; newest/latest; substitution; coercion; defaulting; repair;
retry; hidden cache; fallback; majority; consensus; score; ranking; popularity;
or implementation preference.

## Representation, schema, rule, and implementation boundary

This Definition states logical responsibilities only. It creates no:

- JSON property, member, type, enum value, object shape, array shape, payload,
  declaration syntax, field vocabulary, media type, or Serialization Binding;
- Definition instance, Extension Module instance, Profile Definition, Profile
  instance, Artifact Type, or Artifact Instance;
- Definition Schema Identifier, Schema Version, canonical `$id`, Schema
  Resource, schema assertion, manifest, testcase, expected-validity
  declaration, fixture, or scenario matrix;
- portable rule identity/version, rule representation, evaluation-record
  representation, diagnostic code, severity, status, or output vocabulary;
- policy identity/version, policy representation, threshold, algorithm,
  canonicalization, clock service, resolver, retrieval mechanism, or network
  behavior;
- Tool Identity/Version, Implementation Identity/Version, capability profile,
  dependency, configuration, interface, validator, runner, library, SDK, CLI,
  API, workflow, CI, runtime, product, or service; or
- execution, validation output, Portable Conformance Evidence, Evidence Bundle,
  Review Record, Decision Record, release record, publication, support,
  certification, hosting, or deployment.

Concrete representation, schemas/cases, evaluation rules, Tool/Implementation
capability versions, implementation, practice, and evidence each require later
separate authority gates.

## Evidence, review, and claim boundaries

Evidence under this Definition would support only a bounded claim over exact
sources, revisions, policies, times, clock/reference provenance, derivations,
context, evaluator capability, observation, and limitations.

Evidence MUST preserve favorable, adverse, conflicting, missing, restricted,
unverifiable, blocked, and non-executed information without automatic weighting
or erasure. Restricted content MUST NOT be copied into a public record; only
the minimum public-safe existence, access, scope, and limitation metadata may
be stated when authorized.

Preparation, promotion, validation, publication, and a transparent
non-independent ARCHITECT review are not independent assurance. They do not
prove implementation behavior,
authenticity, integrity, freshness, applicability, security/privacy,
interoperability, support, certification, release fitness, or deployment
fitness.

No implementation or adversarial execution evidence exists for this
capability. No evidence instance is created by this document.

## Security, privacy, and resource boundary

Source and provenance information may expose identities, relationships,
locations, timings, access patterns, restricted material, or sensitive
derivations. Any later representation or processing MUST separately govern:

- minimization, purpose, access, disclosure, retention, and cleanup;
- public/private and restricted-evidence separation;
- source substitution, spoofing, revision ambiguity, and provenance conflict;
- malicious or excessive derivation graphs and temporal inputs;
- digest and canonicalization confusion;
- clock manipulation, skew, precision loss, and timezone conversion;
- dependency, input, graph, memory, CPU, time, handle, thread, process, output,
  log, storage, and network limits;
- correction, withdrawal, deprecation, and supersession; and
- unknown and unsupported mechanisms.

Secrets, credentials, tokens, private keys, personal data, production
configuration, private paths, local absolute paths, restricted content,
private project context, and private implementation details remain outside
public CNTX sources.

This Definition grants no access, permission, disclosure, authenticity, trust,
security, privacy, legal, compliance, support, certification, release, or
deployment claim.

## Compatibility, conformance, and lifecycle

Any later compatibility or conformance statement MUST name the exact
Definition Identifier/Version, authoritative source revision, Core basis,
source categories, source/revision pins, policies, frozen context, evaluator
capabilities, evidence, observation time, limitations, claimant, claim
dimension, and attributable authority.

Conformance in one dimension proves no other dimension. A source may be fresh
under one exact policy and inapplicable, unverifiable, or stale under another.
A digest may match while authenticity or meaning remains unproven. Successful
schema evaluation, if separately created later, would not prove Definition,
implementation, interoperability, security/privacy, support, certification,
release, or deployment conformance.

Upon separately governed integration, Accepted Definition Version `1.0.0` is
allocated, activated, and immutable. Correction, normative change, withdrawal,
deprecation, or supersession requires a new exact baseline, scope, evidence,
review, attributable acceptance, integration, and completion lifecycle under
ARCH-029. Historical versions remain identifiable.

The immutable prerelease `0.1.0-prealpha.1`, its tag, subject, GitHub Release,
and verification remain unchanged. This Definition and status promotion do not
extend that release subject or publish this Definition.

## Dependency-first handoff

This Accepted Definition is the first documentation-only dependency in the
Source, Provenance and Freshness roadmap phase. Its status promotion authorizes
no later step.

Exact-head acceptance is recorded in comment `5252557346`. Only after
separately governed integration, completion, synchronization, and a new
read-only reassessment may a later authority consider another bounded phase. A
possible Profile remains separately governed and may not invent a capability
absent from exact pinned Accepted inputs.

No Profile name, Identifier, Version, issue, branch, path, representation,
schema, rule, tool, implementation, evidence, release, or authority is reserved
or created by this handoff.

## Consequences and limitations

Positive consequences:

- source role, identity, revision, provenance, and availability cannot be
  collapsed into one unqualified source reference;
- publication, observation, record-production, and valid-through times remain
  separate;
- freshness requires an exact policy and clock/reference basis;
- digest meaning requires an explicit algorithm and exact subject boundary;
- derived context retains upstream and transformation traceability;
- model recollection remains visible and non-governing;
- missing, inaccessible, conflicting, restricted, and unverifiable conditions
  remain visible; and
- no technical result acquires automatic authority.

Costs and limitations:

- complete exact pins and provenance increase caller responsibility;
- no source authenticity, integrity, freshness, applicability, completeness,
  correctness, safety, or fitness is proven by the Definition itself;
- a timestamp without clock/reference provenance and policy evaluation proves
  no freshness;
- a digest without an explicit algorithm, exact subject bytes or separately
  governed canonicalization, and verification evidence proves no integrity or
  authenticity;
- restricted evidence may leave a dependent claim Unverifiable;
- model recollection may be stale, incomplete, or wrong;
- no concrete representation, schema, rule, policy, tool, implementation, or
  execution evidence exists; and
- preparation, promotion, validation, publication, and review are
  non-independent.

## Protected predecessors and historical integrity

This decision preserves without semantic or object change:

- ARCH-001 through ARCH-037 and ADR-0001 through ADR-0037;
- CONTRACT-001 through CONTRACT-009;
- all ten Accepted Schema Versions `1.0.0` and historical Test Manifests;
- the exact `203/38/165`, `957/948/9`, and `9/1` inventories;
- all thirteen Cross-Record Integrity Rules;
- the Accepted Tool and Implementation identities and Version `1.0.0` pins;
- Package E and practice inputs, execution records, outcomes, limitations,
  adverse/restricted evidence, and non-independent review boundaries;
- issue #126, issue #128, and all historical issues, comments, reviews, PRs,
  commits, trees, blobs, settings, tags, Releases, and evidence; and
- final-human-authority semantics.

## Explicit non-decisions and non-execution

ARCH-038 creates no Profile, concrete representation, property, schema,
Schema Resource, testcase, rule, Tool/Implementation Version, dependency,
Python, code, runner, execution, evidence instance, workflow, CI, setting
change, release, tag, GitHub Release, publication, distribution, support,
certification, hosting, or deployment.

It performs no source retrieval, network access, discovery, redirect following,
digest verification, clock verification, policy evaluation, derivation,
schema validation, integrity evaluation, implementation test, adversarial test,
evidence production, correction, withdrawal, deprecation, supersession,
release action, or deployment action.

Exact-head acceptance and this status promotion do not by themselves integrate
the Definition, allocate its Identifier, or activate Version `1.0.0`.
Separately governed integration is required for those exact integration and
activation effects. ARCH-038 does not reserve a Profile, grant merge
permission, close issue #128, authorize branch cleanup, or authorize a
follow-on phase.

## Final-human authority and stopgate

This Accepted document did not approve itself. Exact-head acceptance is
recorded in attributable EIGENAAR / Final Authority comment `5252557346`.
Issue-contract acceptance, candidate preparation, repository presence, the
status-promotion commit, static validation, Ready-for-review, transparent
non-independent ARCHITECT review, mergeability, technical access, and
implementation recognition do not by themselves integrate the decision,
activate the Definition, or grant consequential authority.

Work stops at a new attributable EIGENAAR / Final Authority gate for the exact
reviewed promotion head. Integration, completion, issue closure, branch
cleanup, and every later phase require separate express authority.

## References

- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Extension Module and Profile Identity and Version Policy](extension-module-profile-identity-version-policy.md)
- [Extension Module and Profile Dependency, Activation, Composition and Conflict Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [Extension Module and Profile Schema Resource, Packaging and Declaration Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [Extension Module and Profile Executable Schema and Validation/Conformance Boundary](extension-module-profile-executable-schema-validation-conformance-boundary.md)
- [Extension Module and Profile Tooling and Implementation Boundary](extension-module-profile-tooling-implementation-boundary.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Portable Conformance Evidence Boundary](portable-conformance-evidence-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0038](adr/0038-epistemic-provenance-freshness-extension-module-definition.md)
