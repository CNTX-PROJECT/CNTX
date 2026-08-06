# CNTX Common Artifact Envelope Schema Identity and Initial Version Policy (ARCH-006)

## Status and authority

Status: **Proposed**.

This document is a proposed, documentation-only architecture decision prepared under issue #36 and recorded by [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md). It does not become binding unless the human Owner / Final Authority accepts the exact reviewed candidate revision and the resulting decision is integrated under [GOVERNANCE.md](../../GOVERNANCE.md).

This proposal refines only the schema-identity and initial-version decision left open by accepted [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), [ARCH-003](artifact-contract-schema-architecture.md), [ARCH-004](common-artifact-envelope-schema-boundary.md), and [ARCH-005](common-artifact-envelope-representation-boundary.md). It does not alter those sources, any accepted artifact contract, or final human authority.

Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms express requirement strength only within this document.

## Purpose and decision boundary

ARCH-005 requires schema identity and initial version policy to be decided before schema language, dialect, composition, packaging, or an executable Common Artifact Envelope is proposed. This decision allocates one stable, technology-neutral logical identity for that future common definition and establishes how its first accepted version would enter the accepted schema-version line.

This is an identity and version **policy**, not an executable schema. It creates no machine-readable schema definition, active Schema Version, concrete identifier string, field, type, syntax, resolver, registry entry, serialization binding, validator, implementation, release, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Human final authority, bounded tasks, evidence-before-claims, canonical artifact responsibilities, minimal context, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Schema Identifier and Schema Version remain distinct from artifact, contract, status, implementation, digest, and provenance dimensions; identifiers are stable, namespaced, non-authoritative, and independent of technology. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | The Common Artifact Envelope remains one future Layer 3 common definition in a Schema Family; executable schemas and Serialization Bindings remain subordinate, separately reviewable layers. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) | The universal, conditional, artifact-specific, and excluded ownership categories remain intact; one common identity does not create a monolithic global schema. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) | Representation obligations, activation conditions, semantic couplings, absence distinctions, and the ordered decision gates remain unchanged. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Each canonical artifact retains its accepted purpose, classification, authority limits, relationships, lifecycle participation, and payload semantics. |
| Issue #36 | Work remains documentation-only and limited to the five-path ARCH-006 decision; all executable and lower-layer work remains prohibited. |

## Logical schema identity allocation

The future executable Common Artifact Envelope definition has exactly one logical Schema Identifier allocation:

| Identity property | Allocated value or rule |
| --- | --- |
| Logical namespace | **CNTX Public Core Schema Family** |
| Logical local identity | **Common Artifact Envelope** |
| Identified schema role | The one future executable common definition that implements the accepted Common Artifact Envelope boundary and representation obligations. |
| Allocation count | Exactly one logical schema identity for this common definition. |
| Current executable-definition state | No executable Common Artifact Envelope schema exists. |
| Current Schema Version | None. |
| Initial accepted version target | **1.0.0**, subject to separate proposal, review, and exact-revision human acceptance of a future executable definition. |

The logical namespace and logical local identity together constitute the technology-neutral identity allocation required before a future concrete Schema Identifier can be encoded. They are reviewable identity coordinates, not a URI, URN, URL, file path, filename, schema keyword value, registry key, resolver address, or serialization token.

A later separately accepted language, dialect, and publication decision MUST encode or bind a concrete Schema Identifier to this same logical identity without changing its meaning. Moving a file, changing a title, changing a publication location, selecting a syntax, or introducing a resolver MUST NOT silently create or replace the logical identity.

## Identity invariants

The Common Artifact Envelope logical schema identity:

1. MUST remain stable across all versions of the same logical executable definition, including a future MAJOR version;
2. MUST NOT be reassigned to a different schema role, artifact-specific definition, Extension Module, Profile, Serialization Binding, validator, or implementation;
3. MUST remain distinct from an Artifact Type, Artifact Instance Identifier, Contract Definition Identifier, Artifact Revision, Contract Definition Version, Schema Version, Document Status, Implementation Version, Content Digest, Provenance Reference, file path, branch, tag, release, or display title;
4. MUST NOT derive authority, approval, trust, conformance, lifecycle state, compatibility, or integration state from its name, encoding, location, version, or discoverability;
5. MUST remain model-, vendor-, runtime-, transport-, storage-, serialization-, product-, and domain-agnostic; and
6. MUST NOT contain or require secrets, credentials, personal data, private project data, production configuration, or private implementation detail.

