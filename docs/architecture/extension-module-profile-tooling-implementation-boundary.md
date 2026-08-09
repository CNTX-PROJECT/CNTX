# CNTX Extension Module and Profile Tooling and Implementation Boundary (ARCH-033)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed, documentation-only architecture decision governed
by [issue #108](https://github.com/CNTX-PROJECT/CNTX/issues/108) and recorded by
[ADR-0033](adr/0033-extension-module-profile-tooling-implementation-boundary.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in issue
comment [5231158990](https://github.com/CNTX-PROJECT/CNTX/issues/108#issuecomment-5231158990).

Creation authority, repository presence, validation, mergeability, and
transparent non-independent ARCHITECT review do not grant acceptance. This
decision remains Proposed until the exact reviewed revision receives separate
attributable EIGENAAR / Final Authority acceptance and a separately authorized
status promotion and governed integration complete successfully.

## Purpose and decision boundary

Accepted ARCH-028 establishes the Extension Module/Profile architecture
boundary. ARCH-029 defines Definition identities and versions. ARCH-030 defines
dependencies, explicit activation, composition, and fail-closed conflicts.
ARCH-031 defines Schema Resource, package, bundle, and declaration boundaries.
ARCH-032 defines the frozen validation context, prerequisite-ordered evaluation,
separate conformance dimensions, bounded results, and evidence relationships.

This decision defines only the fifth roadmap layer: the conceptual boundary
within which future tooling and implementations may be specified, selected,
built, evaluated, reviewed, released, or operated. It defines:

1. distinct tooling and implementation categories;
2. independent identity, version, capability, environment, output, evidence,
   conformance, support, release, and deployment dimensions;
3. the complete frozen execution-context responsibilities;
4. closed, caller-supplied, offline-first, deterministic processing;
5. fail-closed and observable processing conditions;
6. output, evidence, and final-human-authority boundaries;
7. a non-normative reference-implementation boundary;
8. resource, security, privacy, public/private, and lifecycle limits; and
9. dependency-first gates for any later concrete work.

It creates or selects no concrete Definition, Schema Resource, declaration,
package, binding, output format, evidence format, tool, implementation,
interface, runtime, provider, product, hosted service, release, publication,
distribution, support commitment, certification, or deployment.

## Exact decision basis

This decision was prepared on exact public baseline
`61cf29ced99ddebe1304bbcd19e6fa12f6afef84` and tree
`cd2aa9cdabd1fe68e1f0985ace91fad53c870dc8`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-032 and ADR-0001 through ADR-0032;
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
expected results, evidence, limitations, statuses, settings, or authority.

## Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
express requirement strength within this decision. They define a conceptual
boundary only. They do not instantiate, select, authorize, certify, release,
operate, support, host, or deploy any tool or implementation.

## Separate tooling and implementation categories

The following categories remain distinct. One system MAY later participate in
more than one category only when every claimed category, identity, capability,
interface, governing input, output, evidence item, limitation, and authority is
explicitly declared and separately evaluated.

| Category | Bounded future responsibility | Does not establish |
| --- | --- | --- |
| Specification authoring and consistency tooling | Assist authors with source structure, cross-reference, inventory, terminology, and consistency observations. | Normative meaning, acceptance, or authority. |
| Definition, source, and provenance inspection | Inspect exact Definition identities, versions, sources, revisions, and recorded provenance. | Authenticity, trust, activation, or acceptance. |
| Closed supply, resolution, and catalog views | Present caller-supplied exact resources and keys within a frozen context. | Discovery authority, network authority, or registry truth. |
| Dependency, activation, composition, and conflict evaluation | Evaluate declared graphs, active sets, subjects, composition constraints, and fail-closed conflicts. | Permission, precedence, repair, or final decision. |
| Schema Resource, package, and bundle tooling | Inspect or construct identity-preserving views of exact caller-supplied resources and packages. | New identity, canonical bytes, acceptance, or release. |
| Schema evaluation and validation orchestration | Coordinate exact evaluators and prerequisite-ordered phases for a frozen context. | Universal validity, broader conformance, or approval. |
| Output and diagnostic presentation | Present bounded observations, failures, warnings, limitations, and non-execution. | Canonical Validation Output or portable vocabulary. |
| Evidence capture and reproduction support | Preserve exact inputs, environment, commands, observations, provenance, and limitations. | Canonical Portable Conformance Evidence or independent reproduction. |
| Test runner and conformance suite | Execute separately governed cases against exact subjects and capabilities. | Completeness, certification, or universal conformance. |
| Reference implementation | Demonstrate one non-normative interpretation of fully specified requirements. | Specification authority, precedent, or exclusivity. |
| Reusable library or SDK | Expose bounded implementation capabilities to callers. | A standard interface, support commitment, or compatibility guarantee. |
| CLI or API | Provide a separately specified invocation or integration surface. | Governing semantics, authority, or stable protocol. |
| Workflow, automation, engine, scheduler, or orchestrator | Coordinate separately authorized actions and state transitions. | Approval, consequential authority, or implicit execution permission. |
| Runtime or product integration | Embed bounded capabilities in one declared environment or product. | Public-Core conformance, provider neutrality, or deployment fitness. |
| Hosted service, registry, publication, or distribution | Make separately governed artifacts or capabilities available through a channel. | Identity, authenticity, acceptance, currentness, trust, or support. |
| Support, compatibility, certification, or deployment | Govern separately evidenced operational or assurance claims. | Automatic consequence of implementation or successful execution. |

Naming a category is descriptive only. It reserves no implementation scope,
repository, language, dependency, interface, provider, product, service,
release, support line, or deployment target.

## Independent dimensions

The following dimensions MUST remain separate:

| Dimension | Required distinction | Does not imply |
| --- | --- | --- |
| Tool Identity | Stable logical identity for one later separately governed tool definition. | Tool Version or implementation identity. |
| Tool Version | Exact version of one Tool Identity. | Supported specifications or currentness. |
| Implementation Identity | Stable logical identity for one concrete implementation. | Normative status or Tool Identity. |
| Implementation Version | Exact revision of one Implementation Identity. | Compatibility, support, or deployment. |
| Supported specification set | Exact Accepted source identities, versions, and revisions claimed in scope. | Complete capability or conformance. |
| Capability profile | Explicit mechanisms, dialects, vocabularies, limits, and behaviors claimed. | Correctness, availability, or support. |
| Configuration | Exact consequential settings used for one execution. | Identity, capability, or governing authority. |
| Dependency set | Exact implementation and execution dependencies and versions. | Specification dependencies or activation. |
| Execution environment | Exact runtime, platform, locale, encoding, resources, and relevant state. | Portability or independent reproduction. |
| Supplied governing inputs | Exact caller-supplied frozen sources, declarations, resources, packages, bindings, and targets. | Authenticity, acceptance, or permission. |
| Output | Raw and processed observations produced in one execution. | Evidence sufficiency or canonical status. |
| Evidence | Provenance-bearing support for a bounded claim. | Review, decision, approval, or certification. |
| Conformance | One exact dimension-specific claim against exact governing requirements. | Another conformance dimension. |
| Interoperability | Equivalent bounded behavior across exact compared implementations and contexts. | General compatibility or support. |
| Compatibility | Bounded relation among exact identities, versions, interfaces, and evidence. | Future compatibility or support commitment. |
| Security and privacy | Evidence about exact controls, threats, data, and observation scope. | Legal completeness, compliance, or absence of risk. |
| Support | Explicit separately governed commitments for an exact scope and period. | Compatibility, certification, or warranty. |
| Certification | Separately governed attestation or accreditation. | Authority beyond its exact subject and scheme. |
| Release | One exact published or otherwise released subject and channel state. | Support, deployment, or currentness. |
| Deployment | One exact operational placement and environment. | Release quality, conformance, or approval. |

No dimension allocates, selects, activates, authenticates, accepts, approves,
or proves another. Repository presence, successful execution, popularity, or a
claim by a tool or implementation creates no normative authority.

## Frozen execution context

Every consequential future execution MUST use one explicit, closed, frozen,
and exactly pinned context. It MUST identify or preserve:

1. exact governing CNTX Public-Core sources, identities, versions, and
   revisions;
2. exact governing Extension Module/Profile Definition sources, identifiers,
   versions, revisions, and provenance;
3. exact Definition categories and active Definition keys;
4. exact activation roots and activation authority;
5. exact Required Definition Dependencies;
6. exact separately active Optional Definition Dependencies;
7. exact Profile Subjects;
8. complete finite Required dependency closure;
9. one complete Governing Definition Declaration for every active key;
10. the complete frozen Governing Declaration Set;
11. exactly one Schema Resource key or explicit `None` for every active key;
12. exact authoritative Schema Resource sources, versions, revisions, and
    provenance where present;
13. the complete finite, acyclic, exact-versioned Schema Resource graph;
14. the complete closed caller-supplied Definition Package;
15. linked or identity-preserving bundled supply mode;
16. the exact Serialization Binding where applicable;
17. exact Tool Identity and Tool Version where defined;
18. exact Implementation Identity and Implementation Version where defined;
19. exact supported specification set and capability profile;
20. exact tool/implementation dependency set;
21. exact consequential configuration;
22. exact execution environment, runtime, locale, encoding, and observation
    time;
23. exact target and other supplied inputs;
24. explicit resource, memory, CPU, wall-time, recursion, expansion,
    concurrency, file-descriptor, output, log, temporary-storage, and network
    limits;
25. source, supply, configuration, environment, execution, and output
    provenance;
26. limitations, warnings, adverse evidence, unknown, unsupported, ambiguous,
    conflicting, unresolved, and blocked conditions;
27. restricted-evidence, minimization, access, disclosure, and retention
    boundaries;
28. non-executed phases and reasons;
29. raw output, interpretation, and claim boundaries;
30. claimant and exact claim scope;
31. evaluator, reviewer, reproducer, and decision-maker roles where
    applicable; and
32. attributable governing and final-human authority.

The context MUST remain immutable throughout one execution. A change to any
governing source, identity, version, revision, active key, declaration,
dependency, Profile Subject, Schema Resource, package, binding, tool,
implementation, dependency, configuration, capability, environment, target,
limit, evidence boundary, claimant, or authority creates a new context and
requires separate execution and evidence.

## Closed, offline-first, deterministic processing

Governing inputs MUST be caller-supplied, exact, closed, frozen, and available
without automatic network resolution. A tool or implementation MUST NOT infer,
complete, alter, or select governing state from:

- repository, directory, path, filename, or adjacent-file presence;
- discovered identifier, `$id`, URL availability, HTTP response, or redirect;
- registry, catalog, mirror, cache, installation, or package-manager state;
- automatic discovery, retrieval, or network access;
- environment variables, undeclared configuration, product state, or ambient
  process state;
- processor defaults or implementation preference;
- previous success or cached result;
- mutable aliases, `latest`, newest, or latest-wins selection;
- document, load, registration, insertion, dependency, package, or lexical
  order;
- popularity, majority, consensus, score, or ranking; or
- substitution, coercion, defaulting, repair, fallback, or silent capability
  downgrade.

Determinism is bounded to exact inputs, exact context, exact implementation,
exact dependencies, exact configuration, exact environment, and declared
resource limits. It does not promise canonical bytes, universal evaluator
agreement, cross-platform equivalence, interoperability, or reproducibility
beyond the evidenced scope.

## Fail-closed and observable processing

Every material condition MUST retain its own category and provenance. At
minimum, a future execution MUST keep separate:

1. governing-input mismatch;
2. missing input;
3. duplicate input or key;
4. conflicting source, revision, content, or provenance;
5. ambiguous identity, version, activation, dependency, subject, resource,
   package, binding, configuration, capability, or authority;
6. unknown required Definition, Schema Resource, mechanism, or capability;
7. unsupported required mechanism or capability;
8. assertion failure;
9. processing failure;
10. warning;
11. limitation;
12. resource-limit blockage;
13. security/privacy ambiguity or conflict;
14. required but restricted evidence;
15. Unverifiable condition;
16. blocked dependent phase;
17. non-execution; and
18. adverse evidence or unresolved conflict.

Each condition MUST remain visible and fail closed for every dependent claim.
It MUST NOT be hidden, overwritten, upgraded, or silently resolved through a
retry, alternative source, redirect, mirror, hidden cache, previous result,
substitution, coercion, defaulting, repair, fallback, order, newest/latest,
latest-wins, specificity guess, implementation preference, majority,
consensus, score, ranking, aggregation, or automatic conflict resolution.

Failure to execute is not a successful execution. A processing failure is not
an assertion failure. An unsupported capability is not a negative assertion.
A warning is not proof. Restricted evidence is not absent evidence. A blocked
or non-executed phase is not Satisfied or conforming.

## Output and diagnostic boundary

Tool or implementation output is bounded to one exact execution context. It
MUST preserve, where applicable:

- raw observations and their source;
- exact phase, assertion, or processing operation;
- success, failure, warning, limitation, blocked, unsupported, Unverifiable,
  Not Evaluated, and non-execution categories without collapse;
- exact governing inputs, tool, implementation, dependencies, configuration,
  environment, limits, and observation time;
- interpretation and claim provenance;
- adverse and conflicting evidence;
- restricted-evidence and disclosure boundaries; and
- the distinction between technical output, evidence, review, decision, and
  final-human authority.

No output is canonical Validation Output, Portable Conformance Evidence, an
Evidence Bundle, Review Record, Decision Record, certification, release record,
or other Artifact Instance unless a later separately Accepted identity,
version, schema, binding, provenance, lifecycle, and Artifact Instance contract
expressly establishes that status.

Output syntax, diagnostic identifiers, severity, ordering, localization,
media type, serialization, canonicalization, transport, storage, retention,
redaction, and disclosure remain undecided. Implementation-specific output
MUST NOT silently become a portable or normative vocabulary.

## Evidence and reproduction boundary

Evidence capture or reproduction support MAY later record exact supplied
inputs, tools, versions, dependencies, configuration, environment, commands,
resource limits, observations, outputs, failures, warnings, limitations,
adverse evidence, restricted evidence, observation time, and responsible roles.

Such evidence supports bounded reassessment only. It does not automatically:

- become a canonical Portable Conformance Evidence Artifact Instance;
- prove independent reproduction when one operator, environment, provider, or
  implementation performed the work;
- prove universal validator, tool, implementation, Artifact Instance, or
  interoperability conformance;
- prove completeness, security, privacy, legal compliance, support,
  certification, or release fitness; or
- perform review, recommendation, approval, decision, publication, or
  deployment.

Missing, adverse, conflicting, limited, uncertain, or restricted evidence MUST
remain visible. Favorable evidence MUST NOT erase or outweigh it automatically.

## Reference implementation boundary

A future reference implementation, if separately authorized, MUST remain
non-normative. Its code, tests, behavior, defaults, output, limitations, issue
history, popularity, deployment, or maintainer statements MUST NOT:

- fill a specification gap;
- resolve ambiguity as precedent;
- change, replace, weaken, reinterpret, coerce, default, repair, or override
  Core or Definition semantics;
- allocate identity or version;
- activate a Definition, dependency, Profile, declaration, package, resource,
  binding, or authority;
- establish precedence or conflict resolution;
- prove conformance, interoperability, compatibility, security, privacy,
  support, certification, release fitness, or deployment fitness;
- create vendor, language, runtime, provider, product, registry, or platform
  lock-in; or
- exclude another conforming implementation.

Implementation-defined behavior MUST be explicit, bounded, attributable, and
versioned where applicable. It MUST be reported as implementation-defined and
without normative authority. A required but unspecified or ambiguous behavior
MUST fail closed rather than be silently converted into implementation policy.

## Separate conformance and claim dimensions

The following remain independently governed:

1. specification-source conformance;
2. Definition and Schema Resource conformance;
3. Governing Definition Declaration and Declaration Set conformance;
4. Definition Package and bundle conformance;
5. executable-schema and schema-local evaluation;
6. Artifact Contract and Artifact Instance conformance;
7. validator conformance;
8. tool conformance;
9. implementation conformance;
10. interoperability;
11. compatibility;
12. security and privacy;
13. support;
14. certification;
15. release;
16. deployment; and
17. attributable final-human authority.

No successful execution, test run, schema-valid result, matched case set,
reference behavior, published package, or deployed service automatically proves
another dimension. No such event grants identity, provenance, authenticity,
acceptance, activation, applicability, authority, permission, trust, support,
certification, release approval, or deployment approval.

No universal aggregate valid result, pass/fail, traffic light, score, grade,
badge, threshold, rubric, checklist verdict, quality gate, ranking,
recommendation, approval, or consequential authority is defined.

## Security, privacy, and resource boundary

Definitions, sources, declarations, packages, Schema Resources, bundles,
targets, configurations, dependencies, outputs, diagnostics, logs, and evidence
are untrusted input. A later implementation MUST explicitly bound and evidence,
where applicable:

- document, package, resource, declaration, node, edge, reference, target,
  result, and output counts;
- document, package, resource, bundle, target, output, diagnostic, log, and
  temporary-storage size;
- graph depth and breadth;
- recursion and nested composition;
- reference expansion and repeated evaluation;
- regular-expression and general evaluation cost;
- memory, CPU, and wall time;
- concurrency, process/thread use, and file descriptors;
- output, diagnostic, and logging volume;
- temporary-file location, access, lifetime, and cleanup;
- minimization, least privilege, redaction, access, disclosure, retention, and
  restricted evidence; and
- the prohibition or separately governed use of network access.

Limits and enforcement behavior MUST be explicit inputs or capabilities and
part of execution evidence. Exceeding or lacking a required limit MUST remain a
visible resource-blocked or unsupported condition, not be treated as success.

This decision selects no concrete threshold, algorithm, regular-expression
engine, timeout, sandbox, process model, isolation mechanism, permission or
access-control model, filesystem layout, log format, cleanup mechanism,
redaction rule, retention policy, encryption, digest, signature, attestation,
trust store, transport, storage, or network mechanism.

## Public/private and authority boundary

Public CNTX sources MUST remain free of private implementations, private
project context, secrets, credentials, personal data, production
configuration, provider-specific requirements, and restricted evidence unless
a separately approved public-safe contract expressly permits exact material.

A private implementation MAY later conform to public CNTX sources, but private
existence, behavior, tests, configuration, evidence, deployment, or success
MUST NOT modify public semantics, establish precedent, grant authority, or
become a hidden prerequisite for public conformance.

Technical access, authorship, maintainership, execution, review, evidence
production, recommendation, approval, and final decision remain separate.
Tools and implementations MUST NOT allocate authority, approve their own
outputs, infer permission, or perform consequential action without separate
attributable authority.

## Lifecycle and dependency-first future work

Even if this decision later becomes Accepted, it authorizes no concrete tool or
implementation. Every later consequential phase requires an exact baseline,
scope, issue or contract, paths, identity/version policy where applicable,
evidence, transparent review, attributable acceptance, and separate lifecycle.

Dependency-first future work, if separately authorized, proceeds in this order:

1. concrete Extension Module/Profile Definitions;
2. concrete Definition Schema Resources, assertions, cases, and fixed expected
   results;
3. concrete declaration, package, Serialization Binding, Validation Output,
   and Portable Conformance Evidence identities and representations;
4. concrete Tool and Implementation Identity, Version, capability,
   configuration, dependency, and interface contracts;
5. implementation, tests, and bounded evidence production;
6. independent review, reassessment, and attributable decision; and
7. any release, publication, distribution, support, certification, hosting, or
   deployment.

This order authorizes none of those phases and reserves no ARCH, issue, branch,
path, Definition, Schema, Binding, Tool, Implementation, package, interface,
release, provider, product, or deployment identifier or version.

Correction, withdrawal, deprecation, supersession, reassessment, maintenance,
new release cycles, settings changes, and immutable-object changes remain
separately governed. Repository or channel state never creates implied
maintenance, support, compatibility, or currentness authority.

## Consequences and limitations

Positive consequences:

- future tools cannot silently become normative sources;
- every consequential execution has an exact reproducible claim boundary;
- tool, implementation, capability, environment, output, evidence, and broader
  conformance remain independently reviewable;
- missing, conflicting, unsupported, blocked, restricted, and non-executed
  conditions remain visible;
- reference behavior cannot establish precedent or lock-in;
- resource, security, and privacy obligations are explicit before selection or
  implementation; and
- final-human authority remains separate from technical execution.

Costs and limitations:

- callers must supply complete exact governing inputs and provenance;
- no ambient discovery, mutable selection, hidden cache, repair, or fallback is
  available;
- no concrete declaration, package, output, evidence, capability, configuration,
  or interface representation exists;
- no tool, validator, runner, suite, SDK, library, API, CLI, workflow, runtime,
  product, service, or reference implementation exists;
- no implementation, interoperability, compatibility, security/privacy,
  support, certification, release, or deployment claim is proven; and
- multiple separately governed decisions remain necessary before practical
  implementation can be considered.

## Protected predecessors and immutable history

This decision preserves without semantic or object change:

- ARCH-001 through ARCH-032 and ADR-0001 through ADR-0032;
- CONTRACT-001 through CONTRACT-009;
- ten Accepted Schema Versions `1.0.0` and ten synthetic test manifests;
- Core Artifact JSON Binding Version `1.0.0`;
- Accepted resolution/catalog, validation/output, Portable Conformance
  Evidence, release-readiness, assessment, remediation, final-decision,
  release, verification, completion, maintenance, and Extension Module/Profile
  sources;
- Release Version `0.1.0-prealpha.1`;
- immutable tag `v0.1.0-prealpha.1` and exact target
  `109e6f293b150f48572cd747fab446c141d57193`;
- release-subject tree `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- GitHub Release ID `367290932`, node ID `RE_kwDOTsnR984V5Go0`, prerelease
  flags, body, and zero custom assets;
- immutable releases enabled;
- issue #106 and PR #107;
- issue #80 and every historical issue, PR, review, comment, setting, tag,
  Release, commit, tree, and blob.

## Explicit non-decisions

ARCH-033 creates no concrete Extension Module or Profile; Definition Identifier
or Version; Definition Schema Identifier or Version; `$id`; Schema Resource;
executable schema; assertion; case; declaration field or token; package
instance; Validation Output instance; Portable Conformance Evidence instance;
Artifact Instance; portable vocabulary; Tool Identity or Version;
Implementation Identity or Version; capability representation; configuration
schema; dependency manifest; interface contract; protocol; media type; or new
Serialization Binding.

It creates no resolver, registry, catalog, cache, bundler, mirror, redirect,
automatic discovery, retrieval, network access, validator, test runner,
conformance suite, SDK, library, API, CLI, workflow, automation, engine,
scheduler, orchestrator, runtime, provider, product, private implementation,
reference implementation, hosted service, publication, alternate distribution,
support service, compatibility claim, certification, release, tag, GitHub
Release, or deployment.

It performs no project closure, repository archival, maintenance action,
correction, withdrawal, deprecation, supersession, reassessment, new release
cycle, repository-setting mutation, immutable-object mutation, full
repository/issue audit, audit remediation, Claude or Opus interaction,
external-model analysis, optimization proposal, optimization execution,
ARCH-034 allocation, or other follow-on phase.

## Final-human authority

Tools and implementations may produce bounded observations and evidence. They
do not approve, accept, authorize, release, publish, distribute, support,
certify, host, deploy, correct, withdraw, deprecate, supersede, or close work.

Any consequential decision requires separately attributable human authority
under the governing CNTX lifecycle. Ambiguous or missing authority MUST remain
visible and fail closed.

## Current lifecycle state

This document is Proposed. Exactly one candidate revision may be reviewed under
issue #108. The transparent ARCHITECT review is non-independent and cannot
accept the candidate.

After exact-head review, work MUST stop for separate attributable EIGENAAR /
Final Authority acceptance. No Ready-for-review transition, status promotion,
promotion commit, merge, issue completion or closure, branch cleanup, concrete
tooling or implementation, audit, remediation, external-model interaction,
optimization, release, publication, distribution, support, certification,
hosting, deployment, ARCH-034, or other follow-on action is authorized.
