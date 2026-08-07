# ADR-0014: Task Contract executable schema definition

- **Status:** Accepted
- **Date:** 2026-08-07
- **Decision owners:** Cintao66, Owner / Final Authority
- **Issue:** [#54](https://github.com/CNTX-PROJECT/CNTX/issues/54)
- **Governing architecture:** [ARCH-014](../task-contract-executable-schema.md)

Owner / Final Authority acceptance of the exact reviewed candidate is recorded
in issue comment `5215700352`. On governed integration to `main`, Task Contract
Schema Version `1.0.0` becomes active under repository governance. Exact-head
operational review was transparently non-independent and did not grant final
acceptance.

## Context

Accepted ARCH-010 allocated the Task Contract logical Schema Identity, an
inactive `1.0.0` target, a closed `envelope`/`payload` root, and the exact
Common Artifact Envelope dependency. ARCH-011 activated the exact Task
Contract Definition Identifier/Version. CONTRACT-003 defines the authoritative
bounded-task meaning and human approval boundary.

ARCH-012 and ARCH-013 activated the Project Charter and Workstream schemas in
dependency order. Their acceptance did not authorize this candidate, and their
resources need not become executable dependencies merely because a Task
Contract traces to governing artifact instances.

## Decision

CNTX proposes one JSON Schema Draft 2020-12 Schema Resource at:

`schemas/task-contract/1.0.0/schema.json`

with canonical identity:

`https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0`

The resource evaluates a closed root with exactly required `envelope` and
`payload`. `/envelope` uses exactly one static external `$ref` to the Accepted
Common Artifact Envelope Schema Version `1.0.0` and overlays only the Task
Contract Artifact Type, governing Contract Definition Identifier/Version, and
governing Schema Identifier/Version constants.

The closed payload requires exactly:

1. `governingProjectCharter`;
2. `governingWorkstream`;
3. `objectiveAndOutcome`;
4. `scopeAndResources`;
5. `authorityAndExecution`;
6. `dependenciesAndConditions`;
7. `contextPacketExpectations`;
8. `securityAndPrivacy`;
9. `assuranceAndAcceptance`;
10. `consequentialDecisionBoundaries`; and
11. `lifecycleConditions`.

The two governing artifacts are opaque Artifact Instance/Revision pins, not
embedded artifacts or schema `$ref` values. Declaration sets use exactly
`specified` with non-empty unique non-blank items or assessed `none` without
items. Every defined object is closed; ordinary required arrays are non-empty
and unique; ordinary strings are non-blank.

The resource contains one root `$schema`, one root `$id`, internal
fragment-local `$defs` references, and exactly one external reference. It has
no nested resource, dynamic reference, anchor, `format`, default, custom
vocabulary, artifact-specific schema dependency, or public subschema API.

## Rationale

This design translates only CONTRACT-003 into executable structural
assertions while preserving the Accepted container, common-envelope,
identity/version, authority, and dependency architecture.

Opaque governing-artifact pins provide traceability without coupling
independent schemas or pretending JSON Schema can establish existence,
applicability, approval, or authority. Closed objects and explicit declaration
sets fail closed and distinguish assessed absence from omission.

Scope, actions, resources, authority, evidence, and decision boundaries remain
human-reviewable statements. The schema deliberately does not invent a
permission language, path grammar, allow/deny precedence, approval mechanism,
workflow, or runtime.

## Consequences and tradeoffs

- A complete Task Contract resource becomes structurally evaluable.
- All eleven direct CONTRACT-003 responsibilities become explicit.
- Governing Project Charter and Workstream traceability remains independently
  governed and non-executable.
- Required closed structure improves consistency and reviewability.
- Lexically broad statements preserve model, provider, runtime, product, and
  domain independence.
- The schema cannot prove truth, least privilege, contract conformance,
  approval, execution, completion, or decision authority.
- Later structural or semantic change requires independent Schema Version
  assessment.
- No canonical artifact serialization, permission engine, resolver, validator,
  workflow, or runtime is created.

## Rejected alternatives

- Flat, optional, or open roots.
- Copying or weakening the common envelope.
- Common-internal, mutable, relative, dynamic, or moving references.
- Project Charter or Workstream schema `$ref` values or embedded artifacts.
- Embedded peer Task Contracts or downstream artifacts.
- One schema or lockstep version for all artifacts.
- Executable action/resource/path taxonomies, wildcard semantics, allow/deny
  precedence, permission languages, or policy engines.
- Approval state, signatures, timestamps, trust, credentials, task progress,
  lifecycle status, workflows, schedulers, orchestration, or runtime fields.
- Arbitrary payload maps, unknown properties, blank values, empty arrays,
  duplicates, null, or fabricated `N/A`.
- Mandatory personal names.
- Canonical JSON or another implied Serialization Binding.
- Normative examples.
- Treating validation, review, or repository presence as acceptance.
- Automatic Context Packet schema authority.

## Validation

The candidate must pass strict JSON and duplicate-key parsing, official Draft
2020-12 meta-schema checking, isolated `jsonschema 4.25.1` evaluation with the
exact common resource registered locally, missing-resource failure, all
committed expected-validity cases, root/payload/closure/constant/reference
assertions, UTF-8 and BOM checks, local-link checks, protected-blob checks,
privacy/security scans, exact eight-path scope, one-commit parent proof, and
GitHub branch/PR/head read-back.

The committed manifest contains sixteen cases: three expected-valid and
thirteen expected-invalid. The schema contains 75 references: exactly one
external Common Artifact Envelope root and 74 fragment-local internal refs.

The exact-head review is transparently non-independent and evidentiary only.
It cannot accept or activate the Schema Version.

## Security and privacy

The schema, tests, and documentation contain only public-safe synthetic
material. They contain no secrets, credentials, personal data, production
configuration, private paths, restricted content, provider assumptions,
product logic, or private implementation. HTTPS-shaped identities and refs
grant no network, access, disclosure, trust, or authority permission.

## Authority and conformance boundary

Schema-valid is not necessarily CONTRACT-003-conformant, approved,
authoritative, truthful, applicable, least-privileged, safe, complete,
executed, accepted, closed, integrated, released, or deployable. The schema
cannot verify either governing artifact, authority source, approver role,
delegation, scope permission, evidence adequacy, acceptance criteria,
lifecycle condition, or consequential decision.

Only applicable human approval of the exact Task Contract Artifact Revision
can grant bounded execution authority. Final authority remains human and
exact-revision-bound.

## Deferred scope

Deferred are Task Contract instances; identifier/revision allocation;
governing-artifact retrieval or validation; permission and path semantics;
approval evidence; signatures; digests; canonicalization; Serialization
Bindings; extensions/profiles; resolvers; registries; catalogs; caches;
bundlers; validators; validation-output contracts; conformance tooling;
migrations; templates; forms; prompts; APIs; CLIs; workflows; engines;
schedulers; orchestrators; runtimes; provider/product work; private/reference
implementations; releases; tags; hosted publication; and deployment.

## Continuing gate

The exact reviewed candidate was accepted by the Owner / Final Authority in
issue comment `5215700352`. Governed integration to `main` activates exactly
Task Contract Schema Version `1.0.0`. No Context Packet or later
artifact-specific schema is automatically authorized.
