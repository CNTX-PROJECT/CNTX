# CNTX Workstream Artifact Contract

## Status and authority

**Status: Proposed.** This contract is submitted under [GOVERNANCE.md](../../GOVERNANCE.md). It is not binding until final human approval and merge. Accepted ARCH-001, ARCH-002, ARCH-003, and CONTRACT-001 remain higher-authority sources. This proposed contract specializes them and MUST NOT modify, replace, broaden, or silently reinterpret the governing Project Charter contract. Future executable schemas, validators, and implementations remain subordinate work.

Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms express requirement strength only within this proposed document.

## Purpose and scope

This contract governs the authoritative project-level coordination boundary that groups related bounded work and its declared state under one applicable approved Project Charter context. It applies to future conforming Workstream contracts, schemas, instances, extensions, profiles, validators, Conformance Claims, and implementations.

It does not redefine the canonical Workstream, amend a Project Charter, create a Workstream instance, select concrete fields, field names, requiredness, syntax, ordering, timestamps, state names, cardinalities, schema language, or serialization. It creates no template, form, payload example, validator, registry, migration, runtime, API, CLI, adapter, project-management product, workflow engine, or other artifact-specific contract. It grants neither task-level execution authority nor autonomous approval, implicit delegation, unbounded authority, or permission to include private implementation content.

## Accepted governing meaning and classification

This contract refers to and specializes, without replacing or competing with, the accepted primary definition:

> Workstream — Groups related bounded work and its declared state.

Workstream is an **authoritative** canonical artifact. A Workstream MUST be governed by the applicable approved Project Charter intent, scope, boundaries, principles, constraints, governance context, and final authority. The Lead Architect MAY conceptually establish and maintain a proposed Workstream within delegated scope; consequential Workstream scope requires approval from the applicable Owner / Final Authority under governing policy.

Only an explicitly approved Workstream Artifact Revision is authoritative for consequential use. Establishment, existence, authorship, participation, schema validity, automation, dashboard status, or implementation status does not itself grant authority. A Workstream MUST NOT alter, broaden, override, replace, or silently reinterpret its governing Project Charter; approve itself or its own revision; or create cyclic authority. Its authority governs bounded coordination context and declared Workstream state, not individual task execution. Task-level authority arises only through an approved Task Contract.

## Conceptual responsibilities

A conforming Workstream MUST address these semantic responsibilities without presenting them as concrete schema fields, task lists, status codes, or implementation workflows:

- a resolvable governing Project Charter identity and applicable revision/version context;
- bounded Workstream purpose, contribution to approved project intent or outcomes, included scope, enduring boundaries, non-goals, exclusions, and grouping rationale;
- material dependencies and interfaces with the Project Charter, peer Workstreams, and downstream Task Contracts;
- governing principles, material constraints, assumptions, risks, unresolved uncertainty, and escalation conditions;
- governance context, approval authority, bounded delegation, and Workstream-level context isolation;
- expectations and constraints for decomposition into candidate Task Contracts;
- the conceptual declared state needed to govern current disposition without state names or encoding;
- consequential decision, evidence, review, provenance, and change-control expectations; and
- conditions for review, amendment, completion, closure, supersession, or retirement.

## Declared state boundary

**Declared state** is the authoritative Workstream-level statement of its current governed disposition and material coordination condition within the applicable approved revision context. It MUST remain subordinate to the governing Project Charter and applicable approved decisions, and MUST NOT silently amend scope, authority, constraints, or completion criteria.

Declared state MUST be distinguishable from Document Status, approval state, Contract Definition Version, Schema Version, Implementation Version, Workstream Artifact Revision, individual Task Contract lifecycle, task progress, raw telemetry, dashboard status, derived State Snapshot, and snapshot freshness. Dashboards, summaries, status reports, and State Snapshots MAY report derived state only when they preserve provenance; they MUST NOT become the authoritative Workstream. Volatile observations or implementation telemetry MUST NOT automatically become authoritative state. State names, transitions, timestamps, encodings, and automation remain deferred.

## Permitted and forbidden content

A Workstream MAY contain enduring, materially current Workstream-level context needed to coordinate related bounded work under its governing Project Charter. It MUST NOT silently become a Project Charter or Charter amendment; Task Contract or task-execution authorization; Context Packet or unrestricted context dump; detailed task-by-task implementation plan, procedure, prompt collection, or execution script; activity log, raw telemetry feed, or ungoverned project-status report; Execution Result, Evidence Bundle, Review Record, Decision Record, State Snapshot, or dashboard export; executable configuration, workflow definition, schema, API contract, runtime instruction set, or product-backlog implementation; hidden global project brain; container for unrelated context; or repository for secrets, credentials, personal data, production configuration, restricted source material, private project data, or private domain-specific implementation logic.

