# CNTX Schema Resources

CNTX currently has ten Accepted Core JSON Schema Resources: one shared envelope
and one resource for each of the nine artifact contracts. It also contains one
Accepted and integrated Module Definition Schema Resource and one Accepted
Profile Definition Schema Resource pending governed integration. Use this
directory when you need the exact machine-evaluable shape of a record, Module
declaration, or Profile application.

## At a glance

| Layer | What it provides | What it does not provide |
| --- | --- | --- |
| [Artifact contracts](../docs/contracts/README.md) | Meaning and responsibilities | JSON shape or validation execution |
| Schema Resources | Exact JSON Schema Draft 2020-12 assertions | Truth, approval, authority, or complete conformance |
| [Synthetic test manifests](../tests/README.md) | Fixed valid and invalid examples | Production evidence, certification, or a universal score |

`Contract meaning → exact Schema Resource → synthetic cases → separately governed validator or tool`

Choose a contract first, then its same-named schema. The complete identities,
versions, `$id` values, acceptance provenance, evaluation boundaries, and
change rules remain available below.

<details>
<summary><strong>Open the complete technical schema register</strong></summary>


## Status and authority

This directory contains machine-evaluable schema-resource candidates and, after exact-revision human acceptance and governed integration, accepted schema resources. A file's existence, JSON Schema validity, `$id`, Schema Version, test result, repository location, or publication does not grant Document Status, contract conformance, authority, trust, approval, release, deployment, merge permission, or access permission.

The current Accepted resources are the ARCH-009 [Common Artifact Envelope Schema Version `1.0.0`](common-artifact-envelope/1.0.0/schema.json), approved by the Owner / Final Authority in issue comment `5208715683`; the ARCH-012 [Project Charter Schema Version `1.0.0`](project-charter/1.0.0/schema.json), accepted in issue comment `5210242651`; the ARCH-013 [Workstream Schema Version `1.0.0`](workstream/1.0.0/schema.json), accepted in issue comment `5215029431`; the ARCH-014 [Task Contract Schema Version `1.0.0`](task-contract/1.0.0/schema.json), accepted in issue comment `5215700352`; the ARCH-015 [Context Packet Schema Version `1.0.0`](context-packet/1.0.0/schema.json), accepted in issue comment `5216466742`; the ARCH-016 [Execution Result Schema Version `1.0.0`](execution-result/1.0.0/schema.json), accepted in issue comment `5217275706`; the ARCH-017 [Evidence Bundle Schema Version `1.0.0`](evidence-bundle/1.0.0/schema.json), accepted in issue comment `5217888146`; and the ARCH-018 [Review Record Schema Version `1.0.0`](review-record/1.0.0/schema.json), accepted in issue comment `5218629573`. Governed integration to `main` activates each exact resource. The applicable architecture documents and ADRs remain the status sources.

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

## Execution Result Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Execution Result Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/execution-result/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/execution-result` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #58 and Owner acceptance comment `5217275706` |

The resource evaluates one complete closed Execution Result artifact with
mandatory `envelope` and `payload`. Its envelope statically references the
exact Accepted Common Artifact Envelope and constrains only the Execution
Result Artifact Type and governing Contract and Schema coordinates. Its closed
fourteen-property payload translates only CONTRACT-005 and includes one opaque
governing Task Contract pin plus a specified-or-none declaration of opaque
Context Packet pins.

The resource contains no Project Charter, Workstream, Task Contract, Context
Packet, peer Execution Result, Evidence Bundle, Review Record, Decision Record,
State Snapshot, or other artifact-specific schema `$ref`. Output, actions,
resources, provenance, check outcomes, criteria assessments, assumptions,
limitations, failures, deviations, stops, escalations, unperformed work,
security/privacy, and traceability remain bounded evidentiary claims. The
schema defines no execution, mutation, access, validation-output, approval,
acceptance, workflow, release, deployment, or merge mechanism.

The [ARCH-016 architecture decision](../docs/architecture/execution-result-executable-schema.md),
[ADR-0016](../docs/architecture/adr/0016-execution-result-executable-schema.md),
and [non-normative test manifest](../tests/schemas/execution-result/1.0.0/cases.json)
define and evidence the Accepted boundary. Creation, validation, review,
repository presence, or `1.0.0` did not grant acceptance or activation;
exact-head Owner / Final Authority acceptance is recorded in issue comment
`5217275706`, and governed integration to `main` activates Schema Version
`1.0.0`. Schema validity still grants no contract conformance, correctness,
completion, integration authority, release, deployment, merge permission,
Evidence Bundle schema authority, or follow-on authority.

