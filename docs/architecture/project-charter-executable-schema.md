# CNTX Project Charter Executable Schema Definition (ARCH-012)

## Status and authority

**Document Status: Accepted.**

This document is an Accepted executable-schema architecture decision governed
by [issue #48](https://github.com/CNTX-PROJECT/CNTX/issues/48) and recorded by
[ADR-0012](adr/0012-project-charter-executable-schema.md). Owner / Final
Authority acceptance of the exact reviewed candidate is recorded in issue
comment `5210242651`. On governed integration to `main`, the accompanying
[Schema Resource](../../schemas/project-charter/1.0.0/schema.json) becomes the
active Accepted Project Charter Schema Version `1.0.0` within this exact scope.

The same operational agent prepared and reviewed the exact candidate under the
transparent role arrangement authorized in issue #48. That review was not
independent third-party review and did not provide final human approval;
acceptance was given separately by the human Owner / Final Authority.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
expresses permission within this Accepted decision.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Project Charter
Artifact** identity, selects `1.0.0` as its inactive initial target, and fixes
the closed `envelope`/`payload` container and exact Common Artifact Envelope
dependency. Accepted
[ARCH-011](contract-definition-identity-version-binding.md) supplies the exact
Project Charter Contract Definition Identifier and Version. Accepted
[CONTRACT-001](../contracts/project-charter-contract.md) controls Project
Charter payload meaning.

This Accepted decision binds those prerequisites into the first
artifact-specific executable Schema Resource. It defines one complete Project
Charter instance shape, specializes the Accepted common envelope, and converts
only CONTRACT-001's semantic responsibilities into closed payload assertions.

It does not change CONTRACT-001, create or approve a charter instance, select
an artifact Serialization Binding, provide a validator or resolver, or
authorize the next artifact-specific schema.

## Governing traceability

| Governing source | Constraint preserved |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Bounded authority, evidence-before-claims, human final authority, and the public/private boundary. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Artifact, revision, Contract Definition, Schema, status, digest, implementation, and provenance dimensions remain distinct. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | CONTRACT-001 remains above and controls this executable schema; schema validity is narrower than contract conformance or approval. |
| [ARCH-004](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) | Common-owned fields stay in `envelope`; Project Charter meaning stays in `payload`. |
| [ARCH-005](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) | Capability, activation, semantic coupling, absence, and unresolved-information distinctions remain explicit. |
| [ARCH-006](common-artifact-envelope-schema-identity-version-policy.md) through [ARCH-009](common-artifact-envelope-executable-schema.md) | Draft 2020-12, exact resource identity, standalone resource composition, offline-first resolution, and the Accepted Common Artifact Envelope root remain unchanged. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) and [ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md) | The Project Charter logical identity, inactive `1.0.0` target, closed root, exact `/envelope` reference, independent versioning, and rollout order are preserved. |
| [ARCH-011](contract-definition-identity-version-binding.md) and [ADR-0011](adr/0011-contract-definition-identity-version-binding.md) | The exact Project Charter Contract Definition Identifier and Version are used without inventing new coordinates. |
| [CONTRACT-001](../contracts/project-charter-contract.md) | The payload implements only enduring intent, outcome, scope, governance, condition, information-boundary, downstream-expectation, and lifecycle responsibilities. |

## Primary standards basis

