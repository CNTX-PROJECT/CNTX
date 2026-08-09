# CNTX Extension Module and Profile Identity and Version Policy (ARCH-029)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only architecture decision governed
by [issue #100](https://github.com/CNTX-PROJECT/CNTX/issues/100) and recorded by
[ADR-0029](adr/0029-extension-module-profile-identity-version-policy.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in issue
comment `5228909425`, and exact-head acceptance is recorded in issue comment
`5229936609`.

Creation authority, repository presence, validation, and transparent
non-independent review did not grant acceptance. Separate attributable
EIGENAAR / Final Authority acceptance of the exact reviewed revision and
separately authorized governed promotion and integration make this decision
Accepted.

## Purpose and decision boundary

Accepted ARCH-028 separates possible future Extension Modules from Profiles,
preserves CNTX Public Core sovereignty, requires explicit opt-in and exact
pins, and orders later decisions dependency-first. Its first required later
decision is identity and version policy.

This decision defines only:

1. separate Extension Module Definition and Profile Definition identity and
   version dimensions;
2. two stable logical definition families and public family namespaces;
3. one exact child-identifier allocation rule;
4. independent initial and subsequent Definition Version rules;
5. identity continuity and Accepted-version immutability;
6. future allocation, provenance, authority, and exact-pin gates; and
7. security, privacy, public/private, Core-sovereignty, and non-authority
   boundaries.

It creates no concrete Extension Module or Profile, allocates no child
Identifier, activates no child Definition Version, and defines no dependency,
activation, composition, conflict, resource, declaration, schema, validation,
tooling, or implementation mechanism.

## Exact decision basis

This decision was prepared on exact public baseline
`43306b020e2f0d90b2320f9f3846c3dd4c32b835` and tree
`d5bdb89deb62d8191eec441fc77e2679ff8dbfad`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-028 and ADR-0001 through ADR-0028;
- CONTRACT-001 through CONTRACT-009;
- one Accepted Common Artifact Envelope Schema Version `1.0.0`;
- nine Accepted artifact-specific Schema Versions `1.0.0`;
- ten unchanged synthetic validation manifests;
- Accepted Core Artifact JSON Binding Version `1.0.0`;
- the Accepted Schema Resource Resolution and Catalog Boundary;
- the Accepted Validation and Validation Output Contract;
- the Accepted Portable Conformance Evidence Boundary;
- Accepted assessment, remediation, release-policy, final-decision, release,
  verification, completion, and maintenance sources; and
- immutable prerelease `0.1.0-prealpha.1` and its exact historical objects.

This decision changes none of those sources, identities, versions, assertions,
expected results, evidence, limitations, statuses, or authority.

## Separate definition dimensions

This decision defines four separate dimensions:

1. `Extension Module Definition Identifier`;
2. `Extension Module Definition Version`;
3. `Profile Definition Identifier`;
4. `Profile Definition Version`.

No dimension substitutes for or implies another. In particular, these
dimensions remain separate from:

- Artifact Type;
- Artifact Instance Identifier and Artifact Revision;
- Contract Definition Identifier and Contract Definition Version;
- Schema Identifier and Schema Version;
- Serialization Binding Identity and Serialization Binding Version;
- document status and lifecycle status;
- repository path, filename, Git commit, tree, or blob;
- digest, signature, or provenance record;
- validator or implementation identity and version; and
- Release Identity and Release Version.

A Definition Identifier or Definition Version creates no authority,
acceptance, activation, authenticity, trust, compatibility, conformance,
support, security, privacy, legal status, or release status.

## Definition families and category separation

### CNTX Extension Module Definition Family

`CNTX Extension Module Definition Family` is the logical family for possible
future independently governed Extension Module Definitions. A future member
may describe only an additive capability within a separately Accepted scope.

This family is not the CNTX Public Core, a Profile Definition family, an
Artifact Type, a Schema family, a Serialization Binding, an implementation, a
product feature, or a release line.

### CNTX Profile Definition Family

`CNTX Profile Definition Family` is the logical family for possible future
independently governed Profile Definitions. A future member may describe only
an explicit selection or constraint over exact pinned inputs under separately
Accepted architecture.

This family is not an Extension Module Definition family, the CNTX Public
Core, an Artifact Type, a Schema family, a validator configuration, a product
edition, or a deployment configuration.

### Family non-equivalence

An Extension Module Definition is not a Profile Definition. A Profile
Definition is not an Extension Module Definition. Identity or version in one
family does not allocate, activate, select, constrain, support, or establish
compatibility with a member of the other family.

There is no family-wide active version, shared version line, or lockstep
versioning.

## Stable family namespaces

The stable, public, version-independent family bases are:

| Family | Exact family base |
| --- | --- |
| CNTX Extension Module Definition Family | `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions` |
| CNTX Profile Definition Family | `https://github.com/CNTX-PROJECT/CNTX/profile-definitions` |

A future concrete Definition Identifier has exactly this logical form:

`{family-base}/{local-name}`

The family base and complete Definition Identifier contain no Definition
Version. Definition Version is a separate dimension and must be supplied as a
separate exact pin wherever a future governing context requires it.

### Opaque HTTPS boundary

The HTTPS-shaped family bases and future Definition Identifiers are opaque
identifiers. They do not authorize or require:

- dereferencing or automatic retrieval;
- network access or redirect following;
- discovery, registry, catalog, cache, or mirror lookup;
- access, disclosure, authentication, or trust;
- acceptance, activation, authority, or support; or
- compatibility or conformance.

Repository location, URL availability, an HTTP response, filename, path, host,
registry listing, installation, implementation recognition, processor
capability, product use, popularity, or previous successful validation does
not create semantic authority.

## Exact child allocation rule

A future `local-name` must match exactly:

`^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$`

The rule means:

- the first character is a lowercase ASCII letter;
- later characters within a segment are lowercase ASCII letters or digits;
- optional further non-empty segments are separated by exactly one hyphen;
- uppercase letters and non-ASCII letters are prohibited;
- whitespace, slash, backslash, query, and fragment are prohibited;
- empty segments, doubled hyphens, and trailing hyphens are prohibited; and
- a version or mutable selection alias is not part of the Identifier.

Aliases such as `latest`, `current`, `stable`, `recommended`, or an equivalent
mutable selector cannot become version or selection authority.

This decision allocates only the two family bases and the allocation rule. It
does not allocate or reserve a concrete `local-name` or complete child
Identifier.

## Future allocation and acceptance gate

A future concrete Extension Module Definition Identifier or Profile Definition
Identifier is not allocated, Accepted, or activated merely by:

- discussion, documentation draft, issue, branch, or candidate commit;
- repository path, filename, schema `$id`, URL, or media type;
- catalog, registry, cache, mirror, package, or manifest presence;
- implementation, installation, processor capability, or product use;
- publication, popularity, or release-channel presence; or
- previous successful validation.

Every future concrete definition requires its own exact public lifecycle with:

1. an exact public baseline and tree;
2. one unique allocation under the correct family base;
3. a concrete Definition Identifier and Definition Version;
4. one bounded responsibility and explicit non-responsibilities;
5. an authoritative public definition source;
6. source and authority provenance;
7. exact task, issue, branch, path, and change scope;
8. evidence, validation, limitations, and adverse information;
9. review of the exact candidate revision;
10. attributable EIGENAAR / Final Authority acceptance; and
11. separately governed integration and completion.

Proposed, candidate, or reviewed states remain inactive and consume no
Definition Version.

## Initial Definition Version

Every future separately Accepted concrete Extension Module Definition and
every future separately Accepted concrete Profile Definition starts at exact
Definition Version:

`1.0.0`

The initial version is independent for every concrete definition. This
decision creates no active child definition, activates no `1.0.0`, reserves no
child version, and creates no aggregate family version.

Candidate, review, correction, promotion, merge, and repository commits are
lifecycle revisions. They do not by themselves consume a Definition Version
or require a PATCH increment.

The Definition Version dimension is independent of every Contract Definition,
Schema, Serialization Binding, Artifact, implementation, validator, and
Release Version.

## Independent version lines

Every concrete Extension Module Definition and Profile Definition versions
independently. Therefore:

- no family-wide Definition Version exists;
- no lockstep versioning exists;
- no version change propagates automatically;
- equal version values do not establish equivalence or compatibility;
- different version values do not establish incompatibility; and
- a change to one definition does not change another definition unless the
  other definition's own normative content changes through its own lifecycle.

## MAJOR.MINOR.PATCH policy

A Definition Version uses `MAJOR.MINOR.PATCH` with no omitted component.

### MAJOR

A MAJOR increment is required for a breaking normative change, including:

- changing existing valid meaning or making previously conforming use no
  longer conforming;
- adding a mandatory meaning, constraint, dependency, or activation condition;
- weakening a previously stated guarantee;
- changing authority, provenance, privacy, security, disclosure, correction,
  withdrawal, deprecation, supersession, or other lifecycle boundaries;
- requiring existing consumers to interpret the same definition differently;
- materially changing the definition's responsibility; or
- lacking sufficient evidence that a normative change is backward compatible.

Compatibility uncertainty fails closed. It cannot silently be classified as
MINOR or PATCH.

### MINOR

A MINOR increment is permitted only for an evidence-backed,
backward-compatible normative addition within exactly the same definition
responsibility.

A Profile change that adds a mandatory restriction, removes an allowed choice,
or weakens a prior guarantee is not automatically MINOR. Direction and scope
of compatibility must be explicit and evidence-backed.

### PATCH

A PATCH increment is permitted only for a nonsemantic correction or
clarification, such as typography, grammar, or a link correction, when no
requirement, meaning, permission, prohibition, responsibility, authority,
compatibility, or lifecycle effect changes.

A PATCH cannot introduce new normative behavior.

## Identity continuity and distinct identity

A concrete definition retains the same stable Definition Identifier across all
of its versions, including MAJOR versions, while it remains the same
independently governed responsibility.

A new Definition Identifier is permitted only for a genuinely distinct,
separately governed responsibility. A new Identifier cannot be used to:

- avoid breaking-change or compatibility analysis;
- hide incompatibility or adverse information;
- break historical traceability;
- silently replace or reinterpret an earlier version;
- evade correction, withdrawal, deprecation, or supersession; or
- republish the same responsibility as though it were new.

## Accepted-version immutability

An Accepted Definition Version is immutable. It cannot be overwritten,
silently corrected, or reinterpreted in place.

Correction, normative change, withdrawal, deprecation, or supersession
requires a new exact baseline, scope, evidence, attributable authority, review,
acceptance, and lifecycle. Historical Accepted versions remain identifiable
and traceable.

Mutable aliases, `latest`, `current`, newest-wins, and latest-wins create no
governing authority.

## Exact pins and deferred compatibility

Until separately Accepted architecture defines otherwise, every governing
reference to a future Extension Module Definition or Profile Definition must
pin both:

1. the complete Definition Identifier; and
2. the complete Definition Version.

This decision defines no:

- version or compatibility range;
- minimum, maximum, wildcard, caret, or tilde semantics;
- compatibility matrix or supported-version claim;
- negotiation or version-selection mechanism;
- resolver selection, fallback, preferred version, or `latest`;
- precedence, automatic upgrade, or automatic downgrade; or
- implementation support or interoperability guarantee.

The availability of multiple versions grants no selection authority.

## Core sovereignty and activation boundary

Accepted CNTX Public Core remains independently meaningful for its stated
scope without an Extension Module or Profile.

A future Extension Module Definition or Profile Definition cannot:

- modify or replace an Accepted Core source, identity, or version;
- weaken, reinterpret, or silently override Core semantics;
- coerce, default, repair, or fall back around a Core failure;
- convert a Core-invalid representation into a Core-valid one;
- turn missing, adverse, restricted, uncertain, or unverifiable evidence into
  proof; or
- bypass attributable final human authority.

A Definition Identifier or Definition Version activates nothing. Future
activation requires a separately Accepted declaration and activation model,
explicit exact-version opt-in, and a frozen governing context.

## Provenance and authority boundary

Identity is not provenance, and version is not authority. A future governing
context must independently establish the authoritative definition source,
exact source revision, attributable acceptance, supplied resources,
limitations, and applicable evidence.

A repository location, URL, registry listing, implementation, successful
validation, or product configuration cannot substitute for attributable
authority.

EIGENAAR / Final Authority remains the final human authority for consequential
public acceptance. No technical process, review result, vote, majority,
consensus, score, ranking, newest version, or repository permission replaces
that authority.

## Security, privacy, and public/private boundary

Definition identity and version:

- prove no authenticity or integrity;
- replace no digest, signature, verification, attestation, or trust store;
- grant no permission, access, or disclosure;
- expose or declassify no restricted evidence;
- create no security, privacy, legal, compliance, fitness, or absence claim;
- prove no acceptance, approval, compatibility, support, or conformance; and
- authorize no retrieval, processing, implementation, publication, or
  deployment.

Secrets, credentials, personal data, production configuration, private paths,
restricted evidence, private project context, and private implementation
details remain outside public CNTX sources.

## Fail-closed uncertainty and conflict boundary

Unknown identity, ambiguous allocation, missing authoritative source,
unsupported version, insufficient provenance, uncertain compatibility, or
conflicting evidence remains explicit and fails closed for every dependent
claim.

No uncertainty is resolved through document, load, registration, or lexical
order; newest/latest; popularity; implementation preference; cache state;
majority; consensus; score; ranking; or fallback.

This decision does not define a portable outcome, error, severity, warning, or
conflict-resolution vocabulary.

## Compatibility and conformance boundary

Any later compatibility or conformance statement must separately name exact
identities, exact versions, governing context, supplied authoritative sources,
applicable conformance dimension, evidence, evaluator, capabilities,
limitations, observation time, claimant, and attributable authority.

Schema validity cannot prove contract conformance, implementation conformance,
interoperability, security, privacy, support, certification, or release
fitness. No universal compatibility or conformance result is created.

## Lifecycle and historical integrity

Every later change must distinguish:

- proposal from acceptance;
- candidate revision from Definition Version;
- correction from normative change;
- withdrawal from deprecation;
- deprecation from supersession;
- source availability from support; and
- implementation capability from normative authority.

The immutable release `0.1.0-prealpha.1`, its tag, subject, GitHub Release, and
verification remain exact historical objects. This decision does not extend
that release subject or publish Extension Module/Profile material.

## Dependency-first handoff

Acceptance of this decision establishes only the identity/version prerequisite.
The next possible dependency-first decision is a separate Extension Module and
Profile Dependency, Activation, Composition and Conflict decision under a new
exact authority lifecycle.

That later decision would need to address exact dependency pins, declaration
and activation semantics, permitted combinations, evaluation dependencies,
collisions, fail-closed conflicts, and unknown/unsupported outcomes before any
resource, declaration, executable schema, conformance, tooling, or
implementation phase could be considered.

This handoff authorizes no later phase and reserves no ARCH number, issue,
branch, path, Identifier, Version, field, token, or authority.

## Non-decisions and prohibited effects

This decision creates no concrete Extension Module or Profile, child
Identifier, active child Definition Version, dependency or compatibility
range, precedence, activation, composition, conflict-resolution mechanism,
declaration token, field, type, vocabulary, `$id`, Schema Resource, executable
schema, schema file, payload, manifest, package, registry, catalog, resolver,
cache, bundler, mirror, redirect, automatic discovery, or network access.

It creates no validator, test runner, conformance suite, canonical JSON,
digest, signature, verification, attestation, media type, Serialization
Binding, Artifact Instance, Extension Module instance, Profile instance, API,
CLI, workflow, automation, engine, scheduler, orchestrator, runtime,
provider/product work, private/reference implementation, hosted publication,
alternate distribution, support service, release, tag, GitHub Release, or
deployment.

It performs no project closure, repository archival, maintenance action,
correction, withdrawal, deprecation, supersession, reassessment, release cycle,
repository-setting mutation, immutable-object mutation, or follow-on phase.

It changes no Accepted source, schema, test, identity, version, evidence,
assessment, decision, release, verification, issue, pull request, tag, or
GitHub Release.

## Lifecycle and final human authority

This Accepted document did not approve itself. Creation authority, repository
presence, validation, review, mergeability, technical access, and
implementation capability grant no consequential authority.

Separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision is recorded in issue comment `5229936609`; separately
authorized status promotion and governed integration make the decision
binding. Acceptance adopts only this identity and version policy. It does not
allocate, activate, represent, validate, implement, publish, distribute, or
deploy an Extension Module or Profile or authorize another phase.

## References

- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Contract Identity and Versioning](contract-identity-versioning.md)
- [Common Artifact Envelope Schema Identity and Initial Version Policy](common-artifact-envelope-schema-identity-version-policy.md)
- [Contract Definition Identity, Initial Version, and Source Binding](contract-definition-identity-version-binding.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Public-Core Completion and Maintenance Boundary](public-core-completion-and-maintenance-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0029](adr/0029-extension-module-profile-identity-version-policy.md)
