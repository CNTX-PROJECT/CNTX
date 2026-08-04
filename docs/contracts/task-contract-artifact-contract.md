# CNTX Task Contract Artifact Contract

## Status and authority

**Status: Accepted.** Final human approval by the Owner / Final Authority has been granted, and this contract is accepted under [GOVERNANCE.md](../../GOVERNANCE.md). On merge and publication to `main`, it becomes the binding, subordinate artifact-specific contract basis for the canonical Task Contract. Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** strong recommendations, and **MAY** permission; these terms express requirement strength only within this contract.

This contract is subordinate to accepted ARCH-001, ARCH-002, ARCH-003, CONTRACT-001, and CONTRACT-002. It specializes, without redefining, the accepted canonical Task Contract meaning, authoritative classification, authority and lifecycle models, identity/versioning and provenance semantics, privacy boundaries, governing Project Charter and Workstream contracts, or final human authority. Executable schemas, validators, permission engines, and implementations remain subordinate future work.

## Purpose and scope

This artifact-specific contract governs the authoritative task-level authorization boundary for exactly one bounded task under applicable approved Project Charter and Workstream context. It applies to future conforming Task Contract contracts, schemas, instances, extensions, profiles, validators, Conformance Claims, and implementations.

It does not create a Task Contract instance; amend or replace a Project Charter or Workstream; define concrete fields, names, requiredness, syntax, ordering, timestamps, statuses, or cardinalities; select schema or serialization technology; or introduce a permission language, access-control system, policy or execution engine, routing, orchestration, workflow, approval service, template, payload, prompt, script, validator, registry, migration, runtime, API, CLI, adapter, code generator, or private implementation content. It does not define any other artifact-specific contract or grant autonomous approval, implicit authority, unbounded delegation, or unrestricted execution.

## Accepted governing meaning and classification

This contract references and specializes, but does not replace or compete with, the accepted primary definition:

> Task Contract — Authorizes one bounded task, including scope, authority, and expected evidence.

Task Contract is an **authoritative** canonical artifact, bounded by applicable approved Project Charter and Workstream context. The Lead Architect conceptually authors it. The Owner / Final Authority, or a validly delegated authority under governing policy, approves the exact Task Contract Artifact Revision. Only that explicitly approved revision grants task-level authority for consequential use.

Creation, existence, authorship, assignment, participation, schema validity, automation, credentials, access, tools, implementation state, or executor capability MUST NOT grant authority. A Task Contract MUST NOT alter, broaden, override, replace, or silently reinterpret its governing Project Charter or Workstream; approve itself or its own revision; infer authority from silence; or create cyclic authority. Authority for one task or revision MUST NOT be inferred for another.

One Task Contract governs one coherent bounded task. It MUST NOT aggregate unrelated or independently approvable work for convenience. Coherent internal steps MAY exist only as subordinate parts of that one approved boundary. Exact task granularity and decomposition methods remain deferred.

## Bounded authorization and least-privilege boundary

A conforming Task Contract MUST establish the minimum explicit authority required for its task, conceptually addressing the task objective and intended outcome; included scope, non-goals, exclusions, and forbidden zones; permitted and forbidden actions, resources, paths, systems, side effects, and external interactions as applicable; the bounded executor or executor class; authority source and approval/delegation limits; execution preconditions; validity, revocation, supersession, expiration, and reassessment; and stop and escalation conditions.

Authority MUST be explicit, bounded, revocable, traceable, and least-privileged. Privileges remain limited to what the task needs. Possession of credentials, tools, repository rights, network access, or technical capability is not authorization; contextual relevance is not permission; and absence of an explicit prohibition is not permission where authority is required. An executor MUST NOT broaden scope or authority from convenience, inferred intent, previous access, or implementation necessity.

Conflict with higher authority, material ambiguity, missing context, unauthorized access, material dependency change, or security/privacy risk requires stop and escalation, not silent expansion. Permission vocabularies, access-control semantics, risk classes, and enforcement mechanisms remain deferred.

## Conceptual responsibilities

A conforming Task Contract MUST semantically address, without presenting concrete schema fields, prompts, commands, role bindings, state codes, or workflow steps:

- governing Project Charter and Workstream identities with applicable revision/version context;
- one bounded objective, intended outcome, expected deliverables, and result boundary;
- included scope, non-goals, exclusions, allowed and forbidden resources;
- authority source, approver, bounded delegation, and executor responsibility;
- dependencies, interfaces, assumptions, constraints, risks, uncertainty, and escalation;
- minimum Context Packet expectations and source-selection constraints;
- security, privacy, confidentiality, public/private, and least-privilege constraints;
- expected evidence, validation obligations, acceptance criteria, known limitations, and specialist-review boundaries;
- human-decision, integration, release, deployment, and merge boundaries; and
- amendment, revocation, expiration, completion, closure, supersession, and retention expectations.

## Approval, execution, completion, acceptance, and integration

