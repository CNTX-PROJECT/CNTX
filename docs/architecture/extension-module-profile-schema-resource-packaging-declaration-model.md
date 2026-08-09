# CNTX Extension Module and Profile Schema Resource, Packaging and Declaration Model (ARCH-031)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed, documentation-only architecture decision governed
by [issue #104](https://github.com/CNTX-PROJECT/CNTX/issues/104) and recorded by
[ADR-0031](adr/0031-extension-module-profile-schema-resource-packaging-declaration-model.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in issue
comment [5230355484](https://github.com/CNTX-PROJECT/CNTX/issues/104#issuecomment-5230355484).

Creation authority, repository presence, validation, and transparent
non-independent ARCHITECT review do not grant acceptance. Separate attributable
EIGENAAR / Final Authority acceptance of the exact reviewed revision, followed
by separately authorized status promotion and integration, is required before
this decision can become Accepted.

## Purpose and decision boundary

Accepted ARCH-028 separates possible Extension Modules from Profiles and
preserves CNTX Public Core sovereignty. Accepted ARCH-029 establishes their
separate Definition identity and version dimensions. Accepted ARCH-030 defines
exact-keyed dependencies, explicit activation, finite closure, composition,
and fail-closed conflict handling.

This decision defines only the conceptual bridge between those Definition
semantics and a later, separately governed executable-schema phase. It defines:

1. two logical Definition Schema Families;
2. a strict separation between Definition, Schema Resource, source, package,
   declaration, activation, authority, and conformance dimensions;
3. an exact Schema Resource key-or-`None` Definition Schema Binding;
4. a future canonical standalone Schema Resource model;
5. an ARCH-030-aligned Schema Resource dependency graph;
6. a closed caller-supplied logical Definition Package;
7. identity-preserving derived bundling;
8. a logical Governing Definition Declaration and frozen Governing Declaration
   Set outside every existing Core Artifact Instance and Core Artifact JSON;
9. caller-supplied offline-first supply and fail-closed processing; and
10. conformance, evidence, security, privacy, lifecycle, public/private, and
    final-human-authority boundaries.

It creates no concrete Extension Module, Profile, child Definition, Schema
Resource, executable schema, declaration representation, package instance,
Artifact Instance, tooling, implementation, release, publication, or
deployment.

## Exact decision basis

This decision was prepared on exact public baseline
`8ecbb82de03dd0969d7bea6324d14e391d59d871` and tree
`c821b928f44f266263032773adc8d5632211cb9e`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-030 and ADR-0001 through ADR-0030;
- CONTRACT-001 through CONTRACT-009;
- one Accepted Common Artifact Envelope Schema Version `1.0.0`;
- nine Accepted artifact-specific Schema Versions `1.0.0`;
- ten unchanged synthetic validation manifests;
- Accepted Core Artifact JSON Binding Version `1.0.0`;
- the Accepted Schema Resource Resolution and Catalog Boundary;
- the Accepted Validation and Validation Output Contract;
- the Accepted Portable Conformance Evidence Boundary;
- Accepted assessment, remediation, release-policy, final-decision, release,
  verification, completion, maintenance, and Extension Module/Profile sources;
  and
- immutable prerelease `0.1.0-prealpha.1` and its exact historical objects.

This decision changes none of those sources, identities, versions, assertions,
expected results, evidence, limitations, statuses, or authority.

## Two logical Definition Schema Families

This decision defines exactly two logical categories:

1. `CNTX Extension Module Definition Schema Family`;
2. `CNTX Profile Definition Schema Family`.

The first family may later contain separately governed schemas for concrete
Extension Module Definitions. The second may later contain separately governed
schemas for concrete Profile Definitions.

The two families are distinct from each other and from:

- CNTX Public Core;
- `CNTX Extension Module Definition Family`;
- `CNTX Profile Definition Family`;
- the nine Core Artifact Types and their Contract Definitions;
- every existing Core Schema Family and Schema Resource;
- every Serialization Binding;
- every Artifact Instance;
- validators, implementations, products, and releases.

A Definition Schema Family is not a Definition Family and carries no Definition
authority. Family existence allocates no concrete child Schema Identifier,
Schema Version, canonical `$id`, namespace, repository path, or schema file.

## Separate responsibility dimensions

The following dimensions remain separate:

| Dimension | Responsibility | Does not establish |
| --- | --- | --- |
| Definition category | Distinguish Extension Module Definition from Profile Definition. | Schema identity or activation. |
| Definition Identifier | Identify one stable logical Definition. | Definition Version, schema, source, or authority. |
| Definition Version | Identify one immutable revision of Definition meaning. | Schema Version or lockstep change. |
| Definition Schema Identifier | Identify one logical schema line for one concrete Definition. | Concrete allocation, `$id`, or source. |
| Schema Version | Identify one immutable schema revision. | Definition Version, compatibility, or support. |
| Canonical `$id` | Identify one future canonical Schema Resource under its schema policy. | Retrieval, trust, acceptance, or network authority. |
| Schema Resource content | Carry executable assertions when separately authorized later. | Definition semantics, activation, or final authority. |
| Authoritative Definition source | State the normative Definition meaning. | Executable schema or schema-source authenticity. |
| Authoritative Schema Resource source | Supply one exact schema representation. | Definition authority or broader conformance. |
| Source revision and provenance | Pin the exact supplied source and its history. | Acceptance, compatibility, or trust by itself. |
| Package | Group exact caller-supplied governing inputs. | Identity, activation, priority, authority, or evidence sufficiency. |
| Declaration | Record the exact governing Definition context logically. | Acceptance, permission, trust, or serialization. |
| Activation and applicability | Select exact governing Definitions for one frozen context. | Definition acceptance or schema validity. |
| Acceptance and authority | Record attributable governance decisions. | Implementation support or automatic execution. |
| Compatibility | Scope a claim to exact inputs and evidence. | Automatic version choice or support. |
| Conformance | Evaluate one stated dimension against exact governing sources. | Aggregate validity, certification, or approval. |
| Implementation support | State processor capability for exact mechanisms. | Normative authority or universal conformance. |
| Lifecycle and release status | Preserve change history and publication state. | Currentness, support, or mutable latest-wins authority. |

No dimension substitutes for or implies another. Definition Identity is not
Schema Identity. Definition Version is not Schema Version. Equal version values
create no lockstep relationship. Schema presence activates nothing. A
declaration proves no acceptance. A package grants no authority. Schema
validity proves no Definition or contract conformance.

## Future Definition Schema Identity allocation boundary

A later Accepted concrete Definition Identifier may have at most one
corresponding logical Definition Schema Identity in the correct Definition
Schema Family.

Allocation cannot be inferred from:

- the Definition Identifier or Definition Version;
- a repository directory, path, or filename;
- a URL, host, media type, or discovered `$id`;
- package position, declaration order, or bundle key;
- registry, catalog, cache, installation, or network presence;
- implementation support or product configuration; or
- a prior successful validation.

Every future allocation requires a new exact baseline and scope, explicit
identity and version provenance, an authoritative source, review, attributable
EIGENAAR / Final Authority acceptance, governed integration, and separately
authorized lifecycle completion.

ARCH-031 selects no Definition Schema Family namespace, URI path grammar,
concrete HTTPS authority, `$id`, Schema Version, repository path, or schema
file.

## Exact Definition Schema Binding

Every active Definition key in one frozen governing context must explicitly
declare exactly one of these states:

1. one exact `Schema Resource key`; or
2. `None`.

`Schema Resource key` retains the Accepted ARCH-023 meaning: the complete
logical Schema Identifier and complete Schema Version. `None` means that the
active Definition key has no governing executable Definition Schema Resource
in that frozen context. It does not mean unknown, missing, unavailable, or
failed resolution.

No implicit state is permitted. The state cannot be selected from repository
presence, filename, discovered `$id`, URL availability, registry or catalog
listing, cache, network, installation, implementation capability, product
configuration, mutable alias, `latest`, previous validation, package position,
or load order.

A Definition Schema Binding links exactly one active Definition key to at most
one governing Schema Resource key for one frozen context. It does not:

- replace or weaken the authoritative Definition source;
- activate a Definition or expand the active Definition Set;
- create a Required or Optional dependency or Profile Subject;
- grant acceptance, applicability, permission, trust, or authority;
- prove compatibility, conformance, interoperability, or support;
- make Core-invalid input Core-valid; or
- broaden, repair, replace, reinterpret, or override Definition or Core
  semantics.

A missing declaration is not equivalent to `None`. Ambiguous, duplicate,
conflicting, or inconsistent states fail closed.

## Future canonical standalone Schema Resource model

Every later separately Accepted concrete Definition Schema Version must have
conceptually exactly one canonical standalone root Schema Resource with:

- JSON Schema Draft 2020-12;
- an explicit root `$schema`;
- exactly one later allocated version-qualified absolute HTTPS root `$id`
  without fragment;
- media type `application/schema+json`;
- internal reusable schema material only under the root `$defs`;
- no nested `$id`;
- static fragment-only internal `$ref` references;
- no initial public `$anchor`;
- no `$dynamicRef` or `$dynamicAnchor`;
- no custom dialect or vocabulary;
- no Format-Assertion or Hyper-Schema; and
- immutable Accepted standalone content for the exact Schema Version.

The canonical resource is an identity-bearing logical Schema Resource, not
canonical bytes. Object-member order and non-semantic JSON whitespace do not
create another identity. This decision creates no canonical JSON, deterministic
reserialization, digest, signature, or byte-level identity.

ARCH-031 creates no concrete dialect value in an executable resource, `$id`,
Schema Version, `$defs` name, `$ref` value, anchor, field, type, assertion,
test, schema file, or executable schema.

## Schema dependency alignment

The external Schema Resource graph must remain aligned with the exact frozen
ARCH-030 Definition graph:

1. CNTX Public Core Schema Resources never reference an Extension Module or
   Profile resource.
2. An Extension Module Schema Resource may reference only exact governing Core
   resources and exact active Extension Module dependency resources.
3. An Extension Module Schema Resource never references a Profile Schema
   Resource.
4. A Profile Schema Resource may reference only exact governing Core resources
   and exact Extension Module subject or dependency resources.
5. A Profile Schema Resource never references another Profile Schema Resource.
6. The external resource graph is finite, acyclic, exact-versioned, and fully
   caller-supplied.
7. Every external reference edge is justified by the governing Definition
   graph; the schema graph adds or removes no Definition dependency.
8. `$ref` establishes no activation, Definition dependency, Profile Subject,
   authority, acceptance, applicability, or precedence.
9. Existing closed Accepted Core schemas remain closed and unchanged.
10. Extension Module/Profile material cannot make Core-invalid input
    Core-valid.

Dependency order is not precedence. Every valid evaluation order for the same
closed graph must preserve equivalent results. Undeclared dependencies, wrong
keys or versions, missing resources, prohibited directions, category mismatch,
cycles, graph mismatch, order-dependent evaluation, unknown precedence, and
insufficient evidence fail closed.

## Logical Definition Package

A `Definition Package` is a logical, closed, caller-supplied grouping for one
frozen governing context. It may contain:

- exact Definition keys;
- authoritative Definition sources and exact revisions;
- Required and Optional Definition Dependencies;
- Profile Subjects;
- one exact Schema Resource key or `None` for each active Definition key;
- standalone Schema Resources with exact sources and revisions;
- source, acceptance, package, and supply provenance;
- capabilities and processing limitations;
- unknown, unsupported, adverse, and unresolved conditions; and
- restricted-evidence boundaries.

These are logical responsibilities, not fields, manifest entries, filenames,
directory structures, archive members, or serialized tokens.

A package is not:

- an Artifact Instance;
- a Definition, Schema, package, release, or manifest identity/version;
- an authoritative Definition or Schema Resource source;
- a registry, catalog, resolver, cache, trust store, or publication channel;
- acceptance, activation, applicability, authority, or priority;
- compatibility, conformance, support, security/privacy, or certification
  evidence; or
- a permission or disclosure mechanism.

Layout, filename, directory, archive position, package order, bundle key,
transport, media type, or load order activates and prioritizes nothing.

Canonical authoring and acceptance remain separate for each authoritative
Definition source and each standalone Schema Resource. Package construction
cannot rewrite or replace their identities, content, provenance, or history.

## Identity-preserving derived bundling

A later derived Compound Schema Document may be used only as a non-authoritative
offline transport representation. It must preserve:

- every embedded canonical `$id` and `$schema`;
- every static `$ref` target and evaluation relationship;
- each independent Schema Resource Identity and Version;
- the standalone resource content and behavior;
- the complete resource set and exact provenance; and
- linked-versus-bundled evaluation equivalence.

Bundling cannot add, remove, rename, rebase, inline away, flatten, rewrite, or
merge resource identity. It cannot introduce a different dialect, dynamic
reference, public anchor, dependency, activation, precedence, or governing
meaning.

A Compound Schema Document creates no new schema/package identity or version,
normative authority, acceptance, release, canonical bytes, manifest, digest,
signature, attestation, certification, registry, catalog, or trust.

## Logical Governing Definition Declaration

A `Governing Definition Declaration` is a logical, not-yet-serialized record
for one exact active Definition key. It is responsible for exactly:

1. Definition category;
2. exact Definition Identifier;
3. exact Definition Version;
4. authoritative Definition source;
5. exact source revision;
6. provenance;
7. activation role or roles;
8. exact Required Definition Dependencies;
9. exact Optional Definition Dependencies;
10. exact Profile Subjects where applicable;
11. exact Schema Resource key or `None`;
12. authoritative Schema Resource source where present;
13. exact Schema Resource revision where present;
14. resource provenance;
15. supplied package and context provenance;
16. capabilities;
17. evaluator or processing limitations;
18. compatibility and conformance claim scope;
19. unknown, unsupported, adverse, unresolved, and restricted-evidence
    conditions;
20. attributable declaring and governing authority; and
21. correction, withdrawal, deprecation, and supersession traceability.

These are logical responsibilities only. They allocate no JSON member, field
name, type, enum token, object shape, schema assertion, media type, or
Serialization Binding.

One declaration does not approve itself, authenticate its sources, establish
Definition acceptance, activate another Definition, resolve a conflict, prove
evidence sufficiency, or grant access, permission, disclosure, trust, support,
or authority.

## Frozen Governing Declaration Set

A frozen `Governing Declaration Set` exactly represents the ARCH-030 active
Definition Set for one frozen governing context. It must:

1. be complete for every activation root;
2. include the complete Required dependency closure;
3. include only Optional dependencies that were separately explicitly active;
4. preserve Profiles as separate activation roots;
5. include one declaration for every and only active Definition key;
6. be duplicate-free;
7. contain at most one active Definition Version for each Definition
   Identifier;
8. preserve exact authoritative source and revision consistency;
9. declare exactly one Schema Resource key or `None` for every active key;
10. remain closed and frozen throughout consequential evaluation; and
11. expose every limitation, conflict, unknown, unsupported condition, adverse
    evidence, and restricted-evidence boundary.

Set membership records the exact governing context. It creates no Definition
acceptance, authority, permission, trust, support, compatibility, conformance,
certification, or release status.

## Placement and Serialization Binding boundary

The logical Governing Declaration Set is a separate governing input. It is not
part of any existing CNTX Artifact Instance.

ARCH-031 adds no property to:

- Common Artifact Envelope Schema Version `1.0.0`;
- any of the nine Accepted artifact-specific Schema Versions `1.0.0`;
- any Accepted Contract Definition;
- any Core Artifact JSON document; or
- Core Artifact JSON Binding Version `1.0.0`.

Declaration cannot be inferred from unknown artifact properties, payload
content, envelope metadata, repository presence, filename, media type, Schema
Resource reference, package location, processor capability, implementation, or
product configuration.

A future serialized declaration, field vocabulary, Artifact Instance, JSON
Schema, media type, package representation, or Serialization Binding requires a
separate architecture decision, exact scope, review, and attributable
acceptance.

## Caller-supplied offline-first supply and resolution

Accepted ARCH-023 remains controlling. Before consequential evaluation begins,
the caller supplies a closed, frozen, exact-keyed context containing the entry
resources and complete transitive external resource closure.

There is no automatic:

- discovery or registry lookup;
- retrieval, redirect following, or network access;
- mutable alias or `latest` resolution;
- hidden cache, mirror, or prior-success reuse;
- schema, source, or version substitution;
- repair, fallback, coercion, defaulting, or silent omission; or
- expansion of the supplied governing context.

Retrieval coordinates, URL availability, HTTP success, repository presence,
package inclusion, installation, or cache presence establish no identity,
authenticity, acceptance, activation, trust, compatibility, conformance, or
authority.

This decision creates no resolver, registry, catalog, cache, bundler, mirror,
redirect, discovery service, network allowlist, hosted schema authority, or
retrieval protocol.

## Fail-closed conditions

At minimum, each of the following remains separately visible and blocks every
dependent successful claim:

1. missing, duplicate, ambiguous, or conflicting declaration;
2. Definition Identifier, Version, category, source, or revision mismatch;
3. active-set, activation-root, dependency, Profile Subject, or closure
   mismatch;
4. implicit or ambient Schema Resource participation;
5. missing, wrong, ambiguous, conflicting, or unsupported Schema Identifier,
   Schema Version, resource, dialect, or vocabulary;
6. undeclared or prohibited `$ref` direction;
7. external resource cycle or graph mismatch;
8. package collision or inconsistent duplicate;
9. identity-mutating or behavior-changing bundle;
10. order-dependent evaluation or unknown precedence;
11. unsupported processor mechanism or capability;
12. insufficient source, revision, provenance, or governing evidence;
13. required restricted evidence that cannot be accessed under governing
    authority;
14. security or privacy conflict; and
15. a resource-count, document-size, graph-depth, recursion, reference-
    expansion, memory, time, or evaluation-cost condition that prevents
    reliable complete evaluation.

`None` cannot repair a missing or failed Schema Resource declaration. Core-only
processing cannot replace a declared governing context that requires more.

No blocked condition may be resolved silently by document, load, registration,
package, insertion, or lexical order; specificity guesses; newest, `latest`, or
latest-wins; popularity; repository position; implementation preference; cache
state; previous success; majority; consensus; score; ranking; fallback; or
best-effort substitution.

This decision creates no portable conflict, error, diagnostic, warning,
severity, status, or outcome vocabulary.

## Conformance and evidence separation

The following conformance dimensions remain separate:

- CNTX Public Core;
- Definition;
- Governing Definition Declaration and Declaration Set;
- Definition Package;
- Schema Resource and executable schema;
- Artifact Contract and Artifact Instance;
- validator;
- implementation;
- interoperability;
- compatibility and support;
- security and privacy;
- certification; and
- release.

Schema validity does not prove Definition semantics, activation, applicability,
authority, a broader Artifact Instance, contract conformance, validator or
implementation conformance, interoperability, security, privacy, legal or
compliance completeness, compatibility, support, certification, or release
fitness.

Evidence for a future consequential claim must preserve exact Definitions,
Schema Resource keys, sources, revisions, package and declaration context,
resource graph, processor and evaluator identity/capabilities, outcomes,
failures, limitations, uncertainty, adverse information, restricted evidence,
observation time, claimant, and attributable authority.

No aggregate valid result, pass/fail, score, grade, badge, threshold, rubric,
checklist verdict, quality gate, ranking, certification, or support claim is
created.

## Security, privacy, and resource boundary

Every Definition source, Schema Resource, package, declaration, and supplied
context is untrusted input. A later execution decision must bound:

- resource count and package/document size;
- graph depth, recursion, and reference expansion;
- evaluation time, memory, and computational cost;
- malicious or ambiguous identity and provenance;
- dependency substitution and conflicting-source attacks;
- disclosure, restricted evidence, data minimization, and least privilege;
- unknown and unsupported mechanisms; and
- correction and withdrawal handling.

Credentials, secrets, personal data, production configuration, private paths,
private project context, restricted evidence, and private implementation
details remain outside public CNTX sources.

ARCH-031 selects no concrete limit, timeout, sandbox, access-control mechanism,
redaction or sanitization algorithm, cryptographic integrity mechanism, digest,
signature, trust store, attestation, or correction/withdrawal procedure. It
grants no access, permission, disclosure, authenticity, trust, security,
privacy, legal, compliance, or absence claim.

## Lifecycle and historical integrity

Every future consequential Definition Schema allocation, Schema Version,
resource, package/declaration representation, binding, executable validation,
correction, withdrawal, deprecation, or supersession requires a new exact
baseline, scope, issue or contract, evidence, limitations, review, attributable
acceptance, integration, completion, synchronization, and separately authorized
cleanup where applicable.

Accepted Definition Versions remain immutable under ARCH-029. Every future
Accepted Definition Schema Version and its standalone Schema Resource must also
remain immutable. Correction, withdrawal, deprecation, or supersession cannot
rewrite historical meaning or content in place. Mutable aliases and
newest/latest-wins grant no authority.

ARCH-001 through ARCH-030, ADR-0001 through ADR-0030, Contract Definitions,
Accepted schemas and tests, bindings, assessments, remediation evidence,
decisions, release policy, immutable prerelease `0.1.0-prealpha.1`, its tag,
release subject, GitHub Release, verification, completion, and maintenance
history remain unchanged.

## Public/private and final-human-authority boundary

Public CNTX may contain only public-safe normative architecture and evidence.
Private Definition sources, restricted evidence, credentials, personal data,
production configuration, private project material, and private implementation
details remain physically and authoritatively separate.

Repository presence, validation, a clean diff, mergeability, technical access,
processor capability, review, or implementation cannot grant acceptance or
consequential authority. EIGENAAR / Final Authority remains the final human
authority for any public acceptance, activation mechanism, representation,
schema, implementation, release, publication, or deployment.

## Dependency-first handoff

Only after this decision is separately Accepted and integrated may a later
candidate consider the distinct Extension Module and Profile Executable Schema
and Validation/Conformance layer named by ARCH-028.

This handoff authorizes no follow-on phase and reserves no ARCH number, issue,
branch, path, Identifier, Version, namespace, `$id`, Schema Resource, schema,
field, token, declaration, package, validator, test, implementation, release,
or authority.

## Non-decisions and prohibited effects

This decision creates no concrete Extension Module or Profile, child Definition
Identifier or active Definition Version, concrete Definition Schema Identifier
or Schema Version, concrete `$id`, Schema Resource, repository schema file,
executable schema, assertion, test, payload, declaration field or serialized
token, Artifact Instance, Extension Module instance, Profile instance, package
instance, package identity/version, manifest, portable conflict/error/severity/
outcome vocabulary, custom dialect or vocabulary, Format-Assertion,
Hyper-Schema, dynamic-reference mechanism, media type, or new Serialization
Binding.

It creates no resolver, registry, catalog, cache, bundler, mirror, redirect,
automatic discovery, retrieval, network access, validator, test runner,
conformance suite, canonical JSON, digest algorithm, signature, verification,
attestation, certification, API, CLI, workflow, automation, engine, scheduler,
orchestrator, runtime/provider/product work, private or reference
implementation, hosted publication, alternate distribution, support service,
release, tag, GitHub Release, deployment, project closure, repository archival,
maintenance action, correction, withdrawal, deprecation, supersession,
reassessment, new release cycle, settings mutation, or follow-on authority.
No ARCH-032 number, title, issue, branch, path, contract, candidate, or phase is
created, reserved, or authorized.

## Lifecycle and final human authority

This Proposed document does not approve itself. Creation authority, repository
presence, validation, transparent non-independent ARCHITECT review,
mergeability, technical access, and implementation capability grant no
consequential authority.

Separate attributable EIGENAAR / Final Authority exact-head acceptance and
separately authorized status promotion and governed integration are required
before this decision can become Accepted.

## References

- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Extension Module and Profile Identity and Version Policy](extension-module-profile-identity-version-policy.md)
- [Extension Module and Profile Dependency, Activation, Composition and Conflict Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [Common Artifact Envelope Schema Composition and Packaging](common-artifact-envelope-schema-composition-packaging.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Core Artifact JSON Serialization Binding](core-artifact-serialization-binding.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
