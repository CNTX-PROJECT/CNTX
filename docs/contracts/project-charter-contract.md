# Project Charter Artifact Contract

## Status and authority

**Status: Accepted.** The Owner / Final Authority has granted final human approval, and CONTRACT-001 is accepted under [GOVERNANCE.md](../../GOVERNANCE.md). On merge and publication to `main`, it becomes the binding, subordinate artifact-specific contract baseline for Project Charter. It specializes, without redefining, the accepted Project Charter meaning and authoritative classification. The accepted [core architecture contract](../architecture/core-contract.md), [contract identity and versioning contract](../architecture/contract-identity-versioning.md), and [artifact-contract and schema-layering contract](../architecture/artifact-contract-schema-architecture.md) remain higher-authority sources. Future executable schemas, validators, and implementations remain subordinate.

This contract uses **MUST** and **MUST NOT** for mandatory requirements, **SHOULD** and **SHOULD NOT** for strong recommendations, and **MAY** for permission. It specializes, and does not redefine, the accepted primary Project Charter definition, authoritative classification, authority model, lifecycle, identity/versioning semantics, provenance model, privacy boundaries, or final human authority.

## Purpose and scope

This contract governs the root authoritative artifact that establishes enduring project intent and governance context for one declared project scope. It applies to future conforming Project Charter contracts, schemas, instances, extensions, profiles, validators, Conformance Claims, and implementations.

It does not redefine the canonical Project Charter; create a concrete charter; define concrete fields, field names, requiredness, syntax, ordering, timestamps, or cardinalities; select a schema language or serialization; create a template, form, payload example, validator, registry, migration, runtime, API, CLI, or adapter; define another artifact-specific contract; grant autonomous approval or unbounded authority; or include private implementation content.

## Accepted governing meaning and classification

The accepted primary definition, referenced without replacement, is: **Project Charter — Root statement of enduring intent and governance context.**

Project Charter is an authoritative canonical artifact. Its authority MUST derive from explicit final human approval by the applicable Owner / Final Authority under governing policy, not from existence, authorship, schema validity, automation, or implementation status. Only an explicitly approved Artifact Revision is authoritative for consequential use.

A Project Charter MUST NOT override repository governance, accepted architecture, law, applicable policy, privacy or security obligations, or final human authority. It MUST NOT approve itself or its own revision, authorize itself, or create cyclic authority. It supplies enduring project-level context, not task-level execution authority; that authority arises only through an approved Task Contract.

## Conceptual responsibilities

A conforming Project Charter MUST address the following semantic responsibilities without selecting fields or syntax:

- Enduring purpose and project intent.
- Desired outcomes and project-level success direction.
- Project scope and enduring boundaries, including explicit non-goals and exclusions.
- Governing principles and material constraints.
- Applicable governance context and final authority.
- Material assumptions, dependencies, risks, and unresolved uncertainty that shape enduring intent.
- Public/private and confidentiality boundaries.
- Expectations for downstream Workstreams and Task Contracts, consequential decisions, traceability, and change control.
- Conditions for review, amendment, supersession, and retirement.

These are semantic responsibilities, not concrete schema fields.

## Permitted and forbidden content

A Project Charter MAY contain enduring project-level context needed to govern downstream work. It MUST NOT silently become a Workstream; Task Contract or execution authorization; implementation plan or step-by-step procedure; volatile status report; Evidence Bundle; Review Record; Decision Record or decision log; State Snapshot; executable configuration; prompt collection; runtime instruction set; schema; API contract; container for unrelated context; or repository for secrets, credentials, personal data, production configuration, private source material, or private project data.

Implementation-specific detail SHOULD be excluded unless it is genuinely enduring, explicitly authorized project context. This public contract remains model-, provider-, runtime-, transport-, storage-, serialization-, schema-language-, and domain-independent.

## Roles, authority, and accountability

Owner / Final Authority MUST be human or explicitly human-governed. Authorship, consultation, specialist review, and final approval are separate responsibilities. Contributors and agents MAY act only within bounded, explicit, revocable delegation that remains subordinate to higher governance.

Specialist review is evidentiary and does not replace final approval. Approval MUST identify the exact Artifact Revision. Participation in charter authorship or review MUST NOT confer Workstream or Task Contract authority. Consequential self-approval and cyclic authority are prohibited.

## Required relationships and traceability

Project Charter is the root authoritative source for downstream enduring intent and governance context. Consequential downstream references MUST be resolvable and revision- or version-aware when pinning is required. Copied or embedded charter content MUST be identified as derived, preserve provenance, and MUST NOT silently become authoritative. Exact cardinalities, embedding, dereferencing, storage, caching, and offline packaging remain deferred.

