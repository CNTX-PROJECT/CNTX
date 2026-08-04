# Governance

## Authority and roles

CNTX uses an owner/builder model. The repository owner and maintainers hold final authority for approval and merge. The lead architect provides architectural review and direction. Bounded implementation agents perform only explicitly authorized work. Specialist reviewers provide focused review when requested. No role replaces human final authority.

## Decision classes

| Decision class | Required authority |
| --- | --- |
| Routine implementation within an approved scope | Maintainer review and human approval before merge |
| Architecture, public contracts, or scope | Explicit owner/maintainer approval with lead-architect review as appropriate |
| Security or privacy | Private assessment and explicit maintainer decision |
| Release | Explicit owner/maintainer approval |

## Lifecycle

The normal lifecycle is: issue → scoped branch → implementation → evidence and validation → draft pull request → review → human approval → merge. Draft pull requests are not approval. Agents must not merge changes or expand scope autonomously.

## Transition and handoff discipline

When a bounded task is completed, or work transfers to another task, phase, role, agent, conversation, or execution environment, the responsible operational roles MUST provide a concise handoff summary. The Lead Architect preserves architectural direction and the authorized next-task boundary; the Bounded Implementer reports completed execution state, evidence, limitations, and unresolved work.

A handoff summary is derived orientation information only. It is not an authoritative Project Charter, Workstream, Task Contract, Decision Record, or State Snapshot; it grants no approval, task authority, integration authority, release authority, or merge authority; and it does not authorize the next task. A consequential next task still requires its own approved issue or Task Contract. Authoritative repository sources and exact revisions remain controlling.

Handoffs MUST transfer only minimum relevant context. Unrelated historical context MUST NOT be copied by default, and uncertainty, unresolved conditions, and prohibited scope MUST remain explicit. Public handoffs MUST NOT disclose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private implementation content. This discipline does not introduce a concrete schema, formal artifact instance, canonical role, lifecycle state, or automation requirement.

## Escalation and conflicts

When authority, scope, safety, privacy, or a technical decision is unclear, stop the affected work and escalate it to the repository owner or maintainers. Conflicts are resolved by the final authority for the applicable decision class. Evidence and approved task contracts take precedence over assumption.

## Public-core boundary

CNTX remains independent of any specific AI model, provider, runtime, domain, or private implementation. Public work must not disclose private context, credentials, personal data, production configuration, or private reference implementations.
