# CNTX Schema Resources

## Status and authority

This directory contains machine-evaluable schema-resource candidates and, after exact-revision human acceptance and governed integration, accepted schema resources. A file's existence, JSON Schema validity, `$id`, Schema Version, test result, repository location, or publication does not grant Document Status, contract conformance, authority, trust, approval, release, deployment, merge permission, or access permission.

The current Accepted resources are the ARCH-009 [Common Artifact Envelope Schema Version `1.0.0`](common-artifact-envelope/1.0.0/schema.json), approved by the Owner / Final Authority in issue comment `5208715683`; the ARCH-012 [Project Charter Schema Version `1.0.0`](project-charter/1.0.0/schema.json), accepted in issue comment `5210242651`; the ARCH-013 [Workstream Schema Version `1.0.0`](workstream/1.0.0/schema.json), accepted in issue comment `5215029431`; the ARCH-014 [Task Contract Schema Version `1.0.0`](task-contract/1.0.0/schema.json), accepted in issue comment `5215700352`; and the ARCH-015 [Context Packet Schema Version `1.0.0`](context-packet/1.0.0/schema.json), accepted in issue comment `5216466742`. Governed integration to `main` activates each exact resource. The applicable architecture documents and ADRs remain the status sources.

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

## Workstream Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Workstream Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/workstream/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/workstream` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #52 and Owner acceptance comment `5215029431` |

The resource evaluates one complete closed Workstream artifact with mandatory
`envelope` and `payload`. Its envelope statically references the complete
Accepted Common Artifact Envelope and constrains the exact Workstream Artifact
Type, governing Contract, and governing Schema pins. Its closed payload
implements only the Accepted responsibilities of CONTRACT-002, including an
opaque governing Project Charter Artifact Instance/Revision pin. It contains
no Project Charter schema `$ref` or other artifact-to-artifact schema
dependency.

The [ARCH-013 architecture decision](../docs/architecture/workstream-executable-schema.md),
[ADR-0013](../docs/architecture/adr/0013-workstream-executable-schema.md), and
[non-normative test manifest](../tests/schemas/workstream/1.0.0/cases.json)
define and evidence the Accepted boundary. Creation, validation, review,
repository presence, or `1.0.0` did not grant acceptance or activation;
exact-head Owner / Final Authority acceptance is recorded in issue comment
`5215029431`, and governed integration to `main` activates Schema Version
`1.0.0`. Schema validity still grants no contract conformance, approval,
authority, release, deployment, merge permission, or Task Contract schema
authority.

## Task Contract Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Task Contract Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/task-contract/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/task-contract` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #54 and Owner acceptance comment `5215700352` |

The resource evaluates one complete closed Task Contract artifact with
mandatory `envelope` and `payload`. Its envelope statically references the
complete Accepted Common Artifact Envelope and constrains the exact Task
Contract Artifact Type, governing Contract, and governing Schema pins. Its
closed payload implements only the Accepted responsibilities of CONTRACT-003,
including separate opaque governing Project Charter and Workstream Artifact
Instance/Revision pins.

The resource contains no Project Charter, Workstream, peer Task Contract, or
other artifact-specific schema `$ref`. Scope, action, resource, authority,
context, evidence, decision, and lifecycle statements remain declarative. The
schema defines no permission language, approval mechanism, workflow, runtime,
or Task Contract authority.

The [ARCH-014 architecture decision](../docs/architecture/task-contract-executable-schema.md),
[ADR-0014](../docs/architecture/adr/0014-task-contract-executable-schema.md),
and [non-normative test manifest](../tests/schemas/task-contract/1.0.0/cases.json)
define and evidence the Accepted boundary. Creation, validation, review,
repository presence, or `1.0.0` did not grant acceptance or activation;
exact-head Owner / Final Authority acceptance is recorded in issue comment
`5215700352`, and governed integration to `main` activates Schema Version
`1.0.0`. Schema validity still grants no contract conformance, task authority,
merge permission, release, deployment, or Context Packet schema authority.

## Context Packet Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Context Packet Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/context-packet/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #56 and Owner acceptance comment `5216466742` |

The resource evaluates one complete closed Context Packet artifact with
mandatory `envelope` and `payload`. Its envelope statically references the
exact Accepted Common Artifact Envelope and constrains only the Context Packet
Artifact Type and governing Contract and Schema coordinates. Its closed
thirteen-property payload translates only CONTRACT-004 and includes one opaque
governing Task Contract Artifact Instance/Revision pin.

The resource contains no Project Charter, Workstream, Task Contract, peer,
Execution Result, or downstream schema `$ref`. Selected-source references and
representation treatments remain declarative and provide no selection,
retrieval, ranking, access, disclosure, transformation, prompt, workflow, or
runtime behavior.

The [ARCH-015 architecture decision](../docs/architecture/context-packet-executable-schema.md),
[ADR-0015](../docs/architecture/adr/0015-context-packet-executable-schema.md),
and [non-normative test manifest](../tests/schemas/context-packet/1.0.0/cases.json)
define and evidence the Accepted boundary. Creation, validation, review,
repository presence, or `1.0.0` did not grant acceptance or activation;
exact-head Owner / Final Authority acceptance is recorded in issue comment
`5216466742`, and governed integration to `main` activates Schema Version
`1.0.0`. Schema validity still grants no contract conformance, task authority,
source access, retrieval or disclosure permission, merge permission, release,
deployment, or Execution Result schema authority.

## Change boundary

Upon governed integration, exact Accepted versioned canonical standalone content is immutable. Any accepted structural or semantic change requires the applicable identity/version assessment, attributable review and approval, traceable provenance, and a separately authorized change. Schema validity alone cannot approve such a change. The Accepted Project Charter resource does not change the independently Accepted Common Artifact Envelope resource.
