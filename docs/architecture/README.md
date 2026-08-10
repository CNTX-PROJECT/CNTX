# CNTX Architecture

## Reading guide

[The core architecture contract](core-contract.md) is the accepted normative conceptual architecture baseline for CNTX. It specifies public-core concepts and constraints, not an executable architecture. [ADR-0001](adr/0001-public-core-boundaries.md) records the accepted decision that establishes the public-core boundary. [The contract identity and versioning contract](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) are accepted additions: ARCH-001 remains the accepted core baseline, ARCH-002 is an accepted extension of that baseline, and [the artifact-contract and schema-layering contract](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) are the accepted ARCH-003 extension of that baseline. [The Common Artifact Envelope schema boundary](common-artifact-envelope-schema-boundary.md) and [ADR-0004](adr/0004-common-artifact-envelope-schema-boundary.md) are the accepted ARCH-004 conceptual boundary for future common-envelope schema work; they do not alter existing artifact contracts or authorize executable schema work. [The Common Artifact Envelope representation boundary](common-artifact-envelope-representation-boundary.md) and [ADR-0005](adr/0005-common-artifact-envelope-representation-boundary.md) are the accepted ARCH-005 documentation-only refinement that identifies future representation obligations and decision order without selecting fields, schema technology, serialization, validation, or implementation. [The Common Artifact Envelope schema identity and initial version policy](common-artifact-envelope-schema-identity-version-policy.md) and [ADR-0006](adr/0006-common-artifact-envelope-schema-identity-version-policy.md) are the **Accepted**, documentation-only ARCH-006 allocation of one technology-neutral logical identity and the `1.0.0` initial accepted version target; they create no concrete Schema Identifier, executable schema, active Schema Version, schema-language choice, serialization, validation, runtime, or implementation. [The Common Artifact Envelope schema language and dialect](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) are the **Accepted**, documentation-only ARCH-007 selection of JSON Schema Draft 2020-12 with its standard vocabulary profile; they create no executable schema, concrete `$id`, composition or packaging model, artifact Serialization Binding, validator, runtime, or implementation. [The Common Artifact Envelope schema composition and packaging](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) are the **Accepted**, documentation-only ARCH-008 selection of one canonical root resource, internal `$defs`, static exact-version references, standalone canonical resources, derived identity-preserving bundles, and offline-first resolution; they create no executable schema, concrete `$id`, active Schema Version, artifact Serialization Binding, validator, runtime, or implementation. [The Common Artifact Envelope executable schema definition](common-artifact-envelope-executable-schema.md) and [ADR-0009](adr/0009-common-artifact-envelope-executable-schema.md) are the **Accepted** ARCH-009 binding of the one logical Common Artifact Envelope identity to JSON Schema Draft 2020-12 Schema Version `1.0.0`, with a closed six-property envelope, nine canonical Artifact Type tokens, coupled identity/version pins, optional provenance references, and optional digest evidence. Acceptance and schema validity do not define artifact-specific payload or relationships, select an artifact Serialization Binding, or provide authority, a validator, resolver, runtime, product, release, or deployment. The [`adr/`](adr/) directory is the location for architecture decision records. Accepted architecture governs the artifact-specific contracts listed in the [contract index](../contracts/README.md). CONTRACT-001, the Project Charter artifact contract, remains **Accepted** and is a binding, subordinate artifact-specific contract governed by ARCH-001, ARCH-002, and ARCH-003. CONTRACT-002, the Workstream artifact contract, remains **Accepted** and is a binding, subordinate artifact-specific contract governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001. CONTRACT-003, the [Task Contract artifact contract](../contracts/task-contract-artifact-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, accepted CONTRACT-001, and accepted CONTRACT-002. It does not alter or redefine accepted architecture, Project Charter, or Workstream. Only a separately approved change to the applicable higher architecture documents can alter that architecture.

CONTRACT-004, the [Context Packet artifact contract](../contracts/context-packet-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, and CONTRACT-003. It does not alter or redefine accepted architecture, Project Charter, Workstream, or Task Contract.

CONTRACT-005, the [Execution Result artifact contract](../contracts/execution-result-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001, CONTRACT-002, CONTRACT-003, and CONTRACT-004. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, or Context Packet.

CONTRACT-006, the [Evidence Bundle artifact contract](../contracts/evidence-bundle-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-005. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, or Execution Result.

CONTRACT-007, the [Review Record artifact contract](../contracts/review-record-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-006. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, or Evidence Bundle.

CONTRACT-008, the [Decision Record artifact contract](../contracts/decision-record-contract.md), is **Accepted**, binding, and subordinate, and is governed by ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-007. It does not alter or redefine accepted architecture, Project Charter, Workstream, Task Contract, Context Packet, Execution Result, Evidence Bundle, or Review Record.

CONTRACT-009, the [State Snapshot artifact contract](../contracts/state-snapshot-contract.md), is **Accepted**, documentation-only, binding, and subordinate to accepted ARCH-001, ARCH-002, ARCH-003, and accepted CONTRACT-001 through CONTRACT-008. It specializes State Snapshot semantics only and does not alter accepted architecture, any accepted artifact contract, or final human authority. CONTRACT-001 through CONTRACT-009 are **Accepted**.

This architecture documentation is read with the repository [README](../../README.md), [agent instructions](../../AGENTS.md), [governance](../../GOVERNANCE.md), and [security policy](../../SECURITY.md). The README describes the project and its current status. `AGENTS.md` sets execution constraints and source precedence. `GOVERNANCE.md` assigns decision authority and approval. Normative architecture states what the public core requires conceptually; governance assigns who may approve it; implementation is future conforming work; and non-binding discussion is neither an approved decision nor an authority source.

No executable runtime, selector, retrieval system, provider integration, validator, or product functionality is implemented here. ARCH-009 introduces one Accepted executable Common Artifact Envelope Schema Resource only; it is not an artifact-specific schema, a complete artifact definition, a Serialization Binding, or an implementation.

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

## Document status

- **Proposed** — submitted for review and not yet an accepted repository decision.
- **Accepted** — approved under repository governance and adopted as a binding architecture decision or baseline.
- **Superseded** — replaced by a later accepted decision that identifies the replacement.
- **Deprecated** — retained for reference but discouraged for new use; it is not necessarily replaced.

## Future changes

Future architecture changes MUST start with an approved issue or task contract, identify their intended scope and affected documents, and receive the authority and review required by [governance](../../GOVERNANCE.md). An accepted architecture decision record MUST accompany a consequential architecture change when the core contract requires one. Until then, discussion and proposed documents do not alter accepted architecture.
