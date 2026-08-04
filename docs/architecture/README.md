# CNTX Architecture

## Reading guide

[The core architecture contract](core-contract.md) is the accepted normative conceptual architecture baseline for CNTX. It specifies public-core concepts and constraints, not an executable architecture. [ADR-0001](adr/0001-public-core-boundaries.md) records the accepted decision that establishes the public-core boundary. [The contract identity and versioning contract](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) are accepted additions: ARCH-001 remains the accepted core baseline, ARCH-002 is an accepted extension of that baseline, and [the artifact-contract and schema-layering contract](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) are the accepted ARCH-003 extension of that baseline. The [`adr/`](adr/) directory is the location for architecture decision records. Accepted architecture governs the artifact-specific contracts listed in the [contract index](../contracts/README.md). CONTRACT-001, the Project Charter artifact contract, is Proposed and does not alter ARCH-001, ARCH-002, or ARCH-003 unless and until approved.

This architecture documentation is read with the repository [README](../../README.md), [agent instructions](../../AGENTS.md), [governance](../../GOVERNANCE.md), and [security policy](../../SECURITY.md). The README describes the project and its current status. `AGENTS.md` sets execution constraints and source precedence. `GOVERNANCE.md` assigns decision authority and approval. Normative architecture states what the public core requires conceptually; governance assigns who may approve it; implementation is future conforming work; and non-binding discussion is neither an approved decision nor an authority source.

No executable architecture, schema, runtime, provider integration, validator, or product functionality is implemented here.

## Document status

- **Proposed** — submitted for review and not yet an accepted repository decision.
- **Accepted** — approved under repository governance and adopted as a binding architecture decision or baseline.
- **Superseded** — replaced by a later accepted decision that identifies the replacement.
- **Deprecated** — retained for reference but discouraged for new use; it is not necessarily replaced.

## Future changes

Future architecture changes MUST start with an approved issue or task contract, identify their intended scope and affected documents, and receive the authority and review required by [governance](../../GOVERNANCE.md). An accepted architecture decision record MUST accompany a consequential architecture change when the core contract requires one. Until then, discussion and proposed documents do not alter accepted architecture.
