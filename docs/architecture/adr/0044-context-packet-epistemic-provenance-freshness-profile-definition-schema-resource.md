# ADR-0044: CNTX Context Packet Epistemic Provenance and Freshness Profile Definition Schema Resource

- **Status:** Accepted
- **Date:** 2026-08-13
- **Issue:** [#149](https://github.com/CNTX-PROJECT/CNTX/issues/149)
- **Issue-contract acceptance comment:** [5279967413](https://github.com/CNTX-PROJECT/CNTX/issues/149#issuecomment-5279967413)
- **Source-preserving correction addendum:** [5280408320](https://github.com/CNTX-PROJECT/CNTX/issues/149#issuecomment-5280408320)
- **Second source-preserving correction addendum:** [5280832992](https://github.com/CNTX-PROJECT/CNTX/issues/149#issuecomment-5280832992)
- **Exact-head acceptance comment:** [5285702199](https://github.com/CNTX-PROJECT/CNTX/issues/149#issuecomment-5285702199)
- **Baseline:** commit `eec00d698512533c3d40f985fe5d588cd03438f1`, tree `87a2d5aaf01e3f7c45b4fb4e3d8aa40a21dc046a`
- **Accepted candidate:** commit `7420e5d179ab965bfda58780df4f41a08a0b62de`, tree `56d1808cb95f3dd5a0b5d84f2a8e440891dff5e6`
- **Integration-authority comment:** [5286010813](https://github.com/CNTX-PROJECT/CNTX/issues/149#issuecomment-5286010813)
- **Integrated pull request:** [#150](https://github.com/CNTX-PROJECT/CNTX/pull/150)
- **Integrated `main`:** commit `1d9e4667d68cce6e0289464c821bcd95e1d355ae`, tree `3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`
- **Completion comment:** [5286062635](https://github.com/CNTX-PROJECT/CNTX/issues/149#issuecomment-5286062635)
- **Decision:** Accepted ARCH-044 — CNTX Context Packet Epistemic Provenance and Freshness Profile Definition Schema Resource

## Context

Accepted ARCH-039 defines one narrowing-only Profile Definition with exact
Identifier/Version `1.0.0` and exactly two Profile Subjects. Accepted and
integrated ARCH-043 defines one external closed fourteen-member application
record for applying that Profile to one exact Context Packet revision under one
exact approved Task Contract revision.

ARCH-031 and ARCH-032 require every concrete Profile Definition Schema
Identifier, Schema Version, resource, assertion, case inventory, execution,
Tool capability, acceptance, and integration to remain separately governed.
Issue-contract acceptance comment `5279967413`, supplemented by attributable
source-preserving correction addenda `5280408320` and `5280832992`, authorizes
one bounded Proposed candidate only. The first addendum corrects only the
baseline link inventory to `1489 Markdown / 27 HTML` and `1297 local / 219
external`. The second corrects only the evaluation-responsibility count from
sixteen to seventeen while preserving the exact seventeen Accepted ARCH-043
members. Neither changes any semantic or lifecycle term or accepts or activates
this decision or schema. Attributable exact-head candidate acceptance comment
`5285702199` accepts only commit/tree
`7420e5d179ab965bfda58780df4f41a08a0b62de` /
`56d1808cb95f3dd5a0b5d84f2a8e440891dff5e6`. The preceding Proposed status
allocated or activated nothing; the status-only promotion recorded the Accepted
decision while governed integration remained separate. Later integration-
authority comment `5286010813` authorized PR #150, which integrated the
unchanged decision at public `main` commit/tree
`1d9e4667d68cce6e0289464c821bcd95e1d355ae` /
`3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`. Completion comment `5286062635`
records issue #149 closed/completed and the task branch absent locally and
publicly.

## Accepted decision

Accept one child of the `CNTX Profile Definition Schema Family`:

- Definition Schema Identifier
  `https://github.com/CNTX-PROJECT/CNTX/schemas/profiles/context-packet-epistemic-provenance-freshness`;
- initial Schema Version `1.0.0`;
- canonical `$id`
  `https://github.com/CNTX-PROJECT/CNTX/schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0`;
- JSON Schema Draft 2020-12;
- media type `application/schema+json`;
- canonical repository path
  `schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0/schema.json`;
  and
- one operation-based synthetic manifest at
  `tests/schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0/cases.json`.

The Definition Schema Identifier is version independent. Schema Version and
Profile Definition Version remain separate even where both equal `1.0.0`.
The preceding Proposed issue, candidate, path, `$id`, parseability, case result,
review, and repository presence allocated or activated neither coordinate.
Accepted status without governed integration likewise does not integrate,
allocate, or activate either coordinate.

### Standalone zero-external-reference resource

The candidate is one standalone Draft 2020-12 root resource with exactly 52
root `$defs`, exactly 207 static fragment-only internal `$ref` values reaching
all 52 definitions, and exactly zero external `$ref` edges. Its exact separate
reference inventory is `207 total / 207 internal / 0 external`; the existing
`1142/1133/9` inventory remains unchanged. It has no nested `$id`, public
anchor, dynamic reference, custom vocabulary, Format-Assertion requirement,
Hyper-Schema, remote resolution, default, coercion, fallback, aggregate result,
executable action, or authority-bearing annotation.

Zero external references is deliberate. The ARCH-043 record contains only
exact pins and opaque references to its Context Packet, Task Contract, Module
declarations, sources, policies, evidence, and authority. It does not embed
those complete records. Referencing their roots would evaluate the wrong
instance shape; referencing another resource's internal `$defs` would couple
this Profile to non-public resource internals. The one-node resource graph is
finite and acyclic by construction and adds no Definition dependency.

### Closed structural target

The resource evaluates one closed ARCH-043 record with exactly these fourteen
required root members:

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

All root and subordinate objects are closed. Required identifiers, revisions,
references, statements, roles, and explanations are non-blank. JSON `null`,
unknown members/tokens, extension bags, defaults, repair, normalization,
coercion, and fallback are invalid where an exact value or condition is
required.

The candidate structurally preserves:

- exact Profile Definition Identifier/Version/category/source revision;
- exact Context Packet and Module Definition subject pins;
- stable application identity/revision, `external-profile-application`,
  bounded supersession, scope, prohibited uses, and non-aggregation;
- exact target Context Packet and approved governing Task Contract artifact,
  contract, schema, source-revision, and approval pins;
- one closed association for every represented source, with packet-local index,
  repeated source reference, claim roles, six source-category tokens,
  materiality, one reference-only Module declaration pin, applicability,
  provenance, temporal, policy, integrity, derivation, condition, limitation,
  and authority references;
- narrowing declarations using only the seventeen Accepted dimensions;
- exact frozen governing-context, supply, prerequisite, conflict,
  non-execution, and activation references;
- the eight separate information-condition tokens and four separate evaluation
  outcomes;
- all eleven limitation categories, including separate minimality and source-
  coverage responsibilities;
- non-empty declaring, selecting, supplying, applying, evaluating, reviewing,
  governing, and final-human-authority role collections; and
- the prohibition on aggregate or serialized `automaticAuthority` members.

### Finite narrowing

General strings are non-blank and at most 2,048 characters. Identifiers,
revisions, tokens, role labels, and opaque references use a 512-character
maximum where applicable. General collections contain at most 64 items; role
collections contain one through 32 items; supersession, derivation-input, and
transformation collections contain at most 32 items.

`sourceAssociations` contains one through 64 items, with integer packet-local
indices `0` through `63`. `selectedCapabilities` contains one through 64 items.
Conditions and evaluations each contain at most 128 items. Source-category
sets contain one through six items. Duplicate-free collections use
`uniqueItems: true`, which proves only complete JSON-value equality.

A target Context Packet with more than 64 selected sources cannot receive a
valid application under this candidate. No truncation, split, sampling,
omission, fallback, or repair is allowed. Finite structure proves no runtime
resource or denial-of-service safety.

### Schema-local boundary

Standard JSON Schema can evaluate the local structure above. It cannot prove:

- existence, validity, acceptance, authenticity, approval, or availability of
  referenced records or sources;
- equality between the governing Task Contract pin and the external target
  Context Packet's pin;
- complete exactly-once association of the external packet's selected sources,
  external index range, or repeated-source-reference equality;
- projected-key uniqueness when otherwise different objects are supplied;
- resolution or completeness of opaque reference strings;
- external graph completeness or acyclicity;
- narrowing-only semantic meaning;
- source truth, provenance truth, digest correctness, freshness, applicability,
  policy applicability, evidence sufficiency, privacy, access, approval, or
  final-human authority;
- Core validity, Profile conformance, implementation support,
  interoperability, release fitness, or deployment fitness; or
- runtime bounds merely from finite structure.

No custom keyword, hidden semantic validator, network lookup, or private rule
is introduced to conceal these limitations.

## Fixed synthetic cases

The non-normative operation-based manifest fixes one complete `baseInstance`
and exactly 72 named cases before any evaluator execution:

- 11 expected valid; and
- 61 expected invalid.

Each case contains one stable name, one boolean expected-validity value, and an
ordered operation list. Materialization deep-copies the base instance and
applies only closed RFC 6901 `add`, `remove`, or `replace` operations in listed
order. Those operations are deterministic test mechanics only, not a Profile
representation, patch protocol, migration, Serialization Binding, runtime, or
implementation contract.

The valid cases exercise the minimal record, empty conditions/evaluations with
explicit non-execution, repeated references at distinct indices, all six
source categories, all seventeen dimensions, all eight conditions, all four
outcomes, finite derivation, exact policy/digest references, public-safe
adverse/restricted information, and bounded supersession/supply/activation/
authority context.

The invalid cases exercise every material schema-local assertion family:
closed and required roots, exact governing and subject pins, application,
target and task pins, limits and types, source associations, categories,
Module-reference-only structure, capabilities, governing context, supply,
activation, conditions, evaluations, limitations, authority, duplicates, and
the prohibited serialized `automaticAuthority` property.

Historical Core cases remain separately `203/38/165`; ARCH-042 remains
separately `48/8/40`. Manifest construction changes only from
`10 direct / 1 operation-based` to `10 direct / 2 operation-based`. Neither the
new `72/11/61` inventory nor a descriptive `323/57/266` sum is a score,
threshold, conformance verdict, certification, release gate, deployment gate,
or authority.

## Candidate execution boundary

The schema, base instance, operations, and expected results were frozen in one
immutable candidate commit before the one isolated evaluation permitted by
issue #149. The authorized local, non-governing, non-independent run remains
bound only to accepted candidate commit/tree
`7420e5d179ab965bfda58780df4f41a08a0b62de` /
`56d1808cb95f3dd5a0b5d84f2a8e440891dff5e6`: all `72/72` expectations matched
with zero mismatches. Status promotion and integration were not new executions
or evidence instances.

The permitted later evaluation is bounded to one non-independent native-
Windows environment, exact 64-bit CPython `3.13.14`, the five exact dependency
wheels pinned by the corrective `1.0.1` lock, pre-install filename/size/SHA-256
verification, isolated offline hash-required installation, meta-schema
checking, deterministic materialization, exactly one evaluation per case,
separate result comparison, repository-integrity checks, and guarded cleanup.
Any failure stops without retry or favorable claim.

The temporary harness and dependencies add nothing to the public repository.
The existing Tool's exact ten-schema supported set, 29 unittest methods,
thirteen rules, dependencies, practice scenarios, outputs, and evidence remain
unchanged and are not re-executed for this candidate.

## Consequences

Positive consequences:

- the exact ARCH-043 representation becomes structurally reviewable by one
  bounded schema candidate;
- Profile, subject, target, task, source, Module, supply, activation, condition,
  evaluation, limitation, and authority responsibilities remain separate;
- unknown structure, invalid tokens, omitted responsibilities, null repair,
  excessive bounds, and serialized automatic authority fail closed;
- zero external references preserve the exact pin/reference-only model; and
- synthetic expectations are fixed before any candidate execution.

Costs and limitations:

- the closed schema and complete base instance are intentionally large;
- the 64-source maximum is an explicit narrowing and excludes larger packets;
- whole-value uniqueness is weaker than projected-key uniqueness;
- cross-record, graph, source-truth, policy, access, conformance, and authority
  semantics remain outside standard JSON Schema;
- the successful candidate validation is limited to one Windows host, one
  exact runtime and dependency set, one schema, and 72 synthetic cases; it is
  not portability, performance, production, hard-resource, OS-isolation, or
  complete adversarial evidence; and
- the preceding Proposed status allocated and activated nothing, while
  Accepted status without integration likewise activates nothing.

## Alternatives not selected

### Modify Context Packet or Task Contract Schema Version 1.0.0

Rejected because Core resources are immutable and the Profile application is a
separate external narrowing-only record.

### Reference the complete Context Packet, Task Contract, or Module schemas

Rejected because ARCH-043 contains pins and references rather than the complete
external instances. A root reference would evaluate the wrong shape.

### Reference another resource's internal `$defs`

Rejected because internal definitions carry no public independent contract and
would couple this Profile to another resource's internal organization.

### Embed the ARCH-040 Module declaration

Rejected because ARCH-043 requires one exact declaration pin and prohibits a
duplicate or alternative thirteen-member Module representation.

### Add semantic custom keywords or a cross-record validator

Rejected because that would create a custom dialect, hidden implementation,
rule, capability, and evidence boundary outside this schema task.

### Remove finite limits to accept every possible packet

Rejected because issue #149 requires explicit bounded structure. Packets beyond
the selected 64-source bound fail visibly rather than being silently truncated.

### Use 72 complete repeated instances

Rejected because one complete base instance plus closed ordered operations is a
smaller deterministic test construction. It creates no runtime patch contract.

### Report one aggregate case result

Rejected because every case and outcome remains separate and technical output
cannot create approval, certification, release fitness, deployment fitness, or
authority.

## Protected history and non-decisions

The decision changes no Accepted Core schema/test, Artifact Contract,
Definition or Representation meaning, existing Schema Identity/Version,
ARCH-042 schema/cases, Serialization Binding, Tool/Implementation, dependency,
lock, rule, workflow, CI, setting, tag, Release, evidence instance, H2.4 state,
or historical authority record.

The allowlisted current-state corrections only record completed ARCH-043 and
ARCH-042 integrations while preserving all original Proposed, candidate,
execution, evidence, acceptance, promotion, integration, completion, and
cleanup provenance.

The decision creates no Profile instance, Core property, policy instance,
rule, cross-record validator, diagnostic vocabulary, Tool/Implementation
version, supported-set expansion, public runner, workflow, CI, release,
publication beyond the governed issue/candidate/PR records, support,
certification, hosting, deployment, merge, closure, cleanup, Phase 4A3.5, or
later-phase authority.

## Authority and stop boundary

Issue #149, attributable issue-contract acceptance comment `5279967413`, the
link-pin-only source-preserving correction addendum `5280408320`, and the
evaluation-count-only correction addendum `5280832992` authorized candidate
preparation only. Attributable exact-head candidate acceptance comment
`5285702199` plus this status-only promotion establish Accepted status for the
unchanged candidate. They did not by themselves integrate, allocate, or activate
the Definition Schema Identifier, Schema Version, canonical `$id`, or resource.
Separately attributable comment `5286010813` authorized PR #150 integration of
that exact Accepted candidate; completion comment `5286062635` records issue
#149 closed/completed and branch cleanup after public `main` commit/tree
`1d9e4667d68cce6e0289464c821bcd95e1d355ae` /
`3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`.

Candidate preparation, parsing, meta-schema checking, case materialization,
fixed expectations, static validation, the candidate-bound local validation,
Draft PR state, transparent non-independent `COMMENTED` review, rendering,
repository presence, and mergeability grant no integration, activation,
release, deployment, or authority. The status-only promotion is not a new
execution or evidence instance.

Integration and completion preserved all accepted schema/case bytes, original
lifecycle and execution/evidence pins, all 12 Schema Resources, and the separate
Core `203/38/165`, Module `48/8/40`, and Profile `72/11/61` inventories. They
created no Tool support, new execution/evidence instance, Profile instance,
aggregate result, release, deployment, H2.4 completion, Phase 4A3.5, or later-
phase authority.
