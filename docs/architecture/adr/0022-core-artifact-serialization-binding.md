# ADR-0022: Core Artifact JSON serialization binding

- **Status:** Accepted
- **Date:** 2026-08-07
- **Issue:** [#70](https://github.com/CNTX-PROJECT/CNTX/issues/70)
- **Decision:** ARCH-022 — CNTX Core Artifact Serialization Binding Architecture

## Context

Accepted ARCH-001 through ARCH-021, nine artifact contracts, one Common
Artifact Envelope Schema Version `1.0.0`, and nine artifact-specific Schema
Versions `1.0.0` establish a completed contract-and-schema foundation. The
schemas constrain a JSON-compatible instance-data model but do not define
portable artifact bytes, media type, encoding, duplicate behavior, numbers,
Unicode, ordering, whitespace, canonicalization, document boundaries, or
binding failures.

ARCH-021 requires a separately governed Serialization Binding before portable
Artifact Instance validation. The binding must preserve contract and schema
meaning and must not absorb later resolver, validator, conformance,
implementation, or release layers.

## Decision

Adopt logical identity **CNTX Public Core Serialization Binding Family / Core
Artifact JSON** with initial Binding Version `1.0.0`. EIGENAAR / Final Authority
accepted the exact reviewed candidate in issue comment `5221466569`; governed
integration activates the Binding Version.

The binding maps one complete Artifact Instance governed by one exact artifact-
specific Schema Identifier and Version to exactly one RFC 8259 JSON text rooted
in one object. It uses `application/json` and UTF-8 without BOM.

Schema Resource JSON with `application/schema+json` remains distinct. The
standalone Common Artifact Envelope resource is not a complete binding. The
decision adds no field to `envelope` or `payload` and changes no contract,
schema, test, identifier, or version.

## Representation rules

- Object member names are unique after escape processing; duplicates fail
  before schema evaluation.
- Only RFC 8259 numbers are admitted. NaN, Infinity, coercion, rounding,
  truncation, and silent precision loss are forbidden.
- Input is well-formed UTF-8 and strings contain valid Unicode scalar values.
  Malformed bytes and unpaired surrogate escapes fail.
- No implicit Unicode normalization, case folding, locale transformation,
  sanitization, redaction, or coercion occurs.
- Object order and permitted JSON whitespace are non-semantic; array order is
  semantic and preserved.
- Binding Version `1.0.0` defines no canonical JSON/bytes and does not select
  RFC 8785 JCS.
- One representation contains one JSON text for one Artifact Instance. JSONL,
  NDJSON, concatenated JSON, wrapper arrays, comments, trailing commas,
  archives, compression, encryption, transport, storage, and framing are not
  the binding.
- A `.json` filename is conventional and non-authoritative.

## Failure and conformance boundary

Transport/external-boundary, byte/UTF-8/BOM, JSON syntax, binding, governing-
input, executable-schema, and normative-contract outcomes remain distinct. No
recovery, duplicate resolution, defaults, coercion, normalization, filename-
based schema selection, `latest` selection, or automatic network retrieval is
implied.

A future evaluation receives or identifies exact Binding Identity/Version and
artifact-specific Schema Identifier/Version as governing inputs. ARCH-022
defines no diagnostics, validation output, resolver, catalog, validator,
conformance claim, API, CLI, or implementation.

JSON syntax, binding conformance, schema validity, contract conformance, truth,
provenance quality, interoperability, authority, approval, and implementation
conformance remain distinct.

## Identity, compatibility, and change

Binding Identity and Version remain distinct from contract, schema, artifact,
status, implementation, digest, and provenance dimensions. The identity grants
no authority and allocates no URI, registry record, resolver coordinate,
artifact field, release, or implementation.

Binding Versions use `MAJOR.MINOR.PATCH`. MAJOR changes interpretation, media,
encoding, document boundary, or prior validity; MINOR is strictly additive and
preserves every same-major representation and interpretation; PATCH is non-
semantic clarification only. Compatibility is not inferred from JSON, media
type, filename, schema validity, shared numbers, `latest`, path, or branch.

## Rationale

RFC 8259 JSON matches the existing schema instance-data model and is portable
without selecting a vendor, runtime, storage, transport, or product. Strict
UTF-8, duplicate rejection, scalar-value strings, exact numeric handling, and
failure boundaries eliminate parser-dependent interpretations.

Omitting canonicalization permits portable non-canonical exchange without
silently defining cryptographic, digest, signature, revision, or byte-equality
semantics.

## Consequences and tradeoffs

- CNTX gains one concrete portable artifact representation only if this exact
  decision is later Accepted and activated.
- Existing schemas and tests remain unchanged.
- Implementations reject duplicates, malformed UTF-8, BOMs, invalid scalar
  values, and silent numeric loss even when a generic parser is permissive.
- Formatting may vary; byte comparison is not artifact equality.
- Streams and transports require an external document boundary.
- Portable validation still requires later resolution/catalog and
  validation/output decisions.

## Rejected alternatives

Rejected: treating Schema Resource JSON as the artifact binding; allowing
parser-dependent duplicates or numbers; selecting RFC 8785 JCS now; allocating
a custom media type; adding Binding Identity/Version fields; adding JSONL,
NDJSON, YAML, or CBOR; and combining framing, transport, storage, resolution,
validation, tooling, or implementation with this decision.

## Security and privacy

Parsing and binding conformance grant no access, disclosure, permission,
authority, approval, authenticity, integrity, confidentiality, trust, safety,
or retrieval right. Untrusted JSON remains untrusted. Implementations must
bound resource use, but this decision selects no parser, library, limit,
sandbox, access control, redaction, encryption, retention, transport, or
threat-response mechanism.

Public work must not expose secrets, credentials, personal data, production
configuration, private paths/context, restricted content, provider
assumptions, or private implementation details.

## Authority and conformance boundary

This ADR and ARCH-022 are Accepted. Creation, repository presence, validation,
and transparent non-independent review did not grant acceptance. EIGENAAR /
Final Authority acceptance of the exact reviewed revision is recorded in issue
comment `5221466569`; governed integration adopts exactly that decision.

Binding conformance grants no schema validity, contract conformance, truth,
approval, authority, trust, interoperability, merge permission, release,
publication, deployment, or follow-on authority.

## Deferred scope

Deferred and unauthorized: Artifact Instances/examples; identity generation or
revision sequencing; schema/test changes; binding fields; custom media; other
serialization formats; canonical JSON/JCS; digest, signature, verification, or
trust; transport, storage, archive, compression, encryption, or framing;
Extension Module/Profile; resolver, registry, catalog, cache, bundler, mirror,
redirect, or network; validator/output; conformance tooling; code generation;
migration; template; form; prompt; API; CLI; workflow; runtime; provider/product
work; private/reference implementation; release; tag; hosted publication; and
deployment.

## Acceptance and continuing gate

The candidate received one transparent non-independent COMMENT review on its
exact head and then stopped. EIGENAAR / Final Authority separately accepted
that exact revision in issue comment `5221466569`. Acceptance and governed
integration authorize no later roadmap layer, implementation, release,
publication, or deployment.

## References

- [ARCH-022](../core-artifact-serialization-binding.md)
- [ARCH-003](../artifact-contract-schema-architecture.md)
- [ARCH-005](../common-artifact-envelope-representation-boundary.md)
- [ARCH-009](../common-artifact-envelope-executable-schema.md)
- [ARCH-010](../artifact-specific-schema-family-container-boundary.md)
- [ARCH-021](../public-core-completion-boundary-roadmap.md)
- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)
- [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785)
- [Issue #70](https://github.com/CNTX-PROJECT/CNTX/issues/70)
