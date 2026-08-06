# CNTX Common Artifact Envelope Representation Boundary (ARCH-005)

## Status and authority

Status: **Proposed**.

This document is a documentation-only architecture candidate prepared under issue #34 and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md). It is not binding unless the Owner / Final Authority accepts the exact reviewed revision and that revision is integrated under [GOVERNANCE.md](../../GOVERNANCE.md).

This candidate refines only the representation boundary established by accepted [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), [ARCH-003](artifact-contract-schema-architecture.md), and [ARCH-004](common-artifact-envelope-schema-boundary.md). It does not alter those sources, any accepted artifact contract, or final human authority.

Within this document, **MUST** and **MUST NOT** express mandatory requirements, **SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY** expresses permission. These terms describe the proposed boundary only while this document remains Proposed.

## Purpose and decision boundary

ARCH-004 decides which accepted concepts belong to common-envelope ownership. Before an executable Common Artifact Envelope can be proposed, CNTX also needs a stable answer to a narrower representation question: which owned concepts must a future common definition be capable of expressing, and under which activation conditions, without yet deciding their lexical or executable form?

This candidate defines **representation obligations**. A representation obligation means that a future executable common definition must preserve and expose the identified accepted meaning. It does not select a field name, key, alias, data type, nesting model, cardinality, ordering rule, default, identifier syntax, timestamp format, digest algorithm, schema language, dialect, serialization format, or validator behavior.

## Governing traceability

| Governing source | Constraint preserved by this candidate |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Human final authority, bounded tasks, evidence-before-claims, minimal context, canonical artifact responsibilities, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Artifact, contract, schema, status, implementation, digest, and provenance dimensions remain distinct; identifiers and versions do not grant authority or approval. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | The Common Artifact Envelope remains one shared Layer 3 definition above artifact-specific contracts and below accepted identity/versioning semantics; lower layers conform upward. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) | Universal, conditional, artifact-specific, and explicitly excluded ownership categories remain intact; common reference mechanics do not absorb artifact-specific relationship meaning. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Every canonical artifact retains its accepted purpose, classification, lifecycle participation, authority limits, relationships, and payload semantics. |
| Issue #34 | Work remains documentation-only and limited to the five-path ARCH-005 candidate; executable schemas and lower-layer mechanisms remain outside scope. |

## Representation model

The future Common Artifact Envelope must remain one independently reviewable common definition. Its representation model has two distinct dimensions:

1. **definition capability** — the common definition can express an accepted concept consistently across artifact types; and
2. **instance activation** — the concept is present for a particular Artifact Instance only when its universal or conditional rule and the applicable artifact contract require or permit it.

A capability requirement does not make every value present in every instance. A conditional concept does not become universal merely because the common definition can express it. An artifact-specific requirement may activate a common reference mechanism without transferring the relationship's meaning into the envelope.

## Universal-envelope representation obligations

The common definition must provide one shared representation capability for each universal-envelope concept below.

| Accepted concept | Proposed common representation obligation | Boundary retained |
| --- | --- | --- |
| **Artifact Type** | Represent which one of the accepted canonical artifact kinds the Artifact Instance instantiates. | The represented value identifies a kind; it does not define that kind, change its classification, or grant authority. |
| **Artifact Instance Identifier** | Represent the stable identity of one logical Artifact Instance across its revisions. | The identifier is distinct from path, title, revision, contract identity, schema identity, and implementation identity. |
| **Artifact Revision** | Represent the revision of the identified Artifact Instance used or asserted by the current representation. | Revision encoding, ordering, concurrency, and storage remain later decisions. |
| **Contract Definition Identifier** | Represent the stable identity of the artifact-specific normative contract governing the instance. | It is not the Artifact Instance Identifier or Schema Identifier. |
| **Contract Definition Version** | Represent the exact governing contract version together with its Contract Definition Identifier. | Version does not imply acceptance, compatibility, or authority. |
| **Provenance-reference capability** | Provide common mechanics capable of identifying a source and pinning the applicable source revision or definition version when provenance is asserted or required. | The applicable artifact contract still defines why the source matters, whether it is sufficient, and what authority or evidentiary role it has. |

The definition capability for these concepts is universal. Exact instance-level requiredness remains governed by accepted semantics and the future executable schema decision. No future schema may omit the capability merely because one artifact-specific schema currently has no observed example using it.

## Conditional-envelope representation obligations

Conditional concepts use the common definition only when their accepted activation condition is true.

