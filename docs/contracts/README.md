# CNTX Artifact Contracts

## Reading guide

The accepted architecture contracts in [the architecture directory](../architecture/README.md) are the higher normative basis for this directory. Artifact-specific contracts specialize the accepted canonical artifacts without redefining their primary meanings, classifications, authority model, lifecycle, identity and versioning semantics, provenance, or public/private boundaries. The accepted Project Charter contract is the first accepted, binding subordinate specialization under ARCH-001, ARCH-002, and ARCH-003. The accepted Workstream contract is the second accepted, binding subordinate specialization, governed additionally by the accepted Project Charter contract. The accepted Task Contract contract is the third binding subordinate specialization, governed by ARCH-001, ARCH-002, ARCH-003, accepted CONTRACT-001, and accepted CONTRACT-002. The accepted Context Packet contract is the fourth binding subordinate specialization, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, and accepted CONTRACT-003. The accepted Execution Result contract is the fifth binding subordinate specialization, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, CONTRACT-003, and CONTRACT-004. The accepted Evidence Bundle contract is the sixth binding subordinate specialization, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-005. The accepted Review Record contract is the seventh binding subordinate specialization, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006. The accepted Decision Record contract is the eighth binding subordinate specialization, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-007.

Every artifact-specific contract MUST be Accepted before an executable schema for that artifact may be introduced. Document statuses use the existing [architecture status definitions](../architecture/README.md#document-status); this index does not establish a second status system. These documents are conceptual only: no executable schema, selector, retrieval system, permission engine, validator, template, workflow engine, project-management product, runtime, or product functionality is implemented.

## Canonical artifact contracts

The following order follows the accepted dependency direction. Project Charter is the first accepted artifact-specific contract. Workstream is the second accepted subordinate contract. Task Contract is the third accepted subordinate contract. Context Packet is the fourth accepted, binding subordinate contract. Execution Result is the fifth accepted, binding subordinate contract. Evidence Bundle is the sixth accepted, binding subordinate contract. Review Record is the seventh accepted, binding subordinate contract, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006. Decision Record is the eighth accepted, binding subordinate contract, governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-007. State Snapshot is the only remaining future-work contract and has no placeholder file. The canonical order does not authorize an executable schema, validator, engine, workflow, or implementation.

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
| 9 | State Snapshot | Future work |

## Public-core boundary

Public contracts and related documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. Under the current accepted architecture, public artifact-specific contracts remain model-independent, provider-independent, runtime-independent, transport-independent, storage-independent, schema-language-independent, serialization-independent, and domain-independent. An artifact-specific contract, extension, profile, or lower decision MUST NOT silently lift these higher architecture boundaries.