## Evidence Bundle Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Evidence Bundle Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/evidence-bundle/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/evidence-bundle` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #60 and Owner acceptance comment `5217888146` |

The resource evaluates one complete closed Evidence Bundle artifact with
mandatory `envelope` and `payload`. Its envelope statically references the
exact Accepted Common Artifact Envelope and constrains only the Evidence
Bundle Artifact Type and governing Contract and Schema coordinates. Its closed
fifteen-property payload translates only CONTRACT-006 and includes one opaque
governing Task Contract pin, exact reviewable-subject declarations, explicit
opaque artifact relationships, Evidence Items, claim traceability, and
bounded provenance, quality, limitation, security/privacy, and lifecycle
declarations.

The resource contains no Project Charter, Workstream, Task Contract, Context
Packet, Execution Result, peer Evidence Bundle, Review Record, Decision Record,
State Snapshot, or other artifact-specific schema `$ref`. Evidence,
provenance, integrity, relevance, completeness, coverage, independence,
reproducibility, sufficiency, uncertainty, limitation, bias, security/privacy,
review, decision, and lifecycle values remain bounded Evidentiary claims. The
schema defines no collection, retrieval, scoring, verification, access,
disclosure, approval, acceptance, workflow, release, deployment, or merge
mechanism.

The Accepted [ARCH-017 architecture decision](../docs/architecture/evidence-bundle-executable-schema.md),
[ADR-0017](../docs/architecture/adr/0017-evidence-bundle-executable-schema.md),
and [non-normative test manifest](../tests/schemas/evidence-bundle/1.0.0/cases.json)
define and evidence the Accepted boundary. Creation, validation, review,
repository presence, or `1.0.0` did not grant acceptance or activation. Exact-head
Owner / Final Authority acceptance is recorded in issue comment `5217888146`,
and governed integration to `main` activates Schema Version `1.0.0`. Schema validity grants no contract
conformance, source truth, relevance, sufficiency, correctness, acceptance,
integration, release, deployment, merge permission, Review Record schema
authority, or follow-on authority.

## Review Record Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Review Record Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/review-record/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/review-record` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #62 and EIGENAAR acceptance comment `5218629573` |

The resource evaluates one complete closed Review Record artifact with
mandatory `envelope` and `payload`. Its envelope statically references the
exact Accepted Common Artifact Envelope and constrains only the Review Record
Artifact Type and governing Contract and Schema coordinates. Its closed
sixteen-property payload separates Review Authority from Execution Authority,
requires exact reviewable subjects and nine opaque artifact-relationship
categories, preserves distinct observations, interpretations, findings,
rationale, evidence use, uncertainty, dissent, and recommendations, and records
bounded peer-review, correction, security/privacy, escalation, stop, and
lifecycle traceability.

The resource contains no Project Charter, Workstream, Task Contract, Context
Packet, Execution Result, Evidence Bundle, peer Review Record, Decision Record,
State Snapshot, or other artifact-specific schema `$ref`. It defines no
reviewer identity or specialty system, review execution, retrieval, scoring,
severity, confidence, verdict, approval, synthesis, voting, decision, workflow,
runtime, access, disclosure, retention, release, deployment, or merge
mechanism.

The Accepted [ARCH-018 architecture decision](../docs/architecture/review-record-executable-schema.md),
[ADR-0018](../docs/architecture/adr/0018-review-record-executable-schema.md),
and [non-normative test manifest](../tests/schemas/review-record/1.0.0/cases.json)
define and evidence the Accepted boundary. Creation, validation, review, and
repository presence did not grant acceptance or activation. Exact-head
EIGENAAR / Final Authority acceptance is recorded in issue comment
`5218629573`, and governed integration to `main` activates Schema Version
`1.0.0`. Schema validity grants no contract conformance, specialist
authority, review quality, recommendation authority, final acceptance,
integration, release, deployment, merge permission, Decision Record schema
authority, or follow-on authority.

## Accepted Decision Record Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / Decision Record Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/decision-record/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/decision-record` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #64 and EIGENAAR acceptance comment `5219310944` |

