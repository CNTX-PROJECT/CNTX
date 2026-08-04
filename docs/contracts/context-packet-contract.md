# CNTX Context Packet Artifact Contract

## Status and authority

**Status: Accepted.** Final human approval by the Owner / Final Authority has been granted, and this contract is accepted under [GOVERNANCE.md](../../GOVERNANCE.md). On merge and publication to `main`, it becomes the binding, subordinate artifact-specific contract basis for the canonical Context Packet. Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** strong recommendations, and **MAY** permission; these terms express requirement strength only within this contract.

ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-003 remain higher Accepted authority sources. This contract specializes, without redefining, the accepted Context Packet primary definition and Derived classification. Executable schemas, selectors, validators, retrieval systems, and implementations remain subordinate future work.

## Purpose and scope

This contract governs the Derived Context Packet artifact: it is assembled for one exact applicable approved Task Contract revision, supplies the minimum justified task-relevant source material to a Bounded Implementer, preserves source provenance and revision/version context, and supports execution without granting authority. Exact packet cardinality per Task Contract, packet lineage, and reuse between executions remain schema or implementation work.

It does not redefine Context Packet; create an instance; amend Project Charter, Workstream, or Task Contract; define fields, names, requiredness, nesting, syntax, ordering, timestamps, or cardinalities; select a schema or serialization technology; create a template, form, payload example, prompt, prompt library, retrieval, search, ranking, embedding, vector-database, policy, access-control, routing, workflow, orchestration, validator, registry, migration, runtime, CLI, API, adapter, code generator, Execution Result contract, or private implementation content. Token budgets, truncation, chunking, and summarization algorithms remain out of scope.

## Accepted governing meaning and classification

This contract references, without competing with, the accepted primary definition:

> Context Packet — Supplies the minimum task-relevant source material to an executor.

Context Packet is a **Derived** canonical artifact. The Lead Architect or authorized selector conceptually prepares it, and the exact approved Task Contract revision governs selection. It is not an independent authority source. Existence, possession, receipt, technical access, schema validity, generated status, retrieval result, or executor capability grants no authority.

A packet MUST NOT modify, broaden, replace, or reinterpret the Task Contract; replace authoritative Project Charter, Workstream, or Task Contract sources; constitute, replace, or grant final approval, a review decision, integration authority, release authority, or merge authority; or silently share context or authority between different Task Contracts. When task-relevant, it MAY carry provenance-preserving references to or derived selections from applicable approval, review, or decision sources, but those sources remain controlling.

## Governing Task Contract boundary

An exact approved Task Contract revision MUST exist before authoritative Context Packet selection. Its scope, authority, permitted resources, forbidden zones, security/privacy constraints, stop conditions, and evidence expectations remain controlling. Packet content is not permission, contextual relevance is not authorization, and a packet cannot fill missing Task Contract authority or authorize an out-of-scope source or action. Material Task Contract change requires packet reassessment; amendment or refresh does not retroactively authorize prior execution.

## Minimum sufficient context and selection principles

Minimum sufficient context is a bounded selection sufficient to perform the permitted task responsibly without irrelevant or excessive material. Selection MUST use explicit task relevance, least disclosure, and explicit relevance rationale; include only sources needed for objective, constraints, interfaces, safety, validation, or acceptance; preserve explicit provenance and consequential revision/version or time context; and state uncertainty, limitations, conflicts, missing sources, exclusions, and redaction boundaries where material.

Unrelated Workstream, peer-task, and historical context is excluded by default. A full Project Charter, Workstream, conversation history, repository snapshot, maximum-context strategy, or unrestricted context dump MUST NOT be included merely “just in case,” nor may selection become a hidden global project brain. “Minimum” does not permit omitting necessary safety, dependency, uncertainty, or validation context. Sufficiency and minimality are reviewable claims and MUST NOT be silently assumed.

## Source selection, provenance, and conflict handling

