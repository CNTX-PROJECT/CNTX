# ADR-0035: CNTX Validation Evidence and Reproduction Package identity, version, and JSON representation

- **Status:** Proposed
- **Date:** 2026-08-10
- **Issue:** [#116](https://github.com/CNTX-PROJECT/CNTX/issues/116)
- **Issue-contract acceptance:** [5241232823](https://github.com/CNTX-PROJECT/CNTX/issues/116#issuecomment-5241232823)
- **Decision:** ARCH-035 — CNTX Validation Evidence and Reproduction Package
  Identity, Version, and JSON Representation

## Context

Accepted ARCH-034 defines one non-Artifact Validation Execution Record with a
strict JSON representation, frozen context, exact eight-phase results,
diagnostics, limitations, claims, and final-human-authority boundaries. It
deliberately creates no evidence or reproduction package.

Accepted ARCH-025 defines Portable Conformance Evidence responsibilities but
creates no concrete evidence identity or representation. CONTRACT-006 defines
the canonical Evidence Bundle as a separate Evidentiary Artifact Type. ARCH-033
requires concrete output and evidence identities before a Tool or
Implementation contract.

Without one concrete Package B definition, evidence and reproduction material
could use incompatible identities, omit exact inputs or revisions, merge
expected and observed results, conceal adverse or restricted evidence, silently
substitute environments or dependencies, leave local references dangling, or
be mistaken for canonical evidence, review, acceptance, or authority.

## Decision

Define one non-Artifact Validation-layer Evidence and Reproduction Package with
these Proposed logical identity/version pairs:

- Package Definition Identifier
  `https://github.com/CNTX-PROJECT/CNTX/definitions/validation-evidence-reproduction-package`,
  initial Version `1.0.0`;
- Package JSON Representation Identifier
  `https://github.com/CNTX-PROJECT/CNTX/bindings/validation-evidence-reproduction-package-json`,
  initial Version `1.0.0`.

The identifiers are identities, not network-retrieval authority. The package
is not a tenth CNTX Artifact Type, does not use the Common Artifact Envelope,
and is not governed as CONTRACT-001 through CONTRACT-009.

Select one strict UTF-8 JSON-document representation: no BOM, duplicate member
names, comments, coercion, defaulting, repair, substitution, silent fallback,
unknown properties, or trailing non-whitespace bytes.

Require one closed root with exactly twelve properties: `package`, `subjects`,
`governingInputs`, `evaluatorContext`, `executionRecords`, `evidenceItems`,
`reproductionProcedures`, `outputs`, `diagnostics`, `limitations`,
`claimBoundary`, and `authorityBoundary`.

Require exact Package Definition, Representation, Identifier, Revision,
lifecycle, producer, assembler, production-time, and digest coordinates.
Correction, supersession, or withdrawal creates a new immutable Package
Revision and never overwrites prior history.

Require at least one exact Validation Execution Record subject and exact
caller-supplied governing context. Preserve repository, architecture, ADR,
Contract Definition, binding, Definition, Schema Resource, resource closure,
activation, declaration, execution-record, task-authority, and claim-scope
dimensions separately.

Require caller-supplied evaluator, Tool/Implementation when separately defined,
runtime, dependency set, configuration, capabilities, unsupported capabilities,
environment, resource limits, network prohibition, observation method, and
provenance declarations. These declarations allocate or select none of those
dimensions and prove no enforcement or completeness.

Require exact Validation Execution Record identity/version/revision/digest
references and one supplied index of all eight ARCH-034 phase outcomes. The
index cannot replace or correct the referenced record; mismatches remain
diagnostics and adverse evidence.

Define bounded evidence items with unique local references, exact categories,
subject/record/phase/claim relations, source revision and digest, observation
context, separate expected and actual observations, transformations, integrity
claims, uncertainty, limitations, restricted-content handling, provenance, and
time or condition coordinates.

Keep direct, derived, supporting, qualifying, contradictory, missing,
unavailable, restricted, and not-assessed evidence distinguishable. A declared
relation proves no relevance, sufficiency, independence, authenticity, or
correctness.

Define ordered bounded reproduction procedures and steps with exact inputs,
preconditions, expected and actual observations, four separate outcomes,
attempt state, deviations, outputs, evidence, diagnostics, limitations,
cleanup, and provenance. A reproduction description is not execution
authority; reproduced results are new evidence and do not retroactively alter
original material.

Define separately identified outputs, diagnostics, limitations, and claims.
Prohibit any aggregate pass/fail, traffic light, score, grade, badge, threshold,
quality gate, ranking, recommendation, approval, certification, release
fitness, deployment fitness, or universal evidence-sufficiency property.

Require package-local referential integrity for subjects, governing inputs,
execution records, evidence items, procedures, steps, outputs, diagnostics,
limitations, and claims. External references remain opaque exact pins. General
cross-record rules remain Package C work.

Keep Validation Execution Record, raw evaluator output, canonical Validation
Output, this package, Portable Conformance Evidence, Evidence Bundle, Review
Record, Decision Record, certification evidence, release evidence, every other
Artifact Instance, and final-human authority separate.

Require a caller-supplied, exact, closed, frozen, offline-first, bounded,
deterministic, fail-closed context. Prohibit automatic discovery, retrieval,
redirects, network authority, hidden cache, ambient state, mutable aliases,
`latest`, newest-wins, substitution, coercion, defaulting, repair, fallback,
silent downgrade, and score-, ranking-, popularity-, majority-, or consensus-
based meaning.

Require `automaticAuthority` to be `false`. Package production, evidence,
reproduction, digest match, schema validity, publication, or review cannot
approve, accept, merge, release, publish, support, certify, host, deploy,
correct, withdraw, deprecate, supersede, or close work.

Create no executable schema. A later separately governed schema may encode
machine-evaluable representation rules but cannot change normative meaning or
establish broader conformance.

## Consequences

Positive consequences:

- evidence and reproduction packages receive stable identity/version targets;
- exact inputs, revisions, context, observations, differences, provenance,
  limits, adverse evidence, restricted evidence, and non-execution remain
  visible;
- expected and actual observations remain separate;
- deviations and environmental differences cannot be silent;
- package-local dangling and duplicate references are prohibited;
- canonical artifacts, Portable Conformance Evidence, review, decision, and
  authority remain separate; and
- Packages C and D receive a stable dependency without automatic authority.

Costs and limitations:

- the package is detailed and requires explicit caller-supplied context;
- no executable schema, validator, runner, Tool, Implementation, dependency,
  interface, storage, transport, or reproduction execution exists;
- external existence, authenticity, evidence relevance, sufficiency,
  independence, and trust remain unproven;
- package-local integrity is not general cross-record integrity;
- reproduction may remain not executed, blocked, restricted, or unverifiable;
  and
- interoperability and broader conformance remain unproven.

## Alternatives not selected

### Reuse the Common Artifact Envelope or Evidence Bundle

Not selected because the Common Artifact Envelope has a closed nine-value
Artifact Type set and CONTRACT-006 already governs the canonical Evidence
Bundle. This package is validation-layer material and must not silently change
either Accepted family.

### Put evidence directly inside the Validation Execution Record

Not selected because ARCH-034 deliberately separates record-local evidence
references from a concrete evidence/reproduction package. Combining them would
couple validation output, evidence lifecycle, reproduction, and revisioning.

### Define Portable Conformance Evidence now

Not selected because ARCH-025 keeps portability, claim sufficiency, independent
reassessment, and conformance-target evidence separate. This package may later
be an input but is not Portable Conformance Evidence.

### Let the first runner choose fields and reproduction semantics

Not selected because implementation behavior is non-normative and would create
precedent, ambiguity, and provider/runtime lock-in.

### Create an executable schema or run historical harnesses now

Not selected because Package B authority is documentation-only. No schema,
dependency, validator, runner, schema execution, or test execution is
authorized.

## Non-decisions

This ADR creates no tenth Artifact Type, Common Artifact Envelope change,
artifact contract, Artifact Instance, Validation Execution Record revision,
canonical Validation Output, Portable Conformance Evidence, Evidence Bundle,
Review Record, Decision Record, certification evidence, release evidence,
support evidence, or deployment evidence.

It creates no executable schema, `$id`, Schema Version, assertion, testcase,
test manifest, cross-record rule, Tool Identity/Version, Implementation
Identity/Version, dependency, runtime, environment, configuration, capability,
interface, validator, resolver, runner, suite, library, SDK, API, CLI, workflow,
CI, product, service, registry, transport, storage, publication, support,
certification, hosting, or deployment.

It performs no dependency installation, schema/test execution, reproduction,
network access, evidence collection, security scan, specialist review,
settings change, correction, reassessment, Ready transition, merge, issue
closure, branch cleanup, release, publication, support, certification, hosting,
or deployment.

Package C, D, and E remain unauthorized and separately governed.

## Authority boundary

This ADR is Proposed under issue #116 and attributable EIGENAAR / Final
Authority issue-contract acceptance comment `5241232823`. That authority
permits preparation, one branch, one candidate commit/push, one Draft PR,
validation, and transparent non-independent review only.

Repository presence, validation, a COMMENT review, or Draft PR state grants no
acceptance. Only a later attributable EIGENAAR / Final Authority decision on
the exact reviewed candidate may authorize status-only promotion and
integration. Acceptance would activate only the Package Definition and JSON
Representation identity/version pairs and boundaries defined here. It would
not create a package instance or authorize Package C, D, E, an executable
schema, dependency, Tool, Implementation, runner, workflow, release, support,
hosting, or deployment.
