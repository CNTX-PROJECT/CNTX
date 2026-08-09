# ADR-0031: CNTX Extension Module and Profile Schema Resource, packaging, and declaration model

- **Status:** Proposed
- **Date:** 2026-08-09
- **Issue:** [#104](https://github.com/CNTX-PROJECT/CNTX/issues/104)
- **Creation authority comment:** [5230355484](https://github.com/CNTX-PROJECT/CNTX/issues/104#issuecomment-5230355484)
- **Decision:** ARCH-031 — CNTX Extension Module and Profile Schema Resource,
  Packaging and Declaration Model

## Context

Accepted ARCH-028 defines the Extension Module/Profile conceptual boundary.
Accepted ARCH-029 defines separate Definition identity and version dimensions.
Accepted ARCH-030 defines exact dependencies, explicit activation, finite
closure, deterministic composition without precedence, and fail-closed conflict
handling.

No Accepted decision yet separates future Definition Schema identity/version
from Definition identity/version, defines the permitted Schema Resource form
and graph, establishes a closed package boundary, or states how one frozen
active Definition Set is declared outside existing Core Artifact Instances and
Core Artifact JSON. Executable-schema work cannot safely precede those
boundaries.

## Decision

Define two logical and separate schema categories:

1. `CNTX Extension Module Definition Schema Family`;
2. `CNTX Profile Definition Schema Family`.

Keep Definition category, Definition Identifier/Version, Definition Schema
Identifier, Schema Version, canonical `$id`, Schema Resource content,
Definition and resource sources/revisions/provenance, package, declaration,
activation, applicability, acceptance, authority, compatibility, conformance,
implementation support, lifecycle, and release status separate. Definition
Version and Schema Version never imply lockstep.

A later concrete Definition may receive at most one logical schema identity in
the correct family, but only through a separate exact allocation and acceptance
lifecycle. Do not allocate a family namespace, concrete Schema Identifier,
Schema Version, `$id`, path, or file in this decision.

Require each active Definition key in one frozen context to declare exactly one
Schema Resource key or explicit `None`. A missing declaration is not `None`.
Repository/path/filename/URL/catalog/cache/network/installation/product state,
mutable aliases, prior validation, package position, and load order cannot
select the binding. A binding neither activates nor authorizes a Definition and
cannot alter Core or Definition meaning.

For each later separately Accepted Definition Schema Version, require one
canonical standalone root Schema Resource using JSON Schema Draft 2020-12,
root `$schema`, one future version-qualified absolute HTTPS `$id` without
fragment, `application/schema+json`, internal `$defs`, static references, no
nested `$id`, no initial public anchors, no dynamic references, no custom
dialect/vocabulary, no Format-Assertion, and no Hyper-Schema. Accepted
standalone content is immutable per exact Schema Version.

Align the external Schema Resource graph with ARCH-030:

- Core schemas never refer to Extension Module/Profile schemas;
- Module schemas may refer only to exact Core and active Module dependency
  resources, never Profile schemas;
- Profile schemas may refer only to exact Core and Module subject/dependency
  resources, never other Profile schemas;
- the graph is finite, acyclic, caller-supplied, exact-versioned, and justified
  by the governing Definition graph; and
- `$ref` creates no Definition dependency, activation, authority, or
  precedence.

Keep existing closed Core schemas closed. Extension/Profile material cannot
make Core-invalid input Core-valid. Graph mismatch, prohibited reference,
missing/wrong resource, cycle, ambiguity, order dependence, or insufficient
evidence fails closed.

Define a logical `Definition Package` as a closed caller-supplied grouping for
one frozen context. It may group exact Definition keys, sources/revisions,
dependencies, Profile Subjects, schema key-or-`None` bindings, standalone
resources, provenance, capabilities, limitations, conflicts, and restricted
evidence. It is not an Artifact Instance, identity/version, normative source,
manifest, registry/catalog, acceptance, authority, or conformance evidence.
Layout and order activate and prioritize nothing.

Permit a later derived Compound Schema Document only as non-authoritative
offline transport when every canonical `$id`, `$schema`, static reference,
independent resource identity, standalone behavior, resource set, and
provenance remain unchanged. Bundling creates no identity, authority, release,
canonical bytes, digest, signature, attestation, or certification.

Define a logical `Governing Definition Declaration` for one exact active
Definition key. Its responsibilities are Definition category, Identifier,
Version, authoritative source/revision/provenance, activation roles, exact
required and optional dependencies, Profile Subjects, exact Schema Resource
key-or-`None`, resource source/revision/provenance, package/context provenance,
capabilities, limitations, claim scope, unknown/unsupported/adverse/unresolved/
restricted-evidence conditions, attributable authority, and lifecycle
traceability. These responsibilities allocate no fields or tokens.

Define a frozen `Governing Declaration Set` equal to the ARCH-030 active
Definition Set. It is complete for roots and required closure, contains only
explicitly active optional dependencies, keeps Profiles as separate roots,
contains exactly one duplicate-free declaration for every active key, permits
at most one active version per Identifier, preserves exact source/revision
consistency, records a schema key or `None`, stays frozen, and exposes every
limitation and conflict.

Keep that declaration set a separate governing input outside the Common
Artifact Envelope, all nine artifact-specific payloads, every existing Core
Artifact Instance, and Core Artifact JSON. Add no property or Serialization
Binding. A future serialized declaration requires a separate decision.

Preserve ARCH-023 caller-supplied, closed, frozen, offline-first resolution.
There is no automatic discovery, retrieval, redirect, network access, mutable
alias, hidden cache, substitution, repair, or fallback.

Treat declaration mismatch, active-set or dependency mismatch, implicit schema
participation, missing/wrong/unsupported resource or dialect, prohibited
reference, cycle, package collision, identity-changing bundle, order-dependent
result, unsupported capability, insufficient provenance, required restricted
evidence, security/privacy conflict, and unbounded resource conditions as
separately visible and fail closed. No order, newest/latest, popularity,
implementation preference, cache, previous success, majority, consensus,
ranking, or fallback can resolve them silently.

Keep Core, Definition, declaration, package, Schema Resource, executable-schema,
contract, validator, implementation, interoperability, compatibility, support,
security/privacy, certification, and release conformance separate. Schema
validity proves none of the broader dimensions and creates no aggregate result.

Treat every source, resource, package, declaration, and context as untrusted.
Preserve resource, recursion, cost, minimization, restricted-evidence,
disclosure, public/private, lifecycle, historical-integrity, and final-human-
authority boundaries without choosing an implementation.

## Consequences

Positive consequences:

- Definition and Schema identity/version remain independently governable;
- every active Definition has an explicit and reproducible schema-binding
  state;
- future resources use one constrained standalone model;
- the schema graph cannot silently alter the Accepted Definition graph;
- package and bundle transport cannot create authority or mutate identity;
- the governing declaration context is complete, frozen, and outside Core
  artifacts; and
- unknown, unsupported, conflicting, and resource-limited conditions remain
  visible and fail closed.

Costs and limitations:

- callers must supply complete exact sources, declarations, resources, and
  provenance before evaluation;
- no implicit discovery, retrieval, cache, version selection, or fallback is
  available;
- `None` must be declared explicitly and cannot stand in for a failure;
- existing Artifact Instances carry no embedded governing declaration;
- no concrete identity, field, schema, package representation, resolver,
  validator, or output vocabulary exists; and
- compatibility, interoperability, security/privacy, support, and
  certification remain unproven.

## Alternatives not selected

### Derive schema identity from Definition identity

Not selected because Definition and Schema identity/version are separate
dimensions with independent lifecycle, provenance, and compatibility effects.

### Infer a schema binding from repository or package presence

Not selected because availability does not establish exact governing intent,
acceptance, activation, applicability, or authority.

### Embed declarations in current Core artifacts

Not selected because it would change the Accepted envelope, artifact schemas,
payload semantics, and Core Artifact JSON Binding before a separate placement
and serialization decision.

### Let schema references define dependencies or activation

Not selected because `$ref` is a Schema Resource relationship and cannot
replace ARCH-030 Definition dependency and explicit activation semantics.

### Treat a package or bundle as the normative source

Not selected because transport grouping must not replace independent
authoritative sources, resource identities, provenance, or acceptance.

### Define executable schemas now

Not selected because this decision must first establish the conceptual identity,
resource, graph, package, declaration, supply, and failure boundaries.

## Non-decisions

This ADR creates no concrete Extension Module/Profile, child Definition
Identifier/Version, Definition Schema Identifier/Version, `$id`, resource,
schema file, executable assertion/test/payload, declaration field/token,
Artifact/Extension/Profile/package instance, package identity/version,
manifest, portable output vocabulary, custom dialect/vocabulary,
Format-Assertion, Hyper-Schema, dynamic references, media type, or new
Serialization Binding.

It creates no resolver, registry, catalog, cache, bundler, mirror, redirect,
discovery, retrieval, network access, validator, runner, conformance suite,
canonical JSON, digest, signature, verification, attestation, certification,
API, CLI, workflow, automation, runtime/provider/product work,
private/reference implementation, support service, release, publication,
distribution, deployment, maintenance action, settings mutation, ARCH-032, or
follow-on authority.

## Authority boundary

This ADR is Proposed. Creation authority, repository presence, validation, and
transparent non-independent ARCHITECT review do not grant acceptance.

Separate attributable EIGENAAR / Final Authority exact-head acceptance and
separately authorized governed promotion and integration are required before
this decision can become Accepted. Acceptance would adopt only the conceptual
model and would create or activate no concrete Definition, schema, declaration,
package, tooling, implementation, release, publication, or deployment.
