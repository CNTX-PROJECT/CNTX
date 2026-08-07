# ADR-0023: Schema Resource resolution and catalog boundary

- **Status:** Proposed
- **Date:** 2026-08-07
- **Issue:** [#72](https://github.com/CNTX-PROJECT/CNTX/issues/72)
- **Decision:** ARCH-023 — CNTX Schema Resource Resolution and Catalog Boundary

## Context

CNTX Public Core has ten Accepted JSON Schema Draft 2020-12 resources and an
Accepted Core Artifact JSON Binding Version `1.0.0`. Nine artifact-specific
resources each statically reference the exact Accepted Common Artifact
Envelope Schema Version `1.0.0`; the common resource has no external Schema
Resource dependency.

ARCH-008 already requires canonical standalone resources, exact versioned
references, identity-preserving derived bundles, offline-first supply, no
automatic network access, and fail-closed unresolved references. ARCH-021
requires an explicit resource-supply and failure boundary before deterministic
multi-resource validator claims. ARCH-022 requires exact Schema
Identifier/Version inputs but deliberately does not supply Schema Resources.

Without a separate boundary, implementations could silently differ through
mutable aliases, location inference, conflicting mappings, cache contents,
automatic retrieval, or incomplete resource graphs.

## Decision

Define a documentation-only Schema Resource resolution and catalog boundary.

Consequential resolution uses an exact Schema Resource key composed of the
canonical Schema Identifier and exact Schema Version. It begins from one exact
entry resource and one frozen caller-supplied context with governing
provenance.

A catalog view is a non-authoritative mapping over supplied resources. It
creates no identity or version, grants no acceptance or trust, uses no
consequential mutable alias, supplies at most one non-conflicting resource per
key, verifies declared identity/version, and remains frozen during one
resolution.

Normative resolution operates only over a closed context supplied before it
begins. Supply may use canonical standalone resources, a caller-controlled
mapping, or an ARCH-008 identity-preserving derived Compound Schema Document.
Retrieval and discovery remain outside normative resolution. HTTPS-shaped
identifiers grant no network authority, and automatic remote retrieval remains
disabled.

Resolution recursively determines the exact transitive static-reference
closure. It verifies the entry and dependency identities, versions, dialect,
vocabulary boundary, and provenance. Internal fragments resolve within their
resource; external references resolve only against the same frozen context.

Success requires an exact, closed, non-conflicting graph. The same entry key
and frozen context yield the same canonical reference closure independent of
mapping order, repository layout, retrieval coordinate, or linked-versus-
bundled supply.

## Current resource topology

The current Accepted topology contains:

- one Common Artifact Envelope Schema Version `1.0.0` with no external Schema
  Resource dependency; and
- Project Charter, Workstream, Task Contract, Context Packet, Execution
  Result, Evidence Bundle, Review Record, Decision Record, and State Snapshot
  Schema Versions `1.0.0`, each with exactly one external dependency on that
  exact common resource.

There are no artifact-specific-to-artifact-specific schema references and no
external resource cycle. Recording the topology creates no aggregate resource-
set identity, version, catalog, manifest, release, or compatibility line.

## Fail-closed boundary

Resolution distinguishes at least missing resources, ambiguous mappings,
conflicting content, identifier mismatch, wrong or unsupported version,
malformed resources, unsupported dialect or vocabulary requirements,
prohibited cycles or topology, unavailable/access-denied/policy-blocked supply,
unverifiable governing resource or provenance, context mutation, and resource
substitution.

No failure is ignored, guessed, repaired, redirected to a mutable alias,
satisfied from `latest` or an unrelated cache, replaced by defaults, or
reported as schema evaluation, Artifact Instance validity, contract
conformance, trust, approval, acceptance, or authority.

Portable diagnostics, codes, severities, warnings, outputs, API responses, and
CLI exit behavior remain for a later Validation and Validation Output decision.

## Evidence and non-authority

A future validation or conformance claim must be able to identify the exact
entry, transitive resource set, canonical resource keys, governing provenance,
supply form, frozen-context basis, limitations, and blocked or unresolved
conditions.

Resolution success only establishes that the exact required resource closure
was assembled from the supplied context. It proves no resource acceptance or
trust, schema evaluation success, Artifact Instance validity, Serialization
Binding conformance, contract conformance, truth, completeness, approval,
authority, interoperability, or implementation conformance.

## Security and privacy

Identifiers, catalog data, retrieval coordinates, provenance, diagnostics, and
supply metadata must not disclose secrets, credentials, personal data,
production configuration, private paths/context, restricted content, provider
configuration, or private implementation details.

Untrusted schema content remains untrusted input. Resource use must be
bounded, but this decision selects no parser, concrete limit, sandbox,
trust store, integrity algorithm, or threat-response mechanism. Automatic
network access remains excluded.

## Consequences

Positive consequences:

- exact keys prevent mutable-location substitution;
- frozen contexts make one resource closure reproducible;
- fail-closed handling exposes incomplete or conflicting supply;
- catalog non-authority preserves Accepted source precedence;
- linked and bundled supply remain identity-equivalent; and
- no automatic network access reduces security, privacy, and availability
  risk.

Tradeoff: callers must prepare the complete exact resource context before
validation. Discovery, retrieval, caching, hosted publication, diagnostics,
and implementation convenience remain separate work.

## Alternatives rejected

- Automatic HTTPS resolution: identifiers grant no network authority.
- Repository paths as keys: paths are mutable locations, not Schema Identity.
- `latest` or unversioned aliases: consequential use requires exact versions.
- First/newest conflicting mapping wins: order and recency do not resolve
  conflict.
- Catalog presence means acceptance: catalogs are non-authoritative supply
  views.
- Executable catalog/resolver now: implementation is outside this architecture
  decision.
- Canonical bytes or digest requirements: no canonicalization or digest
  algorithm is authorized.

## Deferred scope

Deferred and unauthorized: modifications to existing Accepted sources,
schemas, tests, identities, versions, or Binding Version `1.0.0`; executable
catalog, aggregate resource-set identity/version, schema, manifest, fields,
resolver, registry, cache, bundler, mirror, redirect, discovery service,
hosted authority, automatic network, trust store, digest, canonicalization,
signature, verification, Artifact Instance, validator, validation output,
error vocabulary, conformance tooling, API, CLI, workflow, runtime,
provider/product work, private/reference implementation, release, tag,
publication, or deployment.

## Exact-head acceptance gate

The candidate receives one transparent non-independent COMMENT review on its
exact head and then stops. Creation, validation, review, repository presence,
Draft state, and mergeability grant no acceptance. Ready transition, Accepted
promotion, merge, completion, closure, synchronization, cleanup, and later
roadmap work require separate attributable EIGENAAR / Final Authority.

## References

- [ARCH-023](../schema-resource-resolution-catalog-boundary.md)
- [ARCH-006](../common-artifact-envelope-schema-identity-version-policy.md)
- [ARCH-008](../common-artifact-envelope-schema-composition-packaging.md)
- [ARCH-009](../common-artifact-envelope-executable-schema.md)
- [ARCH-021](../public-core-completion-boundary-roadmap.md)
- [ARCH-022](../core-artifact-serialization-binding.md)
- [Schema Resource index](../../../schemas/README.md)
