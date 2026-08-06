# CNTX Common Artifact Envelope Schema Language and Dialect (ARCH-007)

## Status and authority

Status: **Proposed**.

This document is a proposed, documentation-only architecture decision prepared under issue #38 and recorded by [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md). It does not become binding unless the human Owner / Final Authority accepts the exact reviewed candidate revision and the resulting decision is integrated under [GOVERNANCE.md](../../GOVERNANCE.md).

This proposal refines only the schema-language and dialect decision left open by accepted [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), [ARCH-003](artifact-contract-schema-architecture.md), [ARCH-004](common-artifact-envelope-schema-boundary.md), [ARCH-005](common-artifact-envelope-representation-boundary.md), and [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md). It does not alter those sources, any accepted artifact contract, or final human authority.

Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms express requirement strength only within this document.

## Purpose and decision boundary

ARCH-005 requires schema language and dialect to be decided after logical schema identity and initial version policy and before composition, packaging, or an executable Common Artifact Envelope definition. This decision selects a fixed, publicly specified schema language and dialect, defines the dialect declaration and vocabulary boundary, and distinguishes language-level identity and data-model concepts from the later decisions that will use them.

This decision does not create an executable schema. It defines no field name, key, type constraint, requiredness rule, object shape, reference graph, resource boundary, package, artifact Serialization Binding, validator, schema publication, implementation, release, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Human final authority, bounded work, evidence-before-claims, minimal context, canonical artifact responsibilities, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Schema identity/version remain distinct from contract, artifact, status, implementation, digest, and provenance dimensions; a dialect or successful evaluation grants no authority. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | An executable schema remains subordinate to accepted contracts; the Schema Family, Serialization Bindings, validators, Extension Modules, Profiles, and implementations remain distinct layers. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) | The universal, conditional, artifact-specific, and excluded ownership categories remain intact; a language cannot absorb artifact-specific meaning or authority. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) | Representation obligations, activation conditions, semantic couplings, absence distinctions, and the ordered decision gates remain unchanged. |
| [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) | The one logical Common Artifact Envelope schema identity and the conditional `1.0.0` initial accepted version target remain unchanged and inactive until a later executable definition is accepted. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Every canonical artifact retains its accepted purpose, classification, authority limits, relationships, lifecycle participation, and payload semantics. |
| Issue #38 | Work remains documentation-only and limited to the five-path ARCH-007 decision; composition, packaging, executable schemas, bindings, validation, and implementation remain outside scope. |

## Primary standards basis

