# CNTX Architecture

## Start here

CNTX architecture explains the boundaries behind its records, schemas,
validation, extensions, evidence, and human authority. Public `main` contains
**46 Accepted and integrated architecture decisions and matching ADRs**.

| If you need… | Open… |
| --- | --- |
| The central CNTX boundary | [Core architecture contract](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) |
| The nine collaboration records | [Artifact-contract index](../contracts/README.md) |
| Machine-readable Core structure | [Schema index](../../schemas/README.md) |
| The bounded executable practice slice | [Validation and integrity slice](../../tools/minimal-validation-integrity-slice/README.md) and [Accepted corrective version boundary](minimal-validation-integrity-slice-corrective-version-boundary.md) |
| The source/provenance/freshness layer | [ARCH-038](epistemic-provenance-freshness-extension-module-definition.md), [ARCH-039](context-packet-epistemic-provenance-freshness-profile-definition.md), [ARCH-040](epistemic-provenance-freshness-extension-module-json-representation-boundary.md), integrated [ARCH-042](epistemic-provenance-freshness-extension-module-definition-schema-resource.md), integrated [ARCH-043](context-packet-epistemic-provenance-freshness-profile-json-representation-boundary.md), integrated [ARCH-044](context-packet-epistemic-provenance-freshness-profile-definition-schema-resource.md), and integrated [ARCH-045](governing-definition-declaration-set-json-representation-boundary.md) |
| The integrated execution/task-control boundary | Integrated [ARCH-046](execution-task-control-architecture-boundary.md) and [ADR-0046](adr/0046-execution-task-control-architecture-boundary.md) |
| Current and future order | [Roadmap](../../ROADMAP.md) |

## Architecture map

| Decisions | Subject | Current result |
| --- | --- | --- |
| ARCH-001–011 | Core boundaries, contract identity, envelope, schema families | Accepted foundation |
| ARCH-012–020 | Executable schemas for the nine record types | 10 Accepted Core Schema Resources in total |
| ARCH-021–027 | Completion, binding, resolution, validation, evidence, release boundaries | Accepted public-core and prerelease lifecycle |
| ARCH-028–033 | Extension Module/Profile identity, composition, resources, validation, tooling | Accepted extension architecture |
| ARCH-034–037 | Validation records, evidence package, integrity rules, Tool/Implementation contract | Accepted basis for the bounded local slice |
| ARCH-038–040 | Epistemic provenance and freshness Module/Profile Definitions and Module representation boundary | Accepted and integrated; no Module schema, rule, implementation, or evidence instance |
| ARCH-041 | Minimal validation and integrity slice corrective version boundary | Accepted and integrated; corrective Implementation `1.0.1` is integrated with its bounded evidence, while portability and CI remain separate |
| ARCH-042 | Epistemic provenance and freshness Module Definition Schema Resource | Accepted and integrated with one exact schema and 48 separately matched synthetic cases; no Tool support or new evidence instance |
| ARCH-043 | Context Packet epistemic provenance and freshness Profile JSON representation boundary | Accepted and integrated; one closed external application record, no Core/schema/Tool change or automatic activation |
| ARCH-044 | Context Packet epistemic provenance and freshness Profile Definition Schema Resource | Accepted and integrated with one closed standalone schema and 72 separately matched operation-based cases; no new execution/evidence instance, activation, or Tool support |
| ARCH-045 | Governing Definition Declaration and frozen Governing Declaration Set JSON representation boundary | Accepted and integrated; one reusable closed fourteen-member declaration and one closed six-member set preserving 21 responsibilities and 11 invariants, with no identity, schema, package, Binding, Tool, execution, or authority |
| ARCH-046 | Execution and Task Control Architecture Boundary | Accepted and integrated; exact Task Contract remains controlling, with four descriptive complexity classes, 27 separate participant/control dimensions, and twelve conceptual responsibility groups; no representation, mechanism, Tool/Implementation, execution, or authority |

Architecture documents state conceptual and normative boundaries. They do not
by themselves install software, execute a tool, prove conformance, approve a
result, or authorize a later phase.

<details>
<summary><strong>Open the complete Accepted architecture index</strong></summary>

## Complete reading guide