| Downstream artifact | Relationship purpose | Authority limitation |
| --- | --- | --- |
| Workstream | Traces to the governing Project Charter identity and applicable revision/version context. | It does not alter charter authority or scope. |
| Task Contract | Is bounded by applicable Project Charter and Workstream context and records its own explicit authority. | Charter context alone grants no task execution authority. |
| Context Packet | MAY carry a selected, provenance-preserving derived selection of relevant charter context. | It cannot replace the authoritative charter. |
| Execution Result | MAY reference applicable charter context when relevant to a claimed result. | It cannot mutate or replace the charter. |
| Evidence Bundle | MAY support claims that relate to applicable charter context. | It cannot mutate, approve, or replace the charter. |
| Review Record | MAY evaluate charter-related evidence or results within declared specialty. | It is evidentiary and cannot approve or replace the charter. |
| Decision Record | MUST reference the applicable charter when a consequential decision interprets, changes, supersedes, or materially depends on enduring intent or governance context. | It records authorized decisions; it does not let the charter self-approve. |
| State Snapshot | MAY derive charter-related state for orientation or handoff. | It preserves provenance and cannot become the authoritative charter. |

## Lifecycle and change control

The conceptual lifecycle is initial authoring or proposal, bounded review, explicit final approval, authoritative use, amendment or clarification, and supersession or retirement. Only explicitly approved revisions are authoritative; proposed or reviewed content MUST NOT be represented as approved.

Consequential changes to enduring intent, project scope, non-goals, governance context, final authority, privacy boundaries, or material constraints require explicit review, an applicable Decision Record, and final human approval. A clarification MUST NOT disguise a consequential semantic change. Superseded and retired revisions retain provenance and traceability. Downstream artifacts MUST identify the applicable charter revision/version context where consequences depend on it.

Project Charter lifecycle remains distinct from Document Status, Contract Definition Version, Schema Version, Implementation Version, and downstream work lifecycle. This contract does not select state names, state-machine encoding, timestamps, or transition syntax.

## Identity, revision, versioning, and provenance

The accepted ARCH-002 distinctions apply without redefinition. A conforming Project Charter MUST support, as applicable, a stable Artifact Instance Identifier for one charter lineage; Artifact Revision for concrete charter-instance changes; Contract Definition Identifier and Contract Definition Version; Schema Identifier and Schema Version only if a future executable schema exists; approval state; Implementation Version; Content Digest evidence; Provenance Reference to authoritative source relationships and approval evidence; and declared extensions or profiles.

Artifact Revision is not Contract Definition Version; approval state is not Document Status; Schema Version is not charter revision; and Implementation Version is not charter authority. An identifier, digest, schema-valid result, or generated object does not itself grant approval or authority. Identifier and revision syntax, revision sequencing, digest algorithms, canonicalization, timestamps, signatures, approval-evidence formats, and registries remain deferred.

## Evidence, review, approval, and conformance

Consequential approval MUST be supported by evidence sufficient to identify the exact charter revision under consideration, governing contract/version context, applicable review scope and findings, material assumptions, limitations, dissent and unresolved uncertainty, and the authorized final human decision.

Review findings and Conformance Claims are evidentiary. Schema-valid does not necessarily mean contract-conformant; contract-conformant does not automatically mean approved; and approval does not erase uncertainty or dissent. Validators, reviewers, authors, generated code, and implementations do not acquire final authority merely by producing evidence. Evidence formats, signature mechanisms, conformance fixtures, and validation tooling remain deferred.

## Public/private and security boundaries

Public contracts, examples, tests, schemas, conformance evidence, and documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. A public Project Charter contract MUST NOT make private information mandatory. A conforming charter SHOULD safely reference restricted authoritative sources rather than copy sensitive content when traceability can be preserved.

## Extension and profile boundaries

Project Charter extensions and profiles MUST use explicit stable identities or namespaces, identify the governing contract and version, and remain additive and non-overriding unless a later accepted decision explicitly permits another relationship. They MUST NOT override final human authority, accepted core meaning, authoritative classification, provenance, privacy or security boundaries, lifecycle semantics, or mandatory requirements. They MUST NOT convert optional project-specific semantics into universal public-core requirements or require a provider, model, runtime, storage system, transport, schema language, serialization, or domain.

Namespace syntax, conflict handling, discovery, negotiation, and registry governance remain deferred.

## Deferred schema decisions

This contract defers, without deciding:

- Concrete fields, field names, requiredness, nesting, schema language, and serialization.
- Cardinalities, relationship encoding, status and approval-state encoding, and identity or revision syntax.
- Timestamps, ordering, canonicalization, digest algorithms, signatures, and approval-evidence formats.
- Embedding, dereferencing, unknown fields, unknown extensions, and multi-charter hierarchy, federation, inheritance, or conflict resolution.
- Templates, examples, validators, conformance fixtures, migrations, packaging, code generation, APIs, storage, transport, and runtime behavior.

No technology, provider, or implementation is preselected.
