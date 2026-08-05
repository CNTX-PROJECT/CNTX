# CNTX Review Record Artifact Contract

**Status: Accepted.** Final human approval by the Owner / Final Authority has been granted, and this contract is accepted under [GOVERNANCE.md](../../GOVERNANCE.md). On merge and publication to `main`, it becomes the binding, subordinate artifact-specific contract basis for the canonical Review Record. **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express requirement strength only within this contract and grant no authority.

ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006 remain higher authority sources. This accepted contract specializes only Review Record semantics; it does not redefine its primary definition, canonical responsibility, or Evidentiary classification. Schemas, validators, scoring systems, workflows, and implementations remain future work.

## Accepted governing meaning and classification

> Review Record — Preserves specialist findings, uncertainty, and recommendation.

Review Record remains an **Evidentiary** canonical artifact. A Specialist Reviewer authors it; it does not constitute final approval. It preserves traceable specialist assessment of exact review subjects and revisions within explicit, bounded, traceable authority and declared specialty. It is non-authoritative, not self-approved, and cannot create, broaden, replace, or retroactively grant Task Contract authority. Existence, authorship, completion, schema validity, reviewer title, tool output, status, signature, timestamp, or digest grants neither authority nor approval.

## Purpose, scope, and non-goals

This contract governs Review Records that assess exact Execution Result claims and Evidence Bundle evidence, or another explicitly authorized reviewable outcome; preserve findings, uncertainty, limitations, assumptions, dissent, evidence use, methods, checks, exclusions, and recommendation; distinguish reviewed from unreviewed scope; and support decision-making without becoming the consequential decision. Positive, negative, partial, inconclusive, contradictory, and adverse findings remain preservable.

It does not create a concrete instance, perform a review, modify an Execution Result or Evidence Bundle, create a Decision Record, record final approval, modify a Task Contract, or define fields, serialization, templates, forms, checklists, rubrics, examples, scores, severity, pass/fail labels, validators, reviewbots, scoring or approval engines, APIs, CLIs, workflow, routing, orchestration, runtime, provider, model, tool, storage, transport, or domain choices.

## Review authority, specialty, and subjects

Consequential review work MUST have one exact approved Task Contract revision or other explicit approved review authority. That authority governs scope, declared specialty, subjects, permitted sources, methods, constraints, stop conditions, privacy, security, and integration boundaries. Technical access, expertise, title, usefulness, or possession is not permission. Missing authority cannot be filled by a review; out-of-scope findings and security, privacy, access, provenance, or authority uncertainty require stop or escalation.

Declared specialty, reviewed subject identity and revision, claims, evidence, criteria, concerns, methods, conditions, coverage, depth, and unreviewed areas remain explicit and reviewable. Partial review is not complete review; absence of a finding is not absence of a defect; “no issues found” is meaningful only within actual scope. Mutable labels, branch names, paths, and unversioned summaries do not replace pinned references. Material subject, evidence, method, scope, specialty, or uncertainty change may require reassessment.

## Review and execution authority traceability

Consequential review authority and the authority that governed the reviewed execution remain distinct where they arise from different Task Contracts or approved authority sources. A Review Record MUST preserve the identity and exact applicable revision of its review-authorizing Task Contract or other approved review authority. When reviewed claims, results, or evidence originate under a different execution-authorizing Task Contract, the identity and exact applicable revision of that execution authority MUST also remain traceable.

Review authority does not replace, amend, broaden, reinterpret, or supersede execution authority. Execution authority does not automatically authorize specialist review beyond its approved boundary. Review completion, a review finding, or a recommendation MUST NOT complete, accept, close, revoke, supersede, or otherwise transition either Task Contract. A Review Record MUST NOT retroactively authorize execution, evidence collection, access, disclosure, or review activity that lacked applicable authority when performed.

Where the relationship between review authority and execution authority is missing, conflicting, materially ambiguous, or affected by security or privacy risk, review MUST stop or escalate rather than infer authority. Exact authority-link encoding, delegation representation, review-assignment mechanisms, and lifecycle automation remain deferred.

## Execution Result, Evidence Bundle, and findings

An exact Execution Result Artifact Revision MAY be assessed. Result claims and findings remain separate; Review Record cannot modify, correct, supersede, accept, reject, approve, or replace the result. An exact Evidence Bundle revision MAY be assessed for relevance, provenance, integrity, authenticity, freshness, completeness, coverage, independence, reproducibility, uncertainty, limitations, conflict, bias, and sufficiency. Evidence assembly and review authorship remain distinguishable; overlap, conflict of interest, prior involvement, and material dependency remain visible. Required independence is controlled by governing authority and appropriate to risk.

Observation, interpretation, finding, supporting rationale, contradictory information, unresolved question, uncertainty, limitation, dissent, and recommendation remain distinct semantic responsibilities. Findings are traceable to subject, evidence, and method where material. Facts, interpretations, and recommendations are not silently merged; adverse findings, contradictions, unavailable, inaccessible, stale, redacted, excluded, and missing evidence remain visible. Direct and derived evidence remain distinct, copies or transformations are not independent corroboration, and machine output is not automatically specialist judgment.

## Recommendation, authority, and decisions

A recommendation is specialist and Evidentiary, not authoritative. It is not final approval, rejection, acceptance, integration, release, deployment, or merge. It MAY advise further evidence, correction, reassessment, acceptance, rejection, escalation, or deferral without a fixed enum. An Owner / Final Authority or authorized decision-maker may follow or reject it; any consequential decision remains separately authorized and, where required, recorded in a Decision Record. Review count, majority, score, tool, or automatic conflict resolution creates no decision. Self-approval and cyclic authority are prohibited.

