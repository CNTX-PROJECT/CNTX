# CNTX Governing Definition Declaration and Frozen Governing Declaration Set JSON Representation Boundary (ARCH-045)

## In ordinary language

ARCH-031 says what must be known about every active Extension Module or Profile
Definition and about the complete frozen set that governs one evaluation.
Accepted ARCH-045 gives that information one closed JSON-compatible shape. It
does not make the declaration set a Core record, approve its contents, define a
schema or package, or give software permission to act.

| Quick view | Meaning |
| --- | --- |
| **Status** | Accepted and integrated documentation-only representation decision |
| **Declaration** | One closed fourteen-member record for one exact active Definition key |
| **Declaration Set** | One closed six-member root containing exactly one declaration for every and only active Definition key |
| **Preserved basis** | All 21 ARCH-031 declaration responsibilities and all 11 Declaration Set invariants |
| **Not created** | Core Artifact Instance, identity/version, schema, package/bundle, Serialization Binding, Tool/Implementation, execution, evidence, approval, release, deployment, or authority |

### Reading route

- [Status and authority](#status-and-authority)
- [Declaration root](#closed-fourteen-member-governing-definition-declaration)
- [Exact responsibility mapping](#exact-arch-031-declaration-responsibility-mapping)
- [Declaration Set root](#closed-six-member-governing-declaration-set)
- [Set invariants](#exact-arch-031-declaration-set-invariants)
- [Failure and non-decisions](#fail-closed-and-non-decision-boundary)

This visitor layer is non-normative and adds no requirement beyond the complete
Accepted decision below.

## Status and authority

**Document Status:** Accepted and integrated.

This decision is governed by
[issue #151](https://github.com/CNTX-PROJECT/CNTX/issues/151). Attributable
EIGENAAR / Final Authority acceptance of the exact issue contract is recorded
in issue comment
[5286906192](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5286906192).
The accepted issue body contains exactly 25,517 characters, 25,517 UTF-8 bytes,
and SHA-256
`ebac6d72c098fa27bf6f59913c41a7d5f5f796285911782180f399a918384bde`.

Attributable EIGENAAR / Final Authority exact-head acceptance is recorded in
issue comment
[5290871158](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5290871158),
bound only to candidate commit
`a92cb298a5106db27f0c6b720a5faa3b6571ddf1` and complete tree
`1a68548638f0ff570639a051bbca65e778642ca4`.

The exact public baseline is commit
`1d9e4667d68cce6e0289464c821bcd95e1d355ae`, tree
`3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`, with 206 tracked paths. The
accepted issue contract authorizes only one documentation candidate with two
added paths and seven modified paths. All other 199 baseline paths remain
protected.

Issue-contract acceptance authorized candidate preparation, validation, one
candidate commit, one Draft pull request, transparent non-independent review,
and a mandatory stop. It did not accept ARCH-045 or any candidate commit/tree.
The exact-head comment above and a separately authorized status-only promotion
to commit `c7b8c5cc793516197726344e7d30c12d0a86f514` and complete tree
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4` established Accepted status only.
They made no semantic representation change and did not themselves authorize
integration, merge, issue closure, cleanup, package/bundle work, schema work,
tooling, execution, evidence, release, or deployment. The later separately
governed integration and issue-completion lifecycle is recorded under
[Accepted lifecycle and integrated state](#accepted-lifecycle-and-integrated-state).

## Purpose and exact decision boundary

Accepted ARCH-030 requires one explicit, caller-supplied, closed, finite, and
frozen activation context for every consequential application of Extension
Modules or Profiles. Accepted ARCH-031 defines one logical Governing Definition
Declaration for every active Definition key and one frozen Governing
Declaration Set equal to the complete active Definition Set. Those logical
responsibilities deliberately allocate no fields, tokens, object shapes,
schema, media type, or Serialization Binding.

ARCH-045 defines the first concrete JSON-compatible representation boundary
for exactly those responsibilities:

1. one reusable closed `GoverningDefinitionDeclaration` record shape; and
2. one closed `GoverningDeclarationSet` root shape containing those records.

An exact Definition key remains exactly one complete Definition Identifier and
one complete Definition Version. They are separate dimensions even where this
representation places them in the same closed subobject.

The member names and shapes below are normative only for this representation
decision. JSON-compatible does not choose document bytes, UTF-8 rules,
duplicate-name handling, number handling, member order, canonicalization,
media type, storage, transport, Schema Resource, validation behavior, or
Serialization Binding.

## Accepted basis and precedence

This Accepted decision remains subordinate to and preserves:

1. ARCH-028 and ARCH-029 for Core sovereignty, the two Definition families,
   stable namespaces, child allocation, and independent identity/version;
2. ARCH-030 for Definition keys, permitted dependency direction, explicit
   activation, Profiles as separate roots, finite dependency closure, conflict
   visibility, and one active version per Identifier;
3. ARCH-031 for the exact 21 declaration responsibilities, 11 set invariants,
   separate placement, source/resource/package separation, and offline-first
   failure boundaries;
4. ARCH-032 for separate declaration/set, package, schema, validation,
   conformance, output, and evidence dimensions;
5. ARCH-033 for dependency-first future work and the later concrete Tool and
   Implementation boundary;
6. ARCH-023 and ARCH-024 for caller-supplied resource resolution, separate
   outcomes, visible limitations, and non-aggregation;
7. Accepted and integrated ARCH-038 through ARCH-044 without changing their
   Definition, representation, Schema Resource, case, execution, evidence, or
   lifecycle history; and
8. all Accepted Core architecture, contracts, schemas, bindings, validation,
   evidence, release, public/private, and final-human-authority boundaries.

If a member or rule cannot be justified by this exact basis, it is outside
ARCH-045.

## Shared closed representation primitives

The representation uses these shared logical shapes. They are not Artifact
Types, Definition identities, schema definitions, or a Serialization Binding.

### Definition key

`DefinitionKey` is a closed object containing exactly:

1. `definitionIdentifier`; and
2. `definitionVersion`.

Both values are required, non-blank strings. Each is at most 512 characters.
Neither may be a mutable alias such as `latest`, `current`, `stable`, or
`recommended`. Object equality is complete-value equality; member order is not
meaningful.

### Source pin and provenance reference

`SourcePin` is a closed object containing exactly:

1. `authoritativeSource`;
2. `sourceRevision`; and
3. `provenance`.

All three values are required, non-blank opaque references of at most 2,048
characters; source revisions use the narrower 512-character maximum.
Repository or package presence, filename, media type, cache state, a previous
result, or network availability cannot replace an exact pin.

### Attributable role reference

`RoleReference` is a closed object containing exactly:

1. `roleIdentifier`;
2. `roleLabel`;
3. `scope`; and
4. `attributionReference`.

All values are required and non-blank. Identifiers, labels, and references are
at most 512 characters; scope is at most 2,048 characters. A role reference
records attribution and scope. It does not authenticate the role or grant
permission, acceptance, approval, disclosure, or final authority.

### Condition declaration

`ConditionDeclaration` is a closed object containing exactly:

1. `conditionIdentifier`;
2. `conditionCategory`;
3. `subjectReference`;
4. `statement`;
5. `evidenceReferences`;
6. `limitationReferences`; and
7. `responsibleRoleReferences`.

`conditionCategory` is exactly one of `unknown`, `unsupported`, `adverse`,
`unresolved`, or `restricted-evidence`. Identifiers and references are at most
512 characters; statements are non-blank and at most 2,048 characters.
Reference collections are duplicate-free, contain at most 64 entries, and may
be empty only when the declaration itself explicitly states the bounded absence
or unavailability. Responsible-role references contain one through 32 entries.

These categories remain separate. Unknown is not unsupported; adverse is not
failure; unresolved is not absent; and restricted-evidence metadata does not
replace the restricted evidence.

## Closed fourteen-member Governing Definition Declaration

One `GoverningDefinitionDeclaration` is a closed object with all and only these
fourteen required root members:

1. `definition`;
2. `definitionSource`;
3. `activationRoles`;
4. `requiredDependencies`;
5. `optionalDependencies`;
6. `profileSubjects`;
7. `schemaResource`;
8. `packageAndContextProvenance`;
9. `capabilities`;
10. `processingLimitations`;
11. `claimScope`;
12. `conditions`;
13. `authority`; and
14. `lifecycleTraceability`.

Unknown members are prohibited. Root-member order creates no precedence or
meaning.

### `definition`

`definition` is a closed object containing exactly:

1. `definitionCategory`;
2. `definitionIdentifier`; and
3. `definitionVersion`.

All are required, non-blank strings of at most 512 characters. The Identifier
and Version together are the declaration's exact Definition key. The category
does not create a new Definition family or override Accepted category meaning.

### `definitionSource`

`definitionSource` is exactly one `SourcePin`. It records the authoritative
Definition source, exact source revision, and provenance. It does not prove
source authenticity, acceptance, availability, or authority.

### `activationRoles`

`activationRoles` is a duplicate-free array containing one through 32 closed
`RoleReference` values. It records the declaration's exact activation role or
roles. It does not select an activation root, activate a dependency, or grant
permission.

### `requiredDependencies` and `optionalDependencies`

Each member is a duplicate-free array of zero through 64 exact `DefinitionKey`
values. They remain separate collections. Required or Optional classification
cannot be inferred from array order, repository presence, package position,
availability, reachability, processor preference, or prior success.

A declaration lists dependencies; it does not activate them. Required
dependencies must still be included explicitly in the frozen set. Optional
dependencies become governing only when explicitly active and reachable from a
permitted root.

### `profileSubjects`

`profileSubjects` is a duplicate-free array of zero through 64 exact
`DefinitionKey` values. It is non-empty only for a Profile Definition and is
explicitly empty for an Extension Module Definition. A Profile may narrow only
its exact subjects, remains a separate activation root, and cannot depend on
another Profile.

### `schemaResource`

`schemaResource` is one closed discriminated object with required `state` equal
to exactly `present` or `none`.

When `state` is `present`, the object contains all and only:

1. `state`;
2. `resourceKey`;
3. `authoritativeSource`;
4. `resourceRevision`; and
5. `provenance`.

`resourceKey` is a closed object containing exactly `schemaIdentifier` and
`schemaVersion`. The complete Schema Identifier and complete Schema Version
form the exact Schema Resource key. Values are required and non-blank;
identifiers, versions, and revisions are at most 512 characters, and source/
provenance references are at most 2,048 characters.

When `state` is `none`, the object contains exactly `state` and prohibits every
resource-key, source, revision, or provenance member. Explicit `none` means no
governing executable Definition Schema Resource exists for that active
Definition key in this frozen context. It is not unknown, missing, inaccessible,
unsupported, unresolved, or failed resolution.

Omission, JSON `null`, empty string, repository or package presence, filename,
media type, mutable alias, `latest`, substitution, repair, or fallback cannot
replace either explicit state.

### `packageAndContextProvenance`

`packageAndContextProvenance` is a closed object containing exactly:

1. `packageSupply`;
2. `governingContextProvenance`.

`governingContextProvenance` is a required non-blank opaque reference of at
most 2,048 characters. `packageSupply` is a closed discriminated object with
`state` equal to exactly `present` or `none`. A `present` value contains exactly
`state` and one required non-blank `packageProvenance` reference; `none`
contains only `state`.

This member records provenance only. It creates no package identity, version,
representation, manifest, layout, bundle, source authority, or implicit
supply. A separately supplied package is not the normative Definition source.

### `capabilities`

`capabilities` is a duplicate-free array of zero through 64 non-blank bounded
capability references. It records declared capabilities only. It does not prove
processor support, implementation availability, successful execution,
compatibility, conformance, or acceptance.

### `processingLimitations`

`processingLimitations` is a duplicate-free array of zero through 64 closed
limitation declarations. Each contains exactly `limitationIdentifier`,
`dimension`, `statement`, `subjectReferences`, `evidenceReferences`, and
`responsibleRoleReferences`. Statements and references are bounded as in the
shared primitives. Dimensions remain explicit; no limitation is silently
collapsed into a score or aggregate result.

Evaluator/processor mechanism, capability, resource, security, privacy,
access, disclosure, portability, support, and evidence limitations remain
visible where applicable. An empty array asserts only that this declaration
supplies no limitation declaration; it does not prove that no limitation
exists.

### `claimScope`

`claimScope` is a closed object containing exactly:

1. `compatibilityClaims`;
2. `conformanceClaims`.

Each member is a duplicate-free array of zero through 64 closed claim
references containing exactly `claimIdentifier`, `subject`, `scope`,
`governingRequirementReferences`, `evidenceReferences`, `limitationReferences`,
and `claimantRoleReferences`.

Compatibility and conformance remain separate. A declaration shape, schema
result, package, Tool output, or previous success cannot establish either
claim automatically. No claim becomes an aggregate verdict, approval,
certification, release gate, deployment gate, or authority.

### `conditions`

`conditions` is a duplicate-free array of zero through 128 closed
`ConditionDeclaration` values. Every unknown, unsupported, adverse, unresolved,
or restricted-evidence condition material to the declaration remains separate
and visible. An empty array is not proof that none exists.

### `authority`

`authority` is a closed object containing exactly:

1. `declaringRoles`;
2. `governingRoles`.

Each member is a duplicate-free array of one through 32 closed `RoleReference`
values. It records attributable declaring and governing roles and sources. It
does not let a declaration approve itself, accept a Definition, activate
another Definition, resolve a conflict, grant access, or replace final-human
authority.

### `lifecycleTraceability`

`lifecycleTraceability` is a closed object containing exactly:

1. `correctionReferences`;
2. `withdrawalReferences`;
3. `deprecationReferences`;
4. `supersessionReferences`.

Each member is a duplicate-free array of zero through 32 non-blank opaque
references of at most 512 characters. These references preserve history. They
do not rewrite, erase, reactivate, accept, or silently replace any revision.

## Exact ARCH-031 declaration responsibility mapping

Every ARCH-031 responsibility maps exactly once:

| # | ARCH-031 responsibility | ARCH-045 member |
| ---: | --- | --- |
| 1 | Definition category | `definition.definitionCategory` |
| 2 | Exact Definition Identifier | `definition.definitionIdentifier` |
| 3 | Exact Definition Version | `definition.definitionVersion` |
| 4 | Authoritative Definition source | `definitionSource.authoritativeSource` |
| 5 | Exact source revision | `definitionSource.sourceRevision` |
| 6 | Provenance | `definitionSource.provenance` |
| 7 | Activation role or roles | `activationRoles` |
| 8 | Exact Required Definition Dependencies | `requiredDependencies` |
| 9 | Exact Optional Definition Dependencies | `optionalDependencies` |
| 10 | Exact Profile Subjects where applicable | `profileSubjects` |
| 11 | Exact Schema Resource key or `None` | `schemaResource.state` and `schemaResource.resourceKey` when `present` |
| 12 | Authoritative Schema Resource source where present | `schemaResource.authoritativeSource` |
| 13 | Exact Schema Resource revision where present | `schemaResource.resourceRevision` |
| 14 | Resource provenance | `schemaResource.provenance` |
| 15 | Supplied package and context provenance | `packageAndContextProvenance` |
| 16 | Capabilities | `capabilities` |
| 17 | Evaluator or processing limitations | `processingLimitations` |
| 18 | Compatibility and conformance claim scope | `claimScope` |
| 19 | Unknown, unsupported, adverse, unresolved, and restricted-evidence conditions | `conditions` |
| 20 | Attributable declaring and governing authority | `authority` |
| 21 | Correction, withdrawal, deprecation, and supersession traceability | `lifecycleTraceability` |

The grouping introduces no twenty-second responsibility and omits or duplicates
none of the 21.

## Closed six-member Governing Declaration Set

One `GoverningDeclarationSet` is a closed root object with all and only these
six required members:

1. `governingContext`;
2. `activationRoots`;
3. `explicitlyActiveOptionalDependencies`;
4. `declarations`;
5. `conditions`; and
6. `authority`.

Unknown members are prohibited. Root-member order, declaration order, source
order, package order, load order, or lexical order creates no precedence or
meaning.

### `governingContext`

`governingContext` is a closed object containing exactly:

1. `contextReference`;
2. `contextRevision`;
3. `authoritativeSource`;
4. `provenance`.

All values are required, non-blank, and bounded. The context is caller supplied
and exact. This object creates no declaration-set identity/version or new
governing-context artifact.

### `activationRoots`

`activationRoots` is a duplicate-free array of one through 64 exact
`DefinitionKey` values. Each root is explicitly selected. Profiles remain
separate roots and never become an implicit Profile inheritance or dependency
chain.

### `explicitlyActiveOptionalDependencies`

`explicitlyActiveOptionalDependencies` is a duplicate-free array of zero
through 64 closed directed edges. Each edge contains exactly:

1. `dependentDefinition`; and
2. `optionalDependency`.

Both are exact `DefinitionKey` values. An edge records explicit optional
activation only when both keys are active and the dependency is declared by
the dependent Definition. Presence, availability, reachability, declaration,
installation, or package inclusion alone does not activate it.

### `declarations`

`declarations` is a duplicate-free array of one through 64 complete
`GoverningDefinitionDeclaration` records. It contains exactly one declaration
for every and only active Definition key. Duplicate-free complete JSON values
do not by themselves prove Definition-key uniqueness; projected exact-key
uniqueness remains a set invariant.

### Set-level `conditions`

`conditions` is a duplicate-free array of zero through 128 closed
`ConditionDeclaration` values. It exposes every material set-level limitation,
conflict, unknown, unsupported condition, adverse evidence, and restricted-
evidence boundary. An empty array does not prove their absence.

### Set-level `authority`

`authority` is a closed object containing exactly:

1. `selectingRoles`;
2. `supplyingRoles`;
3. `governingRoles`;
4. `finalHumanAuthorityRoles`.

Each member is a duplicate-free array of one through 32 closed `RoleReference`
values. It preserves attributable selection, supply, governance, and
final-human-authority boundaries. It contains no approval, acceptance,
permission, verdict, automatic authority, or consequential execution command.

## Exact ARCH-031 Declaration Set invariants

The complete supplied root preserves all eleven ARCH-031 invariants:

| # | Invariant | Representation responsibility |
| ---: | --- | --- |
| 1 | Complete for every activation root | Every `activationRoots` key is represented in `declarations` and its full permitted closure is present |
| 2 | Complete Required dependency closure | Every transitive `requiredDependencies` key is active and represented |
| 3 | Only separately explicitly active Optional dependencies | Every governing Optional edge appears in `explicitlyActiveOptionalDependencies`; no undeclared or implicit edge participates |
| 4 | Profiles remain separate activation roots | Every active Profile is listed in `activationRoots` and never inferred through Profile dependency |
| 5 | One declaration for every and only active Definition key | `declarations` membership equals the exact active Definition Set |
| 6 | Duplicate-free | Roots, Optional edges, declaration keys, and other declared unique collections contain no duplicates |
| 7 | At most one active Version per Identifier | No two declaration keys share one Identifier with different active Versions |
| 8 | Exact source/revision consistency | Converging dependency paths preserve identical authoritative Definition source and revision pins for one key |
| 9 | Exactly one Schema Resource key or `None` per active key | Every declaration contains exactly one closed `schemaResource` state |
| 10 | Closed and frozen during consequential evaluation | The complete supplied root is immutable for one evaluation; any change creates another context and evaluation |
| 11 | Every limitation/conflict/unknown/unsupported/adverse/restricted boundary visible | Declaration and set-level `conditions` plus limitations disclose each material condition separately |

These are conformance responsibilities over the complete supplied value. A
self-asserted boolean cannot prove any invariant. This representation contains
no `valid`, `approved`, `accepted`, `complete`, `conformant`, `releaseReady`,
`deploymentReady`, score, grade, badge, traffic light, ranking,
recommendation, aggregate outcome, or serialized `automaticAuthority` member.
The continuing semantic assertion is `automaticAuthority: false`.

## Closed, offline-first, and deterministic supply

All governing inputs are caller supplied, exact, finite, closed, and frozen
before consequential evaluation. This representation creates no ambient or
mutable state and no automatic discovery, retrieval, redirect, network access,
registry, catalog, mirror, cache, installation lookup, package-manager lookup,
substitution, coercion, repair, default, fallback, or processor-selected input.

General non-blank statements and opaque references are at most 2,048
characters. Identifiers, Versions, revisions, labels, and compact references
use the narrower 512-character maximum. General collections contain at most 64
items; role collections contain one through 32; lifecycle collections contain
at most 32; and condition collections contain at most 128. These finite
representation limits prove no runtime memory, CPU, time, recursion,
expansion, handle, process, network-isolation, or denial-of-service guarantee.

Member order, declaration order, dependency order, package position, load
order, specificity, newest/latest, popularity, majority, consensus, ranking,
implementation preference, cache state, or previous success cannot resolve
meaning or conflict.

## Fail-closed and non-decision boundary

Each of these remains separately visible and blocks every dependent successful
claim:

1. declaration key or source mismatch;
2. missing or extra active Definition key;
3. incomplete Required dependency closure;
4. undeclared or implicit Optional activation;
5. Profile dependency or non-root Profile activation;
6. duplicate exact key or multiple active Versions for one Identifier;
7. conflicting source, revision, content, or provenance for one exact key;
8. missing, ambiguous, or inconsistent Schema Resource `present`/`none` state;
9. unresolved, ambiguous, prohibited, cyclic, or direction-invalid edge;
10. unsupported Definition, mechanism, dialect, vocabulary, or capability;
11. insufficient source, resource, package, context, or authority provenance;
12. required inaccessible or restricted evidence;
13. security, privacy, minimization, access, or disclosure conflict;
14. unbounded or unsupported supplied input; and
15. mutation of any governing input during consequential evaluation.

ARCH-045 does not define a validator or result vocabulary. The items above are
documentation responsibilities for later separate conformance, output,
evidence, and Tool/Implementation decisions.

## Core, package, schema, and execution separation

The declaration set is a separate governing input outside every existing CNTX
Artifact Instance. It adds no member to the Common Artifact Envelope, any of
the nine artifact-specific payloads, any existing Core Artifact JSON document,
or Core Artifact JSON Binding Version `1.0.0`.

This representation does not allocate or create:

- a declaration, set, Artifact, package, bundle, manifest, or context Identity
  or Version;
- canonical bytes, media type, digest, signature, storage, transport, API, or
  Serialization Binding;
- a Schema Identifier, Schema Version, `$id`, Schema Resource, assertion,
  testcase, fixed expected result, or schema execution;
- a package/bundle representation, resolver, registry, catalog, cache,
  bundler, mirror, redirect, or network behavior;
- Validation Output, diagnostic vocabulary, Portable Conformance Evidence, or
  a conformance-claim serialization;
- Tool/Implementation Identity, Version, capability, configuration,
  dependency, interface, code, runner, workflow, CI, execution, or evidence;
- Definition acceptance, activation authority, truth, authenticity,
  compatibility, interoperability, permission, trust, approval,
  certification, release fitness, deployment fitness, or final authority; or
- merge, issue closure, branch cleanup, publication, support, hosting, release,
  or deployment authority.

Every such subject remains a separately proposed, reviewed, accepted, and
integrated later gate in ARCH-033 dependency order.

## Security, privacy, and restricted evidence

Every supplied source, declaration, condition, package reference, and context
is untrusted input. A future processor must impose independently governed
bounds on document size, collection count, nesting, reference expansion,
resource use, diagnostics, logs, retention, disclosure, and failure handling.

Public records contain public-safe metadata only. Credentials, secrets,
personal data, private repository content, private context, restricted
evidence, production configuration, and exploitable detail do not belong in
CNTX Public Core. Restricted-evidence metadata cannot expose or replace the
restricted evidence. Unavailable authority or evidence cannot be invented,
defaulted, repaired, substituted, or silently downgraded.

## Conformance and evidence separation

Representation conformance answers only whether a supplied value follows this
closed documented shape. It does not establish:

- completeness or correctness of the active Definition Set or dependency
  graph;
- source authenticity, revision equivalence, provenance sufficiency, or
  Definition acceptance;
- Schema Resource validity, package completeness, linked/bundled equivalence,
  or evaluator support;
- compatibility, interoperability, contract conformance, Profile conformance,
  or Core Artifact validity;
- truthful conditions, adequate evidence, role identity, access, permission,
  disclosure, security, privacy, safety, or resource sufficiency; or
- approval, certification, release status, deployment status, or authority.

Any future claim must keep its exact subject, governing requirement, claimant,
source/resource/context pins, evidence, limitations, adverse/restricted
conditions, observation time, and attributable authority visible. No
individual result becomes an aggregate pass/fail or consequential decision.

## Accepted lifecycle and integrated state

Issue-contract acceptance comment `5286906192` authorized only the exact
documentation candidate, validation, one candidate commit, one Draft pull
request, transparent non-independent review, and the mandatory exact-head stop.

Candidate preparation, Markdown validity, link validity, review, Draft state,
repository presence, and mergeability did not accept ARCH-045. Attributable
exact-head acceptance comment `5290871158` accepted only candidate commit/tree
`a92cb298a5106db27f0c6b720a5faa3b6571ddf1` /
`1a68548638f0ff570639a051bbca65e778642ca4`. The preceding Proposed status
allocated or activated nothing. Exact-head acceptance and status-only promotion
established Accepted status only and made no semantic representation change.

At the Accepted promotion stage, work stopped before separate integration
authority for promotion commit/tree
`c7b8c5cc793516197726344e7d30c12d0a86f514` /
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`. Ready transition, integration,
merge, issue closure, branch cleanup, and every later-layer choice were
unauthorized at that stage. This historical stop remains part of the lifecycle
provenance.

The later public integration-completion record
[5292133876](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5292133876)
records the separately governed, expected-head-pinned squash merge of that exact
promotion head through [PR #152](https://github.com/CNTX-PROJECT/CNTX/pull/152).
The merge produced public `main` commit
`0bccbb39a56044be3a9c7236dd828b1d1959e7ce`, with sole parent
`1d9e4667d68cce6e0289464c821bcd95e1d355ae`, and complete tree
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`. The promotion and integration
trees are identical, and the promotion-to-integration diff is empty. Issue #151
is `closed/completed`.

The former task branch
`codex/arch-045-governing-declaration-set-json-representation` is absent from
the current local, origin-tracking, and live public-remote views. This is a
current-state observation only. It does not reconstruct, replace, or
retroactively grant historical cleanup authority. Issue #151 contains no
separate public cleanup-authority comment after the integration-completion
record's explicit cleanup stop.

Integration and issue completion create no declaration/set identity or version,
package/bundle, media type, canonical serialization, Schema Resource, testcase,
Serialization Binding, Validation Output, Portable Conformance Evidence,
Tool/Implementation, execution, evidence, aggregate result, automatic
authority, release, support, certification, hosting, or deployment. Every such
later-layer choice remains separately governed.

## References

- [Extension Module and Profile Dependency, Activation, Composition, and Conflict Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [Extension Module and Profile Schema Resource, Packaging and Declaration Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [Extension Module and Profile Executable Schema and Validation/Conformance Boundary](extension-module-profile-executable-schema-validation-conformance-boundary.md)
- [Extension Module and Profile Tooling and Implementation Boundary](extension-module-profile-tooling-implementation-boundary.md)
- [ADR-0030](adr/0030-extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [ADR-0031](adr/0031-extension-module-profile-schema-resource-packaging-declaration-model.md)
- [ADR-0032](adr/0032-extension-module-profile-executable-schema-validation-conformance-boundary.md)
- [ADR-0033](adr/0033-extension-module-profile-tooling-implementation-boundary.md)
- [ADR-0045](adr/0045-governing-definition-declaration-set-json-representation-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
