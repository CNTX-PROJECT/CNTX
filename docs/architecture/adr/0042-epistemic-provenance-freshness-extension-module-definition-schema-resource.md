# ADR-0042: CNTX Epistemic Provenance and Freshness Extension Module Definition Schema Resource

- **Status:** Accepted
- **Date:** 2026-08-12
- **Issue:** [#145](https://github.com/CNTX-PROJECT/CNTX/issues/145)
- **Issue-contract acceptance comment:** [5267576754](https://github.com/CNTX-PROJECT/CNTX/issues/145#issuecomment-5267576754)
- **Exact-head candidate acceptance comment:** [5269689952](https://github.com/CNTX-PROJECT/CNTX/issues/145#issuecomment-5269689952)
- **Baseline:** commit `c7650274a2818a5c3eaca0abfb0bc86fd747e4b2`, tree `f7dd74615c11e5390c0680f862668f425285e7f7`
- **Accepted candidate:** commit `d10fb23bdec7c13bb1154bd538d8e691d486fcce`, tree `071a9909efcee1d4d74d7ff65b0b05da30e73875`
- **Decision:** ARCH-042 — CNTX Epistemic Provenance and Freshness Extension Module Definition Schema Resource

## Context

Accepted ARCH-038 defines the Epistemic Provenance and Freshness Extension
Module Definition and Version `1.0.0`. Accepted ARCH-040 defines one closed
thirteen-property JSON-compatible declaration representation. ARCH-031 and
ARCH-032 require any concrete Definition Schema Identity, Schema Version,
canonical resource, assertions, cases, fixed results, evaluation, and Tool
support to remain separately governed.

The representation dependency and the corrective Implementation `1.0.1`
gate are complete. Phase 4A3.2 therefore defines one Accepted Definition
Schema Resource without modifying Core schemas, Context Packet, the existing
Tool supported set, or a later Profile boundary.

## Accepted decision

Accept one child of the `CNTX Extension Module Definition Schema Family`:

- Definition Schema Identifier
  `https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness`;
- initial Schema Version `1.0.0`;
- canonical `$id`
  `https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness/1.0.0`;
- JSON Schema Draft 2020-12;
- media type `application/schema+json`; and
- canonical candidate path
  `schemas/extension-modules/epistemic-provenance-freshness/1.0.0/schema.json`.

The resource is standalone, has internal `$defs` and static fragment-only
internal references, and has no external dependency, nested identity, dynamic
reference, custom vocabulary, remote resolution, default, coercion, fallback,
aggregate result, or executable action.

It evaluates one closed ARCH-040 declaration containing exactly the thirteen
required root properties. It structurally preserves exact Definition pins,
the six source categories, seventeen dimensions, four temporal coordinates,
opaque digest algorithm identity, separate policies, finite derivation, eight
conditions, four evaluation outcomes, limitations, adverse/restricted
metadata, attributable roles, non-aggregation, and final-human authority.

Specified times use a bounded explicit-offset RFC 3339-compatible lexical
shape. Format annotation is not the sole validity assertion. Lexical validity
proves no clock correctness, synchronization, observation truth, freshness, or
policy applicability.

Digest algorithm remains opaque and non-blank; no algorithm enum, default,
canonicalization, signature, certificate, or verifier is selected.

`automaticAuthority: false` remains a semantic invariant rather than a
serialized property. The closed authority object rejects such a member.

## Fixed synthetic cases

The direct non-normative manifest fixes exactly 48 complete public-safe cases
before evaluation: 8 expected valid and 40 expected invalid. Valid cases cover
minimal, governing, model-recollection, derived, restricted, conflicting,
digest, and temporal/policy declarations. Invalid cases cover every material
assertion family.

The historical ten manifests remain unchanged at `203/38/165` and historical
forms `9/1`. The new manifest is one additional direct form. Counts are
descriptive and never an aggregate score, quality gate, conformance claim,
approval, certification, release gate, deployment gate, or authority.

## Evaluation boundary

The immutable candidate commit was evaluated exactly once in one isolated
Windows environment with CPython `3.13.14` and the five exact dependency
artifacts already pinned by the corrective lock. The evaluation checked the
Draft 2020-12 schema and compared each fixed expected validity with the actual
result: all 48 matched. Artifact filename, size, and digest were verified before
installation; resolution and case evaluation used no network access. Temporary
dependencies, environment, outputs, and helper material were removed after
evidence capture. Any acquisition, verification, installation, meta-schema,
evaluation, comparison, isolation, or cleanup failure was required to stop fail
closed without retry or favorable claim. That evidence remains bound
exclusively to candidate commit/tree
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875`; the status-only promotion is not
a new execution or evidence instance. Its execution-evidence SHA-256 remains
`2ec1f7552ee7830d9fa8fccfd4dd0e0d1089ea77f7566a4da4f255cc298ee938`
and its evaluator-result SHA-256 remains
`df9e2af0a2b6cf14830619dd496895bb851ba2e5968417e972bfea739c6db975`.

This does not add public execution code or expand the existing Tool's exact
ten-schema supported set. Any failure stops without retry or favorable claim.

## Consequences

Positive consequences:

- the Accepted ARCH-040 shape becomes structurally machine-evaluable;
- unknown properties/tokens, omissions, null substitutions, incomplete
  wrappers, and prohibited authority/aggregate members fail closed;
- exact cases make material assertion families reviewable before execution;
- historical Core schemas, tests, and Tool behavior remain immutable; and
- schema validity stays separate from semantic or consequential authority.

Costs and limitations:

- the explicit declaration and direct case manifest are intentionally large;
- standard JSON Schema cannot prove external existence, authenticity, truth,
  policy applicability, cross-reference resolution, projected uniqueness, or
  every graph property;
- date-time lexical checking does not prove temporal truth or freshness;
- the one execution environment is Windows-specific and non-independent;
- no alternate-implementation, portability, production, performance, hard
  resource, OS-isolation, or complete adversarial evidence exists; and
- the preceding Proposed status allocated or activated nothing, and Accepted
  status without governed integration still does not integrate, allocate, or
  activate the resource.

## Alternatives not selected

### Modify Context Packet Schema Version 1.0.0

Rejected because the Module is separate and reusable, existing Core versions
are immutable, and the Context Packet Profile is a later narrowing-only task.

### Add the resource directly to the existing Tool supported set

Rejected because Tool capability and Implementation versioning require a
separate governed decision and evidence lifecycle.

### Select SHA-256 as the only digest algorithm

Rejected because ARCH-038 and ARCH-040 require explicit algorithm identity and
algorithm agility without an implicit default.

### Use Format-Assertion alone for timestamps

Rejected because the Accepted vocabulary boundary does not make optional
format assertion a portable structural guarantee.

### Add custom keywords for reference or semantic checks

Rejected because they would introduce an undeclared dialect, hidden
implementation semantics, and unsupported conformance claims.

### Report one aggregate pass/fail

Rejected because ARCH-024, ARCH-038, and ARCH-040 require separate outcomes
and prohibit consequential aggregation.

## Protected history and non-decisions

The Accepted decision and status promotion change no Accepted Core schema/test,
Artifact Contract, Definition Version, existing Schema Identity/Version, Core
binding, Tool/Implementation, dependency, lock, rule, workflow, CI, setting,
tag, Release, evidence instance, H2.4 state, or historical authority record.

It creates no Profile representation or Profile Schema Resource, Context
Packet property, policy instance, digest algorithm, canonicalization, semantic
validator, public harness, supported Tool capability, release, publication,
support, certification, hosting, deployment, merge, closure, cleanup, or later
phase authority.

## Authority boundary

Issue #145 and issue-contract acceptance comment `5267576754` authorized only
the preceding Proposed candidate lifecycle. Exact-head acceptance comment
`5269689952` on candidate commit/tree
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875` establishes Accepted status.
Exact-head acceptance plus later separately authorized governed integration to
`main` allocates and activates only Definition Schema Identifier
`https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness`,
Schema Version `1.0.0`, and canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness/1.0.0`
as the integrated Accepted Schema Resource. Preparation, status promotion,
branch or repository presence, schema or JSON parsing, schema checking, case
results, static validation, Ready state, transparent non-independent
`COMMENTED` review, and mergeability cannot by themselves integrate, allocate,
activate, release, or deploy ARCH-042 or establish conformance, semantic truth,
provenance truth, freshness, approval, certification, support, release fitness,
deployment fitness, or authority.

Work stops at a new attributable exact-head EIGENAAR / Final Authority
integration gate. Merge, issue closure, branch cleanup, Profile work, Tool
expansion, CI, release, publication, support, certification, hosting,
deployment, and later phases require separate authority.
