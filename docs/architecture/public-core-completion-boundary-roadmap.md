# CNTX Public Core Completion Boundary and Remaining Layer Roadmap (ARCH-021)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted architecture decision governed by
[issue #68](https://github.com/CNTX-PROJECT/CNTX/issues/68) and recorded by
[ADR-0021](adr/0021-public-core-completion-boundary-roadmap.md). EIGENAAR /
Final Authority acceptance of the exact reviewed candidate is recorded in
issue comment `5220966638`. Governed integration to `main` adopts this exact
decision. The transparent non-independent review was Evidentiary only and did
not grant acceptance.

This decision remains subordinate to Accepted architecture, Accepted artifact
contracts, Accepted executable schemas, repository governance, security and
privacy boundaries, controlling sources, and final human authority. It changes
none of those sources.

## Purpose and decision boundary

CNTX Public Core has reached a precise boundary: its governance, conceptual
architecture, nine artifact contracts, common envelope schema, and nine
artifact-specific executable schemas form a coherent completed foundation.
That fact must not be understated, but it must not be expanded into a claim
that portable artifact representation, validation, conformance, release,
implementation, runtime, product, or deployment work is complete.

This decision therefore:

1. names the completed boundary;
2. separates distinct completion categories;
3. orders the remaining public-core decision layers by dependency;
4. identifies optional mechanisms that are not currently release-blocking;
5. keeps runtime, provider, product, and implementation work outside the
   public-core completion definition; and
6. identifies the recommended next decision category without authorizing it.

This decision is documentation-only. It creates no schema, artifact instance,
Serialization Binding, resolver, catalog, validator, validation output,
conformance protocol, implementation, release, publication, or deployment.

## Established contract-and-schema foundation

At public baseline
`366085e8a08ff65faa21b251282bd943f292f9e2`, the established foundation
contains:

- Accepted ARCH-001 through ARCH-020 and their Accepted ADR-0001 through
  ADR-0020 records;
- Accepted CONTRACT-001 through CONTRACT-009;
- one Accepted and active Common Artifact Envelope Schema Version `1.0.0`;
- nine active Contract Definition Identifier, Contract Definition Version
  `1.0.0`, and Accepted-source-binding sets;
- nine Accepted and active artifact-specific Schema Versions `1.0.0`, one for
  each canonical CNTX artifact;
- ten executable schema resources in total; and
- ten corresponding synthetic test manifests.

The nine artifact-specific schema resources cover:

1. Project Charter;
2. Workstream;
3. Task Contract;
4. Context Packet;
5. Execution Result;
6. Evidence Bundle;
7. Review Record;
8. Decision Record; and
9. State Snapshot.

This boundary is named the **completed CNTX Public Core contract-and-schema
foundation**.

It is not full public-core completion, portable artifact interoperability,
implementation completion, runtime completion, product completion,
release-readiness, hosted publication, deployment, or production readiness.

## Completion categories

Completion claims must identify their category. The following categories must
remain distinct.

| Category | Current boundary | Not implied |
| --- | --- | --- |
| Governance and architecture foundation | Accepted authority, privacy, identity, versioning, provenance, artifact-family, lifecycle, and schema-layering decisions exist. | Executable behavior, tooling, or implementation. |
| Contract definition foundation | Nine Accepted artifact contracts and nine active Contract Definition Identifier/Version/source-binding sets exist. | Artifact Instances, contract enforcement, or runtime authority. |
| Executable schema foundation | The Common Artifact Envelope and nine artifact-specific Schema Versions `1.0.0` are Accepted and active. | Portable document serialization, contract conformance, truth, approval, or interoperability. |
| Portable representation and conformance layers | Not yet defined as a complete Accepted set. | A binding, deterministic validator contract, or portable conformance claim. |
| Release-readiness and publication | Not yet decided. | A release, tag, supported-version claim, hosted publication, or deployment. |
| Runtime, workflow, provider, product, and deployment layers | Outside the required public-core specification boundary unless separately introduced. | A requirement that CNTX Public Core ship a runtime or product. |

A specification-oriented public core may eventually be release-ready without
supplying a CNTX runtime or product. This decision does not conclude that the
current public core is release-ready.

## Dependency-ordered remaining roadmap

The remaining public-core decisions are ordered below. The order is a
governance and dependency boundary, not authority to create or implement any
item.

### 1. Artifact Serialization Binding architecture

A separate architecture decision must define how an executable CNTX schema is
bound to at least one concrete artifact representation without changing its
governing contract meaning or Schema Identity.

The existing executable schemas constrain the JSON data model evaluated by
JSON Schema. They do not by themselves define the complete portable document,
byte, character, file, or stream representation of a CNTX Artifact Instance.
The media type of a Schema Resource is not an artifact Serialization Binding.

The separate decision must address, or explicitly defer with boundaries:

- artifact representation format and media type;
- charset and encoding;
- duplicate member names;
- numeric representation;
- Unicode treatment;
- member ordering;
- whitespace;
- canonicalization or explicit absence of canonicalization;
- document, file, and stream boundaries;
- binding error boundaries;
- security and privacy consequences; and
- binding identity and compatibility.

This decision decides none of those matters.

### 2. Schema-resource resolution and catalog boundary

A separate decision must define how a validation or conformance process is
supplied with, or identifies, the exact required Schema Resources and how
missing, ambiguous, conflicting, or wrong-version resources fail.

Accepted exact-version references and offline-first composition establish
constraints but do not create a registry service, catalog format, resolver
algorithm, cache, mirror, network policy, hosted authority, or retrieval
mechanism. Deterministic validation claims require an explicit resource-supply
and failure boundary before implementations can be compared portably.

This decision chooses no resolver, registry, catalog implementation, cache,
bundler, mirror, redirect, hosted schema location, or network behavior.

### 3. Validation and validation-output contract

A separate decision must distinguish at least:

- normative-contract conformance;
- executable-schema conformance;
- Artifact Instance conformance;
- Serialization Binding conformance;
- validator conformance; and
- implementation conformance.

It must define the responsibilities of validation inputs, phases, outcomes,
errors, warnings, limitations, unverifiable conditions, governing identifiers
and versions, and reproducible evidence before validator or conformance tooling
is treated as normative.

Existing schema checks and synthetic cases are governed evidence for their
specific accepted candidates. They do not define a portable validator API,
CLI, error vocabulary, validation-output format, severity model, or universal
conformance result.

This decision defines none of those mechanisms or fields.

### 4. Portable conformance evidence boundary

A separate decision must define the evidence required for portable,
reproducible conformance claims and the claims that cannot be derived from
schema validation alone.

It must preserve the Accepted distinction between evidence and approval,
identify the exact target and governing versions, disclose assumptions and
limitations, and keep final human authority intact. It must precede any
release-readiness claim that depends on interoperability or implementation
conformance.

This decision creates no conformance protocol, test runner, certification,
badge, score, threshold, quality gate, compliance service, or reference
implementation.

### 5. Public-core release-readiness and publication boundary

After the applicable preceding decisions are Accepted and integrated, a
separate decision must determine:

- which public-core components are release-blocking;
- which Accepted versions form one coherent release basis;
- which documentation and conformance evidence are required;
- which limitations and unsupported claims must remain visible; and
- whether a release, tag, supported-version claim, or publication is
  justified.

CNTX remains unreleased and pre-alpha. This decision authorizes no release,
version support policy, tag, hosted publication, distribution, or deployment.

## Required dependency rules

The remaining roadmap obeys these rules:

1. Artifact Serialization Binding architecture precedes portable Artifact
   Instance validation.
2. Schema-resource resolution and catalog boundaries precede deterministic
   multi-resource validator claims.
3. Validation and validation-output contracts precede validator or conformance
   tooling.
4. Portable conformance evidence precedes release-readiness claims about
   interoperability or implementation conformance.
5. Every roadmap item requires its own approved creation contract, Proposed
   candidate, exact-head review, separately attributable final acceptance,
   status promotion, governed integration, completion record, closure, and any
   authorized cleanup.

No roadmap entry is self-authorizing. Acceptance of this decision records the
order only.

## Optional Extension Module and Profile boundary

Extension Module and Profile mechanisms remain optional. They are not a
release blocker for the base public core while CNTX makes no claim about:

- extensions or profiles;
- negotiation or discovery;
- profile compatibility or inheritance;
- module resolution; or
- profile conformance.

Before any such mechanism or claim is introduced, its own accepted architecture
must define identity, authority, compatibility, conflict, unknown-mechanism,
privacy, and conformance boundaries. This decision defines and authorizes no
Extension Module or Profile mechanism.

## Runtime, provider, product, and implementation boundary

The public-core completion definition does not automatically require:

- workflow execution or orchestration;
- scheduling or state-transition engines;
- runtime services;
- provider adapters;
- product logic or user interfaces;
- private or reference implementations;
- deployment infrastructure or hosted services; or
- domain-specific extensions.

These may be separately governed work outside the public specification. An
implementation nevertheless cannot claim CNTX conformance before the binding,
validation, and conformance contracts applicable to that claim exist.

## Recommended next decision category

After separate acceptance and integration of ARCH-021, the recommended next
candidate category is **CNTX Core Artifact Serialization Binding
Architecture**.

ARCH-021 allocates no ARCH number, issue, branch, path, commit, representation,
technology, or authority to that future candidate. Its creation requires a new
exact-baseline contract and separately attributable EIGENAAR / Final Authority
approval.

## Security and privacy

All future bindings, catalogs, validation outputs, conformance evidence, and
publication processes remain subject to the Accepted public/private boundary.
They must not expose secrets, credentials, personal data, production
configuration, private paths, restricted source material, private project
context, provider-specific assumptions, or private implementation logic.

Neither schema validity nor a future completion label grants access,
disclosure, trust, authenticity, approval, or permission. Security and privacy
controls remain separate from declarations about them.

## Non-decisions and deferred scope

This decision does not decide or authorize concrete serialization, JSON artifact
binding, canonical JSON, media type, charset, encoding, ordering, whitespace,
Unicode, number, duplicate-name, canonicalization, digest, signature,
verification, trust, Artifact Instance, identifier generation, revision
sequencing, Extension Module, Profile, resolver, registry, catalog
implementation, cache, bundler, mirror, network access, validator,
validation-output fields, conformance tooling, code generation, migration,
template, form, checklist, rubric, prompt, API, CLI, workflow, engine,
scheduler, orchestrator, runtime, provider work, product work, private or
reference implementation, supported-version claim, release, tag, hosted
publication, or deployment.

## Lifecycle and final human authority

This Accepted document did not approve itself. Creation, repository presence,
validation, and transparent non-independent review did not grant acceptance.
EIGENAAR / Final Authority acceptance of the exact reviewed revision is
recorded in issue comment `5220966638`; governed integration to `main` adopts
exactly this decision. Acceptance and integration authorize no next roadmap
decision, implementation, release, publication, or deployment.

ARCH-021 may be changed or superseded only through a new governed decision that
identifies the affected completion categories,
dependencies, sources, compatibility consequences, and authority. Historical
Accepted sources remain preserved.

## References

- [CNTX core architecture contract](core-contract.md)
- [Contract identity and versioning](contract-identity-versioning.md)
- [Artifact contract and schema-layering architecture](artifact-contract-schema-architecture.md)
- [Common Artifact Envelope composition and packaging](common-artifact-envelope-schema-composition-packaging.md)
- [Common Artifact Envelope executable schema definition](common-artifact-envelope-executable-schema.md)
- [Artifact-specific schema family and container boundary](artifact-specific-schema-family-container-boundary.md)
- [Contract Definition identity, version, and source binding](contract-definition-identity-version-binding.md)
- [State Snapshot executable schema definition](state-snapshot-executable-schema.md)
- [Artifact contract index](../contracts/README.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0021](adr/0021-public-core-completion-boundary-roadmap.md)
- [Issue #68](https://github.com/CNTX-PROJECT/CNTX/issues/68)
