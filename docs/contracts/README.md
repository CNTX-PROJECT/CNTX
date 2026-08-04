# CNTX Artifact Contracts

## Reading guide

The accepted architecture contracts in [the architecture directory](../architecture/README.md) are the higher normative basis for this directory. Artifact-specific contracts specialize the accepted canonical artifacts without redefining their primary meanings, classifications, authority model, lifecycle, identity and versioning semantics, provenance, or public/private boundaries. The accepted Project Charter contract is the first accepted, binding subordinate specialization under ARCH-001, ARCH-002, and ARCH-003. The proposed Workstream contract is the next subordinate specialization, governed additionally by the accepted Project Charter contract.

Every artifact-specific contract MUST be Accepted before an executable schema for that artifact may be introduced. Document statuses use the existing [architecture status definitions](../architecture/README.md#document-status); this index does not establish a second status system. These documents are conceptual only: no executable schema, validator, template, workflow engine, project-management product, runtime, or product functionality is implemented.

## Canonical artifact contracts

The following order follows the accepted dependency direction. Project Charter is the first accepted artifact-specific contract. Workstream is the next proposed subordinate contract. The remaining seven contracts are future work and have no placeholder files.

| Order | Canonical artifact | Artifact-contract status |
| --- | --- | --- |
| 1 | [Project Charter](project-charter-contract.md) | **Accepted** — CONTRACT-001 |
| 2 | [Workstream](workstream-contract.md) | **Proposed** â€” CONTRACT-002 |
| 3 | Task Contract | Future work |
| 4 | Context Packet | Future work |
| 5 | Execution Result | Future work |
| 6 | Evidence Bundle | Future work |
| 7 | Review Record | Future work |
| 8 | Decision Record | Future work |
| 9 | State Snapshot | Future work |

## Public-core boundary

Public contracts and related documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. Under the current accepted architecture, public artifact-specific contracts remain model-independent, provider-independent, runtime-independent, transport-independent, storage-independent, schema-language-independent, serialization-independent, and domain-independent. An artifact-specific contract, extension, profile, or lower decision MUST NOT silently lift these higher architecture boundaries.
