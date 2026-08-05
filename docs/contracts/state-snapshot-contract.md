**Status: Accepted**

# CNTX State Snapshot Artifact Contract

This accepted, documentation-only contract is a binding subordinate specialization for the canonical State Snapshot. It is subordinate to accepted ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-008. It specializes State Snapshot semantics only; it does not redefine accepted architecture, any accepted artifact contract, final human authority, or the accepted public/private boundary.

## Requirement language and authority boundary

Within this accepted contract, **MUST** and **MUST NOT** express mandatory conceptual requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms do not authorize a task, approval, acceptance, human decision, integration, publication, merge, release, or deployment. This document cannot replace final human authority or any applicable governing source.

The contract is read with [AGENTS.md](../../AGENTS.md), [GOVERNANCE.md](../../GOVERNANCE.md), [SECURITY.md](../../SECURITY.md), accepted [core architecture](../architecture/core-contract.md), accepted [identity and versioning](../architecture/contract-identity-versioning.md), accepted [artifact-contract and schema layering](../architecture/artifact-contract-schema-architecture.md), and accepted CONTRACT-001 through CONTRACT-008. Where sources differ, the applicable higher-authority source controls.

## Canonical meaning and classification

The accepted primary definition is:

**State Snapshot — Summarizes compact current state for orientation and handoff.**

The accepted canonical responsibility is:

**An authorized process or role derives it; authoritative sources remain controlling.**

State Snapshot is a **Derived** canonical artifact. Derived means that it provides bounded orientation from sources; it is non-authoritative and non-evidentiary. It is not an approval, decision, task authorization, acceptance, or authority source. A State Snapshot cannot create authority by being authored, reviewed, committed, merged, published, or handed off.

## Purpose, scope, and exclusions

A State Snapshot summarizes the compact current state that a reader needs for orientation or a bounded handoff. It SHOULD select relevant minimum context while preserving material provenance, uncertainty, limitations, conflicts, omissions, and unresolved work. Compactness is not permission to erase a material boundary merely to make the snapshot appear self-contained.

A State Snapshot MUST NOT replace, amend, supersede, reinterpret, combine authoritative sources into a new apparently controlling source, or silently become a controlling source. It MUST NOT copy unrelated history, duplicate source material without need, conceal an ambiguity or stopped condition, or claim completeness, correctness, conformance, freshness, or currentness merely because it exists. It is not a substitute for opening the applicable authoritative sources and exact revisions.

## Authorized derivation and controlling sources

Only an authorized process or role may derive a State Snapshot within applicable scope. Technical capability to assemble, alter, distribute, store, or display a snapshot is not authority to produce an authoritative state, modify source state, decide a consequence, authorize work, or approve an action. The applicable governing sources determine the role, scope, and permissions, and final human authority remains unchanged.

Authoritative sources and their applicable exact revisions remain controlling at all times. If a snapshot conflicts with a controlling source, the source controls and the conflict MUST be visible rather than silently resolved. A copied statement, summary, reference, issue, comment, pull request, commit, merge, publication, or recommendation remains derived unless a separate applicable governing source gives it a different status.

## Source identity, provenance, and temporal context

A State Snapshot MUST make its relevant source identity and applicable exact revision, or the limitation preventing that identification, traceable at a conceptual level. It MUST preserve the relevant derivation context: source scope, provenance, dependencies, and temporal context. An optional content digest may assist identification, but does not establish authority, approval, or correctness.

Mutable labels, branch names, mutable file paths, publication order, unversioned summaries, or an unspecified notion of “current” or “latest” are not substitutes for an applicable exact revision. A snapshot MUST NOT treat a newer source, later timestamp, or repository position as automatically controlling. When a source cannot be pinned, the snapshot MUST say so and state the resulting uncertainty.

## Freshness, staleness, and relevance

Freshness, derivation time, source time, publication time, observation time, and any known-valid-through boundary are distinct concepts. A State Snapshot SHOULD state the temporal limitation relevant to its purpose, including the time or period to which reported state applies and the derivation time, and MUST distinguish information known to be current, possibly stale, demonstrably stale, or of unknown freshness when material. Its existence or recent generation does not prove freshness; a later snapshot does not automatically control, and absence of newer information does not prove that reported state remains current. A State Snapshot MUST identify known staleness, freshness uncertainty, or a missing temporal boundary when it materially affects interpretation. No inferred recency rule decides a conflict or makes a snapshot authoritative. This contract defines no concrete timestamp field or expiry algorithm.

Selection MUST remain relevant to the declared orientation or handoff scope. It MUST exclude unrelated context, private material, and excessive duplication, but it MUST NOT hide material source uncertainty, provenance, dependencies, limitations, omissions, conflicts, incomplete work, stopped conditions, unresolved decisions, or verification gaps.

## Reported state, claims, evidence, review, decisions, and integration

Reported state is an orientation summary, not proof of the underlying claim. An [Execution Result](execution-result-contract.md) may report an output and limitations, but neither it nor a snapshot proves completion or correctness. An [Evidence Bundle](evidence-bundle-contract.md) may provide evidence and provenance, but a snapshot is not evidence itself and cannot create evidence by referring to itself. A [Review Record](review-record-contract.md) may contain findings or recommendations, but a snapshot does not replace review.