Each material source MUST retain enough provenance to identify the source type, applicable identity/revision/contract or schema version, whether content is direct, summarized, extracted, redacted, or transformed, and resulting uncertainty, loss, limitation, freshness, unavailable source, or deliberate exclusion. Authoritative references MUST be resolvable and revision-aware where pinning is required. Mutable labels, titles, branch names, paths, or unversioned summaries MUST NOT replace a pinned reference. Embedded authoritative content is a derived copy; summaries and extracts preserve provenance; a Content Digest may strengthen evidence but grants neither authority nor approval. Exact identifiers, digest algorithms, canonicalization, and storage remain deferred.

Packet content never overrides governing Task Contract, Project Charter, Workstream, governance, accepted architecture, or security/privacy requirements. Material conflict MUST be reported and requires stop or escalation; it MUST NOT be silently summarized away. The most recent source is not automatically the highest authority, and a derived summary is not a replacement for authoritative content. Automatic conflict resolution remains deferred.

## Conceptual responsibilities

A conforming Context Packet MUST semantically address governing Task Contract identity and exact revision; applicable Charter and Workstream context; task objective and selection purpose; selected source set and relevance rationale; forbidden context and exclusions; provenance and pinning; material freshness; assumptions, dependencies, uncertainty, conflicts, and inaccessible sources; summary, extraction, transformation, and redaction limits; security, privacy, confidentiality, public/private classification, access and least-disclosure constraints; sufficiency/minimization evidence; stop/escalation conditions; amendment, refresh, withdrawal, expiration, supersession, retirement, and retention expectations; and the packet revision linked to execution evidence. These are semantic responsibilities, not concrete fields.

## Permitted and forbidden content

A Context Packet MAY contain task-relevant authoritative references, minimal derived extracts or summaries, relevant constraints, interfaces, assumptions, uncertainty, necessary safety/privacy/validation/acceptance context, and provenance-preserving references to restricted sources where copying is prohibited.

It MUST NOT become a Project Charter, Workstream, Task Contract, task authorization, unrelated task collection, unrestricted context dump, global project brain, full conversation history, full repository snapshot without task necessity, prompt library, autonomous-agent loop, execution script, workflow/routing/orchestration definition, Execution Result, Evidence Bundle, Review Record, Decision Record, State Snapshot, proof of correctness/completion/approval, executable schema, API contract, runtime configuration, or store for secrets, credentials, personal data, production configuration, private paths, or private project content.

## Roles, authority, and accountability

Owner / Final Authority remains human or explicitly human-governed. The Lead Architect or authorized selector prepares the packet within the governing Task Contract; selector authority is explicit, bounded, traceable, and subordinate. Authorship, selection, execution, review, approval, and final authority remain distinct. The Bounded Implementer receives and uses the packet but MUST NOT broaden it autonomously; it may report missing or conflicting context and request a further selection under the governing Task Contract. Technical access to extra sources is not permission to use them. Specialist Review may assess minimization, sufficiency, provenance, privacy, or security and remains evidentiary. Packet preparation grants no integration, release, deployment, or merge authority. Self-approval and cyclic authority are prohibited. No canonical Context Manager, Context Owner, Prompt Engineer, or Retrieval Agent role is introduced.

## Required relationships and traceability

The accepted dependency direction remains:

`Project Charter → Workstream → Task Contract → Context Packet / Execution Result`

| Related artifact | Required relationship and authority limit |
| --- | --- |
| Project Charter | Only relevant derived Charter context; authoritative Charter remains controlling. |
| Workstream | Only minimal relevant Workstream context; full Workstream context is not included by default. |
| Task Contract | Exact approved revision governs selection, scope, and authority. |
| Peer Context Packet | May be an explicit provenance-bearing source or dependency only; packets share no authority or implicit context. |
| Execution Result | Traces to the used Context Packet revision; it cannot change or approve the packet. |
| Evidence Bundle | May support selection, sufficiency, minimization, and provenance claims; grants no authority. |
| Review Record | May assess packet and evidence; cannot authorize selection or execution. |
| Decision Record | Records consequential selection, exception, conflict, or risk decisions when governance requires. |
| State Snapshot | May orient, remains Derived, and cannot replace authoritative sources or Context Packet. |

