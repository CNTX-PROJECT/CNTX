# CNTX Contract Identity and Versioning Contract

## Status and authority

**Status: Proposed.** This document is submitted for review under [GOVERNANCE.md](../../GOVERNANCE.md). It has no accepted authority and does not alter the accepted [CNTX Core Architecture Contract](core-contract.md) unless final human approval is granted and it is merged to `main`.

Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms express requirement strength only within this document.

## Purpose and scope

This contract establishes the conceptual identity, revision, versioning, compatibility, and reference semantics required before CNTX field-level schemas can be designed. It applies to every canonical CNTX artifact and to future conforming schema definitions and implementations. It refines the public-core boundaries of the accepted [core architecture contract](core-contract.md) without selecting an implementation technology.

This contract does not define executable field-level schemas, a concrete serialization format, identifier-generation algorithms such as UUID, ULID, URI, or database keys, a central registry implementation, validators, migration tooling, compatibility engines, CLI or API behavior, or any storage, transport, runtime, provider, model, or domain selection.

## Distinct identity and version dimensions

The following are the primary definitions of the eleven identity and version concepts. They MUST remain distinct and MUST NOT be conflated.

| Concept | Primary definition | Distinction required |
| --- | --- | --- |
| **Artifact Type** | The canonical kind of an artifact, such as Task Contract or Evidence Bundle. | It identifies a kind, not a particular artifact instance or its content. |
| **Artifact Instance Identifier** | The stable identity of one logical artifact instance across its revisions. | It is not its revision, title, path, or governing contract or schema identity. |
| **Artifact Revision** | The version of the content or state of one artifact instance. | It is not a Contract Definition Version, Schema Version, or Implementation Version. |
| **Contract Definition Identifier** | The stable identity of a normative contract definition. | It is not the identifier of an artifact instance or an executable schema. |
| **Contract Definition Version** | The semantic version of a normative contract definition. | It is not Document Status, an artifact revision, schema version, or implementation version. |
| **Schema Identifier** | The stable identity of a future executable schema definition. | It is not a contract definition identifier or an artifact instance identifier. |
| **Schema Version** | The semantic version of a future executable schema definition. | It is not an Artifact Revision, Contract Definition Version, or Implementation Version. |
| **Document Status** | The governance state `Proposed`, `Accepted`, `Superseded`, or `Deprecated`. | It is not a semantic version and does not express compatibility. |
| **Implementation Version** | The version of a conforming implementation. | It is not a contract or schema version and does not establish acceptance. |
| **Content Digest** | Optional evidence about exact bytes or canonicalized content. | It is not by itself logical identity, authority, approval, or a version. |
| **Provenance Reference** | A reference that identifies a source artifact and the applicable version or revision used. | It is not an unversioned summary or a substitute for the referenced source. |

## Identifier invariants

Identifiers MUST be stable for the lifetime of the logical object they identify and unique within an explicitly declared namespace. They MUST be opaque to decision logic unless a future accepted contract explicitly defines semantics, and MUST NOT be silently reused for a different logical object.

An identifier MUST NOT derive authority, trust, approval, or lifecycle state from its format. It MUST NOT contain secrets, credentials, personal data, production configuration, or private implementation detail. It MUST remain independent of provider, model, runtime, transport, storage, and domain. Mutable names, labels, titles, file paths, branch names, and display text MUST NOT replace it.

Exact identifier syntax, namespace encoding, and generation algorithms remain deferred.

## Semantic version model

Accepted CNTX contract definitions and future executable schema definitions use `MAJOR.MINOR.PATCH` semantic versioning.

- **MAJOR** changes indicate an incompatible or breaking normative or structural change.
- **MINOR** changes indicate a backward-compatible addition or expansion that does not invalidate conforming consumers of the same major version.
- **PATCH** changes indicate only a non-breaking, non-semantic correction or clarification that does not change required behavior or accepted data meaning.

Status and semantic version MUST remain separate dimensions. Accepted contract or schema changes MUST NOT occur silently: every accepted normative change MUST receive the required Decision Record and a version assessment. A change to required behavior, meaning, authority, privacy boundaries, provenance semantics, or lifecycle obligations MUST NOT be classified as PATCH.

Consumers and implementations MUST declare the contract or schema versions they support. Compatibility MUST NOT be inferred merely because two versions share a name or file path. Exact textual prefixing, metadata fields, and serialization encoding remain future schema work.

## Artifact revision semantics

An Artifact Instance Identifier MUST remain stable across revisions of the same logical artifact. A content or state change MUST produce a new Artifact Revision when the applicable Task Contract or future schema requires traceability. Changing an artifact instance does not automatically change its governing Schema Version or Contract Definition Version, and changing a schema MUST NOT silently rewrite existing artifact history.

Prior revisions and their provenance MUST remain traceable according to applicable retention and privacy policy. Exact revision encoding, sequencing, concurrency control, and storage remain deferred.

## Compatibility classifications

- **Breaking** requires a new MAJOR version.
- **Backward-compatible** requires at least a new MINOR version when normative or structural capability expands.
- **Editorial/non-semantic** MAY use a PATCH version only when required behavior and accepted meaning remain unchanged.

Reviewers MUST report uncertainty rather than guessing compatibility. Validation success alone does not prove compatibility. Detailed rules for field addition, field removal, unknown fields, defaulting, coercion, and migration remain schema-level decisions.

## Provenance and reference pinning

Authoritative and evidentiary references MUST identify enough information to resolve the intended source, including, as applicable, an artifact or definition identifier, Artifact Revision, Contract Definition Version or Schema Version, provenance source, and optional Content Digest. A mutable label or unversioned summary MUST NOT silently substitute for an authoritative pinned reference. A Content Digest MAY strengthen evidence but MUST NOT by itself grant authority or approval.

## Status, authority, and approval

`Proposed`, `Accepted`, `Superseded`, and `Deprecated` are governance statuses, not semantic versions. A version number does not grant acceptance, and an accepted status does not eliminate version requirements. Version bumps, identifiers, digests, tests, and evidence do not grant approval. Final consequential approval remains human or explicitly human-governed under the accepted [core architecture contract](core-contract.md).

## Public-repository boundary

Public examples and identifiers MUST NOT expose secrets, credentials, personal data, private project data, production configuration, private paths, or domain-specific private implementation details.

## Deferred decisions

This contract does not decide concrete field names or field-level schemas; identifier encoding and generation algorithms; namespace registry format and governance; canonical serialization and canonicalization; digest algorithms; revision encoding and concurrency semantics; detailed compatibility rules by field operation; migration contracts and tooling; validator behavior; supported-version negotiation; deprecation and retention timeframes; or conformance test suites.
