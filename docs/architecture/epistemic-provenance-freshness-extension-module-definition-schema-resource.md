# CNTX Epistemic Provenance and Freshness Extension Module Definition Schema Resource (ARCH-042)

## In ordinary language

ARCH-038 defines what source provenance and freshness mean. ARCH-040 defines
the closed JSON-compatible declaration shape. This Accepted decision translates
only that accepted shape into one machine-evaluable JSON Schema and fixes 48
synthetic structural examples whose expectations preceded evaluation.

| Quick view | Meaning |
| --- | --- |
| **Status** | Accepted and integrated Definition Schema Resource `1.0.0` |
| **Subject** | One ARCH-040 declaration governed by ARCH-038 Definition `1.0.0` |
| **Machine result** | Structural valid or invalid for one exact schema and instance |
| **Not established** | Source truth, authenticity, integrity, freshness, applicability, conformance, approval, support, release, deployment, or automatic authority |

## Status and authority

**Document Status:** Accepted.

This decision is governed by [issue #145](https://github.com/CNTX-PROJECT/CNTX/issues/145).
Attributable EIGENAAR / Final Authority acceptance of the exact issue contract
is recorded in issue comment
[5267576754](https://github.com/CNTX-PROJECT/CNTX/issues/145#issuecomment-5267576754).
Attributable exact-head candidate acceptance is recorded in issue comment
[5269689952](https://github.com/CNTX-PROJECT/CNTX/issues/145#issuecomment-5269689952),
bound to candidate commit
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` and tree
`071a9909efcee1d4d74d7ff65b0b05da30e73875`.

Issue-contract acceptance authorized only the bounded Proposed candidate
lifecycle. That preceding Proposed status allocated or activated nothing.
Exact-head acceptance established Accepted status. Separately authorized
governed integration is recorded in issue comment
[5271035681](https://github.com/CNTX-PROJECT/CNTX/issues/145#issuecomment-5271035681),
and completion is recorded in issue comment
[5271254252](https://github.com/CNTX-PROJECT/CNTX/issues/145#issuecomment-5271254252).
PR [#146](https://github.com/CNTX-PROJECT/CNTX/pull/146) integrated the exact
Accepted tree into `main` at commit
`9f482043f76c792f6c2e1e96eb4a535ee26b3a99` and tree
`7b2f45791e3b7bff7e856f26fff9b22598c06709`; issue #145 is closed/completed,
and the task branch is absent locally and publicly.

Exact-head acceptance plus that governed integration allocates and activates
only the exact Definition Schema Identifier
`https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness`,
Schema Version `1.0.0`, and canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness/1.0.0`
as the integrated Accepted Schema Resource. Status promotion, branch or
repository presence, schema or JSON parsing, schema checking, case evaluation,
static validation, Ready state, review, or mergeability does not by itself
integrate, allocate, or activate the resource or establish conformance,
semantic truth, provenance truth, freshness, approval, certification, support,
release fitness, deployment fitness, or authority. Integration created no new
execution or evidence instance and did not expand Tool support.

## Exact decision basis

The accepted candidate was prepared directly from public baseline commit
`c7650274a2818a5c3eaca0abfb0bc86fd747e4b2` and tree
`f7dd74615c11e5390c0680f862668f425285e7f7`.

The controlling semantic sources are:

- Accepted ARCH-038 and ADR-0038 for the Epistemic Provenance and Freshness
  Extension Module Definition;
- Accepted ARCH-040 and ADR-0040 for its closed JSON-compatible
  representation;
- Accepted ARCH-028 through ARCH-033 for Extension Module/Profile sovereignty,
  identities, resources, schema evaluation, and Tool/Implementation limits;
- Accepted ARCH-023 and ARCH-024 for offline-first resource resolution and
  separate validation outcomes; and
- all existing Core architecture, contracts, schemas, tests, rules,
  Tool/Implementation sources, evidence, release boundaries, and final-human
  authority.

The schema may enforce only structure justified by those exact sources. It
cannot repair, reinterpret, broaden, narrow, or complete them silently.

## Accepted Definition Schema identity and version

| Dimension | Exact Accepted value |
| --- | --- |
| Schema family | `CNTX Extension Module Definition Schema Family` |
| Definition Schema Identifier | `https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness` |
| Initial Schema Version | `1.0.0` |
| Canonical version-qualified `$id` | `https://github.com/CNTX-PROJECT/CNTX/schemas/extension-modules/epistemic-provenance-freshness/1.0.0` |
| Governing Definition Identifier | `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness` |
| Governing Definition Version | `1.0.0` |
| Schema language and dialect | JSON Schema Draft 2020-12 |
| Media type | `application/schema+json` |
| Canonical repository path | `schemas/extension-modules/epistemic-provenance-freshness/1.0.0/schema.json` |
| Document Status | Accepted and integrated |

The Definition Schema Identifier is version independent. Schema Version is a
separate semantic-version coordinate. The version-qualified `$id` identifies
the one standalone resource. Its HTTPS shape grants no retrieval, redirects,
network access, registry or catalog lookup, availability, trust, acceptance,
support, publication, or authority.

Definition Version `1.0.0` and Schema Version `1.0.0` are independent. Their
equal values create no lockstep lifecycle. The preceding Proposed issue, path,
file, `$id`, candidate, review, and validation presence allocated or activated
nothing. Accepted status alone did not integrate, allocate, or activate the
resource; the completed separately governed integration above did so only for
the exact Schema Identifier, Version, and canonical `$id`.

## One standalone resource

The Accepted decision consists of one canonical standalone root JSON Schema
Resource:

- exact root `$schema` and canonical `$id`;
- internal reusable definitions only below root `$defs`;
- static fragment-only internal `$ref` values;
- no external `$ref`, because the Definition declares no schema dependency;
- no nested `$id`, public `$anchor`, `$dynamicRef`, `$dynamicAnchor`, custom
  dialect, custom vocabulary, Hyper-Schema, or remote resource;
- closed objects and finite string, array, and nesting bounds; and
- no defaults, coercion, repair, inference, fallback, aggregate outcome, or
  executable action.

The resource evaluates one declaration record. It is not a Core Artifact, CNTX
Artifact Instance, Extension Module instance, Definition instance, Governing
Definition Declaration, Definition Package, Profile, Context Packet
attachment, policy, evidence record, validation output, review, decision,
approval, release, or deployment record.

## Closed thirteen-property root

Every evaluated instance is one closed object with all and only:

1. `governingDefinition`;
2. `declaration`;
3. `source`;
4. `claims`;
5. `provenance`;
6. `temporal`;
7. `integrity`;
8. `policies`;
9. `derivation`;
10. `conditions`;
11. `evaluations`;
12. `limitations`; and
13. `authority`.

Root presence prevents omission from being mistaken for Assessed None or Not
Assessed. It does not make missing, restricted, conflicting, or unverifiable
information favorable.

## Exact structural translation

The schema structurally requires:

- exact governing Definition Identifier and Version constants plus a non-blank
  authoritative source-revision pin;
- non-blank declaration identity/revision, one producing role, explicit
  governing context, and bounded supersession pins;
- exactly the six ARCH-040 source-category tokens as a unique closed set;
- separate source identity, revision, locations, availability, roles, and
  material subject boundary;
- bounded claims using only the seventeen ARCH-040 epistemic dimensions;
- separate origin, custody, acquisition, observation, supply, transformation,
  and responsible-role provenance;
- exactly four condition-wrapped temporal coordinates;
- bounded digest claims with separate opaque algorithm identity, value,
  subject boundary, source/acquisition context, procedure, observation-time
  reference, role, condition, result reference, evidence, failures, and
  limitations;
- separate freshness and applicability policy declarations;
- a finite specified derivation value exactly when `derived-source` is
  supplied, and a non-specified derivation condition otherwise;
- exactly eight information-condition tokens;
- exactly four ARCH-024 evaluation outcomes;
- all nine limitation responsibilities; and
- attributable declaring, supplying, evaluating, reviewing, governing, and
  final-human-authority roles.

Objects remain closed. Strings are non-blank and bounded. Arrays are bounded;
sets use `uniqueItems` where exact whole-value equality is meaningful. No
object or array order creates authority or precedence.

## Common condition wrapper

Every condition-bearing dimension uses one closed wrapper with:

- `condition`;
- dimension-specific `value` only for `specified`;
- bounded `explanation`;
- zero or more unique opaque `evidenceRefs`; and
- one or more attributable `responsibleRoles`.

The exact condition tokens are `specified`, `assessed-none`, `not-assessed`,
`missing`, `inaccessible`, `conflicting`, `restricted`, and `unverifiable`.

For `specified`, `value` is required. For every other condition, `value` is
prohibited. Restricted content is never inserted merely to satisfy the schema.
Assessed None is not Missing; Not Assessed is not Assessed None; Inaccessible
is not absence; Restricted is not proof; and Unverifiable is not Not
Satisfied.

Unknown properties or tokens, omitted required properties, empty strings, and
JSON `null` substitutions are invalid. No unknown value is mapped to a known
token or accepted through fallback.

## Temporal lexical boundary

A specified temporal coordinate uses one bounded RFC 3339-compatible lexical
shape containing an explicit `Z` or numeric offset. `format: date-time` remains
an annotation under the selected vocabulary profile; the schema also uses an
explicit pattern so validity does not depend on optional Format-Assertion
behavior alone.

The coordinate separately preserves clock/reference pin, offset, precision,
uncertainty, source pin, and responsible role. The schema cannot prove
calendar-source authenticity, clock correctness, synchronization, actual
observation, value/offset consistency, policy applicability, freshness, or
currentness. The lexical pattern intentionally does not claim full calendar
semantics beyond its bounded structural profile.

## Digest and policy boundary

Digest `algorithm` is a required non-blank opaque identity. There is no default
and no algorithm enum. The schema therefore does not select SHA-256 or another
method, encoding, canonicalization, signature, certificate, attestation,
trust store, or verification implementation. Digest structure proves no match,
integrity, authenticity, semantic equivalence, trust, safety, or authority.

Freshness and applicability policies remain separate. A specified policy
carries exact supplied identifier/version, authoritative source pin,
task/source-class conditions, temporal inputs, assessment reference,
clock/reference pin, condition boundary, roles, evidence, limitations, adverse
and restricted information, and evaluation reference. The schema creates no
policy identity, vocabulary, threshold, duration, tolerance, grace period,
comparison rule, default, ambient selection, or latest-wins behavior.

## Conditions, evaluations, limitations, and authority

Condition declarations remain dimension- and subject-specific. Evaluations
reuse only `satisfied`, `not-satisfied`, `unverifiable`, and `not-evaluated`.
Every evaluation remains separate and retains governing inputs, roles,
evidence, times, diagnostics, failures, limitations, adverse/restricted
information, and non-execution or blocked prerequisites.

There is no aggregate outcome property, score, weighting, count-based result,
majority, ranking, traffic light, grade, badge, threshold, quality gate,
recommendation, approval, certification, release fitness, deployment fitness,
or consequential authority.

All nine limitation categories remain structurally present. Restricted
metadata is public-safe orientation only and never replaces protected
evidence. Role references are opaque attribution boundaries, not persons,
accounts, credentials, authentication, authorization, signatures, delegation,
votes, approvals, or identity-verification proof.

`automaticAuthority: false` remains a governing semantic invariant and is not
a serialized property. Because the authority object is closed, an
`automaticAuthority` member is invalid. Schema validity never becomes final
human authority.

## Synthetic cases fixed before execution

The non-normative direct manifest contains exactly 48 complete public-safe
instances with expected validity fixed in the candidate commit:

- 8 expected valid; and
- 40 expected invalid.

The valid cases cover a minimal non-derived declaration, governing source,
model recollection, finite derivation, restricted metadata, conflicting input,
digest declaration, and temporal/policy declaration. The invalid cases cover
root closure and requiredness, exact pins, blank/null/type failures, token
closure and uniqueness, finite resource bounds, wrapper rules, date-time
lexical structure, digest and policy completeness, derivation/category
coupling, condition/outcome closure, limitation/authority presence, and the
prohibited serialized `automaticAuthority` property.

Every case remains separate. The counts are descriptive inventory, not a score,
threshold, pass rate, conformance claim, badge, certification, release gate,
deployment gate, or authority.

The historical ten manifests remain byte-for-byte unchanged at
`203/38/165` and historical forms `9 direct / 1 operation-based`. The new
manifest is one additional direct form. No combined aggregate result is
created.

## Evaluation and Tool boundary

Expected results were frozen before any evaluator run. The separately bounded
candidate validation evaluated all 48 cases once in one isolated temporary
Windows environment using exact CPython `3.13.14` and only the five exact
artifacts pinned by the integrated corrective lock. Artifact filename, size,
and digest were verified before installation; resolution and evaluation used
no network access. All 48 expected/actual results matched and cleanup
completed. That accepted execution evidence is bound exclusively to candidate
commit/tree
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875`; the status-only promotion is not
a new execution or evidence instance. Its execution-evidence SHA-256 remains
`2ec1f7552ee7830d9fa8fccfd4dd0e0d1089ea77f7566a4da4f255cc298ee938`
and its evaluator-result SHA-256 remains
`df9e2af0a2b6cf14830619dd496895bb851ba2e5968417e972bfea739c6db975`.

This validation does not add a public harness, dependency, lock, Python file,
runner, invocation, output, or evidence instance. It does not expand the
existing minimal Tool/Implementation's exact ten-schema supported set, 29
tests, thirteen rules, or historical/corrective practice scenarios.

The execution was governed by the unchanged rule that any acquisition,
verification, installation, meta-schema, evaluation, comparison, isolation, or
cleanup failure stops fail closed without retry or favorable claim. The same
rule remains required for any future separately authorized execution.

## Standard JSON Schema limitations

The resource can evaluate bounded structure. It cannot prove:

- an external reference exists or resolves;
- a source, policy, clock, role, evidence item, or revision is authentic;
- a proposition is true, complete, current, applicable, safe, or trusted;
- time values and separate offset/reference statements are mutually correct;
- a supplied policy governs the task;
- an external derivation graph is acyclic;
- projected identifiers are globally unique;
- every opaque local reference has a target; or
- a result constitutes Definition conformance or any human decision.

No custom keyword or hidden semantic validator is introduced to conceal these
limits.

## Core sovereignty and protected history

This candidate changes no Common Artifact Envelope, Core Artifact schema,
Context Packet, Artifact Contract, Core JSON binding, existing Schema
Resource, historical test manifest, practice input, Tool/Implementation,
dependency, lock, rule, workflow, CI, setting, tag, Release, evidence instance,
or historical authority record.

Core-invalid data cannot become Core-valid through this separate resource. The
then-future narrowing-only Profile representation and Profile Schema Resource
were later Accepted and governed-integrated under their own separate authority
through ARCH-043 and ARCH-044. That later lifecycle changes no ARCH-042 schema,
case, identifier, assertion, execution, evidence, or semantic boundary.

H2.4 [issue #138](https://github.com/CNTX-PROJECT/CNTX/issues/138) was later
closed as `not planned` without an independent visitor review. That visitor
criterion remains `Not Evaluated`; closure does not establish H2.4 completion,
approval, certification, or current-`main` quality evidence.

## Security and privacy

All identifiers, references, strings, times, digest values, roles, policies,
limitations, and instances are untrusted data. The schema and cases contain no
credential, secret, token, private key, personal data, production
configuration, private path or context, restricted content, provider-specific
assumption, remote-resolution instruction, or unnecessary disclosure.

Bounds reduce unbounded structural supply but prove no runtime memory, CPU,
time, thread, process, handle, parser, operating-system isolation, or denial-
of-service guarantee.

## Integrated lifecycle and boundary

The exact candidate was Accepted and later governed-integrated through PR #146.
The integrated `main` tree equals the Accepted promotion tree, issue #145 is
closed/completed, local `main` was synchronized, and the exact task branch was
removed locally and publicly under the separately attributable integration and
cleanup authority recorded above.

The original isolated execution and evidence remain bound only to candidate
commit/tree `d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875`. Promotion and integration did not
execute the schema or cases again and created no new evidence instance.

Completed integration authorizes no Profile representation, Profile Schema
Resource, Tool expansion, CI, release, publication, support, certification,
hosting, deployment, H2.4 completion, or later phase. Each requires new
separate authority.

## References

- [Epistemic Provenance and Freshness Extension Module Definition](epistemic-provenance-freshness-extension-module-definition.md)
- [Epistemic Provenance and Freshness JSON Representation Boundary](epistemic-provenance-freshness-extension-module-json-representation-boundary.md)
- [Extension Module and Profile Schema Resource, Packaging and Declaration Model](extension-module-profile-schema-resource-packaging-declaration-model.md)
- [Extension Module and Profile Executable Schema and Validation/Conformance Boundary](extension-module-profile-executable-schema-validation-conformance-boundary.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [ADR-0042](adr/0042-epistemic-provenance-freshness-extension-module-definition-schema-resource.md)
- [Accepted Schema Resource](../../schemas/extension-modules/epistemic-provenance-freshness/1.0.0/schema.json)
- [Synthetic cases](../../tests/schemas/extension-modules/epistemic-provenance-freshness/1.0.0/cases.json)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
