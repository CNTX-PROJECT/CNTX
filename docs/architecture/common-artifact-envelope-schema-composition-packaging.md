# CNTX Common Artifact Envelope Schema Composition and Packaging (ARCH-008)

## Status and authority

Status: **Proposed**.

This document is a proposed, documentation-only architecture decision prepared under issue #40 and recorded by [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md). It does not become binding unless the human Owner / Final Authority accepts the exact reviewed candidate revision and the resulting decision is integrated under [GOVERNANCE.md](../../GOVERNANCE.md).

This proposal refines only the composition and packaging decision left open by accepted [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), [ARCH-003](artifact-contract-schema-architecture.md), [ARCH-004](common-artifact-envelope-schema-boundary.md), [ARCH-005](common-artifact-envelope-representation-boundary.md), [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md), and [ARCH-007](common-artifact-envelope-schema-language-dialect.md). It does not alter those sources, any accepted artifact contract, or final human authority.

Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms express requirement strength only within this document.

## Purpose and decision boundary

ARCH-005 requires source layout, composition, resolution, packaging, and publication boundaries to be decided after schema identity/version policy and language/dialect, but before an executable Common Artifact Envelope definition. ARCH-008 selects a deliberately small schema-resource topology and a deterministic distribution model for that later definition.

This decision does not create an executable schema. It defines no field name, key, type constraint, requiredness rule, object shape, concrete `$defs` entry, concrete `$ref` value, active Schema Version, concrete `$id`, artifact Serialization Binding, validator, resolver, bundler, implementation, release, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Human final authority, bounded work, evidence-before-claims, minimal context, public/private separation, and non-self-approval remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Schema identity and Schema Version remain explicit, stable, version-pinned, and distinct from location, status, implementation, digest, provenance, conformance, and authority. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | The Common Artifact Envelope remains one Layer 3 common definition; artifact-specific definitions remain independently reviewable; dependencies point upward without creating a monolithic global schema. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) | Universal, conditional, artifact-specific, and excluded ownership categories remain intact; composition cannot absorb artifact-specific meaning or authority. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) | Representation obligations, activation conditions, semantic couplings, absence distinctions, common-versus-payload separation, and the ordered decision gates remain unchanged. |
| [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) | One logical identity and the conditional `1.0.0` target remain unchanged and inactive; composition, path, retrieval, or bundling cannot multiply or replace that identity. |
| [ARCH-007](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) | JSON Schema Draft 2020-12, its exact dialect URI, seven standard vocabularies, annotation-only `format`, and the no-custom-dialect boundary remain fixed. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Every canonical artifact retains its accepted purpose, classification, authority limits, relationships, lifecycle participation, and payload semantics. |
| Issue #40 | Work remains documentation-only and limited to the five-path ARCH-008 decision; executable schemas, concrete identifiers, fields, bindings, validation, and implementation remain outside scope. |

## Primary standards basis

