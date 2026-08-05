# CNTX Decision Record Artifact Contract

**Status: Proposed.** This document is submitted for review under [GOVERNANCE.md](../../GOVERNANCE.md). It is not an accepted repository decision, does not itself grant approval, and is not binding until final human acceptance under governance and publication on `main`. It is subordinate to accepted ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-007. It specializes Decision Record semantics only and does not redefine the accepted architecture, identity/versioning, schema-layering, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, Evidence Bundle, Review Record, or final human authority. Executable schemas, validators, decision engines, approval systems, voting systems, workflows, runtimes, and implementations remain future work.

## Requirement language and authority

Within this proposed contract, **MUST** and **MUST NOT** express mandatory conceptual requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms grant no authority. This contract is read with [AGENTS.md](../../AGENTS.md), [GOVERNANCE.md](../../GOVERNANCE.md), [SECURITY.md](../../SECURITY.md), the accepted [core architecture contract](../architecture/core-contract.md), [contract identity and versioning contract](../architecture/contract-identity-versioning.md), and [artifact-contract and schema-layering contract](../architecture/artifact-contract-schema-architecture.md). Where sources differ, the applicable higher-authority source controls.

## Accepted governing meaning and classification

This contract refers to and specializes, without replacing or competing with, the accepted primary definition:

**Decision Record — Records an approved consequential decision and its rationale.**

The canonical responsibility is:

**Authorized decision-maker approves it; Lead Architect may author it.**

Decision Record is an **Authoritative** canonical artifact. An authoritative classification describes the role of a valid approved Decision Record within the accepted architecture; it does not make every draft, authored text, review, comment, commit, or publication authoritative. The exact Artifact Revision that carries the decision, its approval provenance, and its applicable scope determine whether it is the authoritative record.

## Purpose and scope

A Decision Record provides a bounded, traceable record of an approved consequential decision and the rationale for it. It makes the decision intelligible without converting the record into a work request, an execution report, a body of evidence, a review, a registry, or an automation mechanism. It records the decision within the authority, scope, and conditions that made it valid. Disclosure of a concrete Decision Record instance remains subject to valid authority, confidentiality, applicable public/private boundaries, and repository or project governance; a conforming instance need not be public.

A conforming Decision Record MUST identify, at a conceptual level:

- the consequential decision and its outcome;
- the decision-maker or decision authority that approved the exact record revision;
- the decision basis and rationale, including applicable governing sources;
- the bounded scope, effective conditions, and temporal applicability of the decision;
- applicable references to the artifacts, evidence, reviews, or prior decisions that informed it; and
- any explicit amendment, correction, revocation, supersession, dependency, or conflict relationship.

The record MUST remain sufficiently bounded that a reader can distinguish what was decided from the work that was proposed, performed, reviewed, evidenced, or later integrated.

One Decision Record governs exactly one coherent consequential decision boundary. It MUST NOT bundle unrelated decisions, and independently approvable decisions MUST be recorded separately. This is a semantic artifact boundary and does not prescribe a schema or cardinality decision.

## Non-goals and prohibited interpretations

A Decision Record MUST NOT:

- create, broaden, delegate, or retroactively infer decision authority;
- turn authorship, a recommendation, a review, evidence, a signature-like marker, a commit, merge, publication, or tool action into approval;
- make a decision effective outside its stated authority, scope, conditions, and temporal boundary;
- silently amend a governing Project Charter, Workstream, Task Contract, architecture contract, or another Decision Record;
- rewrite the content, provenance, status, or classification of a related artifact;
- prove acceptance, integration, release, deployment, publication, merge, implementation correctness, or policy compliance merely by existing;
- prescribe an executable schema, field layout, serialization, registry, validator, decision engine, approval system, voting system, workflow, runtime, storage, transport, provider, model, or domain-specific implementation;
- expose private deliberation, personal data, secrets, credentials, production configuration, or restricted source material in public documentation; or
- define the next artifact contract or State Snapshot semantics.

## Decision authority boundary

Only an authorized decision-maker may approve a consequential decision. The applicable higher-authority governing sources determine who that decision-maker is, which decision is within their authority, and what evidence or review is required. The Owner / Final Authority retains final human authority under governance; a lower artifact, a technical role, an automated system, or a repository operation cannot replace it.

The Lead Architect MAY author a Decision Record, but authorship is not approval. A reviewer MAY identify findings or make a recommendation, but a review is not approval. An evidence provider MAY supply evidence, but evidence is not approval. A contributor, agent, provider, model, service, platform, repository, branch, pull request, commit, merge, or publication MUST NOT be represented as an approving authority unless the applicable governing source expressly assigns that human decision authority and approval is attributable to it.

