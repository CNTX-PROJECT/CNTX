# CNTX Schema Resource Resolution and Catalog Boundary (ARCH-023)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed, documentation-only architecture decision governed
by [issue #72](https://github.com/CNTX-PROJECT/CNTX/issues/72) and recorded by
[ADR-0023](adr/0023-schema-resource-resolution-catalog-boundary.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in
issue comment `5221792750`. Creation, repository presence, validation, and a
transparent non-independent review do not grant acceptance.

This proposal remains subordinate to Accepted architecture, artifact
contracts, executable schemas, repository governance, security and privacy
boundaries, controlling sources, and final human authority. It changes none of
those sources.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
express permission. These terms express requirement strength only within this
Proposed decision.

## Purpose and decision boundary

CNTX Public Core has ten Accepted JSON Schema resources and an Accepted Core
Artifact JSON Serialization Binding. A validation or conformance process still
needs an exact, deterministic boundary for supplying the entry Schema Resource
and every externally referenced Schema Resource before evaluation can begin.

Accepted exact-version references and offline-first composition already forbid
automatic network retrieval and silent substitution. They do not yet define a
complete catalog boundary, frozen resolution context, transitive resource
closure, conflict treatment, wrong-version handling, or the evidence needed to
identify the resource graph used for one validation attempt.

This decision therefore defines:

1. the exact key used to identify a Schema Resource;
2. the non-authoritative role of a catalog view;
3. the boundary between resource supply, retrieval, and resolution;
4. the frozen context used for one resolution;
5. the required transitive static-reference closure;
6. fail-closed resolution conditions;
7. determinism and evidence expectations; and
8. security, privacy, and non-authority limits.

This decision is not a catalog artifact, catalog schema, manifest, resolver,
registry, cache, bundler, mirror, redirect, discovery service, hosted schema
authority, validator, validation-output contract, implementation, release,
publication, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Final human authority, bounded tasks, evidence-before-claims, security/privacy, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Schema identity, version, status, implementation, digest, location, and provenance remain distinct; names and locations grant no authority. |
| [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) | A consequential Schema Resource reference identifies the logical schema through its concrete identifier and pins an exact Schema Version; mutable locations and `latest` do not replace that pin. |
| [ARCH-007](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) | JSON Schema Draft 2020-12, required dialect declaration, and standard-vocabulary boundary remain governing inputs rather than resolver implementation choices. |
| [ARCH-008](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) | Canonical standalone resources, static exact-version references, identity-preserving derived bundles, offline-first supply, no automatic network access, and fail-closed unresolved references remain mandatory. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) through [ARCH-020](state-snapshot-executable-schema.md), with their ADRs | Ten Accepted Schema Versions `1.0.0`, their canonical `$id` values, current reference graph, schema assertions, and independent version lines remain unchanged. |
| [ARCH-021](public-core-completion-boundary-roadmap.md) and [ADR-0021](adr/0021-public-core-completion-boundary-roadmap.md) | Schema-resource resolution and catalog boundaries precede deterministic multi-resource validation claims and remain separate from validation/output, conformance, and release decisions. |
| [ARCH-022](core-artifact-serialization-binding.md) and [ADR-0022](adr/0022-core-artifact-serialization-binding.md) | Exact artifact-specific Schema Identifier/Version inputs remain external governing inputs; serialization conformance and resource resolution remain separate. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Resource resolution changes no contract purpose, authority boundary, artifact relationship, provenance, lifecycle, security, or privacy meaning. |

## Terminology

| Term | Meaning in this decision | Not implied |
| --- | --- | --- |
| **Schema Resource key** | The exact concrete canonical Schema Identifier plus exact Schema Version used for consequential lookup. | Repository path, filename, branch, tag, release, alias, trust, acceptance, or authority. |
| **Entry Schema Resource** | The exact artifact-specific or common Schema Resource from which one resource-closure operation begins. | Artifact Instance validity or permission to evaluate data. |
| **Supplied resource context** | The closed set and mapping of Schema Resources made available by a caller before normative resolution begins. | Discovery, retrieval authority, network access, or acceptance. |
| **Frozen resolution context** | The supplied context whose keys, mappings, content, and provenance remain unchanged throughout one resolution. | A persistent registry, cache, catalog file, or implementation object. |
| **Catalog view** | A non-authoritative exact-key mapping over supplied Schema Resources and provenance. | A new schema identity, accepted aggregate resource set, source of meaning, or trust store. |
| **Resolved resource closure** | The entry Schema Resource and all transitively required external Schema Resources resolved from the same frozen context. | Schema evaluation success, Artifact Instance validity, contract conformance, or authority. |
| **Retrieval coordinate** | A location from which content might be obtained before supply. | Canonical identity, version, acceptance, trust, or permission to retrieve. |
| **Identity-preserving bundle** | A derived Compound Schema Document satisfying ARCH-008 while retaining every embedded resource's canonical `$id`. | Canonical standalone content, byte equality, or a new accepted resource identity. |

## Exact Schema Resource key

Consequential resolution MUST receive or identify all of:

1. the concrete canonical Schema Identifier expressed by the governing `$id`;
2. the exact Schema Version;
3. the required entry Schema Resource;
4. one frozen caller-supplied resolution context; and
5. provenance to the governing Accepted Schema Resource and applicable
   revision.

Schema Identifier and Schema Version remain separate dimensions even where a
version-qualified `$id` contains the version lexically. Matching strings do not
collapse identity, version, content, provenance, status, or acceptance into one
dimension.

The following MUST NOT replace an exact Schema Resource key:

- repository path or filename;
- branch, tag, release, or commit display name;
- unversioned alias, mutable alias, or `latest`;
- redirect, retrieval coordinate, or mirror address;
- cache key or implementation object identity;
- bundle-local key or JSON Pointer into an enclosing document;
- catalog position or registry record number;
- display title; or
- successful network response.

Identity, version, location, availability, supplied content, provenance,
acceptance, trust, applicability, approval, and authority remain distinct.

## Current Accepted resource graph

At baseline `34354125f010584d702c7a63e1f930cc35c496c1`, the current Accepted
resource graph is:

| Entry or common Schema Resource | Canonical `$id` | External Schema Resource dependency |
| --- | --- | --- |
| Common Artifact Envelope `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0` | None |
| Project Charter `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Workstream `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Task Contract `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Context Packet `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Execution Result `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Evidence Bundle `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Review Record `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| Decision Record `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0` | Exact Common Artifact Envelope `1.0.0` |
| State Snapshot `1.0.0` | `https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0` | Exact Common Artifact Envelope `1.0.0` |

The graph has exactly ten Accepted Schema Resources. The common resource has no
external Schema Resource dependency. Each of the nine artifact-specific entry
resources has exactly one external Schema Resource dependency, and all nine
dependencies identify the same exact Common Artifact Envelope Schema Version
`1.0.0`.

No artifact-specific resource externally references another artifact-specific
resource. Fragment-only references remain internal to their declaring
resource. No external resource cycle exists.

This graph description creates no aggregate Schema Resource Set identity,
version, release, catalog, manifest, or compatibility line. A later Accepted
schema or version change requires its own governing process and a fresh exact
resolution context.

## Catalog view boundary

A catalog view is a non-authoritative mapping from exact Schema Resource keys
to:

- one supplied Schema Resource;
- its declared Schema Identifier and Schema Version;
- governing provenance; and
- disclosed supply limitations.

A conforming catalog view MUST:

1. use exact canonical keys for consequential lookup;
2. supply at most one non-conflicting resource for one exact key;
3. verify the resource's declared canonical `$id` against the requested key;
4. preserve Schema Version as a separate governing dimension;
5. expose governing provenance rather than infer acceptance from location;
6. remain frozen throughout one resolution; and
7. fail rather than silently expand, replace, redirect, or repair the context.

A catalog view MUST NOT:

- create or allocate a Schema Identity or Schema Version;
- create an aggregate resource-set identity or version;
- declare acceptance, applicability, authenticity, trust, approval, or
  authority by itself;
- use `latest`, an unversioned alias, or a mutable alias consequentially;
- treat a retrieval coordinate as canonical identity;
- prefer one conflicting resource by mapping order, insertion order, location,
  recency, or implementation policy; or
- mutate supplied content or provenance during resolution.

This decision selects no catalog file, manifest, concrete field, schema,
serialization, identity, versioning model, repository path, storage model,
registry protocol, API, CLI, or implementation.

## Supply and retrieval boundary

Normative resolution operates only over a closed context supplied before
resolution begins. Conceptually permissible supply forms are:

1. preloaded canonical standalone Schema Resources;
2. a caller-controlled exact mapping; or
3. an identity-preserving derived Compound Schema Document conforming to
   ARCH-008.

Supply form does not change canonical Schema Resource identity, version,
meaning, acceptance provenance, or reference values.

Retrieval and discovery occur before or outside normative resolution. An
HTTPS-shaped `$id` or `$ref` does not authorize:

- network access or an HTTP request;
- redirects;
- access or disclosure;
- a hosted authority;
- trust in returned content;
- replacement by content at a similar path; or
- acceptance of a resource.

Automatic remote retrieval MUST remain disabled. A caller MAY supply content
obtained under a separately governed retrieval and access policy, but this
decision neither defines nor authorizes such policy.

This decision selects no resolver API, registry, discovery service, cache,
mirror, redirect, hosted location, network allowlist, transport, timeout,
retry, authentication, access-control, or persistence mechanism.

## Frozen resolution context

For one resolution, the following MUST remain fixed:

- entry Schema Resource key;
- supplied resource keys;
- key-to-resource mappings;
- supplied Schema Resource content;
- declared identifiers and versions;
- governing provenance; and
- disclosed supply limitations.

The context MUST NOT be extended or altered through:

- automatic network access;
- dependency discovery outside the supplied set;
- cache refresh;
- redirect following;
- `latest` selection;
- silent fallback;
- implementation defaults;
- resource replacement; or
- provenance replacement.

The same exact entry key and same frozen context MUST yield the same resolved
resource closure regardless of mapping order, repository layout, filename,
retrieval coordinate, or linked-versus-bundled supply.

## Resolution closure procedure

Starting from one exact entry resource, a resolution process MUST:

1. locate the entry key exactly in the frozen context;
2. verify the supplied resource's canonical `$id` against the requested Schema
   Identifier;
3. verify the exact Schema Version;
4. verify the required `$schema` dialect declaration and supported vocabulary
   boundary;
5. identify governing Accepted provenance or disclose that it is
   unverifiable;
6. resolve fragment-only internal `$ref` values within the same Schema
   Resource;
7. resolve every external static `$ref` exactly against the same frozen
   context;
8. recursively determine the complete transitive external resource closure;
9. detect conflicting keys, prohibited topology, and external resource cycles;
10. prohibit substitutions, mutable aliases, discovery, and context mutation;
    and
11. establish resolution success only for an exact, closed,
    non-conflicting resource graph.

Linked standalone resources and an identity-preserving derived bundle MUST
produce the same canonical reference closure for the same entry key and
resource set.

Closure equivalence does not mean byte equality. A derived bundle adds an
enclosing representation while retaining embedded resource identities. This
decision selects no canonical bytes, deterministic bundling, content-digest
algorithm, signature, or verification mechanism.

## Fail-closed resolution conditions

The following conditions MUST remain distinguishable:

1. missing Schema Resource;
2. ambiguous mapping;
3. conflicting content for the same exact key;
4. canonical Schema Identifier mismatch;
5. wrong Schema Version;
6. unsupported Schema Version;
7. malformed or unreadable Schema Resource;
8. missing or unsupported `$schema` dialect declaration;
9. missing or unsupported vocabulary requirement;
10. prohibited external resource cycle;
11. prohibited reference topology;
12. unavailable supplied content;
13. access-denied supply;
14. policy-blocked supply;
15. unverifiable governing resource;
16. unverifiable acceptance provenance;
17. context mutation during resolution; and
18. resource substitution during resolution.

No resolution failure MAY be:

- ignored or guessed;
- repaired silently;
- resolved by parser, mapping, or insertion order;
- redirected to a mutable or unversioned alias;
- satisfied by `latest`;
- filled from an unrelated cache entry;
- replaced by implementation defaults;
- reported as successful schema evaluation;
- reported as Artifact Instance validity;
- reported as normative-contract conformance; or
- interpreted as trust, approval, acceptance, or authority.

This decision defines no portable error code, diagnostic text, severity,
warning model, output field, validation report, API response, or CLI exit code.
Those remain for a separate Validation and Validation Output decision.

## Determinism and evidence boundary

For one future validation or conformance claim, evidence MUST be able to
identify or disclose:

- exact entry Schema Identifier and Schema Version;
- complete transitive Schema Resource set;
- every concrete canonical resource key;
- governing Accepted provenance;
- supply form;
- frozen-context basis;
- supply and implementation limitations; and
- every blocked, missing, unresolved, ambiguous, conflicting, or unsupported
  condition.

This decision creates no Evidence Bundle, validation output, catalog manifest,
digest, signature, verifier, conformance protocol, test runner,
certification, or badge.

Resolution success establishes only that the exact required resource closure
was assembled within the supplied context. It does not establish:

- Schema Resource acceptance, applicability, or trust;
- executable-schema evaluation success;
- Artifact Instance validity;
- Serialization Binding conformance;
- normative-contract conformance;
- truth or completeness;
- approval or authority;
- interoperability; or
- implementation conformance.

## Separation matrix

| Dimension | Decided here | Not decided or implied |
| --- | --- | --- |
| Resource key | Exact canonical Schema Identifier plus exact Schema Version | Path, filename, alias, catalog position, or trust |
| Entry selection | Exact caller-supplied entry key | Discovery, latest-wins, filename inference, or negotiation |
| Catalog view | Frozen non-authoritative exact-key mapping | Catalog artifact, schema, identity, version, API, or implementation |
| Supply | Closed preloaded, caller-mapped, or identity-preserving bundled context | Retrieval authority, hosted publication, registry, or network |
| Retrieval | Outside normative resolution | HTTP behavior, redirects, authentication, cache, mirror, or service |
| Resolution | Exact transitive static-reference closure | Schema evaluation, validation output, or contract conformance |
| Failure | Fail closed for missing, ambiguous, conflicting, wrong-version, and related conditions | Portable error vocabulary, severity, or output format |
| Determinism | Same entry and frozen context yield the same canonical closure | Byte equality, canonicalization, digest, or reproducible bundling |
| Provenance | Governing resource and revision remain visible | Acceptance, authenticity, trust, approval, or authority by possession |
| Network | Automatic access disabled | Network allowlist, retrieval protocol, timeout, or implementation |
| Document Status | Proposed pending exact-head acceptance | Acceptance through creation, validation, review, or presence |

## Security and privacy

Schema identifiers, catalog data, retrieval coordinates, provenance,
diagnostics, and supply metadata MUST NOT expose secrets, credentials, personal
data, production configuration, private paths or context, restricted source
content, provider-specific configuration, or private implementation details.

Resolution or catalog possession grants no access, disclosure, retrieval
permission, authenticity, integrity, confidentiality, trust, approval,
acceptance, or authority. Untrusted Schema Resource content remains untrusted
input.

Implementations must be able to bound resource use. This decision selects no
size, depth, resource-count, recursion, timeout, memory, sandbox, parser,
trust-store, integrity-check, or threat-response mechanism. An unsupported or
exceeded limitation MUST remain visible and MUST NOT be reported as successful
resolution, schema validity, or contract conformance.

Automatic network access remains excluded so normative resolution does not
create an implied server-side request forgery, redirect, tracking,
dependency-substitution, availability, or confidentiality surface.

## Consequences and tradeoffs

The selected boundary favors deterministic, caller-controlled, offline
evaluation preparation:

- exact keys prevent mutable-location substitution;
- a frozen context makes one resolution reproducible;
- fail-closed behavior prevents incomplete graphs from appearing valid;
- catalog non-authority preserves Accepted source precedence;
- supply-form neutrality permits standalone and bundled use without identity
  rewriting; and
- network exclusion reduces non-determinism and security/privacy exposure.

The tradeoff is that callers must prepare the exact resource context before
validation. Convenience discovery, hosted retrieval, caching, diagnostics, and
implementation APIs remain separately governed work.

## Alternatives rejected

- Resolve canonical HTTPS identifiers automatically: rejected because an
  identifier grants no network authority and automatic retrieval introduces
  security, privacy, availability, and determinism risks.
- Use repository-relative paths as consequential keys: rejected because file
  layout is mutable and not Schema Identity.
- Permit `latest` or unversioned aliases: rejected because consequential
  resolution requires exact version pins.
- Prefer the first or newest conflicting mapping: rejected because mapping
  order or recency cannot resolve identity/content conflict.
- Treat catalog presence as acceptance: rejected because a catalog is
  non-authoritative supply orientation.
- Define an executable catalog or resolver now: rejected because this decision
  is the architecture boundary preceding implementation and validation output.
- Require canonical bytes or digests: rejected because ARCH-022 selects no
  canonicalization and no digest algorithm is authorized here.

## Deferred scope and explicit non-actions

Deferred and unauthorized: changes to earlier Accepted architecture,
contracts, schemas, tests, identities, versions, or Core Artifact JSON Binding
Version `1.0.0`; catalog artifact, aggregate resource-set identity/version,
catalog schema, manifest, file, or concrete fields; resolver, registry, cache,
bundler, mirror, redirect, discovery service, hosted schema authority, or
automatic network access; trust store, digest, canonicalization, signature, or
verification; Artifact Instance; validator, validation output, error
vocabulary, conformance protocol, or conformance tooling; code generation,
migration, template, form, checklist, rubric, prompt, API, CLI, workflow,
engine, scheduler, orchestrator, runtime, provider/product work,
private/reference implementation, supported-version claim, release, tag,
hosted publication, or deployment.

## Review, acceptance, and final human authority

This Proposed document cannot approve itself. Creation, repository presence,
validation, Draft PR state, mergeability, and transparent non-independent
review grant no acceptance, merge permission, issue-closure authority, or
follow-on authority.

Only separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision can authorize a status-only promotion. Ready transition,
merge, completion, closure, synchronization, cleanup, validation/output,
conformance, release, publication, and deployment remain separately governed.

## References

- [CNTX core architecture contract](core-contract.md)
- [Contract identity and versioning](contract-identity-versioning.md)
- [Common Artifact Envelope schema identity and version policy](common-artifact-envelope-schema-identity-version-policy.md)
- [Common Artifact Envelope schema language and dialect](common-artifact-envelope-schema-language-dialect.md)
- [Common Artifact Envelope composition and packaging](common-artifact-envelope-schema-composition-packaging.md)
- [Common Artifact Envelope executable schema](common-artifact-envelope-executable-schema.md)
- [Artifact-specific schema family and container boundary](artifact-specific-schema-family-container-boundary.md)
- [Public Core completion boundary and roadmap](public-core-completion-boundary-roadmap.md)
- [Core Artifact JSON serialization binding](core-artifact-serialization-binding.md)
- [Schema Resource index](../../schemas/README.md)
- [Artifact contract index](../contracts/README.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0023](adr/0023-schema-resource-resolution-catalog-boundary.md)
- [Issue #72](https://github.com/CNTX-PROJECT/CNTX/issues/72)
