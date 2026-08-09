# ADR-0033: CNTX Extension Module and Profile tooling and implementation boundary

- **Status:** Accepted
- **Date:** 2026-08-09
- **Issue:** [#108](https://github.com/CNTX-PROJECT/CNTX/issues/108)
- **Creation authority comment:** [5231158990](https://github.com/CNTX-PROJECT/CNTX/issues/108#issuecomment-5231158990)
- **Exact-head acceptance comment:** [5233773228](https://github.com/CNTX-PROJECT/CNTX/issues/108#issuecomment-5233773228)
- **Decision:** ARCH-033 — CNTX Extension Module and Profile Tooling and
  Implementation Boundary

## Context

Accepted ARCH-028 through ARCH-032 define the conceptual Extension
Module/Profile architecture, Definition identity/version policy, explicit
dependency and activation model, composition and fail-closed conflict rules,
Schema Resource/package/declaration model, and executable-schema validation and
conformance boundary.

No Accepted decision yet distinguishes tool and implementation categories;
separates their identities, versions, capabilities, environments, outputs,
evidence, conformance, support, release, and deployment dimensions; defines the
frozen context for consequential execution; or constrains a future reference
implementation. Without that boundary, implementation behavior could silently
be mistaken for normative meaning, authority, compatibility, or conformance.

## Decision

Define one conceptual Extension Module/Profile Tooling and Implementation
Boundary.

Keep sixteen categories distinct: specification authoring/consistency;
Definition/source/provenance inspection; closed supply/resolution/catalog
views; dependency/activation/composition/conflict evaluation; Schema
Resource/package/bundle tooling; schema evaluation/validation orchestration;
output/diagnostic presentation; evidence capture/reproduction; test
runner/conformance suite; reference implementation; reusable library/SDK;
CLI/API; workflow/automation/engine/scheduler/orchestrator; runtime/product
integration; hosted service/registry/publication/distribution; and
support/compatibility/certification/deployment.

Keep Tool Identity, Tool Version, Implementation Identity, Implementation
Version, supported exact specification set, capability profile, configuration,
dependency set, environment, supplied governing inputs, output, evidence,
conformance, interoperability, compatibility, security/privacy, support,
certification, release, and deployment separate. No dimension implies another.

Require every consequential future execution to use one closed, frozen, and
exactly pinned context containing governing Core and Definition sources,
identities, versions, revisions, provenance, declarations, active Definition
Set, dependencies, Profile Subjects, Schema Resource key-or-`None` bindings,
resource graph, package, Serialization Binding where applicable, tool and
implementation identities/versions where defined, supported specifications,
capabilities, dependencies, configuration, environment, targets, resource
limits, provenance, output boundaries, limitations, adverse/restricted
evidence, non-execution, claimant, roles, and authority.

Require caller-supplied, exact, closed, frozen, offline-first processing.
Prohibit automatic discovery or retrieval, redirects, network authority,
hidden cache, ambient state, mutable aliases, `latest`, substitution, coercion,
defaulting, repair, fallback, silent capability downgrade, and order- or
popularity-based meaning.

Keep governing-input mismatches, missing, duplicate, conflicting, ambiguous,
unknown, unsupported, assertion-failure, processing-failure, warning,
limitation, resource-blocked, security/privacy-ambiguous,
restricted-evidence, Unverifiable, blocked, non-executed, and adverse conditions
separate, visible, and fail closed.

Keep all tool output bounded to one exact execution. Output is not canonical
Validation Output, Portable Conformance Evidence, an Evidence Bundle, Review
Record, Decision Record, certification, release record, or Artifact Instance
without separately Accepted identity, schema, binding, provenance, lifecycle,
and instance contracts.

Keep any future reference implementation non-normative. It cannot fill a
specification gap, resolve ambiguity as precedent, modify Core or Definition
semantics, allocate identity, create activation or precedence, prove
conformance, create lock-in, or exclude another conforming implementation.
Implementation-defined behavior must remain explicit, bounded, attributable,
and without normative authority.

Require future implementation contracts to bound untrusted inputs, counts,
sizes, graph depth and breadth, recursion, reference expansion, regular-
expression and evaluation cost, memory, CPU, wall time, concurrency, file
descriptors, output, diagnostics, logs, temporary storage, minimization,
access, disclosure, restricted evidence, cleanup, and network behavior. Select
no concrete limit or mechanism here.

Keep specification, Definition/resource, declaration, package, schema,
Artifact, validator, tool, implementation, interoperability, compatibility,
security/privacy, support, certification, release, deployment, and final-human
authority dimensions separate. Successful execution proves no broader claim
or authority.

Require separate dependency-first lifecycles before concrete work: concrete
Definitions; concrete Schema Resources/cases; concrete declaration/package/
binding/output/evidence identities; concrete Tool/Implementation identity,
version, capability, configuration, dependency, and interface contracts;
implementation and evidence; independent review/assessment/decision; and any
release, publication, distribution, support, certification, hosting, or
deployment.

## Consequences

Positive consequences:

- tools and implementation behavior cannot silently become normative sources;
- exact execution context and provenance bound every consequential result;
- capabilities, outputs, evidence, conformance, support, release, and
  deployment remain independently reviewable;
- failures, limitations, unsupported behavior, restricted evidence, and
  non-execution remain visible;
- reference behavior cannot create precedent, lock-in, or authority;
- resource, security, and privacy boundaries precede concrete selection; and
- attributable final-human authority remains separate from execution.

Costs and limitations:

- callers must supply complete exact governing inputs and provenance;
- no ambient discovery, mutable selection, hidden cache, repair, or fallback is
  available;
- no concrete tool/implementation identity, capability, configuration,
  interface, output, or evidence representation exists;
- no validator, runner, suite, library, SDK, CLI, API, workflow, runtime,
  product, service, or reference implementation is created; and
- no conformance, interoperability, compatibility, security/privacy, support,
  certification, release, or deployment claim is proven.

## Alternatives not selected

### Let a reference implementation define ambiguous behavior

Not selected because implementation behavior has no normative authority and
would create precedent and lock-in outside attributable governance.

### Infer governing inputs from installation or availability

Not selected because repository, registry, cache, network, package, or product
presence does not establish identity, activation, acceptance, trust, or
authority.

### Treat successful execution as broad conformance

Not selected because schema evaluation, tool behavior, implementation
conformance, interoperability, compatibility, security/privacy, support,
certification, release, and deployment are separate claims.

### Select a concrete implementation stack now

Not selected because no concrete Definition, Definition Schema Resource,
serialized declaration/package/output/evidence model, Tool Identity, or
Implementation Identity is authorized.

## Non-decisions

This ADR creates no concrete Definition, Schema Resource, executable schema,
assertion, case, declaration representation, package, binding, output/evidence
Artifact Instance, portable vocabulary, Tool or Implementation Identity or
Version, capability/configuration/interface contract, resolver, registry,
catalog, cache, bundler, mirror, redirect, network behavior, validator, test
runner, conformance suite, SDK, library, API, CLI, workflow, automation,
engine, scheduler, orchestrator, runtime/provider/product work, private or
reference implementation, hosted service, release, publication, distribution,
support, certification, deployment, audit, remediation, external-model
interaction, optimization, ARCH-034, or follow-on authority.

## Authority boundary

This ADR is Accepted. Creation authority, repository presence, validation, and
transparent non-independent ARCHITECT review did not grant acceptance.

Separate attributable EIGENAAR / Final Authority exact-head acceptance is
recorded in issue comment `5233773228`; separately authorized governed
promotion and integration make this decision Accepted. Acceptance adopts only
the conceptual boundary and creates or authorizes no concrete tool,
implementation, release, publication, support, certification, hosting, or
deployment.
