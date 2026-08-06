# CNTX Canonical Contract Definition Identity, Initial Version, and Source Binding (ARCH-011)

## Status and authority

**Document Status:** Proposed.

This document is a proposed, documentation-only architecture decision governed
by [issue #46](https://github.com/CNTX-PROJECT/CNTX/issues/46) and recorded by
[ADR-0011](adr/0011-contract-definition-identity-version-binding.md). Owner /
Final Authority creation authority is recorded in issue comment `5209713761`.
Creation authority, candidate provenance, review, mergeability, or publication
to a branch does not make this proposal Accepted or activate any allocation.

The same operational agent may prepare and review the exact candidate only
under the transparent role arrangement authorized in issue #46. That review is
not independent third-party review and cannot provide final human approval.
Only the human Owner / Final Authority may accept the exact reviewed revision.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
expresses permission. These terms express requirement strength only within the
scope of this proposed decision.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
requires a future artifact-specific Schema Resource to identify the applicable
artifact-specific Contract Definition and exact Contract Definition Version in
`envelope.governingContract`. It also forbids a later executable-schema task
from inventing those coordinates. Accepted
[ARCH-002](contract-identity-versioning.md) defines the conceptual dimensions
but intentionally defers exact identifier syntax and allocation.

This proposal closes that prerequisite for the nine existing Accepted artifact
contract definitions. It allocates exactly one stable Contract Definition
Identifier and one initial Contract Definition Version for each, and binds each
pair to its exact Accepted public source at the authoritative baseline.

This decision changes no accepted artifact-contract meaning. It creates no
artifact instance, executable artifact-specific schema, payload, Serialization
Binding, resolver, registry service, validator, runtime, implementation,
release, hosted publication, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this proposal |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Human final authority, bounded work, evidence-before-claims, canonical artifact responsibilities, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Contract Definition Identifier and Version remain distinct from artifact, schema, revision, status, implementation, digest, and provenance dimensions; identifiers remain stable, namespaced, non-authoritative, and reusable only for the same logical definition. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | Artifact-specific normative contracts remain above and control their future executable schemas; schemas cannot replace their meaning or authority. |
| [ARCH-009](common-artifact-envelope-executable-schema.md), [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md), and [Common Artifact Envelope Schema Version `1.0.0`](../../schemas/common-artifact-envelope/1.0.0/schema.json) | `governingContract` remains a coupled stable identifier and exact semantic version pin. Its lexical validity does not prove existence, applicability, conformance, acceptance, or authority. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) and [ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md) | Nine artifact-specific schema identities, independent version lines, the closed `envelope`/`payload` root, the exact common-envelope dependency, and the payload ownership boundary remain unchanged. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | All nine existing definitions retain their Accepted purpose, classification, responsibilities, relationships, lifecycle, provenance, privacy, payload meaning, dependency direction, and authority limits. |
| [Issue #46](https://github.com/CNTX-PROJECT/CNTX/issues/46) | Work remains Proposed, documentation-only, limited to five public paths, and stops after one transparently non-independent exact-head COMMENT review. |

## Canonical Contract Definition Family

CNTX allocates the logical namespace **CNTX Public Core Contract Definition
Family**. Within that namespace, each of the nine canonical artifact contracts
has one independently governed normative Contract Definition identity.

The family is an organizational allocation, not a tenth Contract Definition,
an artifact, an executable schema, a registry service, a release unit, or a
lockstep version line. Family membership does not let one contract redefine
another or reverse the Accepted dependency direction.

## Exact nine-definition allocation

| Contract | Artifact Type | Contract Definition Identifier | Initial Contract Definition Version | Exact canonical source at baseline |
| --- | --- | --- | --- | --- |
| CONTRACT-001 | Project Charter | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/project-charter` | `1.0.0` | [`docs/contracts/project-charter-contract.md`](../contracts/project-charter-contract.md) |
| CONTRACT-002 | Workstream | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/workstream` | `1.0.0` | [`docs/contracts/workstream-contract.md`](../contracts/workstream-contract.md) |
| CONTRACT-003 | Task Contract | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/task-contract` | `1.0.0` | [`docs/contracts/task-contract-artifact-contract.md`](../contracts/task-contract-artifact-contract.md) |
| CONTRACT-004 | Context Packet | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet` | `1.0.0` | [`docs/contracts/context-packet-contract.md`](../contracts/context-packet-contract.md) |
| CONTRACT-005 | Execution Result | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/execution-result` | `1.0.0` | [`docs/contracts/execution-result-contract.md`](../contracts/execution-result-contract.md) |
| CONTRACT-006 | Evidence Bundle | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/evidence-bundle` | `1.0.0` | [`docs/contracts/evidence-bundle-contract.md`](../contracts/evidence-bundle-contract.md) |
| CONTRACT-007 | Review Record | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/review-record` | `1.0.0` | [`docs/contracts/review-record-contract.md`](../contracts/review-record-contract.md) |
| CONTRACT-008 | Decision Record | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/decision-record` | `1.0.0` | [`docs/contracts/decision-record-contract.md`](../contracts/decision-record-contract.md) |
| CONTRACT-009 | State Snapshot | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/state-snapshot` | `1.0.0` | [`docs/contracts/state-snapshot-contract.md`](../contracts/state-snapshot-contract.md) |

While this document is Proposed, the table records proposed coordinates only.
The nine pairs become Accepted and active only if the exact reviewed candidate
receives separate Owner / Final Authority acceptance, status-only promotion,
and governed integration to `main`.

## Identifier namespace and lexical binding

Each allocated identifier is an absolute, fragment-free HTTPS URI under the
publicly attributable `github.com/CNTX-PROJECT/CNTX/contract-definitions/`
namespace. Its final path segment provides a human-reviewable local allocation,
but consumers MUST treat the complete string as an opaque Contract Definition
Identifier unless a later Accepted contract defines additional semantics.

The identifier is version-independent. Contract Definition Version is carried
as the distinct paired value required by the Common Artifact Envelope. A
version number, mutable branch, tag, release, `latest` alias, filename, or
source-document path MUST NOT be inserted into or silently substituted for the
allocated identifier.

The HTTPS scheme does not authorize or require network access. The identifier
remains the identity coordinate even if its text is not dereferenceable, if the
public source is mirrored or relocated, or if GitHub is unavailable. A resolver
MUST NOT infer permission, trust, acceptance, or authority from the identifier.

## Identity invariants

Each allocated Contract Definition Identifier:

1. MUST identify exactly one normative Contract Definition line;
2. MUST remain stable across versions of the same normative responsibility,
   including future MAJOR versions;
3. MUST remain unique within the CNTX Public Core Contract Definition Family;
4. MUST NOT be reassigned to a different artifact contract, schema, extension,
   profile, binding, validator, implementation, or artifact instance;
5. MUST remain distinct from Artifact Type, Artifact Instance Identifier,
   Artifact Revision, Schema Identifier, Schema Version, Document Status,
   Implementation Version, Content Digest, Provenance Reference, source path,
   branch, tag, release, and display title;
6. MUST NOT derive authority, trust, approval, lifecycle, compatibility,
   conformance, acceptance, release, deployment, or access permission from its
   syntax, version, location, discoverability, or apparent ownership; and
7. MUST NOT contain or require secrets, credentials, personal data, private
   project data, production configuration, or private implementation detail.

A new Contract Definition Identifier requires a separately Accepted decision
that establishes a genuinely distinct normative responsibility. A new identity
MUST NOT be used merely to avoid a breaking-version assessment, discard
provenance, or evade deprecation or compatibility obligations.

## Initial Contract Definition Version allocation

The initial Contract Definition Version for every allocation is `1.0.0`. CNTX
repository maturity, pre-alpha wording, release numbering, and implementation
versions remain independent and do not require a `0.x` definition line.

Candidate drafting, review corrections, replacement commits, and review before
first exact-revision acceptance are provenance events. They do not create an
Accepted Contract Definition Version and do not consume PATCH numbers.

If this exact proposal is later Accepted, promoted, and integrated, each
existing Accepted source identified in the allocation table becomes the active
initial Contract Definition Version `1.0.0` under its own stable identifier.
Activation changes neither the previously Accepted contract meaning nor its
authority classification.

## Exact Accepted-source binding

Each proposed `1.0.0` allocation binds to the exact content of its canonical
source path in public repository commit
`27b022d8d83df2d60f45762579d8c5a1c8257f37`. That commit has tree
`d9d188f279b8ff5391a15ece2e4a8147b7bc8386`.

The Contract Definition Identifier and Version identify the logical normative
definition and semantic version. Repository identity, exact commit, and source
path provide provenance sufficient to locate the intended public source
revision. Those provenance coordinates do not replace the logical identifier
or semantic version and do not grant approval independently.

A mutable path, branch, title, alias, release, `latest` label, or unversioned
summary MUST NOT replace this exact binding. This decision selects no digest
algorithm, canonicalization method, signature, verification process, or trust
store. It creates no duplicate or versioned contract-document copy, and it
changes none of the nine canonical contract source files.

After acceptance, the normative meaning bound to a Contract Definition Version
is immutable. A later Accepted normative or editorial change requires a
compatibility assessment, the applicable new semantic version, traceable
provenance, review, and human approval. Moving a source path without changing
normative meaning does not by itself change identity or semantic version, but
the canonical-source provenance must be updated through separately governed
work and cannot rewrite the historical `1.0.0` binding.

## Version progression and dependency consequences

The nine version lines progress independently. There is no family-wide version,
lockstep increment, or automatic propagation.

- **MAJOR** is required for an incompatible or breaking normative change.
- **MINOR** is required for a backward-compatible normative addition or
  expansion.
- **PATCH** is permitted only for a non-breaking, non-semantic correction or
  clarification that leaves required behavior and Accepted meaning unchanged.

A change to required behavior, meaning, authority, privacy, provenance,
lifecycle, classification, or dependency obligations MUST NOT be PATCH. A
change to one definition does not automatically increment another, but impact
on dependants MUST be assessed in the Accepted contract dependency direction.
Reviewers MUST expose uncertainty rather than infer compatibility from a shared
name, path, version prefix, successful validation, or unchanged schema.

## Dimension-separation and non-authority boundary

Contract Definition identity/version, Schema identity/version, Artifact Type,
Artifact Instance identity/revision, Document Status, approval state,
Implementation Version, Content Digest, Provenance Reference, release, and
deployment remain distinct.

The `governingContract` pair declares which normative definition and exact
version an Artifact Instance claims to use. A syntactically valid or correctly
allocated pair does not prove that the definition exists at runtime, applies to
the instance, is Accepted in the consumer's context, is retrievable, has been
followed, or grants authority. Contract conformance requires evaluation of the
applicable Accepted meaning and evidence; schema validity alone is insufficient.

## Reference, retrieval, and publication boundary

Consequential references SHOULD carry the exact Contract Definition Identifier
and Version and enough provenance to locate the intended Accepted source.
Unversioned summaries and moving aliases cannot silently substitute for a pin.

The URI allocation creates no registry service, resolver, catalog, cache,
redirect, automatic network behavior, hosted contract publication, media type,
transport, storage convention, or availability guarantee. A conforming offline
consumer may use an explicitly controlled local mapping without changing the
identifier. Network access, if ever introduced, requires separate authority and
security/privacy review.

## Security and privacy boundary

The allocations are intentionally public and generic. Contract identifiers,
source bindings, provenance, examples, or later mappings MUST NOT expose
secrets, credentials, personal data, private project data, production
configuration, private paths, restricted sources, or private implementation
detail. Identity, version, discoverability, repository hosting, and retrieval
success provide no trust, authorization, endorsement, safety, or permission to
access or disclose referenced material.

## Review, acceptance, and activation boundary

The exact candidate must be validated and reviewed under issue #46. The
combined Architect/Implementer review is transparently non-independent and may
identify whether the candidate conforms to the approved task contract; it
cannot grant final acceptance.

Only attributable Owner / Final Authority acceptance of the exact reviewed
head may authorize a later status-only promotion. Promotion, integration,
activation, issue completion, closure, synchronization, and branch cleanup are
separate governed actions. No identifier, version, test, review, PR state,
mergeability result, or public visibility silently authorizes them.

## Rejected alternatives

### Use `CONTRACT-00x`, Artifact Type, or a Markdown path as the identifier

Rejected because contract numbers, type labels, and paths are classification,
display, or mutable source coordinates rather than the stable, explicitly
namespaced Contract Definition identity required by ARCH-002.

### Use a branch, tag, release, `latest`, or version-bearing identifier

Rejected because the stable identifier must span semantic versions while the
paired Contract Definition Version pins exact accepted meaning. Moving
coordinates cannot replace either dimension.

### Use one family identity or lockstep family version

Rejected because the nine normative responsibilities, reviews, compatibility
assessments, and version lines remain independent even where dependencies exist.

### Allocate a new identity for each MAJOR version

Rejected because a breaking evolution of the same normative responsibility
remains under the same stable identity and receives a new MAJOR version.

### Begin at `0.x` because CNTX is pre-alpha

Rejected because repository maturity and release state are distinct from the
first Accepted semantic version of an already Accepted normative definition.

### Increment PATCH for candidates or review corrections

Rejected because pre-acceptance commits are provenance events, not Accepted
semantic-definition changes.

### Declare `1.0.0` without exact source binding

Rejected because an unpinned mutable notion of current content cannot identify
the exact intended normative definition revision.

### Require a new digest algorithm or automatic network resolution

Rejected because exact repository provenance is sufficient for this decision,
while digest mechanics, resolver behavior, network access, and publication are
separate architecture and security concerns.

### Treat the combined operational review as final approval

Rejected because issue #46 permits transparent operational role combination
but preserves sole human final authority and the exact-head acceptance gate.

## Deferred and prohibited by this decision

This decision does not define or authorize changes to CONTRACT-001 through
CONTRACT-009; new artifact-contract meaning; an executable artifact-specific
Schema Resource or payload; concrete artifact-specific `$id` or active Schema
Version; a change to Common Artifact Envelope Schema Version `1.0.0`; Artifact
Instance Identifier generation or Artifact Revision sequencing; digest
algorithm, encoding, canonicalization, signature, verification, or trust store;
artifact Serialization Binding or canonical artifact JSON; artifact-to-artifact
schema references; Extension Module or Profile mechanics; validator or
validation-output contract; resolver, registry service, catalog, cache,
bundler, redirect, automatic network retrieval, or hosted publication;
conformance tooling, code generation, migration, template, form, API, CLI,
workflow, engine, scheduler, orchestrator, runtime, provider, product, private
or reference implementation, release, tag, or deployment.

## Continuing gate

ARCH-011 remains Proposed until the exact reviewed candidate receives separate
attributable Owner / Final Authority acceptance and any later authorized
status-promotion and integration sequence succeeds. This proposal authorizes no
such later phase.

Only after these nine identifier/version/source bindings are Accepted and
active may a Project Charter artifact-specific executable Schema Version
`1.0.0` become the next separately authorized candidate. That later task must
use the exact Project Charter Contract Definition Identifier and Version from
this decision and must preserve every ARCH-010 boundary. No follow-on task is
implied or authorized here.