The selection is grounded in the public [JSON Schema specification index](https://json-schema.org/specification), [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core), and [JSON Schema Validation 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation). At the issue #38 task baseline, the official specification index identifies 2020-12 as the current published version. This observation supports the selection but does not create a moving dependency on whichever version may later be called current.

The normative dialect pin is the exact published 2020-12 meta-schema URI. Later publication of a newer JSON Schema release does not silently alter this decision.

## Language and dialect selection

| Selection dimension | Proposed decision |
| --- | --- |
| Schema language | **JSON Schema** |
| Fixed dialect | **JSON Schema Draft 2020-12 Core and Validation dialect** |
| Dialect identifier | `https://json-schema.org/draft/2020-12/schema` |
| Dialect declaration keyword | `$schema` |
| Vocabulary profile | The seven standard vocabularies declared by the selected default dialect meta-schema |
| Custom dialect or vocabulary | None |
| `format` behavior | Annotation-only under the selected default dialect; Format-Assertion is not selected |
| Instance evaluation model | The JSON-compatible data model defined by JSON Schema Core |
| Executable-definition state | No executable Common Artifact Envelope schema exists |
| Current Schema Version | None |

JSON Schema is selected because it is public, declarative, implementation-independent, explicitly dialected, vocabulary-based, and designed to describe and evaluate a JSON-compatible data model across tools and programming environments. These properties fit CNTX's need for a reviewable structural layer without making a validator, runtime, provider, product, transport, or private implementation authoritative.

Selection does not make every feature of the language appropriate for CNTX. Accepted higher-layer semantics and later bounded decisions remain controlling.

## Fixed dialect declaration

Every future standalone Common Artifact Envelope executable schema document governed by this decision MUST declare the selected dialect at its document root using `$schema` with the exact value `https://json-schema.org/draft/2020-12/schema`.

The declaration:

1. identifies the JSON Schema dialect and its keyword semantics;
2. MUST NOT be omitted in reliance on an implementation default;
3. MUST NOT use an unversioned, moving-latest, implementation-selected, or locally substituted dialect identifier;
4. MUST NOT be interpreted as the Common Artifact Envelope Schema Identifier, Schema Version, Document Status, approval, authority, or conformance claim; and
5. MUST NOT silently change when a new JSON Schema release is published.

Whether separately addressable embedded resources repeat `$schema` or inherit the enclosing resource dialect depends on the later composition and packaging decision and the selected dialect's rules. ARCH-007 does not decide that resource topology.

An implementation that does not recognize or correctly support the declared dialect cannot claim to have evaluated a future Common Artifact Envelope schema under this decision. Exact processor qualification, test evidence, unsupported-dialect behavior, and validation output remain later conformance and validator decisions.

## Standard vocabulary profile

The selected default dialect consists of exactly the following standard vocabularies as declared by its official meta-schema:

| Standard vocabulary | Vocabulary URI | Role retained by this decision |
| --- | --- | --- |
| Core | `https://json-schema.org/draft/2020-12/vocab/core` | Dialect bootstrapping, schema-resource identity, anchors, references, comments, and definitions at the language level. |
| Applicator | `https://json-schema.org/draft/2020-12/vocab/applicator` | Application and combination of subschemas. |
| Unevaluated | `https://json-schema.org/draft/2020-12/vocab/unevaluated` | Standard unevaluated-instance-location semantics. |
| Validation | `https://json-schema.org/draft/2020-12/vocab/validation` | Structural assertion keywords. |
| Meta-Data | `https://json-schema.org/draft/2020-12/vocab/meta-data` | Standard schema annotations. |
| Format-Annotation | `https://json-schema.org/draft/2020-12/vocab/format-annotation` | Annotation semantics for `format`. |
| Content | `https://json-schema.org/draft/2020-12/vocab/content` | Standard annotations for string-encoded content. |

ARCH-007 selects the official dialect as published. CNTX MUST NOT silently remove, replace, reinterpret, or add a vocabulary while claiming to use that unchanged dialect.

The initial Common Artifact Envelope definition MUST NOT introduce a custom CNTX dialect, custom vocabulary, or unknown keyword carrying normative meaning. An extension to the language surface requires a separately accepted architecture decision, explicit vocabulary identity and semantics, compatibility assessment, processor-support boundary, security/privacy assessment, and version assessment. Layer 5 Extension Modules and Profiles remain governed separately and do not acquire a schema vocabulary through this decision.

## `format` semantics

Under the selected default dialect, `format` belongs to the Format-Annotation vocabulary. A future use of `format` therefore supplies annotation information; it does not by itself create a required validation assertion.

CNTX processors and conformance claims MUST NOT silently depend on an implementation option that treats Format-Annotation as assertion behavior. Two implementations can differ in optional format checking while both recognize the selected dialect, so such behavior cannot define portable CNTX conformance.

The Format-Assertion vocabulary is not selected. If a later requirement needs portable assertion semantics for a value currently associated with `format`, that requirement must be expressed through an accepted structural decision or a separately accepted dialect/vocabulary change. This document decides no concrete value format, timestamp syntax, identifier syntax, or field.

## JSON-compatible instance data model and Serialization Bindings

JSON Schema evaluates instances according to its JSON-compatible data model: null, boolean, object with string member names, array, number, and string. Selecting that evaluation model is part of selecting the schema language.

It is not an artifact Serialization Binding. This decision does not require CNTX artifacts to be physically serialized as JSON text, does not select canonical JSON, and does not decide YAML, CBOR, or another binding. A later Serialization Binding may be considered only through a separate decision and must define a lossless, unambiguous mapping into the accepted schema evaluation model, including any differences in numeric representation, map keys, duplicate names, ordering, tags, aliases, or binary values.

The JSON representation of future schema documents is also distinct from the representation of artifact instances governed by those schemas. Selecting JSON Schema does not make a schema document an Artifact Instance and does not transfer schema-language syntax into the Common Artifact Envelope's accepted semantic ownership.

## Dialect identity, schema identity, version, and status separation

| Dimension | Meaning under ARCH-007 | Explicit non-equivalence |
| --- | --- | --- |
| `$schema` value | Identifies the fixed JSON Schema dialect used to interpret schema keywords. | Not the CNTX logical Schema Identifier, future concrete schema-resource `$id`, Schema Version, Document Status, or artifact serialization. |
| Selected dialect | The standard 2020-12 Core and Validation vocabulary set. | Not an executable Common Artifact Envelope definition, validator, binding, conformance claim, or authority source. |
| Logical Schema Identifier | The accepted technology-neutral identity allocated by ARCH-006: **CNTX Public Core Schema Family / Common Artifact Envelope**. | Not a dialect URI, file path, title, vocabulary URI, or active schema resource. |
| Future `$id` value | The future canonical URI of a JSON Schema resource through the standard Core identity keyword. | Not assigned by ARCH-007; not automatically the stable logical identity alone or Schema Version alone. |
| Schema Version | The semantic version of an accepted executable schema definition. | None exists; `1.0.0` remains only the ARCH-006 initial accepted target. |
| Document Status | `Proposed`, `Accepted`, `Superseded`, or `Deprecated` governance state. | Not a dialect version, Schema Version, processor-support level, or validation result. |
| Vocabulary URI | Identifies one standard set of JSON Schema keywords and semantics. | Not a CNTX schema, contract, artifact, implementation, or approval identity. |
| File path or publication URL | A mutable storage or retrieval coordinate. | Not stable logical identity, governance status, or authority. |

## Future `$id` binding boundary

JSON Schema Core defines `$id` as the standard keyword for establishing a schema resource's canonical URI. ARCH-007 selects that standard mechanism for future schema-resource identity and rejects an ad hoc CNTX identity keyword.

ARCH-007 assigns no `$id` value. It does not decide:

- the public URI authority or namespace;
- the lexical mapping from the ARCH-006 logical identity to a URI;
- whether or where Schema Version appears in a resource URI;
- root and embedded resource boundaries;
- canonical versus retrieval URIs;
- redirects, mirrors, offline catalogs, registries, or resolvers;
- filename or directory layout; or
- publication and persistence obligations.

Those questions depend on composition, packaging, and publication. The next separate decision must preserve both the stable ARCH-006 logical identity and its distinct Schema Version while defining how a versioned JSON Schema resource is identified without silent conflation. Until that decision and a later executable schema acceptance, no concrete Common Artifact Envelope Schema Identifier or `$id` is active.

## Composition and packaging separation

The selected language defines standard keywords and semantics for reuse and references, including `$defs`, `$ref`, `$anchor`, `$dynamicRef`, and `$dynamicAnchor`. Selecting their language semantics does not decide whether or how CNTX will use them.

ARCH-007 does not define a reference graph, resource granularity, embedded-resource boundary, anchor policy, dynamic-scope policy, bundling rule, package layout, offline distribution, retrieval behavior, publication location, or artifact-specific dependency. Those concerns form the next separately reviewable composition and packaging decision and must be resolved before executable Common Artifact Envelope schema work can be proposed.

## Dialect evolution and compatibility

The dialect pin is immutable for the scope of a future executable schema version. A processor MUST NOT interpret a schema written for the selected dialect using a different dialect merely because that dialect is newer or locally preferred.

Moving to a later JSON Schema release, a custom dialect, or a changed vocabulary profile requires a separate accepted architecture decision. That decision must assess:

- language-level behavioral differences;
- effects on the Common Artifact Envelope Schema Version;
- effects on composition, packaging, resource identity, and references;
- processor interoperability and conformance evidence;
- migration and coexistence requirements; and
- security, privacy, and public-core compatibility.

A language or dialect change does not by itself allocate a new logical Common Artifact Envelope schema identity under ARCH-006. It may nevertheless require a new MAJOR Schema Version if it changes accepted executable meaning or compatibility.

## Security and privacy boundary

Schema dialect declarations, schema-resource identifiers, references, annotations, and validation results MUST NOT contain or disclose secrets, credentials, personal data, private project data, production configuration, private paths, restricted source content, or private implementation detail.

URI syntax does not imply that dereferencing is safe, authorized, online, deterministic, or required. A future processor MUST NOT gain network access, trust a retrieved resource, or disclose a private location merely because the language supports URI references. Fetch policy, registry trust, offline resolution, denial-of-service limits, regular-expression controls, content handling, and remote-reference security require later explicit decisions.

Unknown keywords, annotations, `format`, content metadata, successful schema evaluation, and dialect support MUST NOT grant authority, approval, trust, classification, contract conformance, integration permission, release status, deployment status, or access permission.

## Review, approval, and conformance boundary

The same operational agent may prepare and architecturally review this candidate only under the transparent role arrangement authorized in issue #38. Such a combined operational review is not independent third-party review and cannot provide final human approval. Only the human Owner / Final Authority may accept the exact reviewed architecture revision under the applicable governance.

Dialect recognition, meta-schema validity, schema validity, instance validity, contract conformance, evidence quality, compatibility, acceptance, integration, release, and deployment remain distinct. No language feature, identifier, version, annotation, test, or validation result grants any of them automatically.

## Rejected alternatives

### Use an unspecified or moving “latest” JSON Schema dialect

Rejected because processing semantics could change without a CNTX decision, compatibility assessment, or Schema Version evaluation.

### Use Draft 2019-09 or an older JSON Schema dialect

Rejected because 2020-12 is the current published version at the task baseline and provides a fixed, explicit vocabulary-based dialect. Choosing an older baseline would add migration debt without an accepted CNTX requirement.

### Adopt draft-next features before publication

Rejected because work-in-progress behavior and feature proposals can change. CNTX needs a fixed published interoperability target.

### Define a custom CNTX dialect or vocabulary now

Rejected because the initial common definition has no proven requirement that outweighs the interoperability, processor-support, governance, and security burden. Unknown normative keywords could also hide behavior from standard processors.

### Select Format-Assertion

Rejected because it would create a custom vocabulary profile with stricter and potentially uneven processor requirements before any concrete value-format need has been accepted.

### Select JSON Hyper-Schema

Rejected because hypermedia and link-description behavior is outside the Common Artifact Envelope language-selection need and would introduce API or interaction concerns not authorized by issue #38.

### Treat JSON Schema selection as an artifact JSON Serialization Binding

Rejected because schema evaluation and artifact serialization are different architecture layers. A future binding must be separately specified and reviewed.

### Decide composition and packaging together with language selection

Rejected because references, resource boundaries, bundling, URI layout, and distribution have distinct compatibility and security consequences. The Owner explicitly requires that decision as a separate phase.

### Treat the combined Architect/Implementer review as final approval

Rejected because issue #38 permits transparent operational role combination but preserves sole human final authority and the exact-head decision gate.

## Deferred and prohibited by this decision

This decision does not define or authorize an executable Common Artifact Envelope or artifact-specific schema; concrete fields, aliases, keys, types, constraints, nesting, cardinalities, ordering, defaults, requiredness, examples, payloads, or fixtures; a concrete Common Artifact Envelope `$id`, URI namespace, version placement, filename, registry, resolver, or publication location; `$defs` layout, reference graph, anchors, dynamic references, resource boundaries, bundling, composition, packaging, or distribution; artifact JSON serialization, canonical JSON, YAML or CBOR bindings, media-type policy, transport, storage, or canonicalization; custom vocabularies or dialects; Format-Assertion; Hyper-Schema; validators, validation output, conformance tooling, templates, code generation, migrations, APIs, CLIs, workflows, engines, Layer 5 mechanisms, runtimes, providers, products, private implementations, reference implementations, Schema Version assignment, releases, or deployments.

## Continuing gate

Acceptance would establish only the schema language, fixed dialect, standard vocabulary profile, language-level data model, and keyword boundaries described above. It would not create an executable schema or authorize the next task. Common Artifact Envelope composition and packaging remain the next candidate decision, followed only later by separately authorized executable-definition work. Every later phase requires its own approved issue or Task Contract, authoritative baseline, explicit path allowlist, evidence, review, security/privacy assessment, and human decision.