The language semantics are read from the public primary sources for
[JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12),
[Core](https://json-schema.org/draft/2020-12/json-schema-core),
[Validation](https://json-schema.org/draft/2020-12/json-schema-validation), the
[official default meta-schema](https://json-schema.org/draft/2020-12/schema),
and [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986).

Draft 2020-12 supplies the standard `$schema`, `$id`, `$ref`, `$defs`,
applicator, and validation-keyword semantics. The closed property models,
exact resource coordinates, one permitted external dependency, declaration-set
shape, prohibited dynamic surface, and non-authority boundaries are stricter
CNTX choices governed by the Accepted architecture and CONTRACT-001.

## Canonical identity, version, and repository path

| Dimension | Accepted value |
| --- | --- |
| Logical Schema Identity | CNTX Public Core Schema Family / Project Charter Artifact |
| Schema language | JSON Schema |
| Dialect | Draft 2020-12 |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0` |
| Schema Version | `1.0.0` |
| Canonical repository path | `schemas/project-charter/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Accepted under issue #48 and Owner acceptance comment `5210242651` |

The `$id` is an absolute, fragment-free, version-qualified HTTPS identity. It
is not a branch, tag, release, mutable retrieval coordinate, automatic network
instruction, artifact identifier, Contract Definition Identifier, approval,
or trust assertion. The corresponding repository path is a source coordinate,
not the identity itself.

Drafting and validation did not activate Schema Version `1.0.0`. The Owner /
Final Authority accepted the exact reviewed revision in issue comment
`5210242651`; governed integration to `main` makes that exact Accepted resource
active.

## Canonical full-artifact root

The root evaluates one complete Project Charter Artifact Instance. It is a
closed object with exactly two mandatory direct members:

1. `envelope`; and
2. `payload`.

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

- `artifactType` to `project-charter`;
- governing Contract Definition Identifier to
  `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/project-charter`;
- governing Contract Definition Version to `1.0.0`;
- governing Schema Identifier to
  `https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0`; and
- governing Schema Version to `1.0.0`.

The overlay relies on the common resource for type, requiredness, closure,
identifier/version lexical constraints, artifact identity, provenance
references, and content digests. It does not copy, fork, weaken, open, or
redefine the common resource. It does not reference a common internal `$defs`
member or use a moving, relative, dynamic, branch, tag, release, mirror, or
bundle-local coordinate.

Processors MUST receive or preload the exact common resource. The HTTPS-shaped
reference grants no automatic network access. Evaluation MUST fail if the
exact referenced resource is unavailable.

## Project Charter payload property model

The closed `payload` object contains exactly ten required properties. Each
property implements a responsibility already accepted in CONTRACT-001.

| Property | Concrete responsibility | Explicit non-meaning |
| --- | --- | --- |
| `purpose` | Enduring project purpose and intent as a non-blank statement. | Approval, task authority, implementation plan, or truth proof. |
| `outcomes` | Desired outcomes and project-level success direction. | KPI engine, volatile status, measurement implementation, or guarantee. |
| `scope` | Included scope, enduring boundaries, and explicit non-goals. | Workstream plan, task scope grant, or universal domain model. |
| `governingPrinciples` | One or more enduring declarative principles. | Executable policy or permission engine. |
| `materialConstraints` | Explicit specified constraints or an assessed-none declaration. | Legal-completeness or feasibility proof. |
| `governance` | Applicable governance context and final-authority role. | Approval evidence, appointment proof, or self-authorization. |
| `projectConditions` | Assumptions, dependencies, risks, and unresolved uncertainty. | Truth, probability, completeness, or automatic resolution. |
| `informationBoundaries` | Public-information and restricted-information handling boundaries. | Permission to disclose restricted content. |
| `downstreamExpectations` | Enduring expectations for Workstreams, Task Contracts, decisions, traceability, and change control. | Embedded downstream artifacts, workflow, or execution authority. |
| `lifecycleConditions` | Review, amendment, supersession, and retirement conditions. | State machine, transition engine, timestamp, or approval state. |

Every defined object is closed. Every ordinary string must contain at least one
non-whitespace character. Required statement arrays contain at least one
unique non-blank item. There are no defaults, coercion, implicit aliases, or
unknown payload fields.

## Outcome and scope structures

`outcomes` requires:

- `desired`: one or more unique non-blank outcome statements; and
- `successDirection`: one non-blank enduring success-direction statement.

`scope` requires:

- `included`: one or more unique included-scope statements;
- `boundaries`: one or more unique enduring-boundary statements; and
- `nonGoals`: one explicit declaration set.

These structures make CONTRACT-001 responsibilities reviewable without
selecting a domain-specific project template, metric system, schedule, or
execution mechanism.

## Governance and project conditions

`governance` requires a non-empty governance-context statement set and a
non-blank `finalAuthorityRole`. The role value allows a public-safe role or
opaque role identifier and does not require personal data. JSON Schema cannot
establish that the role is human, correctly appointed, applicable, or acting
within authority. A valid value does not approve the charter.

`projectConditions` requires explicit declarations for assumptions,
dependencies, risks, and unresolved uncertainty. Requiring every category to
be addressed prevents silent omission while the declaration-set model avoids
fabricated placeholder content.

## Declaration sets and absence semantics

A declaration set is exactly one of two closed forms:

1. `disposition: specified` with a non-empty unique `items` array; or
2. `disposition: none` with no `items` member.

`none` means only that the category was assessed for the represented revision
and no item is declared. It does not mean not reviewed, unknown, automatically
inapplicable, approved, complete, true, sufficient, risk-free, or permanently
absent. `disposition` is not a lifecycle state, Document Status, approval
state, authority claim, or runtime state.

The schema rejects null, empty objects, empty arrays, blank items, unknown
dispositions, `specified` without items, and `none` with items. It creates no
generic `N/A`, `unknown`, or `unresolved` sentinel. Unresolved uncertainty is a
specific CONTRACT-001 category whose declared items remain human-interpreted.

## Information and downstream boundaries

`informationBoundaries.publicInformation` describes the public information
boundary. `restrictedInformation` describes only public-safe categories,
limitations, reference rules, or handling boundaries. It MUST NOT copy
restricted content. A schema-valid instance can still violate privacy or
security policy; schema validity is not disclosure authority.

`downstreamExpectations` contains declarative expectations for Workstreams,
Task Contracts, consequential decisions, traceability, and change control. It
does not embed those artifacts or create their authority. No artifact-specific
Schema Resource is referenced other than the higher Common Artifact Envelope.

## Lifecycle boundary

Review, amendment, supersession, and retirement conditions are mandatory
declarative statement sets. They do not encode current lifecycle state,
approval state, timestamps, transition syntax, automation, or authority.
Only an explicitly approved Artifact Revision is authoritative under
CONTRACT-001; this schema does not determine or grant that approval.

## Resource composition and reference graph

The canonical document contains exactly one Schema Resource:

- `$schema` and `$id` occur once at the root;
- no nested `$schema` or `$id` exists;
- internal reusable schemas occur only under root `$defs`;
- internal `$ref` values are fragment-local;
- exactly one external `$ref` identifies the exact common root;
- no public `$anchor`, `$dynamicAnchor`, or `$dynamicRef` exists; and
- no artifact-to-artifact, cross-resource JSON Pointer, relative, or cyclic
  dependency exists.

Internal `$defs` names are implementation details of this resource. They are
not separately accepted identities or a public compatibility surface.

## Test evidence

The [non-normative test manifest](../../tests/schemas/project-charter/1.0.0/cases.json)
contains public-safe synthetic positive and negative cases. It covers the
minimal and fully specified payloads, Unicode content, common provenance and
digest capabilities, root and envelope specialization, every payload
responsibility, declaration-set errors, closure, lexical assertions, arrays,
and forbidden fields.

Expected validity is evidence only. The manifest is not a validator,
Serialization Binding, canonical charter, template, approval, conformance
claim, authority source, reference implementation, release, or deployment.

## Review, approval, and conformance boundary

Schema validity is narrower than CONTRACT-001 conformance. Evaluation cannot
determine whether statements are truthful, complete, sufficient, applicable,
safe, approved, or authoritative; whether a role is correctly appointed;
whether an identifier or revision exists; whether provenance is adequate; or
whether a consequential action is authorized.

The disclosed exact-head Architect review remains evidentiary and
non-independent. It did not activate Schema Version `1.0.0` or replace
attributable human Owner / Final Authority acceptance of the exact reviewed
revision, which is recorded separately in issue comment `5210242651`.

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

The Accepted resource makes a complete Project Charter structurally
evaluable, preserves the independently accepted common envelope, pins exact
governing definitions, closes the payload, and makes every CONTRACT-001
responsibility explicit.

The tradeoffs are deliberate:

- required structure increases reviewability but later semantic changes need
  a Schema Version assessment;
- non-blank strings remain lexically broad because public-core semantics are
  domain-independent;
- `none` requires explicit assessment but cannot prove that assessment was
  competent or complete;
- the final-authority role is representable but not machine-verifiable;
- no downstream artifact is embedded or executable-schema-referenced; and
- no complete serialized CNTX artifact format exists without a separately
  Accepted Serialization Binding.

## Rejected alternatives

- **Flat envelope and payload** — rejected because it erases the Accepted
  ownership boundary.
- **Optional `envelope` or `payload`** — rejected because ARCH-010 requires a
  complete canonical artifact root.
- **Unknown root or payload properties** — rejected because they could create
  unreviewed public semantics.
- **Copy or fork the common envelope** — rejected because common meaning and
  versioning must remain independently governed.
- **Reference common internal `$defs`** — rejected because they are not a
  public compatibility surface.
- **Moving, relative, or dynamic common references** — rejected because exact
  Accepted dependency identity and offline determinism are required.
- **Point `governingSchema` at the common schema** — rejected because it must
  identify the complete artifact-specific definition.
- **One schema or lockstep version for all artifacts** — rejected because the
  nine identities and versions are independent.
- **Arbitrary unstructured payload map** — rejected because CONTRACT-001
  responsibilities would not be reviewable or fail closed.
- **Empty arrays, blank strings, null, or `N/A` placeholders** — rejected
  because they collapse assessed absence, unresolved information, and missing
  content.
- **Approval, authority, or lifecycle-status payload fields** — rejected
  because the schema does not own or grant those meanings.
- **Mandatory personal name for final authority** — rejected because a public
  schema must not require personal data and cannot verify authority.
- **Embed Workstreams or Task Contracts** — rejected because upstream and
  downstream artifacts retain independent identity and authority.
- **Artifact-to-artifact schema references** — rejected because ARCH-010
  authorizes only the common resource as an initial external dependency.
- **Imply canonical JSON or another Serialization Binding** — rejected because
  the JSON-compatible instance model is not a byte-level binding.
- **Treat fixtures, validation, or review as acceptance** — rejected because
  final authority remains human and exact-revision-bound.
- **Automatically authorize Workstream schema work** — rejected because each
  artifact-specific schema requires a separate task and Owner gate.

## Deferred and prohibited scope

ARCH-012 does not define or authorize a concrete authoritative Project Charter
instance; Artifact Instance Identifier generation; Artifact Revision syntax or
sequencing; approval evidence or mechanism; signatures, verification, trust
stores, digest algorithms, encoding, or canonicalization; canonical artifact
JSON or any artifact Serialization Binding; artifact media type, transport,
storage, or archive; artifact-to-artifact schema references; a cross-artifact
shared resource; Extension Module or Profile mechanics; resolver, registry,
catalog, cache, mirror, redirect, automatic network access, Compound Schema
Document, or bundler implementation; validator selection or implementation;
validation-output contract; conformance tooling; code generation; migration;
templates; forms; APIs; CLIs; workflows; engines; schedulers; orchestrators;
runtimes; providers; products; private or reference implementations; releases;
tags; hosted publication; or deployment.

It changes no Accepted contract, architecture source, or Common Artifact
Envelope resource and authorizes no Workstream or later artifact-specific
schema.

## Continuing gate

This document, ADR-0012, the Schema Resource, and its tests are Accepted under
the exact-revision Owner / Final Authority decision recorded in issue comment
`5210242651`. Governed integration to `main` activates exactly Project Charter
Schema Version `1.0.0`. Acceptance and integration of ARCH-012 do not authorize
the next artifact-specific schema.
