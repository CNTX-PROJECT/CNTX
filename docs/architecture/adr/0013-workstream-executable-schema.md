# ADR-0013: Workstream executable schema definition

- **Status:** Accepted
- **Date:** 2026-08-07
- **Decision owners:** Cintao66, Owner / Final Authority
- **Issue:** [#52](https://github.com/CNTX-PROJECT/CNTX/issues/52)
- **Governing architecture:** [ARCH-013](../workstream-executable-schema.md)

Owner / Final Authority acceptance of the exact reviewed candidate is recorded
in issue comment `5215029431`. On governed integration to `main`, Workstream
Schema Version `1.0.0` becomes active under repository governance.

## Context

Accepted ARCH-010 allocated the logical Workstream Artifact Schema Identity,
an inactive `1.0.0` initial target, a closed `envelope`/`payload` root, and the
exact Common Artifact Envelope dependency. ARCH-011 activated the exact
Workstream Contract Definition Identifier/Version pair. CONTRACT-002 defines
Workstream meaning. ARCH-012 activated the Project Charter schema but granted
no automatic authority for a Workstream schema.

The next dependency-first decision is whether and how to define one complete,
closed, machine-evaluable Workstream artifact while preserving independent
artifact identity, authority, versioning, and schema dependencies.

## Decision

CNTX adopts one JSON Schema Draft 2020-12 Schema Resource at:

`schemas/workstream/1.0.0/schema.json`

with canonical identity:

`https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0`

The resource evaluates one closed root with exactly required `envelope` and
`payload` members. `/envelope` uses exactly one static external `$ref` to the
Accepted Common Artifact Envelope Schema Version `1.0.0` and overlays only the
Workstream Artifact Type, governing Contract Definition Identifier/Version,
and governing Schema Identifier/Version constants.

The closed payload requires exactly:

1. `governingProjectCharter`;
2. `purposeAndContribution`;
3. `scopeAndGrouping`;
4. `coordinationRelationships`;
5. `governingPrinciples`;
6. `materialConstraints`;
7. `workstreamConditions`;
8. `governance`;
9. `taskContractDecomposition`;
10. `declaredState`;
11. `assuranceExpectations`; and
12. `lifecycleConditions`.

The governing Project Charter is an opaque Artifact Instance/Revision pin,
not an embedded artifact or Project Charter schema `$ref`. Declaration sets
use exactly `specified` with non-empty unique non-blank items or assessed
`none` without items. Every defined object is closed; ordinary required arrays
are non-empty and unique; ordinary strings are non-blank.

The canonical resource contains one root `$schema`, one root `$id`, internal
fragment-local `$defs` references, and exactly one external reference. It has
no nested resource, dynamic reference, anchor, `format`, default, custom
vocabulary, Project Charter schema dependency, or public subschema API.

## Rationale

This choice translates only CONTRACT-002 into executable structural
assertions while preserving the Accepted artifact-container and common-envelope
architecture. An opaque governing-charter pin provides required traceability
without coupling independent artifact-specific schemas or pretending that
JSON Schema can establish existence, applicability, approval, or authority.

Closed objects and explicit declaration sets fail closed and distinguish
assessed absence from omission. A free non-blank declared-state statement
preserves CONTRACT-002's declared-state responsibility without inventing a
status vocabulary, transition system, timestamp model, or runtime.

## Consequences and tradeoffs

- A complete Workstream resource becomes structurally evaluable.
- The exact common envelope remains independently versioned and reusable.
- All twelve CONTRACT-002 responsibilities become explicit and reviewable.
- The Project Charter relationship remains an opaque, human-governed pin.
- Required structure improves consistency but later semantic changes require
  independent Schema Version assessment.
- Lexically broad statements preserve domain independence but cannot prove
  truth, completeness, safety, conformance, applicability, or approval.
- No canonical serialized artifact, resolver, validator, registry, workflow,
  or runtime is created.

## Rejected alternatives

- Flat, optional, or open root objects.
- Copying or weakening the common envelope.
- Common-internal, mutable, relative, dynamic, or moving references.
- A Project Charter schema `$ref` or embedded Project Charter.
- Embedded peer Workstreams or Task Contracts.
- One schema or lockstep version for all artifacts.
- Arbitrary payload maps, unknown properties, blank values, empty arrays,
  null, or fabricated `N/A`.
- Enumerated declared-state names, transitions, timestamps, or automation.
- Approval, authority, task-progress, lifecycle-status, execution,
  configuration, extension, or runtime fields.
- Mandatory personal names.
- Canonical JSON or another implied Serialization Binding.
- Treating validation, review, or repository presence as acceptance.
- Automatic Task Contract schema authority.

## Validation

The candidate must pass strict JSON and duplicate-key parsing, official Draft
2020-12 meta-schema checking, isolated `jsonschema 4.25.1` evaluation with the
exact common resource registered locally, missing-resource failure, all
committed expected-validity cases, root/payload/closure/constant/reference
assertions, UTF-8 and BOM checks, local-link checks, protected-blob checks,
privacy/security scans, exact eight-path scope, one-commit parent proof, and
GitHub branch/PR/head read-back.

The exact-head review is transparently non-independent and evidentiary only.
It cannot accept or activate the Schema Version.

## Security and privacy

The schema, tests, and documentation contain only public-safe synthetic
material. They contain no secrets, credentials, personal data, production
configuration, private paths, restricted content, provider assumptions,
product logic, or private implementation. HTTPS-shaped identities and
references grant no network or disclosure permission.

## Authority and conformance boundary

Schema-valid is not necessarily CONTRACT-002-conformant, approved,
authoritative, truthful, applicable, safe, complete, released, or deployable.
The schema cannot verify the governing Project Charter, final-authority role,
delegation, declared state, evidence adequacy, lifecycle condition, or
consequential decision. Final authority remains human and exact-revision-bound.

## Deferred scope

Deferred are Workstream instances; identifier/revision allocation;
Project Charter retrieval or validation; artifact-to-artifact schema refs;
state vocabularies or automation; approval evidence; signatures; digests;
canonicalization; Serialization Bindings; extensions/profiles; resolvers;
registries; catalogs; caches; bundlers; validators; validation-output
contracts; conformance tooling; migrations; templates; forms; APIs; CLIs;
workflows; engines; schedulers; orchestrators; runtimes; provider/product work;
private/reference implementations; releases; tags; hosted publication; and
deployment.

## Continuing gate

The exact reviewed candidate was accepted by the Owner / Final Authority in
issue comment `5215029431`. Governed integration to `main` activates exactly
Workstream Schema Version `1.0.0`. No Task Contract or later artifact-specific
schema is automatically authorized.
