# ADR-0040: CNTX Epistemic Provenance and Freshness Extension Module JSON Representation Boundary

- **Status:** Accepted
- **Date:** 2026-08-11
- **Issue:** [#139](https://github.com/CNTX-PROJECT/CNTX/issues/139)
- **Issue-contract acceptance comment:** [5259097128](https://github.com/CNTX-PROJECT/CNTX/issues/139#issuecomment-5259097128)
- **Exact-head acceptance comment:** [5259328712](https://github.com/CNTX-PROJECT/CNTX/issues/139#issuecomment-5259328712)
- **Accepted candidate:** commit
  `60d815ed9545c5ab16a4531df9a83cc00ed65340`, tree
  `4671ec2dac4df5029dddaaa5876375ba2b7b749d`
- **Baseline:** commit `67e04ad50d9563b7942c4f402841417391a72ac4`, tree `89b7a2610d43684d6e48fc8455ad2480d0055ab7`
- **Decision:** ARCH-040 — CNTX Epistemic Provenance and Freshness Extension
  Module JSON Representation Boundary

## Context

Accepted ARCH-038 defines one Epistemic Provenance and Freshness Extension
Module Definition with exact Identifier and Version `1.0.0`. It keeps source
category, exact source identity/revision, availability, provenance,
authenticity, integrity, four temporal coordinates, freshness/applicability,
clock/reference provenance, derivation, validation, evidence, conditions,
outcomes, limitations, and authority separate. It also preserves closed supply,
fail-closed behavior, non-aggregation, adverse/restricted evidence, and
`automaticAuthority: false`.

ARCH-038 deliberately creates no property, token, object shape, payload,
representation, schema, rule, implementation, or execution. Accepted ARCH-031
and ARCH-032 require concrete representation, Definition Schema Resource,
assertions, cases, fixed expected results, validation, and implementation to
remain separately governed. An executable schema cannot reliably validate a
target shape that has not first been explicitly defined.

Phase 4A3 must therefore begin with a representation boundary for the general
Module. The Context Packet Profile remains a later narrowing-only dependency,
and existing Core Artifact JSON and schemas remain immutable.

## Decision

Accept one closed JSON-compatible instance-data model for one bounded
declaration record about one exact primary source subject governed by:

- Definition Identifier
  `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness`;
- Definition Version `1.0.0`; and
- category `CNTX Extension Module Definition`.

No separate Representation Identifier or Version is allocated. No
Serialization Binding is selected. The model is subordinate to ARCH-038 and is
the Accepted target boundary for a later separately governed Module Definition
Schema Resource.

### Closed root

Define exactly thirteen lower-camel-case root properties:

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

All thirteen root properties are present. Conditional applicability is
represented through explicit condition declarations, not silent omission,
`null`, empty values, processor defaults, or fallback. Root and subordinate
objects are closed. Unknown properties, vendor members, wildcard namespaces,
and extension bags are prohibited.

### Exact source categories

Serialize the six ARCH-038 categories as exactly:

- `governing-source`;
- `observation-source`;
- `evidence-source`;
- `derived-source`;
- `human-assertion-source`; and
- `model-recollection-source`.

Multiple categories are permitted only with separately declared roles and
claim boundaries. Order creates no precedence. Restricted, inaccessible,
conflicting, missing, and unverifiable remain conditions, not categories.
Unknown or unsupported supplied categories are not mapped to a seventh token;
their public-safe supplied value remains visible as adverse condition input and
dependent favorable claims are blocked.

### Exact information conditions

Serialize the eight separate conditions as exactly:

- `specified`;
- `assessed-none`;
- `not-assessed`;
- `missing`;
- `inaccessible`;
- `conflicting`;
- `restricted`; and
- `unverifiable`.

Each condition remains bound to its exact dimension, subject, explanation,
evidence references, responsible roles, limitations, and dependent claim
effects. Assessed None is not Missing; Not Assessed is not Assessed None;
Inaccessible is not absent; Restricted is not proof; and Unverifiable is not
Not Satisfied.

### Existing evaluation outcomes

Reuse only the existing ARCH-024 tokens:

- `satisfied`;
- `not-satisfied`;
- `unverifiable`; and
- `not-evaluated`.

Every evaluation remains dimension- and subject-specific and preserves exact
governing pins, policies, evidence, evaluator context, observation/reference
time, limitations, adverse/restricted information, roles, authority, and
non-execution. Define no aggregate outcome property, score, weighting,
majority, traffic light, grade, badge, threshold, recommendation, approval,
certification, release fitness, deployment fitness, or consequential
authority.

### Source, claim, and provenance responsibilities

Require exact governing Definition pins, declaration identity/revision, one
exact primary source identity/revision or explicit unfavorable condition,
source locations as provenance only, separate availability, exact material
subject boundary, bounded claims and dimensions, origin, custody, acquisition,
observation, supply, transformation, responsible roles, limitations, adverse
information, and public-safe restricted metadata.

A mutable URL, branch, alias, `latest`, `current`, search result, filename,
cache item, repository position, installation, or previous use cannot replace
an exact revision pin. Location is not identity. Availability is not
authenticity. Provenance is not truth or authority.

### Temporal, digest, policy, and clock responsibilities

Keep exactly four temporal coordinates separate:

- `sourcePublicationRevisionTime`;
- `observationRetrievalTime`;
- `recordProductionTime`; and
- `validThroughTime`.

Every supplied coordinate preserves the exact value, reference identity and
revision where available, offset, precision, resolution/uncertainty/skew,
source/provenance, and attributable role. No coordinate is inferred from
another. This decision selects no timestamp syntax, calendar profile, default
timezone, clock service, threshold, tolerance, duration, or comparison rule.

Every digest claim preserves exact algorithm identity, digest value, exact
subject bytes or separately governed canonicalization reference, source
revision/acquisition context, verification procedure, observation time,
responsible role, separate outcome reference, evidence, failures, limitations,
and adverse/restricted information. Select no algorithm, encoding,
canonicalization, signature, certificate, trust store, attestation, or
verification implementation.

Keep freshness and applicability policy pins separate. Every specified policy
preserves exact identifier/version, authoritative source/revision, task/source
applicability coordinates, temporal inputs, assessment reference basis,
condition boundary, roles, evidence, limitations, and evaluation reference.
No ambient, provider/product-selected, newest, cached, `latest`, or fallback
policy is permitted.

### Derivation responsibilities

For `derived-source`, require one finite closed acyclic derivation declaration
with exact upstream source pins/categories/access conditions, transformation
identity/revision pins, responsible roles, material parameters, order,
input/output relationships, omissions, filtering, redaction, aggregation,
interpretation, loss, propagated or introduced uncertainty, digest references,
conditions, claims, evidence, limitations, and authority.

Create no transformation vocabulary, operation semantics, processor, graph
engine, execution, or proof that meaning, authenticity, integrity,
completeness, freshness, or applicability was preserved.

### Limitations and authority

Keep scope, method, evidence, access, security/privacy, resource, adverse,
restricted, unknown/unsupported, and non-executed limitations visible and
bound to affected subjects and claims. Restricted public-safe metadata never
replaces protected content.

Represent attributable declaring, supplying, evaluating, reviewing,
governing, and final-human-authority roles as opaque bounded references. Create
no person/account system, credential, authentication, authorization,
signature, delegation, voting, approval, or identity-verification mechanism.

Preserve `automaticAuthority: false` as a controlling semantic invariant, not
a serialized property. Technical results never become self-acceptance, merge,
release, deployment, or final-human authority.

### Core, placement, and activation boundary

Keep this representation separate from every existing Artifact Instance,
Common Artifact Envelope, Core payload/schema, Core Artifact JSON
Serialization Binding, Governing Definition Declaration, package, bundle,
activation mechanism, and the ten-schema Tool/Implementation supported set.

Add no property to Context Packet Schema Version `1.0.0`. Define no Context
Packet attachment or Profile binding. ARCH-039 remains a separate later
narrowing-only representation task.

Representation or repository presence activates nothing. URI-shaped values
grant no network/retrieval authority. Core-invalid input cannot become
Core-valid. Document, member, array, package, insertion, lexical, or processing
order creates no precedence or conflict resolution.

## Consequences

Positive consequences:

- ARCH-038 receives one inspectable target shape before schema design;
- separate source, temporal, policy, digest, derivation, condition, evaluation,
  limitation, and authority meanings remain explicit;
- missing or unfavorable information cannot be hidden by property omission or
  defaults;
- existing Core JSON and schemas remain unchanged;
- a later schema can enforce an explicit model rather than invent one; and
- no aggregate or automatic authority is introduced.

Costs and limitations:

- the explicit closed model is verbose;
- callers must supply exact pins, provenance, conditions, limitations, and
  roles rather than ambient context;
- timestamp syntax, policy vocabularies, digest methods, resource bounds,
  schemas, tests, bindings, and implementations remain unresolved;
- structural completeness cannot prove truth, authenticity, integrity,
  freshness, applicability, correctness, security, privacy, support, or
  fitness;
- preparation and review are non-independent; and
- no implementation or adversarial execution evidence exists.

## Alternatives not selected

### Build the schema before defining the representation

Not selected because ARCH-038 creates no target shape and requires concrete
representation and schemas/cases through separate gates.

### Add fields directly to Context Packet

Not selected because the general Module must remain reusable and the
Context Packet Profile is a later separate narrowing-only decision. Existing
Core schema and contract versions are immutable.

### Use open vendor extension members

Not selected because unknown members, ambient namespaces, and fallback weaken
closed supply, exact meaning, fail-closed processing, and deterministic review.

### Collapse condition and outcome into one status

Not selected because information availability/quality and evaluation result
are separate dimensions with distinct evidence and claim effects.

### Select default time, policy, or digest mechanisms

Not selected because ARCH-038 intentionally creates no timestamp syntax,
default timezone, policy instance, threshold, digest algorithm,
canonicalization, clock service, or comparison implementation.

### Use model recollection to repair missing values

Not selected because model recollection remains visible, non-governing, and
possibly stale, incomplete, or wrong.

## Protected predecessors and historical integrity

Preserve ARCH-001 through ARCH-039, ADR-0001 through ADR-0039, all Artifact
Contracts, identities, versions, ten Accepted Schema Resources, twenty
historical schema/test JSON files, five practice JSON files, `203/38/165`,
`957/948/9`, `9/1`, thirteen integrity rules, Tool/Implementation contracts,
Package E/practice evidence, H2.4, immutable release objects, settings,
ruleset, limitations, adverse/restricted evidence, and every historical
authority record unchanged.

## Non-decisions and non-execution

Accepted status creates no Representation Identifier/Version, Serialization
Binding, Schema Identifier/Version, `$id`,
Schema Resource, schema file, assertion, testcase, expected result, fixture,
policy identity/version, digest algorithm, timestamp syntax, rule, diagnostic
vocabulary, Tool/Implementation version, dependency, Python, code, runner,
execution, output, evidence instance, workflow, CI, release, publication,
support, certification, hosting, deployment, merge, issue closure, branch
cleanup, or later Phase 4A3 authority.

It performs no retrieval, network access, source resolution, policy
evaluation, time comparison, digest verification, transformation, validation,
testing, evidence production, release, or deployment.

## Authority boundary

Issue #139, attributable issue-contract acceptance comment `5259097128`, and
exact-head acceptance comment `5259328712` govern this Accepted decision.
Acceptance is bound to candidate commit
`60d815ed9545c5ab16a4531df9a83cc00ed65340` and tree
`4671ec2dac4df5029dddaaa5876375ba2b7b749d`. The preceding Proposed status,
candidate preparation, repository presence, validation, Draft PR state,
transparent non-independent COMMENT review, mergeability, parsing, or
implementation recognition did not accept, activate, integrate, or release
ARCH-040.

Status promotion, Ready-for-review, review, repository presence, and
mergeability do not integrate or activate ARCH-040. Merge, issue closure,
branch cleanup, Module Schema Resource work, Profile representation,
implementation, release, publication, support, certification, hosting,
deployment, and every later phase require separate authority.
