# ADR-0029: CNTX Extension Module and Profile identity and version policy

- **Status:** Proposed
- **Date:** 2026-08-09
- **Issue:** [#100](https://github.com/CNTX-PROJECT/CNTX/issues/100)
- **Creation authority comment:** [5228909425](https://github.com/CNTX-PROJECT/CNTX/issues/100#issuecomment-5228909425)
- **Decision:** ARCH-029 — CNTX Extension Module and Profile Identity and
  Version Policy

## Context

Accepted ARCH-028 separates possible Extension Modules from Profiles,
preserves Core sovereignty, requires explicit exact-version opt-in, keeps
identity/version/provenance/authority/activation responsibilities distinct,
and orders later decisions dependency-first. Its first prerequisite is a
general identity and version policy.

Without stable family namespaces, an exact allocation rule, independent
version lines, change classification, immutability, and future allocation
gates, later dependency or declaration work could confuse repository presence,
URLs, implementations, mutable aliases, or release versions with normative
identity and authority.

## Decision

Define four separate dimensions:

1. Extension Module Definition Identifier;
2. Extension Module Definition Version;
3. Profile Definition Identifier; and
4. Profile Definition Version.

Adopt two separate logical families:

- `CNTX Extension Module Definition Family` with stable base
  `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions`;
- `CNTX Profile Definition Family` with stable base
  `https://github.com/CNTX-PROJECT/CNTX/profile-definitions`.

A future child Definition Identifier has form `{family-base}/{local-name}`.
The local name must match exact lowercase ASCII kebab-case
`^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$`. The Identifier contains no Definition
Version, query, fragment, or mutable alias.

Treat every HTTPS-shaped Identifier as opaque. It grants no dereferencing,
retrieval, redirect, registry, discovery, cache, network, trust, acceptance,
activation, compatibility, conformance, or support authority.

Every future separately Accepted concrete definition starts at independent
Definition Version `1.0.0`. Candidate and repository revisions do not consume
Definition Versions. There is no family-wide version, lockstep, automatic
propagation, or inferred compatibility from equal or different numbers.

Use `MAJOR.MINOR.PATCH`:

- MAJOR for breaking normative change or insufficiently demonstrated backward
  compatibility;
- MINOR only for evidence-backed backward-compatible normative additions
  within the same responsibility; and
- PATCH only for nonsemantic correction or clarification.

Compatibility uncertainty fails closed. A Profile restriction is not
automatically backward compatible merely because it is additive text.

Keep the same Identifier across MAJOR versions while the same responsibility
continues. Allocate a new Identifier only for a genuinely distinct,
independently governed responsibility, never to evade breaking-change,
history, correction, withdrawal, deprecation, supersession, or adverse-evidence
boundaries.

Make each Accepted Definition Version immutable. Require a separate exact
lifecycle for later correction or change. Mutable aliases, `latest`,
latest-wins, newest-wins, and ambient selection have no authority.

Until separately Accepted compatibility architecture exists, require complete
exact Definition Identifier and Definition Version pins. Define no range,
wildcard, negotiation, precedence, resolver selection, fallback, upgrade, or
downgrade behavior here.

Allocate no concrete child Definition Identifier or active Definition Version.
Every future child requires a separate exact baseline, allocation,
responsibility, authoritative source, provenance, evidence, review,
attributable EIGENAAR / Final Authority acceptance, and integration.

Preserve Accepted Core sovereignty. Identity/version activates nothing and
cannot modify, weaken, reinterpret, coerce, default, repair, or fall back
around Core semantics. Future activation requires separately Accepted explicit
exact-version opt-in under a frozen governing context.

Preserve security, privacy, provenance, public/private separation, fail-closed
uncertainty, and final human authority. Identity/version proves no
authenticity, integrity, compatibility, conformance, support, approval,
security, privacy, legal status, or release status.

## Consequences

Positive consequences:

- Module and Profile definitions have distinct stable identity spaces;
- versions remain separate from identifiers and every other version dimension;
- future allocations are exact, independently governed, and traceable;
- Accepted versions cannot be silently rewritten;
- breaking and uncertain changes fail closed into MAJOR treatment; and
- later dependency/activation work can rely on exact pins without inventing
  ambient authority.

Costs and limitations:

- no concrete Extension Module or Profile is yet allocated;
- no dependency, compatibility range, activation, composition, conflict,
  declaration, resource, schema, or implementation mechanism exists;
- exact pins remain required; and
- every concrete allocation and consequential change requires a separate
  governed lifecycle.

## Alternatives not selected

### Put versions inside Definition Identifiers

Not selected because identity and version are separate dimensions and stable
identity must remain continuous across versions.

### Use repository paths or filenames as identifiers

Not selected because storage location is mutable representation and grants no
normative authority.

### Use one shared family or version line

Not selected because Extension Modules and Profiles have different
responsibilities and every definition changes independently.

### Use `latest`, automatic discovery, or resolver-selected versions

Not selected because mutable or ambient selection prevents a frozen,
reproducible governing context.

### Allocate a concrete starter Module or Profile now

Not selected because this decision establishes only family-level identity and
version policy. Every child needs its own separately authorized definition and
lifecycle.

## Non-decisions

This ADR creates no concrete Extension Module/Profile, child Identifier or
active Definition Version, dependency/compatibility range, precedence,
activation, composition, conflict resolution, declaration token, field, type,
vocabulary, `$id`, Schema Resource, executable schema, payload, manifest,
package, registry, catalog, resolver, cache, bundler, mirror, redirect,
validator, conformance suite, canonical JSON, digest, signature, verification,
attestation, media type, or Serialization Binding.

It creates no Artifact Instance, Module/Profile instance, API, CLI, workflow,
automation, runtime, provider/product work, private/reference implementation,
support service, hosted publication, distribution, release, tag, GitHub
Release, deployment, maintenance action, correction, withdrawal, deprecation,
supersession, reassessment, ARCH-030, or follow-on authority.

## Dependency-first handoff

Only after separate exact-head acceptance and integration of this decision may
a separate Dependency, Activation, Composition and Conflict decision be
considered. No ARCH number, issue, branch, path, Identifier, Version, or
authority is reserved for it here.

## Authority boundary

This ADR is Proposed. Creation authority, repository presence, validation,
transparent non-independent ARCHITECT review, mergeability, and technical
access do not grant acceptance.

Separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision is required before promotion or integration. Any later
acceptance would adopt only this policy and would not allocate, activate,
represent, validate, implement, publish, distribute, or deploy an Extension
Module or Profile or authorize another phase.
