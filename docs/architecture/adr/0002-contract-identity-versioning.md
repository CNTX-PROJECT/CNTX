# ADR-0002: Contract Identity and Versioning Semantics

## Status

**Accepted.** Final human approval has been granted under [GOVERNANCE.md](../../../GOVERNANCE.md). On merge and publication to `main`, ADR-0002 is published as an accepted architecture decision.

## Context

The accepted [core architecture contract](../core-contract.md) establishes CNTX as a conceptual public-core foundation. Before future field-level schemas can be considered, CNTX needs a clear separation between a logical artifact and its content revision, governing contract version, schema version, document status, implementation version, optional content digest, and provenance reference. Without that separation, provenance, compatibility, review, migration, and conformance would be ambiguous.

This is documentation-only work. It must not select technology or introduce executable schemas, validators, registries, migration tooling, runtime behavior, or provider integrations.

## Decision

CNTX separates logical identity, Artifact Revision, Contract Definition Version, Schema Version, Document Status, Implementation Version, Content Digest, and Provenance Reference as defined in the accepted [contract identity and versioning contract](../contract-identity-versioning.md). It applies `MAJOR.MINOR.PATCH` semantics to accepted contract definitions and future executable schema definitions: MAJOR is breaking, MINOR is a backward-compatible addition or expansion, and PATCH is only a non-semantic correction or clarification that changes neither required behavior nor accepted meaning.

Identifiers are stable, namespaced, opaque, non-authoritative references. CNTX forbids silent mutation or reuse of accepted identities and versions. Consequential normative changes require explicit version assessment and an accepted Decision Record. Exact identifier encodings, generation algorithms, and executable schema fields remain deferred.

CNTX remains independent of providers, models, runtimes, transports, storage systems, and domains. Document Status remains a governance dimension, not a semantic version, and neither a version nor an identifier grants approval or authority.

## Consequences

Future conforming schema and implementation proposals must distinguish the identity and version dimensions identified here, state their supported contract or schema versions, and preserve traceable provenance. Compatibility cannot be inferred from a shared name or file path, and validation success does not itself prove compatibility or grant approval.

The separation supports bounded review and evidence without preselecting serialization, storage, registry, digest, or migration technology. ARCH-001 remains the accepted core baseline, and ARCH-002 is an accepted extension of that baseline.

## Rejected alternatives

- One generic `version` value for artifacts, schemas, contracts, and implementations, because it conflates independent meanings and compatibility obligations.
- Deriving identity from mutable names, paths, titles, or branch names, because these can change without preserving logical identity.
- Using a content hash as the sole logical identifier, because a digest evidences content but does not by itself preserve logical identity or authority.
- Using provider-specific identifiers as public-core identity, because that would violate provider independence.
- Silently changing accepted definitions without a version change and Decision Record, because consequential normative changes require traceable assessment and governance.

## Follow-up decisions

Future accepted decisions may address identifier encoding and generation; namespace registry governance; executable fields and schemas; canonical serialization and canonicalization; digest algorithms; revision concurrency semantics; detailed compatibility and migration rules; validators; supported-version negotiation; retention timeframes; and conformance testing. They MUST NOT preselect a technology or provider without an approved decision.