It MAY identify conceptual sequencing, dependencies, interfaces, and completion conditions when necessary to govern bounded work, but MUST NOT replace the explicit scope, authority, deliverables, or evidence expectations of individual Task Contracts. Implementation detail SHOULD be excluded unless genuinely necessary, enduring, and explicitly authorized. This public contract remains model-, provider-, runtime-, transport-, storage-, serialization-, schema-language-, project-management-product-, and domain-independent.

## Roles, authority, and accountability

Owner / Final Authority MUST remain human or explicitly human-governed. Authorship, coordination, consultation, specialist review, consequential approval, and final authority are distinct responsibilities. The Lead Architect MAY establish and maintain a proposed Workstream within delegated scope. Operational coordination creates no new canonical role: this contract introduces no canonical “Workstream Lead.”

Delegation MUST be bounded, explicit, revocable, and subordinate to higher governance and the governing Project Charter. Specialist review and Conformance Claims are evidentiary, not final authority. Approval MUST identify the exact Workstream Artifact Revision. Participation grants no automatic authority to create, approve, execute, review, integrate, or merge a Task Contract or result. Consequential self-approval and cyclic authority are prohibited. Authority for one Workstream MUST NOT be inferred for another Workstream or for the Project Charter.

## Required relationships and traceability

Workstream is the authoritative coordination boundary between its governing Project Charter and applicable downstream Task Contracts. The accepted direction is **Project Charter → Workstream → Task Contract**. Every Workstream MUST trace to governing Project Charter identity and applicable revision/version context; its purpose, scope, boundaries, constraints, and declared state MUST conform to that source. Consequential references MUST be resolvable and revision- or version-aware where pinning is required; embedded or copied content MUST remain derived and preserve provenance.

| Related artifact | Relationship purpose | Authority limitation |
| --- | --- | --- |
| Project Charter | Governs Workstream intent, scope, boundaries, constraints, and authority context. | Workstream cannot alter or replace it. |
| Peer Workstream | Declares explicit interfaces or dependencies. | It cannot silently merge scope, authority, context, state, or approval. |
| Task Contract | Receives governing Workstream context and records its own explicit task authority. | Workstream context alone cannot authorize execution. |
| Context Packet | May carry a justified, minimal, derived, provenance-preserving selection. | It cannot replace authoritative sources or receive complete context by default. |
| Execution Result | May identify the Workstream through its governing Task Contract. | It cannot mutate scope, authority, declared state, or completion. |
| Evidence Bundle | May support Workstream-related claims. | It cannot approve, mutate, or replace the Workstream. |
| Review Record | May evaluate claims or evidence within declared specialty. | It is evidentiary and cannot approve, mutate, or replace the Workstream. |
| Decision Record | Records consequential interpretation, change, completion, supersession, retirement, or material dependency. | It must reference both Workstream and governing Project Charter; it does not enable self-approval. |
| State Snapshot | May derive orientation state. | It preserves provenance and cannot become authoritative. |

Exact cardinalities, optionality, relationship encoding, embedding, dereferencing, storage, caching, retention, and offline packaging remain deferred.

## Context isolation and decomposition boundaries

A Workstream MUST contain only bounded context needed to coordinate its related work; unrelated Workstream detail is excluded by default. Cross-Workstream inclusion requires explicit relevance and provenance. Decomposition produces candidate Task Contracts, not implicit task authority. Each Task Contract remains independently bounded, reviewable, approvable, and traceable.

A Workstream MUST NOT force its complete context into every Context Packet. Executors receive only a minimum justified task-relevant selection. Compact summaries MUST NOT replace authoritative sources. Relevant assumptions, dependencies, uncertainty, and unresolved questions remain explicit. Context-selection algorithms, routing, token budgets, prompt formats, and orchestration behavior are deferred.

## Lifecycle and change control

The conceptual lifecycle includes proposal or establishment; bounded review; approval of consequential scope; authoritative use for decomposition and coordination; declared-state review or change; amendment or clarification; completion or closure assessment; and supersession or retirement. It does not select concrete state names, a state machine, transition syntax, timestamps, or automation triggers.