Approval of the exact Task Contract revision authorizes only bounded execution within that revision. It does not approve an Execution Result, evidence, correctness, completion, review, integration, release, deployment, or merge. An Execution Result is an evidentiary claim by the Bounded Implementer and is not self-approved; Evidence Bundle and Review Record remain evidentiary. Meeting acceptance criteria is evidence for an authorized decision, not that decision.

Completion or closure MUST NOT approve a result or authorize integration. Integration, release, deployment, and merge require separate authority and the applicable human decision. Architecture, security/privacy, release, and merge decisions retain final human authority. A Task Contract cannot delegate away final human authority. Later approval MUST NOT retroactively authorize previously unauthorized work, even if it is useful or technically correct.

## Permitted and forbidden content

A Task Contract MAY contain bounded task-level authorization context and task-specific procedural or sequencing constraints only when necessary for safety, authority, validation, or acceptance. It MUST NOT silently become a Project Charter or Workstream amendment; unrelated task collection or unbounded backlog; Context Packet or unrestricted context dump; Execution Result, Evidence Bundle, Review Record, Decision Record, or State Snapshot; evidence that execution occurred or succeeded; final approval of its own output; general prompt library, unrestricted implementation plan, reusable execution script, autonomous loop, workflow engine, routing policy, orchestration definition, runtime configuration, or access-control implementation.

It MUST NOT become an executable schema, serialization binding, API or CLI contract, policy-engine configuration, project-management product, hidden global project brain, container for unrelated context, or repository for secrets, credentials, personal data, production configuration, private source material, private project data, or private domain-specific implementation logic. This public contract remains model-, provider-, runtime-, transport-, storage-, serialization-, schema-language-, permission-system-, product-, and domain-independent.

## Roles, authority, and accountability

Authorship, approval, execution, context selection, evidence assembly, specialist review, consequential decision, integration, and final authority remain distinguishable responsibilities. Owner / Final Authority remains human or explicitly human-governed. The Lead Architect prepares a proposed Task Contract within delegated scope; Owner / Final Authority or validly delegated authority approves its exact revision.

Delegation MUST be explicit, bounded, revocable, traceable, subordinate to its source, and limited to the declared task and revision. It MUST NOT exceed its source or arise from title, access, participation, prior approval, or tools. The Bounded Implementer acts only within an approved Task Contract and supplied Context Packet; it MUST NOT self-authorize, broaden scope, approve consequential changes, or treat successful execution as approval. Specialist Review and Conformance Claims remain evidentiary. Participation grants no integration, release, deployment, or merge authority. Consequential self-approval and cyclic authority are prohibited. No canonical Task Owner, Task Manager, Task Lead, or Approver Agent role is introduced.

## Required relationships and traceability

The dependency direction is:

`Project Charter → Workstream → Task Contract → Context Packet / Execution Result`

Every Task Contract traces to governing Project Charter and Workstream identity and revision/version context; scope, authority, constraints, and expected evidence remain conformant to both. Consequential references MUST be resolvable and revision- or version-aware where pinning is required. Embedded copies remain derived and cannot replace authoritative sources.

| Related artifact | Relationship purpose | Authority limitation |
| --- | --- | --- |
| Project Charter | Governs enduring intent and boundaries. | Task Contract cannot amend, override, or broaden it. |
| Workstream | Supplies applicable bounded work context. | Task Contract cannot amend, override, or broaden it. |
| Peer Task Contract | May identify an explicit dependency or interface. | Peers retain independent scope, approval, context, evidence, lifecycle, completion, and authority; none is shared, inherited, merged, or transferred. |
| Context Packet | Supplies minimal derived task-relevant context. | It preserves provenance and cannot grant or broaden authority. |
| Execution Result | Records an execution claim under the task boundary. | It cannot approve, amend, or replace the Task Contract. |
| Evidence Bundle | Supports identified execution or review claims. | It cannot grant, broaden, or retroactively create authority. |
| Review Record | Evaluates identified evidence and results. | It cannot authorize execution, amend scope, or become final approval. |
| Decision Record | Records a consequential decision referencing governing sources. | It does not enable self-approval; required human authority remains controlling. |
| State Snapshot | May derive orientation state with provenance. | It cannot become the Task Contract or an authority source. |

Exact cardinalities, optionality, relationship encoding, embedding, dereferencing, storage, caching, retention, and offline packaging remain deferred.

## Context selection and execution boundaries

An approved Task Contract revision MUST exist before authoritative Context Packet selection or bounded execution. The packet is prepared under that exact revision, contains only minimum justified task-relevant context, preserves source provenance and revision/version pinning, and excludes unrelated Workstream, task, private, and historical context by default. It grants no authority and cannot broaden the Task Contract.

Conflicts favor applicable higher authority; missing context, unresolved conflict, material uncertainty, or security/privacy concern prevents silent execution or expansion. The Bounded Implementer uses only explicitly authorized actions and resources. Each execution claim traces to its Task Contract revision and Context Packet. Unrelated or independently approvable work requires separate Task Contracts. Context-selection algorithms, routing, token budgets, prompt assembly, scheduling, retries, concurrency, and orchestration remain deferred.

