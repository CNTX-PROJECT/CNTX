# CNTX Evidence Bundle Artifact Contract

**Status: Accepted.** Final human approval by the Owner / Final Authority has been granted, and this contract is accepted under [GOVERNANCE.md](../../GOVERNANCE.md). On merge and publication to `main`, it becomes the binding, subordinate artifact-specific contract basis for the canonical Evidence Bundle. Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** strong recommendations, and **MAY** permission; these terms express requirement strength only within this contract and grant no authority.

ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-005 remain higher authority sources. This accepted contract specializes only the canonical Evidence Bundle semantics; it does not redefine the accepted primary definition or Evidentiary classification. Executable schemas, validators, formats, collection systems, and implementations remain subordinate future work.

## Accepted governing meaning and classification

The accepted primary definition is:

> Evidence Bundle — Collects provenance, checks, assumptions, and limitations supporting a claim.

Evidence Bundle remains an **Evidentiary** canonical artifact. A bundle conceptually gathers or provenance-preservingly references evidence for one or more exactly identified claims about an exact Execution Result revision or another exactly identified reviewable outcome. The bundle itself is not authoritative. Referencing an authoritative source as evidence does not transfer that source's authority to the bundle; the authoritative source remains controlling in its own role.

Bundling, copying, embedding, summarizing, or transforming a source does not replace that source. Existence, authorship, collection, receipt, storage, schema validity, validator success, digest, signature, timestamp, tool output, or bundle status grants neither authority nor approval. A bundle cannot automatically prove correctness, completeness, acceptance, integration, release, deployment, or merge; it is not self-approved and cannot create or broaden Task Contract authority.

## Purpose and scope

This contract governs Evidence Bundles that make identified claims traceably supported, qualified, contradicted, or insufficiently supported; connect evidence to an exact reviewable subject and revision; preserve material provenance, collection and transformation context, uncertainty, and limitations; and make evidence available for Specialist Review and final human decision-making without elevating it into a decision or authority.

A conforming bundle is not limited to favorable evidence. It MUST be able to retain material evidence that supports a claim wholly or partly, qualifies or contradicts it, increases uncertainty, exposes a limitation, shows missing evidence, or shows that the claim cannot responsibly be established.

## Non-goals

This contract does not redefine the primary meaning; create a concrete bundle, evidence item, Execution Result approval, Review Record, Decision Record, or final human approval; modify a Task Contract; or determine concrete fields, names, requiredness, nesting, syntax, ordering, templates, payloads, examples, evidence-type enumeration, scores, quality grades, or acceptance thresholds.

It selects no JSON, YAML, XML, serialization, chain-of-custody implementation, signing, hashing, encryption, timestamp technology, collector, crawler, recorder, database, validator, test runner, API, CLI, workflow, routing, orchestration, runtime, provider, model, tool, storage, transport, or domain requirement. Private implementation content is outside this public contract.

## Governing Task Contract boundary

One exact approved Task Contract revision remains the governing authority source for bounded execution. Its objective, scope, permitted resources, forbidden zones, acceptance criteria, expected evidence, security and privacy requirements, stop conditions, and integration boundaries remain controlling. Evidence Bundle cannot modify, broaden, replace, reinterpret, or retroactively authorize that Task Contract.

Evidence obtained outside authorized scope creates no retroactive authority. Technical access to a source is not permission to collect, copy, retain, or publish it. Missing Task Contract authority cannot be filled by evidence. Unexpected evidence of possibly unauthorized work MUST be reported and handled under separate security and governance authority. Expected evidence is a governing expectation, but its presence is not an acceptance decision; missing expected evidence remains visible, and additional evidence cannot expand scope or authority.

## Context Packet and Execution Result relationships