Methods, checks, tools, and procedures are used only within authorized scope. Their outputs are bounded evidence: validation, schema validity, conformance, and tests do not automatically establish correctness, completeness, safety, acceptance, or approval. Procedures, toolchains, checklists, tests, and validator behavior remain deferred.

## Revision-aware correction and historical traceability

A material correction, supplementation, qualification, or replacement of a Review Record MUST produce a new Review Record Artifact Revision when consequential traceability requires it. The Review Record revision actually used for a review, decision, approval, rejection, integration, release, deployment, or merge assessment MUST remain historically traceable and MUST NOT be silently overwritten or replaced.

Evidence or information obtained after Review Record authoring remains recognizably later evidence. Later evidence MAY require reassessment or supplementation but MUST NOT be represented as having been available to the earlier reviewer. A later Review Record or correction MUST NOT retroactively authorize earlier unauthorized work or silently erase the uncertainty, limitations, dissent, or evidence gaps recorded in an earlier revision.

Stale, withdrawn, corrected, superseded, or otherwise non-current Review Record revisions MUST NOT be presented as current. Their prior use, provenance, applicable subject revisions, evidence revisions, findings, uncertainty, recommendation, and relationship to later revisions remain traceable subject to applicable retention, privacy, and security boundaries. Exact revision sequencing, correction markers, supersession encoding, freshness rules, and retention mechanisms remain deferred.

## Peer reviews, conflicting reviews, and synthesis

Each peer Review Record retains its own Artifact Instance Identifier, Artifact Revision, declared specialty, authority boundary, reviewed subjects, evidence basis, methods, findings, uncertainty, limitations, dissent, and recommendation. Peer Review Records MUST NOT be silently merged, collapsed, rewritten, or represented as one shared review.

Agreement between reviews does not constitute final approval. Disagreement does not constitute an authorized rejection. Review count, majority, reviewer ranking, confidence score, severity score, tool output, or apparent consensus grants no authority and does not resolve a consequential decision.

A review synthesis MAY be produced only under explicit bounded authority. It MUST provenance-preservingly identify every Review Record revision and other source used, preserve material agreement, disagreement, uncertainty, dissent, limitations, specialty boundaries, conflicts of interest, and unreviewed scope, and MUST NOT replace or erase the source Review Records. A synthesis remains Evidentiary and is not a Decision Record or final human decision.

Unresolved conflicting findings or recommendations remain explicit. Majority voting, weighting, automatic reviewer ranking, automatic synthesis, conflict resolution, and consensus algorithms remain deferred.

## Conformance, review outcome, and decision boundaries

Schema-valid does not automatically mean contract-conformant. Contract-conformant does not automatically mean correct, complete, safe, sufficient, current, accepted, integrated, released, deployed, or merged. Validation success, conformance claims, test results, reviewer credentials, review completion, or tool output grant neither task authority nor final approval.

A review-pass, favorable finding, or positive recommendation does not automatically constitute acceptance, integration authority, release authority, deployment authority, or merge authority. A review-fail, adverse finding, or negative recommendation does not automatically constitute an authorized rejection, revocation, rollback, or prohibition. Each consequential outcome requires the separate authority and decision required by applicable governance.

Satisfaction of acceptance criteria is evidence for an authorized acceptance decision, not the decision itself. Reviewer confidence, uncertainty assessment, severity assessment, recommendation, review status, or consensus is not approval state or Decision Record status. A Decision Record, where required, separately records the authorized consequential decision and its rationale. Final consequential authority remains human or explicitly human-governed.

Review Record, Evidence Bundle, Conformance Claim, Decision Record, final human approval, integration, release, deployment, and merge remain distinct. Exact conformance vocabularies, review outcomes, verdicts, scores, thresholds, decision matrices, and automated policy evaluation remain deferred.

## Roles, restricted evidence, and escalation

Owner / Final Authority remains human or explicitly human-governed. Specialist Reviewer remains the canonical author of a Review Record and acts only within declared specialty and explicit bounded authority. Lead Architect, Bounded Implementer, Execution Result author, Evidence Bundle assembler, Specialist Reviewer, peer reviewer, authorized decision-maker, approver, integrator, and Owner / Final Authority remain distinguishable responsibilities.

Participation in architecture, implementation, result authoring, evidence assembly, review, validation, or repository administration grants no automatic review, approval, acceptance, integration, release, deployment, or merge authority. Role overlap remains explicit and traceable, MUST NOT be represented as independence when it is not independent, and MUST NOT create self-approval, cyclic authority, or authority laundering.

This contract introduces no canonical Review Owner, Review Manager, Review Approver, Auditor Agent, Quality Gatekeeper, Review Bot, or Approval Agent role. Titles, credentials, repository rights, tools, assignments, automation, reviewer status, or organizational position do not create canonical authority.

Access to restricted evidence or source material is not authority to review, copy, transform, retain, disclose, publish, transmit, or redistribute it. Restricted evidence SHOULD be safely referenced rather than copied when provenance and reviewability can be preserved. Redaction and sanitization MUST keep provenance, material information loss, uncertainty, and limitations visible and MUST NOT silently change findings, dissent, recommendation, or apparent review outcome.

Missing or uncertain authority, access, provenance, scope, specialty, evidence integrity, privacy handling, security handling, conflict-of-interest handling, or redaction effects require bounded stop or escalation. Creating a Review Record does not legitimize unauthorized access, evidence handling, review activity, or disclosure. Exact access-control, redaction, secure-reference, escalation-level, and retention mechanisms remain deferred.

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