Artifact-specific executable definitions will require their own separately governed Schema Identifiers. They may depend on the Common Artifact Envelope definition but MUST NOT reuse its identity for their artifact-specific payload or relationship semantics. The same separation applies to later Extension Modules, Profiles, Serialization Bindings, and independently governed shared components.

## Initial version policy

No active Schema Version exists under this decision because no executable Common Artifact Envelope schema exists. The value `1.0.0` is reserved only as the **initial accepted version target** for the first executable definition that is later shown to implement the accepted Common Artifact Envelope boundaries and is accepted through its own exact-revision human decision.

The following rules apply:

1. Candidate drafting, review corrections, and replacement commits before first acceptance do not create accepted Schema Versions and do not consume PATCH numbers. Git provenance identifies those candidate revisions.
2. The first accepted executable Common Artifact Envelope definition MUST use Schema Version `1.0.0`, unless a later accepted architecture decision explicitly supersedes this policy before that first schema acceptance.
3. CNTX repository descriptions such as `pre-alpha` and any future project release version are independent of this schema-version line. They do not require or imply an accepted `0.x` Common Artifact Envelope schema.
4. Acceptance of ARCH-006 does not itself assign Schema Version `1.0.0` to a schema, because there is no executable definition to version.
5. Once an exact executable definition is accepted as `1.0.0`, that versioned definition MUST be immutable. Any accepted change to it requires a new Schema Version, a compatibility assessment, traceable provenance, and the applicable Decision Record and human approval.
6. A version number MUST NOT grant Document Status, authority, approval, trust, conformance, release status, or deployment status.

## Version progression after the initial acceptance

After `1.0.0` exists as an accepted executable definition, the accepted ARCH-002 semantic version model governs the same logical Schema Identifier:

- **MAJOR** is required for an incompatible or breaking normative or structural change.
- **MINOR** is required for a backward-compatible normative or structural addition or expansion.
- **PATCH** is permitted only for a non-breaking, non-semantic correction or clarification that leaves required behavior and accepted data meaning unchanged.

A change to required behavior, accepted meaning, authority boundaries, privacy boundaries, provenance semantics, activation conditions, semantic coupling, or lifecycle obligations MUST NOT be classified as PATCH. Reviewers MUST disclose compatibility uncertainty rather than infer compatibility from a shared name, location, language, successful validation, or version prefix. Detailed compatibility rules for field addition, removal, requiredness, unknown values, defaulting, coercion, migration, and serialization remain deferred until concrete schema structure exists.

## Identity continuity and new-identity boundary

A later revision remains under this logical Schema Identifier when it continues to be the one Common Artifact Envelope executable definition governed by the same accepted Layer 3 role, even when the revision requires a new MAJOR Schema Version. A language or dialect upgrade, file relocation, packaging change, publication-address change, or serialization binding does not by itself create a new logical schema identity.

A new logical Schema Identifier requires a separate accepted decision that establishes a genuinely distinct, independently governed schema responsibility. A new identity MUST NOT be used merely to avoid a breaking-version assessment, discard provenance, evade deprecation obligations, or allow an artifact-specific definition to redefine the common envelope.

Whether multiple concrete dialect encodings are equivalent representations of one executable definition or distinct executable definitions remains a later language, dialect, composition, and packaging decision. This policy requires only that no later technology choice silently change or multiply the accepted logical identity.

## Dimension-separation matrix

