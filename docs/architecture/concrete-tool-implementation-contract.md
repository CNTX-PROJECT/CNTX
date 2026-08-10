# CNTX Concrete Validation and Integrity Tool and Implementation Contract (ARCH-037)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed, documentation-only architecture candidate governed
by public issue [#120](https://github.com/CNTX-PROJECT/CNTX/issues/120).
Attributable EIGENAAR / Final Authority acceptance of the exact issue/task
contract is recorded in issue comment
[`5243736163`](https://github.com/CNTX-PROJECT/CNTX/issues/120#issuecomment-5243736163).

The accepted issue body is pinned to public baseline commit
`d8e9d71ae4c65bf74e31a9a19b1875316df26c8f` and tree
`5db225d96cea975eb05484eac4a9d09bb0622d07`, contains `5,619`
characters and `5,621` UTF-8 bytes, and has SHA-256
`228692c1bcc7d5f27b75d39d0bba2c25de02ccc2a3bd0fe4ff6e4d168212d8ed`.

Issue-contract acceptance authorizes preparation and review only. It does not
accept this candidate, activate an identity or version, install a dependency,
create executable code, execute a schema or testcase, release a tool, or grant
consequential authority. Exact-head acceptance and governed integration remain
separate later gates.

## Purpose and decision boundary

Accepted ARCH-034 through ARCH-036 define the documentation contracts needed
to record validation execution, bounded evidence and reproduction, both
historical Test Manifest forms, thirteen initial Cross-Record Integrity Rules,
and individual Integrity Evaluation results. CNTX still has no concrete Tool
Identity, Implementation Identity, executable runner, or accepted mechanism
that can perform those responsibilities.

This candidate proposes the exact contract for one small future validation and
integrity slice. It proposes:

1. one stable Tool Identity and initial Tool Version;
2. one separate Implementation Identity and initial Implementation Version;
3. one exact supported specification set;
4. explicit capabilities and non-capabilities;
5. exact proposed runtime and dependency pins;
6. closed configuration and execution-environment responsibilities;
7. bounded logical input, output, diagnostic, and evidence interfaces;
8. deterministic ordering and fail-closed behavior;
9. resource, security, privacy, disclosure, retention, and cleanup limits; and
10. separate provenance, claim, review, decision, and final-human-authority
    boundaries.

This is Package D. It remains documentation only. It creates no code, package,
executable schema, dependency installation, runtime environment, Tool Instance,
Implementation Instance, Validation Execution Record instance, Evidence and
Reproduction Package instance, Integrity Evaluation Record instance, canonical
Validation Output, Portable Conformance Evidence, workflow, CI, release,
service, hosting, or deployment.

## Governing traceability

This candidate is subordinate to and preserves:

- ARCH-001 through ARCH-036 and ADR-0001 through ADR-0036;
- CONTRACT-001 through CONTRACT-009;
- Core Artifact JSON Binding Version `1.0.0`;
- all ten Accepted Schema Resources and their exact Version `1.0.0` identities;
- all ten historical synthetic Test Manifests and their exact Git objects;
- the exact static manifest inventory `203/38/165`;
- Accepted Validation Execution Record Definition and JSON Representation
  Version `1.0.0`;
- Accepted Validation Evidence and Reproduction Package Definition and JSON
  Representation Version `1.0.0`;
- Accepted Test Manifest, Cross-Record Integrity Rule, and Cross-Record
  Integrity Evaluation Record Definition and JSON Representation Versions
  `1.0.0`;
- the thirteen Accepted Cross-Record Integrity Rule Identities and Rule
  Versions `1.0.0`;
- Accepted Tooling and Implementation Boundary ARCH-033;
- immutable Release Version `0.1.0-prealpha.1`; and
- attributable final human authority.

No statement here changes a predecessor, schema byte, testcase, expected-
validity statement, historical evidence record, release object, or historical
Git/GitHub object.

## Terminology

**Tool** means the logical, implementation-independent bounded capability
contract proposed here. It states what one tool version may claim to do.

**Implementation** means one concrete, separately identified realization of
that Tool contract. Its language, runtime, dependencies, code, build, and
behavior are not normative specification sources.

**Supported Specification Set** means the complete closed list of exact
Accepted specification, definition, representation, schema, manifest, and rule
versions that Tool Version `1.0.0` claims to process. It is not a claim that
every valid CNTX source, future version, extension, profile, or artifact is
supported.

**Invocation** means one future bounded execution using one exact frozen input
set, configuration, implementation, dependency set, environment, and limit
set. This candidate performs no invocation.

**Logical Interface** means the required information crossing a boundary. It
does not select a CLI, API, SDK, process protocol, transport, media type,
filesystem layout, service, or deployment.

**Raw Tool Output** means implementation-produced observations. It is not by
itself canonical Validation Output, Portable Conformance Evidence, an Evidence
Bundle, a Review Record, a Decision Record, certification, release evidence,
or final-human authority.

## Proposed identities and initial versions

This candidate proposes exactly these independent identity/version pairs:

| Dimension | Proposed exact value |
| --- | --- |
| Tool Identity | `https://github.com/CNTX-PROJECT/CNTX/tools/minimal-validation-integrity-slice` |
| Tool Version | `1.0.0` |
| Implementation Identity | `https://github.com/CNTX-PROJECT/CNTX/implementations/minimal-validation-integrity-slice/python-jsonschema` |
| Implementation Version | `1.0.0` |

The HTTPS-shaped identifiers are opaque identities, not retrieval authority.
They authorize no network access, redirect, registry lookup, package download,
hosted content, installation, trust, support, release, or deployment.

Tool Identity, Tool Version, Implementation Identity, Implementation Version,
supported specification set, capability, configuration, dependency set,
runtime, environment, input, output, diagnostic, evidence, conformance,
interoperability, compatibility, security/privacy, support, certification,
release, deployment, and final-human authority remain separate dimensions. No
dimension implies, allocates, selects, activates, authenticates, accepts,
approves, certifies, or proves another.

Repository presence, a Proposed status, static validation, transparent review,
or later successful execution does not activate these values. Only later
attributable exact-head acceptance and governed integration may activate the
exact accepted candidate.

## Proposed supported specification set

Tool Version `1.0.0` proposes support for exactly the closed set below. Any
missing, additional, ambiguous, conflicting, or differently versioned member
is outside the supported set and fails closed for every dependent operation.

### Schema language, binding, and resources

| Supported member | Exact version or identity |
| --- | --- |
| JSON data model and document syntax | RFC 8259 through Accepted Core Artifact JSON Binding Version `1.0.0` |
| Schema language and dialect | JSON Schema Draft 2020-12 under Accepted ARCH-007 |
| Vocabulary profile | The exact standard vocabulary profile selected by Accepted ARCH-007 |
| Core Artifact JSON Binding | `1.0.0` |
| Common Artifact Envelope Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0` |
| Project Charter Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0` |
| Workstream Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/workstream/1.0.0` |
| Task Contract Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/task-contract/1.0.0` |
| Context Packet Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/context-packet/1.0.0` |
| Execution Result Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0` |
| Evidence Bundle Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0` |
| Review Record Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0` |
| Decision Record Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0` |
| State Snapshot Schema Resource | `https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0` |

Every Schema Resource is caller-supplied and identity-preserving. Its `$id` is
an opaque identity. It MUST NOT trigger HTTP retrieval or location trust.

### Validation-layer definitions and representations

The supported set includes exactly Version `1.0.0` of each identity below:

- `https://github.com/CNTX-PROJECT/CNTX/definitions/validation-execution-record`;
- `https://github.com/CNTX-PROJECT/CNTX/bindings/validation-execution-record-json`;
- `https://github.com/CNTX-PROJECT/CNTX/definitions/validation-evidence-reproduction-package`;
- `https://github.com/CNTX-PROJECT/CNTX/bindings/validation-evidence-reproduction-package-json`;
- `https://github.com/CNTX-PROJECT/CNTX/definitions/test-manifest`;
- `https://github.com/CNTX-PROJECT/CNTX/bindings/test-manifest-json`;
- `https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-rule`;
- `https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-rule-json`;
- `https://github.com/CNTX-PROJECT/CNTX/definitions/cross-record-integrity-evaluation-record`;
  and
- `https://github.com/CNTX-PROJECT/CNTX/bindings/cross-record-integrity-evaluation-record-json`.

### Test Manifests and case construction

The supported set includes exactly the ten historical manifests under
`tests/schemas/*/1.0.0/cases.json` in the frozen supplied repository revision.
It recognizes exactly:

- nine direct manifests whose cases contain complete `instance` values; and
- one State Snapshot operation-based manifest with `baseInstance`, exact
  `caseConstruction`, and ordered `add`, `remove`, or `replace` operations.

The static expected inventory is exactly `203` cases, `38` expected-valid, and
`165` expected-invalid. A future invocation MUST derive and compare these
counts. It MUST NOT repair, rewrite, migrate, skip, duplicate, or silently
reinterpret a supplied manifest or case.

### Cross-record rules

The supported set includes exactly these thirteen Accepted Rule Identities,
each at Rule Version `1.0.0`, under
`https://github.com/CNTX-PROJECT/CNTX/rules/cross-record/`:

1. `supplied-record-exists`;
2. `identity-version-revision-complete`;
3. `record-key-unique`;
4. `identity-revision-content-consistent`;
5. `reference-resolves-exactly-once`;
6. `task-context-execution-chain`;
7. `validation-record-subject-link`;
8. `evidence-package-execution-link`;
9. `role-overlap-visible`;
10. `review-independence-declared`;
11. `self-review-prohibited`;
12. `self-acceptance-prohibited`; and
13. `automatic-authority-false`.

Rule order creates no precedence. Each applicable rule keeps its own exact
outcome: `satisfied`, `not-satisfied`, `unverifiable`, or `not-evaluated`.
Those outcomes remain separate from the eight Validation Execution Record
phase outcomes. No aggregate pass/fail or authority result is supported.

### Explicitly unsupported specification scope

Tool Version `1.0.0` does not claim support for:

- a future schema, contract, Definition, Representation, Binding, Rule, or
  version not listed above;
- any concrete Extension Module or Profile Definition, declaration, Schema
  Resource, package, activation set, or Profile Subject;
- automatic repository-wide discovery or arbitrary graph evaluation;
- remote schemas, registries, catalogs, mutable aliases, redirects, or network
  resolution;
- YAML, XML, JSON5, comments, duplicate JSON member names, or non-JSON input;
- canonical JSON, canonical Validation Output, Portable Conformance Evidence,
  certification evidence, release evidence, or deployment evidence;
- a universal conformance verdict; or
- support, certification, release, publication, hosting, or deployment.

## Proposed Tool capability profile

Tool Version `1.0.0` proposes exactly these bounded capabilities:

| Capability | Proposed responsibility |
| --- | --- |
| `strict-json-input` | Parse caller-supplied JSON as strict UTF-8, reject BOM, duplicate member names, comments, invalid JSON values, and trailing non-whitespace bytes. |
| `closed-resource-registration` | Register exactly the ten caller-supplied Schema Resources by exact `$id` and reject missing, duplicate, conflicting, or additional active resources. |
| `static-reference-closure` | Resolve static `$ref` values only within the exact registered resource set and preserve missing or conflicting targets as failures. |
| `draft-2020-12-schema-check` | Check each supplied Schema Resource against the exact supported JSON Schema Draft 2020-12 dialect and vocabulary profile. |
| `direct-manifest-construction` | Read direct cases without changing their supplied instance values. |
| `operation-manifest-construction` | Deep-copy the supplied State Snapshot base and apply declared ordered operations under ARCH-036 semantics. |
| `case-evaluation` | Evaluate each constructed case against its exact pinned Schema Resource and retain actual validity, expected validity, and diagnostics separately. |
| `inventory-comparison` | Derive manifest/case/construction counts and compare them to exact caller-supplied expected counts without aggregate authority. |
| `cross-record-rule-evaluation` | Evaluate only the thirteen exact Rule Identities against one closed caller-supplied record set. |
| `validation-record-production` | Produce one bounded candidate Validation Execution Record representation for one invocation. |
| `evidence-package-production` | Produce one bounded candidate Validation Evidence and Reproduction Package representation for one invocation. |
| `integrity-record-production` | Produce one bounded candidate Cross-Record Integrity Evaluation Record representation for one supplied record set. |
| `deterministic-presentation` | Present manifests, cases, rules, results, diagnostics, and limitations in the deterministic ordering defined below. |
| `non-execution-recording` | Record blocked, unsupported, restricted, unverifiable, not-evaluated, and non-executed work without treating it as success. |

The words `production` and `produce` describe a future output capability. They
do not create an Artifact Instance or grant canonical status. Package E must
provide code, tests, execution, and evidence before any capability claim can be
assessed.

## Explicit Tool non-capabilities

Tool Version `1.0.0` does not:

- discover repositories, files, schemas, records, packages, or rules;
- retrieve from a network, registry, catalog, package service, redirect, or
  mutable URL;
- install or upgrade its runtime or dependencies;
- infer an active Definition Set or governing source from location, order,
  popularity, previous state, or a `latest` alias;
- modify a supplied repository, input, schema, manifest, testcase, record, or
  expected result;
- repair, normalize, coerce, default, substitute, retry, fall back, or silently
  downgrade a capability;
- execute unlisted Extension Module/Profile semantics;
- evaluate truth, source authenticity, evidence relevance or sufficiency,
  reviewer independence, security/privacy fitness, legal compliance, support,
  certification, release fitness, or deployment fitness beyond an exact
  supported rule's bounded observable requirements;
- review, approve, accept, merge, release, publish, support, certify, host, or
  deploy anything;
- create a score, grade, badge, traffic light, threshold, checklist verdict,
  quality gate, recommendation, or universal pass/fail; or
- make an automatic or final-human decision.

## Proposed Implementation contract

Implementation Version `1.0.0` proposes one non-normative realization of Tool
Version `1.0.0`. Its proposed implementation language is Python. Its schema
evaluation mechanism is the `jsonschema` package. Cross-record rules, strict
input handling, deterministic ordering, record construction, and resource
limits remain implementation responsibilities that Package E must implement
and test explicitly.

The implementation MUST NOT fill a specification gap, resolve ambiguity as
precedent, alter an Accepted source, infer authority, or exclude another later
conforming implementation. Any implementation-defined behavior MUST be
visible, bounded, attributable, and versioned where consequential. Required
but unspecified or ambiguous behavior fails closed.

This proposed first implementation is not designated as a normative reference
implementation. Even if later described as a reference implementation, ARCH-
033's non-normative reference-implementation boundary remains controlling.

## Proposed runtime and dependency set

Implementation Version `1.0.0` proposes exactly this closed runtime and
distribution set:

| Dependency dimension | Proposed exact value | Role |
| --- | --- | --- |
| Runtime | CPython `3.13.14` | Execute the future implementation. |
| Direct distribution | `jsonschema` `4.26.0` | JSON Schema Draft 2020-12 evaluation. |
| Resolved distribution | `attrs` `26.1.0` | Exact dependency of the evaluated environment. |
| Resolved distribution | `jsonschema-specifications` `2025.9.1` | Exact dependency of the evaluated environment. |
| Resolved distribution | `referencing` `0.37.0` | Exact resource registration and offline reference support dependency. |
| Resolved distribution | `rpds-py` `2026.6.3` | Exact dependency of the evaluated environment. |

These values reuse an exact historically observed public evidence set. That
history supports feasibility only. It does not prove the future implementation
exists, is correct, secure, reproducible, compatible, supported, or accepted.

No package is installed by this candidate. Package E must separately govern
the concrete dependency acquisition method, integrity pins, isolated
environment, build inputs, lock or manifest representation, installation,
execution, and cleanup. If any exact runtime or distribution is unavailable,
conflicting, substituted, differently resolved, or unverified, the future
invocation fails closed and remains non-executed.

Python standard-library modules used later are part of the exact CPython
runtime but still require explicit implementation provenance. Operating-system
libraries, interpreter build details, architecture, and platform components
that can affect behavior belong in the execution environment and evidence;
they are not silently excluded from the dependency boundary.

## Proposed configuration contract

Every future invocation MUST receive one complete immutable configuration. The
configuration has exactly these consequential responsibilities:

1. Tool Identity and Tool Version;
2. Implementation Identity and Implementation Version;
3. exact supported specification set;
4. exact caller-supplied repository commit and tree or equivalent immutable
   subject revision;
5. exact Schema Resource identity-to-content mapping;
6. exact Test Manifest set and construction form per manifest;
7. exact Cross-Record Rule Identity/Version set;
8. exact supplied record set for integrity evaluation;
9. JSON Schema dialect and vocabulary profile;
10. format behavior: no `FormatChecker` supplied and format remains annotation-
    only;
11. automatic network resolution: disabled;
12. duplicate JSON member handling: reject;
13. unknown or additional active input handling: reject;
14. deterministic ordering rules;
15. resource and output limits;
16. security/privacy, disclosure, retention, and cleanup boundaries;
17. exact output destinations supplied by the caller;
18. claim scope and attributable roles; and
19. `automaticAuthority`, exactly `false`.

There is no default configuration. Missing, duplicated, ambiguous,
conflicting, unknown, unsupported, or differently versioned configuration
fails closed before dependent processing. Environment variables, current
working directory, adjacent files, installed packages, locale defaults,
previous results, caches, and host state MUST NOT silently supply configuration.

## Proposed execution-environment contract

One future invocation MUST record at least:

- runtime identity, version, implementation, build, and executable digest or an
  explicit inability to provide the digest;
- operating-system identity, version, architecture, and relevant patch state;
- exact installed distribution names, versions, and integrity/provenance pins;
- locale, timezone, encoding, newline, and filesystem case behavior;
- process identity and applicable user/permission boundary without disclosing
  personal data;
- available and applied memory, CPU, wall-time, concurrency, process/thread,
  file-descriptor, temporary-storage, output, diagnostic, and log limits;
- network state, which MUST prohibit automatic external access;
- input and output locations as role-relative caller-supplied references, not
  private machine paths in public evidence;
- observation start and end times where an Accepted representation permits
  them, or an explicit not-representable limitation; and
- environment provenance, limitations, warnings, adverse evidence, and
  restricted evidence.

An environment difference creates a different execution context. Equivalent
results across environments may support one bounded interoperability claim only
after separate evidence and review. They do not prove universal portability.

## Logical input interface

One future invocation accepts only one explicit caller-supplied frozen input
bundle. The logical input boundary contains:

1. invocation identity and immutable revision;
2. exact Tool and Implementation identity/version pins;
3. the complete configuration described above;
4. exact governing architecture, ADR, contract, binding, Definition,
   Representation, Schema Resource, manifest, and rule source pins;
5. exactly ten Schema Resource documents and their exact identity/content/
   digest/provenance mapping;
6. exactly ten Test Manifest documents and their exact location/content/
   digest/provenance mapping;
7. zero or more exact subject records for the thirteen Cross-Record Integrity
   Rules, with explicit record keys, identities, versions, revisions, digests,
   kinds, roles, and provenance;
8. exact expected static inventory and expected-validity declarations;
9. exact requested operations and phase applicability;
10. resource/security/privacy/disclosure/retention/cleanup limits;
11. allowed output destinations and disclosure classification;
12. claim scope, requester, executor, reviewer, decision-maker, acceptor, and
    Final Authority declarations; and
13. explicit network prohibition and `automaticAuthority: false`.

The bundle is logical. This candidate selects no archive format, directory
layout, filename convention, CLI argument, API field, SDK type, transport,
storage service, or executable interface. Package E must propose any concrete
invocation representation within a separate exact allowlist and authority.

Missing, additional, duplicate, ambiguous, conflicting, malformed,
unsupported, inaccessible, restricted, or unpinned required input prevents all
dependent phases. The implementation MUST NOT discover or substitute it.

## Processing sequence and deterministic ordering

A future Implementation Version `1.0.0` invocation MUST preserve this logical
dependency order:

1. verify exact invocation, Tool, Implementation, configuration, environment,
   role, limit, and authority pins;
2. parse each supplied JSON document strictly without mutation;
3. verify the exact closed supported specification set and source digests;
4. register exactly the ten Schema Resources by exact identity;
5. evaluate static reference closure without network access;
6. check each Schema Resource against the supported dialect/profile;
7. recognize each Test Manifest as exactly direct or operation-based;
8. construct cases without rewriting the supplied manifests;
9. evaluate every individually identified case against its exact schema;
10. preserve expected validity, actual validity, and diagnostics separately;
11. derive and compare manifest/case inventory counts;
12. evaluate each applicable Cross-Record Integrity Rule independently;
13. construct bounded candidate records and evidence references;
14. verify record-local and supported cross-record integrity;
15. record outputs, diagnostics, limitations, warnings, adverse/restricted
    evidence, blocked conditions, and non-execution; and
16. finalize provenance and claim scope without review, acceptance, or
    authority.

No later phase may execute when a prerequisite phase is not satisfied for that
dependency. Independent remaining phases may continue only when their inputs
and claims do not depend on the failed phase, and the partial nature remains
explicit.

Presentation order is deterministic:

- Schema Resources by exact Schema Identifier, then Schema Version;
- manifests by exact Schema Identifier, candidate Schema Version, then exact
  supplied manifest key;
- cases by exact supplied case order within each manifest, while preserving a
  separate exact case key;
- rules by exact Rule Identifier, then Rule Version;
- rule results by Rule Identifier, Rule Version, then exact subject key tuple;
- diagnostics by phase identifier, subject key, rule or case key, diagnostic
  category, and stable implementation-local diagnostic identifier;
- limitations and warnings by stable implementation-local identifier; and
- evidence and claims by their exact local reference identifiers.

Ordering is presentation behavior only. It creates no priority, precedence,
severity, authority, conflict resolution, newest-wins meaning, or aggregate
result.

## Logical output interface

One future invocation may emit only these separately identified output groups:

1. invocation metadata and exact context pins;
2. per-phase Validation Execution Record candidate content;
3. per-schema and per-case raw evaluation observations;
4. derived manifest/case inventory observations;
5. per-rule Cross-Record Integrity Evaluation Record candidate content;
6. Validation Evidence and Reproduction Package candidate content;
7. diagnostics;
8. warnings;
9. limitations;
10. adverse and conflicting evidence;
11. restricted-evidence references and disclosure conditions;
12. blocked conditions and non-execution records;
13. dependency, runtime, configuration, environment, resource, and timing
    provenance; and
14. bounded claims and `automaticAuthority: false`.

Each output group must retain its exact producing Tool/Implementation version,
input revision, configuration, environment, phase, subject, and provenance.
Raw output, interpreted observations, evidence items, claims, reviews,
decisions, and acceptance remain separate.

This candidate selects no canonical serialization, filename, directory,
stream, media type, severity vocabulary, localization, transport, storage,
database, API response, CLI output, UI, or publication format. Any future
concrete representation requires separate authority.

## Diagnostic interface

Every diagnostic MUST retain:

- one stable implementation-local diagnostic identifier;
- exact phase and operation;
- exact subject, manifest, case, record, reference, or rule key;
- exact category;
- a bounded human-readable explanation;
- exact related input and source references;
- observed and expected information where safely representable;
- resource or security/privacy boundary involvement;
- related evidence, warning, limitation, and blocked-phase references; and
- disclosure/redaction state and provenance.

At minimum the following categories remain separate:

1. governing-input mismatch;
2. missing input;
3. additional or duplicate input;
4. malformed input;
5. conflicting identity, version, revision, content, digest, or provenance;
6. ambiguous reference, role, configuration, capability, or authority;
7. unknown requirement;
8. unsupported capability;
9. schema-definition failure;
10. reference-closure failure;
11. case-construction failure;
12. assertion failure;
13. cross-record integrity failure;
14. processing failure;
15. warning;
16. limitation;
17. resource-limit blockage;
18. security/privacy ambiguity or conflict;
19. restricted evidence;
20. `unverifiable`;
21. `not-evaluated`;
22. blocked dependent phase;
23. non-execution; and
24. adverse evidence or unresolved conflict.

A processing failure is not an assertion failure. An unsupported capability is
not a negative assertion. A warning is not proof. Restricted evidence is not
absent evidence. A blocked or non-executed phase is not satisfied, valid, or
conforming.

## Evidence interface and reproduction boundary

The future implementation may construct Package B candidate content only from
exact invocation evidence. Each evidence item MUST have one unique package-
local reference and must preserve:

- exact subject, claim, phase, case, rule, and output relationships;
- source identity, version, revision, digest, origin, and observation method;
- Tool, Implementation, dependency, configuration, runtime, environment, and
  resource-limit context;
- expected observation, actual observation, and difference;
- reproduction inputs and ordered steps;
- output and diagnostic references;
- limitation, warning, adverse, restricted, blocked, and non-execution state;
- responsible roles and observation time where representable; and
- minimization, disclosure, retention, and cleanup boundaries.

Every local reference must resolve exactly once within its governing closed
representation. Every supported cross-record reference must be assessed by the
applicable Accepted rule against the exact supplied set. A successful mapping
does not prove source existence outside that set, authenticity, relevance,
sufficiency, independence, trust, or truth.

Evidence from one operator, implementation, provider, environment, or run is
not independent reproduction. Repeating the same execution is not automatically
new evidence. Reproduction differences, missing sources, restricted evidence,
and uncertainty remain visible.

## Fail-closed behavior

Every material condition remains visible and attributable. The implementation
MUST NOT hide, overwrite, upgrade, or silently resolve a condition through:

- automatic discovery, retrieval, redirect, registry, mirror, or network;
- hidden cache, prior output, ambient process or package state;
- mutable alias, `latest`, newest, latest-wins, or local-preferred selection;
- source, file, registration, manifest, rule, or lexical order;
- substitution, coercion, normalization, defaulting, repair, retry, fallback,
  or silent capability downgrade;
- specificity guesses, implementation preference, popularity, majority,
  consensus, score, ranking, or aggregation; or
- suppression, redaction, or omission without an explicit disclosure reason.

Missing, ambiguous, conflicting, unknown, unsupported, blocked, restricted,
inaccessible, unverifiable, not-evaluated, resource-blocked, non-executed, and
adverse states fail closed for each dependent operation and claim. They do not
become an aggregate failure verdict and do not automatically block unrelated
observable work.

## Resource boundaries

Each future invocation requires caller-supplied finite limits for applicable:

- input document, schema, manifest, case, operation, record, reference, rule,
  result, diagnostic, evidence, limitation, warning, and output counts;
- individual and total byte sizes;
- JSON node counts and nesting depth;
- resource-graph node/edge counts, depth, breadth, and reference expansion;
- recursion, composition, repeated evaluation, regular-expression, and general
  evaluation cost;
- memory, CPU, wall time, concurrency, process/thread, file-descriptor,
  temporary-storage, log, diagnostic, and output use; and
- reproduction-step and retained-evidence size.

Reaching a limit stops the affected operation and all dependent operations. It
must produce a visible resource-limit diagnostic and non-execution record where
possible within the remaining safe output budget. A limit is not a threshold
for conformance, quality, acceptance, or authority.

This candidate chooses no numeric thresholds, timeout values, sandbox,
container, operating system, process model, scheduler, access-control model,
temporary-directory mechanism, or cleanup implementation. Package E must
propose exact safe values and mechanisms before execution.

## Security, privacy, disclosure, retention, and cleanup

All schemas, manifests, records, configuration, dependencies, paths, outputs,
diagnostics, logs, and evidence are untrusted input or derived untrusted data.
A future implementation MUST:

- use least privilege and a caller-approved isolated environment;
- prohibit automatic network access during frozen execution;
- avoid evaluating executable content from supplied JSON;
- reject path traversal, unauthorized external references, unsafe symbolic
  link behavior, and writes outside caller-approved output locations;
- minimize collected and retained data;
- never place secrets, credentials, tokens, personal data, private project
  context, production configuration, or exploitable restricted detail in public
  output;
- preserve restricted evidence by safe opaque reference and visible impact,
  not by public disclosure;
- bound logs, diagnostics, temporary files, and error excerpts;
- apply explicit redaction and disclosure decisions without converting redacted
  evidence into absent evidence;
- record retention and cleanup requirements; and
- verify cleanup or retain an explicit cleanup limitation.

No declaration proves that a sandbox, access control, redaction, cleanup,
retention policy, dependency, or implementation is secure. Package E requires
separate implementation evidence and review. Specialist security, privacy, and
legal review remain separate and are not performed by this candidate.

## Output, evidence, and artifact separation

The following remain separate:

- input parsing;
- Schema Resource dialect checking;
- static reference closure;
- Test Manifest recognition and case construction;
- individual schema evaluation;
- expected/actual comparison;
- manifest/case inventory observation;
- Validation Execution Record phase and outcome;
- individual Cross-Record Integrity Rule and outcome;
- Integrity Evaluation Record;
- raw evaluator output;
- diagnostic, warning, limitation, adverse/restricted evidence, blocked
  condition, and non-execution;
- Validation Evidence and Reproduction Package;
- canonical Validation Output, if later separately Accepted;
- Portable Conformance Evidence;
- Evidence Bundle;
- Review Record;
- Decision Record;
- acceptance, support, certification, release evidence, and deployment
  evidence; and
- final-human authority.

No item becomes another through matching bytes, a reference, a digest,
successful parsing, schema validity, a satisfied rule, case agreement,
reproduction, publication, popularity, or repository presence.

## Separate conformance and claim dimensions

The following remain independently governed:

1. specification-source conformance;
2. Definition and Schema Resource conformance;
3. Serialization Binding conformance;
4. Test Manifest representation and construction conformance;
5. executable-schema and schema-local evaluation;
6. Validation Execution Record conformance;
7. Evidence and Reproduction Package conformance;
8. Cross-Record Integrity Rule and Evaluation Record conformance;
9. Artifact Contract and Artifact Instance conformance;
10. validator/evaluator conformance;
11. Tool conformance;
12. Implementation conformance;
13. interoperability;
14. compatibility;
15. security and privacy;
16. support;
17. certification;
18. release;
19. deployment; and
20. attributable final-human authority.

No successful execution, schema-valid result, expected-case match, satisfied
rule, evidence package, reference behavior, publication, or deployment proves
another dimension. No such event grants identity, provenance, authenticity,
acceptance, activation, applicability, authority, permission, trust, support,
certification, release approval, or deployment approval.

## No aggregate result or automatic authority

The Tool and Implementation MUST NOT produce or imply a universal aggregate
valid result, boolean pass/fail, traffic light, score, grade, badge, threshold,
rubric, checklist verdict, quality gate, ranking, recommendation, approval,
certification, release fitness, deployment fitness, or consequential authority.

Descriptive counts may summarize individually preserved observations but MUST
not replace or hide any not-satisfied, unverifiable, not-evaluated, blocked,
warning, limitation, adverse, restricted, or non-executed item.

Every applicable output authority boundary MUST set `automaticAuthority` to
exactly `false`. Missing, ambiguous, conflicting, unsupported, or non-false
authority information fails closed. Only attributable EIGENAAR / Final
Authority may make the final human decision under repository governance.

## Compatibility, interoperability, support, release, and deployment

Tool Version and Implementation Version evolve independently. A change to an
identity, supported set, capability, required input, output responsibility,
configuration meaning, dependency, runtime, deterministic ordering, failure
behavior, security/privacy boundary, or authority boundary is compatibility-
significant and requires separate governance.

Compatibility is bounded to exact compared identities, versions, interfaces,
configuration, dependencies, environments, and evidence. Interoperability
requires separately governed comparison of exact outputs and relevant behavior.
Neither creates a support commitment.

This candidate defines no release artifact, installation package, distribution
channel, signature, software bill of materials, update mechanism, compatibility
promise, support period, certification scheme, hosted service, or deployment.
Repository presence is not a release. Proposed Version `1.0.0` is not Release
Version `1.0.0` and does not alter immutable CNTX Release Version
`0.1.0-prealpha.1`.

## Versioning and lifecycle

Tool Version `1.0.0` and Implementation Version `1.0.0` are initial proposed
contract versions only. If later Accepted and integrated, each accepted version
is immutable. Correction, supersession, withdrawal, or a new compatible or
incompatible version requires a separate attributable decision that preserves
history.

The dependency-first continuation is:

1. exact-head acceptance or rejection of this Package D candidate;
2. governed integration if accepted;
3. Package E issue/task contract for code, dependency acquisition, exact
   resource limits, concrete invocation/output representation, cases,
   execution, bounded evidence, review, and attributable decision;
4. independent reproduction and reassessment where separately authorized; and
5. any later release, publication, distribution, support, certification,
   hosting, or deployment under separate authority.

This order authorizes no later phase, branch, path, code, dependency,
environment, interface, execution, evidence instance, release, or deployment.

## Consequences and limitations

Positive consequences:

- Package E can target one exact Tool and Implementation contract instead of
  inventing identity, supported scope, dependencies, ordering, or authority in
  code;
- the ten schemas, both manifest forms, 203 cases, and thirteen integrity rules
  receive one closed supported set;
- Python and `jsonschema` are pinned for one proposed implementation without
  making them normative or excluding another implementation;
- input, output, diagnostics, evidence, resources, security/privacy, and
  non-execution are explicit before code exists;
- no aggregate result can hide adverse or unevaluated detail; and
- final human authority remains outside the Tool and Implementation.

Costs and limitations:

- the detailed contract increases documentation surface;
- the proposed runtime and dependencies have not been installed or executed by
  this candidate;
- no source code, executable interface, dependency lock, build, package,
  evaluator, validator, resolver, runner, test, CI, or output instance exists;
- static documentation validation cannot prove implementability, runtime
  correctness, deterministic behavior, resource safety, security/privacy,
  evidence sufficiency, interoperability, or conformance;
- Python-specific implementation details may require later platform-specific
  limits, while the Tool contract remains implementation-independent;
- the supported set intentionally excludes future versions and Extension
  Module/Profile execution; and
- broader truth, authenticity, applicability, support, certification, release
  fitness, deployment fitness, and final-human decisions remain unproven.

## Protected predecessors and immutable history

This candidate preserves without modification:

- every baseline path outside the exact five-path allowlist, with only the two
  new paths added inside that allowlist;
- all Accepted ARCH-001 through ARCH-036 and ADR-0001 through ADR-0036
  semantics;
- CONTRACT-001 through CONTRACT-009;
- all ten Accepted Schema Resources and ten historical Test Manifests;
- exact static case inventory `203/38/165`;
- Accepted Package A, B, and C identity/version allocations and boundaries;
- all thirteen Accepted initial Rule Identities and Rule Versions;
- all Accepted validation, evidence, assessment, remediation, release,
  verification, completion, maintenance, and Extension Module/Profile sources;
- tag `v0.1.0-prealpha.1`, target
  `109e6f293b150f48572cd747fab446c141d57193`, and release-subject tree
  `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- GitHub Release `367290932` / `RE_kwDOTsnR984V5Go0`, prerelease true, draft
  false, zero custom assets, and immutable releases enabled; and
- all historical Git and GitHub objects.

## Explicit non-decisions and non-execution

This candidate changes no path under `schemas/` or `tests/`. It creates no
Artifact Type, Artifact Instance, executable schema, schema version, manifest
instance, rule instance, evaluation instance, Validation Execution Record
instance, Evidence and Reproduction Package instance, canonical Validation
Output, Portable Conformance Evidence, evaluator, validator, resolver, runner,
graph engine, code, library, SDK, CLI, API, workflow, CI, product, service,
registry, transport, storage, package, installer, release, support,
certification, hosting, or deployment.

It performs no dependency installation, schema checking, schema evaluation,
testcase execution, integrity evaluation, reproduction, evidence collection,
network retrieval, external-model interaction, code scan, specialist security/
privacy/legal review, restricted-source access, settings change, Ready-for-
review transition, merge, issue closure, branch cleanup, release, publication,
support, certification, hosting, or deployment.

Package E remains unauthorized and separately governed.

## Final-human authority and stopgate

EIGENAAR / Final Authority remains the sole final human authority. This
candidate cannot approve or accept itself. Static validation, repository
presence, a Draft PR, a matching supported set, a transparent non-independent
ARCHITECT review, or later successful execution cannot grant acceptance or
consequential authority.

ARCHITECT must stop after candidate preparation, full static validation, one
candidate commit, one push, one Draft PR, transparent non-independent COMMENT
review, and exact GitHub read-back. Any status promotion, activation,
implementation, execution, integration, merge, closure, cleanup, Package E, or
later lifecycle action requires a new exact attributable EIGENAAR / Final
Authority decision.
