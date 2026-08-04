# CNTX Artifact Contracts

## Reading guide

The accepted architecture contracts in [the architecture directory](../architecture/README.md) are the higher normative basis for this directory. Artifact-specific contracts specialize the accepted canonical artifacts without redefining their primary meanings, classifications, authority model, lifecycle, identity and versioning semantics, provenance, or public/private boundaries.

Every artifact-specific contract MUST be Accepted before an executable schema for that artifact may be introduced. Document statuses use the existing [architecture status definitions](../architecture/README.md#document-status); this index does not establish a second status system. These documents are conceptual only: no executable schema, validator, template, runtime, or product functionality is implemented.

## Canonical artifact contracts

The following order follows the accepted dependency direction. Only Project Charter has a proposed artifact-specific contract; the remaining contracts are future work and have no placeholder files.

| Order | Canonical artifact | Artifact-contract status |
| --- | --- | --- |
| 1 | [Project Charter](project-charter-contract.md) | **Proposed** — CONTRACT-001 |
| 2 | Workstream | Future work |
| 3 | Task Contract | Future work |
| 4 | Context Packet | Future work |
| 5 | Execution Result | Future work |
| 6 | Evidence Bundle | Future work |
| 7 | Review Record | Future work |
| 8 | Decision Record | Future work |
| 9 | State Snapshot | Future work |

## Public-core boundary

Public contracts and related documentation MUST NOT expose secrets, credentials, personal data, production configuration, private paths, restricted source material, private project data, or private domain-specific implementation logic. Future artifact-specific work remains model-, provider-, runtime-, transport-, storage-, schema-language-, serialization-, and domain-independent unless a later accepted decision authorizes otherwise.
