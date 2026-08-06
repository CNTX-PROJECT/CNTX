# CNTX Common Artifact Envelope Executable Schema Definition (ARCH-009)

## Status and authority

Status: **Accepted**.

This document is an accepted executable-schema architecture decision approved under issue #42 and recorded by [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md). Owner / Final Authority acceptance of the exact reviewed candidate head is recorded in issue comment `5208715683`. On merge and publication to `main`, the accompanying [Schema Resource](../../schemas/common-artifact-envelope/1.0.0/schema.json) becomes the active Accepted Common Artifact Envelope Schema Version `1.0.0` within this exact scope.

The same operational agent acted transparently as DE ARCHITECT and Bounded Implementer for the accepted candidate. That review arrangement was not independent third-party review and did not provide final human approval; acceptance was given separately by the Owner / Final Authority.

## Purpose and decision boundary

ARCH-009 proposes the first concrete, standalone Common Artifact Envelope Schema Resource. It implements only the shared representation capability accepted by ARCH-002 through ARCH-008 and makes the smallest structural choices necessary for machine evaluation.

The resource evaluates one Common Artifact Envelope object. It does not define a full canonical artifact, an artifact-specific payload, a relationship role, an authority record, a lifecycle state, an Extension Module, a Profile, a Serialization Binding, a validator, a resolver, a bundle, a transport, a runtime, or a product.

Within this document, **MUST** and **MUST NOT** state mandatory requirements within this accepted decision. Schema assertions determine instance validity only; they do not create normative authority beyond the accepted architecture and applicable artifact contracts.

## Governing traceability

| Governing source | Requirement implemented or preserved |
| --- | --- |
| [ARCH-001](core-contract.md) | Human final authority, public/private separation, bounded work, evidence, and non-self-approval remain controlling. |
| [ARCH-002](contract-identity-versioning.md) | Artifact, contract, schema, revision, version, digest, provenance, status, and implementation dimensions remain distinct. |
| [ARCH-003](artifact-contract-schema-architecture.md) | The executable schema is Layer 6, implements higher accepted meaning, remains separate from artifact-specific payloads, and grants no authority. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) | Universal, conditional, artifact-specific, and outside-envelope ownership categories are preserved. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) | Universal capabilities, conditional activation, semantic coupling, absence, payload separation, and non-authority boundaries become concrete without absorbing artifact-specific meaning. |
| [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md) | The one allocated logical identity is bound to the concrete accepted `$id`; `1.0.0` is the accepted initial Schema Version and becomes active on governed integration. |
| [ARCH-007](common-artifact-envelope-schema-language-dialect.md) | The root declares the exact JSON Schema Draft 2020-12 default dialect; no custom vocabulary or Format-Assertion behavior is added. |
| [ARCH-008](common-artifact-envelope-schema-composition-packaging.md) | One standalone root resource, no nested `$id`, internal `$defs`, static fragment references, closed canonical identity, and offline-first processing are implemented. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Canonical artifact responsibilities, classifications, payloads, relationships, lifecycles, authority, review, decision, and state semantics remain artifact-specific. |
| Issue #42 | The exact eight-path executable-definition task, validation evidence, branch, PR, review gate, and prohibited follow-on scope remain binding. |

## Primary standards basis

