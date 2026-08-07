# ADR-0015: Context Packet executable schema definition

- **Status:** Accepted
- **Date:** 2026-08-07
- **Decision owners:** Cintao66, Owner / Final Authority
- **Issue:** [#56](https://github.com/CNTX-PROJECT/CNTX/issues/56)
- **Owner acceptance:** issue comment `5216466742`
- **Governing architecture:** [ARCH-015](../context-packet-executable-schema.md)

Owner / Final Authority acceptance of the exact reviewed candidate is recorded
in issue comment `5216466742`. On governed integration to `main`, Context
Packet Schema Version `1.0.0` becomes active under repository governance.
Exact-head operational review was transparently non-independent and did not
grant final acceptance.

## Context

ARCH-010 allocated the Context Packet logical Schema Identity, inactive
`1.0.0` target, closed `envelope`/`payload` root, and exact Common
Artifact Envelope dependency. ARCH-011 activated the exact Context Packet
Contract Definition Identifier/Version. CONTRACT-004 defines the authoritative
derived-context meaning, responsibility model, and non-authority boundary.

Accepted Project Charter, Workstream, and Task Contract schemas establish the
dependency-first rollout context, but their existence neither authorizes this
candidate nor requires executable schema coupling.

## Decision

CNTX adopts one JSON Schema Draft 2020-12 resource at
`schemas/context-packet/1.0.0/schema.json`, with canonical identity
`https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0`.

The resource evaluates a closed root with exactly required `envelope` and
`payload`. The envelope uses exactly one static external `$ref` to the
Accepted Common Artifact Envelope Schema Version `1.0.0` and overlays only
the Context Packet Artifact Type and exact governing Contract and Schema
coordinates.

The closed payload requires exactly thirteen direct properties:

1. `governingTaskContract`;
2. `selectionPurpose`;
3. `applicableGoverningContext`;
4. `selectedSources`;
5. `exclusionsAndForbiddenContext`;
6. `provenanceAndPinning`;
7. `freshnessAndApplicability`;
8. `assumptionsDependenciesAndUncertainty`;
9. `transformationAndRedaction`;
10. `securityPrivacyAndAccess`;
11. `sufficiencyAndMinimization`;
12. `stopAndEscalation`; and
13. `lifecycleAndExecutionTraceability`.

The governing Task Contract is an opaque Artifact Instance/Revision pin, not
an embedded artifact or schema `$ref`. Selected sources are closed
provenance-bearing entries with opaque references, relevance rationale,
revision/version assessment, included-material assessment, limited
representation-treatment tokens, authority/applicability context, and known
loss/limitations.

Declaration sets are exactly `specified` with non-empty unique non-blank
items or assessed `none` without items. Every defined object is closed;
required ordinary arrays are non-empty and unique; ordinary strings are
non-blank.

The resource contains one root `$schema`, one root `$id`, internal
fragment-local `$defs` references, and exactly one external common-envelope
reference. It contains no Project Charter, Workstream, Task Contract, peer,
Execution Result, or downstream schema reference; dynamic reference; anchor;
`format`; default; custom vocabulary; or public subschema API.

## Rationale

The design translates only CONTRACT-004 into structural assertions while
preserving the Accepted container, identity/version, common-envelope,
authority, and dependency architecture.

Opaque pins and references retain traceability without coupling independent
schemas or pretending JSON Schema can establish source existence,
applicability, approval, access, or authority. Closed objects and explicit
declaration sets fail closed and distinguish assessed absence from omission.

Representation-treatment tokens describe what happened to content without
implementing the transformation. Selection purpose, relevance, freshness,
security, access, sufficiency, minimization, stop, and lifecycle fields remain
human-reviewable declarations rather than executable behavior.

## Consequences and tradeoffs

- The thirteen CONTRACT-004 responsibility groups become structurally
  explicit.
- Governing and source traceability remains declarative and independently
  governed.
- Closed shapes improve reviewability and reject silent extension.
- Lexically broad statements preserve model, provider, runtime, product, and
  domain independence.
- Explicit declarations and complete source entries are verbose.
- Schema validity cannot prove relevance, sufficiency, minimality, authority,
  access, disclosure permission, freshness, security, privacy, or execution
  suitability.

## Authority and conformance boundary

The schema creates no Context Packet Artifact Instance and allocates no
Artifact Instance Identifier or Revision. It neither retrieves nor validates
the governing Task Contract or selected sources. A valid reference grants no
access or disclosure permission. A valid constraint enforces nothing beyond
shape.

Conformance means only structural validity under this exact Accepted schema
and the exact locally supplied common-envelope resource. It does not prove
CONTRACT-004 semantic conformance, approval, task authority, provenance truth,
selection quality, review, acceptance, release, deployment, or merge
permission.

## Validation evidence

The non-normative manifest contains exactly twenty ordered public-safe
synthetic cases. Validation uses Draft 2020-12 with the exact common resource
registered locally and no network retrieval. Failure when that resource is
absent demonstrates the explicit dependency.

Validation also checks strict duplicate-free JSON, UTF-8 without BOM, root and
nested closure, exact constants, the thirteen-property payload, one opaque
Task Contract pin, selected-source treatments, declaration sets, non-blank
strings, non-empty unique arrays, reference locality, protected baseline
blobs, exact eight-path scope, links, and privacy/security boundaries.

## Security and privacy

Fixtures contain no secrets, credentials, personal data, production
configuration, private paths, restricted source content, or private
implementation details. The schema declares security/privacy/access
constraints but provides no enforcement, credential, retrieval, redaction,
sanitization, or disclosure mechanism.

## Rejected alternatives

Rejected alternatives include open or flattened artifacts, copied/weakened or
dynamic common content, embedded or schema-referenced artifacts, unrestricted
context dumps, automatic selection/retrieval/ranking/RAG, prompt and token
mechanisms, executable access/disclosure policies, transformation algorithms,
mandatory network resolution, approval/signature/trust fields, timestamps and
state machines, workflows and runtimes, unknown fields, null/placeholders, and
review or validation as acceptance.

## Deferred scope

Deferred and unauthorized work includes artifact instances, identifier or
revision allocation, artifact-specific schema references, retrieval, search,
ranking, RAG, embedding, vector storage, prompt assembly, token/chunk handling,
transformation/redaction/sanitization algorithms, access/disclosure
mechanisms, Serialization Binding, canonical JSON, validator and output
contract, resolver, registry, catalog, cache, bundler, network access,
conformance tooling, code generation, migration, template, form, prompt, API,
CLI, workflow, engine, scheduler, orchestrator, runtime, implementation,
provider/product work, release, tag, hosted publication, and deployment.

## Continuing gate

The exact reviewed candidate was accepted by the Owner / Final Authority in
issue comment `5216466742`. Governed integration to `main` activates exactly
Context Packet Schema Version `1.0.0`. No Execution Result or later schema work
is automatically authorized.
