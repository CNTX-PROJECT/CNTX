# CNTX Artifact Contracts

Nine Accepted contracts describe the public records that carry CNTX work from
an agreed purpose to a bounded handoff. Start here when you want to understand
**what a record means** before looking at its schema or examples.

## The nine-record route

`Project Charter → Workstream → Task Contract → Context Packet → Execution Result → Evidence Bundle → Review Record → Decision Record → State Snapshot`

| You are looking for… | Start with… |
| --- | --- |
| Why the work exists | [Project Charter](project-charter-contract.md) |
| What one bounded task may do | [Task Contract](task-contract-artifact-contract.md) |
| What context was supplied | [Context Packet](context-packet-contract.md) |
| What happened and what supports it | [Execution Result](execution-result-contract.md) and [Evidence Bundle](evidence-bundle-contract.md) |
| What was reviewed or decided | [Review Record](review-record-contract.md) and [Decision Record](decision-record-contract.md) |
| A derived handoff view | [State Snapshot](state-snapshot-contract.md) |

**Next technical layer:** open the [schema index](../../schemas/README.md) only
after choosing the governing contract. Schemas check representation; they do
not replace contract meaning or human authority.

## Reading guide

The accepted architecture contracts in [the architecture directory](../architecture/README.md) are the higher normative basis for this directory. Artifact-specific contracts specialize accepted canonical artifacts without redefining their primary meanings, classifications, authority model, lifecycle, identity and versioning semantics, provenance, or public/private boundaries. CONTRACT-001 through CONTRACT-009 are **Accepted**, binding subordinate specializations in their canonical order. CONTRACT-009, the State Snapshot contract, is the ninth accepted, documentation-only specialization, governed by accepted ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-008. Its accepted status does not itself grant task, decision, approval, acceptance, integration, release, deployment, publication, or merge authority, and it does not change final human authority.

Every artifact-specific contract MUST be Accepted before an executable schema for that artifact may be introduced. Document statuses use the existing [architecture status definitions](../architecture/README.md#document-status); this index does not establish a second status system. These documents are conceptual only: no executable schema, selector, retrieval system, permission engine, validator, template, workflow engine, project-management product, runtime, or product functionality is implemented.

## Canonical artifact contracts

The following order follows the accepted dependency direction. Project Charter, Workstream, Task Contract, Context Packet, Execution Result, Evidence Bundle, Review Record, and Decision Record are the first eight accepted, binding subordinate contracts. [State Snapshot](state-snapshot-contract.md) is the ninth **Accepted**, binding subordinate contract and specializes derived orientation and handoff semantics only. All nine contracts are Accepted; no canonical artifact contract remains listed as future work. The canonical order and accepted status do not authorize an executable schema, template, payload, validator, registry, selector, engine, workflow, runtime, or implementation.

| Order | Canonical artifact | Artifact-contract status |
| --- | --- | --- |
| 1 | [Project Charter](project-charter-contract.md) | **Accepted** — CONTRACT-001 |
| 2 | [Workstream](workstream-contract.md) | **Accepted** — CONTRACT-002 |
| 3 | [Task Contract](task-contract-artifact-contract.md) | **Accepted** — CONTRACT-003 |
| 4 | [Context Packet](context-packet-contract.md) | **Accepted** — CONTRACT-004 |
| 5 | [Execution Result](execution-result-contract.md) | **Accepted** — CONTRACT-005 |
| 6 | [Evidence Bundle](evidence-bundle-contract.md) | **Accepted** — CONTRACT-006 |
| 7 | [Review Record](review-record-contract.md) | **Accepted** — CONTRACT-007 |
| 8 | [Decision Record](decision-record-contract.md) | **Accepted** — CONTRACT-008 |
| 9 | [State Snapshot](state-snapshot-contract.md) | **Accepted** — CONTRACT-009 |

## Public-core boundary

Public contracts and related documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. Under the current accepted architecture, public artifact-specific contracts remain model-independent, provider-independent, runtime-independent, transport-independent, storage-independent, schema-language-independent, serialization-independent, and domain-independent. An artifact-specific contract, extension, profile, or lower decision MUST NOT silently lift these higher architecture boundaries.