The Accepted resource evaluates one complete closed Decision Record artifact with
mandatory `envelope` and `payload`. Its envelope statically references the exact
Accepted Common Artifact Envelope and constrains only the Decision Record
Artifact Type and governing Contract and Schema coordinates. Its closed
seventeen-property payload records one exact Decision Authority pin, an opaque
human decision-maker reference, the exact revision represented as approved,
attributable approval provenance, one bounded question and outcome, decision
basis, nine artifact-relationship categories, separated input, timing, scope,
consequences, seven downstream-action boundaries, change/conflict provenance,
roles, external records, security/privacy, restricted basis, lifecycle, and
historical traceability.

The resource contains no Project Charter, Workstream, Task Contract, Context
Packet, Execution Result, Evidence Bundle, Review Record, peer Decision Record,
State Snapshot, or other artifact-specific schema `$ref`. It allocates no
authority or identity, proves no approval, retrieves no source, makes or
executes no decision, resolves no conflict, changes no state, and implements no
acceptance, integration, release, deployment, publication, merge, workflow,
runtime, access, disclosure, retention, or verification mechanism.

The Accepted [ARCH-019 architecture decision](../docs/architecture/decision-record-executable-schema.md),
[ADR-0019](../docs/architecture/adr/0019-decision-record-executable-schema.md),
and [non-normative test manifest](../tests/schemas/decision-record/1.0.0/cases.json)
define and evidence the Accepted boundary. Governed integration to `main`
activates exactly Schema Version `1.0.0` under issue #64 and EIGENAAR acceptance
comment `5219310944`; acceptance and activation grant no State Snapshot schema
or follow-on authority.

## Accepted State Snapshot Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Logical schema identity | CNTX Public Core Schema Family / State Snapshot Artifact |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Dialect declaration | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/state-snapshot/1.0.0/schema.json` |
| Exact external dependency | Accepted Common Artifact Envelope Schema Version `1.0.0` |
| Governing Contract Definition | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/state-snapshot` at `1.0.0` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #66 and EIGENAAR acceptance comment `5219885650` |

The Accepted resource evaluates one complete closed State Snapshot artifact
with mandatory `envelope` and `payload`. Its envelope statically references the
exact Accepted Common Artifact Envelope and constrains only the State Snapshot
Artifact Type and governing Contract and Schema coordinates. Its closed
eighteen-property payload preserves authorized derivation and Derived/non-
authoritative classification, purpose and scope, controlling sources and exact
revisions or pinning limitations, provenance, six temporal coordinates, four
freshness classifications, relevance and material context, reported state and
separated claims, evidence/review/decision/integration traceability, nine
artifact-relationship categories, uncertainty, incomplete work and stops,
snapshot history, five peer relations, bounded handoff, security/privacy, and
non-automatic lifecycle effects.

The resource contains no Project Charter, Workstream, Task Contract, Context
Packet, Execution Result, Evidence Bundle, Review Record, Decision Record, peer
State Snapshot, or other artifact-specific schema `$ref`. It allocates no
authority or identity, proves no source or claim, retrieves no content,
calculates no freshness, resolves no conflict, changes or synchronizes no state,
and implements no workflow, runtime, access, disclosure, retention,
verification, release, deployment, publication, or merge mechanism.

The Accepted [ARCH-020 architecture decision](../docs/architecture/state-snapshot-executable-schema.md),
[ADR-0020](../docs/architecture/adr/0020-state-snapshot-executable-schema.md),
and [non-normative test manifest](../tests/schemas/state-snapshot/1.0.0/cases.json)
define and evidence the Accepted boundary. Governed integration to `main`
activates exactly Schema Version `1.0.0` under issue #66 and EIGENAAR acceptance
comment `5219885650`; acceptance and activation grant no artifact instance,
implementation, release, deployment, publication, or follow-on authority.

## Accepted Epistemic Provenance and Freshness Module Definition Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Governing Module Definition | `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness` at `1.0.0` |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/extension-modules/epistemic-provenance-freshness/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted and integrated under issue #145, Owner / Final Authority issue-contract acceptance comment `5267576754`, exact-head candidate-acceptance comment `5269689952`, integration comment `5271035681`, and completion comment `5271254252` |

The Accepted resource evaluates one closed Module declaration with explicit
source, claim, provenance, temporal, digest, policy, derivation, condition,
outcome, limitation, and non-automatic-authority structure. Its
[architecture decision](../docs/architecture/epistemic-provenance-freshness-extension-module-definition-schema-resource.md),
[ADR-0042](../docs/architecture/adr/0042-epistemic-provenance-freshness-extension-module-definition-schema-resource.md),
and [48-case manifest](../tests/schemas/extension-modules/epistemic-provenance-freshness/1.0.0/cases.json)
describe the exact Accepted boundary.

The preceding Proposed status allocated or activated nothing. Accepted status,
repository presence, `$id`, schema validity, case evaluation, Ready state,
review, or mergeability did not integrate or activate the resource. Separately
governed PR #146 integrated it at commit/tree
`9f482043f76c792f6c2e1e96eb4a535ee26b3a99` /
`7b2f45791e3b7bff7e856f26fff9b22598c06709`; issue #145 is closed/completed and
the task branch is absent locally and publicly. The original execution and
evidence remain bound only to candidate commit/tree
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875`. Integration created no new
execution/evidence instance, Definition, Profile, Core field, rule, Tool or
Implementation version, supported input set, automatic authority, release,
support, certification, hosting, or deployment.