A [Decision Record](decision-record-contract.md) records an approved consequential decision and its rationale at an exact applicable revision; its scoped decision authority remains authoritative. A State Snapshot may report a traceable relationship to that decision, but cannot cite itself as authority, convert reported status into acceptance or integration, or equate a commit, pull request, merge, publication, or public visibility with current authoritative state.

## Uncertainty and limitations

A State Snapshot MUST explicitly preserve material uncertainty and limitations, including missing or unavailable sources, unpinned revisions, omissions, conflicts, incomplete work, stopped conditions, unresolved decisions, and verification gaps. It SHOULD state the reason for a material omission when needed to avoid misleading interpretation. It MAY state that an assessment is unknown or incomplete. It MUST NOT imply that silence resolves a conflict, that absence proves a negative, or that a compact handoff proves its source state.

## Identity, revision, and replacement

Artifact identity identifies the continuing State Snapshot concept; Artifact Revision identifies one exact derived instance. Contract definition identity and version identify this governing specification, document status identifies governance state, implementation version is distinct, and provenance identifies derivation context. These concepts MUST NOT be collapsed. A substantive content change MAY require a new Artifact Revision under applicable governing rules and MUST NOT be silently folded into an existing revision.

A later State Snapshot does not silently replace an earlier one. Any dependency, replacement, correction, supersession, or conflict relation to a peer snapshot MUST be explicit, attributable, revision-specific, scoped, and traceable. Historical provenance MUST NOT be silently overwritten. No implicit `latest-wins` rule applies.

## Required artifact relationships

| Related artifact | Required conceptual relationship |
| --- | --- |
| [Project Charter](project-charter-contract.md) | Its enduring intent and governance boundaries remain controlling; a snapshot cannot amend or replace them. |
| [Workstream](workstream-contract.md) | It may supply relevant bounded state; a snapshot cannot mutate its state or scope. |
| [Task Contract](task-contract-artifact-contract.md) | It may identify task status and bounded authority; a snapshot cannot grant or alter task authority. |
| [Context Packet](context-packet-contract.md) | Both are Derived and may provide minimum context; neither replaces its controlling sources. |
| [Execution Result](execution-result-contract.md) | Its claimed output and limitations may be reported; a snapshot does not prove it complete or correct. |
| [Evidence Bundle](evidence-bundle-contract.md) | Its evidence status and provenance may be referenced; a snapshot is not evidence itself. |
| [Review Record](review-record-contract.md) | Its findings, recommendations, and limitations may be reported; a snapshot does not replace review. |
| [Decision Record](decision-record-contract.md) | An exact approved decision revision may be referenced; its scoped decision authority remains authoritative. |
| Peer State Snapshot | Dependencies, replacement, revisions, and conflicts must be explicit; no implicit recency or silent merge applies. |

These relationships are conceptual only. They do not prescribe identifiers, fields, references, queries, storage, or runtime behavior, and they do not change the accepted meaning of a related artifact.

## Conceptual lifecycle and handoff

The accepted lifecycle relation is:

**integration → compact state update**

This relation is conceptual. A State Snapshot may be derived after integration to orient later work; it does not integrate, prove integration, or establish that any separate lifecycle stage occurred. A partial, stopped, conflicted, or unresolved state MUST remain visible.

A snapshot may support handoff, but the handoff is not task authority. Future work requires its own applicable Task Contract and authorization. A handoff MUST remain bounded to relevant sources and resolvable revisions; it MUST NOT reproduce a full conversation, unrelated history, or private material merely to appear complete.

## Public, privacy, and security boundary

Public State Snapshots MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, private implementation logic, sensitive operational details, or other protected information. A public snapshot may state a limitation or refer to an authorized public-safe source without reproducing protected content.

This accepted contract remains model-independent, vendor-independent, runtime-independent, transport-independent, storage-independent, serialization-independent, schema-language-independent, and domain-independent. It establishes no provider-specific behavior, private implementation, or product assumption.

## Extensions and profiles

Future extensions or profiles MAY add explicitly named, bounded conventions only when they remain subordinate to applicable accepted higher-authority sources. They MUST identify their governing contract and governing contract version, and state their own identity, scope, compatibility, and limitations. They MUST preserve the canonical definition, Derived classification, source precedence, provenance, final human authority, and public/private boundary.

An extension or profile MUST NOT silently redefine canonical meaning, introduce a new authority source, create an implicit replacement rule, make a lower implementation layer controlling, or require private implementation behavior in the public core. It does not replace this contract unless separately accepted under governance.

## Deferred schema and implementation decisions

The following remain expressly deferred: concrete fields and their requiredness; identifier syntax; revision encoding; timestamps and freshness algorithms; serialization; file format; template or payload design; content-digest algorithm; registry; selector or retrieval system; validator; state engine; synchronization engine; workflow or automation; storage and transport; API or CLI; runtime; provider integration; user interface; domain-specific implementation; private reference implementation; migration and conformance tooling.

This accepted contract creates no schema or implementation authority. Any later concrete work requires an accepted applicable artifact contract and a separately authorized bounded task, and remains subordinate to the accepted architecture and governance.

## Status and change boundary

As **Accepted**, this document records a binding subordinate artifact-specific contract. It does not alter accepted ARCH-001 through ARCH-003 or accepted CONTRACT-001 through CONTRACT-008. The applicable authoritative sources remain controlling.
