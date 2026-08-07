# CNTX Schema Resources

## Status and authority

This directory contains machine-evaluable schema-resource candidates and, after exact-revision human acceptance and governed integration, accepted schema resources. A file's existence, JSON Schema validity, `$id`, Schema Version, test result, repository location, or publication does not grant Document Status, contract conformance, authority, trust, approval, release, deployment, merge permission, or access permission.

The current Accepted resources are the ARCH-009 [Common Artifact Envelope Schema Version `1.0.0`](common-artifact-envelope/1.0.0/schema.json), approved by the Owner / Final Authority in issue comment `5208715683`, and the ARCH-012 [Project Charter Schema Version `1.0.0`](project-charter/1.0.0/schema.json), accepted in issue comment `5210242651`. Governed integration to `main` activates each exact resource. The applicable architecture documents and ADRs remain the status sources.

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

## Project Charter Schema Version 1.0.0

| Dimension | Accepted value |
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
| Document Status | Accepted under issue #48 and Owner acceptance comment `5210242651` |

The resource evaluates one complete closed Project Charter artifact with mandatory `envelope` and `payload`. Its envelope statically references the complete Accepted Common Artifact Envelope and constrains the exact Project Charter Artifact Type, governing Contract, and governing Schema pins. Its closed payload implements only the Accepted responsibilities of CONTRACT-001.

The [ARCH-012 architecture decision](../docs/architecture/project-charter-executable-schema.md), [ADR-0012](../docs/architecture/adr/0012-project-charter-executable-schema.md), and [non-normative test manifest](../tests/schemas/project-charter/1.0.0/cases.json) define and evidence the Accepted boundary. Validation, repository presence, `$id`, or review did not grant acceptance or activation; exact-head Owner / Final Authority acceptance is recorded in issue comment `5210242651`, and governed integration to `main` activates Schema Version `1.0.0`. Schema validity still grants no conformance, approval, authority, release, or deployment.

## Change boundary

Upon governed integration, exact Accepted versioned canonical standalone content is immutable. Any accepted structural or semantic change requires the applicable identity/version assessment, attributable review and approval, traceable provenance, and a separately authorized change. Schema validity alone cannot approve such a change. The Accepted Project Charter resource does not change the independently Accepted Common Artifact Envelope resource.
