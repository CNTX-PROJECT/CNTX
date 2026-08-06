# CNTX Artifact-Specific Schema Family and Canonical Artifact Container Boundary (ARCH-010)

## Status and authority

**Document Status:** Accepted.

This document is a documentation-only accepted architecture decision governed by
[issue #44](https://github.com/CNTX-PROJECT/CNTX/issues/44) and recorded by
[ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md).
Owner / Final Authority creation authority is recorded in issue comment
`5209318215`. The Owner / Final Authority separately accepted exact reviewed
candidate head `5e8d003ffd6d6f27cfb53201a6d55c570a7b99e4`.

This Accepted decision adds only the documented boundary to Accepted
architecture. It creates no
artifact-specific executable Schema Resource, concrete artifact-specific
`$id`, repository schema file, active artifact-specific Schema Version,
payload definition, Serialization Binding, validator, runtime, product,
release, or deployment.

## Purpose and decision boundary

The Accepted Common Artifact Envelope Schema Version `1.0.0` evaluates one
envelope object only. Before an artifact-specific executable schema can be
considered, CNTX needs one stable documentation-only answer to four remaining
architecture questions:

1. which artifact-specific logical Schema Identities belong to the CNTX Public
   Core Schema Family;
2. what the uniform root of a complete canonical Artifact Instance is;
3. where and how the Accepted Common Artifact Envelope is evaluated relative
   to the artifact-specific payload; and
4. in which dependency order later artifact-specific executable-schema tasks
   may be considered.

ARCH-010 answers only those questions. It allocates technology-neutral logical
identities and inactive initial version targets, selects a closed two-member
full-artifact root, fixes the exact common-envelope reference boundary, and
preserves independent artifact-specific payload ownership. It does not define
the payload of any artifact or create an executable resource.

## Governing traceability

| Governing source | Preserved requirement |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | CNTX remains public, bounded, model-, provider-, runtime-, and domain-independent; human final authority and public/private boundaries remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Artifact, contract, schema, revision, version, provenance, approval, implementation, release, and deployment dimensions remain distinct. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | Schema Family organization, independently reviewable artifact-specific definitions, upward dependency direction, and distinct conformance targets are preserved. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) | Common-envelope ownership remains limited to universal and activated conditional concepts; payload and relationship meaning remain artifact-specific. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) | Semantic coupling, absence behavior, payload separation, and the dependency-first schema-foundation order remain controlling. |
| [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) | Logical identity is allocated before lexical encoding; initial targets are inactive until exact-revision acceptance and governed integration. |
| [ARCH-007](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) | JSON Schema Draft 2020-12 and the standard-vocabulary-only boundary govern future executable resources. |
| [ARCH-008](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) | Standalone resources, static exact-version references, immutable accepted content, offline-first resolution, and no automatic network access remain mandatory. |
| [ARCH-009](common-artifact-envelope-executable-schema.md), [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md), and [Schema Version `1.0.0`](../../schemas/common-artifact-envelope/1.0.0/schema.json) | The exact accepted envelope resource, its nine Artifact Type tokens, envelope-only evaluation scope, coupled pins, internal-only `$defs`, and non-authority boundary remain unchanged. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Each artifact retains its Accepted purpose, classification, responsibilities, relationships, lifecycle, provenance, privacy, payload meaning, and authority limits. |

## Primary standards basis