Only explicitly approved Workstream revisions are authoritative for consequential use; proposed or reviewed content MUST NOT be represented as approved. Task Contract creation, execution, review, or completion MUST NOT automatically approve or amend a Workstream. Completion of all known tasks MUST NOT automatically complete it: approved completion conditions must be satisfied and the required decision recorded. Completion or closure MUST NOT retroactively approve Task Contracts, Execution Results, Evidence Bundles, Review Records, integrations, or other downstream artifacts.

Consequential changes to purpose, scope, boundaries, non-goals, governance, authority, context isolation, privacy or security, constraints, dependencies, completion criteria, or declared state require explicit review, an applicable Decision Record, and final human approval. Clarification MUST NOT conceal semantic change, and volatile reporting MUST NOT silently mutate authoritative state. Completed, closed, superseded, and retired revisions retain provenance and traceability. Workstream lifecycle remains distinct from Document Status, approval state, contract and schema versions, Implementation Version, Task Contract lifecycle, and State Snapshot freshness.

## Identity, revision, versioning, and provenance

ARCH-002 applies without redefinition. A conforming Workstream supports, as applicable, stable Artifact Instance Identifier, Artifact Revision, Contract Definition Identifier, Contract Definition Version, governing Project Charter identity and revision/version reference, Schema Identifier and Schema Version only if a future executable schema exists, Document Status, approval state, Implementation Version, Content Digest, Provenance Reference, and declared extensions or profiles.

Artifact Revision is not Contract Definition Version; approval state is not Document Status; Schema Version is not Workstream revision; Implementation Version is not Workstream authority or declared state; State Snapshot freshness is not Workstream revision; and task lifecycle is not Workstream lifecycle. An identifier, digest, schema-valid result, generated object, dashboard, or implementation state does not itself grant authority, approval, or a state transition. Identifier and revision syntax, sequencing, digest algorithm, canonicalization, timestamps, signatures, registries, concurrency, and conflict handling remain deferred.

## Evidence, review, approval, and conformance

Consequential approval or amendment MUST be supported by evidence identifying the exact Workstream revision; governing Project Charter identity and revision/version context; governing contract/version context; reviewed purpose, scope, boundaries, constraints, dependencies, declared state, and completion conditions; review scope and findings; assumptions, limitations, dissent, risks, and unresolved uncertainty; impacts on existing or candidate Task Contracts and peer Workstreams; and the final authorized human decision.

Review findings and Conformance Claims are evidentiary. Schema-valid does not necessarily mean contract-conformant; contract-conformant does not itself mean approved or authoritative. Approval does not erase uncertainty, dissent, risk, or dependency constraints. Validators, reviewers, authors, coordinators, generated code, dashboards, and implementations acquire no final authority merely by producing evidence or representations. Evidence formats, signatures, conformance fixtures, and validation tooling remain deferred.

## Public/private and security boundaries

Public contracts, examples, tests, schemas, conformance evidence, and documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. A public Workstream contract MUST NOT make private information mandatory. Restricted authoritative sources SHOULD be referenced rather than copied when traceability can be preserved safely. Context isolation MUST NOT be weakened merely to make a Workstream or downstream artifact self-contained.

## Extension and profile boundaries

Workstream extensions and profiles MUST use explicit stable identities or namespaces, identify the governing Workstream contract/version, and remain additive and non-overriding. They MUST NOT override final human authority, accepted Workstream meaning or classification, Project Charter governance, provenance, privacy or security, lifecycle, context isolation, or mandatory requirements; convert optional semantics into universal public-core requirements; merge unrelated Workstreams; or require a provider, model, runtime, storage system, transport, schema language, serialization, project-management product, or domain. Namespace syntax, conflict handling, discovery, negotiation, registry governance, and profile interoperability remain deferred.

## Deferred schema decisions

This contract defers, without deciding:

- concrete fields, requiredness, field names, nesting, schema language, and serialization;
- state names, encoding, transitions, automation, task grouping, ordering, sequencing, dependency encoding, cardinalities, and relationship encoding;
- identity and revision syntax; timestamps, freshness, ordering, canonicalization, digests, signatures, and approval-evidence formats;
- embedding, dereferencing, unknown fields, extensions, hierarchy, nesting, federation, inheritance, splitting, merging, conflict resolution, and cross-Workstream dependency resolution;
- templates, examples, dashboards, status views, validators, conformance fixtures, migrations, packaging, code generation, APIs, storage, transport, routing, orchestration, and runtime behavior.

No technology, provider, project-management product, or domain is preselected.
