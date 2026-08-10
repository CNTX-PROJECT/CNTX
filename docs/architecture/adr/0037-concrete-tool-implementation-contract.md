# ADR-0037: CNTX Concrete Validation and Integrity Tool and Implementation Contract

- **Status:** Accepted
- **Date:** 2026-08-10
- **Issue:** [#120](https://github.com/CNTX-PROJECT/CNTX/issues/120)
- **Issue-contract acceptance:** [5243736163](https://github.com/CNTX-PROJECT/CNTX/issues/120#issuecomment-5243736163)
- **Exact-head acceptance:** [5243941231](https://github.com/CNTX-PROJECT/CNTX/issues/120#issuecomment-5243941231)
- **Decision:** ARCH-037 — CNTX Concrete Validation and Integrity Tool and
  Implementation Contract

## Context

Accepted ARCH-034 defines a Validation Execution Record. Accepted ARCH-035
defines a bounded Validation Evidence and Reproduction Package. Accepted ARCH-
036 recognizes the two historical Test Manifest forms, defines thirteen
individually identified Cross-Record Integrity Rules, and defines a bounded
Integrity Evaluation Record. The repository still has no concrete Tool
Identity, Implementation Identity, executable runner, or accepted mechanism
that performs these responsibilities.

If implementation begins without a prior concrete contract, code could silently
choose its supported specifications, evaluator, dependencies, defaults, input
discovery, ordering, output meaning, resource limits, and authority behavior.
Those choices could become accidental precedent despite ARCH-033's requirement
that implementations remain non-normative.

Package D therefore needs to make one future minimal slice precise before code
exists. It must remain documentation-only and must not install dependencies,
execute schemas or tests, implement Package E, create a canonical output, or
grant acceptance, release, or deployment authority.

## Decision

Define one logical Tool identity/version pair:

- Tool Identity:
  `https://github.com/CNTX-PROJECT/CNTX/tools/minimal-validation-integrity-slice`;
- Tool Version: `1.0.0`.

Define one separate concrete Implementation identity/version pair:

- Implementation Identity:
  `https://github.com/CNTX-PROJECT/CNTX/implementations/minimal-validation-integrity-slice/python-jsonschema`;
- Implementation Version: `1.0.0`.

The identifiers are opaque identities, not network-retrieval authority.
Governed integration of this Accepted decision activates exactly these four
values and no other identity or version.

### Supported specification set

Define Tool Version `1.0.0` as supporting exactly:

- RFC 8259 through Accepted Core Artifact JSON Binding Version `1.0.0`;
- JSON Schema Draft 2020-12 and the exact vocabulary profile selected by
  Accepted ARCH-007;
- the ten exact Accepted Schema Resource identities at Version `1.0.0`;
- the ten exact historical Test Manifests in one frozen supplied repository
  revision;
- nine direct manifests and one State Snapshot operation-based manifest;
- the exact static inventory `203` cases, `38` expected-valid, and `165`
  expected-invalid;
- Validation Execution Record Definition and JSON Representation Version
  `1.0.0`;
- Validation Evidence and Reproduction Package Definition and JSON
  Representation Version `1.0.0`;
- Test Manifest, Cross-Record Integrity Rule, and Cross-Record Integrity
  Evaluation Record Definition and JSON Representation Versions `1.0.0`; and
- the thirteen Accepted Cross-Record Integrity Rule Identities, each at Rule
  Version `1.0.0`.

Any missing, additional, ambiguous, conflicting, or differently versioned
member is outside the supported set and fails closed for every dependent
operation. Future specification versions and concrete Extension Module/Profile
execution are not supported by Tool Version `1.0.0`.

### Capabilities

Define these exact bounded Tool capabilities:

- strict UTF-8 JSON input and duplicate-member rejection;
- closed caller-supplied registration of exactly ten Schema Resources;
- static offline reference-closure evaluation;
- Draft 2020-12 schema-definition checking;
- direct and operation-based Test Manifest construction;
- individual evaluation of the 203 supplied cases;
- separate expected/actual validity and diagnostic preservation;
- static manifest/case inventory derivation and comparison;
- individual evaluation of the thirteen accepted cross-record rules;
- bounded candidate construction for Validation Execution Record, Validation
  Evidence and Reproduction Package, and Cross-Record Integrity Evaluation
  Record representations;
- deterministic presentation ordering; and
- visible blocked, unsupported, restricted, unverifiable, not-evaluated,
  adverse, and non-executed conditions.

`Production` of candidate record content does not create a canonical output or
Artifact Instance. Package E must implement and evidence every capability
before it can be assessed.

### Non-capabilities

The Tool does not discover or retrieve inputs, access a network, install or
upgrade dependencies, infer active governing state, modify inputs, repair or
default data, silently downgrade capability, execute unlisted Extension
Module/Profile semantics, prove truth or evidence sufficiency, review or accept
work, produce an aggregate verdict, or release, publish, support, certify, host,
or deploy anything.

### Implementation, runtime, and dependencies

Define one Python implementation using exactly:

- CPython `3.13.14`;
- `jsonschema` `4.26.0`;
- `attrs` `26.1.0`;
- `jsonschema-specifications` `2025.9.1`;
- `referencing` `0.37.0`; and
- `rpds-py` `2026.6.3`.

These pins reuse one exact historically observed public evaluation environment
as feasibility evidence. Historical success does not prove that the future
implementation exists, conforms, reproduces, is secure, is supported, or is
accepted. This ADR installs and executes nothing.

Package E must separately govern acquisition, package integrity, lock or
manifest representation, isolated environment, build, code, exact resource
limits, execution, evidence, and cleanup. An unavailable, conflicting,
substituted, differently resolved, or unverified pin fails closed.

### Configuration

Require every future invocation to receive one complete immutable
configuration containing exact Tool and Implementation pins, supported set,
subject commit/tree, resource mapping, manifest set and forms, rule set,
supplied records, dialect/profile, format behavior, network prohibition,
duplicate/unknown-input handling, ordering, resource/security/privacy limits,
output destinations, claim scope, attributable roles, and
`automaticAuthority: false`.

There is no default configuration. Ambient environment, current directory,
adjacent files, installed packages, caches, previous results, mutable aliases,
and host defaults supply no governing meaning.

Format assertions are disabled for this implementation configuration:
`FormatChecker` is not supplied and format remains annotation-only. A later
change is compatibility-significant and separately governed.

### Environment

Require exact runtime/build, operating system, architecture, distribution,
locale, timezone, encoding, filesystem, permission, resource-limit, network,
observation-time, and provenance information for every future invocation.
Private local paths and personal data do not belong in public evidence.

An environment difference creates a different execution context. Reproduction
or interoperability claims remain bounded to exact compared contexts and
evidence.

### Logical interfaces

Define one closed logical caller-supplied input bundle containing exact
invocation, Tool, Implementation, configuration, governing-source, Schema
Resource, Test Manifest, subject-record, expected-inventory, requested-
operation, limit, output-destination, role, authority, and provenance
responsibilities.

Define separate logical output groups for invocation context, per-phase
validation records, per-schema/per-case observations, inventory observations,
per-rule integrity results, bounded evidence/reproduction content, diagnostics,
warnings, limitations, adverse/restricted evidence, blocked/non-execution,
environment provenance, and scoped claims.

Define each diagnostic with a stable implementation-local identifier, phase,
subject key, category, explanation, source/input references, expected/actual
information, related evidence/limitations, disclosure state, and provenance.

Define evidence items with unique package-local references and exact subject,
claim, phase, case, rule, output, source, context, reproduction, difference,
limitation, adverse/restricted, role, time, disclosure, retention, and cleanup
relations.

These are logical boundaries only. This ADR selects no CLI, API, SDK, process
protocol, archive, directory layout, filename, media type, transport, storage,
database, user interface, hosted service, or deployment.

### Processing and ordering

Require caller-supplied, exact, closed, frozen, bounded, offline-first,
deterministic, and fail-closed processing. Preserve dependency order from exact
context verification, strict parsing, supported-set verification, resource
registration, reference closure, schema checking, manifest construction, case
evaluation, inventory comparison, individual rule evaluation, bounded record
construction, integrity checking, and provenance finalization.

Use deterministic presentation ordering by exact schema identity/version,
manifest key, supplied case order plus exact case key, rule identity/version,
subject-key tuple, diagnostic key, limitation/warning key, and evidence/claim
reference. Ordering creates no priority, precedence, severity, conflict
resolution, or authority.

Prohibit automatic discovery, retrieval, redirects, network authority, hidden
cache, ambient state, mutable aliases, `latest`, newest-wins, substitution,
coercion, normalization, defaulting, repair, retry, fallback, silent capability
downgrade, and order-, popularity-, majority-, consensus-, score-, or ranking-
based meaning.

### Fail-closed outcomes

Keep governing-input mismatch, missing/additional/duplicate/malformed input,
identity/version/revision/content/digest/provenance conflict, ambiguity,
unknown requirement, unsupported capability, schema-definition failure,
reference-closure failure, case-construction failure, assertion failure,
integrity failure, processing failure, warning, limitation, resource blockage,
security/privacy conflict, restricted evidence, unverifiable, not-evaluated,
blocked phase, non-execution, and adverse evidence separately visible.

A processing failure is not an assertion failure. An unsupported capability is
not a negative assertion. A warning is not proof. Restricted evidence is not
absent evidence. Non-execution is not success.

### Resources, security, privacy, and cleanup

Require caller-supplied finite limits for input/output sizes and counts, JSON
depth/nodes, graph nodes/edges/depth/breadth, reference expansion, recursion,
composition, repeated evaluation, regex/general evaluation cost, memory, CPU,
wall time, concurrency, processes/threads, file descriptors, temporary storage,
logging, diagnostics, output, and retained evidence.

Treat every input and derived output as untrusted. Require least privilege,
network prohibition during execution, no executable-content evaluation, safe
path handling, bounded writes, minimization, redaction, restricted-evidence
references, disclosure controls, retention, cleanup, and visible limitations.

This ADR chooses no numeric threshold, sandbox, container, operating system,
process model, access-control implementation, log format, cleanup mechanism,
retention policy, transport, or storage. Package E must propose and evidence
concrete safe mechanisms before execution.

### Output, evidence, conformance, and authority separation

Keep parsing, resource closure, schema checking, manifest construction, case
evaluation, inventory observation, validation phases, individual integrity
rules, raw output, diagnostics, evidence packages, canonical Validation Output,
Portable Conformance Evidence, Evidence Bundle, Review Record, Decision Record,
acceptance, certification, release/deployment evidence, and final-human
authority separate.

Keep specification, Definition/Schema Resource, Binding, manifest, schema-
local, validation-record, evidence-package, integrity-rule, Artifact, evaluator,
Tool, Implementation, interoperability, compatibility, security/privacy,
support, certification, release, deployment, and final-human-authority
conformance separate.

Prohibit a universal aggregate result, boolean pass/fail, traffic light, score,
grade, badge, threshold, rubric, checklist verdict, quality gate, ranking,
recommendation, approval, certification, release fitness, deployment fitness,
or consequential authority. Descriptive counts cannot replace adverse or
unevaluated individual results.

Require `automaticAuthority` to be exactly `false`. Missing, ambiguous,
conflicting, unsupported, or non-false authority information fails closed.

## Consequences

Positive consequences:

- Package E can implement against exact identities, scope, capabilities,
  dependencies, interfaces, ordering, limits, and authority boundaries;
- the ten schemas, both manifest forms, 203 cases, and thirteen rules form one
  closed supported slice;
- Python-specific choices stay in one Implementation rather than
  becoming normative Tool or specification meaning;
- adverse, restricted, blocked, unverifiable, not-evaluated, and non-executed
  conditions stay visible; and
- no Tool or Implementation can grant final human authority.

Costs and limitations:

- the contract adds substantial documentation before code;
- no dependency, environment, implementation, executable interface, test,
  execution, record instance, or canonical output exists;
- static validation cannot prove implementability, runtime correctness,
  determinism, safety, evidence sufficiency, interoperability, or conformance;
- the supported set intentionally excludes future versions and Extension
  Module/Profile execution; and
- truth, authenticity, acceptance, support, certification, release fitness,
  deployment fitness, and final decisions remain unproven.

## Alternatives not selected

### Let Package E choose identities and behavior in code

Not selected because implementation choices could become accidental normative
precedent and make review of scope, dependencies, outputs, and authority too
late.

### Keep the Tool abstract and leave the first Implementation unpinned

Not selected because reproducibility requires one exact implementation,
runtime, and dependency target before code and execution are authorized.

### Select both historical Python and Ajv evaluators

Not selected for the first minimal slice. Two implementations would double the
Package E implementation surface. Historical Ajv evidence remains preserved
and may later support an independently governed interoperability or
reproduction candidate.

### Define a CLI or API now

Not selected because Package D may define logical interface boundaries but is
not authorized to create code, a CLI, an API, an SDK, a transport, or a hosted
service.

### Produce one green/red result

Not selected because an aggregate result hides individual failures,
limitations, restricted evidence, unverifiable conditions, and non-execution
and could be mistaken for acceptance or authority.

### Enable network schema resolution

Not selected because it conflicts with the Accepted closed, caller-supplied,
offline-first, deterministic, identity-preserving, and fail-closed boundaries.

## Non-decisions and non-execution

This ADR changes no Accepted source, schema, manifest, testcase, expected-
validity value, release object, or historical Git/GitHub object. It creates no
Artifact Type, Artifact Instance, executable schema, manifest/rule/evaluation
instance, evaluator, validator, resolver, runner, graph engine, code, library,
SDK, CLI, API, workflow, CI, product, service, registry, package, release,
support, certification, hosting, or deployment.

It installs and executes nothing. It performs no schema/test/integrity
evaluation, reproduction, evidence collection, network access, external-model
interaction, code scan, specialist security/privacy/legal review, restricted-
source access, settings change, Ready transition, merge, issue closure, branch
cleanup, release, publication, support, certification, hosting, or deployment.

Package E remains unauthorized and separately governed.

## Authority boundary

This ADR is Accepted under issue #120, attributable EIGENAAR / Final Authority
issue-contract acceptance comment `5243736163`, and exact-head acceptance
comment `5243941231` for reviewed candidate commit
`d047b754efe17b66505443fad1d5891254db15e8` and tree
`460d0f3ae014339507bdeecbc86db544a1836331`. Repository presence, static
validation, and transparent non-independent ARCHITECT COMMENT review
`4899510683` did not grant that acceptance.

Governed integration activates only the exact Tool and Implementation
identity/version pairs, supported set, capabilities, pins, interfaces, and
boundaries defined here. Acceptance and integration do not create code,
execution, evidence instances, release, support, deployment, or Package E
authority.