The relevant public standards sources are:

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12);
- [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core);
- [JSON Schema Validation 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation);
- the exact [Draft 2020-12 default dialect meta-schema](https://json-schema.org/draft/2020-12/schema); and
- [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986).

JSON Schema defines Schema Resources, identifiers, references, applicators,
and structural validation behavior. The exact two-member root, closed-world
rules, identity allocations, version targets, and rollout order below are
stricter CNTX architecture choices rather than requirements imposed by JSON
Schema itself.

## Terms for this decision

| Term | Meaning here |
| --- | --- |
| **Schema Family** | The organized set of separately governed common, artifact-specific, future extension/profile, binding, and conformance definitions. It is not one resource or one version line. |
| **Artifact-specific logical Schema Identity** | One technology-neutral identity allocation for the future executable definition of one complete canonical Artifact Type. |
| **Canonical full-artifact root** | The uniform object evaluated by a future artifact-specific Schema Resource, containing exactly `envelope` and `payload`. |
| **Envelope dependency** | The exact static dependency from an artifact-specific resource to the Accepted Common Artifact Envelope Schema Version `1.0.0`. |
| **Artifact-specific payload** | The contract-owned object whose meaning and future executable assertions are unique to one canonical artifact. |

## Schema Family organization

The CNTX Public Core Schema Family conceptually contains:

1. the one Accepted Common Artifact Envelope Schema Identity and its Accepted
   Schema Version `1.0.0`;
2. exactly nine separately governed artifact-specific logical Schema
   Identities;
3. future Extension Module Schema Identities only after a separate Accepted
   mechanism;
4. future Profile Schema Identities only after a separate Accepted mechanism;
5. future Serialization Bindings governed separately from Schema Resources;
   and
6. future conformance fixtures or tooling that remain evidence or
   implementation rather than schema authority.

The Schema Family is an organizational relationship. It is not one monolithic
Schema Resource, global `$id`, family-wide Schema Version, repository
directory, bundle, archive, release, registry, resolver, validator, runtime,
product, or authority source.

The Accepted Common Artifact Envelope is the only required shared executable
Schema Resource selected at this stage.

## Artifact-specific logical Schema Identity allocations

ARCH-010 allocates exactly these nine technology-neutral identities:

| Order | Contract | Artifact Type token | Logical namespace | Logical local Schema Identity | Initial accepted Schema Version target |
| --- | --- | --- | --- | --- | --- |
| 1 | CONTRACT-001 | `project-charter` | CNTX Public Core Schema Family | Project Charter Artifact | `1.0.0` |
| 2 | CONTRACT-002 | `workstream` | CNTX Public Core Schema Family | Workstream Artifact | `1.0.0` |
| 3 | CONTRACT-003 | `task-contract` | CNTX Public Core Schema Family | Task Contract Artifact | `1.0.0` |
| 4 | CONTRACT-004 | `context-packet` | CNTX Public Core Schema Family | Context Packet Artifact | `1.0.0` |
| 5 | CONTRACT-005 | `execution-result` | CNTX Public Core Schema Family | Execution Result Artifact | `1.0.0` |
| 6 | CONTRACT-006 | `evidence-bundle` | CNTX Public Core Schema Family | Evidence Bundle Artifact | `1.0.0` |
| 7 | CONTRACT-007 | `review-record` | CNTX Public Core Schema Family | Review Record Artifact | `1.0.0` |
| 8 | CONTRACT-008 | `decision-record` | CNTX Public Core Schema Family | Decision Record Artifact | `1.0.0` |
| 9 | CONTRACT-009 | `state-snapshot` | CNTX Public Core Schema Family | State Snapshot Artifact | `1.0.0` |

Each namespace/local-identity pair identifies one future executable definition
for one complete canonical artifact type. The identity remains stable across
later versions of that same definition and MUST NOT be reassigned to another
artifact, common definition, Extension Module, Profile, Serialization Binding,
validator, implementation, provider, or product.

These allocations are not concrete `$id` values, URIs, URNs, URLs, repository
paths, filenames, registry keys, resolver coordinates, media types,
serialization tokens, branches, tags, releases, Contract Definition
Identifiers, Artifact Instance Identifiers, active Schema Versions, or
evidence of acceptance, authority, compatibility, conformance, publication,
release, or deployment.

## Initial artifact-specific Schema Version policy

For each allocated identity, no executable Schema Resource and no active
Schema Version currently exists. `1.0.0` is only the initial accepted Schema
Version target.

Candidate drafting, review, corrections, replacement commits, branch names,
and pull-request revisions do not activate or consume a Schema Version. The
first exact executable definition may become Accepted as `1.0.0` only through
its own separately authorized creation, review, exact-head human acceptance,
status promotion, governed integration, and completion record.

After acceptance, that exact versioned Schema Resource is immutable. A later
Accepted semantic change requires a new independently assessed Schema Version.
The nine version lines advance independently: there is no family-wide version,
lockstep increment, or automatic propagation. A Schema Version grants no
authority, approval, trust, conformance, release, deployment, or runtime
status.

ARCH-010 binds none of the nine logical identities to a concrete `$id` or
repository path.

## Canonical full-artifact root

Every future core artifact-specific Schema Resource MUST evaluate one complete
canonical CNTX Artifact Instance. Its root is one object in the JSON Schema
JSON-compatible instance data model with exactly two direct members:

1. `envelope`; and
2. `payload`.

Both members are mandatory. A future executable resource MUST assert an object
root, `properties` consisting exactly of `envelope` and `payload`, `required`
consisting exactly of both members, and closed-root behavior equivalent to
`additionalProperties: false`.

The root MUST NOT add parallel direct members for authority, approval,
lifecycle state, artifact classification, relationships, provenance, digests,
extensions, profiles, transport metadata, storage metadata, implementation
metadata, signatures, or runtime state. Common-owned concepts remain under
`envelope`; artifact-specific normative meaning remains under `payload`.

## Exact Common Artifact Envelope placement and evaluation

The Common Artifact Envelope occurs exactly at the full-artifact instance
location `/envelope`.

The schema applied through `properties` to the `envelope` value MUST evaluate
that value through a static `$ref` to the complete Accepted Common Artifact
Envelope root. The consequential reference value is exactly:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

The future artifact-specific resource MUST:

- use this exact version-qualified canonical URI without a fragment;
- apply it at the schema location governing `envelope`;
- evaluate the envelope object, not the full-artifact root or payload;
- preserve the Accepted resource without copying, forking, shadowing,
  weakening, redefining, or selectively reproducing it;
- never reference an internal Common Artifact Envelope `$defs` member;
- never substitute a repository-relative path, branch, tag, release, bundle
  location, redirect, mirror, unversioned alias, or `latest` coordinate;
- never use `$dynamicRef`, `$dynamicAnchor`, or another dynamic override
  mechanism for this dependency;
- fail when the exact referenced resource is unavailable; and
- grant no automatic network access merely because the reference uses an
  HTTPS-shaped URI.

The `properties` application and static `$ref` are the selected applicator
boundary. The exact executable keyword arrangement surrounding later
artifact-type specialization remains for the applicable artifact-specific
schema task, provided it does not alter the common resource.

## Artifact Type specialization

Every future artifact-specific resource MUST require the envelope's
`artifactType` to equal the exact canonical token allocated to that artifact
identity. A Project Charter resource, for example, must require
`project-charter` and must not validate another canonical Artifact Type as a
Project Charter.

This specialization belongs to the artifact-specific resource. It MUST NOT
change or fork the common resource, widen the Accepted nine-token enum, treat
Artifact Type as authority or Contract Definition identity, or reverse the
dependency direction. The later executable task must prove that the exact
common `$ref` and exact Artifact Type assertion compose correctly under Draft
2020-12.

## Governing Contract and governing Schema pins

For a complete Artifact Instance:

- `envelope.governingContract` identifies the applicable artifact-specific
  Contract Definition and exact Contract Definition Version;
- `envelope.governingSchema` identifies the applicable artifact-specific
  Schema Identity and exact Schema Version;
- `envelope.governingSchema` does not identify the Common Artifact Envelope
  merely because the artifact-specific schema depends on that resource; and
- the common dependency and governing artifact-specific schema pin remain
  distinct.

Schema identity/version, Contract Definition identity/version, Artifact Type,
Artifact Instance identity/revision, Document Status, approval state,
Implementation Version, release, and deployment remain distinct. Valid pins
do not prove that their targets exist, are Accepted, are applicable, are
authoritative, or may be retrieved.

ARCH-010 does not allocate concrete Contract Definition Identifiers or
Contract Definition Versions. A later task MUST NOT invent those coordinates.
If an executable artifact-specific schema requires exact Contract Definition
constants and no Accepted allocation exists, that is a separate architecture
dependency and stop condition.

## Artifact-specific payload boundary

The artifact-specific payload occurs exactly at `/payload`. Its value is an
object whose meaning is owned exclusively by the applicable Accepted
artifact-specific contract.

A later artifact-specific executable Schema Resource MUST define and evaluate
its own payload object; implement only the Accepted responsibilities of its
contract; preserve its inherited Authoritative, Evidentiary, or Derived
classification; preserve permitted and forbidden content, relationships,
provenance, lifecycle, privacy, security, review, approval, and authority
boundaries; close the payload to unknown properties unless a separately
Accepted Extension Module or Profile mechanism governs another behavior; and
avoid duplicating Common Artifact Envelope semantics.

Relationship role, purpose, direction, multiplicity, sufficiency, freshness,
replacement, conflict, embedding, and interpretation remain artifact-specific.
ARCH-010 defines no payload field, required property, relationship
representation, cardinality, reference shape, example, fixture, or executable
constraint beyond the payload-object boundary.

## Cross-artifact dependency and reference boundary

The canonical contract dependency order governs design and rollout. It does
not automatically create schema `$ref` dependencies between artifact-specific
resources.

For the first Accepted version of each artifact-specific resource, the exact
Accepted Common Artifact Envelope Schema Version `1.0.0` is the only mandatory
external Schema Resource dependency authorized by ARCH-010. One
artifact-specific resource MUST NOT automatically reference another merely
because their contracts have a conceptual dependency.

Relationships between Artifact Instances remain artifact-specific payload
semantics and use governed identity/revision/version pinning rather than
implicit schema embedding. Cyclic schema dependencies are prohibited. A new
reusable cross-artifact resource requires separately Accepted identity,
ownership, versioning, compatibility, packaging, and authority decisions.
Each artifact-specific resource remains independently reviewable, versioned,
replaceable, and attributable.

Internal reuse within one artifact-specific resource may later use its own
root `$defs`. Those internal names are not automatically public compatibility
surfaces or shared Schema Identities.

## Dependency-first rollout order

Later artifact-specific executable-schema tasks may be considered only in
this order:

1. Project Charter / CONTRACT-001;
2. Workstream / CONTRACT-002;
3. Task Contract / CONTRACT-003;
4. Context Packet / CONTRACT-004;
5. Execution Result / CONTRACT-005;
6. Evidence Bundle / CONTRACT-006;
7. Review Record / CONTRACT-007;
8. Decision Record / CONTRACT-008; and
9. State Snapshot / CONTRACT-009.

Each task requires its own exact baseline, approved issue or Task Contract,
concrete `$id` and repository-path authority, Proposed `1.0.0` candidate,
payload definition, tests, validation, review, exact-head human acceptance,
status promotion, integration authority, and completion record. Acceptance or
integration of one artifact-specific schema does not authorize the next.

## Schema-family change and compatibility boundary

A change to the Accepted Common Artifact Envelope may affect every
artifact-specific resource that pins the changed version. Changed Accepted
common meaning requires a new Common Artifact Envelope Schema Version,
compatibility assessment against affected artifact schemas, and explicit
decisions about whether and when each artifact schema moves to that version.
Existing Accepted `$ref` values are never rewritten automatically.

An artifact-specific payload change affects its own Schema Identity and
Schema Version unless a separate Accepted cross-resource decision establishes
a broader consequence. There is no automatic family-wide increment.

## Serialization and canonical-artifact boundary

The `envelope`/`payload` container is a logical object structure in the JSON
Schema JSON-compatible instance data model. It does not select an artifact
JSON Serialization Binding, canonical JSON, member ordering, whitespace,
artifact byte encoding, duplicate-member transport behavior, YAML, CBOR,
Artifact Instance media type, transport, storage, archive, database, API,
canonicalization, digest, signature, or verification procedure.

A future Serialization Binding may map the Accepted logical structure to a
concrete representation but MUST NOT change its meaning. The full-artifact
root is not a ZIP archive, transport envelope, storage record, API message,
workflow object, or runtime object.

## Extension Module and Profile boundary

ARCH-010 creates no Extension Module or Profile mechanism. The closed root
reserves no ungoverned extension or profile member. Future extension/profile
work must separately decide identities, versions, namespaces, compatibility,
composition, payload effects, conflict behavior, conformance targets, and
version consequences.

An extension or profile MUST NOT override the Common Artifact Envelope,
artifact-specific contract meaning, final human authority, provenance,
privacy, or mandatory core constraints.

## Conformance and authority boundary

Accepted architecture conformance, artifact-specific normative-contract
conformance, executable-schema validity, complete Artifact Instance
conformance, Serialization Binding conformance, implementation conformance,
review outcome, Owner acceptance, integration, release, and deployment remain
distinct.

A future artifact-specific schema can establish only the structural assertions
it contains. Schema validity cannot prove that an identifier, revision,
version, reference, contract, schema, source, relationship, evidence claim, or
approval is real, Accepted, applicable, authoritative, sufficient, current,
safe, accessible, or authorized. It cannot grant disclosure, execution,
release, merge, or deployment authority.

## Security and privacy boundary

This decision requires no secret, credential, personal data, private path,
private repository content, production configuration, restricted source
material, provider token, private project context, or implementation detail.

Identifiers and references grant no permission to discover, retrieve,
dereference, cache, mirror, publish, disclose, trust, or execute their targets.
Automatic network retrieval remains disabled by default under the Accepted
offline-first boundary.

## Review, approval, and validation boundary

The same operational agent prepared and reviewed the exact candidate head
under issue #44 with a disclosed non-independent Architect/Implementer
arrangement. Review findings and the PASS recommendation were evidence, not
acceptance. The Owner / Final Authority separately accepted the exact reviewed
candidate revision.

Markdown validity, link resolution, standards-source availability, internal
consistency, GitHub mergeability, or later schema validity cannot accept this
decision or authorize another phase.

## Consequences and tradeoffs

Positive consequences include:

- all nine canonical artifacts receive one stable logical schema identity;
- every future full Artifact Instance has one uniform closed root;
- common metadata and artifact-specific meaning remain independently
  reviewable;
- every artifact schema pins one exact Accepted common resource;
- version lines remain independent and consequentially traceable;
- contract dependency order guides rollout without forcing schema coupling;
  and
- no artifact Serialization Binding or implementation is prematurely chosen.

Costs and limitations include:

- the closed root requires explicit versioned evolution;
- no artifact-specific instance is executable-schema-valid yet;
- all nine payloads still require separate design and acceptance;
- Contract Definition Identifier/Version allocation may remain a prerequisite;
- a common-envelope change requires cross-schema compatibility assessment;
- extensions and profiles cannot add ungoverned root members; and
- no validator, resolver, binding, runtime, release, or deployment is supplied.

## Rejected alternatives

- **Flat combined root** — rejected because it erases common/payload ownership.
- **Optional envelope or payload** — rejected because a complete artifact
  requires both regions.
- **Open root** — rejected because unknown members could add ungoverned
  semantics.
- **Copied common definitions** — rejected because they can drift or weaken.
- **Internal `$defs` references** — rejected because internal names are not a
  public compatibility surface.
- **Moving, relative, or dynamic common references** — rejected because exact
  Accepted dependencies must remain immutable and offline-controllable.
- **One monolithic artifact schema** — rejected because artifact identities,
  payloads, reviews, and versions remain separate.
- **Family-wide version** — rejected because meanings evolve independently.
- **Automatic artifact-to-artifact schema dependencies** — rejected because
  contract dependency does not imply executable embedding.
- **Embedded upstream artifacts** — rejected because a copy is derived and
  does not become the governing source.
- **Relationship meaning in the common envelope** — rejected because role,
  direction, sufficiency, freshness, and conflict remain artifact-specific.
- **Container as Serialization Binding** — rejected because instance-model
  shape does not determine bytes, encoding, transport, or storage.
- **Concrete `$id` or executable payload now** — rejected as outside this
  documentation-only phase.
- **Review or validity as acceptance** — rejected because final authority
  remains human and exact-revision-bound.
- **Automatic authorization of the next schema** — rejected because Project
  Charter schema work requires a separate exact task and authority gate.

## Deferred and prohibited scope

ARCH-010 does not define or authorize an executable Project Charter or other
artifact-specific Schema Resource; payload or relationship fields; concrete
artifact-specific `$id` values, repository schema paths, or schema files;
active artifact-specific Schema Versions; Contract Definition Identifier or
Version allocation; Artifact Instance Identifier generation or revision
sequencing; changes to Common Artifact Envelope Schema Version `1.0.0`; a
cross-artifact shared resource; artifact-to-artifact schema references;
Extension Module or Profile mechanics; artifact Serialization Bindings;
canonical JSON, YAML, CBOR, transport, storage, archive, or Artifact Instance
media type; digest algorithms, encoding, canonicalization, signatures, trust
stores, or verification; resolvers, registries, catalogs, caches, automatic
network retrieval, mirrors, redirects, hosted schema publication, bundles,
validators, validation output, conformance tooling, fixtures, code generation,
migrations, templates, forms, APIs, CLIs, workflows, engines, schedulers,
orchestrators, runtimes, providers, products, private implementations,
reference implementations, releases, tags, hosted publication, or deployment.

## Continuing gate

ARCH-010 and ADR-0010 are Accepted. No artifact-specific executable Schema
Resource or active artifact-specific Schema Version exists under this
decision; all nine `1.0.0` values remain inactive initial accepted targets.
The Owner / Final Authority accepted exact reviewed head
`5e8d003ffd6d6f27cfb53201a6d55c570a7b99e4`, authorizing only the separately
enumerated status-promotion and governed-integration sequence.

Project Charter executable-schema work is only the next candidate. It requires
a separate approved task and must stop if concrete Contract Definition
identity/version or another prerequisite remains unresolved. No follow-on
phase is implied or authorized by this document.