| Dimension | What it identifies or records | What it does not establish |
| --- | --- | --- |
| Logical Common Artifact Envelope schema identity | The stable logical identity allocated by namespace and local identity in this decision. | A concrete lexical Schema Identifier, executable content, version, status, location, or authority. |
| Concrete Schema Identifier | A future technology-specific encoding or binding that identifies an executable schema definition. | Schema Version, Contract Definition identity, artifact identity, status, approval, or authority. |
| Schema Version | The semantic version of an executable schema definition. | Artifact Revision, Contract Definition Version, Document Status, Implementation Version, or acceptance. |
| Contract Definition Identifier and Version | The identity and semantic version of a normative contract definition. | The identity or version of an executable schema. |
| Artifact Instance Identifier and Artifact Revision | One logical artifact instance and the revision of that instance. | Its governing contract or schema identity and version. |
| Document Status | The governance state `Proposed`, `Accepted`, `Superseded`, or `Deprecated`. | Semantic compatibility or version progression. |
| Implementation Version | The version of a conforming implementation. | Contract or schema version, acceptance, or conformance by itself. |
| Content Digest | Optional evidence about exact bytes or canonicalized content. | Logical identity, version, provenance, authority, or approval by itself. |
| Provenance Reference | A pin to an identified source and applicable revision or definition version. | A substitute for the source, its accepted meaning, or human authority. |
| Path, filename, URL, branch, tag, or release | A mutable location or repository/publication coordinate. | Stable logical schema identity or governance status. |

## Reference and provenance consequences

Once an accepted executable schema exists, a consequential schema reference MUST identify the logical schema through its future concrete Schema Identifier and pin the exact Schema Version. A mutable path, filename, title, branch, tag, unversioned summary, or `latest` label MUST NOT silently replace that pin. A Content Digest MAY strengthen exact-content evidence but MUST NOT replace logical identity, Schema Version, provenance, acceptance, or authority.

Before an executable schema exists, references to this proposal MUST identify ARCH-006 and its applicable repository revision or governance state. They MUST NOT claim that a Common Artifact Envelope Schema Identifier or Schema Version is already active.

## Language, dialect, and publication handoff

The next separately authorized schema-foundation decision may evaluate schema language and dialect. Any such candidate MUST preserve this logical identity allocation and initial version policy while separately deciding:

- the concrete lexical Schema Identifier syntax and namespace encoding;
- language- or dialect-specific identity keywords and resolution behavior;
- equivalence or separation rules for multiple dialect representations;
- composition and packaging dependencies that must precede an executable definition; and
- publication and discovery behavior, if those concerns are placed in scope.

Those items are not decided here. No URI, URN, URL, path, filename, schema-language keyword, registry, resolver, or publication location is reserved by ARCH-006.

## Security and privacy boundary

The logical identity is intentionally public and generic. Future concrete identifiers, schemas, examples, registries, and provenance records MUST NOT expose secrets, credentials, personal data, private project data, production configuration, private paths, restricted sources, or private implementation detail. Identity, version, provenance, digest, schema validity, and publication MUST NOT be interpreted as trust, authorization, approval, endorsement, safety, or permission to access referenced material.

## Review, approval, and conformance boundary

The same operational agent may prepare and architecturally review this candidate only under the transparent role arrangement authorized in issue #36. Such a combined operational review is not independent third-party review and cannot provide final human approval. Only the human Owner / Final Authority may accept the exact reviewed architecture revision under the applicable governance.

Document review, schema validity, contract conformance, evidence quality, compatibility assessment, acceptance, integration, release, and deployment remain distinct. No identifier, version, digest, test, or validation result grants any of them automatically.

## Deferred and prohibited by this decision

This decision does not define or authorize a concrete or lexical Schema Identifier; URI, URN, URL, path, filename, schema keyword value, registry, resolver, or generation algorithm; concrete fields, aliases, keys, types, nesting, cardinalities, ordering, defaults, requiredness, or examples; schema language or dialect; executable schema; composition or packaging mechanism; serialization format or binding; content-digest algorithm or canonicalization; templates, payloads, fixtures, validators, conformance tooling, migration tooling, code generation, APIs, CLIs, workflows, engines, Layer 5 Extension Module or Profile mechanisms, runtimes, providers, products, private implementations, reference implementations, releases, or deployments.

## Continuing gate

Acceptance would establish only the technology-neutral logical schema identity and initial version policy described above. It would not create an executable schema or authorize the next task. Schema language and dialect remain the next candidate decision in the ARCH-005 order; composition and packaging remain a later separate gate before executable-definition work. Every later phase requires its own approved issue or Task Contract, authoritative baseline, explicit path allowlist, evidence, review, security/privacy assessment, and human decision.
