# CNTX Extension Module and Profile Architecture Boundary (ARCH-028)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed, documentation-only architecture decision governed
by [issue #98](https://github.com/CNTX-PROJECT/CNTX/issues/98) and recorded by
[ADR-0028](adr/0028-extension-module-profile-architecture-boundary.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in issue
comment `5228583661`.

Creation, repository presence, validation, and transparent non-independent
review do not grant acceptance. Only separate attributable EIGENAAR / Final
Authority acceptance of the exact reviewed revision and separately authorized
governed integration can make this decision Accepted.

## Purpose and decision boundary

Accepted ARCH-027 places the initial CNTX Public-Core specification and
prerelease cycle on a quiescent, event-driven maintenance boundary. It names
Extension Module and Profile architecture as one possible future consequential
change category, but it creates neither mechanism.

This proposal defines only the conceptual boundary within which future
Extension Module and Profile architecture could be governed. It:

1. separates Extension Modules from Profiles;
2. preserves the sovereignty of the Accepted CNTX Public Core;
3. requires explicit opt-in and exact pins for any future activation;
4. identifies the responsibilities that later decisions must satisfy;
5. requires fail-closed conflict handling;
6. orders later decisions dependency-first; and
7. preserves final human authority and the public/private boundary.

It allocates no concrete identity or version, defines no declaration field or
token, creates no executable schema or resource, and authorizes no tooling or
implementation.

## Exact decision basis

This proposal was prepared on exact public baseline
`7403cb7b28733f2d6a31a8eebf0a2a6a99c7b8aa` and tree
`e1b7e309b26f7d674107d5f713122429e8e6c32f`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-027 and ADR-0001 through ADR-0027;
- CONTRACT-001 through CONTRACT-009;
- one Accepted Common Artifact Envelope Schema Version `1.0.0`;
- nine Accepted artifact-specific Schema Versions `1.0.0`;
- ten unchanged synthetic validation manifests;
- the Accepted Core Artifact JSON Binding Version `1.0.0`;
- the Accepted Schema Resource Resolution and Catalog Boundary;
- the Accepted Validation and Validation Output Contract;
- the Accepted Portable Conformance Evidence Boundary;
- Accepted assessment, remediation, release-policy, final-decision, release,
  verification, completion, and maintenance sources; and
- immutable prerelease `0.1.0-prealpha.1` and its exact historical objects.

This proposal changes none of those sources, identities, versions, assertions,
expected results, evidence, limitations, statuses, or authority.

## Terms and category separation

### CNTX Public Core

`CNTX Public Core` means the Accepted Core architecture, contracts, schemas,
binding, resolution, validation/output, evidence, release, verification, and
maintenance boundaries that exist independently of any future Extension Module
or Profile.

The Core remains complete for its stated boundary without an Extension Module
or Profile. Optional mechanisms cannot become a hidden prerequisite for Core
interpretation or conformance.

### Extension Module

`Extension Module` means a possible future, separately governed, additive
capability contract with its own logical identity and version dimension.

An Extension Module may add capabilities only within a later explicitly
defined boundary. It cannot:

- edit or replace an Accepted Core source;
- weaken a Core requirement or schema assertion;
- reinterpret a Core identity, version, field, token, or relationship;
- claim authority over Core validity or conformance;
- silently become mandatory for a Core artifact; or
- acquire authority merely because a repository, schema, processor, or product
  recognizes it.

No concrete Extension Module is created by this decision.

### Profile

`Profile` means a possible future, separately governed constraint and selection
contract with its own logical identity and version dimension. A Profile may be
defined only over exact pinned versions of the Core and, where separately
authorized, exact pinned Extension Modules.

A Profile may later be permitted to select, require, or narrow capabilities. It
cannot:

- weaken or contradict a Core or Extension Module requirement;
- invent a capability that its pinned inputs do not define;
- redefine the meaning of a pinned capability;
- grant permission, approval, acceptance, or authority;
- create implicit precedence over another Profile; or
- acquire support or compatibility status by declaration or use.

No concrete Profile is created by this decision.

### Category non-equivalence

An Extension Module is not a Profile. A Profile is not an Extension Module.
Neither is a Core contract, Schema Resource, Artifact Instance, Serialization
Binding, validator configuration, implementation feature flag, product
edition, deployment configuration, or release channel.

Future architecture must preserve this category separation unless an exact
later Accepted decision explicitly changes it.

## Core sovereignty and non-override rule

The Accepted Core always retains authority over its own scope. A future
Extension Module or Profile cannot:

1. modify an Accepted Core source in place;
2. replace a Core identity or version;
3. remove a Core-required property, relationship, assertion, or obligation;
4. convert an invalid Core representation into a valid one;
5. authorize coercion, defaulting, repair, or fallback around a Core failure;
6. turn missing, adverse, restricted, uncertain, or unverifiable evidence into
   proof;
7. change a release, assessment, decision, or verification outcome; or
8. bypass attributable final human authority.

Where a future extension/profile requirement conflicts with the exact pinned
Core, processing must fail closed for that governed context. There is no silent
override or implicit extension/profile precedence.

## Explicit opt-in and exact pinning

Any future activation must be explicit and attributable to a later Accepted
declaration model. It must identify exact logical identities and exact versions
under a frozen governing context.

Activation cannot be inferred from:

- repository location;
- filename, path, media type, host, registry, or deployment environment;
- presence of unknown data;
- processor capabilities;
- product configuration;
- mutable aliases such as `latest`;
- cache state;
- network availability;
- a Profile or module being popular, newer, installed, or discoverable; or
- a previous validation run.

This decision does not define the future declaration representation, placement,
field names, tokens, identifiers, versions, or syntax.

## Required responsibility dimensions

Later decisions must keep the following dimensions separate:

| Dimension | Required future responsibility | Not created here |
| --- | --- | --- |
| Identity | Distinguish every logical Extension Module and Profile from Core, schemas, artifacts, bindings, and implementations. | Concrete Identifier or namespace. |
| Versioning | Pin exact independent revisions and define change compatibility. | Version values or a version policy. |
| Provenance | Identify the authoritative source and attributable lifecycle. | Registry, signature, or trust service. |
| Authority | State who may propose, accept, activate, change, withdraw, or supersede. | Delegation or automated approval. |
| Dependency | Identify exact Core, module, and profile dependencies without hidden inputs. | Dependency syntax or range. |
| Activation | Require explicit opt-in under a frozen context. | Field, token, or runtime switch. |
| Declaration | Keep representation separate from semantic authority. | JSON property, schema, or media type. |
| Composition | Define permitted combinations and evaluation order. | A composition algorithm. |
| Conflict | Detect contradiction, collision, ambiguity, and unsupported combinations fail closed. | Precedence or automatic resolution. |
| Unknown/unsupported handling | Preserve unknown identity/version and unsupported capability as visible conditions. | Fallback or best-effort processing. |
| Supply and resolution | Require exact caller-supplied resources under a closed context unless separately changed. | Resolver, registry, catalog, or network retrieval. |
| Compatibility | Scope compatibility claims to exact identities, versions, contexts, and evidence. | Compatibility matrix or guarantee. |
| Conformance and evidence | Keep Core, module, profile, validator, and implementation conformance separate. | Aggregate valid result or certification. |
| Security and privacy | Apply minimization, least privilege, disclosure, untrusted-input, and resource boundaries. | Access control, sanitization, or security proof. |
| Lifecycle | Separate correction, withdrawal, deprecation, supersession, and historical traceability. | Lifecycle automation or mutable aliases. |

No one dimension substitutes for another. Identity is not version; version is
not activation; activation is not authority; validation is not acceptance;
implementation support is not normative conformance.

## Dependency and composition boundary

A future Extension Module may depend on exact Core or module versions only when
later Accepted architecture permits that dependency. A future Profile may
select exact Core and module versions only when all selected inputs are
independently supplied and authoritative for their own scope.

This proposal creates no:

- dependency grammar or compatibility range;
- optional-versus-required dependency token;
- multiple-module or multiple-profile composition rule;
- evaluation sequence;
- merge, overlay, patch, inheritance, import, or include mechanism;
- namespace or collision algorithm;
- dynamic reference mechanism; or
- packaging or bundling model.

Those are later architecture decisions. Until they exist, no executable
composition can be inferred.

## Fail-closed conflict and unknown handling

A later governed processor must expose and stop on any unresolved material
conflict, including:

- contradiction with the pinned Core;
- contradiction between pinned modules or Profiles;
- identity or version ambiguity;
- undeclared dependency;
- missing authoritative source;
- unsupported mechanism or capability;
- name, assertion, vocabulary, or resource collision;
- unknown precedence requirement; or
- insufficient evidence to establish the required governing context.

Conflict cannot be resolved silently through:

- document order;
- load order;
- registration order;
- newest or latest version;
- lexical sorting;
- specificity guesses;
- majority or consensus;
- score, ranking, or popularity;
- implementation preference;
- cached prior success; or
- fallback to Core-only processing when the declared governed context requires
  more.

An unknown or unsupported Extension Module/Profile is not automatically
invalid for every possible purpose, but it makes any dependent evaluation
`Unverifiable` or otherwise fail closed under the later applicable contract.
This proposal does not allocate a portable outcome vocabulary.

## Supply and resolution boundary

Accepted ARCH-023 keeps Schema Resource resolution caller-supplied,
offline-first, closed, and free of automatic network access. ARCH-028 does not
change that boundary.

Future Extension Module/Profile sources and resources must remain explicit
inputs under a frozen governing context until separately Accepted architecture
states otherwise. Repository presence, a public URL, registry listing, cache,
mirror, redirect, or successful retrieval does not establish authority,
authenticity, acceptance, compatibility, or trust.

This proposal creates no resolver, registry, catalog, cache, bundler, mirror,
redirect, discovery service, hosted authority, trust store, or network
behavior.

## Compatibility and conformance boundary

Any future compatibility statement must name:

1. exact Core identity and version;
2. exact Extension Module/Profile identities and versions;
3. exact governing context and supplied resources;
4. exact conformance dimension;
5. evidence, evaluator, capabilities, limitations, and observation time; and
6. claimant and attributable authority.

Compatibility in one dimension does not imply compatibility in another.
Schema validity does not prove contract conformance, implementation
conformance, interoperability, security, privacy, support, or release fitness.

No universal compatibility result, support matrix, score, certification,
badge, grade, accreditation, or supported-version claim is created here.

## Security, privacy, and public/private boundary

Extension Module and Profile mechanisms may increase attack surface,
dependency risk, disclosure risk, processing cost, ambiguity, and supply-chain
exposure. Later work must therefore define:

- untrusted-input handling and resource limits;
- dependency minimization and least privilege;
- provenance and authoritative-source boundaries;
- restricted-evidence handling;
- disclosure and data-minimization responsibilities;
- unknown and unsupported capability behavior;
- denial-of-service and recursive-composition boundaries;
- correction and withdrawal handling; and
- public/private source separation.

Secrets, credentials, personal data, production configuration, private paths,
restricted evidence, private project context, and private implementation
details remain outside public CNTX sources.

This proposal grants no access, permission, disclosure, trust, authenticity,
security, privacy, legal, or compliance claim.

## Dependency-first decision order

Before executable Extension Module/Profile work can be considered, later
separately governed decisions must proceed in this order:

1. **Identity and Version Policy** — define logical identity, concrete
   identifier allocation, independent version dimensions, and change rules.
2. **Dependency, Activation, Composition, and Conflict** — define exact pins,
   declaration semantics, permitted combinations, evaluation dependencies,
   collisions, and fail-closed outcomes.
3. **Schema Resource, Packaging, and Declaration Model** — define whether and
   how resources, fields, vocabularies, packaging, and offline supply represent
   the Accepted semantics.
4. **Executable Schema and Validation/Conformance** — define exact assertions,
   cases, output/evidence relations, and distinct conformance dimensions.
5. **Tooling and Implementation** — only after the governing specification
   layers are Accepted may a resolver, validator, registry, CLI, API, runtime,
   or product be separately proposed.

This ordering authorizes none of those phases and does not reserve their ARCH
numbers, issue numbers, paths, identities, or versions.

## Lifecycle and historical integrity

Every future Extension Module or Profile change must distinguish:

- proposal from acceptance;
- correction from a semantic change;
- withdrawal from deprecation;
- deprecation from supersession;
- source availability from support;
- historical availability from current applicability; and
- implementation capability from normative authority.

A future consequential lifecycle requires a new exact baseline, subject,
scope, issue or contract, evidence, limitations, review, attributable
acceptance, integration, completion, synchronization, and any separately
authorized cleanup.

The immutable release `0.1.0-prealpha.1`, its tag, subject, GitHub Release, and
verification remain exact historical objects. ARCH-028 does not extend that
release subject or publish Extension Module/Profile material.

## Non-decisions and prohibited effects

This proposal does not define or create a concrete Extension Module, Profile,
Identifier, Version, version policy, dependency or compatibility range,
precedence, conflict algorithm, declaration token, field, type, vocabulary,
`$id`, Schema Resource, executable schema, payload, manifest, package, catalog,
registry, resolver, cache, bundler, mirror, redirect, validator, test runner,
conformance suite, canonical JSON, digest, signature, verification,
attestation, media type, or Serialization Binding.

It creates no Artifact Instance, Extension Module instance, Profile instance,
API, CLI, workflow, automation, engine, scheduler, orchestrator, runtime,
provider/product work, private or reference implementation, hosted
publication, alternate distribution, support service, deployment, release,
tag, GitHub Release, maintenance action, correction, withdrawal, deprecation,
supersession, reassessment, or later phase.

It changes no Accepted source, schema, test, identity, version, evidence,
assessment, decision, release, verification, repository setting, issue, pull
request, tag, or GitHub Release.

## Lifecycle and final human authority

This Proposed document does not approve itself. Creation authority is not
acceptance. Validation, review, mergeability, technical access, repository
presence, and implementation capability grant no consequential authority.

Only separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision, followed by separately authorized status promotion and
governed integration, can make this decision Accepted. Even then, acceptance
would adopt only the architecture boundary; it would not create or implement
an Extension Module or Profile or authorize another phase.

## References

- [Public-Core Completion and Maintenance Boundary](public-core-completion-and-maintenance-boundary.md)
- [Artifact-Specific Schema Family and Canonical Artifact Container Boundary](artifact-specific-schema-family-container-boundary.md)
- [Contract Identity and Versioning](contract-identity-versioning.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Portable Conformance Evidence Boundary](portable-conformance-evidence-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0028](adr/0028-extension-module-profile-architecture-boundary.md)