The decision authority boundary MUST be explicit enough to distinguish an authority to decide from an authority to prepare, review, publish, administer, or execute related work. A Decision Record cannot manufacture authority by reference, implication, majority, recency, or technical control.

## Approval of the exact Artifact Revision

Approval attaches to one identifiable Artifact Revision of a Decision Record, not to an unbounded title, artifact identity, branch, discussion, or future edit. The approved revision MUST be distinguishable from prior and later revisions by the accepted identity, versioning, and provenance model. Any material change after approval requires its own attributable approval or an explicit relationship that defines the permitted correction or amendment.

The approval provenance MUST make clear, at the conceptual level, who approved, what exact revision was approved, under which governing authority, and when or under which condition the approval became effective. A reference alone is insufficient when it cannot distinguish the exact revision. Approval of a Decision Record does not approve an unrelated revision of a Task Contract, Context Packet, Execution Result, Evidence Bundle, Review Record, or another Decision Record.

## Authorship, approval, and decision timing

Authorship time, review time, approval time, decision time, effective time, publication time, and implementation time are distinct temporal concepts. A record MAY be authored before it is approved; its documented decision MAY concern a prior, current, or contingent future state only when the stated authority and conditions support that interpretation. The record MUST NOT collapse these times into an unstated assumption.

If a decision is conditional, deferred, time-bounded, or effective only on a later event, the Decision Record MUST state that boundary. A later merge, publication, execution, release, deployment, or operational event does not alter timing semantics unless the approved record explicitly states the relationship and the higher governing sources permit it.

## Rationale and decision basis

The rationale MUST explain why the authorized decision-maker reached the documented outcome within the available scope. It SHOULD identify material trade-offs, constraints, alternatives, risks, and the governing sources that materially informed the decision, without exposing restricted deliberation or creating a private record in the public repository.

Rationale is explanatory, not a substitute for approval provenance. A concise rationale may be sufficient when it preserves the consequential basis; exhaustive narrative is not required. The decision basis MAY reference accepted architecture, applicable charter/workstream/task boundaries, evidence, review findings, prior decisions, or public external sources, provided that references remain attributable and do not silently elevate a non-authoritative source.

Material uncertainty and material dissent MUST remain visible in the record or traceable through an exact revision-pinned reference, and the record MUST show how the authorized decision-maker handled them. Approval MUST NOT retrospectively erase them. This does not require rewriting or duplicating Evidence Bundles or Review Records and MUST respect restricted deliberation, confidentiality, and applicable public/private boundaries.

## Evidence, review, and recommendation boundaries

[Evidence Bundle](evidence-bundle-contract.md) and [Review Record](review-record-contract.md) are **Evidentiary** artifacts. They MAY support, challenge, qualify, or contextualize a decision, but they do not make the decision, grant authority, or become authoritative merely because a Decision Record cites them.

A recommendation is a proposed conclusion or course of action. It is not an approved decision unless an authorized decision-maker approves the exact Decision Record revision. Review findings, PASS-like assessments, quality signals, conformance checks, and signatures or attestations have the same boundary: they may inform approval but MUST NOT be conflated with it. Evidence and review provenance SHOULD remain traceable so that the relation between the basis and the decision can be inspected without claiming that evidence itself is the decision.

## Governing work-boundary relationships

The [Project Charter](project-charter-contract.md), [Workstream](workstream-contract.md), and [Task Contract](task-contract-artifact-contract.md) remain distinct authoritative artifacts with their own meanings and lifecycles. A Decision Record MAY decide within their applicable boundaries, but it cannot silently create a new charter, mutate enduring intent, change workstream state, revise a task’s authorization, or retroactively authorize work that lacked approval when it occurred.

The canonical dependency direction remains:

**Project Charter → Workstream → Task Contract → Context Packet / Execution Result**

This direction describes governing and contextual relationships. A Decision Record may reference any applicable artifact in that direction, but the reference does not reverse dependencies, turn downstream material into a source of authority, or permit a lower artifact to redefine a higher one.

## Context Packet and Execution Result boundaries

[Context Packet](context-packet-contract.md) is **Derived**. It MAY supply bounded context used by an authorized decision-maker, yet it remains non-authoritative and is not approved by the decision. A Decision Record MUST NOT claim that approving the decision approves, freezes, or validates a Context Packet revision unless another governing source explicitly establishes that separate action.

[Execution Result](execution-result-contract.md) is **Evidentiary**. A Decision Record MAY accept, reject, qualify, or otherwise decide the disposition of an exact Execution Result revision within scope. The Decision Record MUST identify the relation without rewriting the result, treating the result as approval, or making a disposition apply to a different result revision by implication.

## Decision outcome and consequence

