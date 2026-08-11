# CNTX Context Packet Epistemic Provenance and Freshness Profile Definition (ARCH-039)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only Profile Definition governed by
[issue #130](https://github.com/CNTX-PROJECT/CNTX/issues/130) and recorded by
[ADR-0039](adr/0039-context-packet-epistemic-provenance-freshness-profile-definition.md).
Attributable EIGENAAR / Final Authority issue-contract acceptance is recorded
in issue comment
[5254030218](https://github.com/CNTX-PROJECT/CNTX/issues/130#issuecomment-5254030218).
Exact-head EIGENAAR / Final Authority acceptance is recorded in issue comment
[5255793839](https://github.com/CNTX-PROJECT/CNTX/issues/130#issuecomment-5255793839)
on candidate commit `4e0af44a238713f41692ce864b9f3616ff39c4c9` and tree
`927ca72b1f692a045f1746ba800e699d9ee14576`.

Issue-contract acceptance, candidate preparation, status promotion, branch or
repository presence, static validation, review, mergeability, URL availability,
and Ready-for-review state do not by themselves integrate this Definition,
allocate its Profile Definition Identifier, activate its initial Profile
Definition Version, create a Profile instance, or grant consequential
authority. Exact-head attributable EIGENAAR / Final Authority acceptance has
occurred. Separately governed integration to `main` remains required for the
Definition allocation and activation effects.

## Purpose and decision boundary

CNTX has an Accepted Context Packet Contract Definition and an Accepted
Epistemic Provenance and Freshness Extension Module Definition. This Accepted
Profile Definition selects and narrows only capabilities already present in
those two exact Accepted subjects for the bounded preparation and assessment of
one Context Packet under one exact approved Task Contract revision.

The Profile addresses a specific risk: material sources can be listed in a
Context Packet without making their claim role, exact revision, provenance,
temporal basis, applicable freshness policy, digest boundary, derivation, or
unfavorable information conditions sufficiently explicit for a bounded later
assessment. The Profile does not decide that a source is authentic, fresh,
complete, applicable, trustworthy, safe, or fit for execution.

This Definition creates no representation, property, token, schema, Schema
Resource, policy instance, rule, testcase, validator, tool, implementation,
execution, evidence instance, release, publication, support, certification,
hosting, or deployment.

## Exact acceptance basis

This Definition was prepared on exact public baseline commit
`affa8d154cdfd5da1f83c9f90f3b2518439bb9bf` and tree
`e89dabd2a99a072ec25e6b8b793948b68a034189`.

Its controlling Accepted basis includes:

- ARCH-001 through ARCH-038 and ADR-0001 through ADR-0038;
- especially ARCH-028 through ARCH-033 for Profile category,
  identity/version, exact subjects, dependency, activation, composition,
  conflict, resources, validation, conformance, tooling, and implementation;
- the Accepted Context Packet Contract Definition, Identifier
  `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet`,
  Version `1.0.0`;
- the Accepted Epistemic Provenance and Freshness Extension Module Definition,
  Identifier
  `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness`,
  Version `1.0.0`;
- all nine Accepted artifact contracts, ten Accepted Core Schema Versions,
  ten historical Test Manifests, exact `203/38/165`, `957/948/9`, and `9/1`
  inventories, and thirteen Accepted Cross-Record Integrity Rules;
- the Accepted Tool and Implementation identities and Version `1.0.0` pins;
- the completed Package E and bounded practice evidence, including every
  limitation and `automaticAuthority: false`; and
- immutable prerelease `0.1.0-prealpha.1`, tag `v0.1.0-prealpha.1`, immutable
  GitHub Release `367290932` / `RE_kwDOTsnR984V5Go0`, ruleset `20518984`,
  disabled Actions, current security settings, and all historical authority
  records.

## Definition subject

| Dimension | Exact Accepted value |
| --- | --- |
| Definition category | CNTX Profile Definition |
| Local name | `context-packet-epistemic-provenance-freshness` |
| Profile Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/profile-definitions/context-packet-epistemic-provenance-freshness` |
| Initial Profile Definition Version | `1.0.0` |
| Lifecycle status | Accepted |

The Identifier is an opaque, version-independent logical identifier. It grants
no dereferencing, discovery, retrieval, redirect, registry, catalog, network,
trust, support, or authority semantics. Profile Definition Version is a
separate exact pin.

The preceding Proposed status consumed no version. Candidate preparation,
status promotion, repository presence, path, filename, review,
Ready-for-review, mergeability, implementation recognition, or product use do
not by themselves allocate or activate anything. Exact-head acceptance plus
separately governed integration to `main` allocates and activates only the exact
Identifier and Version above. No other Profile identity or version is created
or reserved.

## Exact Profile Subjects

This Accepted Profile has exactly two Profile Subjects:

1. Context Packet Contract Definition Identifier
   `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet`,
   Contract Definition Version `1.0.0`;
2. Epistemic Provenance and Freshness Extension Module Definition Identifier
   `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness`,
   Extension Module Definition Version `1.0.0`.

A Profile Subject is an exact logical identified/versioned basis. It is not a
schema reference, Artifact Instance relation, retrieval instruction,
dependency range, permission, compatibility claim, support claim, or evidence
of activation.

The Profile has no Profile dependency, creates no Extension Module dependency,
selects no other Core artifact contract, and cannot make Core depend on this
Profile. A different subject Identifier or Version is a different governing
context and cannot be substituted silently.

## Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
express requirement strength inside this Accepted Definition. They create no
representation, processor, implementation, execution permission, acceptance,
or consequential authority.

## Profile sovereignty and narrowing-only composition

This Profile MAY only select, require, limit, or narrow capabilities already
present in its two exact pinned Accepted Profile Subjects. It MUST NOT:

1. invent, extend, weaken, replace, reinterpret, repair, coerce, default, or
   override a governing capability;
2. make a Core-invalid representation Core-valid;
3. change an Accepted identity, version, field, token, schema assertion,
   testcase, expected result, binding, rule, Tool/Implementation contract,
   evidence record, or authority boundary;
4. neutralize a conflict or make conflicting Profile constraints optional;
5. select another Definition Version through a range, alias, `latest`,
   repository position, availability, popularity, or implementation choice;
6. turn Missing, Inaccessible, Conflicting, Restricted, adverse,
   insufficient, unsupported, or Unverifiable information into proof; or
7. bypass attributable final-human authority.

All applicable constraints from the Context Packet Contract Definition,
ARCH-038, and every other separately active compatible Profile apply
conjunctively. Profile order creates no precedence. Conflict, ambiguity, or an
unsatisfied prerequisite MUST remain visible and fail closed for every
dependent favorable claim.

## Bounded Context Packet application

For one Context Packet prepared under one exact approved Task Contract
revision, this Profile requires the following logical responsibilities.

### Materiality, claim roles, and categories

Every source material to packet selection, execution context, safety,
validation, evidence, review, or acceptance MUST have an explicit bounded claim
role. Materiality MUST be stated relative to the exact Task Contract revision
and packet boundary; it MUST NOT be inferred from retrieval order, file
location, recency, popularity, model attention, or implementation preference.

Every material source MUST declare one or more separately applicable logical
ARCH-038 source categories. Multiple roles MUST remain separate and
independently assessable. Category order creates no authority or precedence.

### Exact source identity and revision

Every material source MUST preserve an exact source identity and an exact
revision or version appropriate to its governing context. When a reliable
exact revision or version cannot be established, the packet MUST preserve an
explicit non-favorable information condition and its effect on dependent
claims.

A mutable alias, branch, `latest`, `current`, search result, filename, cache,
repository position, product setting, installation state, or prior successful
use MUST NOT replace an exact revision/version pin.

### Separate epistemic dimensions

Source availability, provenance, authenticity, integrity, freshness,
applicability, completeness, validation, evidence, acceptance, authority,
support, release, and deployment MUST remain separate. No one dimension
substitutes for or proves another.

Availability is not authenticity; authenticity is not integrity; integrity is
not freshness; freshness is not applicability; applicability is not
correctness; validation is not acceptance; evidence is not approval; and
implementation support is not normative authority.

### Separate temporal coordinates

Source Publication/Revision Time, Observation/Retrieval Time, Record
Production Time, and optional Valid-Through Time MUST remain distinct. One
coordinate MUST NOT be inferred from or used to repair another.

Every asserted coordinate MUST preserve its source, time reference, timezone
or offset, precision, uncertainty, and clock/reference provenance. A timestamp
without those boundaries proves no freshness or currentness.

### Freshness and applicability policy

Every consequential freshness or currentness claim MUST pin:

1. an exact freshness/applicability policy identity and version;
2. the declared task or source class to which the policy applies;
3. the exact source identity, revision/version, and source category;
4. the temporal coordinates used and their clock/reference provenance;
5. the assessment reference time;
6. the policy conditions actually assessed;
7. evidence, individual outcome, diagnostics, and limitations;
8. adverse or restricted information and non-execution; and
9. claimant and governing authority.

Policy identity is not policy content. Policy version is not applicability.
Applicability is not freshness. Missing or ambiguous exact policy or
applicability basis makes a dependent favorable freshness claim
`Unverifiable` or `Not Evaluated`, never `Satisfied`.

This Profile selects no policy identity, representation, task/source-class
vocabulary, duration, threshold, comparison rule, tolerance, grace period, or
default reference time.

### Digest-bounded integrity claims

Every digest material to an integrity claim MUST preserve its exact algorithm,
value, subject bytes or separately governed canonicalization, source revision,
comparison procedure, observation provenance, responsible role, evidence,
individual outcome, and limitations.

There is no default digest algorithm or canonicalization. A digest without an
explicit algorithm and exact subject boundary proves no integrity. A digest
match proves no authenticity, semantic equivalence, freshness, safety, trust,
authority, support, or fitness.

### Closed derivation chains

Every Derived Source material to the packet MUST preserve a finite, closed,
caller-supplied derivation chain. The chain MUST identify exact upstream source
identities/revisions/categories, observations, temporal coordinates,
transformations and their identities/revisions, material parameters, order,
input/output relations, omissions, redactions, aggregation, loss, uncertainty,
adverse/restricted conditions, claim boundaries, evidence, and limitations.

Cycles, missing material inputs or transformations, conflicting sources,
unsupported mechanisms, restricted dependencies, or insufficient provenance
MUST block dependent favorable claims. Derivation transfers no governing
authority and proves no authenticity, integrity, completeness, freshness,
applicability, correctness, or semantic preservation.

### Model recollection

Model Recollection Source MUST remain visible, attributable to its production
context where available, non-governing, and explicitly possibly stale,
incomplete, or wrong. It MUST NOT replace a Governing Source, exact source
revision, retrieval evidence, policy pin, validation evidence, or human
decision.

### Information conditions and outcomes

Specified, Assessed None, Not Assessed, Missing, Inaccessible, Conflicting,
Restricted, and Unverifiable information conditions MUST remain distinct.
They MUST NOT be collapsed into generic pass, warning, failure, or unknown.

Where a separately authorized evaluation applies, `Satisfied`,
`Not Satisfied`, `Unverifiable`, and `Not Evaluated` MUST remain separate for
each exact subject, dimension, requirement, and policy. An information
condition is not automatically an evaluation outcome.

This Profile creates no aggregate pass/fail, valid result, traffic light,
score, grade, badge, threshold, rubric, quality gate, recommendation, approval,
certification, release fitness, deployment fitness, or consequential authority.

### Restricted and adverse information

Restricted is an access/disclosure condition, not a favorable evidence state
or seventh source category. A required restricted source MAY be represented
publicly only through the minimum authorized public-safe metadata needed to
preserve its existence, role, governing restriction, claim effect, and
limitation. Restricted content MUST NOT be copied, exposed, reconstructed, or
treated as favorable evidence.

Adverse, incomplete, contradictory, inaccessible, restricted, or uncertain
information MUST remain visible at its exact affected claim boundary. It MUST
NOT be omitted to improve an outcome.

### Fail-closed unknown and unsupported inputs

Unknown or unsupported source categories, Definition Versions, policies,
temporal mechanisms, digest mechanisms, derivations, evaluator capabilities,
or resource requirements MUST remain visible and fail closed for every
dependent favorable claim.

No discovery, network retrieval, redirect, registry, catalog, cache, newest-
wins selection, substitution, coercion, defaulting, repair, retry, fallback,
majority, consensus, score, or ranking may silently resolve them.

### Result and authority traceability

Every separately produced result governed by this Profile MUST preserve its
exact subject, dimension, governing sources and exact pins, applicable policy,
evidence, observation and assessment times, limitations, adverse/restricted
information, non-execution, claimant, reviewer where applicable, and governing
authority.

The logical assertion `automaticAuthority: false` remains fixed. It describes
a non-authority invariant and does not create a JSON property or executable
rule. Technical output never becomes self-acceptance, merge permission, release
approval, deployment approval, or final-human authority.

## Activation, supply, and conflict boundary

Consequential use of a future Accepted version of this Profile would still
require a separately Accepted declaration/activation representation and one
exact, closed, caller-supplied, frozen governing context under ARCH-030 and
ARCH-031. Repository, URL, package, installation, processor, product, cache,
or prior-execution presence activates nothing.

Supply MUST remain explicit, bounded, offline-first, and identity preserving.
This Definition authorizes no source retrieval, network access, discovery,
redirect following, mutable alias, registry, automatic policy/version
selection, fallback, substitution, repair, or silent downgrade.

## Representation, schema, rule, and implementation boundary

This Accepted Definition creates no:

- JSON property, value, enum, object shape, payload, declaration syntax, media
  type, Serialization Binding, package, bundle, or Governing Definition
  Declaration representation;
- Profile instance, Context Packet Artifact Instance, Definition instance,
  Extension Module instance, new Artifact Type, or new Artifact Instance;
- schema identifier or version, `$id`, Schema Resource, executable schema,
  assertion, manifest, testcase, expected-validity declaration, fixture, or
  scenario matrix;
- source-category token, timestamp syntax, calendar profile, policy instance,
  task/source-class vocabulary, duration, threshold, comparison rule,
  tolerance, digest algorithm, canonicalization, clock service, or derivation
  serialization;
- rule identity/version, rule representation, evaluation-record shape,
  diagnostic code, severity, output vocabulary, or conformance claim;
- Tool Identity/Version, Implementation Identity/Version, dependency, library,
  SDK, CLI, API, workflow, CI, runtime, provider, product, hosted service,
  registry, support, certification, release, or deployment; or
- execution, validation output, Portable Conformance Evidence, Evidence Bundle,
  Review Record, Decision Record, release record, or other evidence instance.

Concrete representation, schemas and cases, policies, evaluation rules,
Tool/Implementation capability versions, implementation, practice, and
evidence each require later separate governance.

## Security, privacy, and resource boundary

A Context Packet governed by this Profile SHOULD minimize source content and
metadata to the exact approved task and claim boundary. It MUST preserve access
restrictions, confidentiality, data minimization, purpose limitation,
retention, deletion, licensing, disclosure, and audit constraints from its
governing sources and Task Contract.

Exact identity and provenance requirements do not authorize disclosure.
Digests are not automatically non-sensitive. Timestamps, source locations,
revision identifiers, derivation details, diagnostics, and combinations of
otherwise public metadata may be sensitive and require minimization.

Resource exhaustion, insufficient memory or storage, input count or depth
limits, derivation expansion, policy complexity, unavailable resources,
unsupported mechanisms, and interrupted evaluation MUST remain visible. They
MUST NOT be converted into a favorable result.

## Evidence, review, and claim boundary

This Definition states logical responsibilities but performs no retrieval,
freshness assessment, digest verification, clock verification, derivation
verification, validation, execution, or evidence production.

Future evidence MUST remain bound to one exact subject, revision, Definition
Version, policy, execution context, observation time, method, claimant,
limitations, adverse/restricted information, and authority. Repository
presence, a valid link, a schema result, or one successful execution proves no
broader conformance, correctness, support, release fitness, or deployment
fitness.

Candidate preparation, validation, publication, and ARCHITECT review are
non-independent. They are not independent assurance, certification, or final
acceptance.

## Compatibility, lifecycle, and change

Compatibility MUST be claimed separately for exact Profile Subject versions,
Profile Definition Version, representation, policies, rules, Tool and
Implementation capabilities, evidence, and operating context. No compatibility
range, backward-compatibility promise, support window, maintenance promise, or
automatic migration is created here.

When separately governed integration to `main` occurs, exact-head acceptance
and integration together allocate and activate the exact Identifier and Version
above as an immutable Accepted Definition subject. Correction, withdrawal,
deprecation, supersession, replacement, or a later Version requires separate
governance and must preserve historical provenance.

## Consequences and limitations

Positive consequences of this Definition are:

- Context Packet material sources receive explicit bounded roles and exact
  categories;
- exact source identity/revision and unfavorable pinning conditions remain
  visible;
- epistemic and authority dimensions cannot be silently collapsed;
- four temporal coordinates and their clock/reference provenance remain
  separate;
- freshness claims require an exact applicable policy and evidence;
- digest claims require an explicit algorithm and exact subject boundary;
- derived material retains a closed upstream/transformation chain;
- model recollection remains visible and non-governing;
- restricted and adverse information cannot silently become proof; and
- individual outcomes never acquire aggregate or automatic authority.

Costs and limitations are:

- callers bear the cost of supplying exact pins, roles, provenance, policies,
  temporal context, derivations, evidence, limitations, and authority;
- the Definition proves no source authenticity, integrity, freshness,
  applicability, completeness, correctness, safety, trust, minimality, or
  execution fitness;
- timestamps without clock/reference provenance and exact policy evaluation
  prove no freshness;
- digests without explicit algorithm, exact subject boundary, and verification
  evidence prove no integrity or authenticity;
- restricted evidence may leave dependent claims Unverifiable;
- model recollection may be stale, incomplete, or wrong;
- non-independent preparation and review provide no independent assurance; and
- no representation, schema, policy, rule, implementation, adversarial
  execution, or evidence instance exists for this Accepted Profile.

## Protected predecessors and historical integrity

This acceptance changes no preceding Accepted architecture, ADR, contract, Definition,
Representation, Schema Resource, schema, testcase, expected-validity result,
binding, rule, Tool/Implementation identity or version, evidence, release,
setting, tag, limitation, adverse/restricted condition, or historical authority
record.

It preserves exact `203/38/165`, `9/1`, and `957/948/9` inventories, the seven
issue-#126 frozen pins, all completed Package E and practice evidence, and the
immutable prerelease and GitHub Release unchanged.

## Explicit non-decisions and non-execution

This Accepted Definition makes no Profile instance, concrete representation,
schema, Schema Resource, testcase, rule, policy instance, Tool/Implementation
Version, dependency, Python, code, runner, execution, evidence instance,
workflow, CI, setting change, release, tag, GitHub Release, publication,
distribution, support, certification, hosting, deployment, merge, issue
closure, branch cleanup, or follow-on decision.

It performs no source access, retrieval, network operation, policy evaluation,
digest verification, clock verification, transformation, validation, testing,
evidence production, release action, or deployment.

## Final-human authority and stopgate

`automaticAuthority: false` remains fixed. Exact-head EIGENAAR / Final
Authority acceptance comment `5255793839` accepts candidate commit
`4e0af44a238713f41692ce864b9f3616ff39c4c9` and tree
`927ca72b1f692a045f1746ba800e699d9ee14576`. This status promotion records the
Accepted lifecycle. Preparation, status promotion, static validation,
transparent non-independent ARCHITECT review, branch or repository presence,
mergeability, and Ready state do not by themselves grant integration authority.

Work stops after status promotion, publication, review, and verification at a
new attributable EIGENAAR / Final Authority integration gate bound to the exact
promotion commit and tree. Merge, Identifier/Version allocation or activation,
issue closure, branch cleanup, representation, schema, policy, rule, tooling,
implementation, execution, evidence, release, publication, support,
certification, hosting, deployment, and every later phase require separate
express authority.

## References

- [Issue #130](https://github.com/CNTX-PROJECT/CNTX/issues/130)
- [ADR-0039](adr/0039-context-packet-epistemic-provenance-freshness-profile-definition.md)
- [Context Packet artifact contract](../contracts/context-packet-contract.md)
- [ARCH-028](extension-module-profile-architecture-boundary.md)
- [ARCH-029](extension-module-profile-identity-version-policy.md)
- [ARCH-030](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [ARCH-031](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [ARCH-032](extension-module-profile-executable-schema-validation-conformance-boundary.md)
- [ARCH-033](extension-module-profile-tooling-implementation-boundary.md)
- [ARCH-038](epistemic-provenance-freshness-extension-module-definition.md)
