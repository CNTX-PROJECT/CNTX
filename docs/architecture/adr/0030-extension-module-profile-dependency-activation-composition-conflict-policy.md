# ADR-0030: CNTX Extension Module and Profile dependency, activation, composition, and conflict policy

- **Status:** Accepted
- **Date:** 2026-08-09
- **Issue:** [#102](https://github.com/CNTX-PROJECT/CNTX/issues/102)
- **Creation authority comment:** [5230085538](https://github.com/CNTX-PROJECT/CNTX/issues/102#issuecomment-5230085538)
- **Exact-head acceptance comment:** [5230166187](https://github.com/CNTX-PROJECT/CNTX/issues/102#issuecomment-5230166187)
- **Decision:** ARCH-030 — CNTX Extension Module and Profile Dependency,
  Activation, Composition and Conflict Policy

## Context

Accepted ARCH-028 separates Extension Modules from Profiles, protects Core
sovereignty, requires explicit exact-version opt-in, and orders later decisions
dependency-first. Accepted ARCH-029 defines the two definition families,
stable family namespaces, child-allocation rule, and independent Definition
Identifier and Definition Version policy.

No Accepted decision yet states how exact future definitions may depend on one
another, become explicitly active, form a complete frozen dependency graph,
compose without implicit precedence, or fail closed on conflicts, unknown
definitions, and unsupported mechanisms. Executable declaration or schema work
cannot safely precede those semantics.

## Decision

Adopt an exact-keyed, explicit, closed, caller-supplied, and fail-closed policy
for future Extension Module/Profile dependency, activation, composition, and
conflict handling.

Every consequential definition dependency and activation pins the complete
Definition Identifier and Definition Version. Mutable aliases, ranges,
`latest`, automatic upgrades, ambient selection, and implementation or product
preference grant no selection authority.

Keep required dependencies, optional dependencies, Profile Subjects,
activation roots, active definitions, dependency closure, applicability,
compatibility, conformance, evidence, and authority separate. These are logical
responsibilities and allocate no serialized fields or tokens.

Require one frozen activation context with exact roots, an explicit active
Definition Set, authoritative sources and revisions, exact Core inputs,
dependency relations, provenance, limitations, unknown/unsupported conditions,
and conflicts. Every active definition must be an explicit root or explicitly
listed and reachable by a permitted declared dependency. Presence, installation,
repository location, registry, cache, network availability, implementation
support, or previous validation activates nothing.

Require a finite directed acyclic dependency graph, no self-dependency, complete
transitive required closure, and at most one active Definition Version for one
Definition Identifier. Reject conflicting sources or revisions for one exact
key. Create no multi-version isolation or negotiation.

Preserve dependency direction:

- Core never depends on an Extension Module or Profile;
- Extension Modules may depend on exact Core inputs and exact Extension Module
  Definitions, never Profiles;
- Profiles may select or narrow exact Core and Extension Module subjects,
  never depend on Profiles; and
- multiple Profiles are separately active roots and apply conjunctively.

Apply Core first, Extension Modules in dependency-topological order, and
Profiles after their subjects. Dependency order is not precedence. All valid
topological orders must have equivalent meaning or composition fails closed.

Extension Modules may add only non-conflicting capability within their
separately Accepted responsibility. Profiles may only select, require, limit,
or narrow and cannot create absent capability. Multiple Profiles form the
intersection of their constraints. Contradiction, empty meaning, ambiguity,
absent capability, version conflict, implicit precedence, or order dependence
blocks composition.

Treat Core contradiction, identity/version ambiguity, multiple versions,
missing/wrong/undeclared/unreachable dependency, self-dependency, cycle,
unsupported mechanism, unknown required definition, conflicting source,
module collision, Profile contradiction, absent capability, order dependence,
unknown precedence, insufficient evidence, security/privacy conflict,
inaccessible required evidence, and unbounded processing as fail-closed
conditions.

Prohibit silent conflict resolution by document/load/registration/insertion/
lexical order, specificity guess, newest/latest/latest-wins, popularity, cache,
implementation or product preference, majority, consensus, score, ranking, or
fallback.

Preserve the caller-supplied, offline-first, closed supply boundary and no
automatic network access. Keep compatibility and every conformance dimension
scoped to exact inputs, sources, context, evidence, capabilities, limitations,
claimant, time, and authority.

Preserve untrusted-input, resource, provenance, restricted-evidence,
minimization, least-privilege, disclosure, correction/withdrawal, public/private,
and final human authority boundaries without choosing an implementation.

## Consequences

Positive consequences:

- future activation is explicit and reproducible;
- dependency graphs are exact, finite, acyclic, and provenance-bearing;
- Core sovereignty and permitted dependency direction remain enforceable;
- modules cannot silently override and Profiles cannot widen;
- multiple Profiles have one deterministic conjunctive meaning;
- conflict and unsupported conditions remain visible and fail closed; and
- executable declaration, schema, and tooling remain behind required
  architecture.

Costs and limitations:

- callers must supply the full exact active set and dependency closure;
- ranges, aliases, ambient discovery, automatic upgrades, and fallback are not
  available;
- multiple versions of one definition cannot coexist in one frozen context;
- Profile-to-Profile dependency is not permitted;
- unknown or unsupported active material blocks dependent claims;
- no concrete declaration representation, portable conflict output, schema,
  resolver, validator, or tooling exists; and
- compatibility, interoperability, support, and security/privacy are not
  proven.

## Alternatives not selected

### Infer activation from installation or repository presence

Not selected because availability cannot establish exact opt-in, applicability,
authority, or reproducible governing context.

### Allow version ranges or `latest`

Not selected because mutable selection prevents exact provenance and stable
evidence and can change meaning without changing the governing input.

### Allow Profiles to depend on Profiles

Not selected for this boundary because it adds recursive selection,
precedence, and compatibility complexity. Multiple Profiles instead remain
independently selected activation roots and combine conjunctively.

### Let load order establish precedence

Not selected because ordering would silently redefine normative meaning and
make equivalent supplied sets produce different outcomes.

### Merge conflicting module or Profile content automatically

Not selected because merge, overlay, specificity, newest-wins, or
implementation preference would create undeclared authority.

### Define fields, manifests, or executable schemas now

Not selected because conceptual dependency, activation, composition, and
conflict semantics must be Accepted before their representation can be safely
designed.

## Non-decisions

This ADR creates no concrete Extension Module/Profile, child Identifier or
active Version, range, executable grammar, precedence, declaration field/token,
portable conflict/output vocabulary, type, vocabulary, `$id`, Schema Resource,
schema, payload, manifest, package, registry, catalog, resolver, cache, bundler,
mirror, redirect, network behavior, validator, runner, conformance suite,
canonical JSON, digest, signature, verification, attestation, media type, or
Serialization Binding.

It creates no Artifact Instance, Extension Module/Profile instance, API, CLI,
workflow, automation, engine, scheduler, orchestrator, runtime, provider or
product work, private/reference implementation, support service, release,
publication, distribution, deployment, maintenance, correction, withdrawal,
deprecation, supersession, reassessment, settings mutation, ARCH-031, or
follow-on authority.

## Authority boundary

This ADR is Accepted. Creation authority, repository presence, validation, and
transparent non-independent ARCHITECT review did not grant acceptance.

Separate attributable EIGENAAR / Final Authority exact-head acceptance and
separately authorized governed promotion and integration make this decision
Accepted. Acceptance adopts only the conceptual policy and creates or activates
no concrete Extension Module, Profile,
declaration, schema, tooling, implementation, release, publication, or
deployment.
