# CNTX Extension Module and Profile Dependency, Activation, Composition and Conflict Policy (ARCH-030)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed, documentation-only architecture candidate governed
by [issue #102](https://github.com/CNTX-PROJECT/CNTX/issues/102) and recorded by
[ADR-0030](adr/0030-extension-module-profile-dependency-activation-composition-conflict-policy.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in issue
comment `5230085538`.

Creation authority, repository presence, validation, and transparent
non-independent review do not grant acceptance. This candidate remains inactive
until separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision and separately authorized governed promotion and integration.

## Purpose and decision boundary

Accepted ARCH-028 separates possible Extension Modules from Profiles,
preserves CNTX Public Core sovereignty, requires explicit exact-version opt-in,
and orders later decisions dependency-first. Accepted ARCH-029 establishes the
two definition families, their stable namespaces, child-allocation rule, and
independent Definition Identifier and Definition Version dimensions.

This decision defines only the conceptual policy for:

1. exact pinned Definition dependencies;
2. explicit activation and one frozen activation context;
3. complete finite dependency closure and permitted dependency directions;
4. deterministic composition without implicit precedence;
5. fail-closed conflicts, unknown definitions, and unsupported mechanisms;
6. caller-supplied offline-first supply;
7. compatibility, conformance, evidence, security, and privacy boundaries; and
8. lifecycle and final human authority.

It applies only to possible future concrete Extension Module and Profile
Definitions separately allocated, reviewed, Accepted, and integrated under
ARCH-029. It creates no concrete definition, allocates no child Identifier,
activates no child Definition Version, and defines no serialized declaration,
Schema Resource, executable schema, validator, tooling, or implementation.

## Exact decision basis

This decision was prepared on exact public baseline
`47dec36d3339298931c1193f3143d35d1d1aebeb` and tree
`9800a1aa698c20cc746b65536aa06564561366db`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-029 and ADR-0001 through ADR-0029;
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

## Separate responsibility dimensions

The following dimensions remain separate:

| Dimension | Responsibility | Does not establish |
| --- | --- | --- |
| Definition key | Identify one exact Definition Identifier and Definition Version. | Source, activation, acceptance, or authority. |
| Authoritative source | Identify the exact accepted definition source and revision. | Activation or compatibility. |
| Dependency category | State whether one exact dependency is required or optional. | Serialized token or implicit activation. |
| Dependency direction | Bound which categories may depend on which inputs. | Precedence or processing authority. |
| Activation | Select an exact Definition key explicitly in one frozen context. | Acceptance, support, or permission. |
| Activation root | Identify an explicitly selected starting definition. | Ambient activation of reachable material. |
| Dependency closure | Establish the exact complete finite graph for the selected roots. | Successful composition or conformance. |
| Applicability | Bound the context in which a definition is governing. | Identity, source authenticity, or support. |
| Composition | Combine non-conflicting governing meaning under this policy. | Merge, override, repair, or implementation. |
| Conflict | Expose a material contradiction, ambiguity, collision, or missing prerequisite. | Portable diagnostic vocabulary or automatic resolution. |
| Processor capability | State whether required mechanisms are supported. | Normative authority or universal conformance. |
| Compatibility | Scope a claim to exact inputs, context, evidence, and dimension. | Support guarantee or automatic version selection. |
| Conformance and evidence | Preserve exact claim/evidence/provenance boundaries. | Aggregate validity, certification, or acceptance. |
| Security and privacy | Bound untrusted input, resources, access, and disclosure. | Security, privacy, legal, or compliance proof. |
| Lifecycle and authority | Govern correction, withdrawal, history, and human acceptance. | Automated consequential authority. |

No dimension substitutes for or implies another. In particular, dependency is
not activation; activation is not acceptance; availability is not authority;
composition is not conformance; and validation is not final human approval.

## Exact Definition-key model

Every consequential dependency and activation identifies exactly:

1. the complete Definition Identifier; and
2. the complete Definition Version.

Together they form one logical `Definition key`. This logical term allocates no
field, token, object shape, media type, manifest entry, or serialization.

Definition Identifier and Definition Version remain separate dimensions even
when a future representation places them together. The following cannot
replace an exact Definition key:

- an unversioned or mutable alias;
- `latest`, `current`, `stable`, or `recommended`;
- minimum, maximum, wildcard, caret, tilde, or other version range;
- automatic upgrade, downgrade, negotiation, or fallback;
- repository path, filename, branch, tag, release, or commit alone;
- URL availability, HTTP success, registry position, or package presence;
- cache entry, installation state, implementation preference, or product
  configuration; or
- prior successful validation, composition, or execution.

Availability of multiple versions creates no selection authority.

## Logical dependency categories

### Required Definition Dependency

A Required Definition Dependency is one exact Definition key necessary for the
governing meaning of an activated definition.

The required dependency must:

1. be explicitly declared by the dependent definition;
2. be explicitly present in the frozen active Definition Set;
3. have one authoritative definition source and exact source revision;
4. carry source and acceptance provenance;
5. be supported for every mechanism required by the dependent claim; and
6. be included in the complete governing dependency closure.

A missing dependency, wrong version, insufficient provenance, conflicting
source or content, unsupported mechanism, or inaccessible required governing
evidence blocks dependent evaluation fail closed.

Requiredness does not automatically activate a definition. The caller must
explicitly supply and select the complete active set.

### Optional Definition Dependency

An Optional Definition Dependency is one exact declared Definition key whose
absence does not automatically invalidate the base definition.

Presence alone does not activate it. It becomes governing only when:

1. the base definition declares it as an optional dependency;
2. its exact Identifier and Version are supplied;
3. it is explicitly included in the frozen active Definition Set; and
4. it is reachable through a permitted dependency path from an activation
   root.

An inactive optional dependency changes no Core, Extension Module, or Profile
meaning and creates no implied capability, compatibility, conformance, or
support claim.

### Profile Subject

A Profile Subject is an exact identified and versioned Core or Extension Module
basis that one future Profile may select or narrow.

A Profile Subject is not:

- a schema `$ref` or Schema Resource dependency;
- an Artifact Instance relationship;
- an instruction to retrieve or execute a source;
- a permission, approval, or authority delegation; or
- a compatibility or support claim.

## Permitted dependency directions

The permitted direction is deliberately narrow:

1. CNTX Public Core never depends on an Extension Module or Profile.
2. An Extension Module may depend only on:
   - the exact governing Core basis needed for its responsibility; and
   - exact pinned Extension Module Definitions.
3. An Extension Module must not depend on a Profile.
4. A Profile may select or narrow only exact pinned Core and Extension Module
   subjects.
5. A Profile must not depend on another Profile.
6. Multiple Profiles may be separately selected as explicit activation roots
   and apply conjunctively without Profile inheritance or an implicit Profile
   dependency chain.
7. No optional Layer-5 definition may make Core dependent on it.
8. A Profile cannot create a capability absent from its exact pinned Core and
   Extension Module inputs.

These direction rules allocate no concrete dependency, Core aggregate identity,
Profile subject field, or declaration mechanism.

## Frozen activation context

Every consequential application of future Extension Modules or Profiles
requires one explicit, closed, caller-supplied, and frozen activation context.

The logical context contains at least:

- exact activation roots;
- the complete explicit active Definition Set;
- every Definition Identifier and Definition Version;
- every authoritative definition source and exact source revision;
- every declared dependency and its required/optional classification;
- exact governing Core inputs;
- provenance and disclosed limitations;
- unknown or unsupported definitions and capabilities; and
- every detected conflict or unresolved condition.

This list defines responsibilities, not fields or serialization.

Every active definition must be either:

1. an explicitly selected activation root; or
2. explicitly listed in the active Definition Set and reachable from an
   activation root through a permitted declared dependency.

Required dependencies must be explicitly included in the active Definition Set.
They are not activated merely because they are declared, installed, available,
or reachable. Optional dependencies are governing only after the same explicit
selection and reachability conditions are satisfied.

Definitions supplied but not selected remain non-governing. A definition
presented as active without an activation root or permitted dependency path
makes the activation context inconsistent and blocked.

There is no:

- global, ambient, or mutable activation state;
- repository-wide automatically active module or Profile;
- activation inferred from location, filename, media type, or host;
- installation, registry, discovery, cache, or network activation;
- processor-selected or implementation-preferred activation;
- product-, provider-, deployment-, or configuration-driven authority;
- prior-success activation cache; or
- mutable alias or `latest` selection.

Identity, version, source availability, activation, applicability, authority,
acceptance, permission, support, and conformance remain separate.

## Dependency closure and graph invariants

The complete governing dependency closure must be:

- finite;
- statically determinable from exact pins;
- fully caller-supplied before consequential evaluation;
- frozen for the evaluation;
- complete for every transitive Required Definition Dependency;
- complete for every explicitly active Optional Definition Dependency;
- free of unresolved or ambiguous edges;
- free of self-dependencies; and
- free of cycles.

The graph is a directed acyclic graph.

One frozen activation context permits at most one active Definition Version for
one Definition Identifier. Two active versions for the same Identifier are a
material conflict. This decision creates no multi-version isolation, namespace
sandbox, compatibility negotiation, or side-by-side execution mechanism.

Converging dependency paths may deduplicate one identical Definition key only
when the authoritative definition source and exact source revision are also
identical. The same key with different content, sources, revisions,
insufficiently proven source equivalence, or conflicting provenance fails
closed.

Graph discovery or closure must not expand the supplied context, retrieve a
missing definition, select an alias, or mutate the active Definition Set.

## Composition order without precedence

The semantic dependency order is:

1. the exact Accepted Core basis;
2. active Extension Modules in dependency-topological order; and
3. active Profiles after all their exact Core and Extension Module subjects are
   available.

This is dependency order, not precedence. It cannot authorize an override or
choose a winner between conflicting meanings.

When more than one topological order is valid, governing meaning must be
equivalent in every valid order. Any order-dependent result is a conflict and
blocks successful composition.

## Extension Module composition

A future Extension Module may add only capability within its separately
Accepted responsibility. It cannot:

- modify, replace, weaken, or reinterpret Core;
- make a Core-invalid representation Core-valid;
- coerce, default, repair, ignore, or bypass a Core failure;
- silently overwrite another Extension Module;
- use dependency or processing order as precedence;
- turn missing, restricted, adverse, uncertain, or unverifiable evidence into
  proof; or
- create authority, permission, approval, acceptance, or support.

Multiple Extension Modules can compose only when their independently governed
responsibilities and meanings do not conflict. An unresolved name, assertion,
resource, vocabulary, capability, or semantic collision fails closed.

## Profile composition

A future Profile may only:

- select;
- require;
- limit; or
- narrow.

A Profile cannot:

- extend, weaken, replace, or reinterpret a governing input;
- coerce, default, repair, or bypass a failure;
- create an absent capability;
- neutralize a Core or Extension Module conflict;
- silently select a different Definition Version;
- create permission, approval, acceptance, or authority; or
- transform unavailable or insufficient evidence into proof.

Multiple explicitly active Profiles apply conjunctively. Their combined meaning
is the intersection of all applicable constraints. A combination fails closed
when it is contradictory, empty, ambiguous, requires an absent capability,
requires multiple versions of one Definition Identifier, depends on implicit
precedence, or yields an order-dependent result.

This decision creates no merge, overlay, patch, inheritance, import, include,
dynamic-reference, namespace-rewrite, or automatic conflict-resolution
mechanism.

## Fail-closed conflict model

Material conflicts and blocked conditions include:

1. contradiction with the exact pinned Core basis;
2. ambiguous Definition Identifier;
3. ambiguous Definition Version;
4. multiple active versions for one Identifier;
5. missing or wrong-version Required Definition Dependency;
6. undeclared or unreachable active dependency;
7. self-dependency or dependency cycle;
8. unsupported definition, mechanism, or processor capability;
9. unknown required Identifier or Version;
10. conflicting authoritative sources, content, revisions, or provenance for
    one exact Definition key;
11. Extension Module collision;
12. Profile contradiction;
13. a Profile requirement for an absent capability;
14. order-dependent composition or unknown precedence;
15. insufficient governing evidence;
16. security or privacy conflict;
17. required restricted evidence that cannot be accessed under governing
    authority; and
18. a resource or recursion condition that prevents reliable complete
    evaluation.

No conflict may be silently resolved by:

- document, load, registration, insertion, or lexical order;
- specificity guesses;
- newest, latest, or latest-wins;
- popularity or repository position;
- cached prior success;
- implementation or product preference;
- majority, consensus, score, grade, or ranking;
- fallback or best-effort substitution; or
- Core-only processing when the active context requires more.

This decision allocates no portable conflict, error, diagnostic, warning,
severity, or outcome vocabulary. A later applicable validation/output contract
must represent blocked processing without weakening this policy.

## Unknown and unsupported handling

Unknown material that is not active changes no Core or governing Extension
Module/Profile meaning.

An explicitly active or required unknown/unsupported definition or mechanism:

- remains visible;
- cannot be ignored;
- cannot be treated as successfully applied;
- cannot be replaced by fallback, a cached version, or a different source; and
- blocks every dependent successful-composition or conformance claim.

Unknown does not mean universally invalid for every purpose. It means that a
claim dependent on the unknown or unsupported material cannot be established
under the frozen context. This decision creates no portable result token.

## Supply and resolution boundary

Accepted ARCH-023 remains controlling. Definition sources and governing inputs
are caller-supplied, offline-first, closed, frozen, and exact-keyed before
consequential evaluation. Automatic network access remains excluded.

Repository presence, URL availability, registry listing, discovery, retrieval,
cache, mirror, redirect, package presence, installation, or HTTP success does
not establish authority, authenticity, acceptance, activation, applicability,
compatibility, conformance, or trust.

This decision creates no resolver, registry, catalog, cache, bundler, mirror,
redirect, discovery service, hosted definition authority, retrieval protocol,
network allowlist, or automatic network behavior.

## Compatibility boundary

Any future compatibility statement must identify:

1. exact Core sources and versions;
2. exact Extension Module/Profile Definition Identifiers and Versions;
3. exact authoritative sources and source revisions;
4. the exact frozen activation context and dependency closure;
5. the exact conformance dimension;
6. evidence, provenance, evaluator capabilities, and limitations;
7. observation time, claimant, and attributable authority.

Changing a dependency pin, requiredness, activation condition, permitted
composition, or conflict meaning is a normative Definition change and must be
classified under ARCH-029. Compatibility uncertainty fails closed and cannot
silently become a MINOR or PATCH claim.

This decision defines no compatibility range, compatibility matrix, supported
version, automatic upgrade, negotiation, or support guarantee.

## Conformance and evidence boundary

Core, Extension Module, Profile, contract, schema, validator, implementation,
interoperability, compatibility, support, security/privacy, certification, and
release conformance remain separate.

Schema validity, exact graph closure, or successful composition does not prove:

- contract conformance;
- implementation or validator conformance;
- interoperability;
- authenticity or integrity;
- security or privacy;
- legal or compliance completeness;
- compatibility or support;
- certification or accreditation; or
- release fitness.

Evidence for a future consequential claim must preserve the exact activation
roots, active Definition Set, dependency graph, sources, revisions, provenance,
processor capabilities, conflicts, unknown/unsupported conditions, limitations,
adverse information, restricted-evidence boundaries, observation time,
claimant, and authority.

No aggregate valid, score, badge, grade, certification, or support claim is
created.

## Security, privacy, and resource boundary

Future processing must treat definition sources and activation data as
untrusted input and address:

- dependency substitution and source/provenance ambiguity;
- graph size, depth, recursion, and cycle attacks;
- excessive processing, memory, and time use;
- nested composition and denial-of-service exposure;
- dependency minimization and least privilege;
- restricted evidence, disclosure, and data minimization;
- unknown and unsupported capability handling;
- correction and withdrawal; and
- public/private source separation.

This decision selects no concrete size/depth limit, timeout, memory limit,
sandbox, verification algorithm, access-control mechanism, redaction or
sanitization algorithm, trust store, digest, signature, attestation, or
correction/withdrawal procedure.

Secrets, credentials, personal data, production configuration, private paths,
restricted evidence, private project context, and private implementation
details remain outside public CNTX sources.

This decision grants no access, permission, disclosure, trust, authenticity,
security, privacy, legal, or compliance claim.

## Lifecycle and historical integrity

Every future consequential definition or composition change requires a new
exact baseline, scope, issue or contract, evidence, limitations, review,
attributable acceptance, integration, completion, synchronization, and any
separately authorized cleanup.

Accepted Definition Versions remain immutable under ARCH-029. Correction,
withdrawal, deprecation, or supersession cannot rewrite historical meaning in
place. Mutable aliases and newest/latest-wins grant no authority.

The immutable release `0.1.0-prealpha.1`, its tag, release subject, GitHub
Release, and verification remain exact historical objects. This Proposed
decision does not extend that release subject or publish Extension
Module/Profile material.

## Dependency-first handoff

If this decision is later separately accepted and integrated, the next
candidate layer is a separate Extension Module and Profile Schema Resource,
Packaging and Declaration Model decision.

This handoff authorizes no follow-on phase and reserves no ARCH number, issue,
branch, path, field, token, Identifier, Version, schema, resource, package, or
authority.

## Non-decisions and prohibited effects

This decision does not define or create a concrete Extension Module or Profile,
child Identifier or active Definition Version, dependency or compatibility
range, executable dependency/activation grammar, concrete precedence,
declaration field or serialized token, portable conflict/error vocabulary,
type, vocabulary, `$id`, Schema Resource, executable schema, schema file,
payload, manifest, package, catalog, registry, resolver, cache, bundler, mirror,
redirect, automatic discovery or network access, validator, test runner,
conformance suite, canonical JSON, digest algorithm, signature, verification,
attestation, media type, or new Serialization Binding.

It creates no Artifact Instance, Extension Module instance, Profile instance,
API, CLI, workflow, automation, engine, scheduler, orchestrator, runtime,
provider/product work, private or reference implementation, hosted publication,
alternate distribution, support service, release, tag, GitHub Release,
deployment, project closure, repository archival, maintenance action,
correction, withdrawal, deprecation, supersession, reassessment, new release
cycle, settings mutation, or follow-on authority.

It changes no Accepted source, contract, schema, test, identity, version,
evidence, assessment, decision, release, verification, issue, pull request,
tag, GitHub Release, or repository setting.

## Lifecycle and final human authority

This Proposed document does not approve itself. Creation authority, validation,
review, mergeability, technical access, repository presence, and implementation
capability grant no consequential authority.

EIGENAAR / Final Authority remains the final human authority for public
acceptance. Separate attributable acceptance of the exact reviewed revision and
separately authorized status promotion and integration are required before this
decision can become Accepted.

## References

- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Extension Module and Profile Identity and Version Policy](extension-module-profile-identity-version-policy.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Common Artifact Envelope Schema Composition and Packaging](common-artifact-envelope-schema-composition-packaging.md)
- [Contract Identity and Versioning](contract-identity-versioning.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Portable Conformance Evidence Boundary](portable-conformance-evidence-boundary.md)
- [Public-Core Completion and Maintenance Boundary](public-core-completion-and-maintenance-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0030](adr/0030-extension-module-profile-dependency-activation-composition-conflict-policy.md)
