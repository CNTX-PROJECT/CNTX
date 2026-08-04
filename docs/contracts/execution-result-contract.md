# CNTX Execution Result Artifact Contract

## Status and authority

**Status: Proposed.** This contract is submitted under [GOVERNANCE.md](../../GOVERNANCE.md) and is not binding before final human acceptance and publication on `main`. Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** strong recommendations, and **MAY** permission; these terms express requirement strength only within this proposed contract.

ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-004 remain higher Accepted authority sources. This contract specializes, without redefining, the accepted Execution Result primary definition and Evidentiary classification. Executable schemas, validators, templates, runtimes, and implementations remain subordinate future work.

## Purpose and scope

This contract governs the Evidentiary Execution Result artifact: it records the bounded task's claimed output and limitations under one exact applicable approved Task Contract revision and relevant Context Packet revision or revisions where used. It preserves material provenance, revision context, assumptions, uncertainty, deviations, stops, escalations, and unperformed work without granting authority. Concrete result fields, payloads, templates, schemas, and encodings remain future work.

It does not redefine Execution Result; create an instance; amend Project Charter, Workstream, Task Contract, or Context Packet; approve correctness, completion, acceptance, integration, release, deployment, or merge; select validation, schema, serialization, storage, transport, workflow, orchestration, runtime, API, CLI, or private implementation behavior.

## Accepted governing meaning and classification

This contract references, without competing with, the accepted primary definition:

> Execution Result — Records the bounded task's claimed output and limitations.

Execution Result is an **Evidentiary** canonical artifact. A Bounded Implementer conceptually authors it under the exact approved Task Contract revision. It is not self-approved. Existence, possession, receipt, technical access, schema validity, generated status, test result, digest, storage, or implementer capability grants no authority or approval.

An Execution Result MUST NOT modify, broaden, replace, or reinterpret its governing Task Contract; replace authoritative Project Charter, Workstream, Task Contract, or Context Packet sources; constitute final approval, acceptance, integration authority, release authority, deployment authority, or merge authority; or silently transfer claims, context, or authority between different Task Contracts.

## Governing Task Contract and Context Packet boundary

An exact approved Task Contract revision MUST exist before a conforming Execution Result is authored. Its objective, scope, authority, permitted resources, forbidden zones, constraints, acceptance criteria, expected evidence, security/privacy requirements, stop conditions, and integration boundaries remain controlling. A result cannot fill missing Task Contract authority or retroactively authorize out-of-scope work.

Context Packet remains Derived and may supply the minimum task-relevant source material used for permitted execution. Packet content is not permission, contextual relevance is not authorization, and an Execution Result cannot treat a packet as authority. Relevant Context Packet identity, revision, limitations, missing context, and provenance MUST remain traceable where material.

## Claims, limitations, and evidence

An Execution Result MUST semantically identify the governing Task Contract identity and exact revision; the claimed output; material actions and side effects where applicable; relevant accessed or changed resources; provenance and revision context; validation or check claims; assumptions; limitations; uncertainty; failures; deviations; stops; escalations; and work deliberately not performed where material. These are semantic responsibilities, not concrete fields.

Completion, acceptance-criteria satisfaction, tests, validation, review, schema validity, or a conformance claim are evidence for an applicable authorized decision, not that decision. A result claim does not itself establish correctness, completion, acceptance, integration, release, deployment, or merge.

Evidence Bundle may support claims about the result, provenance, checks, assumptions, and limitations but grants no authority. Review Record may assess result and evidence within declared specialty but cannot approve the result or execution. Decision Record records a consequential decision when governance requires it; Execution Result, Evidence Bundle, Review Record, Decision Record, and final human approval remain distinct.

## Source, provenance, and conflict handling

Each material claim or source reference MUST retain enough provenance to identify the applicable source type, identity or revision, whether content is direct, summarized, extracted, transformed, or unavailable, and resulting uncertainty or limitation. Consequential references MUST be resolvable and revision-aware where pinning is required. A digest may strengthen evidence but grants neither authority nor approval.

Material conflict, missing required context, uncertain provenance, security/privacy risk, or an apparent authority conflict MUST be reported and requires stop or escalation. It MUST NOT be silently omitted, summarized away, or represented as resolved. Automatic conflict resolution remains deferred.

## Permitted and forbidden content

An Execution Result MAY contain bounded claims about authorized task output, limitations, relevant actions and side effects, validation, assumptions, uncertainty, failures, deviations, stops, escalations, unperformed work, and provenance-preserving references to applicable Task Contract, Context Packet, evidence, review, or decision sources.

It MUST NOT become a Project Charter, Workstream, Task Contract, Context Packet, unrestricted context dump, unrelated result collection, approval, acceptance decision, integration decision, release or deployment authorization, merge permission, Evidence Bundle, Review Record, Decision Record, State Snapshot, executable schema, validator, template, prompt, workflow, runtime configuration, API contract, CLI contract, or private implementation repository.