The accepted resource uses only the standard language surface of:

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12);
- [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core);
- [JSON Schema Validation 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation);
- the official default-dialect [meta-schema](https://json-schema.org/draft/2020-12/schema); and
- [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986).

JSON Schema permits broader choices than this resource uses. The one-resource topology, closed objects, exact field surface, no public anchors, no dynamic references, no custom keywords, no `format`, and no automatic network retrieval are stricter CNTX decisions governed by the accepted architecture.

## Selected executable definition

| Dimension | Accepted decision |
| --- | --- |
| Logical identity | CNTX Public Core Schema Family / Common Artifact Envelope |
| Schema language | JSON Schema |
| Dialect | JSON Schema Draft 2020-12 default dialect |
| Root `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Root `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0` |
| Accepted Schema Version | `1.0.0` |
| Canonical repository path | `schemas/common-artifact-envelope/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Root instance type | Object |
| Root evaluation scope | One Common Artifact Envelope only |
| Root properties | Exactly six |
| Required root properties | `artifactType`, `artifactInstance`, `governingContract`, `governingSchema` |
| Optional root properties | `provenanceReferences`, `contentDigests` |
| Unknown properties | Rejected at every defined object boundary |
| Internal reuse | Root `$defs` only |
| References | Static fragment-only `$ref` values |
| Public anchors | None |
| Dynamic references | None |
| External Schema Resource dependencies | None |
| Artifact payload | Not represented |
| Extension Module or Profile fields | None |
| Document Status | Accepted under issue #42 and Owner acceptance comment `5208715683` |

## Canonical identity, version, and repository path

The accepted decision binds the one ARCH-006 logical identity to this concrete root identifier:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

The identifier is an absolute HTTPS URI without a fragment. It contains the exact accepted Schema Version and no moving alias. The `github.com/CNTX-PROJECT/CNTX` namespace is attributable to the public repository controlled by the Owner and requires no private namespace or deployment.

The `$id` is not an instruction to fetch the schema from the network. It is also not a branch, tag, release, repository file path, mirror, redirect, registry key, artifact identifier, Contract Definition Identifier, approval, or trust assertion. The canonical repository file is [separately identified](../../schemas/common-artifact-envelope/1.0.0/schema.json); identity and repository coordinate remain distinct even though they use corresponding human-readable path components.

The schema document is the accepted initial Common Artifact Envelope Schema Version `1.0.0`. On governed integration to `main`, it becomes active and its canonical standalone content becomes immutable. Any later accepted structural or semantic change requires a new version assessment under ARCH-002 and ARCH-006.

## Root evaluation scope and composition

The root instance is the envelope object itself. This avoids choosing the future full-artifact container shape or the property name and applicator placement through which an artifact-specific schema will evaluate the envelope.

A future artifact-specific Schema Resource may reference the exact accepted common root by its canonical version-qualified URI. That later resource must decide where this envelope appears relative to its independently governed payload. It must not copy, fork, weaken, or redefine the common fields.

The canonical schema document contains exactly one Schema Resource:

- `$schema` and `$id` occur exactly once at the document root;
- no `$defs` member declares `$id` or `$schema`;
- every reusable subschema is located under root `$defs`;
- every `$ref` begins with `#/$defs/` and resolves within this root resource;
- no `$anchor`, `$dynamicAnchor`, or `$dynamicRef` exists; and
- no external, repository-relative, bundle-relative, or cross-resource JSON Pointer reference exists.

Root `$defs` names are internal implementation details. They are not a public compatibility surface and must not be referenced directly by future artifact-specific resources.

## Root property model

| Property | Required | Concrete meaning | Explicit non-meaning |
| --- | --- | --- | --- |
| `artifactType` | Yes | Which Accepted canonical artifact kind the represented Artifact Instance instantiates. | Authority, classification assignment, lifecycle, Document Status, contract identity, or schema identity. |
| `artifactInstance` | Yes | One stable Artifact Instance Identifier coupled with the exact Artifact Revision represented. | Title, path, governing contract, schema, approval, or implementation identity. |
| `governingContract` | Yes | The stable Contract Definition Identifier coupled with the exact Contract Definition Version governing the instance. | Artifact identity, schema identity, acceptance, or authority. |
| `governingSchema` | Yes | The stable Schema Identifier coupled with the exact Schema Version governing the represented artifact when this executable envelope is used. | Contract identity, implementation version, validation result, approval, or authority. |
| `provenanceReferences` | No | One or more complete generic source pins when provenance is asserted. | Relationship purpose, sufficiency, freshness, replacement, authority, retrieval permission, or embedded source content. |
| `contentDigests` | No | One or more subject-bound digest-evidence assertions with an explicit method and value. | Identity, provenance by itself, truth, authenticity, anonymization, authority, approval, or verification result. |

The first four properties are required because an instance evaluated under this resource must state the universal artifact identity/type and the exact normative and executable definitions against which it is being represented. The schema does not fabricate those values: blank strings, incomplete pairs, `null`, or defaults are invalid.

The evidence properties are optional. Their absence means that the envelope makes no such representation. If present, each array must be non-empty and every member must be complete. This schema introduces no `not applicable`, `not asserted`, or `unresolved` sentinel. An artifact-specific schema may later decide whether a distinct state must be represented for its own claim while preserving the common meaning.

## Artifact Type tokens

The schema uses exactly nine lower-kebab-case tokens:

| Token | Accepted canonical artifact |
| --- | --- |
| `project-charter` | Project Charter |
| `workstream` | Workstream |
| `task-contract` | Task Contract |
| `context-packet` | Context Packet |
| `execution-result` | Execution Result |
| `evidence-bundle` | Evidence Bundle |
| `review-record` | Review Record |
| `decision-record` | Decision Record |
| `state-snapshot` | State Snapshot |

The enum is closed. A new canonical Artifact Type requires its own accepted higher-layer contract and a compatibility/version assessment before this schema can recognize it. The token does not encode whether an artifact is Authoritative, Evidentiary, or Derived; those classifications come from accepted architecture and artifact-specific contracts.

## Lexical constraints

### Opaque identifiers and revisions

Artifact, Contract Definition, Schema, and source identifiers are non-empty strings containing at least one non-whitespace character. Artifact Revision uses the same lexical boundary. No URL, URN, UUID, repository coordinate, provider identifier, title, sequence, timestamp, or numeric ordering semantics is imposed.

This deliberately small assertion preserves ARCH-002 opacity and domain independence. A later identity-specific contract may narrow the syntax for its own identifier without changing the Common Artifact Envelope's cross-artifact meaning.

### Semantic versions

Contract Definition Version and Schema Version must match exact three-component `MAJOR.MINOR.PATCH` syntax. Each component is a non-negative decimal integer; only the single digit `0` may begin with zero. Pre-release identifiers, build metadata, omitted components, signs, whitespace, coercion, and moving labels such as `latest` are rejected.

The assertion checks lexical structure only. It does not establish that a version exists, is Accepted, is compatible, is applicable, or is authorized for use.

## Semantic coupling

The schema uses closed objects so concepts that are unsafe or meaningless alone are evaluated together:

1. `artifactInstance.identifier` and `artifactInstance.revision` are both required.
2. `governingContract.identifier` and `governingContract.version` are both required.
3. `governingSchema.identifier` and `governingSchema.version` are both required.
4. Every artifact source reference includes Artifact Type, identifier, and revision.
5. Every contract-definition source reference includes identifier and exact version.
6. Every schema-definition source reference includes identifier and exact version.
7. Every digest entry includes a complete subject pin, method, and value.

The object grouping preserves coupling without merging the meanings of identifier, revision, and version.

## Provenance-reference capability

`provenanceReferences` accepts exactly three closed reference shapes distinguished by `kind`:

| `kind` | Required pin |
| --- | --- |
| `artifact` | Artifact Type, Artifact Instance Identifier, and Artifact Revision |
| `contract-definition` | Contract Definition Identifier and Contract Definition Version |
| `schema-definition` | Schema Identifier and Schema Version |

The array uses `uniqueItems: true`, which rejects exact duplicate JSON-compatible values. It does not establish identifier-global uniqueness or semantic equivalence between differently encoded references.

A reference records only what source is pinned. It does not say why the source matters, whether it is authoritative or sufficient, whether it is fresh, which direction a relationship has, whether retrieval is allowed, or whether the referenced content may be copied. Those remain artifact-specific and policy-governed questions.

## Content Digest evidence

Each `contentDigests` entry contains:

- `subject`, using one complete provenance-reference target;
- `method`, as a non-empty opaque string; and
- `value`, as a non-empty opaque string.

No algorithm registry, canonicalization, encoding, byte scope, signature, verification process, trust model, or security claim is selected. A method string does not prove that an algorithm was executed correctly. A value does not establish integrity, authenticity, provenance, authority, approval, or permission to disclose the subject.

## Closed-world behavior

Every object schema uses `additionalProperties: false`. This rejects fields that would otherwise silently expand the common boundary, including authority, approval, lifecycle, Document Status, Implementation Version, payload, relationship role, extensions, profiles, runtime metadata, or provider-specific values.

Closed objects are a CNTX compatibility choice. A later accepted property addition changes the executable structural surface and requires at least a MINOR version assessment; removing or tightening an accepted property can require a MAJOR version. Validation success against `1.0.0` must not be inferred for future versions.

The schema supplies no `default`. Validators and consumers must not synthesize missing identity, revision, version, provenance, or digest values.

## Validation evidence

The [non-normative test manifest](../../tests/schemas/common-artifact-envelope/1.0.0/cases.json) covers:

- all nine Artifact Type enum values;
- the four-property minimal envelope;
- all three provenance target kinds;
- optional digest evidence;
- semantic-version zero and multi-digit components;
- missing required properties and incomplete pins;
- unknown Artifact Type and unknown properties;
- blank identifiers and methods;
- malformed semantic versions;
- `null` and empty evidence placeholders;
- duplicate provenance entries;
- malformed digest entries; and
- forbidden authority, lifecycle, and extension fields.

The manifest records expected validity only. It is synthetic evidence, not a Serialization Binding, accepted Artifact Instance, artifact contract, validator, validation-output contract, conformance claim, approval, or authority source.

Validation of the accepted resource must reject duplicate JSON object member names, validate the schema under the official Draft 2020-12 meta-schema, and execute every test case with a standards-conformant Draft 2020-12 validator isolated outside the repository. No validator dependency or implementation is part of this decision.

## Serialization and instance-data boundary

The Schema Resource is represented as JSON because JSON Schema itself is a JSON-based schema language. Test instances are stored as JSON solely to supply reproducible values in the JSON-compatible instance data model.

This does not select an artifact JSON Serialization Binding, canonical JSON, member ordering, whitespace, encoding beyond repository UTF-8, duplicate-member handling for artifact transports, YAML, CBOR, transport, storage, archive, or media type for artifact instances. Those remain separate decisions.

## Security and privacy boundary

The schema requires no secret, credential, personal data, private path, production configuration, provider-specific value, private project context, restricted source content, or private implementation detail.

Opaque identifiers and references do not grant permission to discover, fetch, reveal, cache, mirror, publish, or trust their targets. An HTTPS-shaped Schema Identifier is not network authorization. Validators and resolvers must not infer automatic retrieval from this resource, although their concrete security controls remain outside ARCH-009.

The schema cannot determine whether a syntactically valid identifier or digest value contains information that policy forbids. Producers, artifact-specific contracts, review, and applicable security/privacy policy remain responsible for that judgment.

## Review, approval, and conformance boundary

Schema validity is narrower than normative-contract conformance. The schema checks the structural envelope assertions it contains; it cannot determine whether:

- an identifier names the claimed logical object;
- a revision or version exists or is Accepted;
- a source is authoritative, sufficient, current, or accessible;
- a digest is correctly calculated;
- an artifact-specific payload satisfies its contract;
- an approval was validly given; or
- a release, deployment, merge, or action is authorized.

The exact reviewed candidate received human Owner / Final Authority acceptance in issue comment `5208715683`. Governed integration makes the accepted resource and Schema Version `1.0.0` active without changing the non-authority boundary of schema validity.

## Consequences and tradeoffs

The accepted decision provides a small executable foundation:

- common identity and version pins are machine-checkable;
- incomplete semantic pairs fail closed;
- the nine canonical artifact kinds cannot drift lexically;
- generic provenance and digest capabilities exist without absorbing artifact-specific meaning;
- unknown fields cannot silently redefine the common boundary;
- the schema has no external dependency or automatic-network requirement; and
- future artifact-specific schemas can depend on one exact common resource.

The tradeoffs are intentional:

- identifiers and revisions remain lexically broad because their generation and namespace policies are not common-envelope concerns;
- the schema cannot verify authority, acceptance, source existence, digest correctness, or privacy safety;
- closed objects require explicit versioned evolution;
- no extension or profile field exists before Layer 5 governance; and
- no complete artifact can be validated until an independently governed artifact-specific schema defines its payload and common-envelope placement.

## Rejected alternatives

### Validate a complete artifact at the common root

Rejected because it would select artifact container layout, absorb payload structure, and erase independently governed artifact-specific schemas.

### Put all coupled values in flat root fields

Rejected because identifier/revision and identifier/version pairs would be easier to separate accidentally and harder to review as semantic pins.

### Make identifiers absolute URIs universally

Rejected because ARCH-002 requires opaque, domain-independent identifiers and no accepted common rule requires all artifact or contract identifiers to use URI syntax.

### Make provenance required for every envelope

Rejected because ARCH-005 requires representation capability but leaves instance activation to accepted artifact semantics. Fabricated provenance is worse than explicit absence.

### Encode relationship roles in provenance references

Rejected because relationship purpose, direction, sufficiency, freshness, replacement, and conflict are artifact-specific responsibilities.

### Select a digest algorithm

Rejected because algorithm, encoding, canonicalization, scope, and verification remain separately governed and are not necessary to express subject-bound digest evidence.

### Add authority, approval, lifecycle, status, or implementation fields

Rejected because ARCH-004 and ARCH-005 explicitly place those meanings outside common-envelope ownership.

### Reserve extension or profile properties

Rejected because ARCH-005 forbids activating those capabilities before a separately accepted Layer 5 representation and mechanics decision.

### Permit unknown fields for forward compatibility

Rejected because ungoverned properties could silently create public semantics, weaken reviewability, and pre-empt version assessment.

### Use public `$anchor` or dynamic references

Rejected because ARCH-008 selects no public subschema API and no dynamic extension surface for the initial definition.

### Use a moving or unversioned `$id`

Rejected because consequential references must pin an immutable accepted Schema Version.

### Treat a passing validator as acceptance

Rejected because executable validity is evidence only; final acceptance remains an attributable human governance decision.

## Deferred and prohibited scope

ARCH-009 does not define or authorize artifact-specific schemas or payloads; full artifact container structure; a normative `envelope` property or placement; relationship role, purpose, direction, multiplicity, sufficiency, freshness, replacement, or conflict; approval evidence, decision rationale, findings, task content, declared state, or canonical classification fields; Contract Definition identity/version allocation; Artifact Instance Identifier generation or revision sequencing; digest algorithms, encoding, canonicalization, signatures, or verification; Extension Module or Profile mechanics; artifact Serialization Bindings; canonical JSON, YAML, or CBOR bindings; transport, storage, archives, media types for artifact instances; bundles, manifests, registries, resolvers, catalogs, caches, automatic network retrieval, mirrors, redirects, or hosted publication; validator selection or implementation; validation-output contracts; conformance tooling; code generation; migrations; APIs; CLIs; workflows; engines; runtimes; providers; products; private implementations; reference implementations; releases; tags; or deployments.

## Continuing gate

The exact candidate was validated and reviewed at commit `e589f465f55195ff512de84a524f2812e49fc197`, then accepted by the human Owner / Final Authority in issue comment `5208715683`. The authorized status-only promotion and governed integration do not authorize the first artifact-specific executable schema, a Serialization Binding, validator, resolver, bundle, release, deployment, or any other Schema Family layer.
