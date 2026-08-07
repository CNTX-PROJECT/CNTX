# CNTX Workstream Executable Schema Definition (ARCH-013)

## Status and authority

**Document Status: Accepted.**

This document is an Accepted executable-schema architecture decision governed
by [issue #52](https://github.com/CNTX-PROJECT/CNTX/issues/52) and recorded by
[ADR-0013](adr/0013-workstream-executable-schema.md). The accompanying
[Schema Resource](../../schemas/workstream/1.0.0/schema.json) and
[synthetic test evidence](../../tests/schemas/workstream/1.0.0/cases.json) are
Accepted in the exact reviewed revision recorded by Owner / Final Authority
acceptance comment `5215029431`. On governed integration to `main`, Workstream
Schema Version `1.0.0` becomes active within this exact scope.

The same operational agent prepared and reviewed the exact candidate under the
transparent role arrangement authorized in issue #52. That review is not
independent third-party review and did not provide final human approval;
acceptance was given separately by the human Owner / Final Authority.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
expresses permission within this Accepted decision.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Workstream Artifact**
identity, selects `1.0.0` as its inactive initial target, and fixes the closed
`envelope`/`payload` container and exact Common Artifact Envelope dependency.
Accepted [ARCH-011](contract-definition-identity-version-binding.md) supplies
the exact Workstream Contract Definition Identifier and Version. Accepted
[CONTRACT-002](../contracts/workstream-contract.md) controls Workstream payload
meaning. Accepted [ARCH-012](project-charter-executable-schema.md) proves the
dependency-first artifact-specific pattern without becoming a Workstream
schema dependency.

This Accepted decision binds those prerequisites into one complete Workstream
Schema Resource. It specializes the Accepted common envelope, represents the
governing Project Charter as an opaque Artifact Instance/Revision pin, and
converts only CONTRACT-002's semantic responsibilities into closed payload
assertions.

It does not change CONTRACT-002, create or approve a Workstream instance,
allocate an Artifact Instance Identifier, sequence an Artifact Revision,
retrieve or validate a Project Charter, select an artifact Serialization
Binding, provide a validator or resolver, create a Task Contract, or authorize
the next artifact-specific schema.

## Governing traceability

| Governing source | Constraint preserved |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Bounded authority, evidence-before-claims, human final authority, and public/private boundaries. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Artifact, Revision, Contract Definition, Schema, status, digest, implementation, provenance, and declared-state dimensions remain distinct. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | CONTRACT-002 remains above this schema; schema validity is narrower than contract conformance or approval. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) through [ARCH-009](common-artifact-envelope-executable-schema.md) | Common-owned fields remain in `envelope`; Draft 2020-12, exact identity, standalone resource composition, offline-first resolution, and the Accepted common root remain unchanged. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) and [ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md) | The Workstream logical identity, inactive `1.0.0` target, closed root, exact common reference, independent versioning, and dependency-first rollout are preserved. |
| [ARCH-011](contract-definition-identity-version-binding.md) and [ADR-0011](adr/0011-contract-definition-identity-version-binding.md) | The exact Workstream Contract Definition Identifier and Version are used. |
| [ARCH-012](project-charter-executable-schema.md) and [ADR-0012](adr/0012-project-charter-executable-schema.md) | The Accepted Project Charter schema remains unchanged and is not referenced by this resource. |
| [CONTRACT-002](../contracts/workstream-contract.md) | The payload implements only Workstream purpose, scope, relationships, conditions, governance, decomposition, declared-state, assurance, and lifecycle responsibilities. |

## Primary standards basis