| Accepted concept | Activation condition | Proposed representation obligation | Still deferred |
| --- | --- | --- | --- |
| **Schema Identifier and Schema Version** | An executable schema governs the represented Artifact Instance. | Represent the schema identity and exact schema version as one semantically coupled pin. | Initial schema identity/version assignment, lexical form, resolver behavior, and compatibility enforcement. |
| **Content Digest evidence** | A digest is deliberately asserted as integrity evidence. | Represent enough conceptual information to associate the digest evidence with its identified subject and declared digest method. | Algorithms, encoding, canonicalization, byte scope, requiredness, and verification behavior. |
| **Extension Module declarations** | A later accepted Extension Module is applicable and explicitly declared. | Reserve no concrete field now; a later Layer 5 decision must define the representation before this capability can be activated. | Namespaces, extension syntax, registry, unknown-extension handling, conflicts, discovery, and runtime behavior. |
| **Profile declarations** | A later accepted Profile is applicable and explicitly declared. | Reserve no concrete field now; a later Layer 5 decision must define the representation before this capability can be activated. | Profile identity, composition, negotiation, narrowing rules, packaging, and runtime behavior. |
| **Authoritative-source reference mechanics** | An accepted artifact-specific contract requires or permits an authoritative-source relationship. | Use common identity, revision, version, and provenance pinning mechanics for the referenced source. | Relationship role, direction, sufficiency, freshness, replacement, conflict, embedding, retrieval, and access behavior. |

An unmet activation condition must not be represented as a fabricated value. Placeholder identities, invented versions, empty authority claims, and synthetic provenance are not valid substitutes for absence or unresolved information.

## Semantic coupling and separation rules

The future common definition must preserve the following conceptual couplings without merging their distinct meanings:

1. An Artifact Revision is interpreted only in relation to its Artifact Instance Identifier.
2. A Contract Definition Version is interpreted only with its Contract Definition Identifier.
3. A Schema Version is interpreted only with its Schema Identifier.
4. A provenance or authoritative-source pin identifies both the referenced logical source and the applicable source revision or definition version when consequential traceability requires it.
5. Digest evidence identifies its subject and method context; a bare digest must not silently stand for identity, revision, provenance, authority, approval, or conformance.
6. Artifact Type identifies the canonical kind but remains separate from the governing contract pin and from the artifact-specific payload.

Coupling means that the concepts must be reviewable together where one is meaningless or unsafe without the other. It does not require one container, tuple, object, key layout, or serialization shape.

## Absence, inapplicability, and unresolved information

A future executable definition must not collapse these conceptual states when the distinction affects provenance or conformance:

- **not applicable** — the accepted activation condition does not apply;
- **not asserted** — the concept is permitted but no claim is made;
- **unresolved** — the concept should be known for the intended claim but cannot currently be established; and
- **known and represented** — the concept is asserted with the applicable identity, revision, version, or evidence context.

This candidate does not select null values, sentinels, omission rules, error objects, status fields, or another encoding for those states. Artifact-specific contracts and later schema decisions determine whether a distinction is required for a particular claim. The common envelope must not turn missing information into implied approval, trust, validity, freshness, or authority.

## Common envelope and artifact-specific payload

The future Schema Family must preserve an independently reviewable separation between the common envelope definition and each artifact-specific definition.

- The common envelope owns only the representation mechanics identified in the universal and activated conditional obligations above.
- The artifact-specific definition owns payload structure and the representation of its accepted responsibility, claims, rationale, findings, state, or task content.
- Artifact-specific schemas may constrain when a common capability is used, but they must not redefine the shared meaning of identifiers, revisions, versions, provenance pins, or digest evidence.
- The common definition must not absorb relationship purpose, role, direction, multiplicity, sufficiency, freshness, replacement, conflict, or authority semantics.
- Shared composition must not create a monolithic global artifact, require unrelated context, or copy authoritative source content into every downstream artifact.

The exact schema-composition mechanism, module layout, import syntax, resolution model, packaging, and publication process remain deferred.

## Concepts explicitly not represented as common-envelope authority

The Common Artifact Envelope must not represent the following as values capable of creating or changing their governed meaning:

- authority or permission;
- approval or acceptance;
- trust;
- canonical Authoritative, Evidentiary, or Derived classification;
- artifact or governance lifecycle state;
- Document Status;
- Implementation Version;
- contract conformance;
- schema validity; or
- merge, release, deployment, or execution authorization.

Other artifacts may record evidence or decisions about these concepts where their accepted contracts permit it. Such records remain artifact-specific and do not make envelope metadata an authority source.

## Contract-by-contract preservation check