Context Packet remains Derived and may provide minimal task-relevant source context. A bundle MAY reference the applicable Context Packet identity and revision where material to provenance or claim assessment, but packet content is not authority or permission. Evidence about context selection, sufficiency, minimization, or provenance cannot amend or approve the packet. Conflicts with packet context remain explicit, full packet contents are not copied by default, and minimal disclosure with provenance-preserving references is preferred.

An Evidence Bundle MAY have an exact Execution Result Artifact Revision as reviewable subject. Result claims and evidence remain distinct: a result claim is not true merely because a bundle exists. A bundle may traceably support or contradict material result claims, limitations, checks, side effects, assumptions, uncertainty, failures, deviations, stops, escalations, and unperformed work. It cannot modify, correct, supersede, accept, or reject the result. A changed result can require reassessment; later evidence remains recognizably later and cannot retroactively authorize earlier execution. Exact cardinality between Execution Results and bundles remains deferred.

## Reviewable outcome and evidence-item semantics

A reviewable subject MUST be exactly identifiable and revision-aware, with the claim or outcome explicitly bounded. A bundle MUST NOT silently combine evidence for independent tasks or outcomes, or add unrelated evidence "just in case." Relevance per claim or subject remains reviewable. Evidence MAY be reused for multiple claims when that relationship is explicit and provenance-preserving; reuse grants neither implicit authority, approval, independence, nor double-counted corroboration. Cardinality, nesting, composition, and packaging remain deferred.

Evidence may conceptually include direct observations, measurements, logs, test and validation outputs, before/after state observations, provenance records, checks, human attestations, external source references, derived analyses, negative or contradictory evidence, and unavailable or missing evidence. These are conceptual categories, not a concrete schema enumeration.

Each material item MUST retain sufficient conceptual context to assess the relevant claim or outcome; source identity and revision; observation or collection context; relevant conditions, environment, configuration, method, or tool; whether it is direct, derived, summarized, transformed, redacted, or copied; uncertainty, limitation, bias, completeness, freshness, validity, provenance-chain, privacy, access, and disclosure constraints. These are semantic responsibilities, not concrete fields.

## Claim-to-evidence traceability and quality boundaries

Material evidence MUST be traceable to one or more identified claims or reviewable outcomes, and material claims MUST be traceable to supporting, qualifying, contradictory, or missing evidence where relevant. Evidence without clear task relevance is not included by default; its relevance rationale remains reviewable. Subject and evidence revisions remain exact, unsupported claims are not presented as proven, and missing evidence, gaps, and unresolved uncertainty remain explicit.

Assessment keeps relevance, source identity, provenance, integrity, authenticity, freshness, validity context, completeness, coverage, independence, reproducibility, transformation loss, uncertainty, limitations, conflict, bias, and adverse evidence distinct. Quality and sufficiency are reviewable claims, not silent facts. Complete or minimal does not automatically mean correct or sufficient. Schema validity, collection success, retrieval success, a tool exit code, or a passed test is evidence only for its bounded source, scope, conditions, and environment. Freshness creates neither authority nor correctness, and stale evidence is not silently presented as current. Universal scores, confidence scales, and thresholds remain deferred.

## Direct, derived, contradictory, and sufficient evidence

Direct evidence and derived evidence remain distinct. Derived analysis MUST provenance-preservingly identify material source inputs and transformations. A summary, extract, normalization, conversion, or aggregation does not become direct evidence; information loss, uncertainty, and transformation limitations remain explicit. Machine-generated analysis does not automatically establish correctness or independent corroboration. A Content Digest may help support integrity, but guarantees no truth, accuracy, authenticity, authority, or approval. Any future signatures or timestamps retain the same authority limit; their mechanisms remain deferred.

Material contradictory or adverse evidence MUST NOT be silently omitted or cherry-picked away. Unresolved contradictions remain reported and are not silently resolved by summarization or aggregation. A bundle may contradict a claim or state it insufficiently supported. Absence of evidence is not automatically evidence of absence; an evidence-of-absence claim requires reviewable search scope, method, and coverage. Copies or transformations of one source are not independent corroboration, and automatic conflict resolution remains deferred.

