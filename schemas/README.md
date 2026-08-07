# CNTX Schema Resources

## Status and authority

This directory contains machine-evaluable schema-resource candidates and, after exact-revision human acceptance and governed integration, accepted schema resources. A file's existence, JSON Schema validity, `$id`, Schema Version, test result, repository location, or publication does not grant Document Status, contract conformance, authority, trust, approval, release, deployment, merge permission, or access permission.

The current Accepted resource is the ARCH-009 [Common Artifact Envelope Schema Version `1.0.0`](common-artifact-envelope/1.0.0/schema.json), approved by the Owner / Final Authority in issue comment `5208715683`. Governed integration to `main` activated that exact resource. This directory also contains the **Proposed** ARCH-012 [Project Charter Schema Version `1.0.0` candidate](project-charter/1.0.0/schema.json) governed by issue #48. The candidate is not Accepted or active. The applicable architecture document and ADR remain the status sources.

## Common Artifact Envelope Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Common Artifact Envelope |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/common-artifact-envelope/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #42 and Owner acceptance comment `5208715683` |

The `$id` is the canonical identity of the Schema Resource, not a branch, mutable retrieval coordinate, automatic network instruction, hosted-publication claim, release, tag, artifact Serialization Binding, or authority source. Processors are expected to receive the exact resource explicitly; an HTTPS-shaped identifier does not authorize network access.

## Evaluation boundary

The schema evaluates one Common Artifact Envelope object. It does not define a complete artifact container, normative `envelope` placement, artifact-specific payload or relationship semantics, Extension Module, Profile, validator, resolver, bundler, serialization, transport, storage, runtime, provider, product, or private implementation.

All reusable subschemas are internal members of the root `$defs`. They have no nested `$id`, independent Schema Version, Document Status, or public compatibility guarantee. External schemas must reference the accepted root resource, not a root `$defs` JSON Pointer.

The non-normative [test-case manifest](../tests/schemas/common-artifact-envelope/1.0.0/cases.json) supplies synthetic validation evidence only. It is not an artifact contract, Serialization Binding, validator, conformance claim, authority source, or accepted example payload.

## Proposed Project Charter Schema Version 1.0.0

| Dimension | Proposed value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Project Charter Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0` |
| Candidate Schema Version | `1.0.0` |
| Canonical repository path | `schemas/project-charter/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/project-charter` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Proposed under issue #48 |

The candidate evaluates one complete closed Project Charter artifact with mandatory `envelope` and `payload`. Its envelope statically references the complete Accepted Common Artifact Envelope and constrains the exact Project Charter Artifact Type, governing Contract, and governing Schema pins. Its closed payload implements only the Accepted responsibilities of CONTRACT-001.

The [ARCH-012 architecture candidate](../docs/architecture/project-charter-executable-schema.md), [ADR-0012](../docs/architecture/adr/0012-project-charter-executable-schema.md), and [non-normative test manifest](../tests/schemas/project-charter/1.0.0/cases.json) define and evidence the Proposed boundary. Validation, repository presence, `$id`, review, or mergeability does not activate Schema Version `1.0.0` or grant conformance, approval, authority, acceptance, release, or deployment. Exact-head Owner / Final Authority acceptance and governed integration remain separate gates.

## Change boundary

Upon governed integration, exact Accepted versioned canonical standalone content is immutable. Any accepted structural or semantic change requires the applicable identity/version assessment, attributable review and approval, traceable provenance, and a separately authorized change. Schema validity alone cannot approve such a change. The Proposed Project Charter candidate does not change the already Accepted Common Artifact Envelope resource.