The language semantics are read from the public primary sources for
[JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12),
[Core](https://json-schema.org/draft/2020-12/json-schema-core),
[Validation](https://json-schema.org/draft/2020-12/json-schema-validation), the
[official default meta-schema](https://json-schema.org/draft/2020-12/schema),
and [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986).

Draft 2020-12 supplies the standard `$schema`, `$id`, `$ref`, `$defs`,
applicator, and validation-keyword semantics. The closed property models,
exact resource coordinates, single external dependency, declaration-set
shape, prohibited dynamic surface, and non-authority boundaries are stricter
CNTX choices governed by Accepted architecture and CONTRACT-002.

## Canonical identity, version, and repository path

| Dimension | Accepted value |
| --- | --- |
| Logical Schema Identity | CNTX Public Core Schema Family / Workstream Artifact |
| Schema language | JSON Schema |
| Dialect | Draft 2020-12 |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/workstream/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #52 and Owner acceptance comment `5215029431` |

The `$id` is an absolute, fragment-free, version-qualified HTTPS identity. It
is not a branch, tag, release, mutable retrieval coordinate, automatic network
instruction, Artifact Instance Identifier, Contract Definition Identifier,
approval, or trust assertion. The repository path is a source coordinate, not
the identity itself. Drafting, validation, review, and repository presence did
not activate the Schema Version. The Owner / Final Authority accepted the
exact reviewed revision in issue comment `5215029431`; governed integration to
`main` activates that exact resource.

## Canonical full-artifact root

The root evaluates one complete Workstream Artifact Instance. It is a closed
object with exactly two mandatory direct members: `envelope` and `payload`.

No parallel root member may represent authority, approval, lifecycle,
classification, relationship, provenance, digest, extension, profile,
transport, storage, implementation, signature, or runtime state. The common
and artifact-specific ownership boundary remains visible and independently
reviewable.

## Common Artifact Envelope composition

The schema applied at `/envelope` uses exactly one external static reference:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

That reference identifies the complete Accepted Common Artifact Envelope
Schema Version `1.0.0`. A local assertion overlay constrains only:

- `artifactType` to `workstream`;
- governing Contract Definition Identifier to
  `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/workstream`;
- governing Contract Definition Version to `1.0.0`;
- governing Schema Identifier to
  `https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0`; and
- governing Schema Version to `1.0.0`.

The common resource remains owner of type, requiredness, closure, lexical
constraints, Artifact Instance pins, provenance references, and content
digests. The overlay does not copy, fork, weaken, open, or redefine it; does
not reference its internal `$defs`; and uses no moving, relative, dynamic,
branch, tag, release, mirror, redirect, or bundle-local coordinate.

Processors MUST receive or preload the exact common resource. The HTTPS-shaped
reference grants no automatic network access. Evaluation MUST fail if the
exact referenced resource is unavailable.

## Governing Project Charter pin

`payload.governingProjectCharter` is a closed object containing exactly two
required non-blank opaque strings:

- `artifactInstanceIdentifier`; and
- `artifactRevision`.

These values preserve the CONTRACT-002 requirement for a resolvable governing
Project Charter identity and revision context without creating an executable
schema dependency. This resource contains no `$ref` to the Project Charter
schema, embeds no Project Charter, allocates no identifier, defines no revision
syntax or sequence, performs no retrieval, and cannot prove that the referenced
artifact exists, is Accepted, applies, or grants authority.

## Workstream payload property model

The closed `payload` contains exactly twelve required properties:

| Property | Concrete responsibility | Explicit non-meaning |
| --- | --- | --- |
| `governingProjectCharter` | Opaque governing Project Charter Artifact Instance/Revision pin. | Retrieval, embedded charter, schema dependency, existence, applicability, or approval proof. |
| `purposeAndContribution` | Workstream purpose and contribution to approved project intent. | Charter amendment, outcome guarantee, task plan, or execution authority. |
| `scopeAndGrouping` | Included scope, boundaries, non-goals, exclusions, and grouping rationale. | Project-scope expansion, automatic grouping, or task authorization. |
| `coordinationRelationships` | Material dependencies and interfaces with the charter, peers, and downstream Task Contracts. | Embedded artifacts, automatic resolution, or merged authority. |
| `governingPrinciples` | One or more enduring declarative principles. | Executable policy or permission engine. |
| `materialConstraints` | Specified constraints or explicit assessed absence. | Legal, feasibility, or completeness proof. |
| `workstreamConditions` | Assumptions, risks, uncertainty, and escalation conditions. | Probability, truth, resolution, or automatic escalation. |
| `governance` | Governance context, final-authority role, bounded delegation, and context isolation. | Approval evidence, appointment proof, personal-name requirement, or self-authorization. |
| `taskContractDecomposition` | Expectations and constraints for candidate Task Contracts. | A Task Contract, task authority, task list, or execution workflow. |
| `declaredState` | Current governed disposition and material coordination conditions. | Approval state, status vocabulary, state machine, timestamp, task progress, telemetry, or dashboard state. |
| `assuranceExpectations` | Decision, evidence, review, provenance, and change-control expectations. | Conformance proof, final approval, signature, or automated enforcement. |
| `lifecycleConditions` | Review, amendment, completion, closure, supersession, and retirement conditions. | Executable transition, automatic completion/closure, or approval mechanism. |

Every defined object is closed. Every ordinary string contains at least one
non-whitespace character. Required statement arrays contain at least one
unique non-blank item. There are no defaults, coercion, implicit aliases,
unknown payload fields, or embedded downstream artifacts.

## Scope, coordination, and condition structures

`purposeAndContribution` requires one non-blank `purpose` and one non-empty
unique `projectContribution` statement set.

`scopeAndGrouping` requires non-empty unique `included` and `boundaries`,
declaration-set `nonGoals` and `exclusions`, and a non-blank
`groupingRationale`.

`coordinationRelationships` requires declaration sets for
`materialDependencies`, `projectCharterInterfaces`,
`peerWorkstreamInterfaces`, and `downstreamTaskContractInterfaces`.

`workstreamConditions` requires declaration sets for `assumptions`, `risks`,
`unresolvedUncertainty`, and `escalationConditions`. Requiring each category
to be assessed prevents silent omission without fabricating placeholder data.

## Governance, decomposition, and declared state

`governance.context` and `contextIsolation` are non-empty unique statement
sets. `finalAuthorityRole` is a non-blank public-safe role or opaque role
identifier; the schema cannot prove appointment or authority.
`boundedDelegation` is a declaration set and cannot create delegation merely
by being present.

`taskContractDecomposition.expectations` is a non-empty unique statement set;
`constraints` is a declaration set. These values govern only candidate Task
Contract decomposition. An approved Task Contract remains the sole source of
task-level execution authority.

`declaredState.currentDisposition` is a non-blank human-interpreted statement,
not an enumerated vocabulary. `materialCoordinationConditions` is a
declaration set. Declared state remains distinguishable from Document Status,
approval state, Schema Version, Artifact Revision, task progress, volatile
observations, and State Snapshot freshness.

## Declaration sets and absence semantics

A declaration set is exactly one of two closed forms:

1. `disposition: specified` with a non-empty unique non-blank `items` array;
   or
2. `disposition: none` with no `items` member.

`none` means only that the category was assessed for the represented revision
and no item is declared. It does not mean not reviewed, unknown, automatically
inapplicable, approved, complete, true, sufficient, risk-free, or permanently
absent. `disposition` is not a lifecycle state, Document Status, approval
state, authority claim, or runtime state.

The schema rejects null, empty objects, empty arrays, blank items, duplicate
items, unknown dispositions, `specified` without items, and `none` with items.
It creates no generic `N/A`, `unknown`, or automatic sentinel.

## Assurance and lifecycle boundary

`assuranceExpectations` requires non-empty unique statement sets for
`consequentialDecisions`, `evidence`, `review`, `provenance`, and
`changeControl`.

`lifecycleConditions` requires non-empty unique statement sets for `review`,
`amendment`, `completion`, `closure`, `supersession`, and `retirement`.
These declarations cannot approve, complete, close, supersede, retire, or
otherwise transition a Workstream. Completion of known tasks does not
automatically satisfy Workstream completion conditions.

## Resource composition and reference graph

The canonical document contains exactly one Schema Resource:

- `$schema` and `$id` occur once at the root;
- no nested `$schema` or `$id` exists;
- internal reusable schemas occur only under root `$defs`;
- internal `$ref` values are fragment-local and start with `#/$defs/`;
- exactly one external `$ref` identifies the exact common root;
- no Project Charter or other artifact-specific Schema Resource is referenced;
- no public `$anchor`, `$dynamicAnchor`, or `$dynamicRef` exists; and
- no cross-resource JSON Pointer, moving reference, or cyclic dependency
  exists.

Internal `$defs` names are implementation details of this resource. They are
not separately accepted identities or a public compatibility surface.

## Test evidence

The [non-normative test manifest](../../tests/schemas/workstream/1.0.0/cases.json)
contains public-safe synthetic positive and negative cases. It covers assessed
and specified declaration sets, Unicode content, common provenance/digest
capabilities, root/envelope specialization, the twelve payload
responsibilities, the opaque Project Charter pin, closure, lexical and array
assertions, and forbidden fields or embedded artifacts.

Expected validity is evidence only. The manifest is not a validator,
Serialization Binding, canonical Workstream, template, approval, conformance
claim, authority source, reference implementation, release, or deployment.

## Review, approval, and conformance boundary

Schema validity is narrower than CONTRACT-002 conformance. Evaluation cannot
determine whether statements are truthful, complete, sufficient, applicable,
safe, approved, or authoritative; whether a role is correctly appointed;
whether a Project Charter pin exists or applies; whether declared state is
accurate; whether provenance is adequate; or whether a consequential action is
authorized.

The disclosed exact-head Architect review is evidentiary and non-independent.
It did not activate Schema Version `1.0.0` or replace separately attributable
human Owner / Final Authority acceptance of the exact reviewed revision,
which is recorded in issue comment `5215029431`.

## Security and privacy boundary

The schema, documentation, and tests MUST NOT contain secrets, credentials,
personal data, production configuration, private paths, restricted source
content, private project data, provider-specific requirements, product logic,
or private implementation detail.

URI syntax grants no retrieval permission. A processor MUST NOT access the
network merely because `$id` or `$ref` uses HTTPS. Validation success grants no
access, disclosure, trust, approval, acceptance, merge, release, or deployment
permission.

## Consequences and tradeoffs

The Accepted resource makes a complete Workstream structurally evaluable,
preserves the independent common envelope, pins exact governing definitions,
and makes every CONTRACT-002 responsibility explicit.

The tradeoffs are deliberate:

- required structure improves reviewability but later semantic changes need a
  Schema Version assessment;
- non-blank strings remain lexically broad because public-core semantics are
  domain-independent;
- an opaque Project Charter pin preserves traceability without proving or
  retrieving the referenced artifact;
- `none` requires explicit assessment but cannot prove competent completeness;
- `currentDisposition` remains human-interpreted rather than becoming a state
  machine;
- no Task Contract or peer Workstream is embedded or schema-referenced; and
- no complete serialized CNTX artifact format exists without a separately
  Accepted Serialization Binding.

## Rejected alternatives

- **Flat, optional, or open root** — rejected because it erases the Accepted
  container boundary or permits unreviewed semantics.
- **Copy or fork the common envelope** — rejected because common meaning and
  versioning remain independently governed.
- **Reference common internal `$defs` or use moving/dynamic references** —
  rejected because those internals are not a public compatibility surface and
  exact offline determinism is required.
- **Point `governingSchema` at the common schema** — rejected because it must
  identify the complete Workstream definition.
- **One schema or lockstep version for all artifacts** — rejected because the
  nine identities and versions are independent.
- **Reference the Project Charter Schema Resource** — rejected because the
  relationship is an artifact pin, not a structural schema dependency.
- **Embed a Project Charter, peer Workstream, or Task Contract** — rejected
  because each artifact retains independent identity, revision, and authority.
- **Arbitrary payload maps or unknown properties** — rejected because
  CONTRACT-002 responsibilities would not be fail-closed or reviewable.
- **Empty arrays, blank strings, null, or fabricated `N/A`** — rejected because
  they collapse assessed absence, unresolved information, and missing content.
- **Enumerated declared-state vocabulary or transitions** — rejected because
  CONTRACT-002 defers state names, encoding, transitions, timestamps, and
  automation.
- **Approval, authority, task-progress, lifecycle-status, or runtime fields** —
  rejected because this schema does not own or grant those meanings.
- **Mandatory personal names** — rejected because public schemas must not
  require personal data and cannot verify authority.
- **Imply canonical JSON or another Serialization Binding** — rejected because
  the JSON-compatible instance model is not a byte-level binding.
- **Treat fixtures, validation, or review as acceptance** — rejected because
  final authority remains human and exact-revision-bound.
- **Automatically authorize Task Contract schema work** — rejected because
  every later artifact-specific schema requires a separate task and Owner gate.

## Deferred and prohibited scope

ARCH-013 does not define or authorize an authoritative Workstream instance;
Artifact Instance Identifier generation; Artifact Revision syntax or
sequencing; Project Charter retrieval or validation; artifact-to-artifact
schema references; declared-state vocabulary, timestamps, transitions, or
automation; approval evidence; signatures; verification; trust stores; digest
methods; canonicalization; artifact Serialization Binding; canonical JSON;
YAML or CBOR; extension/profile mechanisms; resolver, registry, catalog,
cache, mirror, redirect, or network retrieval; Compound Schema Documents or a
bundler implementation; validator selection or implementation; validation
output contract; conformance tooling; code generation; migration; template;
form; API; CLI; workflow; engine; scheduler; orchestrator; runtime;
provider/product work; private/reference implementation; release; tag; hosted
publication; or deployment.

It changes neither CONTRACT-001 through CONTRACT-009 nor ARCH-001 through
ARCH-012, and it grants no Task Contract or later schema authority.

## Continuing gate

The exact reviewed candidate was accepted by the Owner / Final Authority in
issue comment `5215029431`. Governed integration to `main` activates exactly
Workstream Schema Version `1.0.0`. No Task Contract or later artifact-specific
schema is automatically authorized.