Evidence sufficiency is claim- and decision-context-specific. Task Contract expected evidence and acceptance criteria provide controlling context, but the bundle does not authorize a final sufficiency decision. Completeness, coverage, and sufficiency remain separate. Material missing, unavailable, inaccessible, redacted, or excluded evidence and reasons for exclusion remain reviewable. A bundle does not collect unlimited logs, files, conversations, or repository content; maximum-evidence collection is not a default. Evidence minimization cannot conceal necessary adverse, safety, security, dependency, or validation evidence, and must be balanced with privacy and least disclosure. Algorithms and thresholds remain deferred.

## Provenance, integrity, and change control

Material evidence MUST identify its source and applicable revision where material. Copies, extracts, summaries, transformations, redactions, and aggregations remain visible. Consequential references are resolvable and revision-aware where pinning is required; mutable labels, file paths, branch names, or unversioned summaries do not replace pinned references. Bundle assembly creates no source authority. Integrity and authenticity claims remain distinct, provenance gaps are explicit, and silent replacement or tampering is prohibited. A consequential correction or replacement requires a new Artifact Revision where traceability requires it; historical revisions remain available or traceable. Chain-of-custody encoding, signing, timestamping, hashing, secure storage, and audit-log mechanisms remain deferred.

The conceptual lifecycle is evidence identification; authorized collection or reference; provenance-preserving assembly; availability for review; assessment and use as decision input; correction or supplementation; supersession or withdrawal; retention, archival, or disposal; and historical traceability. Only evidence under valid authority is added. Availability is not approval, review does not imply mutation or approval, and later evidence remains identifiable as later. Corrections do not erase the originally used revision. Withdrawn, stale, or superseded evidence is not silently presented as current. Retention and disposal respect security, privacy, legal, and provenance requirements. Concrete states, transition rules, timestamps, and automation remain deferred.

## Roles, authority, and accountability

Owner / Final Authority remains human or explicitly human-governed. A Bounded Implementer may normally assemble evidence for its own bounded execution; another contributor may collect or add evidence only under explicit bounded authority. This contract introduces no canonical Evidence Collector, Evidence Curator, Auditor, or Approver role.

A Bounded Implementer or Specialist Reviewer MAY assemble an Evidence Bundle under explicit, bounded, and traceable authority. Other contributors MAY collect or contribute evidence only under explicit bounded authority, but such contribution does not assign them the canonical bundle-assembler responsibility or create a new canonical role. Bundle assembly grants no review, approval, or final authority.

Authorship, collection, assembly, execution, review, approval, and final authority remain distinct. An assembler does not approve its bundle, and a Bounded Implementer MUST NOT conceal contradictory evidence. Specialist Review may assess quality, relevance, sufficiency, provenance, and limitations within declared expertise, but remains Evidentiary. Review Record grants no final approval; Decision Record records a separately authorized consequential decision where governance requires it. Evidence Bundle grants no integration, release, deployment, or merge authority. Self-approval, cyclic authority, and authority laundering are prohibited.

## Required artifact relationships

| Related artifact | Required conceptual relationship |
| --- | --- |
| Project Charter | Governing enduring intent and boundaries remain controlling; a bundle cannot amend or replace them. |
| Workstream | Relevant bounded work context may be referenced; a bundle cannot mutate Workstream scope or state. |
| Task Contract | Exact approved revision governs scope, authority, expected evidence and acceptance criteria; the bundle grants no authority. |
| Context Packet | May provide traceable Derived source context; packet content remains non-authoritative and is not copied without task need. |
| Execution Result | Exact result revision or its identified claims may be supported, qualified or contradicted; the bundle cannot modify or approve the result. |
| Peer Evidence Bundle | May be explicitly referenced or composed with provenance; no implicit merge, independence, authority or double-counting is created. |
| Review Record | May assess identified evidence within declared expertise; review remains Evidentiary and separate from approval. |
| Decision Record | May cite the bundle as decision basis; the consequential decision remains separately authorized and recorded. |
| State Snapshot | May orient to integrated state and provenance; it cannot replace the bundle, underlying evidence or authoritative sources. |

