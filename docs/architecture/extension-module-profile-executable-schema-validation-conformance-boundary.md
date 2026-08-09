# CNTX Extension Module and Profile Executable Schema and Validation/Conformance Boundary (ARCH-032)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only architecture decision governed
by [issue #106](https://github.com/CNTX-PROJECT/CNTX/issues/106) and recorded by
[ADR-0032](adr/0032-extension-module-profile-executable-schema-validation-conformance-boundary.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in issue
comment [5230742345](https://github.com/CNTX-PROJECT/CNTX/issues/106#issuecomment-5230742345),
and exact-head acceptance is recorded in issue comment
[5230968570](https://github.com/CNTX-PROJECT/CNTX/issues/106#issuecomment-5230968570).

Creation authority, repository presence, validation, mergeability, and
transparent non-independent ARCHITECT review did not grant acceptance. Separate
attributable EIGENAAR / Final Authority acceptance of the exact reviewed
revision is recorded above; separately authorized status promotion and governed
integration make this decision Accepted.

## Purpose and decision boundary

Accepted ARCH-028 orders Extension Module/Profile decisions dependency-first.
Accepted ARCH-029 defines Definition identity and version dimensions. Accepted
ARCH-030 defines dependencies, explicit activation, finite closure,
composition, and fail-closed conflicts. Accepted ARCH-031 defines Definition
Schema Families, key-or-`None` schema participation, a constrained future
standalone resource model, resource-graph alignment, packages, bundles, and a
logical frozen Governing Declaration Set.

This decision defines only the fourth roadmap layer: the conceptual boundary
for future executable Definition Schema evaluation and its relationship to
validation, conformance, output, evidence, security/privacy, and final human
authority. It defines:

1. the exact frozen validation context responsibilities;
2. separate validation and conformance dimensions;
3. prerequisite-ordered logical evaluation phases;
4. schema-local versus broader CNTX outcome boundaries;
5. future test-case responsibilities;
6. fail-closed conditions and non-execution semantics;
7. validation-output and Portable Conformance Evidence relationships;
8. resource, security, privacy, lifecycle, and authority limits; and
9. the dependency-first handoff to a later Tooling and Implementation Boundary
   decision.

It creates no concrete Extension Module, Profile, child Definition, Schema
Resource, executable schema, assertion, case file, declaration representation,
package instance, validator, tooling, implementation, release, publication, or
deployment.

## Exact decision basis

This decision was prepared on exact public baseline
`3e7a8ba367ab915d30d2ca1c86b2e23cb277b7a4` and tree
`88c7f2a96fee1650cdaafd4697fc2ba49e3b72c0`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-031 and ADR-0001 through ADR-0031;
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

## Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
express requirement strength within this decision. They do not create an
implementation, processor, network service, or authority beyond the stated
architecture boundary.

## Separate validation and conformance dimensions

The following dimensions remain separate:

| Dimension | Governing responsibility | Does not establish |
| --- | --- | --- |
| CNTX Public Core | Conformance to exact Accepted Core sources and versions. | Extension/Profile conformance. |
| Definition | Conformance to one exact authoritative Definition source and Version. | Schema validity or activation. |
| Definition Schema Resource | Conformance of one exact resource to its separately Accepted schema identity, version, dialect, source, and graph obligations. | Definition semantics or authority. |
| Governing Definition Declaration | Completeness and consistency for one active Definition key. | Source authenticity, acceptance, or serialization. |
| Governing Declaration Set | Exact representation of one frozen active Definition Set. | Permission, trust, or Artifact Instance validity. |
| Definition Package | Closed supply of exact governing sources and resources. | Identity, priority, or evidence sufficiency. |
| Executable schema | Evaluation of one target against one exact governing Schema Resource. | Broader contract or Definition conformance. |
| Schema-local result | Valid, invalid, annotation, or processing result within JSON Schema evaluation. | Universal CNTX validity or approval. |
| Artifact Contract and Artifact Instance | Conformance to exact Artifact Contract and governing schemas. | Extension/Profile Definition conformance. |
| Validator | Evidence about one evaluator against exact required behavior. | Implementation or universal validator conformance. |
| Implementation | Evidence about one implementation and supported capability set. | Normative authority or interoperability. |
| Interoperability | Equivalent outcomes for exact shared inputs and contexts. | Compatibility outside the tested scope. |
| Compatibility and support | A bounded claim for exact identities, versions, and evidence. | Mutable selection, guarantee, or SLA. |
| Security and privacy | Evidence for exact controls, threats, and observation scope. | Legal completeness or absence of risk. |
| Certification | A separately governed attestation or accreditation decision. | Automatic consequence of validation. |
| Release | Conformance or readiness for one exact release subject. | General support, deployment, or currentness. |
| Final-human authority | Attributable consequential acceptance or decision. | Technical validity or evidence generation. |

No dimension substitutes for or implies another. Schema validity MUST NOT be
reported as Definition conformance, implementation conformance,
interoperability, security/privacy proof, certification, release fitness,
approval, or authority.

## Frozen Extension Module/Profile validation context

Every consequential Extension Module/Profile evaluation MUST use one explicit,
closed, and frozen validation context. It MUST identify or preserve:

1. exact governing CNTX Public-Core sources, identities, and versions;
2. exact active Extension Module/Profile Definition keys;
3. Definition category for every active key;
4. exact Definition Identifier and Definition Version;
5. authoritative Definition source and exact revision;
6. source provenance and attributable acceptance status;
7. explicit activation root or dependency role;
8. exact Required Definition Dependencies;
9. exact separately active Optional Definition Dependencies;
10. exact Profile Subjects;
11. complete finite Required dependency closure;
12. one Governing Definition Declaration for every and only active key;
13. the complete frozen Governing Declaration Set;
14. exactly one Schema Resource key or explicit `None` per active key;
15. authoritative Schema Resource source and exact revision where present;
16. resource provenance and separately Accepted status where applicable;
17. the complete closed Definition Package;
18. the complete finite, acyclic, exact-versioned resource graph;
19. linked or identity-preserving bundled supply mode;
20. evaluator or processor identity and version where available;
21. declared dialect, vocabulary, mechanism, and capability support;
22. resource, memory, time, recursion, and evaluation limits;
23. processing limitations and known unsupported behavior;
24. adverse, unknown, ambiguous, unresolved, and blocked conditions;
25. restricted-evidence and disclosure boundaries;
26. observation time;
27. claimant and claim scope; and
28. attributable governing and final-decision authority.

The context MUST remain immutable throughout one consequential evaluation. A
change to any governing identity, version, source, revision, active key,
dependency, Profile Subject, Schema Resource key, package, capability, limit,
or evidence boundary creates another context and requires another evaluation.

## Closed input and no-ambient-state rule

The governing context MUST be supplied explicitly. It MUST NOT be completed,
altered, or inferred from:

- repository, directory, path, or filename presence;
- discovered `$id`, URL availability, HTTP response, or redirect;
- registry, catalog, mirror, cache, installation, or package-manager state;
- automatic network discovery or retrieval;
- processor defaults, product configuration, environment variables, or hidden
  state;
- prior successful validation or cached results;
- mutable aliases, `latest`, newest, or latest-wins selection;
- document, load, registration, insertion, package, or lexical order; or
- implementation preference, popularity, majority, consensus, score, or
  ranking.

Caller-supplied inputs remain untrusted. Availability establishes no identity,
authenticity, acceptance, activation, applicability, compatibility, trust, or
authority.

## Prerequisite-ordered logical evaluation phases

An evaluation MUST keep the following phases separate and ordered by
prerequisite. A later phase MAY execute only when its required earlier phases
are sufficiently established for that exact context.

### Phase 1: governing-input supply and exact pins

Confirm that all claimed governing sources, identities, versions, revisions,
keys, resources, packages, capabilities, limits, and evidence boundaries are
explicitly supplied and exactly pinned.

Missing, ambiguous, mutable, or conflicting pins block dependent phases.

### Phase 2: frozen-context completeness

Confirm that the supplied context contains all required responsibilities and
is closed and frozen for the evaluation. Hidden or late-added governing state
is not permitted.

### Phase 3: Definition source and provenance consistency

For every active key, confirm Definition category, Identifier, Version,
authoritative source, exact source revision, provenance, and separately
recorded acceptance state. This phase does not authenticate or accept the
source by technical inspection alone.

### Phase 4: activation and Definition graph consistency

Confirm activation roots, Required dependencies, separately active Optional
dependencies, Profile Subjects, permitted dependency directions, complete
finite closure, acyclicity, one active Version per Identifier, and
source/revision consistency under ARCH-030.

Dependency order establishes evaluation prerequisites only. It creates no
precedence over Core or another Definition.

### Phase 5: declaration conformance

Confirm one complete Governing Definition Declaration for every and only active
Definition key. Confirm that the frozen Governing Declaration Set exactly
equals the active Definition Set and preserves all 21 ARCH-031 logical
responsibilities.

This phase evaluates logical completeness and consistency. It creates no
serialized declaration format, field vocabulary, media type, or Artifact
Instance.

### Phase 6: Definition Package completeness

Confirm that the package supplies every exact governing Definition source,
resource, revision, provenance item, capability declaration, limitation, and
restricted-evidence boundary required by the frozen context. Package layout or
order grants no meaning or priority.

### Phase 7: Definition Schema Binding

For every active Definition key, confirm exactly one explicit governing state:

- one exact Schema Resource key; or
- explicit `None`.

Missing is not `None`. `None` MUST NOT repair a missing, failed, wrong,
unsupported, or unavailable resource. A binding creates no Definition
dependency, activation, authority, or semantic override.

### Phase 8: Schema Resource identity and capability

Where a Schema Resource key is present, confirm its exact Schema Identifier,
Schema Version, authoritative source, revision, provenance, root `$schema`,
canonical `$id`, dialect, vocabulary profile, static-reference mechanisms, and
required evaluator capabilities.

Unsupported required capabilities block schema evaluation. They MUST NOT be
silently ignored, downgraded, substituted, or treated as annotations.

### Phase 9: Schema Resource graph conformance

Confirm that the complete external graph is finite, acyclic, exact-versioned,
fully caller-supplied, and aligned with the ARCH-030 Definition graph:

- Core resources never reference Extension Module/Profile resources;
- Extension Module resources may reference only exact governing Core and
  active Extension Module dependency resources;
- Extension Module resources never reference Profile resources;
- Profile resources may reference only exact governing Core and exact active
  Extension Module subject/dependency resources;
- Profile resources never reference other Profile resources; and
- `$ref` creates no Definition dependency, activation, authority, or
  precedence.

### Phase 10: standalone and bundle equivalence

When resources are supplied in an identity-preserving derived Compound Schema
Document, confirm preservation of every canonical `$id`, `$schema`, static
reference target, independent identity, standalone behavior, exact resource
set, and provenance. Linked and bundled evaluation MUST be equivalent for the
same frozen context.

A mismatch blocks dependent conformance claims and MUST remain visible.

### Phase 11: executable schema evaluation

This phase is applicable only where a later separately Accepted concrete
Definition Schema Resource is explicitly governing. Evaluate only the exact
target, resource, dialect, capability set, and frozen context named by the
claim.

ARCH-032 creates no target representation, concrete schema, assertion, or
evaluation result. Explicit `None` means no Definition-schema evaluation is
governing for that active key; it does not imply Definition conformance.

### Phase 12: Module and Profile composition evaluation

Preserve Core-first constraints, topological Module dependency prerequisites,
additive Module semantics, narrowing-only Profile semantics, and conjunctive
application of multiple explicit Profile roots. Evaluation order MUST NOT
become precedence.

Contradiction, order-dependent outcome, unknown precedence, or Core weakening
blocks the affected claim.

### Phase 13: failure, blocked, unsupported, and non-execution recording

Record each assertion failure, processing failure, warning, limitation,
blocked prerequisite, unsupported capability, unknown condition, and phase not
executed separately. Do not rewrite one category as another.

### Phase 14: output and evidence relation

Relate schema-local output to the broader ARCH-024 validation dimensions and
to the logical ARCH-025 Portable Conformance Evidence responsibilities. Keep
raw observations, interpretations, claims, limitations, adverse evidence,
restricted evidence, and authority distinct.

### Phase 15: scoped conformance statements

Any claim MUST name the exact dimension, subject, governing sources, identities,
versions, revisions, context, evaluator, capabilities, limits, evidence,
limitations, observation time, claimant, and authority. No universal aggregate
result is created.

## Outcomes and schema-local result boundary

For broader CNTX validation dimensions, preserve the ARCH-024 outcomes:

1. `Satisfied`;
2. `Not Satisfied`;
3. `Unverifiable`; and
4. `Not Evaluated`.

`Not Satisfied` means applicable requirements were evaluated and at least one
was not satisfied. `Unverifiable` means the available governing context,
evidence, capability, or access is insufficient for a reliable outcome. `Not
Evaluated` means the dimension was not executed, including because a
prerequisite blocked it.

JSON Schema Draft 2020-12 schema-local validity and output remain bounded to
the exact evaluated instance and resource graph. They MUST NOT be relabeled as
Definition, declaration, package, contract, Artifact Instance, validator,
implementation, interoperability, compatibility, support, security/privacy,
certification, or release conformance.

No aggregate `valid`, pass/fail, traffic light, score, grade, badge, threshold,
rubric, checklist verdict, quality gate, certification, recommendation,
approval, or consequential authority is defined.

## Future synthetic case responsibilities

Every later concrete Definition Schema Version MUST be accompanied by
separately governed synthetic cases appropriate to its assertions and graph.
The case set MUST cover, where applicable:

- expected-valid examples;
- one or more expected-invalid cases for every material assertion family;
- wrong Definition Identifier or Version;
- wrong Schema Identifier or Version;
- wrong Definition or Schema source/revision;
- missing declaration versus explicit `None`;
- missing Required dependency;
- undeclared or ambient Optional dependency;
- wrong Profile Subject;
- prohibited Core-to-extension reference;
- prohibited Module-to-Profile reference;
- prohibited Profile-to-Profile reference;
- resource or Definition cycle;
- duplicate Definition key;
- multiple active Versions for one Identifier;
- conflicting source, revision, content, or provenance;
- linked-versus-bundled equivalence;
- unsupported dialect, vocabulary, keyword, or capability;
- unknown required Definition or Schema Resource;
- order-dependent outcome;
- Module collision or Profile contradiction;
- attempted Core weakening or repair;
- resource-count, size, depth, recursion, expansion, memory, time, or cost
  blockage;
- adverse evidence;
- required but restricted evidence; and
- expected blocked, Unverifiable, and Not Evaluated behavior.

Expected outcomes MUST be fixed before evaluator execution. Evaluator results
MUST NOT silently rewrite case inputs or expected results. A case set does not
prove completeness, validator conformance, interoperability, security/privacy,
compatibility, support, certification, or release fitness.

ARCH-032 creates no concrete test manifest, case, fixture, coverage threshold,
test runner, or conformance suite.

## Fail-closed conditions

The following conditions MUST remain separately visible and fail closed for
dependent claims:

1. missing, duplicate, ambiguous, or conflicting declaration;
2. missing authoritative Definition or Schema source;
3. Definition category, Identifier, Version, source, or revision mismatch;
4. provenance conflict or insufficiency;
5. activation-root, active-set, dependency, Profile Subject, or closure
   mismatch;
6. self-dependency, cycle, or multiple active Versions per Identifier;
7. missing, wrong, ambiguous, conflicting, or unsupported Schema Resource;
8. missing declaration incorrectly treated as `None`;
9. `None` used as repair, fallback, or capability substitution;
10. unsupported dialect, vocabulary, keyword, or required evaluator mechanism;
11. undeclared, wrong-version, unresolved, or prohibited `$ref`;
12. resource-graph mismatch or cycle;
13. standalone/bundled identity or behavior mismatch;
14. order-dependent schema or composition outcome;
15. Module collision, Profile contradiction, or Core weakening;
16. unknown precedence or unsupported required Definition;
17. incomplete evaluation or non-executed prerequisite;
18. insufficient, adverse, conflicting, or required restricted evidence;
19. security/privacy ambiguity or disclosure conflict; and
20. resource, memory, time, recursion, expansion, or evaluation-cost condition
    preventing reliable complete evaluation.

No blocked condition may be resolved silently by document, load,
registration, package, insertion, or lexical order; specificity guesses;
newest, `latest`, or latest-wins; popularity; implementation preference;
cache; previous success; majority; consensus; score; ranking; coercion;
defaulting; repair; substitution; or fallback.

This decision creates no portable conflict, error, severity, warning, status,
or outcome vocabulary.

## Validation-output relationship

ARCH-024 remains controlling. JSON Schema Flag, Basic, Detailed, or Verbose
output MAY be retained as schema-local evaluator material. Such output does not
replace broader CNTX validation-output responsibilities for:

- exact frozen governing context;
- target and conformance dimension;
- evaluator identity/version and capabilities;
- phase execution and prerequisite state;
- schema-local results and processing failures;
- blocked, unsupported, Unverifiable, and Not Evaluated conditions;
- warnings, limitations, uncertainty, and adverse evidence;
- restricted-evidence and disclosure boundaries;
- reproducibility and observation time; and
- claimant and attributable authority.

No concrete validation-output identity, version, field, schema, media type,
serialization, diagnostic vocabulary, API, or CLI is created.

## Portable Conformance Evidence relationship

ARCH-025 remains controlling. Logical evidence for a claim MUST preserve exact
claim scope, governing requirements, source and resource pins, package and
declaration context, evaluator/capability provenance, observations, failures,
limitations, uncertainty, adverse and conflicting evidence, restricted
evidence, reproduction responsibilities, claimant, and authority.

Logical evidence is not automatically a Portable Conformance Evidence Artifact
Instance, canonical Validation Output, Evidence Bundle, Conformance Claim,
Review Record, Decision Record, certification, accreditation, release record,
or approval. Production by ARCHITECT or one evaluator environment does not
establish independent reproduction.

Evidence supports review and decision; it does not perform them.

## Security, privacy, and resource boundary

Every Definition source, Schema Resource, declaration, package, bundle,
evaluation target, validation output, and evidence input is untrusted. A later
implementation MUST explicitly bound:

- resource count and document/package size;
- graph depth, recursion, and reference expansion;
- evaluation time, memory, and computational cost;
- malicious or ambiguous identity, version, and provenance;
- dependency substitution and conflicting-source attacks;
- dialect, vocabulary, keyword, and capability abuse;
- disclosure, restricted evidence, data minimization, and least privilege;
- error and diagnostic information exposure;
- unknown and unsupported mechanisms; and
- correction and withdrawal handling.

Credentials, secrets, personal data, production configuration, private paths,
private project context, restricted evidence, and private implementation
details remain outside public CNTX sources.

ARCH-032 selects no concrete limit, timeout, sandbox, process isolation,
access-control mechanism, redaction or sanitization algorithm, cryptographic
integrity mechanism, digest, signature, trust store, attestation, or
correction/withdrawal procedure. It grants no access, permission, disclosure,
authenticity, trust, security, privacy, legal, compliance, or absence claim.

## Lifecycle and historical integrity

Every future concrete Definition, Definition Schema allocation, Schema
Version, resource, representation, test manifest, validation output,
evidence protocol, implementation, correction, withdrawal, deprecation, or
supersession requires a new exact baseline, scope, issue or contract, evidence,
limitations, review, attributable acceptance, integration, completion,
synchronization, and separately authorized cleanup where applicable.

Accepted Definitions and Schema Resources remain immutable per their exact
Versions. A correction or supersession MUST NOT rewrite historical meaning,
content, evidence, output, or release objects in place. Mutable aliases and
newest/latest-wins grant no authority.

ARCH-001 through ARCH-031, ADR-0001 through ADR-0031, Contract Definitions,
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
processor capability, schema validity, review, or implementation cannot grant
acceptance or consequential authority. EIGENAAR / Final Authority remains the
final human authority for public acceptance, activation mechanisms,
representations, schemas, implementations, releases, publications, and
deployments.

## Dependency-first tooling and implementation handoff

Only after this decision is separately Accepted and integrated may the
resulting public `main` be reassessed read-only and a distinct Tooling and
Implementation Boundary decision be prepared.

That later decision MUST first establish what can be meaningfully implemented
without a concrete Extension Module/Profile Definition, concrete Definition
Schema Resource, serialized declaration, package representation, validation
output protocol, or conformance evidence Artifact Instance. It MUST distinguish
specification tooling, reference implementation, product/runtime behavior,
hosting, distribution, support, and deployment.

ARCH-032 selects no repository, programming language, dependency, package,
resolver, validator, registry, catalog implementation, test runner, API, CLI,
runtime, distribution, support model, hosted service, or product.

This handoff authorizes no later phase and reserves no ARCH number, issue,
branch, path, identifier, version, schema, tool, implementation, release, or
authority.

## Non-decisions and prohibited effects

This decision creates no concrete Extension Module or Profile, child Definition
Identifier or Version, Definition Schema Identifier or Schema Version,
namespace, `$id`, Schema Resource, repository schema file, executable
assertion, case file, target representation, declaration field or serialized
token, Artifact Instance, Extension Module instance, Profile instance, package
instance, manifest, media type, new Serialization Binding, portable
conflict/error/severity/outcome vocabulary, custom dialect or vocabulary,
Format-Assertion, Hyper-Schema, or dynamic-reference mechanism.

It creates no resolver, registry, catalog, cache, bundler, mirror, redirect,
automatic discovery, retrieval, network access, validator implementation, test
runner, conformance suite, canonical JSON, digest, signature, verification,
attestation, certification, API, CLI, workflow, automation, engine, scheduler,
orchestrator, runtime/provider/product work, private or reference
implementation, hosted publication, alternate distribution, support service,
release, tag, GitHub Release, deployment, project closure, repository archival,
maintenance action, correction, withdrawal, deprecation, supersession,
reassessment, new release cycle, settings mutation, or follow-on authority.

No ARCH-033 number, title, issue, branch, path, contract, candidate, or phase is
created, reserved, or authorized.

## Lifecycle and final human authority

This Accepted document did not approve itself. Creation authority, repository
presence, validation, transparent non-independent ARCHITECT review,
mergeability, technical access, and implementation capability grant no
consequential authority.

Separate attributable EIGENAAR / Final Authority exact-head acceptance is
recorded in issue comment `5230968570`; separately authorized status promotion
and governed integration make this decision Accepted. Acceptance adopts only
this conceptual boundary and creates or activates no concrete Definition,
schema, declaration, package, tooling, implementation, release, publication,
distribution, hosting, or deployment.

## References

- [Extension Module and Profile Architecture Boundary](extension-module-profile-architecture-boundary.md)
- [Extension Module and Profile Identity and Version Policy](extension-module-profile-identity-version-policy.md)
- [Extension Module and Profile Dependency, Activation, Composition and Conflict Policy](extension-module-profile-dependency-activation-composition-conflict-policy.md)
- [Extension Module and Profile Schema Resource, Packaging and Declaration Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Portable Conformance Evidence Boundary](portable-conformance-evidence-boundary.md)
- [Core Artifact JSON Serialization Binding](core-artifact-serialization-binding.md)
- [Public-Core Completion and Maintenance Boundary](public-core-completion-and-maintenance-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0032](adr/0032-extension-module-profile-executable-schema-validation-conformance-boundary.md)