## Lifecycle and change control

The conceptual lifecycle includes proposal or authoring, bounded review, approval of the exact revision, availability for context selection and bounded execution, evidence assembly and specialist review, completion or acceptance assessment, and closure, revocation, expiration, supersession, or retirement. It does not select states, transitions, timestamps, or automation.

Only approved revisions authorize consequential execution; proposed, expired, revoked, or superseded revisions are not current authority. Materially different work needs a new instance or approved revision. Consequential changes to objective, scope, resources, executor authority, delegation, dependencies, context, deliverables, evidence, acceptance, security/privacy, stop conditions, validity, or integration boundaries require new revision, review, and applicable approval before further execution. Clarification MUST NOT hide scope or authority expansion, and material Project Charter or Workstream change requires reassessment.

Amendment does not retroactively authorize out-of-scope work. Action completion, Execution Result, validation, or acceptance-criteria satisfaction does not automatically approve, close, or integrate the task. Revocation, expiration, closure, and supersession end future authority while preserving provenance and history. Task lifecycle remains distinct from Document Status, approval state, contract/schema/implementation version, Workstream state, executor activity, result status, review status, decision status, and State Snapshot freshness.

## Identity, versioning, and provenance

ARCH-002 applies without redefinition. Artifact Instance Identifier, Artifact Revision, Contract Definition Identifier, Contract Definition Version, governing Project Charter reference, governing Workstream reference, Schema Identifier, Schema Version, Document Status, approval state, Implementation Version, Workstream declared state, executor activity, Execution Result status, Review Record status, Decision Record status, Content Digest, Provenance Reference, and State Snapshot freshness remain distinct.

Approval applies to the exact Artifact Revision. A task lineage MUST NOT silently be reused for materially different work. An identifier, digest, schema-valid result, credential, assignment, dashboard, or implementation state grants neither authority, approval, completion, nor transition. Syntax and encoding for identity, lineage, revision, approval, and provenance remain deferred.

## Evidence, review, approval, and conformance

Consequential approval MUST be supported by evidence identifying the exact Task Contract revision; governing Charter and Workstream context; governing contract/version context; objective, scope, authority, permitted and forbidden resources, dependencies, deliverables, expected evidence, acceptance criteria, risks, stop conditions, authority source and delegation limits, approver, review findings, assumptions, limitations, dissent, uncertainty, peer and downstream impacts, integration/release/deployment/merge boundaries, and authorized approval decision.

Expected execution evidence addresses, where applicable, accessed or changed resources, actions and material side effects, provenance, tests and validation, assumptions, limitations, failures, unresolved questions, security/privacy/confidentiality/least-privilege checks, deviations, stops, escalations, and unperformed work. Approval evidence and execution evidence remain separate, as do Execution Result, Evidence Bundle, Review Record, Conformance Claim, and Decision Record. Schema-valid does not imply contract-conformant; contract-conformant does not imply approved, executed, complete, correct, accepted, integrated, released, deployed, or merged. Validators, reviewers, authors, executors, code, credentials, tools, and implementations have no final authority merely by producing evidence.

## Public/private and security boundaries

Public contracts, examples, tests, schemas, evidence, and documentation MUST NOT disclose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. Task authority does not authorize disclosure, copying, retention, publishing, or transmission of restricted information. Context minimization and least privilege remain mandatory; secrets and credentials are referenced only through approved secure mechanisms, never embedded in public artifacts. Security or privacy uncertainty requires stop and escalation. Public examples MUST NOT use realistic private identifiers, hostnames, paths, or project context.

## Extensions and profiles

Extensions and profiles MUST use explicit stable identities or namespaces, identify this governing Task Contract artifact contract/version, and remain additive and non-overriding. They MUST NOT override final human authority, Task Contract meaning or classification, Project Charter or Workstream, provenance, privacy, lifecycle, least privilege, or context isolation; silently broaden scope, authority, permissions, side effects, evidence, or acceptance criteria; merge unrelated Task Contracts; or transfer authority. They MUST NOT require a provider, model, runtime, storage, transport, schema language, serialization, permission engine, workflow engine, product, or domain.

## Deferred schema decisions

This contract deliberately defers concrete fields, requiredness, names, nesting, schema language, serialization, identity/lineage/revision/approval syntax, actor and delegation representation, permission vocabulary, action/resource taxonomy, path and wildcard semantics, allow/deny precedence, side-effect categories, enforcement, state names, timestamps, validity/revocation/concurrency rules, risk and trust classes, review independence, expression languages, relationship cardinalities, dependency encoding, embedding/dereferencing/caching/retention, unknown fields, profiles, templates, examples, prompts, dashboards, validators, conformance fixtures, migrations, packaging, code generation, APIs, storage, transport, routing, scheduling, orchestration, execution, integration, release, deployment, and merge behavior.