The accepted dependency direction remains:

`Project Charter → Workstream → Task Contract → Context Packet / Execution Result`

Evidence Bundle adds supporting traceability but is not an authority node in that direction. Derived and Evidentiary artifacts do not replace authoritative artifacts. Peer bundles share no implicit context, authority, or approval. Exact relationship encoding, cardinality, nesting, composition, and packaging remain deferred.

## Identity, revision, versioning, and conformance

ARCH-002 applies without redefinition. Artifact Type; Evidence Bundle Artifact Instance Identifier and Artifact Revision; constituent item identities and revisions; reviewable-subject identity and revision; governing Task Contract identity and exact approved revision; applicable Context Packet and Execution Result identities and revisions; Contract Definition Identifier and Version; future Schema Identifier and Version; Document Status; lifecycle; evidence freshness or validity context; approval state; Implementation Version; Content Digest; and Provenance Reference remain distinct.

Identifiers grant no authority, revisions no approval, digests no truth, timestamps no correctness, schema validity no authenticity or sufficiency, and collection success no relevance. Exact identity syntax, revision sequencing, timestamp, digest, and canonicalization decisions remain deferred.

Evidence Bundle and Review Record remain Evidentiary and separate. Review is specialist assessment, not final approval. Decision Record separately records an authorized consequential decision. Meeting acceptance criteria is evidence for a decision, not the decision itself; a sufficiency assessment grants no task authority. Contract conformance does not automatically mean complete, sufficient, correct, authentic, current, accepted, or safe. Schema validity does not automatically mean contract conformance, and review pass does not automatically mean acceptance, integration, release, deployment, or merge. Contradictory review evidence and reviewer uncertainty, scope, and expertise limits remain explicit; final human authority remains intact.

## Public/private, security, and confidentiality boundaries

Public bundles, examples, tests, and documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, hostnames, restricted source material, private project, deployment, infrastructure, or domain-specific implementation context. Collection follows least privilege and least disclosure. Restricted evidence is preferably safely referenced rather than copied; access is not authority to bundle or disclose it. Redaction and sanitization preserve visible provenance and material information loss and do not silently change meaning. Unauthorized collection is not legitimized by bundling. Security, privacy, access, or provenance uncertainty requires stop and escalation. Retention and disposal preserve privacy and security boundaries. This public contract requires no private evidence or private implementation.

## Extensions and deferred decisions

Extensions and profiles MUST use explicit stable identity or namespace, identify the governing CONTRACT-006 version, remain additive and non-overriding, and not weaken integrity, provenance, relevance, uncertainty, privacy, or final human authority. They must not require favorable-evidence-only policy, a universal confidence score, or a provider, model, runtime, evidence tool, storage, transport, database, schema language, serialization, or domain. They cannot add authority or approval to Evidence Bundle.

Concrete fields, names, requiredness, nesting, ordering, schema language, serialization, evidence-item taxonomy, bundle and item cardinality, subject-claim-evidence encoding, composition, identifiers, revision syntax, timestamps, freshness and expiry encoding, provenance and chain-of-custody encoding, integrity, authenticity and quality representations, confidence scales, scores, thresholds, acceptance matrices, source ranking, corroboration, duplicate detection, conflict resolution, digests, signing, encryption, canonicalization, redaction algorithms, capture, collection, retrieval, environment capture, reproducibility, storage, transport, caching, retention implementations, validators, conformance fixtures, test suites, templates, examples, dashboards, interfaces, APIs, CLIs, scheduling, retries, routing, workflow, orchestration, runtime behavior, and provider, model, database, and domain choices remain deferred. No technology or provider is selected.