[The core architecture contract](core-contract.md) is the accepted normative conceptual architecture baseline for CNTX. It specifies public-core concepts and constraints, not an executable architecture. [ADR-0001](adr/0001-public-core-boundaries.md) records the accepted decision that establishes the public-core boundary. [The contract identity and versioning contract](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) are accepted additions: ARCH-001 remains the accepted core baseline, ARCH-002 is an accepted extension of that baseline, and [the artifact-contract and schema-layering contract](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) are the accepted ARCH-003 extension of that baseline. [The Common Artifact Envelope schema boundary](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) are the accepted ARCH-004 conceptual boundary for future common-envelope schema work; they do not alter existing artifact contracts or authorize executable schema work. [The Common Artifact Envelope representation boundary](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) are the accepted ARCH-005 documentation-only refinement that identifies future representation obligations and decision order without selecting fields, schema technology, serialization, validation, or implementation. [The Common Artifact Envelope schema identity and initial version policy](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) are the **Accepted**, documentation-only ARCH-006 allocation of one technology-neutral logical identity and the `1.0.0` initial accepted version target; they create no concrete Schema Identifier, executable schema, active Schema Version, schema-language choice, serialization, validation, runtime, or implementation. [The Common Artifact Envelope schema language and dialect](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) are the **Accepted**, documentation-only ARCH-007 selection of JSON Schema Draft 2020-12 with its standard vocabulary profile; they create no executable schema, concrete `$id`, composition or packaging model, artifact Serialization Binding, validator, runtime, or implementation. [The Common Artifact Envelope schema composition and packaging](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) are the **Accepted**, documentation-only ARCH-008 selection of one canonical root resource, internal `$defs`, static exact-version references, standalone canonical resources, derived identity-preserving bundles, and offline-first resolution; they create no executable schema, concrete `$id`, active Schema Version, artifact Serialization Binding, validator, runtime, or implementation. [The Common Artifact Envelope executable schema definition](common-artifact-envelope-executable-schema.md) and [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md) are the **Accepted** ARCH-009 binding of the one logical Common Artifact Envelope identity to JSON Schema Draft 2020-12 Schema Version `1.0.0`, with a closed six-property envelope, nine canonical Artifact Type tokens, coupled identity/version pins, optional provenance references, and optional digest evidence. Acceptance and schema validity do not define artifact-specific payload or relationships, select an artifact Serialization Binding, or provide authority, a validator, resolver, runtime, product, release, or deployment. The [`adr/`](adr/) directory is the location for architecture decision records. Accepted architecture governs the artifact-specific contracts listed in the [contract index](../contracts/README.md). CONTRACT-001, the Project Charter artifact contract, remains **Accepted** and is a binding, subordinate artifact-specific contract governed by ARCH-001, ARCH-002, and ARCH-003. CONTRACT-002, the Workstream artifact contract, remains **Accepted** and is a binding, subordinate artifact-specific contract governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001. CONTRACT-003, the [Task Contract artifact contract](../contracts/task-contract-artifact-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, accepted CONTRACT-001, and accepted CONTRACT-002. It does not alter or redefine accepted architecture, Project Charter, or Workstream. Only a separately approved change to the applicable higher architecture documents can alter that architecture.

CONTRACT-004, the [Context Packet artifact contract](../contracts/context-packet-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, and CONTRACT-003. It does not alter or redefine accepted architecture, Project Charter, Workstream, or Task Contract.

CONTRACT-005, the [Execution Result artifact contract](../contracts/execution-result-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, CONTRACT-003, and CONTRACT-004. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, or Context Packet.

CONTRACT-006, the [Evidence Bundle artifact contract](../contracts/evidence-bundle-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-005. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, or Execution Result.

CONTRACT-007, the [Review Record artifact contract](../contracts/review-record-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, or Evidence Bundle.

CONTRACT-008, the [Decision Record artifact contract](../contracts/decision-record-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-007. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, Evidence Bundle, or Review Record.

CONTRACT-009, the [State Snapshot artifact contract](../contracts/state-snapshot-contract.md), is **Accepted**, documentation-only, binding, and subordinate to accepted ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-008. It specializes State Snapshot semantics only and does not alter accepted architecture, any accepted artifact contract, or final human authority. CONTRACT-001 through CONTRACT-009 are **Accepted**.

This architecture documentation is read with the repository [README](../../README.md), [agent instructions](../../AGENTS.md), [governance](../../GOVERNANCE.md), and [security policy](../../SECURITY.md). The README describes the project and its current status. `AGENTS.md` sets execution constraints and source precedence. `GOVERNANCE.md` assigns decision authority and approval. Normative architecture states what the public core requires conceptually; governance assigns who may approve it; every conforming implementation remains subordinate; and non-binding discussion is neither an approved decision nor an authority source.

The repository contains one bounded local Tool/Implementation slice for its exact supported set. No general runtime, selector, retrieval system, provider integration, supported product, or broad validator is implemented here. ARCH-009 introduces one Accepted executable Common Artifact Envelope Schema Resource only; it is not an artifact-specific schema, a complete artifact definition, a Serialization Binding, or an implementation.

The [Artifact-Specific Schema Family and Canonical Artifact Container Boundary](artifact-specific-schema-family-container-boundary.md) and [ADR-0010](adr/0010-artifact-specific-schema-family-container-boundary.md) are **Accepted**, documentation-only architecture. They allocate nine technology-neutral artifact-specific logical Schema Identities and inactive `1.0.0` targets, select one closed full-artifact root with mandatory `envelope` and `payload`, and pin the envelope location to the exact Accepted Common Artifact Envelope Schema Version `1.0.0`. They create no executable artifact-specific schema or payload, concrete artifact-specific `$id`, active Schema Version, binding, validator, runtime, implementation, release, or deployment; their acceptance authorizes no follow-on phase.

The [Canonical Contract Definition Identity, Initial Version, and Source Binding](contract-definition-identity-version-binding.md) and [ADR-0011](adr/0011-contract-definition-identity-version-binding.md) are **Accepted**, documentation-only architecture. They allocate exactly nine stable Contract Definition Identifiers, independent initial Contract Definition Version `1.0.0` values, and exact Accepted-source bindings for CONTRACT-001 through CONTRACT-009. The nine integrated identifier/version/source-binding pairs are Accepted and active. They change no accepted contract meaning, create no executable artifact-specific schema, binding, resolver, validator, runtime, implementation, release, or deployment, and authorize no follow-on phase.

The [Project Charter Executable Schema Definition](project-charter-executable-schema.md) and [ADR-0012](adr/0012-project-charter-executable-schema.md) are **Accepted** under issue #48 and Owner acceptance comment `5210242651`. They bind the logical Project Charter Artifact Schema Identity to a concrete Draft 2020-12 `$id` and Schema Version `1.0.0`, apply the exact Accepted Common Artifact Envelope at mandatory `/envelope`, constrain the exact Project Charter Artifact Type and governing-definition pins, and define a closed CONTRACT-001 payload with synthetic validation evidence. Governed integration to `main` activates that exact Schema Version. Acceptance and schema validity grant no contract conformance, approval, authority, release, deployment, or follow-on schema authority.

The [Workstream Executable Schema Definition](workstream-executable-schema.md)
and [ADR-0013](adr/0013-workstream-executable-schema.md) are **Accepted** under
issue #52 and Owner acceptance comment `5215029431`. They define one Draft
2020-12 resource with the exact
Accepted Common Artifact Envelope at mandatory `/envelope`, exact Workstream
Artifact Type and governing-definition pins, an opaque governing Project
Charter Artifact Instance/Revision pin, and a closed twelve-property
CONTRACT-002 payload. The resource contains no Project Charter schema `$ref`.
Governed integration to `main` activates that exact Schema Version. Acceptance,
schema validity, or repository presence grants no contract conformance,
approval, authority, release, deployment, merge permission, or Task Contract
schema authority.

The [Task Contract Executable Schema Definition](task-contract-executable-schema.md)
and [ADR-0014](adr/0014-task-contract-executable-schema.md) are **Accepted**
under issue #54 and Owner acceptance comment `5215700352`. They define one
Draft 2020-12 Task Contract Schema Version
`1.0.0` with the exact Accepted Common Artifact Envelope at mandatory
`/envelope`, exact Task Contract Artifact Type and governing-definition pins,
separate opaque governing Project Charter and Workstream Artifact
Instance/Revision pins, and a closed eleven-property CONTRACT-003 payload. It
contains no Project Charter, Workstream, peer Task Contract, or downstream
artifact schema `$ref`, permission language, approval mechanism, workflow, or
runtime. Governed integration to `main` activates that exact Schema Version.
Acceptance, schema validity, or repository presence grants no contract
conformance, task authority, integration authority, release, deployment,
merge permission, Context Packet schema authority, or follow-on authority.

The [Context Packet Executable Schema Definition](context-packet-executable-schema.md)
and [ADR-0015](adr/0015-context-packet-executable-schema.md) are **Accepted**
under issue #56 and Owner acceptance comment `5216466742`. They define one
Draft 2020-12 Context Packet Schema Version `1.0.0` with the exact Accepted
Common Artifact Envelope at
mandatory `/envelope`, exact Context Packet Artifact Type and governing
definition pins, one opaque governing Task Contract Artifact Instance/Revision
pin, and a closed thirteen-property CONTRACT-004 payload. The resource contains
no Project Charter, Workstream, Task Contract, peer, Execution Result, or
downstream schema `$ref` and no executable selection, retrieval, ranking,
access, disclosure, transformation, prompt, workflow, or runtime mechanism.
Governed integration to `main` activates that exact Schema Version.
Acceptance, schema validity, or repository presence grants no contract
conformance, task authority, source access, retrieval or disclosure permission,
merge permission, release, deployment, Execution Result schema authority, or
follow-on authority.

The [Execution Result Executable Schema Definition](execution-result-executable-schema.md)
and [ADR-0016](adr/0016-execution-result-executable-schema.md) are **Accepted**
under issue #58 and Owner acceptance comment `5217275706`. They define one
Draft 2020-12 Execution Result Schema Version `1.0.0` that composes the exact
Accepted Common Artifact Envelope with a closed fourteen-property CONTRACT-005
payload, one opaque governing Task Contract pin, and explicit opaque Context
Packet pin declarations. It contains no artifact-specific schema `$ref`.
Output, actions, side effects, resources, provenance, checks, criteria
assessments, assumptions, limitations, failures, deviations, stops,
escalations, security/privacy, and evidence/review/decision/lifecycle
traceability remain evidentiary declarations. Governed integration to `main`
activates that exact Schema Version. Acceptance, schema validity, or repository
presence grants no correctness, completion, conformance, integration authority,
release, deployment, merge permission, Evidence Bundle schema authority, or
follow-on authority.

The [Evidence Bundle Executable Schema Definition](evidence-bundle-executable-schema.md)
and [ADR-0017](adr/0017-evidence-bundle-executable-schema.md) are **Accepted**
under issue #60 and Owner acceptance comment `5217888146`. They define one
Accepted Draft 2020-12 Evidence Bundle Schema Version `1.0.0` that composes the
exact Accepted Common Artifact Envelope with a
closed fifteen-property CONTRACT-006 payload, one opaque governing Task
Contract pin, exact reviewable-subject declarations, explicit opaque artifact
relationships, Evidence Items, claim traceability, and bounded provenance,
quality, limitation, security/privacy, and lifecycle declarations. It contains
no artifact-specific schema `$ref` and implements no collection, retrieval,
scoring, verification, access, disclosure, approval, acceptance, workflow,
release, deployment, or merge mechanism. Creation, validation, review, schema
validity, or repository presence grants no contract conformance, source truth,
relevance, sufficiency, correctness, acceptance, integration, release,
deployment, merge permission, Review Record schema authority, or follow-on
authority. Governed integration to `main` activates the exact Schema Version.

The [Review Record Executable Schema Definition](review-record-executable-schema.md)
and [ADR-0018](adr/0018-review-record-executable-schema.md) are **Accepted**
under issue #62 and EIGENAAR acceptance comment `5218629573`. They define one
Accepted Draft 2020-12 Review Record Schema Version `1.0.0` that composes the exact Accepted Common Artifact
Envelope with a closed sixteen-property CONTRACT-007 payload. Review Authority
and Execution Authority remain separate opaque pins; exact reviewable subjects,
nine artifact-relationship categories, findings, evidence use, uncertainty,
dissent, recommendations, peer reviews, correction, security/privacy, and
lifecycle values remain bounded Evidentiary declarations. The resource
contains no artifact-specific schema `$ref` and implements no reviewer identity
or specialty system, review, retrieval, scoring, severity, confidence, verdict,
approval, voting, synthesis, decision, workflow, runtime, access, disclosure,
retention, release, deployment, or merge mechanism. Creation, validation,
review, schema validity, or repository presence grants no contract conformance,
specialist authority, review quality, recommendation authority, acceptance,
integration, release, deployment, merge permission, Decision Record schema
authority, or follow-on authority. Governed integration to `main` activates
the exact Schema Version; acceptance and activation authorize no Decision
Record schema or other follow-on work.

The [Decision Record Executable Schema Definition](decision-record-executable-schema.md)
and [ADR-0019](adr/0019-decision-record-executable-schema.md) are **Accepted**
under issue #64 and EIGENAAR acceptance comment `5219310944`. They define one
Accepted Draft 2020-12 Decision Record Schema Version `1.0.0` that composes the exact Accepted Common Artifact
Envelope with a closed seventeen-property CONTRACT-008 payload. Decision
Authority, the opaque human decision maker, the exact revision represented as
approved, approval provenance, the bounded question and outcome, basis, nine
artifact relationships, inputs, timing, scope, consequences, seven downstream
boundaries, change/conflict provenance, roles, external records,
security/privacy, restricted basis, lifecycle, and history remain declarative
and non-automatic. The resource contains no artifact-specific schema `$ref`
and implements no identity, authority, approval, retrieval, reasoning,
recommendation, decision, conflict-resolution, state, workflow, consequential-
action, runtime, access, disclosure, retention, release, deployment,
publication, or merge mechanism. Creation, validation, review, schema validity,
or repository presence grants no acceptance, activation, State Snapshot schema,
or follow-on authority. Governed integration to `main` activates the exact
Schema Version; acceptance and activation authorize no State Snapshot schema or
other follow-on work.

The [State Snapshot Executable Schema Definition](state-snapshot-executable-schema.md)
and [ADR-0020](adr/0020-state-snapshot-executable-schema.md) are **Accepted**
under issue #66 and EIGENAAR acceptance comment `5219885650`. They define one
Draft 2020-12 State Snapshot Schema Version `1.0.0` that composes the exact
Accepted Common Artifact Envelope with a closed eighteen-property CONTRACT-009
payload. Authorized
derivation and Derived/non-authoritative classification, controlling sources
and exact revisions or pinning limitations, six temporal coordinates, four
freshness classifications, reported state and separated claims,
evidence/review/decision/integration traceability, nine artifact relationships,
uncertainty, stops, history, five peer relations, bounded handoff,
security/privacy, and non-automatic lifecycle effects remain declarative. The
resource contains no artifact-specific schema `$ref` and implements no
authority, retrieval, freshness calculation, conflict resolution, state,
synchronization, workflow, runtime, access, disclosure, retention,
verification, release, deployment, publication, or merge mechanism. Creation,
validation, review, schema validity, or repository presence did not grant
acceptance or activation. Exact-head acceptance is recorded in comment
`5219885650`; governed integration to `main` activates the exact Schema Version.
Acceptance and activation authorize no further phase automatically.

The [CNTX Public Core Completion Boundary and Remaining Layer
Roadmap](public-core-completion-boundary-roadmap.md) and
[ADR-0021](adr/0021-public-core-completion-boundary-roadmap.md) are
**Accepted** under issue #68 and EIGENAAR acceptance comment `5220966638`.
They identify the completed contract-and-schema
foundation and dependency-order the still-separate Serialization Binding,
schema-resource resolution/catalog, validation/output, portable conformance,
and release-readiness decisions. They create no binding, resolver, validator,
conformance tooling, implementation, release, publication, deployment, or
follow-on authority.

The [CNTX Core Artifact Serialization Binding
Architecture](core-artifact-serialization-binding.md) and
[ADR-0022](adr/0022-core-artifact-serialization-binding.md) are **Accepted**
as ARCH-022
under issue #70 and EIGENAAR acceptance comment `5221466569`. They define one
logical Core Artifact JSON binding identity and initial Binding Version `1.0.0`,
activated by governed integration, RFC 8259 `application/json`,
UTF-8 without BOM, duplicate-name rejection, bounded numeric and Unicode
treatment, non-semantic object order and whitespace, preserved array order,
explicit absence of canonicalization, one-artifact document boundaries,
separated error layers, compatibility, and security/privacy limits. They
change no Accepted contract, schema, test, identity, or version and create no
Artifact Instance, canonical JSON, resolver, validator, conformance tooling,
implementation, release, publication, deployment, acceptance, merge
permission, or follow-on authority.

The [CNTX Schema Resource Resolution and Catalog
Boundary](schema-resource-resolution-catalog-boundary.md) and
[ADR-0023](adr/0023-schema-resource-resolution-catalog-boundary.md) are
**Accepted** as ARCH-023 under issue #72, attributable EIGENAAR
creation-authority comment `5221792750`, and EIGENAAR acceptance comment
`5222126273`. They define exact Schema Identifier/Version resource keys, a
frozen caller-supplied context, a non-authoritative catalog view,
preloaded/caller-mapped/identity-preserving bundled supply, no automatic
network retrieval, exact transitive static-reference closure, fail-closed
missing/ambiguous/conflicting/wrong-version handling, determinism, provenance,
and security/privacy limits. They create no catalog artifact or identity,
resolver, registry, cache, bundler, mirror, redirect, network mechanism,
validator, validation output, conformance tooling, implementation, release,
publication, deployment, acceptance, merge permission, or follow-on authority.

The [CNTX Validation and Validation Output
Contract](validation-and-validation-output-contract.md) and
[ADR-0024](adr/0024-validation-and-validation-output-contract.md) are
**Accepted** as ARCH-024 under issue #74, attributable EIGENAAR creation-
authority comment `5222505304`, and EIGENAAR acceptance comment `5222756874`.
They define a frozen validation context, six
separate conformance dimensions, logical phases and dependencies, Satisfied /
Not Satisfied / Unverifiable / Not Evaluated outcomes, fail-closed claim rules,
diagnostic and limitation boundaries, the relationship to JSON Schema Draft
2020-12 output, reproducibility responsibilities, and security/privacy/non-
authority limits. They create no output identity, field, schema, portable
error/severity vocabulary, universal result, validator,
conformance tool, Artifact Instance, portable evidence, implementation,
release, publication, deployment, merge permission, or follow-on authority.

The [CNTX Portable Conformance Evidence
Boundary](portable-conformance-evidence-boundary.md) and
[ADR-0025](adr/0025-portable-conformance-evidence-boundary.md) are
**Accepted** as ARCH-025 under issue #76, attributable EIGENAAR creation-
authority comment `5223043068`, and EIGENAAR acceptance comment `5223192303`.
They define a logical boundary for exactly
scoped, version-bound, provenance-bearing, offline-first, independently
reassessable conformance evidence; twelve evidence responsibilities;
claim/evidence/requirement traceability; validation-output and Evidence Bundle
separation; fail-closed missing, restricted, conflicting, or unreproducible
evidence; six conformance-target evidence boundaries; reproduction, conflict,
security/privacy, disclosure, and non-authority limits. They create no evidence
Artifact Instance, Conformance Claim artifact, field, schema, manifest,
package, serialization, protocol, validator, test runner, suite, score, badge,
certification, supported-version claim, release-readiness decision,
implementation, release, publication, deployment, acceptance, merge
permission, or follow-on authority.

The [CNTX Public-Core Release Readiness and Publication
Boundary](public-core-release-readiness-publication-boundary.md) and
[ADR-0026](adr/0026-public-core-release-readiness-publication-boundary.md) are
**Accepted** as ARCH-026 under issue #78, attributable EIGENAAR creation-
authority comment `5223389264`, and EIGENAAR acceptance comment `5223546552`.
They define an exact release-subject and frozen-basis boundary, six separately
assessed readiness dimensions, ten logical
release-basis responsibilities, fail-closed governing-source and evidence
closure, documentation/policy/license/notice, security/privacy/legal/
disclosure, publication, compatibility, support, correction, and final-human-
authority limits. They keep readiness assessment, approval, release, version,
tag, publication, distribution, support, certification, and deployment
separate. The decision performs no current readiness assessment, changes no
other Accepted source, creates no aggregate `ready` result, record, manifest,
package, version, tag, compatibility or support claim, implementation,
release, publication, deployment, merge permission, or follow-on authority.

The [CNTX Public-Core Completion and Maintenance
Boundary](public-core-completion-and-maintenance-boundary.md) and
[ADR-0027](adr/0027-public-core-completion-and-maintenance-boundary.md) are
**Accepted** as ARCH-027 under issue #96, attributable EIGENAAR / Final
Authority creation comment `5228385928`, and exact-head acceptance comment
`5228459221`. They name the work through
Accepted VERIFY-001 the completed initial Public-Core specification and
prerelease cycle, while keeping repository archival, supported-version status,
maintenance promises, implementation/runtime/provider/product completion,
hosted-publication completion, and deployment separate. They define only a
quiescent, event-driven governance boundary for possible future changes. They
perform no project closure, maintenance action, correction, withdrawal,
release-object mutation, support or compatibility claim, implementation,
publication, deployment, or follow-on action.

The [CNTX Extension Module and Profile Architecture
Boundary](extension-module-profile-architecture-boundary.md) and
[ADR-0028](adr/0028-extension-module-profile-architecture-boundary.md) are
**Accepted** as ARCH-028 under issue #98, attributable EIGENAAR / Final
Authority creation comment `5228583661`, and exact-head acceptance comment
`5228762336`. They separate optional Extension
Module and Profile categories, preserve Core sovereignty, require explicit
exact-version opt-in and fail-closed conflict handling, identify the distinct
identity, versioning, provenance, authority, dependency, activation,
declaration, composition, compatibility, conformance/evidence,
security/privacy, and lifecycle responsibilities, and order every possible
later decision dependency-first. Acceptance and integration allocate no
concrete identity, version, field, token, vocabulary, Schema Resource,
executable schema, resolver, validator, registry, tooling, implementation,
release, publication,
deployment, or follow-on authority.

The [CNTX Extension Module and Profile Identity and Version
Policy](extension-module-profile-identity-version-policy.md) and
[ADR-0029](adr/0029-extension-module-profile-identity-version-policy.md) are
**Accepted** as ARCH-029 under issue #100, attributable EIGENAAR / Final
Authority creation comment `5228909425`, and exact-head acceptance comment
`5229936609`. They define four separate
Extension Module/Profile Definition Identifier/Version dimensions, two stable
definition-family namespaces, one exact child-allocation rule, independent
initial `1.0.0` version lines, MAJOR.MINOR.PATCH change rules, identity
continuity, Accepted-version immutability, exact future allocation gates,
opaque no-network identifiers, Core sovereignty, and final human authority.
They create no concrete Extension Module/Profile, child Identifier/Version,
dependency/activation/composition/conflict mechanism, Schema Resource,
executable schema, validator, implementation, release, publication,
deployment, or follow-on authority.

The [CNTX Extension Module and Profile Dependency, Activation, Composition and
Conflict
Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
and
[ADR-0030](adr/0030-extension-module-profile-dependency-activation-composition-conflict-policy.md)
are **Accepted** as ARCH-030 under issue #102, attributable EIGENAAR / Final
Authority creation comment `5230085538`, and exact-head acceptance comment
`5230166187`. They define only exact Definition
keys, logical required/optional dependencies and Profile Subjects, one explicit
frozen activation context, permitted dependency directions, a finite acyclic
closure, one active version per Identifier, Core-first and topological
dependency order without precedence, additive Module and narrowing-only
conjunctive Profile composition, fail-closed conflicts and unknown/unsupported
conditions, caller-supplied offline supply, scoped compatibility/conformance
evidence, security/privacy limits, and final human authority. Acceptance and
integration create no concrete definition, child Identifier/Version, declaration field or
token, Schema Resource, executable schema, resolver, validator, tooling,
implementation, release, publication, deployment, merge permission,
or follow-on authority.

The [CNTX Extension Module and Profile Schema Resource, Packaging and
Declaration
Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
and
[ADR-0031](adr/0031-extension-module-profile-schema-resource-packaging-declaration-model.md)
are **Accepted** as ARCH-031 under issue #104, attributable EIGENAAR / Final
Authority creation comment `5230355484`, and exact-head acceptance comment
`5230552794`. They define only two logical
Definition Schema Families, strict Definition/Schema/source/package/declaration
dimension separation, one exact Schema Resource key-or-`None` binding per
active Definition key, a constrained standalone Draft 2020-12 resource model,
an ARCH-030-aligned resource graph, closed caller-supplied packages,
identity-preserving derived bundles, and a frozen logical Governing Declaration
Set outside all Core Artifact Instances and Core Artifact JSON. Acceptance and
integration allocate no concrete identity, version, `$id`, resource, executable
schema, field, token, package instance, resolver, validator, implementation,
release, publication, deployment, merge permission, or follow-on authority.

The [CNTX Extension Module and Profile Executable Schema and
Validation/Conformance
Boundary](extension-module-profile-executable-schema-validation-conformance-boundary.md)
and
[ADR-0032](adr/0032-extension-module-profile-executable-schema-validation-conformance-boundary.md)
are **Accepted** as ARCH-032 under issue #106, attributable EIGENAAR / Final
Authority creation comment `5230742345`, and exact-head acceptance comment
`5230968570`. They define only a future frozen
Extension Module/Profile validation context, separate conformance dimensions,
fifteen prerequisite-ordered logical evaluation phases, bounded schema-local
results, future synthetic-case responsibilities, fail-closed conditions,
validation-output and Portable Conformance Evidence relationships,
security/privacy/resource limits, historical integrity, and final human
authority. Acceptance and integration create no concrete Definition, child identity/version, `$id`,
Schema Resource, executable schema, assertion, case, declaration
representation, package instance, resolver, validator, tooling,
implementation, release, publication, deployment, merge permission, or
follow-on authority. Any Tooling and Implementation Boundary remains a
separately governed decision and is not authorized by ARCH-032.

The [CNTX Extension Module and Profile Tooling and Implementation
Boundary](extension-module-profile-tooling-implementation-boundary.md) and
[ADR-0033](adr/0033-extension-module-profile-tooling-implementation-boundary.md)
are **Accepted** as ARCH-033 under issue #108, attributable EIGENAAR / Final
Authority creation comment `5231158990`, and exact-head acceptance comment
`5233773228`. They distinguish sixteen conceptual
tooling and implementation categories; keep tool, implementation, capability,
configuration, environment, output, evidence, conformance, support, release,
and deployment dimensions separate; require a closed frozen exact-pinned
execution context and offline-first deterministic processing; preserve visible
fail-closed failures, limitations, restricted evidence, and non-execution;
keep reference implementations non-normative; and define resource,
security/privacy, public/private, lifecycle, and final-human-authority
boundaries. Acceptance and integration create no concrete Definition,
Schema Resource, declaration, package, binding, output/evidence identity,
tool, implementation, interface, runtime, service, release, publication,
support, certification, deployment, merge permission, or follow-on authority.

The [CNTX Validation Execution Record Identity, Version, and JSON
Representation](validation-execution-record.md) and
[ADR-0034](adr/0034-validation-execution-record.md) are **Accepted** as
ARCH-034 under issue #114, attributable EIGENAAR / Final Authority Package A
creation comment `5240354818`, and exact-head acceptance comment `5240683870`.
The documentation-only decision defines one
non-Artifact Validation-layer record, one stable Definition Identifier and
initial Version `1.0.0`, one JSON Representation Identifier and initial Version
`1.0.0`, a strict closed ten-property JSON root, exact tokens for the eight
ARCH-024 phases and four outcomes, frozen governing and evaluator-context
responsibilities, bounded diagnostics and limitations, record-local
referential integrity, separate conformance claims, immutable revision
lifecycle, disabled network authority, security/privacy/resource limits, and
automatic-authority prohibition. Acceptance and integration allocate and
activate only the stated Definition and Representation identity/version pairs
and create no executable schema, evidence package, cross-record rule, Tool,
Implementation, dependency, validator, runner, workflow, CI, release, support,
hosting, deployment, merge permission, or authority for Package B, C, D, or E.

The [CNTX Validation Evidence and Reproduction Package Identity, Version, and
JSON Representation](validation-evidence-reproduction-package.md) and
[ADR-0035](adr/0035-validation-evidence-reproduction-package.md) are
**Accepted** as ARCH-035 under issue #116, attributable EIGENAAR / Final
Authority issue-contract acceptance comment `5241232823`, and exact-head
acceptance comment `5241789812`. The documentation-only decision defines one
non-Artifact Validation-layer
Evidence and Reproduction Package Definition Identifier and initial Version
`1.0.0`, one JSON Representation Identifier and initial Version `1.0.0`, and a
strict closed twelve-property JSON root. It separately records exact subjects,
governing inputs, evaluator context, Validation Execution Record references,
evidence, reproduction procedures, outputs, diagnostics, limitations, claims,
and authority; requires package-local referential integrity; preserves
offline-first, deterministic, bounded, fail-closed processing; and keeps raw
evaluator output, canonical Validation Output, Portable Conformance Evidence,
Evidence Bundle, review, decision, certification, release evidence, other
Artifact Instances, and final-human authority separate. Acceptance and
integration allocate and activate only the stated Definition and Representation
identity/version pairs and create no executable schema, package instance,
cross-record rule, Tool, Implementation, dependency, validator, runner,
workflow, CI, release, publication, support, certification, hosting,
deployment, merge permission, or authority for Package C, D, or E.

The [CNTX Test Manifest and Initial Cross-Record Integrity Rules Identity,
Version, and JSON Representation](test-manifest-cross-record-integrity-rules.md)
and
[ADR-0036](adr/0036-test-manifest-cross-record-integrity-rules.md) are
**Accepted** as ARCH-036 under issue #118, attributable EIGENAAR / Final
Authority issue-contract acceptance comment `5242339896`, and exact-head
acceptance comment `5243304427`. The documentation-only Package C decision
defines three separate non-Artifact
Validation-layer Definition and JSON Representation families for the two
historical Test Manifest construction forms, individually versioned bounded
Cross-Record Integrity Rules, and one closed Integrity Evaluation Record. It
preserves the ten test manifests and exact static `203/38/165` inventory;
defines thirteen individual rule identities; keeps `satisfied`,
`not-satisfied`, `unverifiable`, and `not-evaluated` outcomes separate; and
requires exact caller-supplied closed offline-first fail-closed processing,
visible role overlap, review-independence and self-acceptance boundaries,
individual evidence/diagnostic/limitation traceability, no aggregate result,
and `automaticAuthority: false`. Acceptance and integration allocate and
activate only the stated Definition, Representation, and Rule identity/version
pairs and create no executable schema, manifest/rule/evaluation instance,
Tool, Implementation, dependency, validator, resolver, runner, graph engine,
workflow, CI, release, publication, support, certification, hosting,
deployment, merge permission, or authority for Package D or E.

The [CNTX Concrete Validation and Integrity Tool and Implementation
Contract](concrete-tool-implementation-contract.md) and
[ADR-0037](adr/0037-concrete-tool-implementation-contract.md) are
**Accepted** as ARCH-037 under issue #120, attributable EIGENAAR / Final
Authority issue-contract acceptance comment `5243736163`, and exact-head
acceptance comment `5243941231`. The documentation-only Package D decision
defines one Tool Identity and initial Tool Version
`1.0.0`, one separate Python/`jsonschema` Implementation Identity and initial
Implementation Version `1.0.0`, one exact supported specification set covering
the ten Accepted Schema Resources, both historical manifest forms, exact
`203/38/165` inventory, Package A/B/C definitions and representations, and the
thirteen Accepted integrity rules. It also defines explicit capabilities and
non-capabilities, exact runtime/dependency pins, closed configuration and
environment responsibilities, bounded logical input/output/diagnostic/evidence
interfaces, deterministic ordering, fail-closed processing, resource and
security/privacy limits, no aggregate result, and `automaticAuthority: false`.
Acceptance and integration allocate and activate only the exact Tool and
Implementation identity/version pairs, supported set, capabilities, pins,
interfaces, and boundaries defined by the decision. They create no dependency
installation, executable schema, instance, evaluator, validator, resolver,
runner, code, library, SDK, CLI, API, workflow, CI, release, publication,
support, certification, hosting, deployment, merge permission, or authority
for Package E.

The [CNTX Epistemic Provenance and Freshness Extension Module
Definition](epistemic-provenance-freshness-extension-module-definition.md) and
[ADR-0038](adr/0038-epistemic-provenance-freshness-extension-module-definition.md)
are **Accepted** as ARCH-038 under issue #128, attributable EIGENAAR / Final
Authority issue-contract acceptance comment `5251980826`, and exact-head
acceptance comment `5252557346` on candidate commit
`e6700258c584deaabf028e8d339680567ed1715f` and tree
`664f00045fc7dcfb26ff2d9cf12c5787c0524493`. The documentation-only Definition
specifies exactly one Extension Module Definition with local name
`epistemic-provenance-freshness`, version-independent
Identifier
`https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness`,
and initial Definition Version `1.0.0`. It defines closed logical
source categories, exact source identity/revision and provenance
responsibilities, separate publication/revision, observation/retrieval,
record-production and valid-through times, explicit digest and policy pins,
clock/reference provenance, derivation, visible condition states, fail-closed
processing, non-aggregation, and `automaticAuthority: false`. Exact-head
acceptance plus separately governed integration to `main` allocates and
activates only this exact Identifier and Version as the integrated Accepted
Definition. Status promotion, branch or repository presence, Ready-for-review,
review, and mergeability do not by themselves integrate, allocate, or activate
it. The Definition creates no
Profile, property, representation, schema, Schema Resource, testcase, rule,
Tool/Implementation Version, dependency, code, runner, execution, evidence,
release, publication, support, certification, hosting, deployment, merge
permission, or follow-on authority.

The [CNTX Context Packet Epistemic Provenance and Freshness Profile
Definition](context-packet-epistemic-provenance-freshness-profile-definition.md)
and
[ADR-0039](adr/0039-context-packet-epistemic-provenance-freshness-profile-definition.md)
are **Accepted** as ARCH-039 under issue #130, attributable EIGENAAR / Final
Authority issue-contract acceptance comment `5254030218`, and exact-head
acceptance comment `5255793839` on candidate commit
`4e0af44a238713f41692ce864b9f3616ff39c4c9` and tree
`927ca72b1f692a045f1746ba800e699d9ee14576`. The documentation-only Definition
specifies one Profile Definition with local name
`context-packet-epistemic-provenance-freshness`, version-independent Profile
Definition Identifier
`https://github.com/CNTX-PROJECT/CNTX/profile-definitions/context-packet-epistemic-provenance-freshness`,
initial Version `1.0.0`, and exactly two Profile Subjects: the Accepted
Context Packet Contract Definition `1.0.0` and Accepted Epistemic Provenance
and Freshness Extension Module Definition `1.0.0`. It only selects and narrows
capabilities from those exact subjects for bounded source roles, exact
identity/revision, provenance, temporal and clock/reference context, applicable
freshness policies, digest boundaries, derivation, visible conditions,
fail-closed individual outcomes, restricted/adverse information,
non-aggregation, and `automaticAuthority: false`. The preceding Proposed status
allocated or activated nothing. Exact-head acceptance plus separately governed
integration to `main` allocates and activates only the exact Identifier and
Version as the integrated Accepted Definition. Status promotion, branch or
repository presence, review, Ready-for-review, and mergeability do not by
themselves integrate, allocate, or activate it. The Definition creates no Profile instance,
property, representation, schema, policy, rule, tool, implementation,
execution, evidence instance, release, publication, support, certification,
hosting, deployment, merge permission, or follow-on authority.

The Accepted [CNTX Epistemic Provenance and Freshness Extension Module JSON
Representation Boundary](epistemic-provenance-freshness-extension-module-json-representation-boundary.md)
and
[ADR-0040](adr/0040-epistemic-provenance-freshness-extension-module-json-representation-boundary.md)
are the first bounded Phase 4A3 dependency. Under issue #139 and attributable
issue-contract acceptance comment `5259097128`, exact-head acceptance comment
`5259328712`, accepted candidate commit
`60d815ed9545c5ab16a4531df9a83cc00ed65340`, and tree
`4671ec2dac4df5029dddaaa5876375ba2b7b749d`, they define one closed
thirteen-property JSON-compatible instance-data model for one bounded source
declaration governed by exact ARCH-038 Definition Identifier/Version pins.
They serialize only the existing six source categories, eight information
conditions, four ARCH-024 outcomes, and separate source, claim, provenance,
temporal, digest, policy, clock/reference, derivation, limitation, and
authority responsibilities. The decision adds nothing to Core Artifact JSON
or Context Packet Schema Version `1.0.0`, allocates no Representation or Schema
Identifier/Version, and creates no `$id`, Schema Resource, testcase, rule,
tool, implementation, execution, evidence instance, release, support,
deployment, or follow-on authority. The preceding Proposed status and
candidate/review state allocated or activated nothing. Exact-head acceptance
established Accepted status only. Later separately governed integration was
squash-merged as commit `97d72439bcad31c144352091cb74eaac342f0ae3` with
exact tree `831c8e953de06a1dd8b124904779653df43543fa`. Integration creates no
Schema Resource, testcase, rule, implementation, execution, evidence instance,
release, support, deployment, or automatic authority.

The Accepted [CNTX Minimal Validation and Integrity Slice Corrective Version
Boundary](minimal-validation-integrity-slice-corrective-version-boundary.md)
and
[ADR-0041](adr/0041-minimal-validation-integrity-slice-corrective-version-boundary.md)
are a bounded correction gate before Phase 4A3.2. Under issue #141 and
attributable issue-contract acceptance comment `5262502160` and exact-head
candidate-acceptance comment `5262723710` on commit
`89f7a46319fd64e517e160b03b390e90bf1534ed` and tree
`2c519280a71491d3484bfebfc809f7e50e3bed50`, they preserve immutable
Tool/Implementation Version `1.0.0` history, define exact Git-blob bytes as the
subject for new repository-file pins, accept only corrective Implementation
Version `1.0.1` as the exact later integration target, and bound the
path-safety change to rejecting colon-bearing relative path segments on every
supported host. Historical invocations and evidence are not overwritten.
Runtime portability, workflows, Actions settings, CI, and Phase 4A3.2 remain
separate. Later governed work integrated ARCH-041 and the bounded corrective
Implementation Version `1.0.1` with its exact execution evidence, without
rewriting Version `1.0.0` history or creating a portability, CI, support,
release, certification, or deployment claim.

The Accepted [CNTX Epistemic Provenance and Freshness Extension Module
Definition Schema Resource](epistemic-provenance-freshness-extension-module-definition-schema-resource.md)
and [ADR-0042](adr/0042-epistemic-provenance-freshness-extension-module-definition-schema-resource.md)
are the bounded Phase 4A3.2 decision under issue #145, attributable Owner /
Final Authority issue-contract acceptance comment `5267576754`, and exact-head
candidate-acceptance comment `5269689952` on commit/tree
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875`. The decision binds one Accepted
Draft 2020-12 Schema Resource at Definition Version `1.0.0`
to the already Accepted `epistemic-provenance-freshness` Module Definition and
supplies [48 separate synthetic cases](../../tests/schemas/extension-modules/epistemic-provenance-freshness/1.0.0/cases.json):
8 expected valid and 40 expected invalid. These counts remain separate from the
historical Core `203/38/165` inventory and form no aggregate score or gate.
The preceding Proposed status allocated or activated nothing. Separately
governed integration acceptance comment `5271035681` and completion comment
`5271254252` record integration through PR #146 at commit/tree
`9f482043f76c792f6c2e1e96eb4a535ee26b3a99` /
`7b2f45791e3b7bff7e856f26fff9b22598c06709`; issue #145 is closed/completed and
the task branch is absent locally and publicly. Integration allocates and
activates only the exact Schema Identifier, Version, and canonical `$id`; it
does not expand Tool support or create a new execution/evidence instance. The
successful candidate execution remains bound only to the accepted candidate
commit/tree above.

The Accepted and integrated [CNTX Context Packet Epistemic Provenance and Freshness Profile
JSON Representation Boundary](context-packet-epistemic-provenance-freshness-profile-json-representation-boundary.md)
and [ADR-0043](adr/0043-context-packet-epistemic-provenance-freshness-profile-json-representation-boundary.md)
are the bounded Phase 4A3.3 decision under issue #147, attributable issue-
contract acceptance comment `5273569440`, and exact-head candidate-acceptance
comment `5277015423` on commit/tree
`05e55ded2a7d0276ee9832b0bdff973b8b19b0d5` /
`d8d5855b0c986f008da2b123cd21f2cd6c6f0b2b`. They define one closed standalone
fourteen-member application record for the exact Accepted Profile Definition,
one exact Context Packet revision, one exact approved Task Contract revision,
and deterministic packet-local associations to exact ARCH-040 Module
declarations. The preceding Proposed status allocated or activated nothing.
Exact-head acceptance and status promotion established Accepted status only.
Separately governed integration acceptance comment `5277937526` and completion
comment `5277961696` record PR #148 integration at public `main` commit/tree
`eec00d698512533c3d40f985fe5d588cd03438f1` /
`87a2d5aaf01e3f7c45b4fb4e3d8aa40a21dc046a`; issue #147 is closed/completed and
the task branch is absent locally and publicly. Integration established only
the exact representation boundary and created no Profile instance, Core
property, schema, case, rule, Tool capability, execution, evidence, aggregate
outcome, release, deployment, or automatic authority.

The Accepted [CNTX Context Packet Epistemic Provenance and Freshness Profile
Definition Schema Resource](context-packet-epistemic-provenance-freshness-profile-definition-schema-resource.md)
and [ADR-0044](adr/0044-context-packet-epistemic-provenance-freshness-profile-definition-schema-resource.md)
form the bounded Phase 4A3.4 decision under issue #149, attributable EIGENAAR /
Final Authority issue-contract acceptance comment `5279967413`, source-
preserving correction addenda `5280408320` and `5280832992`, and exact-head
candidate-acceptance comment `5285702199` on commit/tree
`7420e5d179ab965bfda58780df4f41a08a0b62de` /
`56d1808cb95f3dd5a0b5d84f2a8e440891dff5e6`. The first addendum changes only
the baseline link pins to `1489 Markdown / 27 HTML` and `1297 local / 219
external`; the second changes only the
evaluation-responsibility count from sixteen to seventeen while preserving the
exact seventeen Accepted ARCH-043 members. Neither makes a semantic or
lifecycle change. The decision defines
one standalone JSON Schema Draft 2020-12 resource for the exact ARCH-043
fourteen-member application record, with exactly 52 root `$defs`, `207/207/0`
separate total/internal/external references, finite limits, and one separate
operation-based manifest of 72 fixed cases: 11 expected valid and 61 expected
invalid. The schema is intentionally schema-local: it cannot prove external
packet/task equality, source-association coverage or equality, projected-key
uniqueness, opaque-reference resolution, graph semantics, source truth,
conformance, or authority. The preceding Proposed status allocated or activated
nothing. Accepted status, status promotion, repository presence, schema
parseability, case materialization, validation, review, Ready state, or
mergeability did not by themselves integrate or activate the resource. The successful local
candidate validation remains bound only to the accepted candidate commit/tree
above; this status-only promotion is not a new execution or evidence instance.

Separately governed integration-authority comment `5286010813` and completion
comment `5286062635` record PR #150 integration at public `main` commit/tree
`1d9e4667d68cce6e0289464c821bcd95e1d355ae` /
`3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`; issue #149 is closed/completed and
the task branch is absent locally and publicly. Integration preserved the
accepted schema and case bytes, all historical lifecycle and execution/evidence
pins, the separate Core `203/38/165`, Module `48/8/40`, and Profile `72/11/61`
inventories, and all 12 Schema Resources. It created no Tool support or new
execution/evidence instance.

The Accepted [CNTX Governing Definition Declaration and Frozen Governing
Declaration Set JSON Representation
Boundary](governing-definition-declaration-set-json-representation-boundary.md)
and [ADR-0045](adr/0045-governing-definition-declaration-set-json-representation-boundary.md)
form the bounded documentation-only Phase 4A3.5 decision under issue #151 and
attributable EIGENAAR / Final Authority issue-contract acceptance comment
`5286906192`. Exact-head candidate-acceptance comment `5290871158` accepts
candidate commit/tree `a92cb298a5106db27f0c6b720a5faa3b6571ddf1` /
`1a68548638f0ff570639a051bbca65e778642ca4`. The decision defines one reusable closed fourteen-member
`GoverningDefinitionDeclaration`, maps every exact ARCH-031 declaration
responsibility once, and defines one closed six-member frozen
`GoverningDeclarationSet` preserving all eleven set invariants. It stays outside
every existing Core Artifact Instance and creates no declaration/set identity
or version, package/bundle representation, media type, canonical serialization,
Schema Resource, testcase, Binding, Tool/Implementation, execution, evidence,
approval, release, support, certification, hosting, deployment, or later-phase
authority. The preceding Proposed status allocated or activated nothing.
Exact-head acceptance and status-only promotion established Accepted status
only; validation, review, Draft state, repository presence, and mergeability
did not integrate the decision.

The Accepted promotion commit/tree is
`c7b8c5cc793516197726344e7d30c12d0a86f514` /
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`. Separately governed
[PR #152](https://github.com/CNTX-PROJECT/CNTX/pull/152) integrated that exact
tree into public `main` at commit/tree
`0bccbb39a56044be3a9c7236dd828b1d1959e7ce` /
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`; the promotion-to-integration diff
is empty and the complete trees are equal. Completion comment
[5292133876](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5292133876)
records the integrated result; issue #151 is now `closed/completed`.

The former task branch
`codex/arch-045-governing-declaration-set-json-representation` is absent from
the current local, origin-tracking, and live public-remote views. This is a
present-state observation only; it does not reconstruct, replace, or
retroactively grant historical cleanup authority. Integration changed none of
the representation semantics or later-layer non-effect boundaries above.

The Accepted [CNTX Execution and Task Control Architecture
Boundary](execution-task-control-architecture-boundary.md) and
[ADR-0046](adr/0046-execution-task-control-architecture-boundary.md) form the
documentation-only decision under issue
[#155](https://github.com/CNTX-PROJECT/CNTX/issues/155) and attributable
EIGENAAR / Final Authority issue-contract acceptance comment
[5297998742](https://github.com/CNTX-PROJECT/CNTX/issues/155#issuecomment-5297998742).
The exact accepted baseline is commit/tree
`255e781daf8d691c769c84a71dfdb3bd5b95ad4c` /
`558f87c5ce31500624a7d0a3839b368611735729`, with 208 paths.

Attributable exact-head candidate-acceptance comment
[5298435115](https://github.com/CNTX-PROJECT/CNTX/pull/156#issuecomment-5298435115)
accepts candidate commit/tree
`d8ce562b7d4cf3cb10188216e706f6d4dbebe53a` /
`375345f27d6b122349b8cb7ba4eda5749d372856`.

The Accepted decision keeps one exact approved Task Contract Artifact Revision
controlling, defines exactly four descriptive complexity classes — `light`,
`moderate`, `heavy`, and `complex` — independently from risk and authority,
distinguishes exactly 27 participant/control dimensions, and identifies
exactly twelve conceptual task-control responsibility groups. Minimum context,
least privilege, exact pins, caller-supplied closed frozen input, offline-first
processing, visible fail-closed conditions, non-aggregation, separate
evidence/review/decision, `automaticAuthority: false`, and final human
authority remain explicit.

ARCH-046 allocates no Artifact Type, record, representation, field, token,
state, schema, Tool/Implementation/Model/Skill identity or version, capability,
provider, participant, access, selection, routing, scheduler, orchestrator,
workflow, execution, output, evidence, support, release, deployment, or
authority. Team authority/context, a vertical slice, adapters, portability/CI,
reassessment, release, and deployment remain separate later gates.

The preceding Proposed status allocated or activated nothing. Issue-contract
acceptance authorized only candidate preparation, validation, one commit, one
push, one Draft PR, one transparent non-independent `COMMENTED` review, and the
mandatory exact-head stop. Exact-head acceptance and status-only promotion
established Accepted status only; candidate preparation, validation, review,
Draft state, repository presence, and mergeability did not integrate ARCH-046.
At that lifecycle stage, Ready, integration, merge, closure, synchronization,
cleanup, and every later technical phase remained separately governed.

The Accepted status-only promotion commit/tree is
`7f0b76242c6bcc22b52a0ef7e227126798454364` /
`87ad12a0af13fd0578c84a29175de5d0c75ed7ce`. Separately governed
[PR #156](https://github.com/CNTX-PROJECT/CNTX/pull/156) integrated that exact
tree into public `main` at commit/tree
`198bcd24abd0db9c9b13fb8be4df31168c6b6312` /
`87ad12a0af13fd0578c84a29175de5d0c75ed7ce`, with the prior public `main`
commit `255e781daf8d691c769c84a71dfdb3bd5b95ad4c` as sole parent. The promotion
and integration trees are identical and the complete promotion-to-integration
diff is empty. Completion comment
[5300854335](https://github.com/CNTX-PROJECT/CNTX/issues/155#issuecomment-5300854335)
records the integrated result; issue #155 is `closed/completed` and local,
origin-tracking, and live public `main` were synchronized to the integrated
commit/tree.

The former task branch
`codex/arch-046-execution-task-control-architecture-boundary` is absent from
the current local, origin-tracking, and live public-remote views. This is a
present-state observation only; it does not reconstruct, replace, or
retroactively grant historical cleanup authority. Integration, completion,
synchronization, and branch absence changed none of the decision semantics or
later-layer non-effect boundaries above. This correction authorizes no
follow-on technical execution; every next subject requires its own exact
attributable contract.

</details>

## Document status

- **Proposed** — submitted for review and not yet an accepted repository decision.
- **Accepted** — approved under repository governance and adopted as a binding architecture decision or baseline.
- **Superseded** — replaced by a later accepted decision that identifies the replacement.
- **Deprecated** — retained for reference but discouraged for new use; it is not necessarily replaced.

## Future changes

Future architecture changes MUST start with an approved issue or task contract, identify their intended scope and affected documents, and receive the authority and review required by [governance](../../GOVERNANCE.md). An accepted architecture decision record MUST accompany a consequential architecture change when the core contract requires one. Until then, discussion and proposed documents do not alter accepted architecture.