Derived and evidentiary artifacts do not replace authoritative artifacts, and peer packets transfer no authority. Cardinalities, relationship encoding, embedding, caching, dereferencing, and packaging remain deferred.

## Lifecycle and change control

The conceptual lifecycle includes selection preparation; bounded sufficiency/minimization review where required; packet release or supply; use under the exact Task Contract revision; refresh, amendment, or replacement; withdrawal, expiration, supersession, or retirement; and provenance-preserving retention for execution traceability. Only a packet assembled under a current approved Task Contract may be used for execution. Execution traces to the exact used packet revision. Packet change produces a new Artifact Revision when traceability requires it; material source, Task Contract, dependency, security, privacy, or uncertainty change requires reassessment.

Refresh does not change Task Contract authority. Historical packet revisions remain traceable; stale, withdrawn, or superseded packets MUST NOT be silently represented as current execution context. Packet freshness remains distinct from Document Status, approval state, Contract Definition Version, Schema Version, and Implementation Version. Concrete states, transition syntax, timestamps, and automation remain deferred.

## Identity, revision, versioning, and provenance

ARCH-002 applies without redefinition. Artifact Type, Context Packet Artifact Instance Identifier, Context Packet Artifact Revision, governing Contract Definition Identifier and Version, governing Task Contract identity and exact revision, governing Charter/Workstream references, future Schema Identifier and Version, Document Status, packet lifecycle/freshness, approval state, Implementation Version, Content Digest, and Provenance Reference remain distinct. Identifiers, digests, freshness, schema validity, and retrieval success grant neither authority nor approval. A packet lineage MUST NOT be silently reused for a materially different Task Contract. Lineage criteria, syntax, revision sequencing, timestamps, and digests remain deferred.

## Evidence, review, approval, and conformance

Evidence supports claims about relevance, minimum selection, sufficiency, provenance, source revision/freshness, exclusions/redactions, missing sources, assumptions, uncertainty, conflicts, privacy/security/least disclosure, and transformation integrity where relevant. Schema-valid does not necessarily mean contract-conformant; contract-conformant does not mean sufficient, current, approved, or safe for execution; retrieval success does not show the selected source is right or authoritative; completeness does not show minimality; and minimality does not show necessary context is present. Validation or review grants no task authority. Context Packet, Execution Result, Evidence Bundle, Review Record, Decision Record, and approval remain distinct; reviewers report uncertainty and contradictory evidence.

## Public/private, security, and confidentiality boundaries

Public packets, examples, tests, and documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, hostnames, private project content, or private domain-specific implementation. Restricted authoritative content SHOULD be safely referenced rather than copied. Redaction and sanitization preserve provenance and identify information loss. Access to restricted content is not authority to disclose it; minimization applies within private implementations too; and public CONTRACT-004 never makes private material mandatory. Security/privacy uncertainty requires stop and escalation. Private project, deployment, infrastructure, production, and domain-specific implementation context are forbidden.

## Extensions and profiles

Extensions and profiles MUST use explicit stable identity or namespace, identify governing CONTRACT-004/version, remain additive and non-overriding, and not weaken minimization, provenance, privacy, context isolation, or final human authority. They MUST NOT require complete-context strategy, provider, model, runtime, retrieval product, vector database, storage, transport, schema language, serialization, or domain, or elevate optional private implementation semantics to universal core.

## Deferred schema and implementation decisions

This contract defers concrete fields, requiredness, names, nesting, schema language, serialization, packet cardinality/lineage, identity/revision/approval representation, timestamps/freshness/expiry/refresh encoding, provenance encoding, digest/signing/encryption/canonicalization, embedding/dereferencing/offline packaging, ranking/relevance scoring, retrieval/search/RAG/embedding/vector technology, chunking/truncation/summarization/token budgets, redaction/sanitization algorithms, access-control/secure references, caching/invalidation, conflict resolution, packet/prompt assembly and delivery, validators/conformance fixtures/tests, templates/examples, migrations/compatibility tooling, APIs, CLIs, storage, transport, scheduling, retries, orchestration, and runtime behavior. No technology or provider is selected.
