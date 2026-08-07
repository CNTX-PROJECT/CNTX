# CNTX Task Contract Executable Schema Definition (ARCH-014)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed architecture candidate governed by
[issue #54](https://github.com/CNTX-PROJECT/CNTX/issues/54) and recorded by
[ADR-0014](adr/0014-task-contract-executable-schema.md). Owner / Final
Authority creation authority is recorded in issue comment `5215411581`.

The candidate defines one inactive Task Contract Schema Version `1.0.0` for
exact-head review. Creation, schema validity, tests, review, Draft PR status,
repository presence, or the `1.0.0` string does not accept or activate it. A
transparent non-independent review is evidentiary only. Separate attributable
Owner / Final Authority acceptance of the exact reviewed head is required.

This decision remains subordinate to Accepted architecture, Accepted
[CONTRACT-003](../contracts/task-contract-artifact-contract.md), repository
governance, and final human authority. It changes no Accepted contract or
schema and creates no Task Contract Artifact Instance, approval, task
authority, permission engine, workflow, validator, implementation, release,
or deployment.

## Purpose and decision boundary

Accepted [ARCH-010](artifact-specific-schema-family-container-boundary.md)
allocates the logical **CNTX Public Core Schema Family / Task Contract
Artifact** identity, an inactive `1.0.0` target, the mandatory closed
`envelope`/`payload` root, and the exact Common Artifact Envelope dependency.
Accepted [ARCH-011](contract-definition-identity-version-binding.md) allocates
the exact Task Contract Definition Identifier and Version. Accepted
CONTRACT-003 controls Task Contract meaning and authority boundaries.

Accepted ARCH-012 and ARCH-013 activate the Project Charter and Workstream
schema resources in dependency order. They do not automatically authorize a
Task Contract resource and are not executable dependencies of this candidate.

This Proposed decision binds the Task Contract logical identity to one
concrete Draft 2020-12 Schema Resource, specializes only the common envelope
constants, represents governing Project Charter and Workstream relationships
as opaque instance/revision pins, and translates only CONTRACT-003's accepted
responsibilities into a closed payload.

It defines structural assertions, not semantic proof. It cannot establish that
a governing artifact exists, that a Task Contract is approved, that declared
permissions apply, that execution occurred, or that evidence and acceptance
criteria are sufficient.

## Governing traceability

| Governing source | Constraint preserved |
| --- | --- |
| [ARCH-001](core-contract.md), [ARCH-002](contract-identity-versioning.md), and [ARCH-003](artifact-contract-schema-architecture.md) | Final human authority, identity-dimension separation, artifact/schema layering, evidence boundaries, and public/private separation remain unchanged. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) and the [Accepted Common Artifact Envelope Schema](../../schemas/common-artifact-envelope/1.0.0/schema.json) | The complete common envelope remains independently governed and is referenced once at its exact root identity. |
| [ARCH-010](artifact-specific-schema-family-container-boundary.md) | The Task Contract logical identity, independent version line, closed full-artifact root, payload ownership, and dependency-first rollout remain controlling. |
| [ARCH-011](contract-definition-identity-version-binding.md) | The exact Task Contract Contract Definition Identifier `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/task-contract` and Version `1.0.0` are used. |
| [ARCH-012](project-charter-executable-schema.md) and [ARCH-013](workstream-executable-schema.md) | Both Accepted resources remain unchanged; neither is referenced by this schema. |
| [CONTRACT-003](../contracts/task-contract-artifact-contract.md) | Only the Accepted bounded-task, authority, scope, context, assurance, decision, lifecycle, provenance, privacy, and non-self-approval responsibilities are translated into structure. |
| [Issue #54](https://github.com/CNTX-PROJECT/CNTX/issues/54) | Exact baseline, eight-path scope, validation, transparent review, stop gate, and prohibited actions remain binding. |

## Exact resource identity and version

| Dimension | Proposed value |
| --- | --- |
| Logical Schema Identity | CNTX Public Core Schema Family / Task Contract Artifact |
| Schema language | JSON Schema |
| Dialect | Draft 2020-12 |
| `$schema` | `https://json-schema.org/draft/2020-12/schema` |
| Canonical `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0` |
| Candidate Schema Version | `1.0.0` |
| Canonical repository path | `schemas/task-contract/1.0.0/schema.json` |
| Schema-resource media type | `application/schema+json` |
| Document Status | Proposed under issue #54 |

The `$id` is the stable identity of this exact Schema Version. Its HTTPS form
does not require or authorize network access. It is not a branch, tag, release,
resolver mapping, registry entry, hosted-publication guarantee, artifact
Serialization Binding, trust marker, or authority source.

Schema Version, Contract Definition Version, Artifact Instance Identifier,
Artifact Revision, Document Status, approval state, Implementation Version,
Content Digest, Provenance Reference, release, and deployment remain distinct.

## Complete artifact root

The resource evaluates one complete Task Contract Artifact Instance in the
JSON-compatible instance model. The root is a closed object with exactly two
required direct members:

1. `envelope`;
2. `payload`.

The root uses exact `properties`, exact `required`, and
`additionalProperties: false`. It cannot be flattened, opened, extended by an
unknown root member, or used to validate the common envelope or payload alone
as if either were the complete Task Contract artifact.

## Common Artifact Envelope specialization

`/envelope` uses exactly one static external reference to:

`https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`

One local overlay constrains only:

| Envelope coordinate | Exact constant |
| --- | --- |
| `artifactType` | `task-contract` |
| `governingContract.identifier` | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/task-contract` |
| `governingContract.version` | `1.0.0` |
| `governingSchema.identifier` | `https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0` |
| `governingSchema.version` | `1.0.0` |

The overlay does not copy, fork, weaken, or redefine the common resource. The
common resource retains ownership of envelope shape, requiredness, artifact
identity, coupled definition pins, provenance references, digest evidence,
lexical assertions, and closure.

No common internal `$defs` JSON Pointer, moving reference, relative reference,
branch, tag, release, `latest`, mirror, redirect, dynamic override, or network
retrieval behavior is used.

## Governing artifact pins and schema-dependency boundary

The payload contains separate mandatory `governingProjectCharter` and
`governingWorkstream` members. Each is a closed opaque pin with exactly:

- `artifactInstanceIdentifier`;
- `artifactRevision`.

Both values are required non-blank strings. The schema does not assign their
syntax, allocate identifiers, sequence revisions, retrieve an artifact,
resolve a pin, embed an artifact, validate the referenced artifact, or prove
existence, applicability, approval, compatibility, or current authority.

The resource contains no `$ref` to the Project Charter, Workstream, peer Task
Contract, Context Packet, or other artifact-specific schema. Accepted
contract dependency direction guides rollout and traceability but does not
force executable schema coupling. Peer Task Contract relationships remain
declarative statements with independent authority and lifecycle.

## Task Contract payload property model

The closed `payload` contains exactly eleven required properties:

| Property | Structural responsibility | Explicit non-meaning |
| --- | --- | --- |
| `governingProjectCharter` | Opaque governing Project Charter Artifact Instance/Revision pin. | No retrieval, embedded charter, schema dependency, existence, applicability, or approval proof. |
| `governingWorkstream` | Opaque governing Workstream Artifact Instance/Revision pin. | No retrieval, embedded workstream, schema dependency, status, or authority proof. |
| `objectiveAndOutcome` | One bounded objective, intended outcome, expected deliverables, and result boundary. | No backlog, Execution Result, completion claim, or outcome proof. |
| `scopeAndResources` | Included scope and assessed action, resource, side-effect, and external-interaction declarations. | No permission language, path matcher, policy evaluation, or enforcement. |
| `authorityAndExecution` | Authority-source, approver-role, delegation, executor, precondition, responsibility, and stop declarations. | No approval state/evidence, credential, signature, self-approval, or automatic activation. |
| `dependenciesAndConditions` | Dependencies, interfaces, peer relationships, assumptions, constraints, risks, uncertainty, and escalation. | No embedded artifacts, shared authority, automatic resolution, or workflow. |
| `contextPacketExpectations` | Minimum context, source selection, provenance, and isolation expectations. | No Context Packet, context retrieval, routing, prompt assembly, token budget, or source-access permission. |
| `securityAndPrivacy` | Security, privacy, confidentiality, public/private, and least-privilege constraints. | No credential storage, disclosure authority, or security implementation. |
| `assuranceAndAcceptance` | Expected evidence, validation obligations, acceptance criteria, limitations, and specialist-review boundaries. | No evidence production, criteria satisfaction, review, approval, completion, or integration proof. |
| `consequentialDecisionBoundaries` | Human-decision and integration, release, deployment, and merge boundaries. | No Decision Record, decision engine, or consequential approval. |
| `lifecycleConditions` | Validity, amendment, revocation, expiration, reassessment, completion, closure, supersession, and retention conditions. | No state vocabulary, transition, timestamp, timer, progress model, or automation. |

Unknown payload properties and unknown properties in every nested object are
invalid. The payload does not embed another canonical artifact.

## Objective, scope, and authority structure

`objectiveAndOutcome` requires non-blank `objective` and `intendedOutcome`
strings plus non-empty unique `expectedDeliverables` and `resultBoundary`
statement arrays. These fields make one coherent bounded task reviewable; they
cannot establish that any output exists or is accepted.

`scopeAndResources` requires non-empty unique `includedScope` statements and
explicit declaration sets for `nonGoals`, `exclusions`, `permittedActions`,
`forbiddenActions`, `permittedResources`, `forbiddenResources`,
`sideEffectBoundaries`, and `externalInteractions`.

Those categories are declarative. The schema assigns no grammar, wildcard,
path semantics, action taxonomy, resource taxonomy, allow/deny precedence, or
enforcement behavior. A valid permitted-action string cannot grant authority.
Only separate human approval of the exact Task Contract Artifact Revision can
authorize bounded execution under higher governing sources.

`authorityAndExecution` requires non-blank `authoritySource`, `approverRole`,
and `executorClass`; an explicit `boundedDelegation` declaration; and non-empty
unique `executorResponsibilities`, `executionPreconditions`, and
`stopConditions`. It contains no approval boolean, status, timestamp,
signature, credential, token, trust score, authorization decision, executable
delegation, or self-approval mechanism. Personal names are not mandatory.

## Dependencies and Context Packet expectations

`dependenciesAndConditions` requires explicit declaration sets for
`materialDependencies`, `interfaces`, `peerTaskContractRelationships`,
`assumptions`, `constraints`, `risks`, `unresolvedUncertainty`, and
`escalationConditions`. A declared peer relationship cannot merge or transfer
scope, approval, evidence, completion, context, lifecycle, or authority.

`contextPacketExpectations` requires an assessed `minimumContext` declaration
plus non-empty unique `sourceSelectionConstraints`, `provenanceRequirements`,
and `contextIsolation` statements. These are constraints for a later,
separately governed Context Packet selection. They create no packet, retrieve
no source, authorize no access or disclosure, and define no routing,
scheduling, prompt-assembly, or token mechanism.

## Security, assurance, and consequential decisions

`securityAndPrivacy` requires non-empty unique statements for security,
privacy, confidentiality, public/private, and least-privilege constraints.
The schema cannot determine whether those statements are sufficient or
followed. Security or privacy uncertainty requires stop and escalation under
the governing Task Contract, not silent schema-level defaulting.

`assuranceAndAcceptance` requires non-empty unique expected-evidence,
validation-obligation, and acceptance-criteria statements, plus explicit
known-limitations and specialist-review declarations. Expected evidence is not
produced evidence. Criteria text is not proof of satisfaction. Validation and
review remain evidence, not final approval.

`consequentialDecisionBoundaries` requires human-decision statements and
assessed integration, release, deployment, and merge boundaries. These fields
cannot make or record a consequential decision. Separate applicable human
authority remains controlling.

## Lifecycle conditions

`lifecycleConditions` requires substantive statement arrays for `validity`,
`amendment`, `revocation`, `completion`, and `closure`. It requires explicit
declarations for `expiration`, `reassessment`, `supersession`, and
`retention`.

The fields describe conditions only. They do not introduce a status
vocabulary, approval state, active flag, progress measure, timestamps, timers,
transitions, automation, scheduler, workflow, dashboard, or telemetry. Schema
validity cannot establish proposal, approval, activity, execution,
completion, acceptance, closure, expiration, revocation, or supersession.

## Declaration sets and assessed absence

One internal declaration-set shape is reused where a category may be empty but
must be explicitly assessed:

- `specified`: a closed object with `disposition: specified` and required
  non-empty unique non-blank `items`;
- `none`: a closed object containing only `disposition: none`, with `items`
  absent and forbidden.

`none` means assessed for this Artifact Revision and no item declared. It does
not mean unknown, skipped, automatically inapplicable, true, complete,
approved, safe, sufficient, risk-free, authorized, or permanently absent.
`disposition` is not Document Status, approval state, task status, lifecycle
state, progress, or runtime state.

Null, empty objects, unknown dispositions or properties, missing/empty/blank
or duplicate specified items, and items on `none` are invalid. No fabricated
`N/A`, empty string, empty array, or null placeholder is needed.

## Lexical and collection assertions

Ordinary strings use a shared non-blank assertion requiring at least one
non-whitespace code point. The schema deliberately does not normalize Unicode,
trim strings, prescribe human language, impose domain vocabularies, or treat a
string as executable syntax.

Ordinary statement arrays are non-empty and unique by JSON value. Uniqueness
does not prove semantic non-duplication. Array order is instance data and does
not define execution, priority, precedence, workflow, or approval order.

## Internal composition and reference graph

The canonical resource has one root `$schema`, one root `$id`, and no nested
resource identity. Reusable shapes occur only in root `$defs`. All internal
references are fragment-local `#/$defs/...` values. Exactly one external
reference targets the complete Accepted Common Artifact Envelope root.

The resource has no `$anchor`, `$dynamicAnchor`, `$dynamicRef`, recursive
resource graph, artifact-to-artifact Schema Resource dependency, custom
dialect, custom vocabulary, unknown normative keyword, `format`, default,
coercion, mutation, Hyper-Schema, or public subschema API. Internal `$defs`
names are implementation details with no independent version or compatibility
promise.

## Validation evidence

The non-normative
[test manifest](../../tests/schemas/task-contract/1.0.0/cases.json) contains
sixteen ordered public-safe synthetic instances: three expected-valid and
thirteen expected-invalid. Coverage includes:

- minimal assessed and fully specified Unicode payloads;
- optional common provenance and digest evidence;
- root, envelope, constant, and governing-pin failures;
- closure, requiredness, string, array, uniqueness, type, and declaration-set
  failures;
- forbidden approval, permission-engine, lifecycle-status, workflow, embedded
  artifact, extension, and runtime shapes.

Validation uses strict JSON parsing, official Draft 2020-12 schema checking,
an isolated `jsonschema 4.25.1` runtime, explicit local registration of the
exact common resource, and demonstrated failure when that resource is absent.
No repository dependency, validator implementation, lockfile, workflow, or
configuration is added. The isolated runtime is removed after evidence is
captured. The schema reference graph contains 75 `$ref` values: exactly one
external Common Artifact Envelope root reference and 74 fragment-local
internal references.

Fixtures are evidence only. They are not canonical Task Contracts, approved
Artifact Revisions, templates, forms, prompts, permission policies,
Serialization Bindings, conformance claims, or reference implementations.

## Contract conformance and authority boundary

Schema validity establishes only that an instance satisfies the evaluated
structural assertions. It cannot establish:

- CONTRACT-003 conformance;
- governing Project Charter or Workstream existence or applicability;
- accuracy, completeness, safety, or least privilege;
- that declared scope or authority is authorized;
- approval of the exact Artifact Revision;
- execution, completion, acceptance, closure, or evidence adequacy;
- integration, release, deployment, or merge authority.

Only applicable human-governed approval of the exact Task Contract Artifact
Revision can grant bounded task authority. Later approval cannot retroactively
authorize earlier out-of-scope work. Schema validity, review, repository
access, credentials, tools, or implementation capability cannot substitute.

## Security and privacy

The schema, documentation, and tests contain only public-safe generic material.
They contain no secrets, credentials, personal data, production configuration,
private paths, restricted source material, private project data, provider
assumptions, product logic, or private implementation detail. HTTPS-shaped
identifiers grant no network, access, trust, or disclosure permission.

## Consequences and tradeoffs

- One complete Task Contract becomes structurally evaluable.
- All eleven direct CONTRACT-003 responsibilities become explicit and closed.
- Governing-artifact traceability is represented without executable schema
  coupling.
- Explicit absence distinguishes assessed `none` from omission.
- Required structure improves consistency and reviewability.
- Broad declarative statements preserve domain independence but cannot enforce
  permission semantics or prove correctness, applicability, or authority.
- Independent Schema Version assessment is required for later structural or
  semantic change.
- No canonical serialization, validator, resolver, workflow, permission
  engine, or runtime is created.

## Rejected alternatives

- Flat, optional, or open root objects.
- Copying, weakening, or dynamically overriding the common envelope.
- Relative, mutable, branch, tag, release, `latest`, mirror, or redirect refs.
- Pointing `governingSchema` at the common schema.
- Artifact Type as Contract Definition identity.
- One artifact schema or lockstep family versioning.
- Project Charter or Workstream schema `$ref` values.
- Embedded Project Charter, Workstream, peer Task Contract, Context Packet, or
  downstream artifacts.
- Executable action/resource taxonomies, wildcard/path grammars, allow/deny
  precedence, permission languages, or policy engines.
- Approval, signature, timestamp, trust, credential, lifecycle-status,
  progress, workflow, scheduler, orchestration, or runtime fields.
- Mandatory personal names.
- Arbitrary payload maps and unknown properties.
- Blank strings, empty required arrays, duplicates, null, or fabricated `N/A`.
- Implied canonical JSON or another Serialization Binding.
- Normative example artifacts.
- Treating validation, review, or repository presence as acceptance.
- Automatic Context Packet or later schema authority.

## Deferred and prohibited scope

Deferred are Task Contract Artifact Instances; identifier allocation and
revision sequencing; governing-artifact retrieval or validation; peer artifact
resolution; permission/action/resource/path semantics and enforcement;
approval evidence; signatures and trust; digest algorithms and
canonicalization; artifact Serialization Bindings; canonical artifact JSON;
extensions/profiles; resolvers; registries; catalogs; caches; mirrors;
bundlers; validators and validation-output contracts; conformance tooling;
migrations; code generation; templates; forms; prompts; APIs; CLIs; workflows;
engines; schedulers; orchestrators; runtimes; provider/product work;
private/reference implementations; releases; tags; hosted publication; and
deployment.

This decision changes no Accepted source and grants no Context Packet or later
schema authority.

## Continuing gate

The candidate remains Proposed and Task Contract Schema Version `1.0.0`
remains inactive. The transparent exact-head review cannot accept it.

Only separate attributable Owner / Final Authority acceptance of the exact
reviewed candidate may authorize a status-only promotion and governed
integration. Even after possible future acceptance and activation, no Context
Packet or later artifact-specific schema, binding, validator, runtime,
implementation, release, or deployment is automatically authorized.