The outcome MUST state what was decided, including a clear affirmative, negative, qualified, conditional, deferred, or otherwise bounded disposition. Consequences MAY identify permitted next actions, constraints, dependencies, or obligations, but they MUST NOT broaden the approved scope or imply unapproved work.

Acceptance, integration, release, deployment, publication, and merge are separate states and actions. A Decision Record MUST specify any intended relationship to them rather than treating them as automatic consequences. Conversely, a merge or publication of a Decision Record does not prove that the decision’s operational consequence occurred. Where a separate authority is required for acceptance, integration, release, deployment, or merge, that authority remains required.

## Effective boundary, conditions, and temporal scope

Every decision has an effective boundary. The record MUST state the applicable scope, conditions, and temporal interpretation sufficiently to prevent accidental application to another artifact, revision, workstream, task, environment, audience, or time. A decision MAY be limited to a named Artifact Revision, a bounded task or workstream, a stated condition, or a defined interval.

Conditions and temporal bounds MUST be read narrowly. A decision that is effective only after a prerequisite, review, publication, or other event does not become effective before that condition. A decision that is limited to one circumstance MUST NOT be generalized to comparable circumstances without an explicit authorized decision. Absence of an expiry date does not authorize an inference that the decision changes higher authority or remains applicable after a stated supersession or revocation.

## Amendment, correction, revocation, and supersession

An amendment changes a prior decision’s substance within authorized scope. A correction fixes a non-substantive error without silently changing the approved decision. A revocation withdraws an applicable decision or its effect. A supersession replaces a prior decision with a later approved decision that explicitly identifies the relationship and scope of replacement.

Each relationship MUST be explicit, attributable, and tied to exact Artifact Revisions. A later authored, published, or more recent record is not automatically an amendment, correction, revocation, or supersession. A correction that affects substance, authority, rationale, outcome, conditions, scope, or effective time MUST be treated as a material change requiring appropriate approval. A Decision Record MUST preserve the provenance of the prior record rather than overwriting historical meaning.

## Conflicting Decision Records

Conflicting Decision Records MUST NOT be resolved by an implicit latest-wins rule, repository order, branch order, merge order, publication order, authorship identity, or tool behavior. A conflict requires an explicit, authorized resolution that identifies the relevant records, their exact revisions, the scope of conflict, and the resulting relationship.

Until resolved, the applicable higher-authority sources and explicit boundaries remain controlling. A record MAY declare a dependency, conflict, amendment, correction, revocation, or supersession relation to a peer Decision Record, but it MUST NOT silently merge their semantics or erase an unresolved conflict.

## Existing ADRs, issues, comments, pull requests, and commits

Existing architecture decision records, issues, comments, pull requests, and commits may provide provenance, context, discussion, evidence, or a publication trail. They are not automatically Decision Records and do not automatically possess a Decision Record’s authority, status, or lifecycle. An accepted ADR remains governed by its own accepted architecture meaning and must not be silently reclassified by this contract.

An issue or pull request may authorize or track work; a comment may express discussion, review, or approval evidence; a commit may identify a repository revision. None of these forms substitutes for an approved exact Artifact Revision unless the applicable governing source explicitly establishes that artifact and its attributable approval. Cross-references SHOULD be precise enough to avoid mistaking orientation information for an authority source.

## Roles, authority, and accountability

The authorized decision-maker is accountable for approving the consequential decision within their assigned authority. The Owner / Final Authority retains the final human authority established by governance. The Lead Architect may author the Decision Record and clarify architectural implications, but does not gain approval authority merely by authoring it. Contributors, reviewers, evidence providers, and operators remain accountable only for their distinct contributions and must not be presented as a substitute decision-maker.

The record MUST distinguish role from authority, and accountability from technical access. Delegation, if any, must be explicit in a higher-authority source; a Decision Record cannot assert a delegation that does not exist. The document also MUST NOT impose a private organizational structure, provider-specific role, or automated approver.

## Required artifact relationships

| Related artifact | Required conceptual relationship |
| --- | --- |
| Project Charter | Governing enduring intent and boundaries remain controlling; a Decision Record cannot silently amend or replace them. |
| Workstream | Applicable bounded scope and declared state may inform the decision; the record cannot silently mutate them. |
| Task Contract | Exact approved authority, scope, evidence and integration boundaries remain traceable; the decision cannot retroactively authorize work. |
| Context Packet | May supply Derived context used in decision-making; it remains non-authoritative and is not approved by the decision. |
| Execution Result | Exact result revision may be accepted, rejected, qualified or otherwise decided within scope; the record cannot rewrite the result. |
| Evidence Bundle | Exact evidence revision may support the rationale; evidence remains Evidentiary and is not the decision. |
| Review Record | Exact review revision may inform the decision; findings and recommendations remain Evidentiary and separate. |
| Peer Decision Record | May establish an explicit dependency, amendment, conflict or supersession relationship; no implicit merge or latest-wins rule applies. |
| State Snapshot | May derive orientation from integrated authoritative state after the decision; it cannot replace the Decision Record. |