The selection is grounded in the public [JSON Schema Draft 2020-12 index](https://json-schema.org/draft/2020-12), [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core), its official [default dialect meta-schema](https://json-schema.org/draft/2020-12/schema), and [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986).

JSON Schema Core establishes that:

- a Schema Resource is canonically identified by an absolute URI;
- root and embedded resources are distinct from ordinary subschemas;
- `$id` establishes canonical and base URI behavior;
- `$ref` is a static URI-reference applicator, while `$dynamicRef` and `$dynamicAnchor` create a runtime dynamic-reference mechanism;
- `$defs` reserves a location for reusable schemas without itself affecting evaluation;
- a URI-shaped identifier does not require network retrieval;
- linked and embedded resources are intended to preserve the same reference behavior; and
- a Compound Schema Document may bundle identified resources for transport while retaining their identities and references.

JSON Schema permits broader topologies than CNTX selects here. The restrictions below are CNTX architecture choices for bounded review, deterministic resolution, portability, privacy, and compatibility; they are not claims that JSON Schema forbids other conforming designs.

## Terms for this decision

| Term | CNTX meaning in this decision | Not equivalent to |
| --- | --- | --- |
| **Schema Resource** | A JSON Schema root with its own canonical URI identity and resource-level processing scope. | Every subschema, file location, or `$defs` member. |
| **Canonical Common Envelope Resource** | The one independently reviewable root Schema Resource that will implement one accepted Common Artifact Envelope Schema Version. | A bundle, artifact-specific schema, retrieval URL, or repository path. |
| **Internal subschema** | A reusable schema owned by the canonical resource, kept under its root `$defs`, with no nested `$id` or independent version. | An embedded Schema Resource or public module. |
| **Cross-resource dependency** | A static `$ref` from one independently identified Schema Resource to another exact versioned resource. | Copying content, transferring authority, or a filesystem import. |
| **Canonical resource set** | The separately accepted standalone resources and exact versions intended to be used together. | A monolithic global schema or generated bundle. |
| **Compound Schema Document** | A JSON Schema document containing multiple identified embedded Schema Resources as defined by JSON Schema Core. | An archive, arbitrary concatenation, or total dereferencing. |
| **Derived distribution bundle** | A non-authoritative Compound Schema Document produced from an exact accepted canonical resource set for transport or offline use. | A new schema identity, version, acceptance, or source of contract meaning. |
| **Retrieval coordinate** | A location or resolver mapping through which content may be obtained. | Canonical `$id`, logical Schema Identifier, Schema Version, or authority. |

## Composition and packaging selection

| Selection dimension | Proposed decision |
| --- | --- |
| Common Envelope resource cardinality | Exactly one canonical root Schema Resource per accepted Schema Version |
| Canonical authoring form | One standalone JSON Schema document for that resource |
| Root dialect declaration | Exact ARCH-007 `$schema` declaration |
| Root resource identity | One future version-qualified absolute HTTPS `$id`, not assigned here |
| Internal reusable schemas | Root `$defs` members without nested `$id` |
| Internal references | Static fragment-only `$ref` values within the same root resource |
| Public anchors | None in the initial composition surface |
| Dynamic references | `$dynamicRef` and `$dynamicAnchor` not used initially |
| Common resource dependencies | No mandatory external Schema Resource dependency |
| Artifact-specific dependency | Future artifact-specific resources may statically reference the exact versioned common root |
| Dependency shape | Acyclic and aligned with accepted layer direction |
| Canonical distribution | Separately reviewable standalone resource documents |
| Offline/transport distribution | Optional derived Compound Schema Document bundle |
| Resolution default | Exact resources preloaded or supplied; no automatic network retrieval |
| Schema resource media type | `application/schema+json` |

## One canonical root resource per Schema Version

Each future accepted Common Artifact Envelope Schema Version MUST have exactly one canonical root Schema Resource. That resource is the independently reviewable executable definition governed by the one logical identity allocated in ARCH-006.

The root resource MUST eventually contain:

1. the exact `$schema` declaration required by ARCH-007; and
2. exactly one root `$id` bound to the ARCH-006 logical identity and the active exact Schema Version.

ARCH-008 does not provide either executable document or a concrete `$id`. The first active binding remains conditional on separately authorized executable-definition work and exact-revision human acceptance.

The canonical resource MUST NOT contain a nested `$id`. Consequently, the canonical Common Artifact Envelope source has no embedded Schema Resources, hidden independent identities, or separately versioned modules. This keeps the public Layer 3 common definition one review unit and prevents internal layout choices from silently multiplying the Schema Family.

## Canonical URI and Schema Version policy

The future root `$id` MUST be a normalized absolute HTTPS URI without a fragment. It MUST be controlled through a public namespace governed by the Owner, and it MUST include the exact `MAJOR.MINOR.PATCH` Schema Version in an immutable form.

The canonical URI:

- MUST identify exactly one accepted Schema Resource and Schema Version;
- MUST NOT use `latest`, an unversioned moving alias, a branch, a tag, or an implementation-selected value;
- MUST remain stable if the repository file, publication host, mirror, registry, cache, or resolver mapping changes;
- MUST NOT be inferred from a retrieval location when the schema content declares a different canonical `$id`; and
- MUST NOT be interpreted as Document Status, acceptance, conformance, authority, trust, or permission to retrieve content.

This decision intentionally does not select the HTTPS authority, namespace tokens, URI path grammar, repository path, filename, redirect behavior, mirror, registry key, or concrete `$id` value. Those lexical bindings must be reviewed with the later executable resource and publication evidence; they may not change the topology or invariants accepted here.

## Internal reuse through `$defs`

Reusable schemas that are owned entirely by the Common Artifact Envelope resource MUST be placed under the root `$defs`. They remain internal subschemas rather than independent Schema Resources.

An internal `$defs` member:

1. MUST NOT declare `$id` or `$schema`;
2. MUST inherit the root resource's base URI and ARCH-007 dialect;
3. MUST NOT receive an independent logical Schema Identifier, Schema Version, Document Status, or governance lifecycle;
4. MUST NOT be presented as a public extension, profile, artifact-specific contract, or separately accepted module; and
5. MAY be changed only through the compatibility and versioning process of the containing Common Artifact Envelope resource.

Static internal reuse MUST use fragment-only `$ref` values that resolve within the same canonical root resource. A future executable definition may name concrete `$defs` entries only within its own separately approved scope.

Crossing a Schema Resource boundary with a JSON Pointer based on an enclosing document's layout is prohibited. Such a pointer would be fragile when resources are bundled or unbundled and would confuse retrieval structure with canonical resource identity.

## Anchor and dynamic-reference boundary

The initial Common Artifact Envelope composition exposes no `$anchor`-based public subschema API. Internal composition therefore does not depend on a stable plain-name fragment surface.

Introducing a public `$anchor` later would create an externally consumable reference point. It requires an explicit compatibility assessment, ownership statement, and accepted change tied to an exact Schema Version. It cannot arise merely from refactoring a `$defs` layout.

The initial composition MUST NOT use `$dynamicRef` or `$dynamicAnchor`. JSON Schema Core defines them as a cooperative runtime extension mechanism, particularly for recursive schemas. No such recursion or dynamically replaceable extension point has been justified for the Common Artifact Envelope, and adopting one would pre-empt the separately governed Layer 5 Extension Module and Profile boundary.

This restriction does not redefine or remove the ARCH-007 dialect's language support. It limits what the initial CNTX composition may use.

## Cross-resource dependency direction

The canonical Common Artifact Envelope root MUST have no mandatory external Schema Resource dependency. Its evaluation can therefore be prepared from the one accepted resource without retrieving unrelated definitions.

Future artifact-specific Schema Resources MAY depend on the exact accepted Common Artifact Envelope root through static `$ref`. Any such dependency:

- MUST identify the common resource by its exact version-qualified canonical URI;
- MUST preserve the artifact-specific schema's separate identity, version, contract responsibility, and payload ownership;
- MUST NOT copy, fork, shadow, weaken, or redefine common-envelope semantics;
- MUST NOT use an unversioned alias, repository-relative file path, bundle location, or network redirect as the consequential identity pin; and
- MUST NOT form a resource cycle.

The allowed dependency direction is lower, artifact-specific definition to higher, common definition. The common root MUST NOT depend on artifact-specific, Extension Module, Profile, binding, validator, implementation, provider, or product resources.

ARCH-008 does not decide where the common reference appears in a later artifact-specific executable schema, which applicator context surrounds it, or which instance location it evaluates. Those questions depend on concrete field and object structure and remain later executable-schema work.

## Canonical resource set

Canonical authoring and publication use separately reviewable standalone Schema Resource documents. Each resource retains its own accepted identity, exact Schema Version, dialect declaration, contract responsibility, provenance, and compatibility history.

The standalone form is canonical because it:

- keeps review and versioning aligned with accepted ownership boundaries;
- avoids making distribution layout part of identity;
- permits resource consumers to preload only the exact resources they need;
- preserves artifact-specific independence; and
- allows a derived bundle without changing reference values or canonical identities.

A canonical resource set is not automatically one release, repository directory, archive, deployment, or validator configuration. Those coordinates remain separate evidence and distribution concerns.

## Derived Compound Schema Document bundle

A future distribution process MAY produce a Compound Schema Document from an exact accepted canonical resource set when offline transport or single-document delivery is required. That bundle is derived and non-authoritative.

Bundling MUST:

1. select one accepted resource as the containing root for the intended evaluation entry point;
2. place referenced embedded resources as values beneath the containing root's `$defs`;
3. use unique, non-normative bundle keys that do not collide with or alter the containing resource's existing internal `$defs` entries and are never used as reference identities;
4. retain every embedded resource's canonical `$id` unchanged;
5. explicitly retain every embedded resource's `$schema` declaration, even when it matches the containing resource's dialect;
6. leave all static `$ref` values unchanged;
7. preserve evaluation behavior, annotation locations, and canonical reference results between linked and bundled forms;
8. keep embedded resources independently identifiable and processable; and
9. preserve traceability to the exact accepted identities and Schema Versions from which the bundle was derived.

Bundling MUST NOT:

- replace references with copied target constraints or attempt total dereferencing;
- rewrite a canonical URI to a bundle-local JSON Pointer;
- wrap an embedded resource in a new applicator;
- remove or synthesize resource identities;
- change a resource's dialect, vocabulary profile, accepted meaning, or Schema Version;
- turn a `$defs` key into a normative reference target;
- be presented as the canonical standalone content or as a byte-identical mirror of its containing root;
- combine unrelated artifact payloads or private context merely to be self-contained; or
- create a new source of authority, approval, trust, acceptance, or conformance.

The bundle itself receives no new Common Artifact Envelope logical identity or Schema Version. Its containing root continues to identify the same canonical root resource semantically, while embedded resources retain their own identities. The document-level addition of embedded resources makes the bundle a derived representation rather than the immutable canonical standalone document. A bundle retrieval coordinate is not a substitute for any embedded canonical URI.

## Resolution and offline behavior

Processors are expected to know the exact accepted resource set before evaluating an instance. Resources MAY be preloaded, supplied through a caller-controlled mapping, or made available through another later accepted resolution mechanism keyed by canonical URI.

An HTTPS-shaped `$id` or `$ref` does not authorize network access. Automatic remote retrieval MUST be disabled by default. A required reference that is not present in the supplied resource set MUST be reported as unresolved; it MUST NOT be ignored, guessed, redirected to an unversioned alias, satisfied from an unrelated cache entry, or replaced by an implementation default.

This fail-closed resolution boundary is not a validator selection or error-output format. Resolver APIs, catalog formats, caches, trust stores, integrity checks, timeouts, resource limits, network allowlists, and diagnostic structures remain later decisions.

Resolution success establishes only that the identified schema resource was found. It does not establish that the resource is accepted, applicable, trustworthy, safe, contract-conformant, or authorized for use.

## Publication and persistence boundary

Future JSON Schema resources governed by this decision MUST be published as `application/schema+json`. This describes schema-resource representation and does not select an artifact instance Serialization Binding.

Once a versioned Schema Resource is accepted, its canonical standalone representation is fixed:

- its canonical identity and accepted content are immutable;
- a changed accepted meaning requires a new Schema Version under ARCH-002 and ARCH-006;
- a retrieval coordinate or mirror MAY change only while preserving the canonical identity and exact accepted standalone content; a derived bundle is not such a mirror;
- an unversioned or `latest` alias MAY exist only for human discovery and MUST NOT be used in consequential `$ref` values, conformance evidence, or provenance pins; and
- publication, availability, or successful HTTP retrieval MUST NOT imply acceptance, trust, endorsement, or permission to access referenced material.

ARCH-008 does not select a hosting provider, domain, repository path, filename, redirect, registry, discovery service, release process, deployment, archive format, or persistence service.

## Equivalence and provenance requirements

Linked standalone resources and a derived Compound Schema Document MUST preserve equivalent schema evaluation and canonical reference behavior for the same entry resource and resource set. Equivalence does not mean byte equality: the bundle document adds embedded resource copies under `$defs` while the canonical standalone documents remain unchanged.

A future bundle must be traceable to the exact accepted logical Schema Identifiers and Schema Versions from which it was produced. A Content Digest or signature MAY later strengthen exact-content evidence, but neither may replace identity, version, provenance, acceptance, or authority.

This decision defines no bundle manifest fields, digest algorithm, signature system, reproducible-build process, bundler implementation, fixture, or equivalence test suite. Those mechanisms require separate authorization and evidence.

## Separation matrix

| Dimension | Decided here | Still separate |
| --- | --- | --- |
| Logical Schema Identifier | Preserved as the one ARCH-006 identity | Concrete lexical `$id` value |
| Schema Version | Must appear exactly in the future immutable canonical URI | Activation of `1.0.0` |
| `$schema` | Required at the canonical root and retained for embedded bundle resources | Any dialect change |
| `$id` | One root identity; no nested identity in canonical source | Concrete HTTPS authority, namespace, path, or value |
| `$defs` | Sole internal-reuse location in the canonical resource | Concrete definitions, names, fields, or constraints |
| `$ref` | Static internal and exact-version cross-resource policy | Concrete reference values and applicator placement |
| Anchors | No initial public anchor surface | Any later named-fragment API |
| Dynamic references | Not used initially | Any future recursive extension mechanism |
| Canonical packaging | Standalone resource documents | Repository file layout and hosting |
| Derived packaging | Compound Schema Document with identity-preserving embedding | Bundler, manifest, archive, digest, or signature implementation |
| Resolution | Offline-first, exact URI mapping, no automatic network | Resolver technology, catalog, cache, trust, and diagnostics |
| Media type | `application/schema+json` for schema resources | Artifact instance Serialization Binding |
| Document Status | ARCH-008 remains `Proposed` until exact-revision human acceptance and integration | Schema validity, publication, or bundle status |

## Security and privacy boundary

Schema-resource identifiers, retrieval coordinates, references, bundle provenance, annotations, diagnostics, and package metadata MUST NOT disclose secrets, credentials, personal data, private project data, production configuration, private paths, restricted source content, or private implementation detail.

Self-contained packaging MUST NOT be achieved by copying private or authoritative source content into a public schema bundle. A reference does not grant permission to fetch, reveal, cache, mirror, publish, or trust its target.

Automatic network retrieval is excluded because URI processing can otherwise introduce server-side request forgery, tracking, non-determinism, dependency substitution, availability, and confidentiality risks. Exact protections, limits, and trust policy remain a later resolver or validator decision.

## Review, approval, and conformance boundary

The same operational agent may prepare and architecturally review this candidate only under the transparent role arrangement authorized in issue #40. Such a combined review is not independent third-party review and cannot provide final human approval. Only the human Owner / Final Authority may accept the exact reviewed architecture revision.

Schema identity, reference resolution, bundle construction, schema validity, contract conformance, evidence quality, compatibility, acceptance, integration, release, and deployment remain distinct. None grants another automatically.

## Consequences and tradeoffs

The selected model favors a small public surface and deterministic processing:

- one canonical root keeps the common definition independently reviewable;
- no nested `$id` avoids hidden resource/version boundaries;
- root `$defs` permits local reuse without creating modules;
- static version-pinned references make dependency behavior visible;
- no dynamic references avoids prematurely defining an extension mechanism;
- standalone canonical resources preserve ownership and version histories;
- derived bundles support offline delivery without rewriting identity; and
- no automatic network retrieval reduces security and reproducibility risks.

The tradeoff is that future executable schemas cannot rely on implicit module discovery, moving aliases, dynamic override points, or arbitrary remote loading. Bundle production and exact resource provisioning require explicit evidence and later tooling. This cost is acceptable because CNTX prioritizes bounded, verifiable collaboration over convenience through hidden resolution behavior.

## Rejected alternatives

### Use one monolithic schema for the common envelope and all artifact payloads

Rejected because it would erase independently governed artifact responsibilities, force unrelated context into common validation, and violate the ARCH-003 and ARCH-005 layer boundaries.

### Split the canonical Common Artifact Envelope into multiple embedded Schema Resources

Rejected for the initial definition because nested `$id` values would create multiple resource identities and version surfaces before reuse or independent governance needs are demonstrated.

### Publish internal `$defs` members as public reference targets

Rejected because it would make an internal layout a compatibility API and allow downstream schemas to depend on subschemas that have no independent contract or version.

### Use `$dynamicRef` and `$dynamicAnchor` for extensibility

Rejected because no recursive dynamic extension requirement is established, and the mechanism would pre-empt later Layer 5 Extension Module and Profile decisions.

### Let artifact-specific schemas copy the common envelope

Rejected because copies drift, obscure provenance, and can silently redefine common meaning. Exact static dependency is required instead.

### Make a Compound Schema Document the canonical authoring source

Rejected because distribution layout would become entangled with resource ownership, versioning, and review. Bundles remain derived from standalone accepted resources.

### Rewrite `$ref` values to bundle-local JSON Pointers

Rejected because it would make bundled and unbundled forms differ, cross resource boundaries through document layout, and weaken canonical identity.

### Fully dereference and inline every schema

Rejected because reference removal is not always behavior-preserving, can break recursion and annotations, and destroys explicit dependency provenance.

### Automatically retrieve HTTPS references

Rejected because an identifier is not a network authorization. Implicit retrieval introduces security, privacy, availability, and determinism risks.

### Use an unversioned or `latest` canonical URI

Rejected because consequential references must pin the exact Schema Version and must not change meaning without changing their identifier.

### Assign the concrete `$id` and repository file now

Rejected because no executable resource exists in this documentation-only phase. The lexical binding must be reviewed with the exact future schema content and publication evidence.

### Treat the combined Architect/Implementer review as final approval

Rejected because operational review is not independent and cannot replace the human Owner / Final Authority decision.

## Deferred and prohibited by this decision

This decision does not define or authorize an executable Common Artifact Envelope or artifact-specific schema; concrete fields, aliases, keys, types, constraints, nesting, cardinalities, ordering, defaults, requiredness, examples, payloads, or fixtures; a concrete Common Artifact Envelope `$id`, HTTPS authority, namespace, URI path grammar, repository path, filename, retrieval URL, redirect, mirror, registry, or publication location; activation of Schema Version `1.0.0`; concrete `$defs` names or entries, `$ref` values, anchor names, schema documents, dependency manifests, bundle manifests, digests, signatures, or archives; artifact JSON serialization, canonical JSON, YAML or CBOR bindings, transport, storage, or canonicalization; dynamic-reference extension behavior; Extension Module or Profile mechanics; custom vocabularies or dialects; Format-Assertion; Hyper-Schema; validators, validation output, conformance tooling, bundlers, resolvers, catalogs, caches, trust stores, templates, code generation, migrations, APIs, CLIs, workflows, engines, runtimes, providers, products, private implementations, reference implementations, releases, or deployments.

## Continuing gate

Acceptance would establish only the composition, resource-topology, reference, packaging, resolution, and publication boundaries described above. It would not create an executable schema or authorize the next task.

Only after ARCH-008 is separately accepted and integrated may an executable Common Artifact Envelope definition become the next candidate task. That later phase requires its own approved issue or Task Contract, exact authoritative baseline, explicit path allowlist, concrete identity/publication evidence, executable-schema review, security/privacy assessment, validation expectations, and exact-revision human decision.
