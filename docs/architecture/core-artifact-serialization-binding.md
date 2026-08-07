# CNTX Core Artifact Serialization Binding Architecture (ARCH-022)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only architecture decision governed
by [issue #70](https://github.com/CNTX-PROJECT/CNTX/issues/70) and recorded by
[ADR-0022](adr/0022-core-artifact-serialization-binding.md). EIGENAAR / Final
Authority acceptance of the exact reviewed candidate is recorded in issue
comment `5221466569`. Governed integration to `main` adopts this exact decision
and activates Binding Version `1.0.0`. Creation, repository presence,
validation, and transparent non-independent review did not grant acceptance.

This decision remains subordinate to Accepted architecture, Accepted artifact
contracts, Accepted executable schemas, repository governance, security and
privacy boundaries, controlling sources, and final human authority. It changes
none of those sources.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
expresses permission. These terms express requirement strength only within
this Accepted decision.

## Purpose and decision boundary

The completed CNTX Public Core contract-and-schema foundation constrains the
JSON-compatible instance-data model evaluated by ten Accepted JSON Schema
resources. Those resources do not define the portable bytes, characters,
media type, document boundary, duplicate-name behavior, numeric handling,
Unicode treatment, ordering, whitespace, or reserialization behavior of a
complete CNTX Artifact Instance.

This decision defines the first concrete artifact Serialization Binding. It
maps one complete artifact-specific executable-schema instance-data model to
one RFC 8259 JSON text while preserving the exact governing contract meaning,
Schema Identity, Schema Version, Common Artifact Envelope, and artifact-
specific payload boundary.

This decision is not an Artifact Instance, example payload, executable schema,
schema change, storage format, transport protocol, canonicalization scheme,
validator, resolver, conformance protocol, implementation, release,
publication, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Final human authority, bounded tasks, evidence-before-claims, security/privacy, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Artifact, contract, schema, status, implementation, digest, and provenance dimensions remain distinct; lexical form grants no authority. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | A Serialization Binding maps an executable schema to a concrete representation, remains subordinate to Accepted contracts and schemas, and is not a storage decision. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) | Common-envelope capabilities, instance activation, semantic coupling, absence distinctions, and artifact-specific payload ownership remain intact. |
| [ARCH-008](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) | Schema-resource identity, exact-version references, standalone resources, and offline-first supply do not become artifact representation or network authority. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) and [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md) | Common Artifact Envelope Schema Version `1.0.0` remains unchanged and is not a complete Artifact Instance container or binding. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) and [ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md) | Every complete artifact retains one closed root object with exact `envelope` and `payload` ownership. |
| ARCH-012 through ARCH-020 and their ADRs | The nine Accepted artifact-specific Schema Versions `1.0.0`, assertions, tests, and independent version lines remain unchanged. |
| [ARCH-021](public-core-completion-boundary-roadmap.md) and [ADR-0021](adr/0021-public-core-completion-boundary-roadmap.md) | Serialization Binding precedes portable Artifact Instance validation and must decide representation and compatibility boundaries without authorizing later layers. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Every artifact retains its Accepted purpose, classification, authority limits, payload meaning, relationships, provenance, lifecycle, and privacy boundary. |
| [Issue #70](https://github.com/CNTX-PROJECT/CNTX/issues/70) | Work remained documentation-only and limited to five paths; exact-head acceptance and governed integration grant no authority beyond this decision. |

## Serialization Binding identity and version

| Coordinate | Accepted value |
| --- | --- |
| Logical namespace | **CNTX Public Core Serialization Binding Family** |
| Logical local identity | **Core Artifact JSON** |
| Full logical identity | **CNTX Public Core Serialization Binding Family / Core Artifact JSON** |
| Initial Binding Version | `1.0.0` |
| Current status | Accepted; active upon governed integration to `main` |

The version-independent identity identifies one mapping from the CNTX complete-
artifact JSON-compatible instance model to the representation defined here. It
is not a Schema Identifier, Contract Definition Identifier, Artifact Type,
Artifact Instance Identifier, media type, URI, repository path, registry key,
resolver address, release coordinate, implementation, authority, approval, or
trust assertion.

Binding Version remains distinct from Contract Definition Version, Schema
Version, Artifact Revision, Document Status, and Implementation Version.
Governed integration after exact-revision acceptance and status promotion
activates Binding Version `1.0.0`; completion evidence records that lifecycle.
Matching version numbers across dimensions imply no identity or compatibility.

No artifact field is allocated for Serialization Binding Identity or Binding
Version. A future conformance evaluation receives or identifies them as
governing inputs outside the artifact content.

## Applicability and schema relationship

The binding applies to one complete CNTX Artifact Instance governed by one
exact artifact-specific Schema Identifier and Schema Version. Its
representation contains exactly one JSON object subject to that complete-
artifact schema and its Accepted closed `envelope` and `payload` root model.

Under the Accepted and integrated Binding Version `1.0.0`, this binding can represent
instances governed by the nine current artifact-specific Schema Versions
`1.0.0`. It does not alter those schemas. A future schema version or artifact
kind requires an explicit binding-compatibility assessment.

The standalone Common Artifact Envelope Schema Resource is not a complete
Artifact Instance binding. Schema Resources use JSON and media type
`application/schema+json`; artifacts under this binding use `application/json`.
A schema `$id`, repository file, schema bundle, or synthetic test manifest does
not become an Artifact Instance or artifact binding.

## JSON representation and media type

A conforming representation MUST be one JSON text as defined by
[RFC 8259](https://www.rfc-editor.org/rfc/rfc8259). Its media type is
`application/json`.

This decision allocates no custom, vendor, or profile media type and no
normative `charset` parameter. The media type identifies generic JSON only; it
does not identify a binding version, Artifact Type, Contract Definition,
Schema Identifier or Version, authority, privacy classification, trust,
approval, validity, or conformance result.

Content negotiation, profile negotiation, transport metadata, filename
inference, and media-type registration processes remain outside scope.

## UTF-8 and byte-order mark

Core Artifact JSON MUST be well-formed UTF-8. A conforming producer MUST NOT
emit a byte-order mark. Binding Version `1.0.0` treats a leading UTF-8 BOM as a
binding error so conformance does not depend on optional parser tolerance.

Another character encoding or implementation-default decoding is not this
binding. A decoder MUST establish valid UTF-8 before parsing and MUST NOT
silently replace malformed byte sequences.

## Duplicate object member names

Every member name within a JSON object MUST be unique in that object. A
duplicate is a Serialization Binding error before executable-schema
evaluation. First-wins, last-wins, overwriting, merging, warning-only handling,
silent deduplication, and parser-dependent selection are forbidden.

Uniqueness is evaluated on represented JSON string values after escape
processing, not on raw escape spelling. Schema success cannot convert a
duplicate-bearing representation into a binding-conformant representation.

## Numeric representation

Only numbers permitted by the RFC 8259 JSON grammar are admitted. NaN,
positive or negative Infinity, locale-specific forms, and implementation-
specific numeric tokens are forbidden.

A producer MUST preserve the intended mathematical JSON number value. A
consumer unable to preserve or evaluate that value without rounding, coercion,
overflow, underflow, truncation, or precision loss MUST fail or report an
unsupported limitation. It MUST NOT silently alter the value.

No current Accepted artifact-specific schema defines an instance field with
type `integer` or `number`. Future numeric schema semantics require their own
compatibility assessment. This decision selects no numeric library, machine
type, IEEE profile, precision limit, or numeric API.

## Unicode and string treatment

After UTF-8 decoding and JSON escape processing, every member name and string
value MUST represent valid Unicode scalar values. Malformed UTF-8 and unpaired
surrogate escapes are binding errors. Different valid escape spellings that
encode the same sequence represent the same JSON string value.

A producer or consumer MUST preserve the represented scalar-value sequence
unless a separately Accepted semantic rule explicitly authorizes a
transformation. This binding performs no implicit Unicode normalization, case
folding, locale transformation, transliteration, sanitization, redaction, or
string coercion. NFC, NFD, NFKC, and NFKD are not selected.

## Ordering and whitespace

JSON object member order is non-semantic. No contract, schema, authority,
identity, approval, digest, conformance, lifecycle, or revision meaning may be
derived from it. Array element order remains part of the JSON data model and
MUST be preserved.

Only whitespace permitted by RFC 8259 is allowed. It is non-semantic.
Indentation, line endings, compactness, and presentation style do not change
the represented Artifact Instance.

## Explicit absence of canonicalization

Binding Version `1.0.0` defines no canonical JSON or bytes, object-member sort,
whitespace form, numeric lexical form, escape form, Unicode normalization, or
deterministic reserialization. Semantically equivalent representations may
differ byte-for-byte.

[RFC 8785 JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785)
is not selected. A Content Digest, signature, verification process, cache key,
equality test, provenance assertion, or Artifact Revision MUST NOT assume
canonical bytes from this binding.

A future canonicalization decision must define its exact input model,
algorithm, Unicode and numeric rules, output bytes, compatibility,
digest/signature scope, errors, and authority under a separate Accepted
decision and version assessment.

## Document, file, and stream boundaries

One representation contains exactly one RFC 8259 JSON text for exactly one
Artifact Instance. The root value MUST be one object. Only RFC 8259 whitespace
may precede or follow the value; no other bytes are allowed.

The following are not this binding: JSON Lines, NDJSON, concatenated JSON,
multi-artifact wrapper arrays, comments, trailing commas, alternative JSON,
multipart packaging, archives, compression, encryption, transport framing,
message framing, stream framing, or storage layout.

A `.json` filename is conventional only. File naming, directories, storage,
delivery, compression, encryption, and framing remain outside scope. A stream
or message must provide its boundary externally; this binding provides no
framing protocol.

## Failure-layer separation

Processes applying this binding MUST keep distinct:

1. transport or externally supplied document-boundary failure;
2. byte, UTF-8, or BOM failure;
3. JSON syntax failure;
4. binding failure, including duplicate, Unicode, numeric, root, or boundary
   violations;
5. missing, ambiguous, conflicting, unavailable, or unsupported governing
   binding or schema input;
6. executable-schema evaluation failure; and
7. normative-contract nonconformance or an unverifiable condition.

Parser recovery, duplicate resolution, default insertion, type coercion,
normalization, silent precision loss, filename-based schema selection,
automatic `latest` selection, and automatic network retrieval are forbidden as
implied binding behavior.

This decision defines no portable diagnostics, codes, severity, warning model,
validation output, API, or CLI. Those remain for a separate layer.

## Governing inputs and conformance boundary

A future binding-conformance evaluation MUST receive or identify the exact
Serialization Binding Identity, Binding Version, artifact-specific Schema
Identifier, and Schema Version. These are governing inputs, not new envelope
or payload fields. Schema-resource supply remains for the later resolution and
catalog decision.

JSON syntax validity, binding conformance, schema validity, contract
conformance, provenance quality, truth, completeness, authority, approval,
interoperability, and implementation conformance remain distinct. No result
proves another unless a future Accepted contract defines that relationship.

Binding validity grants no final acceptance, merge permission, release
permission, access, disclosure, trust, or authority.

## Compatibility and change boundary

Accepted Binding Versions use `MAJOR.MINOR.PATCH`:

- **MAJOR** changes interpretation, media type, encoding, required document
  boundary, or makes a previously conforming representation nonconforming.
- **MINOR** adds capability while preserving every conforming representation
  and interpretation of the same major line.
- **PATCH** is a non-semantic correction or clarification only.

Compatibility is not inferred from `application/json`, a filename, schema
validity, shared version number, mutable `latest`, branch, or repository path.
Every Accepted change requires governance, compatibility assessment, and
provenance. A future schema version must identify whether it remains
representable by this binding. A binding version cannot redefine Accepted
contract or schema meaning.

## Security and privacy

Parsing or binding conformance grants no access, disclosure, permission,
authority, approval, authenticity, integrity, confidentiality, trust, safety,
or right to retrieve referenced content. Artifact classification and allowed
disclosure remain governed by Accepted contracts and policy.

Implementations must treat untrusted JSON as untrusted input and bound resource
use. This decision selects no parser, library, size, depth, string, or numeric
limit, sandbox, access control, redaction, sanitization, encryption, retention,
transport, or threat-response mechanism. Limitations must remain visible and
must not be silently reported as schema validity or contract conformance.

Public artifacts, examples, fixtures, logs, and reports MUST NOT expose
secrets, credentials, personal data, production configuration, private paths,
restricted source content, private project context, provider assumptions, or
private implementation details.

## Alternatives considered and rejected

- Treat schema-resource JSON as the artifact binding: rejected because schema
  representation and Artifact Instance representation are different layers.
- Permit parser-dependent duplicate and numeric behavior: rejected because it
  creates implementation-dependent data models and evidence.
- Select RFC 8785 JCS now: rejected because canonicalization and cryptographic
  scope require a separate reviewable decision.
- Allocate a custom media type: rejected because `application/json` identifies
  the format while no media type alone identifies all governing dimensions.
- Put Binding Identity and Version in every artifact: rejected because the
  Accepted schemas contain no such field and a binding cannot add one.
- Combine framing, transport, storage, validation, or tooling: rejected because
  these are separate layers and implementation choices.

## Deferred and prohibited scope

This decision defines no Artifact Instance or example; identifier generation
or revision sequencing; Contract Definition or Schema identity/version;
schema/test change; binding field; custom media type; JSONL, NDJSON, YAML,
CBOR, or another binding; canonical JSON/JCS; digest algorithm, byte scope,
signature, verification, or trust store; transport, storage, archive,
compression, encryption, or framing; Extension Module/Profile; resolver,
registry, catalog, cache, bundler, mirror, redirect, or network; validator or
output; conformance protocol/tooling; code generation; migration; template;
form; checklist; rubric; prompt; API; CLI; workflow; engine; scheduler;
orchestrator; runtime; provider/product work; private/reference implementation;
supported-version claim; release; tag; hosted publication; or deployment.

## Lifecycle and final human authority

The Proposed candidate did not approve itself. Creation, validation,
repository presence, issue or PR state, and transparent non-independent review
did not grant acceptance. EIGENAAR / Final Authority accepted the exact
reviewed revision in issue comment `5221466569`; governed integration activates
exactly Binding Version `1.0.0`.

Acceptance, promotion, and integration authorize no later roadmap layer.
Resolver/catalog, validation/output, conformance, implementation, release,
publication, and deployment work remains unauthorized.

## References

- [CNTX core architecture](core-contract.md)
- [Contract identity and versioning](contract-identity-versioning.md)
- [Artifact contract and schema layering](artifact-contract-schema-architecture.md)
- [Common Artifact Envelope representation boundary](common-artifact-envelope-representation-boundary.md)
- [Common Artifact Envelope schema composition and packaging](common-artifact-envelope-schema-composition-packaging.md)
- [Common Artifact Envelope executable schema](common-artifact-envelope-executable-schema.md)
- [Artifact-specific schema family and container boundary](artifact-specific-schema-family-container-boundary.md)
- [Public Core completion boundary and roadmap](public-core-completion-boundary-roadmap.md)
- [Artifact contract index](../contracts/README.md)
- [Schema resource index](../../schemas/README.md)
- [Governance](../../GOVERNANCE.md)
- [Security](../../SECURITY.md)
- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)
- [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785)
- [ADR-0022](adr/0022-core-artifact-serialization-binding.md)
- [Issue #70](https://github.com/CNTX-PROJECT/CNTX/issues/70)