## Roles, authority, and accountability

Owner / Final Authority remains human or explicitly human-governed. The Bounded Implementer authors a result within the governing Task Contract but MUST NOT broaden scope, authority, or claims autonomously. The Lead Architect may define or review applicable task boundaries but does not become the result's final approver merely by doing so. Specialist Review is evidentiary. Final acceptance, integration, release, deployment, and merge remain separate human authority decisions. Self-approval and cyclic authority are prohibited.

## Required relationships and traceability

The accepted dependency direction remains:

`Project Charter → Workstream → Task Contract → Context Packet / Execution Result`

| Related artifact | Required relationship and authority limit |
| --- | --- |
| Project Charter | Supplies governing enduring intent and boundaries through the Task Contract. It cannot be replaced or amended by a result. |
| Workstream | Supplies applicable bounded work context through the Task Contract. A result cannot mutate Workstream scope or state. |
| Task Contract | Exact approved revision governs execution claims, scope, authority, and expected evidence. A result cannot approve, amend, or replace it. |
| Context Packet | May identify the minimal Derived context used for execution. It grants no authority or permission. |
| Peer Execution Result | May be an explicit dependency or comparison source only. Peers share no implicit scope, authority, approval, or context. |
| Evidence Bundle | May support result claims and limitations. It cannot grant authority or final approval. |
| Review Record | May evaluate identified result claims and evidence. It remains evidentiary and cannot approve execution or integration. |
| Decision Record | May record a required consequential decision. It remains separate from the result and retains applicable human authority. |
| State Snapshot | May derive orientation from integrated authoritative state. It cannot replace a result or become an authority source. |

Derived and Evidentiary artifacts do not replace authoritative artifacts. Relationship cardinalities, encoding, embedding, caching, dereferencing, and packaging remain deferred.

## Lifecycle and change control

The conceptual lifecycle includes result authoring; bounded evidence and review availability; assessment against applicable acceptance criteria; correction, supersession, withdrawal, retention, and traceability. It does not select concrete state names, transitions, timestamps, automation, or closure mechanics.

Result lifecycle remains distinct from Document Status, Task Contract lifecycle, approval state, Contract Definition Version, Schema Version, Implementation Version, review status, decision status, and State Snapshot freshness. Completion or closure of a task or result does not automatically approve, accept, integrate, release, deploy, or merge it. Material claim, source, Task Contract, side-effect, privacy, security, or uncertainty change requires reassessment and a new revision when traceability requires it.

## Identity, revision, versioning, and provenance

ARCH-002 applies without redefinition. Execution Result Artifact Instance Identifier, Execution Result Artifact Revision, governing Contract Definition Identifier and Version, governing Task Contract identity and exact revision, Context Packet references where used, future Schema Identifier and Version, Document Status, result lifecycle, approval state, Implementation Version, Content Digest, and Provenance Reference remain distinct. Identifiers, revisions, digests, schema validity, and storage state grant neither authority nor approval. Concrete syntax, sequencing, timestamps, and canonicalization remain deferred.

## Evidence, review, approval, and conformance

Evidence may support claims about output, actions, side effects, provenance, checks, assumptions, limitations, uncertainty, failures, deviations, stops, escalations, and unperformed work. Schema-valid does not necessarily mean contract-conformant; contract-conformant does not mean correct, complete, accepted, integrated, released, deployed, or merged. Validation, review, and conformance claims grant no task authority or final approval.

## Public/private, security, and confidentiality boundaries

Public results, examples, tests, and documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, hostnames, restricted source material, private project content, or private domain-specific implementation. Restricted sources SHOULD be safely referenced rather than copied. Access to restricted content is not authority to disclose it. Security/privacy uncertainty requires stop and escalation. Private project, deployment, infrastructure, production, and domain-specific implementation context are forbidden.

## Extensions and profiles

Extensions and profiles MUST use explicit stable identity or namespace, identify governing CONTRACT-005/version, remain additive and non-overriding, and not weaken scope, provenance, privacy, context isolation, or final human authority. They MUST NOT require a provider, model, runtime, retrieval product, storage, transport, schema language, serialization, or domain, or elevate optional private implementation semantics to universal core.

## Deferred schema and implementation decisions

This contract defers concrete fields, requiredness, names, nesting, schema language, serialization, payload formats, templates, examples, prompts, identity and revision syntax, timestamps, state names, transition rules, approval representation, digest/signing/encryption/canonicalization, provenance encoding, validators, conformance fixtures, tests, dashboards, APIs, CLIs, storage, transport, scheduling, routing, workflow, orchestration, runtime behavior, automatic conflict resolution, and provider or implementation selection. No technology or provider is selected.
