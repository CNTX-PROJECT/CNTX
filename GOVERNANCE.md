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

## Escalation and conflicts

When authority, scope, safety, privacy, or a technical decision is unclear, stop the affected work and escalate it to the repository owner or maintainers. Conflicts are resolved by the final authority for the applicable decision class. Evidence and approved task contracts take precedence over assumption.

## Public-core boundary

CNTX remains independent of any specific AI model, provider, runtime, domain, or private implementation. Public work must not disclose private context, credentials, personal data, production configuration, or private reference implementations.
