# ADR-0036: CNTX Test Manifest and Initial Cross-Record Integrity Rules identity, version, and JSON representation

- **Status:** Accepted
- **Date:** 2026-08-10
- **Issue:** [#118](https://github.com/CNTX-PROJECT/CNTX/issues/118)
- **Issue-contract acceptance:** [5242339896](https://github.com/CNTX-PROJECT/CNTX/issues/118#issuecomment-5242339896)
- **Exact-head acceptance:** [5243304427](https://github.com/CNTX-PROJECT/CNTX/issues/118#issuecomment-5243304427)
- **Decision:** ARCH-036 — CNTX Test Manifest and Initial Cross-Record
  Integrity Rules Identity, Version, and JSON Representation

## Context

CNTX has ten Accepted Schema Versions `1.0.0` and ten historical non-normative
synthetic test manifests. The exact public baseline contains 203 unique cases:
38 expected-valid and 165 expected-invalid. Nine manifests carry direct
complete instances. The State Snapshot manifest carries one base instance and
ordered `add`, `remove`, or `replace` operations.

Accepted ARCH-034 defines one Validation Execution Record with eight phase
outcomes. Accepted ARCH-035 defines one bounded Validation Evidence and
Reproduction Package with package-local referential integrity. Both retain
external cross-record references as opaque pins and explicitly defer general
cross-record rules to Package C.

Without a Test Manifest contract, a later runner could count the two forms
differently, skip or duplicate cases, silently normalize history, or let its
implementation become normative. Without individually identified cross-record
rules, dangling references, conflicting identity/revision claims, broken
Task Contract–Context Packet–Execution Result chains, evidence-package linkage,
role overlap, review independence, self-review, self-acceptance, and automatic
authority cannot be assessed reproducibly.

## Decision

Define three separate non-Artifact Validation-layer documentation contracts:

1. Test Manifest;
2. Cross-Record Integrity Rule; and
3. Cross-Record Integrity Evaluation Record.

Propose these independent Definition and JSON Representation identity/version
pairs, each initially Version `1.0.0`:

- `https://github.com/CNTX-PROJECT/CNTX/definitions/test-manifest` and
  `https://github.com/CNTX-PROJECT/CNTX/bindings/test-manifest-json`;
- `https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-rule`
  and
  `https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-rule-json`;
  and
- `https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-evaluation-record`
  and
  `https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-evaluation-record-json`.

The identifiers are opaque identities, not network-retrieval authority. The
definitions do not use or extend the Common Artifact Envelope and create no
tenth CNTX Artifact Type.

Recognize exactly two Test Manifest JSON root variants without changing any
historical manifest:

- the direct variant with complete `instance` cases; and
- the State Snapshot variant with `baseInstance`, `caseConstruction`, and
  ordered operation cases.

Preserve exact closed existing properties. Direct cases contain exactly
`name`, `valid`, and `instance`. Operation cases contain exactly `name`,
`valid`, and `operations`; each operation contains `op` and `path`, plus
`value` when required. Operation order is significant. Construction deep-
copies the supplied base and applies the supplied operations in order. This is
representation semantics, not selection of a patch library, runtime, or
implementation.

Define one case key as the exact manifest key plus case name. Count each unique
case key once. Preserve the exact static baseline inventory:

- Common Artifact Envelope: `31/11/20`;
- Context Packet, Decision Record, Evidence Bundle, Execution Result, Project
  Charter, Review Record, and State Snapshot: each `20/3/17`;
- Task Contract and Workstream: each `16/3/13`; and
- total: `203/38/165`.

The inventory is static evidence, not schema/test execution or validator,
conformance, review, acceptance, certification, release, deployment, or
authority proof.

Define one Cross-Record Integrity Rule representation with a closed
eight-property root: `rule`, `applicability`, `requiredSubjects`,
`requirements`, `outcomeBoundary`, `evidenceBoundary`, `processingBoundary`,
and `authorityBoundary`.

Define one Cross-Record Integrity Evaluation Record representation with a
closed nine-property root: `evaluation`, `governingContext`, `suppliedRecords`,
`ruleDefinitions`, `ruleResults`, `diagnostics`, `limitations`,
`claimBoundary`, and `authorityBoundary`.

Require exact caller-supplied record keys, identities, versions, revisions,
content/digest/provenance pins where supplied, exact Rule Identifiers and Rule
Versions, exact applicability, individual requirements, individual outcomes,
diagnostics, limitations, evidence references, claims, and attributable roles.

Define exactly four lowercase individual rule outcomes:

- `satisfied`;
- `not-satisfied`;
- `unverifiable`; and
- `not-evaluated`.

Do not merge those tokens with Validation Execution Record phase results. An
inapplicable rule is represented by its applicability decision and is not
silently satisfied.

Propose thirteen initial Rule Identities under
`https://github.com/CNTX-PROJECT/CNTX/rules/cross-record/`, each initially Rule
Version `1.0.0`:

- `supplied-record-exists`;
- `identity-version-revision-complete`;
- `record-key-unique`;
- `identity-revision-content-consistent`;
- `reference-resolves-exactly-once`;
- `task-context-execution-chain`;
- `validation-record-subject-link`;
- `evidence-package-execution-link`;
- `role-overlap-visible`;
- `review-independence-declared`;
- `self-review-prohibited`;
- `self-acceptance-prohibited`; and
- `automatic-authority-false`.

Keep each rule individually identified, versioned, applicable, subject-bound,
evidence-bound, and outcome-bound. Rule listing order creates no precedence.

Require bounded cross-record integrity within one exact supplied record set:
unique record keys; consistent identity/version/revision/content/digest/
provenance claims; references resolving exactly once; and separately visible
zero-target, multi-target, conflict, unknown, unsupported, restricted,
inaccessible, unverifiable, and not-evaluated conditions.

Keep principal/requester, producer/preparer, executor, reviewer,
decision-maker, acceptor, and Final Authority separate. Require visible role
overlap and exact governing sources. Different identifiers alone do not prove
independence. Transparent non-independent review remains representable but
cannot satisfy an independent-review requirement or grant acceptance.

Require caller-supplied, exact, closed, frozen, offline-first, bounded,
deterministic, and fail-closed processing. Prohibit automatic discovery,
retrieval, redirects, network authority, hidden cache, ambient state, mutable
aliases, `latest`, newest-wins, substitution, coercion, defaulting, repair,
fallback, silent capability downgrade, and order-, popularity-, majority-,
consensus-, score-, or ranking-based meaning.

Prohibit every universal aggregate result, boolean pass/fail, traffic light,
score, grade, badge, threshold, rubric, checklist verdict, quality gate,
ranking, recommendation, approval, certification, release fitness, deployment
fitness, and consequential authority. Descriptive counts cannot replace or
hide individual adverse results.

Keep manifest parsing, case construction, expected-validity interpretation,
Schema Resource binding, static reference closure, schema evaluation,
Validation Execution Record phases, Package B packages, individual rules,
Integrity Evaluation Records, diagnostics, limitations, evidence, raw output,
canonical Validation Output, Portable Conformance Evidence, Evidence Bundle,
Review Record, Decision Record, acceptance, certification, release,
deployment, and final-human authority separate.

Require `automaticAuthority` to be exactly `false`. Missing, ambiguous,
conflicting, or unsupported authority information fails closed.

Create no executable schema. A later separately governed schema may encode the
representation only after an exact Accepted decision and cannot change this
normative meaning.

## Consequences

Positive consequences:

- both historical manifest forms receive one explicit contract without
  rewriting history;
- exact deterministic case identity and `203/38/165` counting become defined;
- initial cross-record gaps become individually falsifiable within one closed
  supplied record set;
- dangling, duplicate, ambiguous, conflicting, unsupported, restricted,
  inaccessible, unverifiable, and not-evaluated conditions cannot be hidden;
- task/context/execution, validation/evidence, role, review-independence,
  self-review, self-acceptance, and authority relationships remain separate;
  and
- Package D receives concrete input/output contract dependencies without
  receiving implementation authority.

Costs and limitations:

- three Definition/Representation families and thirteen initial rules increase
  documentation surface;
- the existing manifest corpus still has two physical representations;
- no executable schema, rule instance, evaluation instance, evaluator,
  validator, resolver, runner, graph engine, Tool, Implementation, dependency,
  interface, or output implementation exists;
- static inventory has not been executed by this candidate;
- external source existence, authenticity, evidence relevance, sufficiency,
  independence, and trust remain unproven;
- supplied-set integrity is not repository-wide or universal integrity; and
- broader interoperability, conformance, security/privacy, release fitness,
  deployment fitness, and final-human decisions remain unproven.

## Alternatives not selected

### Rewrite all manifests into one physical format

Not selected because Package C must preserve the ten historical manifests and
their Git objects. Rewriting would destroy exact evidence continuity and
exceed the five-path allowlist.

### Treat only the nine direct manifests as canonical

Not selected because frequency creates no authority or precedence. The State
Snapshot operation representation is Accepted historical test evidence and
must remain separately recognizable.

### Put all integrity behavior into JSON Schema

Not selected because general cross-record uniqueness, exact supplied-set
resolution, identity/revision consistency, and role relationships are not the
responsibility of the existing artifact Schema Resources. Package C creates no
executable schema.

### Let the first runner choose rule identity and behavior

Not selected because implementation behavior is non-normative. Letting it fill
contract gaps would create precedent and runtime/provider lock-in.

### Produce one green/red result

Not selected because an aggregate hides not-evaluated, unverifiable, blocked,
restricted, and adverse conditions and could be mistaken for acceptance or
authority.

### Build a repository-wide graph engine now

Not selected because the accepted scope is one exact caller-supplied closed
record set. Discovery, crawling, registry lookup, and implementation are later
separately governed work, if ever authorized.

## Non-decisions

This ADR changes no path under `schemas/` or `tests/`; no existing manifest,
case, expected-validity value, Schema Resource, Accepted source, release
object, or historical Git/GitHub object changes.

It creates no Artifact Type, Artifact Instance, manifest instance, rule
instance, evaluation instance, executable schema, Schema Version, assertion,
validator, resolver, runner, suite, graph engine, Tool Identity/Version,
Implementation Identity/Version, dependency, runtime, environment,
configuration, capability, interface, code, library, SDK, API, CLI, workflow,
CI, product, service, registry, transport, storage, publication, support,
certification, hosting, or deployment.

It performs no dependency installation, schema/test execution, integrity
evaluation, reproduction, evidence collection, network access, external-model
interaction, security scan, specialist security/privacy/legal review,
restricted-source access, settings change, Ready-for-review transition, merge,
issue closure, branch cleanup, release, publication, support, certification,
hosting, or deployment.

Package D and Package E remain unauthorized and separately governed.

## Authority boundary

This ADR is Accepted under issue #118, attributable EIGENAAR / Final Authority
issue-contract acceptance comment `5242339896`, and exact-head acceptance
comment `5243304427` for reviewed candidate commit
`8585ac2a04be1a2978b2f155065bc706638191e2` and tree
`fd369393b6b6687fc539a00c9677194e6944c693`. Repository presence, static
validation, and transparent non-independent ARCHITECT COMMENT review
`4898518876` did not grant that acceptance.

Governed integration activates only the Definition, Representation, and Rule
identity/version allocations and boundaries defined here. Acceptance and
integration do not create an instance or authorize Package D, Package E, an
executable schema, dependency, Tool, Implementation, evaluator, runner,
workflow, release, publication, support, certification, hosting, or deployment.