## Accepted Context Packet Epistemic Provenance and Freshness Profile Definition Schema Version 1.0.0

| Dimension | Accepted value |
| --- | --- |
| Governing Profile Definition | `https://github.com/CNTX-PROJECT/CNTX/profile-definitions/context-packet-epistemic-provenance-freshness` at `1.0.0` |
| Definition Schema Identifier | `https://github.com/CNTX-PROJECT/CNTX/schemas/profiles/context-packet-epistemic-provenance-freshness` |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0/schema.json` |
| Separate reference inventory | Exactly `207 total / 207 internal / 0 external`, across 52 root `$defs` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #149, attributable issue-contract acceptance comment `5279967413`, source-preserving correction addenda `5280408320` and `5280832992`, and exact-head candidate-acceptance comment `5285702199`; governed integration pending |

The Accepted resource evaluates one external closed ARCH-043 Profile application
record with all fourteen required root members. It fixes the exact governing
Profile and two subject pins, Context Packet and Task Contract coordinates,
packet-local source associations, six source categories, seventeen capability
dimensions, eight conditions, four separate outcomes, eleven limitation
categories, attributable roles, finite structural limits, non-aggregation, and
the prohibition on a serialized `automaticAuthority` property.

The resource is standalone and uses only fragment-internal `$ref` values. It
does not embed or evaluate the external Context Packet, Task Contract, or
ARCH-040 Module declaration; external reference edges are exactly zero. The
[Accepted ARCH-044 decision](../docs/architecture/context-packet-epistemic-provenance-freshness-profile-definition-schema-resource.md),
[ADR-0044](../docs/architecture/adr/0044-context-packet-epistemic-provenance-freshness-profile-definition-schema-resource.md),
and [72-case operation-based manifest](../tests/schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0/cases.json)
describe the bounded Accepted boundary.

Correction addendum `5280408320` changes only the accepted baseline link pins
to `1489 Markdown / 27 HTML` and `1297 local / 219 external`. It leaves the
baseline commit/tree, schema meaning, exact `207/207/0` candidate reference
inventory, cases, Proposed status, and every lifecycle boundary unchanged.

Second correction addendum `5280832992` changes only the evaluation-
responsibility count from sixteen to seventeen while preserving the exact
seventeen Accepted ARCH-043 members. It changes no schema assertion, case,
identity, version, resource graph, validation requirement, or lifecycle
boundary.

Attributable exact-head candidate-acceptance comment `5285702199` is bound to
candidate commit/tree `7420e5d179ab965bfda58780df4f41a08a0b62de` /
`56d1808cb95f3dd5a0b5d84f2a8e440891dff5e6`. The preceding Proposed status
allocated or activated nothing. Standard JSON Schema cannot prove packet-
external equality, complete selected-source association, projected-key
uniqueness, opaque-reference resolution,
graph completeness or acyclicity, narrowing-only meaning, source truth,
freshness, policy applicability, conformance, access, approval, or authority.
Accepted status, status promotion, path or `$id` presence, parseability, meta-
schema validity, case materialization, validation, Ready state, review, or
mergeability does not integrate, allocate, or activate the Schema Identifier /
Version and grants no Profile instance, Tool support, new execution/evidence,
release, deployment, or final-human authority. The successful local candidate
validation remains bound only to the accepted candidate commit/tree above; this
status-only promotion is not a new execution or evidence instance.

## Change boundary

Upon governed integration, exact Accepted versioned canonical standalone content is immutable. Any accepted structural or semantic change requires the applicable identity/version assessment, attributable review and approval, traceable provenance, and a separately authorized change. Schema validity alone cannot approve such a change. The Accepted Project Charter resource does not change the independently Accepted Common Artifact Envelope resource.

</details>