These relationships are conceptual and do not prescribe references, identifiers, fields, queries, graph storage, or a runtime. They do not permit any related artifact to assume a Decision Record’s authority.

## Conceptual lifecycle

A Decision Record lifecycle is bounded by the following conceptual stages:

1. An applicable consequential decision need is identified within existing authority and scope.
2. The governing sources, affected artifacts, and decision boundary are identified.
3. A Lead Architect or other permitted author prepares a proposed record.
4. Relevant context, evidence, and review may be gathered without becoming approval.
5. The proposed outcome, rationale, conditions, and consequences are made inspectable.
6. The authorized decision-maker assesses the exact Artifact Revision under the applicable governance.
7. The authorized decision-maker approves, rejects, qualifies, defers, or requests revision; only attributable approval creates the approved decision.
8. The approved revision and its provenance are recorded or published through an authorized process.
9. Any separately authorized downstream acceptance, integration, release, deployment, merge, or execution action proceeds according to its own boundary.
10. Later amendment, correction, revocation, supersession, or conflict resolution is explicit, revision-specific, and attributable.

This lifecycle is not a workflow engine, a mandatory organizational process, or a claim that every stage is automated or public. It does not allow a proposed record to become accepted merely by moving through time or repository states.

## Identity, revision, version, and provenance

Artifact identity identifies the continuing Decision Record as a conceptual artifact. Artifact Revision identifies one exact content/provenance-bearing instance. Contract definition identity and version identify this governing specification; they are not the decision’s identity or revision. Document status identifies governance state and is not a semantic compatibility version. Implementation version, content digest, and provenance reference remain distinct concepts under ARCH-002.

An approval, amendment, correction, revocation, supersession, or conflict relation MUST be made against an exact Artifact Revision. A new revision does not inherit approval by default. A version label, a branch name, or a content digest may aid traceability but does not independently establish authority. Provenance SHOULD preserve references needed to understand the decision source, the approver’s authority, the approved revision, and relevant supporting artifacts without disclosing restricted material.

## Evidence, review, approval, and conformance

Evidence establishes or supports claims; review evaluates material against stated criteria; approval is an attributable exercise of authorized human decision authority; conformance assesses whether material meets an applicable contract. These are distinct. A conforming record is not necessarily approved. An approved record is not proof that every implementation is conforming. Review and evidence do not become authoritative by being cited.

Future schemas, validators, or implementations MAY assess conformance only after the applicable artifact contract is accepted and separately authorized. Such mechanisms MUST remain subordinate to this conceptual distinction and MUST NOT infer approval from format validity, test success, signed metadata, automation, or repository state.

## Public and private security boundaries

The public Decision Record contract and any public instance MUST NOT disclose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, sensitive deliberation, or domain-specific implementation details that cannot safely be public. A public rationale may summarize a protected basis at an appropriate level while preserving the boundary; it need not reproduce private evidence or discussion.

This contract remains model-independent, provider-independent, runtime-independent, transport-independent, storage-independent, serialization-independent, schema-language-independent, and domain-independent. It establishes no private decision registry, access-control design, retention schedule, communication channel, operational control, or implementation technology.

## Extensions and profiles

Future extensions or profiles MAY add bounded, explicitly named conventions only when they conform to applicable accepted higher-authority contracts and do not alter the canonical primary definition, authoritative classification, final human authority, approval boundary, provenance distinction, or public/private boundary. An extension or profile MUST state its scope, compatibility relation, and limitations.

An extension or profile MUST NOT silently redefine what counts as an approval, introduce a provider-specific authority source, create an implied latest-wins rule, or make a lower implementation layer authoritative. It does not become a replacement for this artifact contract unless separately accepted under governance.

## Deferred schema and implementation decisions

The following are expressly deferred: concrete field names, required/optional fields, identifier syntax, version syntax, serialization, file format, content digest algorithm, signature method, storage, transport, API, registry, query model, validator, decision engine, approval system, voting system, workflow, runtime, user interface, automation, integration behavior, and operational procedure.

Any future executable schema, profile, validator, binding, implementation, or publication mechanism MUST follow accepted ARCH-001, ARCH-002, ARCH-003, this contract once accepted, and separately authorized work. Such future work MUST NOT reinterpret this proposed document as existing implementation authority.

## Status and change boundary

As **Proposed**, this document records a candidate subordinate contract for review. It does not change the accepted architecture or accepted CONTRACT-001 through CONTRACT-007. Final human acceptance and publication on `main` are required before it can become binding. Until then, all existing accepted governing sources remain controlling.
