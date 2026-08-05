# CNTX Review Record Artifact Contract

**Status: Proposed.** This contract is submitted under [GOVERNANCE.md](../../GOVERNANCE.md). It is not binding before separate final human acceptance and publication on `main`. **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express requirement strength only within this Proposed contract and grant no authority.

ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006 remain higher authority sources. This contract specializes only Review Record semantics; it does not redefine its primary definition, canonical responsibility, or Evidentiary classification. Schemas, validators, scoring systems, workflows, and implementations remain future work.

## Accepted governing meaning and classification

> Review Record — Preserves specialist findings, uncertainty, and recommendation.

Review Record remains an **Evidentiary** canonical artifact. A Specialist Reviewer authors it; it does not constitute final approval. It preserves traceable specialist assessment of exact review subjects and revisions within explicit, bounded, traceable authority and declared specialty. It is non-authoritative, not self-approved, and cannot create, broaden, replace, or retroactively grant Task Contract authority. Existence, authorship, completion, schema validity, reviewer title, tool output, status, signature, timestamp, or digest grants neither authority nor approval.

## Purpose, scope, and non-goals

This contract governs Review Records that assess exact Execution Result claims and Evidence Bundle evidence, or another explicitly authorized reviewable outcome; preserve findings, uncertainty, limitations, assumptions, dissent, evidence use, methods, checks, exclusions, and recommendation; distinguish reviewed from unreviewed scope; and support decision-making without becoming the consequential decision. Positive, negative, partial, inconclusive, contradictory, and adverse findings remain preservable.

It does not create a concrete instance, perform a review, modify an Execution Result or Evidence Bundle, create a Decision Record, record final approval, modify a Task Contract, or define fields, serialization, templates, forms, checklists, rubrics, examples, scores, severity, pass/fail labels, validators, reviewbots, scoring or approval engines, APIs, CLIs, workflow, routing, orchestration, runtime, provider, model, tool, storage, transport, or domain choices.

## Review authority, specialty, and subjects

Consequential review work MUST have one exact approved Task Contract revision or other explicit approved review authority. That authority governs scope, declared specialty, subjects, permitted sources, methods, constraints, stop conditions, privacy, security, and integration boundaries. Technical access, expertise, title, usefulness, or possession is not permission. Missing authority cannot be filled by a review; out-of-scope findings and security, privacy, access, provenance, or authority uncertainty require stop or escalation.

Declared specialty, reviewed subject identity and revision, claims, evidence, criteria, concerns, methods, conditions, coverage, depth, and unreviewed areas remain explicit and reviewable. Partial review is not complete review; absence of a finding is not absence of a defect; “no issues found” is meaningful only within actual scope. Mutable labels, branch names, paths, and unversioned summaries do not replace pinned references. Material subject, evidence, method, scope, specialty, or uncertainty change may require reassessment.

## Execution Result, Evidence Bundle, and findings

An exact Execution Result Artifact Revision MAY be assessed. Result claims and findings remain separate; Review Record cannot modify, correct, supersede, accept, reject, approve, or replace the result. An exact Evidence Bundle revision MAY be assessed for relevance, provenance, integrity, authenticity, freshness, completeness, coverage, independence, reproducibility, uncertainty, limitations, conflict, bias, and sufficiency. Evidence assembly and review authorship remain distinguishable; overlap, conflict of interest, prior involvement, and material dependency remain visible. Required independence is controlled by governing authority and appropriate to risk.

Observation, interpretation, finding, supporting rationale, contradictory information, unresolved question, uncertainty, limitation, dissent, and recommendation remain distinct semantic responsibilities. Findings are traceable to subject, evidence, and method where material. Facts, interpretations, and recommendations are not silently merged; adverse findings, contradictions, unavailable, inaccessible, stale, redacted, excluded, and missing evidence remain visible. Direct and derived evidence remain distinct, copies or transformations are not independent corroboration, and machine output is not automatically specialist judgment.

## Recommendation, authority, and decisions

A recommendation is specialist and Evidentiary, not authoritative. It is not final approval, rejection, acceptance, integration, release, deployment, or merge. It MAY advise further evidence, correction, reassessment, acceptance, rejection, escalation, or deferral without a fixed enum. An Owner / Final Authority or authorized decision-maker may follow or reject it; any consequential decision remains separately authorized and, where required, recorded in a Decision Record. Review count, majority, score, tool, or automatic conflict resolution creates no decision. Self-approval and cyclic authority are prohibited.

Methods, checks, tools, and procedures are used only within authorized scope. Their outputs are bounded evidence: validation, schema validity, conformance, and tests do not automatically establish correctness, completeness, safety, acceptance, or approval. Procedures, toolchains, checklists, tests, and validator behavior remain deferred.

## Required artifact relationships

| Related artifact | Required conceptual relationship |
| --- | --- |
| Project Charter | Governing intent and boundaries remain controlling; review cannot amend or replace them. |
| Workstream | Relevant bounded context may be referenced; review cannot mutate scope or declared state. |
| Task Contract | Exact approved review and execution authority govern scope, specialty, sources, and limits; review grants no authority. |
| Context Packet | May identify Derived context; packet content remains non-authoritative and is not approved by review. |
| Execution Result | Exact result revision may be assessed; findings cannot modify, approve, or replace it. |
| Evidence Bundle | Exact evidence revision may be assessed; review remains separate and Evidentiary. |
| Peer Review Record | May provide explicit comparison or dissent; no implicit consensus, authority, or majority decision is created. |
| Decision Record | May cite review as decision input; the consequential decision remains separately authorized and recorded. |
| State Snapshot | May orient to integrated state and provenance; it cannot replace Review Record or authoritative sources. |

`Project Charter → Workstream → Task Contract → Context Packet / Execution Result` remains controlling. Review Record is decision input, not an authority node; Derived and Evidentiary artifacts do not replace authoritative artifacts.

## Lifecycle, identity, privacy, and deferred decisions

The conceptual lifecycle is authorization and scoping; subject and evidence availability; specialist assessment; authoring; availability as decision input; correction or supplementation; reassessment; supersession or withdrawal; retention and historical traceability. Availability is not approval; stale, withdrawn, or superseded reviews are not silently current.

ARCH-002 applies without redefinition. Artifact Type; Review Record Artifact Instance Identifier and Revision; subject, Execution Result, Evidence Bundle, Task Contract, Context Packet, reviewer, specialty, Contract Definition, schema, lifecycle, recommendation, approval, Decision Record, implementation, digest, provenance, and State Snapshot identities or states remain distinct. Identifiers grant no authority, revisions no approval, digests no truth, timestamps no correctness, and schema validity no review quality or sufficiency.

Public Review Records MUST NOT expose secrets, credentials, personal data, production configuration, private paths, hostnames, restricted material, or private project, deployment, infrastructure, or domain-specific implementation context. Least privilege and least disclosure apply; redaction preserves provenance and visible material loss. Extensions are additive, non-overriding, explicitly identified, and cannot weaken specialty, scope, uncertainty, provenance, privacy, or final human authority.

Concrete fields, names, requiredness, nesting, ordering, serialization, taxonomy, cardinality, specialty representation, accreditation, coverage, depth, finding, severity, confidence, dissent, independence, methods, checklists, aggregation, voting, identifiers, timestamps, digests, signing, encryption, validators, fixtures, templates, interfaces, APIs, CLIs, workflow, runtime, storage, retention, provider, model, database, tool, and domain choices remain deferred. No technology or provider is selected.