| Accepted contract | Payload and relationship meaning that remains artifact-specific |
| --- | --- |
| [CONTRACT-001 — Project Charter](../contracts/project-charter-contract.md) | Enduring intent, approved scope, constraints, authority basis, and governing downstream relationships. |
| [CONTRACT-002 — Workstream](../contracts/workstream-contract.md) | Coordination scope, declared workstream state, dependencies, and Task Contract coordination meaning. |
| [CONTRACT-003 — Task Contract](../contracts/task-contract-artifact-contract.md) | Bounded objective, permissions, prohibitions, resources, governing authority, completion evidence, and stop conditions. |
| [CONTRACT-004 — Context Packet](../contracts/context-packet-contract.md) | Context selection, relevance, sufficiency, freshness, conflicts, omissions, and derived non-authoritative meaning. |
| [CONTRACT-005 — Execution Result](../contracts/execution-result-contract.md) | Performed work, task-governed result claims, limitations, incomplete work, and output interpretation. |
| [CONTRACT-006 — Evidence Bundle](../contracts/evidence-bundle-contract.md) | Evidence claims, quality, integrity, sufficiency, contradictions, limitations, and evidentiary interpretation. |
| [CONTRACT-007 — Review Record](../contracts/review-record-contract.md) | Review subject, specialty, findings, recommendation, uncertainty, dissent, and review provenance. |
| [CONTRACT-008 — Decision Record](../contracts/decision-record-contract.md) | Decision authority, considered evidence, rationale, effective scope, approval, amendment, and conflict resolution. |
| [CONTRACT-009 — State Snapshot](../contracts/state-snapshot-contract.md) | Snapshot scope, source interpretation, temporal meaning, freshness, staleness, replacement, uncertainty, and derived state. |

This check introduces no new artifact responsibility, relationship, field, or classification. Common identity and pinning mechanics support traceability; they do not replace the artifact-specific semantics above.

## Minimum schema-foundation decision order

Acceptance of this representation boundary would establish prerequisites, not implementation authority. Later work must remain separately bounded and should proceed in this order:

1. assign a stable Schema Identifier and initial Schema Version policy for the future common definition, consistent with ARCH-002;
2. select and govern the schema language and exact dialect, including how normative and implementation-specific capabilities are separated;
3. decide source layout, composition, resolution, packaging, and publication boundaries for the common definition;
4. propose the executable Common Artifact Envelope definition against this accepted representation boundary;
5. propose independently reviewable artifact-specific executable schemas against their accepted contracts;
6. define Serialization Bindings only where the executable schema does not itself fully determine the exchanged representation; and
7. define validators, fixtures, negative tests, and Conformance Claim evidence without treating validation as approval.

Schema identity/versioning and schema language/dialect must remain distinct, independently reviewable decisions even when one task identifies dependencies between them. No later item is authorized merely because this order is documented.

## Security and privacy boundary

A future public common definition must be usable without requiring secrets, credentials, personal data, production configuration, private paths, restricted source content, provider-specific data, or private implementation details.

Reference and provenance capabilities identify sources; they do not grant retrieval permission or require copying the referenced content. A public Artifact Instance may record a privacy-safe opaque reference only when the governing contract and applicable policy permit it. Digest evidence must not be treated as anonymization, access control, or permission to publish its subject.

This candidate defines no registry, resolver, discovery mechanism, access-control system, transport, storage, network behavior, or threat-response workflow.

## Review, approval, and conformance boundary

The same operational agent may prepare and architecturally review this candidate only under the disclosed role arrangement in issue #34. That combined operational role is not an independent third-party review and cannot provide final human approval.

Schema validity, contract conformance, evidence quality, review findings, acceptance, integration, release, and deployment remain distinct. Only the human Owner / Final Authority may accept the exact reviewed architecture revision under the applicable governance.

## Deferred and prohibited by this candidate

This candidate does not define or authorize concrete field names, aliases, keys, types, nesting, cardinalities, ordering, defaults, identifier syntax, revision syntax, timestamps, digest algorithms, canonicalization, schema identifiers or initial versions, schema language or dialect, executable schemas, serialization formats or bindings, templates, examples, payloads, fixtures, validators, conformance tooling, registries, discovery, negotiation, extension or profile mechanics, code generation, migrations, APIs, CLIs, workflows, engines, runtimes, providers, products, private implementations, or reference implementations.

## Continuing gate

While Proposed, this document is review material only. If accepted, it establishes only the concrete semantic representation boundary and decision order described above. It does not authorize the next task, assign ARCH-006, or permit executable schema work. Every later phase requires its own approved issue or Task Contract, explicit path allowlist, evidence, review, security/privacy assessment, and human decision.
