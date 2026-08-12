# CNTX Context Packet Epistemic Provenance and Freshness Profile JSON Representation Boundary (ARCH-043)

## In ordinary language

ARCH-039 defines what the Context Packet Profile means. ARCH-043 proposes one
closed JSON-compatible record that can state how that exact Profile is applied
to one exact Context Packet revision under one exact approved Task Contract
revision, without changing either Core artifact.

| Quick view | Meaning |
| --- | --- |
| **Status** | Proposed documentation-only representation boundary |
| **Governing Profile** | `context-packet-epistemic-provenance-freshness` Definition `1.0.0` |
| **Target** | One exact Context Packet Artifact Instance/Revision under one exact approved Task Contract Artifact Instance/Revision |
| **What this establishes** | One closed standalone Profile application record, exact source-to-Module-declaration associations, narrowing-only responsibilities, explicit conditions/evaluations/limitations, and final-human authority |
| **What this does not do** | It creates no Profile instance, Core property, schema, testcase, policy instance, rule, Tool, execution, evidence, aggregate result, or automatic authority |

### Reading route

- [Purpose and boundary](#purpose-and-decision-boundary)
- [Exact governing pins](#exact-governing-profile-and-subject-pins)
- [Closed root](#closed-fourteen-member-root)
- [Source association](#sourceassociations)
- [Conditions and evaluations](#conditions-and-evaluations)
- [Core and activation boundaries](#core-sovereignty-placement-and-activation)
- [Consequences and limitations](#consequences-and-limitations)

This visitor layer is non-normative and adds no requirement beyond the full
Proposed text below.

## Status and authority

**Document Status:** Proposed.

This documentation-only candidate is governed by
[issue #147](https://github.com/CNTX-PROJECT/CNTX/issues/147). Attributable
EIGENAAR / Final Authority acceptance of the exact issue contract is recorded
in issue comment
[5273569440](https://github.com/CNTX-PROJECT/CNTX/issues/147#issuecomment-5273569440).
The accepted issue body contains exactly 28,358 characters, 28,360 UTF-8 bytes,
and SHA-256
`7b154b7738e0ae4cae6ea5b78cdaf24f2c51ecd89c7883dca0a38e19215dfa6b`.
The exact public baseline is commit
`9f482043f76c792f6c2e1e96eb4a535ee26b3a99`, tree
`7b2f45791e3b7bff7e856f26fff9b22598c06709`, with 200 tracked paths.

Issue-contract acceptance authorizes preparation and review of one Proposed
candidate only. Proposed status, branch or repository presence, static
validation, Draft PR state, review, rendering, parsing, or mergeability does
not accept, allocate, activate, integrate, release, or deploy ARCH-043. Exact-
head attributable acceptance and later separately governed integration to
`main` remain necessary.

## Purpose and decision boundary

Accepted ARCH-039 defines one narrowing-only Profile Definition for applying
the Accepted Epistemic Provenance and Freshness Extension Module Definition to
the Accepted Context Packet Contract Definition. It deliberately creates no
Profile application property, representation, schema, rule, implementation,
or execution.

This Proposed decision defines exactly one standalone closed JSON-compatible
Profile application/declaration record. The record applies the exact Accepted
Profile Definition to one exact Context Packet Artifact Instance/Revision
under one exact approved Task Contract Artifact Instance/Revision. It is the
dependency-ordered bridge to a possible later separately governed Profile
Definition Schema Resource.

The record is outside the closed Context Packet Core payload. It references one
exact ARCH-040 Module declaration for each selected Context Packet source and
does not copy, redefine, open, or replace the thirteen-member Module
representation.

The record is not a Profile Definition, Profile Definition Version, Profile
Subject, Profile instance, Context Packet, Task Contract, Module declaration,
Core Artifact, generic Governing Definition Declaration, declaration set,
activation package, policy, evidence record, validation output, review,
decision, approval, release, or deployment record.

## Accepted basis and precedence

This Proposed boundary remains subordinate to and preserves:

1. ARCH-039 and ADR-0039 as the exact Accepted narrowing-only Profile source;
2. ARCH-040 and ADR-0040 as the exact Accepted closed Module declaration
   representation that is referenced and never duplicated;
3. integrated ARCH-042 and ADR-0042, the exact Module Definition Schema
   Resource and its fixed separate 48-case manifest;
4. ARCH-028 through ARCH-033 for category, sovereignty, identity/version,
   Profile Subjects, dependency, activation, composition, conflict,
   declaration, schema, conformance, Tool, and final-authority boundaries;
5. the Accepted Context Packet Contract Definition, representation, Schema
   Resource, and exact `1.0.0` pins;
6. the Accepted Task Contract Definition, representation, Schema Resource, and
   exact governing Task Contract Artifact Instance/Revision relation;
7. every Accepted Core architecture, contract, schema, binding, rule,
   Tool/Implementation, evidence, release, and authority source; and
8. the integrated corrective Implementation `1.0.1` history and exact
   ten-schema supported set.

If a member or meaning cannot be justified by the exact Accepted Profile and
its two Profile Subjects, it is not part of this representation. Nothing here
repairs, broadens, weakens, overrides, defaults, or silently completes an
Accepted source.

## Exact governing Profile and subject pins

The representation is governed by exactly:

| Coordinate | Exact value |
| --- | --- |
| Definition category | `CNTX Profile Definition` |
| Profile local name | `context-packet-epistemic-provenance-freshness` |
| Profile Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/profile-definitions/context-packet-epistemic-provenance-freshness` |
| Profile Definition Version | `1.0.0` |
| Profile Subject 1 Identifier | `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet` |
| Profile Subject 1 Version | `1.0.0` |
| Profile Subject 2 Identifier | `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness` |
| Profile Subject 2 Version | `1.0.0` |

Every Definition and Profile Subject pin also carries one exact authoritative
source revision. Identifier, Version, and authoritative source revision remain
separate. URI shape causes no lookup, network access, redirect, registry use,
existence, authenticity, acceptance, compatibility, support, or authority.

No second Profile Definition identity or version, Profile Representation
Identifier or Version, Serialization Binding, media type, schema identity, or
canonical `$id` is allocated.

## Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
express requirement strength inside this Proposed decision. They create no
processor, execution permission, acceptance, or consequential authority.

## Closed fourteen-member root

The root is a closed object with exactly these fourteen required lower-camel-
case members:

1. `governingProfileDefinition`;
2. `profileSubjects`;
3. `application`;
4. `targetContextPacket`;
5. `governingTaskContract`;
6. `sourceAssociations`;
7. `selectedCapabilities`;
8. `governingContext`;
9. `supply`;
10. `activationContext`;
11. `conditions`;
12. `evaluations`;
13. `limitations`; and
14. `authority`.

Every root member is present. The root and all subordinate objects are closed.
Unknown members, extension bags, wildcard namespaces, vendor fields, and
ambient metadata are prohibited. Conditional absence is represented through
explicit conditions or an exact empty/Assessed None form defined below, never
through omitted roots, JSON `null`, empty strings, processor defaults, repair,
coercion, or fallback.

Object-member order carries no meaning. Array order carries meaning only for a
source-preserving derivation transformation sequence whose source declaration
states that sequence is material. No root, array, source, Profile, document,
lexical, insertion, package, or processor order creates precedence,
specificity, authority, or conflict resolution.

## `governingProfileDefinition`

`governingProfileDefinition` is a closed object with exactly four required
members:

- `definitionIdentifier` — the exact Profile Definition Identifier above;
- `definitionVersion` — exactly `1.0.0`;
- `definitionCategory` — exactly `CNTX Profile Definition`; and
- `authoritativeSourceRevision` — the exact Accepted public source revision
  supplied for this application.

This object pins meaning; it does not embed the Profile Definition, select a
new version, retrieve a source, prove acceptance, or activate the Profile.

## `profileSubjects`

`profileSubjects` is a closed object with exactly two required members:

- `contextPacketContractDefinition`; and
- `epistemicProvenanceFreshnessModuleDefinition`.

Each member is a closed object containing exactly
`definitionIdentifier`, `definitionVersion`, and
`authoritativeSourceRevision`. The Identifier and Version values are the exact
Profile Subject pins above. The property names distinguish the two subjects;
their textual or processing order creates no precedence.

Neither subject pin is a schema reference, artifact relation, dependency
range, retrieval instruction, compatibility claim, or activation statement.

## `application`

`application` is a closed object with exactly:

- required `applicationIdentifier`, a stable opaque identity for this bounded
  application/declaration record;
- required `applicationRevision`, its exact opaque revision;
- required `relationship`, exactly `external-profile-application`;
- required `supersedes`, a duplicate-free array of exact prior application
  identity/revision pairs, which is empty only when no predecessor is claimed;
- required `scope`, a closed object that states the exact bounded purpose,
  intended use, exact Task Contract-relative materiality boundary, and
  prohibited uses; and
- required `nonAggregation`, a closed declaration that technical members and
  outcomes remain separate and create no aggregate result.

Application identity is not Profile Definition identity, Profile instance
identity, Artifact Instance identity, schema identity, activation identity,
approval, or authority. A supersession reference preserves lineage only; it
does not mutate, invalidate, withdraw, retrieve, or replace another record.

## `targetContextPacket`

`targetContextPacket` is a closed object with exactly:

- `artifactInstanceIdentifier`;
- `artifactRevision`;
- `contractDefinitionIdentifier`;
- `contractDefinitionVersion`;
- `schemaIdentifier`;
- `schemaVersion`; and
- `authoritativeSourceRevision`.

The Contract Definition Identifier/Version and Schema Identifier/Version must
be the exact Accepted Context Packet `1.0.0` coordinates applicable to the
supplied target. The exact Artifact Instance Identifier and Revision identify
one target only. The source revision binds the representation inspected for
this application.

These pins prove no existence, retrieval, schema validity, contract
conformance, sufficiency, freshness, approval, or authority.

## `governingTaskContract`

`governingTaskContract` is a closed object with exactly:

- `artifactInstanceIdentifier`;
- `artifactRevision`;
- `contractDefinitionIdentifier`;
- `contractDefinitionVersion`;
- `schemaIdentifier`;
- `schemaVersion`;
- `authoritativeSourceRevision`; and
- `approvalReference`.

The Artifact Instance Identifier and Revision MUST exactly equal the
`payload.governingTaskContract` pin inside the exact target Context Packet.
Mismatch, absence, ambiguity, conflicting pins, unavailable governing source,
or missing approval reference remains visible and blocks every dependent
favorable claim. The application record cannot approve or repair a Task
Contract.

## `sourceAssociations`

`sourceAssociations` is a non-empty array that accounts for every entry in the
exact target Context Packet revision's `payload.selectedSources.items`
collection exactly once. Each closed association contains exactly:

- `associationIdentifier`, unique within the application;
- `contextPacketSourceIndex`, the zero-based array index in the exact pinned
  Context Packet revision;
- `sourceReference`, repeated exactly from the selected-source entry at that
  index as a fail-closed equality check;
- `claimRoles`, a non-empty duplicate-free set of explicit opaque bounded
  roles;
- `sourceCategories`, a non-empty duplicate-free set containing only the six
  exact Accepted tokens below;
- `materiality`, the exact Task Contract-relative material source and claim
  boundary plus rationale;
- `moduleDeclaration`, one exact ARCH-040 Module declaration identity/revision
  and its exact authoritative representation-source revision;
- `applicability`, the bounded selected/narrowed Profile applicability context;
- `provenance`, separate origin, custody, acquisition, observation, supply,
  transformation, responsible-role, limitation, adverse-information, and
  restricted-information public-safe references;
- `temporal`, separate references for the four Accepted temporal coordinates
  and their clock/reference provenance;
- `policies`, exact freshness and applicability policy Identifier/Version,
  authoritative source revision, and applicability-context pins where used;
- `integrity`, explicit digest-claim references with algorithm identity, exact
  subject boundary, verification context, evidence, limitations, and no
  implicit authenticity or integrity conclusion;
- `derivation`, finite source-preserving input and transformation references
  without execution meaning;
- `conditionRefs`, all applicable explicit condition identifiers;
- `limitationRefs`, all applicable limitation identifiers; and
- `authorityRefs`, attributable role and governing-authority references.

The six and only source-category tokens are:

1. `governing-source`;
2. `observation-source`;
3. `evidence-source`;
4. `derived-source`;
5. `human-assertion-source`; and
6. `model-recollection-source`.

`contextPacketSourceIndex` is a locator only inside one exact supplied Context
Packet revision. It creates no semantic array ordering, stable cross-revision
identity, ranking, priority, authority, or canonical serialization. The
repeated `sourceReference` MUST exactly match the selected-source entry at that
index, but `sourceReference` is not presumed unique.

Every selected-source index occurs exactly once. Missing, repeated, out-of-
range, non-integer, mismatching, ambiguous, conflicting, non-matching, or
orphan association data remains visible and blocks dependent favorable claims.
No lookup, discovery, redirect, registry, filesystem access, or network
retrieval is caused.

`moduleDeclaration` references rather than embeds the Accepted ARCH-040
declaration. It MUST NOT copy its thirteen-member model, select another Module
shape, or treat schema validity or repository presence as activation.

Model recollection remains visible, attributable where possible, non-governing,
and possibly stale, incomplete, or wrong. It cannot replace exact governing
sources, revision pins, retrieval evidence, policy pins, validation evidence,
or human decisions.

## `selectedCapabilities`

`selectedCapabilities` is a non-empty array of closed narrowing declarations.
Each contains exactly:

- `capabilityIdentifier`, unique within the application and local to this
  declaration only;
- `dimension`, one of the seventeen exact Accepted dimension tokens;
- `subject`, the exact bounded subject of the narrowing;
- `narrowingStatement`, which selects, requires, limits, or narrows existing
  subject meaning without adding or weakening it;
- `sourceAssociationRefs`, a non-empty duplicate-free set;
- `claimRefs`, a duplicate-free set, empty only when no claim is applicable;
- `policyRefs`, a duplicate-free set, empty only when no policy applies;
- `conditionRefs`, a duplicate-free set;
- `evaluationRefs`, a duplicate-free set;
- `limitationRefs`, a duplicate-free set; and
- `authorityRefs`, a non-empty duplicate-free set.

The seventeen exact dimension tokens are:

`source-category`, `source-identity`, `source-revision`,
`source-availability`, `provenance`, `authenticity`, `integrity`,
`source-publication-revision-time`, `observation-retrieval-time`,
`record-production-time`, `valid-through-time`, `freshness`, `applicability`,
`clock-reference-provenance`, `derivation`, `validation`, and `evidence`.

A capability declaration creates no new governing capability or globally
stable capability vocabulary. Every declaration must trace to the exact
Accepted Profile and one or both exact subjects. All applicable constraints
compose conjunctively and order independently.

## `governingContext`

`governingContext` is a closed reference object with exactly:

- `contextIdentifier` and `contextRevision` for one caller-supplied frozen
  governing context;
- `declarationSetReference` and exact revision for the separately governed
  frozen declaration set;
- `definitionSourcePins`, a complete duplicate-free collection of every exact
  governing Definition source Identifier/Version/revision used;
- `prerequisiteRefs`, a complete duplicate-free collection;
- `conflictRefs`, a duplicate-free collection that is empty only when conflict
  was explicitly assessed and none is declared; and
- `authorityRefs`.

This member references but does not define or serialize a generic Governing
Definition Declaration Set, package, activation root, registry, resolver, or
reusable activation syntax.

## `supply`

`supply` is a closed object with exactly:

- `supplierRoleRefs`;
- `supplyProvenanceRefs`;
- `suppliedDefinitionSourcePins`;
- `suppliedModuleDeclarationPins`;
- `targetContextPacketSupplyRef`;
- `governingTaskContractSupplyRef`;
- `restrictionAndAccessConditionRefs`; and
- `limitationRefs`.

Required collections are non-empty and duplicate-free except a restriction or
limitation collection may be empty only when an explicit Assessed None
condition records that assessment. Supply remains exact, closed, caller-
supplied, identity preserving, bounded, and offline first. It grants no access,
disclosure, authenticity, compatibility, trust, or authority.

## `activationContext`

`activationContext` is a closed reference object with exactly:

- `activationContextIdentifier`;
- `activationContextRevision`;
- `applicationRelationship`, exactly `referenced-prerequisite-context`;
- `prerequisiteRefs`;
- `conflictRefs`;
- `nonExecutionRefs`; and
- `authorityRefs`.

This record is not the activation root. It neither serializes the generic
activation mechanism nor activates itself, the Profile, a Module, a Context
Packet, a Tool, or a consequential action. Consequential use requires all
separately Accepted declarations, exact frozen context, satisfied
prerequisites, and separately attributable authority.

## `conditions` and `evaluations`

`conditions` is a closed array of zero or more separately attributable
condition declarations. The exact condition tokens are:

1. `specified`;
2. `assessed-none`;
3. `not-assessed`;
4. `missing`;
5. `inaccessible`;
6. `conflicting`;
7. `restricted`; and
8. `unverifiable`.

Every condition contains exactly `conditionIdentifier`, `condition`,
`dimension`, `subject`, `sourceAssociationRefs`, `claimRefs`, `evidenceRefs`,
`limitationRefs`, `responsibleRoleRefs`, `dependentCapabilityRefs`, and
`explanation`. References may be empty only when their semantic
inapplicability is explicit. Exact condition key combinations are unique.

`evaluations` is a closed array of zero or more separate dimension-level
evaluation declarations. The only outcome tokens are:

1. `satisfied`;
2. `not-satisfied`;
3. `unverifiable`; and
4. `not-evaluated`.

Every evaluation contains exactly `evaluationIdentifier`, `outcome`,
`dimension`, `subject`, `capabilityRefs`, `sourceAssociationRefs`, `claimRefs`,
`governingSourcePins`, `policyRefs`, `conditionRefs`, `evidenceRefs`,
`observationAndReferenceContext`, `diagnostics`, `limitationRefs`,
`adverseAndRestrictedInformationRefs`, `nonExecutionRefs`, and
`responsibleRoleRefs`.

Assessed None is not Missing. Not Assessed is not Assessed None. Inaccessible
is not absent. Restricted is not favorable proof. Unverifiable condition is
not automatically an Unverifiable evaluation, and Unverifiable evaluation is
not Not Satisfied.

No condition, evaluation, count, ordering, majority, weighting, ranking,
diagnostic, schema result, or processor output creates an aggregate pass/fail,
score, percentage, threshold, traffic light, grade, badge, quality gate,
recommendation, approval, certification, release fitness, deployment fitness,
or consequential authority.

## `limitations`

`limitations` is a closed object with exactly these required members:

- `scopeLimitations`;
- `minimalityLimitations`;
- `sourceCoverageLimitations`;
- `methodLimitations`;
- `evidenceLimitations`;
- `accessLimitations`;
- `securityPrivacyLimitations`;
- `resourceLimitations`;
- `adverseInformation`;
- `restrictedInformationMetadata`; and
- `unknownUnsupportedOrNonExecuted`.

Each member is either a non-empty duplicate-free array of closed attributable
limitation declarations or one explicit closed `assessed-none` declaration.
Completeness, minimality, and source coverage remain separate reviewable claims
and never prove each other, quality, correctness, safety, or sufficiency.

Restricted metadata contains only the minimum authorized public-safe
orientation needed to preserve existence, role, restriction, claim effect,
and limitation. It does not reveal or replace protected information.

## `authority`

`authority` is a closed object with exactly these required role-reference
collections:

- `declaringRoles`;
- `selectingRoles`;
- `supplyingRoles`;
- `applyingRoles`;
- `evaluatingRoles`;
- `reviewingRoles`;
- `governingRoles`; and
- `finalHumanAuthorityRoles`.

Every role reference carries an opaque identity, role label, bounded scope,
and attribution/provenance reference. The representation creates no person,
account, organization, credential, authentication, authorization, access
control, signature, delegation, voting, approval, or identity-verification
system.

The semantic invariant `automaticAuthority: false` is fixed but is not a
serialized member. Its absence cannot be interpreted as true, configurable,
defaulted, missing, or unknown. Technical output never becomes self-
acceptance, merge permission, release approval, deployment approval, or final-
human authority.

## Absence, null, duplicates, and unknown input

Absence, JSON `null`, empty string, empty object, empty array, Assessed None,
Not Assessed, Missing, Inaccessible, Restricted, Conflicting, and Unverifiable
remain distinct.

All root members and all members listed as exact for a subordinate object are
required. Empty strings and JSON `null` never satisfy a value. Empty arrays are
permitted only where this document expressly defines zero items as the exact
meaning and any required semantic absence assessment is represented
separately.

Identifiers and exact key combinations are duplicate-free within their stated
scope. Repeated identical limitations are non-conforming redundancy.
Non-identical declarations about the same exact subject/dimension/key are a
visible conflict, not an override.

Unknown members or tokens are not ignored, retained as extensions, mapped,
coerced, defaulted, repaired, substituted, downgraded, ranked, or resolved by
majority. An exact unknown supplied value may appear only in public-safe
condition or adverse-information text; every dependent favorable claim
remains blocked.

## Core sovereignty, placement, and activation

This representation is separate from and adds no property to:

- the Common Artifact Envelope;
- the Context Packet Contract or payload;
- Context Packet Schema Version `1.0.0`;
- the Task Contract Contract or payload;
- Task Contract Schema Version `1.0.0`;
- any other Core Artifact, contract, representation, schema, or binding; or
- the exact ten-schema Tool/Implementation supported set.

Core validity remains a prerequisite. A Profile application cannot make an
invalid Context Packet valid, repair a missing Task Contract pin, replace an
Artifact Contract, weaken a schema assertion, select a source, or grant
authority. Core does not depend on this Profile.

Presence, parsing, member order, repository path, URL, filename, supply,
future schema validity, implementation recognition, or prior use activates
nothing. No registry, discovery, network retrieval, redirect, mutable alias,
version range, `latest`, fallback, repair, substitution, downgrade, or ambient
implementation selection is allowed.

All applicable exact constraints compose conjunctively and order
independently. Conflict, ambiguity, duplicate incompatible pins, missing
supply, wrong identity/version, unsupported input, or an unsatisfied
prerequisite remains visible and fails closed. There is no precedence,
specificity-wins, latest-wins, majority, override, implicit merge, or automatic
conflict resolution.

## Representation, schema, rule, and execution boundary

ARCH-043 defines only this JSON-compatible member model. It allocates no
Profile Definition Schema Identifier, Schema Version, canonical `$id`, media
type, repository schema path, executable Schema Resource, assertion, manifest,
testcase, expected validity, fixture, policy instance, rule, diagnostic
vocabulary, Tool/Implementation capability/version, dependency, runner,
execution, output, or evidence.

It also selects no JSON text canonicalization, timestamp/calendar syntax,
digest algorithm/encoding, freshness duration, threshold, tolerance, grace
period, task/source-class vocabulary, clock service, transformation
vocabulary, severity, or portable conformance-output shape.

It performs no validation, policy evaluation, source access, network
operation, digest verification, clock verification, transformation, execution,
testing, evidence production, review decision, release, or deployment.

Representation validity is not Profile conformance, Context Packet validity,
source truth, authenticity, integrity, freshness, applicability, completeness,
correctness, safety, trust, acceptance, approval, certification, release
fitness, deployment fitness, or authority.

## Security, privacy, and resources

Every supplied value is untrusted. Public records MUST NOT include
credentials, secrets, private keys, production configuration, unnecessary
personal data, private paths, private project content, or restricted content
merely to make the record complete.

Restricted-information metadata must not disclose protected information
through filenames, paths, identifiers, query strings, error text, timing,
roles, hashes of guessable content, or derivation detail.

This decision selects no maximum size, count, length, nesting depth,
derivation depth, time, memory, CPU, handle, thread, process, recursion,
expansion, redaction, sanitization, access control, encryption, sandbox,
process-isolation, or network-control mechanism. Later schema and
implementation work must separately bound resources and preserve non-
execution when complete reliable processing is not possible.

## Lifecycle and change boundary

Proposed ARCH-043 consumes no identity or version. A later exact-head
acceptance would establish Accepted status only. Status promotion, Ready state,
review, repository presence, and mergeability do not integrate or activate the
representation. Separately governed integration remains required.

A correction may fix documentary error without silently changing represented
meaning. Any normative member, token, requiredness, structure, condition,
reference, association, or semantic change requires a separately governed
compatibility and version decision. Historical sources and authority records
remain source preserved.

Only after exact-head acceptance, governed integration, completion,
synchronization, and separately authorized cleanup may public `main` be
reassessed for a possible Phase 4A3.4 Profile Definition Schema Resource. This
decision reserves no ARCH number, Schema Identifier/Version, `$id`, path,
assertion, case, expected result, validator capability, or authority for that
work.

## Consequences and limitations

Positive consequences:

- ARCH-039 receives one inspectable target representation before schema work;
- exact Profile, subject, packet, Task Contract, Module declaration, supply,
  and authority pins remain separate;
- every selected Context Packet source receives one deterministic packet-local
  association without assuming `sourceReference` uniqueness;
- explicit conditions, evaluations, limitations, and unfavorable information
  cannot be hidden by omission or defaults;
- Core and ARCH-040 remain unchanged; and
- no aggregate or automatic authority is introduced.

Costs and limitations:

- the explicit closed record is intentionally verbose;
- callers must supply exact pins, frozen context, provenance, associations,
  conditions, limitations, and roles instead of ambient context;
- the packet-local source index is meaningful only within the exact supplied
  Context Packet revision and is not cross-revision identity;
- no schema or implementation checks the representation yet;
- preparation and review are non-independent;
- no implementation, interoperability, performance, portability, security,
  privacy-completeness, resource, or adversarial execution evidence exists;
  and
- structural completeness cannot prove truth, authenticity, integrity,
  freshness, applicability, correctness, safety, trust, support, or fitness.

## Alternatives not selected

### Add Profile data to the Context Packet payload

Not selected because Core Schema Version `1.0.0` is immutable and the Profile
must remain an external narrowing-only application.

### Reuse `sourceReference` as the association key

Not selected because the Accepted Context Packet does not guarantee that value
is unique. A zero-based locator plus exact repeated-value check is
deterministic inside one exact pinned revision without changing Core.

### Hash the selected-source entry

Not selected because that would require a digest algorithm, exact byte or
canonicalization boundary, and verification semantics not authorized here.

### Embed the ARCH-040 Module declaration

Not selected because a Profile may narrow the exact Accepted Module
representation but cannot duplicate, redefine, or replace its closed model.

### Define a generic activation or declaration package

Not selected because ARCH-043 is limited to one Profile application record and
cannot serialize the generic ARCH-030/031 mechanisms.

### Collapse conditions and outcomes into one status or score

Not selected because conditions and evaluations answer different questions,
and aggregate scoring would violate non-aggregation and final-human authority.

### Create the Profile schema now

Not selected because Schema Resource identity, assertions, cases, execution,
and Tool support belong to later separately governed work.

## Protected history and explicit non-decisions

ARCH-001 through ARCH-042, ADR-0001 through ADR-0042, all nine Artifact
Contracts, all eleven existing Schema Resources, all 32 existing JSON files,
historical and ARCH-042 cases/references/pins, thirteen integrity rules, Tool
and Implementation identities/versions/tests/dependencies/scenarios/evidence,
corrective `1.0.1`, settings, ruleset, tag, immutable prerelease, H2.4, and all
historical authority records remain unchanged except the separately authorized
present-state wording correction for completed ARCH-042 integration.

This Proposed decision creates no eighth path, second candidate commit,
Accepted status, Ready transition, merge, issue closure, branch cleanup,
Profile instance, Profile Schema Resource, Core property, JSON file, testcase,
policy instance, rule, Tool/Implementation version, supported-set expansion,
dependency, code, execution, evidence instance, workflow, CI, setting, release,
tag, publication beyond the governed issue/candidate/PR records, support,
certification, hosting, deployment, H2.4 completion, Phase 4A3.4, Phase 4A3.5,
or later-phase authority.

## Final-human authority and stopgate

`automaticAuthority: false` remains controlling. No representation, parser,
later schema result, condition, evaluation, evidence reference, review, score,
majority, tool, implementation, or model becomes final authority.

Work stops after one transparent non-independent `COMMENTED` review and final
read-only verification at a new attributable EIGENAAR / Final Authority exact-
head candidate-acceptance gate. No merge, issue closure, branch cleanup,
schema work, execution, release, deployment, or later phase is authorized.

## References

- [Core architecture contract](core-contract.md)
- [Context Packet Contract](../contracts/context-packet-contract.md)
- [Context Packet Executable Schema](context-packet-executable-schema.md)
- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Extension Module and Profile Identity and Version Policy](extension-module-profile-identity-version-policy.md)
- [Extension Module and Profile Dependency, Activation, Composition and Conflict Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [Extension Module and Profile Schema Resource, Packaging and Declaration Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [Context Packet Epistemic Provenance and Freshness Profile Definition](context-packet-epistemic-provenance-freshness-profile-definition.md)
- [Epistemic Provenance and Freshness Extension Module JSON Representation Boundary](epistemic-provenance-freshness-extension-module-json-representation-boundary.md)
- [Epistemic Provenance and Freshness Extension Module Definition Schema Resource](epistemic-provenance-freshness-extension-module-definition-schema-resource.md)
- [ADR-0043](adr/0043-context-packet-epistemic-provenance-freshness-profile-json-representation-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
