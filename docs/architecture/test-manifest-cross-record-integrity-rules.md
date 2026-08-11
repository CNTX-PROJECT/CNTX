# CNTX Test Manifest and Initial Cross-Record Integrity Rules Identity, Version, and JSON Representation (ARCH-036)

## In ordinary language

This decision describes how CNTX identifies test manifests, thirteen initial
cross-record integrity rules, and the separate result of evaluating each rule.
It preserves valid, invalid, unavailable, and genuinely inapplicable conditions
without compressing them into one score.

| Quick view | Meaning |
| --- | --- |
| **Status** | Accepted documentation-only architecture decision |
| **Main question** | How are test inputs, cross-record rules, and individual evaluation outcomes represented and kept separate? |
| **What this establishes** | Two historical manifest forms, thirteen versioned rules, separate evaluation records, four outcome categories, and non-aggregation |
| **What this does not do** | It changes no testcase, runs no rule, creates no aggregate pass/fail, proves no conformance, and grants no approval or release authority |

### Reading route

- [Purpose and boundary](#purpose-and-decision-boundary)
- [Test Manifest representation](#test-manifest-json-representation)
- [Current manifest inventory](#exact-current-manifest-inventory)
- [Rule representation](#cross-record-integrity-rule-json-representation)
- [Evaluation Record representation](#cross-record-integrity-evaluation-record-json-representation)
- [No aggregate authority](#no-aggregate-authority)

This visitor layer is non-normative and introduces no new requirement. The
complete Accepted text below remains controlling.

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only architecture decision governed
by public issue [#118](https://github.com/CNTX-PROJECT/CNTX/issues/118).
Attributable EIGENAAR / Final Authority issue-contract acceptance is recorded
in issue comment
[`5242339896`](https://github.com/CNTX-PROJECT/CNTX/issues/118#issuecomment-5242339896).
Exact-head acceptance of reviewed candidate commit
`8585ac2a04be1a2978b2f155065bc706638191e2` and tree
`fd369393b6b6687fc539a00c9677194e6944c693` is recorded in issue comment
[`5243304427`](https://github.com/CNTX-PROJECT/CNTX/issues/118#issuecomment-5243304427)
after transparent non-independent ARCHITECT COMMENT review `4898518876`.

The accepted issue body is pinned to public baseline commit
`5a50a7c8f19d6667c863a65299bff11a39cb29c3` and tree
`64ed51360d61c340bc32a53c847903c09c746aeb`, contains `23,930`
characters and `23,934` UTF-8 bytes, and has SHA-256
`f8a73ae5200e2e9ab28bbfd5537138ed6317d04670eb83c4166f48865a5f5cb1`.

Issue-contract acceptance, repository presence, validation, and transparent
non-independent review did not accept this decision. Exact-head acceptance is
separate and does not authorize execution, release, publication, support,
certification, hosting, or deployment.

## Purpose and decision boundary

CNTX has ten Accepted Schema Versions `1.0.0` and ten historical synthetic
test manifests containing exactly `203` cases: `38` expected-valid and `165`
expected-invalid. Nine manifests use direct complete instances. The State
Snapshot manifest uses a base instance and ordered operations.

Accepted ARCH-034 defines a Validation Execution Record. Accepted ARCH-035
defines a bounded Validation Evidence and Reproduction Package. Both retain
external and cross-record references as opaque pins. Neither defines the
existing test-manifest structures or a general cross-record integrity rule.

This decision proposes three distinct documentation contracts:

1. one Test Manifest Definition and JSON Representation that recognizes both
   historical construction forms without rewriting them;
2. one Cross-Record Integrity Rule Definition and JSON Representation for
   individually versioned bounded rules; and
3. one Cross-Record Integrity Evaluation Record Definition and JSON
   Representation for caller-supplied subjects, individual rule outcomes,
   diagnostics, limitations, evidence, claims, and authority.

This decision does not create an executable schema, manifest instance,
integrity-rule instance, evaluation-record instance, validator, resolver,
runner, graph engine, Tool, Implementation, workflow, CI configuration,
release, service, or deployment.

## Governing traceability

This candidate is subordinate to and preserves:

- ARCH-001 through ARCH-035 and ADR-0001 through ADR-0035;
- CONTRACT-001 through CONTRACT-009;
- the ten Accepted Schema Versions `1.0.0`;
- the ten historical synthetic test manifests and their exact Git objects;
- Core Artifact JSON Binding Version `1.0.0`;
- Accepted Schema Resource resolution and validation/output boundaries;
- the Accepted Validation Execution Record Definition and JSON
  Representation Version `1.0.0`;
- the Accepted Validation Evidence and Reproduction Package Definition and
  JSON Representation Version `1.0.0`;
- Accepted Portable Conformance Evidence, Extension Module/Profile, and
  Tooling/Implementation boundaries;
- immutable Release Version `0.1.0-prealpha.1`; and
- final human authority.

No statement here changes a predecessor, testcase, expected-validity value,
Schema Resource, release object, or historical Git/GitHub object.

## Terminology

**Test Manifest** means a non-normative JSON test-evidence document that pins
one Schema Resource and carries named expected-validity cases.

**Direct Case** means one case containing one complete `instance` value.

**Operation Case** means one case that deep-copies the manifest's
`baseInstance` and applies its ordered `operations`.

**Supplied Record Set** means the exact closed caller-supplied records and
revisions available to one bounded integrity evaluation.

**Integrity Rule** means one individually identified, versioned,
applicability-bound normative-contract assessment requirement. It is not code
and does not execute itself.

**Integrity Evaluation Record** means one non-Artifact Validation-layer record
of supplied inputs and individual rule outcomes. It is not a Validation
Execution Record, Evidence Bundle, Review Record, Decision Record, or
acceptance.

**Local Reference** means a reference whose target is required within one
supplied representation. **Cross-record Reference** means a reference from one
supplied record to another exact supplied record key and revision.

## Allocated logical identities and initial versions

Governed integration of this Accepted decision allocates and activates exactly
these independent pairs:

| Dimension | Accepted exact value |
| --- | --- |
| Test Manifest Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/definitions/test-manifest` |
| Test Manifest Definition Version | `1.0.0` |
| Test Manifest JSON Representation Identifier | `https://github.com/CNTX-PROJECT/CNTX/bindings/test-manifest-json` |
| Test Manifest JSON Representation Version | `1.0.0` |
| Cross-Record Integrity Rule Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-rule` |
| Cross-Record Integrity Rule Definition Version | `1.0.0` |
| Cross-Record Integrity Rule JSON Representation Identifier | `https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-rule-json` |
| Cross-Record Integrity Rule JSON Representation Version | `1.0.0` |
| Cross-Record Integrity Evaluation Record Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-evaluation-record` |
| Cross-Record Integrity Evaluation Record Definition Version | `1.0.0` |
| Cross-Record Integrity Evaluation Record JSON Representation Identifier | `https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-evaluation-record-json` |
| Cross-Record Integrity Evaluation Record JSON Representation Version | `1.0.0` |

The HTTPS-shaped identifiers are opaque identities, not retrieval authority.
They authorize no network access, redirect, discovery, registry lookup, hosted
content, or trust in content returned from a similar location.

Definition Identity, Definition Version, Representation Identity,
Representation Version, instance identity, revision, location, digest,
provenance, lifecycle, review, acceptance, release, and authority remain
separate dimensions. No dimension implies, allocates, selects, activates,
authenticates, accepts, approves, certifies, or proves another dimension.

## Classification

The three definitions are **Validation-layer contracts**. None is a tenth CNTX
Artifact Type. None uses or extends the Common Artifact Envelope's closed
nine-value `artifactType` enumeration. None is governed as CONTRACT-001 through
CONTRACT-009.

The existing ten manifests remain historical non-normative test evidence.
Recognition by this decision does not rewrite their bytes, convert them into
Artifact Instances, or prove that their expected-validity statements are
correct.

An Integrity Evaluation Record records one bounded assessment. It cannot
approve, accept, correct, merge, release, publish, support, certify, host,
deploy, or make a final-human decision.

## Common JSON document boundary

Each Accepted JSON Representation Version `1.0.0` is exactly one JSON text
containing exactly one root object.

Every representation MUST:

- use strict UTF-8 without a byte-order mark;
- contain no duplicate member names, comments, non-JSON values, or trailing
  non-whitespace bytes;
- preserve supplied strings, numbers, booleans, object members, array items,
  and operation order without coercion, repair, defaulting, normalization,
  substitution, or fallback;
- use exact case-sensitive property names and tokens;
- reject properties outside the applicable closed object; and
- treat array order as meaningful only where this decision says it is.

Parsing success proves only that a JSON value is available. Representation
success proves only the relevant representation dimension. Neither proves
expected validity, schema conformance, contract conformance, referential
integrity, truth, evidence sufficiency, review quality, acceptance, release
fitness, deployment fitness, or authority.

## Common scalar, digest, reference, and condition rules

Unless a closed token is defined:

- a string MUST contain at least one non-whitespace Unicode code point;
- identifiers, versions, revisions, keys, paths, and references are exact
  case-sensitive strings;
- an array declared unique MUST not contain duplicate JSON values;
- a count MUST be a non-negative integer;
- `null` MUST NOT stand for missing, ambiguous, conflicting, unsupported,
  restricted, unavailable, not-defined, or not-assessed information; and
- an explicit condition MUST be used where this decision permits one.

A digest object contains exactly `algorithm` and `value`. `algorithm` is
exactly `sha-256`; `value` is exactly 64 lowercase hexadecimal characters. A
digest binds only the declared bytes. It does not prove authenticity, trust,
currentness, correctness, acceptance, or authority.

An exact record reference contains exactly `recordKey`, `recordIdentity`, and
`recordRevision`. Where a digest is required it additionally contains
`contentDigest`. A matching string alone proves no target existence.

An explicit condition object contains exactly `condition`, `reason`, and
`provenanceReferences`. `condition` is exactly one of:

- `missing`;
- `duplicate`;
- `malformed`;
- `ambiguous`;
- `conflicting`;
- `unknown`;
- `unsupported`;
- `blocked`;
- `inaccessible`;
- `restricted`;
- `unverifiable`;
- `not-evaluated`;
- `not-defined`; or
- `not-applicable`.

An explicit condition is not a value, waiver, success, default, repair, or
permission to continue.

## Test Manifest JSON Representation

The Test Manifest JSON Representation recognizes exactly two root variants.
The variants are alternatives; a document matching both or neither is
`ambiguous` or `malformed` and fails closed.

Recognition does not alter the existing files. A later schema may encode these
rules only after a separate Accepted schema decision.

### Direct manifest variant

The direct variant contains exactly these required properties:

- `schemaId`;
- `candidateSchemaVersion`;
- `documentStatus`;
- `nonNormative`;
- `description`; and
- `cases`.

It MAY additionally contain `issue` and `ownerAcceptanceComment` because those
coordinates exist in some current direct manifests. No other root property is
permitted by this Accepted representation.

For the current historical set:

- `schemaId` is the exact supplied Schema Resource identifier;
- `candidateSchemaVersion` is exactly `1.0.0`;
- `documentStatus` is exactly `Accepted`;
- `nonNormative` is exactly `true`;
- `description` is non-blank; and
- `cases` is a non-empty ordered array.

Each direct case is a closed object containing exactly `name`, `valid`, and
`instance`. `name` is unique within that manifest, `valid` is a JSON boolean,
and `instance` is the complete JSON value supplied to a later evaluator.

### Operation-based State Snapshot manifest variant

The operation-based variant contains exactly:

- `schemaId`;
- `candidateSchemaVersion`;
- `documentStatus`;
- `active`;
- `nonNormative`;
- `issue`;
- `description`;
- `caseConstruction`;
- `baseInstance`; and
- `cases`.

For the current historical State Snapshot manifest,
`candidateSchemaVersion` is `1.0.0`, `documentStatus` is `Accepted`, `active`
is `true`, and `nonNormative` is `true`.

`caseConstruction` is a closed object containing exactly `method`,
`pointerSyntax`, `allowedOperations`, and `nonNormativeBoundary`.
`allowedOperations` contains exactly `add`, `remove`, and `replace` once each.
The declared pointer syntax is RFC 6901 JSON Pointer, and terminal `-` append
semantics apply only to `add` as already stated in the historical manifest.

Each operation case is a closed object containing exactly `name`, `valid`, and
`operations`. `name` is unique within the manifest, `valid` is a JSON boolean,
and `operations` is an ordered array.

Each operation object contains exactly `op` and `path`, plus `value` when the
operation requires supplied value material. `op` is exactly `add`, `remove`,
or `replace`. Operation ordering is significant. The logical construction is:

1. deep-copy the exact supplied `baseInstance`;
2. apply every operation in listed order; and
3. use the resulting JSON value as that case's constructed instance.

This describes the existing fixture representation. It does not select a JSON
Pointer library, patch library, mutation API, error-recovery behavior, runtime,
or implementation. An unknown operation, malformed path, missing required
value, prohibited extra value, failed operation, or ambiguous result is a
separate fail-closed construction condition.

## Exact current manifest inventory

The exact baseline contains these ten supplied manifests:

| Manifest subject | Cases | Expected valid | Expected invalid | Construction form |
| --- | ---: | ---: | ---: | --- |
| Common Artifact Envelope | 31 | 11 | 20 | direct |
| Context Packet | 20 | 3 | 17 | direct |
| Decision Record | 20 | 3 | 17 | direct |
| Evidence Bundle | 20 | 3 | 17 | direct |
| Execution Result | 20 | 3 | 17 | direct |
| Project Charter | 20 | 3 | 17 | direct |
| Review Record | 20 | 3 | 17 | direct |
| State Snapshot | 20 | 3 | 17 | operation-based |
| Task Contract | 16 | 3 | 13 | direct |
| Workstream | 16 | 3 | 13 | direct |
| **Total** | **203** | **38** | **165** | **nine direct, one operation-based** |

This table is a static baseline assertion. It is not evidence that any schema
or testcase was executed. A later evaluator MUST derive counts from the exact
supplied closed manifest set and compare them without silently correcting the
supplied values.

## Manifest identity, uniqueness, and counting

One supplied manifest is keyed by the exact tuple of its location, content
digest, `schemaId`, and `candidateSchemaVersion`. A duplicate or conflicting
tuple fails closed.

One case key is the exact pair of the supplied manifest key and case `name`.
Each unique case key is counted exactly once. Filename order, directory order,
JSON member order, discovery order, case popularity, or evaluation order MUST
NOT create identity or precedence.

An exact inventory contains separate manifest count, case count,
expected-valid count, expected-invalid count, and construction-form counts.
No total may conceal a duplicate, malformed, ambiguous, conflicting, unknown,
unsupported, blocked, inaccessible, restricted, unverifiable, or not-evaluated
manifest or case.

## Cross-Record Integrity Rule JSON Representation

One rule document has a closed root containing exactly eight properties:

1. `rule`;
2. `applicability`;
3. `requiredSubjects`;
4. `requirements`;
5. `outcomeBoundary`;
6. `evidenceBoundary`;
7. `processingBoundary`; and
8. `authorityBoundary`.

The closed `rule` object contains Definition and Representation identity/
version pins, one stable Rule Identifier, one Rule Version, lifecycle state,
exact governing-source references, and provenance. Rule Definition Version,
Rule Identifier, and Rule Version remain separate.

`applicability` defines the exact record kinds, versions, relationship kinds,
preconditions, exclusions, and not-applicable behavior. `requiredSubjects`
defines the minimum exact supplied-record roles without discovering them.

`requirements` is a non-empty ordered array of individually referenced
normative statements. Ordering is presentation only and creates no precedence.

`outcomeBoundary` contains exactly the four tokens `satisfied`,
`not-satisfied`, `unverifiable`, and `not-evaluated`, plus exact conditions for
their use. A rule has no fifth outcome and no aggregate result.

`evidenceBoundary` defines required supplied references, diagnostic and
limitation relations, adverse/restricted evidence handling, and claim limits.
It proves no source existence, authenticity, relevance, sufficiency, or
independence by declaration alone.

`processingBoundary` records caller-supplied, closed, frozen, offline-first,
bounded, deterministic, and fail-closed requirements. `authorityBoundary`
contains producer, reviewer, decision-maker, Final Authority, and
`automaticAuthority`, which MUST be exactly `false`.

## Allocated initial Rule Identities and Versions

Every Accepted initial rule has Rule Version `1.0.0` and an identifier under
`https://github.com/CNTX-PROJECT/CNTX/rules/cross-record/`.

| Rule child identifier | Separate responsibility |
| --- | --- |
| `supplied-record-exists` | The exact required record key resolves to one supplied record. |
| `identity-version-revision-complete` | Every applicable supplied record carries complete exact identity, version, and revision pins. |
| `record-key-unique` | Each supplied record key occurs exactly once. |
| `identity-revision-content-consistent` | Equal identity/revision claims do not carry conflicting content, digest, or provenance. |
| `reference-resolves-exactly-once` | Each applicable cross-record reference resolves to exactly one supplied target. |
| `task-context-execution-chain` | Exact Task Contract, Context Packet, and Execution Result pins form the required supplied chain. |
| `validation-record-subject-link` | A Validation Execution Record subject pin resolves to its exact supplied subject. |
| `evidence-package-execution-link` | A Package B execution-record pin resolves to the exact supplied Validation Execution Record. |
| `role-overlap-visible` | Material identity overlap among supplied role declarations is visible and attributable. |
| `review-independence-declared` | Applicable review independence or non-independence is explicit and source-pinned. |
| `self-review-prohibited` | An applicable executor does not act as its own required independent reviewer. |
| `self-acceptance-prohibited` | A producer, executor, or non-final reviewer does not grant final acceptance to its own work. |
| `automatic-authority-false` | Every applicable automatic-authority declaration is exactly `false`. |

These Accepted identifiers define no code, query, traversal, join algorithm,
graph representation, severity, threshold, precedence, evaluation order,
remediation, approval, or enforcement mechanism.

## Cross-Record Integrity Evaluation Record JSON Representation

One evaluation document has a closed root containing exactly nine required
properties and no others:

1. `evaluation`;
2. `governingContext`;
3. `suppliedRecords`;
4. `ruleDefinitions`;
5. `ruleResults`;
6. `diagnostics`;
7. `limitations`;
8. `claimBoundary`; and
9. `authorityBoundary`.

`evaluation` contains the Accepted Definition and Representation pins, stable
Evaluation Identifier, immutable Evaluation Revision, lifecycle state,
producer, production-time declaration or explicit condition, and digest.

`governingContext` contains exact repository commit/tree when applicable,
governing architecture/ADR/contract identities and revisions, applicable
Definition/Representation/Schema Resource pins, resource closure, evaluator
context, configuration, dependency/environment declarations when separately
defined, resource limits, network prohibition, provenance, and claim scope.
These declarations select or prove none of those dimensions.

`suppliedRecords` is the exact closed record set. Each item contains one unique
`recordKey`, exact kind, identity, version, revision, location or supplied-
content reference, digest when supplied, provenance, accessibility/restriction
condition, and claim boundary.

`ruleDefinitions` is the exact closed caller-supplied Rule Identifier/Version
set. A mutable alias, range, `latest`, discovery result, or implicit rule is
prohibited.

`ruleResults` contains exactly one result entry for every supplied rule and no
result for an unsupplied rule. Each entry contains:

- unique `ruleResultReference`;
- exact Rule Identifier and Rule Version;
- exact supplied subject record keys and revisions;
- applicability determination and basis;
- exactly one outcome when applicable, or one explicit `not-applicable`
  applicability condition and no outcome when inapplicable;
- requirement-level observations;
- resolved, dangling, duplicate, ambiguous, conflicting, unsupported,
  restricted, inaccessible, and unverifiable references as applicable;
- diagnostic, limitation, and evidence references;
- non-execution or blocked reason where applicable;
- exact bounded claim; and
- evaluator and provenance declarations.

The four outcomes are lowercase exact tokens:

- `satisfied`: every applicable requirement has sufficient supplied
  observation for this exact bounded claim and no material applicable failure
  or unverifiable condition remains;
- `not-satisfied`: at least one applicable requirement is observably not met;
- `unverifiable`: the outcome cannot be determined from the exact supplied
  material, including missing, inaccessible, restricted, ambiguous, or
  conflicting required evidence; or
- `not-evaluated`: the rule was applicable or potentially applicable but was
  not executed, including blocked, unsupported, resource-limited, or
  deliberately omitted evaluation.

No outcome is success authority. An inapplicable rule is represented by an
applicability decision and is not silently counted as `satisfied`.

## Cross-record referential integrity

Within one supplied evaluation context:

- each `recordKey` MUST be unique;
- each supplied identity/version/revision tuple MUST resolve consistently;
- each `ruleResultReference`, diagnostic reference, and limitation reference
  MUST be unique in its local collection;
- each required local reference MUST resolve exactly once;
- each applicable cross-record reference MUST resolve to exactly one supplied
  target record and exact revision;
- zero targets remains `dangling` or `missing` as applicable;
- more than one target remains `duplicate` or `ambiguous` as applicable;
- equal identity/revision with different content, digest, or provenance remains
  `conflicting`;
- unknown target kinds remain separate from unsupported known kinds;
- restricted or inaccessible targets MUST NOT be treated as absent;
- an unverifiable target MUST NOT be treated as satisfied or not-satisfied;
  and
- no target may be invented, discovered, retrieved, repaired, substituted,
  defaulted, or selected by ranking.

These are bounded normative-contract assessment rules. They do not create a
repository-wide graph engine, registry, crawler, network resolver, automatic
discovery mechanism, or universal cross-artifact integrity system.

## Task, context, execution, validation, and evidence relationships

The `task-context-execution-chain` rule evaluates only exact supplied pins:

- the Execution Result's governing Task Contract pin resolves to the exact
  supplied Task Contract identity and revision;
- every declared Context Packet pin used by that Execution Result resolves to an
  exact supplied Context Packet;
- every supplied Context Packet's governing Task Contract pin resolves to the
  same exact supplied governing Task Contract when the applicable contract
  requires it; and
- conflicts, omissions, duplicates, inaccessible targets, and unsupported
  versions remain separate.

The `validation-record-subject-link` rule evaluates the exact subject pins of a
supplied Validation Execution Record. It does not decide that the subject is
valid, applicable, authentic, or conforming.

The `evidence-package-execution-link` rule evaluates Package B execution-record
pins against exact supplied Validation Execution Records. It does not prove
that evidence is relevant, sufficient, independent, authentic, or correct.

## Role, review, and final-authority relationships

Role evaluation preserves principal/requester, producer/preparer, executor,
reviewer, decision-maker, acceptor, and Final Authority separately.

`role-overlap-visible` records every exact attributable identity overlap that
is material to an applicable rule. Overlap visibility is not itself a verdict.

`review-independence-declared` requires the applicable review source and exact
independence or non-independence declaration. Different identifiers alone do
not prove independence. Equal identifiers may prove overlap but do not decide
every consequence without the exact governing rule.

`self-review-prohibited` applies only where an independent review is required.
It does not prohibit a transparent non-independent review from being recorded
as non-independent and non-accepting.

`self-acceptance-prohibited` keeps preparation, execution, review,
recommendation, decision, and final acceptance separate. Only the exact
governing attributable Final Authority can grant the consequential acceptance
defined by the applicable source.

`automatic-authority-false` requires exact `false` where an applicable record
defines that property. Absence, ambiguity, conflict, or unsupported versions
fail closed; they are not silently treated as false.

## Diagnostics, limitations, evidence, and claim boundary

Diagnostics identify observed parsing, construction, binding, supplied-record,
reference, applicability, requirement, processing, resource, security/privacy,
or authority conditions. Diagnostics are not rule outcomes by themselves.

Limitations identify material restrictions on inputs, evaluator context,
coverage, evidence, disclosure, reproduction, independence, resources, or
claims. A limitation cannot be hidden by a satisfied rule.

Adverse evidence, contradictory evidence, restricted evidence, inaccessible
evidence, and absence of evidence remain separate. Restricted material is
referenced and minimized without copying it into a public record.

Every claim is bound to exact Rule Identifier/Version, subjects, revisions,
governing context, evaluator declarations, outcomes, diagnostics, limitations,
and evidence references. A claim cannot expand beyond evaluated rules or
supplied records.

## Output, evidence, review, decision, and artifact separation

Keep each of these separate:

- manifest parsing;
- case construction;
- expected-validity interpretation;
- Schema Resource binding and static reference closure;
- Schema Resource evaluation;
- Validation Execution Record phases and outcomes;
- Validation Evidence and Reproduction Package;
- individual Integrity Rule and rule outcome;
- Integrity Evaluation Record;
- diagnostics, limitations, warnings, adverse/restricted evidence, blocked
  conditions, and non-execution;
- raw evaluator output;
- canonical Validation Output, if later separately Accepted;
- Portable Conformance Evidence;
- Evidence Bundle;
- Review Record;
- Decision Record;
- acceptance, certification, release evidence, and deployment evidence; and
- final-human authority.

No record becomes another merely through a reference, matching digest,
successful parse, satisfied rule, repository presence, publication, review, or
later schema validity.

## No aggregate authority

No Test Manifest or Integrity Evaluation representation may contain or imply a
universal aggregate result, boolean pass/fail, traffic light, score, grade,
badge, threshold, rubric, checklist verdict, quality gate, ranking,
recommendation, approval, certification, release fitness, deployment fitness,
or consequential authority.

A descriptive summary MAY count individually preserved outcomes but MUST keep
all `not-satisfied`, `unverifiable`, `not-evaluated`, blocked, warning,
limitation, adverse, and restricted conditions visible. A count cannot replace
the individual result records.

## Closed, frozen, offline-first deterministic processing

Any later conforming processing MUST use one exact caller-supplied context:

- closed manifest and supplied-record sets;
- exact identities, versions, revisions, locations, and digests where supplied;
- exact rule set and Rule Versions;
- exact Definition, Representation, Schema Resource, and resource-closure pins;
- exact configuration, capability, dependency, runtime, environment, target,
  and resource-limit declarations where separately defined;
- exact claim scope and attributable roles; and
- explicit network prohibition.

Automatic discovery, retrieval, redirects, network authority, hidden cache,
ambient state, mutable aliases, `latest`, newest-wins, substitution, coercion,
defaulting, repair, fallback, silent capability downgrade, and order-,
popularity-, majority-, consensus-, score-, or ranking-based meaning are
prohibited.

Unknown requirements, unsupported capabilities, missing inputs, duplicates,
conflicts, ambiguity, resource blockage, warnings, limitations,
security/privacy ambiguity, restricted evidence, unverifiable conditions,
blocked phases, non-execution, and adverse evidence remain separate and fail
closed.

## Resource, security, privacy, disclosure, retention, and cleanup boundary

A future evaluator MUST receive caller-supplied bounds for applicable:

- manifest, case, operation, record, reference, rule, result, diagnostic,
  limitation, evidence, and output counts and sizes;
- node/edge counts, graph depth/breadth, recursion, composition,
  reference-expansion, repeated-evaluation, regex, and general evaluation cost;
- memory, CPU, wall time, concurrency, process/thread, file-descriptor,
  logging, diagnostic, output, and temporary-storage use; and
- minimization, least privilege, redaction, access, disclosure, retention,
  cleanup, and restricted-evidence handling.

No secret, credential, personal data, private project context, production
configuration, or exploitable restricted detail belongs in a public manifest,
rule, evaluation record, diagnostic, limitation, evidence item, or log.

This decision selects no concrete threshold, algorithm, sandbox, process
model, access-control model, log format, cleanup mechanism, retention policy,
transport, storage, Tool, or Implementation.

## Versioning and compatibility

Each Definition and Representation Version evolves independently under exact
governing acceptance. A change that alters a closed root, required property,
construction form, Rule Identity meaning, applicability, requirement, outcome
meaning, reference-resolution behavior, authority boundary, or prohibited
behavior is compatibility-significant.

Accepted versions are immutable. Correction, supersession, withdrawal, or a
new compatible/incompatible version requires a separate attributable decision
and preserves prior history. Repository presence, publication time, or a newer
version never selects an active version automatically.

Compatibility of one Definition, Representation, rule, evaluator, Tool,
Implementation, runtime, or dependency does not prove compatibility of
another dimension.

## Lifecycle and dependency-first next work

Preparation, validation, review, acceptance, integration, schema definition,
Tool/Implementation definition, implementation, execution, evidence,
reassessment, release, and deployment remain separate lifecycle phases.

Governed integration of this Accepted decision activates only the exact
Definition, Representation, and initial Rule identity/version allocations
defined here. It does not create instances or authorize Package D or E.

Dependency-first continuation remains:

1. Package D — concrete Tool and Implementation identity, version, capability,
   configuration, dependency, environment, and interface contracts;
2. Package E — implementation, cases, bounded evidence, review, and
   attributable decision; and
3. any later release, publication, support, certification, hosting, or
   deployment under separate authority.

This order authorizes none of those phases or identifiers.

## Consequences and limitations

Positive consequences:

- the two existing manifest construction forms become explicitly recognized
  without historical rewriting;
- the exact `203/38/165` baseline receives deterministic counting semantics;
- initial cross-record integrity responsibilities become individually named,
  versioned, applicable, evidenced, and outcome-bound;
- dangling, duplicate, ambiguous, conflicting, unsupported, restricted,
  inaccessible, unverifiable, and not-evaluated conditions remain visible;
- task/context/execution, validation/evidence, review-independence, and
  self-acceptance relationships become falsifiable within one exact supplied
  record set; and
- no aggregate result or automatic authority can hide adverse conditions.

Costs and limitations:

- three detailed Definition/Representation families increase documentation
  surface;
- no executable schema proves representation conformance;
- no evaluator, validator, resolver, runner, graph engine, Tool,
  Implementation, runtime, dependency, interface, or output implementation
  exists;
- the current manifest inventory is static and was not executed by this
  candidate;
- external existence, authenticity, relevance, sufficiency, independence, and
  trust remain unproven;
- bounded supplied-set integrity is not repository-wide or universal
  integrity; and
- broader interoperability, conformance, security/privacy, release fitness,
  deployment fitness, and final-human decisions remain unproven.

## Protected predecessors and immutable history

This candidate preserves without modification:

- all 145 baseline paths outside the effective allowlist, with the two new
  paths added only inside that allowlist;
- all Accepted ARCH-001 through ARCH-035 and ADR-0001 through ADR-0035
  semantics;
- CONTRACT-001 through CONTRACT-009;
- all ten Accepted Schema Resources and ten historical test manifests;
- exact static case inventory `203/38/165`;
- Core Artifact JSON Binding Version `1.0.0`;
- all Accepted validation, evidence, assessment, remediation, release,
  verification, completion, maintenance, and Extension Module/Profile sources;
- tag `v0.1.0-prealpha.1`, target
  `109e6f293b150f48572cd747fab446c141d57193`, and release-subject tree
  `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- GitHub Release `367290932` / `RE_kwDOTsnR984V5Go0`, prerelease true, draft
  false, zero custom assets, and immutable releases enabled; and
- all historical Git and GitHub objects.

## Explicit non-decisions

This candidate changes no path under `schemas/` or `tests/` and creates no
testcase, expected-validity change, manifest migration, executable schema,
Schema Version, assertion, rule instance, evaluation instance, validator,
resolver, runner, suite, graph engine, Tool Identity/Version, Implementation
Identity/Version, dependency, runtime, environment, configuration, capability,
interface, code, library, SDK, CLI, API, workflow, CI, product, service,
registry, transport, storage, publication system, release, support,
certification, hosting, or deployment.

It performs no dependency installation, schema execution, testcase execution,
integrity evaluation, network retrieval, evidence collection, security scan,
specialist security/privacy/legal review, restricted-source access,
external-model interaction, settings change, Ready-for-review transition,
merge, issue closure, branch cleanup, release, publication, support,
certification, hosting, or deployment.

Package D and Package E remain unauthorized and separately governed.

## Final-human authority

EIGENAAR / Final Authority remains the sole final human authority. Preparation,
static validation, a matching manifest inventory, a satisfied rule, a review,
repository presence, schema validity, reproduction, or publication cannot
grant acceptance or consequential authority.

Every future Integrity Evaluation Record `authorityBoundary` MUST set
`automaticAuthority` to exactly `false`. Missing, ambiguous, conflicting, or
unsupported authority information fails closed and cannot be repaired by an
evaluator.

## Lifecycle and final human authority

This Accepted decision did not approve itself. Attributable EIGENAAR / Final
Authority acceptance of the exact reviewed candidate is recorded in issue
comment `5243304427`. Repository presence, static validation, and transparent
non-independent ARCHITECT review `4898518876` did not grant that acceptance.

Governed integration activates only the exact Definition, Representation, and
Rule identity/version allocations and boundaries defined here. Acceptance and
integration do not create an executable schema, instance, Tool,
Implementation, dependency, evaluator, resolver, runner, workflow, release,
publication, support, certification, hosting, deployment, Package D, or
Package E.
