# ADR-0034: CNTX Validation Execution Record identity, version, and JSON representation

- **Status:** Accepted
- **Date:** 2026-08-10
- **Issue:** [#114](https://github.com/CNTX-PROJECT/CNTX/issues/114)
- **Creation authority comment:** [5240354818](https://github.com/CNTX-PROJECT/CNTX/issues/114#issuecomment-5240354818)
- **Decision:** ARCH-034 — CNTX Validation Execution Record Identity,
  Version, and JSON Representation

## Context

Accepted ARCH-024 defines a frozen validation context, six separate
conformance dimensions, eight prerequisite-ordered phases, four outcomes,
separate failure layers, diagnostics, limitations, non-execution, output
responsibilities, and final-human-authority boundaries. It deliberately creates
no concrete Validation Output identity, version, object, field, token, binding,
or schema.

Accepted ARCH-025 defines Portable Conformance Evidence responsibilities but
creates no concrete evidence package. Accepted ARCH-033 requires concrete
output and evidence identities and representations before a concrete Tool or
Implementation contract.

Without one concrete record definition, later evaluators could use incompatible
phase names, collapse `Unverifiable` and `Not Evaluated`, omit frozen context or
limitations, invent aggregate pass/fail meaning, or let implementation output
silently become approval or authority.

## Decision

Define one non-Artifact Validation-layer record with these stable logical
identity/version pairs:

- Validation Execution Record Definition Identifier
  `https://github.com/CNTX-PROJECT/CNTX/definitions/validation-execution-record`,
  initial Version `1.0.0`;
- Validation Execution Record JSON Representation Identifier
  `https://github.com/CNTX-PROJECT/CNTX/bindings/validation-execution-record-json`,
  initial Version `1.0.0`.

The identifiers are identities, not network-retrieval authority. The record is
not a tenth CNTX Artifact Type, does not use the Common Artifact Envelope, and
is not governed by CONTRACT-001 through CONTRACT-009.

Select one strict UTF-8 JSON-document representation: no BOM, duplicate member
names, comments, coercion, defaulting, repair, unknown properties, or trailing
non-whitespace bytes. Keep Definition, Representation, Record Identifier,
Record Revision, provenance, digest, status, acceptance, and authority
separate.

Require one closed root object with exactly ten properties:
`record`, `subject`, `governingContext`, `evaluatorContext`,
`executionWindow`, `phaseResults`, `diagnostics`, `limitations`,
`claimBoundary`, and `authorityBoundary`.

Require exact record lineage and immutable revision coordinates. Correction,
supersession, or withdrawal creates a new revision and never overwrites prior
history.

Require one exact frozen governing context. Represent each governing-input
dimension once with one of `supplied`, `not-applicable`, `missing`,
`ambiguous`, `conflicting`, `unavailable`, `unsupported`, or `restricted`.
Only `supplied` values can support a positive outcome.

Require evaluator declarations for evaluator, later Tool and Implementation
references where defined, runtime, dependencies, configuration, capabilities,
unsupported capabilities, environment, resource limits, and disabled network
access. These are supplied declarations and allocate no Tool, Implementation,
runtime, dependency, capability, or interface.

Represent exactly the eight ARCH-024 phases, in order, using these tokens:

1. `supplied-document`;
2. `parse`;
3. `core-artifact-json-binding`;
4. `governing-inputs`;
5. `schema-resource-closure`;
6. `json-schema`;
7. `normative-contract`; and
8. `record-assembly`.

Represent each phase using exactly one of `satisfied`, `not-satisfied`,
`unverifiable`, or `not-evaluated`. Preserve prerequisite failures, missing
evidence, non-execution, diagnostics, limitations, and requirement references.
Prohibit an aggregate `valid`, pass/fail, score, grade, badge, traffic light,
threshold, recommendation, approval, or quality gate.

Define bounded diagnostic categories for assertion, processing, governing-
input, resolution, unsupported capability, warning, resource, security/privacy,
restricted-evidence, adverse-evidence, and non-execution observations. Message
text remains presentation, not a portable vocabulary, severity, repair, or
authority.

Define separately identified material limitations and exact local referential
integrity for diagnostic, limitation, and claim references. External references
remain opaque pins until separately governed definitions and supplied objects
exist. Cross-record integrity remains Package C work.

Allow separately scoped claims only for the six ARCH-024 conformance
dimensions. One dimension never proves another. Positive claims require all
applicable prerequisites and requirements satisfied, no material applicable
unverifiable condition, and no required non-evaluated phase.

Require `automaticAuthority` to be `false`. Record production, validation,
schema success, evidence references, or review cannot approve, accept, merge,
release, publish, support, certify, host, deploy, correct, withdraw, deprecate,
supersede, or close work.

Require SHA-256 only where Representation Version `1.0.0` supplies a digest,
with a 64-character lowercase hexadecimal value over exact declared bytes.
This does not select canonical JSON or prove authenticity, trust, or authority.

Create no executable schema. A later separately governed schema may encode
machine-evaluable representation rules but cannot change normative meaning or
establish broader conformance.

## Consequences

Positive consequences:

- later validation executions have one exact representation target;
- all eight phases and four outcomes stay visible and separate;
- frozen inputs, evaluator declarations, resource limits, timestamps,
  diagnostics, limitations, claims, and authority are preserved;
- record-local dangling or duplicate references are prohibited;
- no aggregate green result can hide blocked or unverifiable conditions; and
- later evidence, test/rule, Tool, Implementation, and runner work receives a
  stable dependency without automatic authority.

Costs and limitations:

- the record is detailed and requires callers to supply explicit context;
- no executable schema, validator, runner, Tool, Implementation, or interface
  exists;
- external reference integrity and evidence sufficiency remain separately
  governed;
- timestamps, producer identities, and evaluator declarations remain claims
  requiring evidence; and
- interoperability and broader conformance remain unproven.

## Alternatives not selected

### Reuse the Common Artifact Envelope and add a tenth Artifact Type

Not selected because the Common Artifact Envelope has a closed nine-value
Artifact Type set governed by accepted contracts and schemas. Validation output
is a separate layer and must not silently alter that artifact family.

### Use a single aggregate `valid` boolean

Not selected because it collapses binding, governing-input, resource,
executable-schema, normative-contract, evidence, and non-execution states and
could be mistaken for approval or broad conformance.

### Let the first implementation choose fields and tokens

Not selected because implementation behavior is non-normative and would create
precedent, ambiguity, and lock-in before attributable governance.

### Define Portable Conformance Evidence in the same record

Not selected because validation output and Portable Conformance Evidence are
separate lifecycle and sufficiency dimensions. Package B remains separate.

### Create the executable schema now

Not selected because Package A authority is documentation-only and no schema
identity, `$id`, version, assertions, cases, or validation authority was
granted.

## Non-decisions

This ADR creates no tenth Artifact Type, artifact contract, Artifact Instance,
Common Artifact Envelope change, executable schema, schema `$id`, test
manifest, case, cross-record rule, Portable Conformance Evidence package,
Evidence Bundle, Review Record, Decision Record, certification, or release
record.

It allocates no Tool or Implementation Identity/Version, runtime, dependency,
capability, configuration, interface, media type, storage, transport, support,
compatibility, release, or deployment target.

It creates no resolver, validator, runner, suite, library, SDK, API, CLI,
workflow, CI, runtime product, hosted service, publication, support,
certification, hosting, or deployment. It performs no dependency installation,
schema/test execution, settings change, correction, reassessment, release,
merge, issue closure, or cleanup.

Package B, C, D, and E remain unauthorized and separately governed.

## Authority boundary

This ADR is Accepted under issue #114, creation-authority comment `5240354818`,
and attributable EIGENAAR / Final Authority exact-head acceptance comment
`5240683870` for reviewed candidate commit
`097a03f06b692f5fc108e48c252d4e5597d8c44c` and tree
`38d039c72f015048fd202fcd78260a9532c9b604`. Repository presence, validation,
and transparent non-independent ARCHITECT COMMENT review `4896887367` did not
grant that acceptance.

Governed integration activates only the Definition and Representation
identity/version pairs and boundaries defined here. Acceptance and integration
do not authorize an executable schema, evidence package, test/rule contract,
Tool, Implementation, dependency, runner, workflow, release, support, hosting,
or deployment.
