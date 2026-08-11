# ADR-0038: CNTX Epistemic Provenance and Freshness Extension Module Definition

- **Status:** Accepted
- **Date:** 2026-08-11
- **Issue:** [#128](https://github.com/CNTX-PROJECT/CNTX/issues/128)
- **Issue-contract acceptance comment:** [5251980826](https://github.com/CNTX-PROJECT/CNTX/issues/128#issuecomment-5251980826)
- **Exact-head acceptance comment:** [5252557346](https://github.com/CNTX-PROJECT/CNTX/issues/128#issuecomment-5252557346), accepting candidate commit `e6700258c584deaabf028e8d339680567ed1715f` and tree `664f00045fc7dcfb26ff2d9cf12c5787c0524493`
- **Decision:** ARCH-038 — CNTX Epistemic Provenance and Freshness Extension
  Module Definition

## Context

Accepted ARCH-028 through ARCH-033 define the conceptual Extension
Module/Profile architecture, separate Definition identity and version policy,
explicit exact-pinned dependency and activation rules, closed resource/package/
declaration boundaries, schema/validation/conformance separation, and
tooling/implementation limits.

CNTX Public Core and the completed Validation and Integrity slice preserve
bounded human-readable source, provenance, evidence, time, limitation, and
non-authority declarations. They do not define one concrete versioned
Extension Module capability for exact source category, identity, revision,
temporal coordinates, policy-pinned freshness, clock/reference provenance,
digest meaning, or derivation.

A Profile cannot supply that missing capability. Under ARCH-028 and ARCH-030,
a Profile may only select or narrow capabilities in its exact pinned Accepted
inputs. The dependency-first next step is therefore one documentation-only
concrete Extension Module Definition before any Profile, representation,
schema, rule, tool, implementation, or evidence phase.

## Decision

Accept exactly one member of the CNTX Extension Module Definition Family:

- local name: `epistemic-provenance-freshness`;
- Definition Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness`;
- initial Definition Version: `1.0.0`;
- category: Extension Module Definition only; and
- lifecycle status: Accepted.

The Identifier is opaque and version-independent. Definition Version remains
a separate exact pin. Proposed status, issue acceptance, candidate preparation,
status promotion, branch or repository presence, Ready-for-review, review,
mergeability, URL availability, implementation recognition, or product use
does not by itself integrate the decision, allocate the Identifier, or activate
Version `1.0.0`. Exact-head acceptance comment `5252557346` plus separately
governed integration to `main` allocates and activates only this exact
Identifier and Version as the integrated Accepted Definition. No Profile
identity, version, or local name is created or reserved.

Define this Extension Module responsibility as additive epistemic provenance
and freshness meaning only. Preserve Core sovereignty and prohibit modification,
weakening, reinterpretation, repair, coercion, defaulting, fallback, or override
of any Accepted Core source, identity, version, field, token, schema assertion,
testcase, expected result, binding, evidence, rule, Tool/Implementation
contract, or final-human-authority boundary.

### Closed source categories

Define exactly six closed logical source categories for Definition
Version `1.0.0`:

1. Governing Source;
2. Observation Source;
3. Evidence Source;
4. Derived Source;
5. Human Assertion Source; and
6. Model Recollection Source.

The categories express semantic roles, not fields or serialized tokens. They
prove no identity, authority, authenticity, integrity, currentness, quality, or
fitness. Model recollection remains visible, non-governing, and unable to
substitute for an exact governing source. An unknown or unsupported category
or category version remains visible and blocks every dependent successful
claim.

Restricted, inaccessible, conflicting, missing, and unverifiable are
conditions rather than extra source categories.

### Source identity, provenance, and revision

Require every material source to preserve its exact category, source identity,
revision/version or explicit inability to establish one, claim role,
acquisition/observation provenance, limitations, adverse information, access
conditions, uncertainty, and attributable roles.

Reject mutable aliases, `latest`, `current`, newest-wins selection, unversioned
URLs, search results, repository position, filenames, cache entries,
installation state, product settings, or prior success as substitutes for an
exact source revision/version.

Keep source identity, revision, availability, provenance, authenticity,
integrity, observation, freshness, applicability, validation, evidence,
acceptance, and authority separate. No dimension substitutes for another.

### Temporal coordinates

Keep exactly four logical coordinates separate:

1. Source Publication/Revision Time;
2. Observation/Retrieval Time;
3. Record Production Time; and
4. optional Valid-Through Time.

Do not infer one from another or use one to repair another. Preserve the
declared time reference, timezone or offset, precision, uncertainty,
clock/reference provenance, and source for every supplied coordinate. A
timestamp without those boundaries and an exact applicable policy proves no
freshness or currentness.

Select no timestamp syntax, calendar profile, clock service, synchronization
mechanism, tolerance, duration, age threshold, or default timezone.

### Digest meaning

Where a digest is material, keep exact algorithm identity, digest value,
subject bytes or separately governed canonicalization, source revision,
procedure, observation time, outcome, role, evidence, and limitations separate.

Define no default algorithm. A digest match supports only its exact bounded
integrity claim. It proves no authenticity, semantic equivalence, safety,
trust, freshness, authority, or fitness. Select no algorithm, encoding,
canonicalization, signature, certificate, trust store, attestation, or
verification implementation.

### Freshness and applicability policies

Require every consequential freshness assessment to pin an exact policy
identity and version for an explicitly declared task class or source class.
Preserve the source identity/revision, source category, temporal inputs,
clock/reference basis, assessment reference time, policy condition, outcome,
diagnostics, limitations, adverse/restricted evidence, non-execution,
claimant, and authority.

Policy identity is not policy content. Policy version is not applicability.
Applicability is not freshness. Freshness is not authenticity, integrity,
correctness, completeness, acceptance, support, release fitness, or deployment
fitness.

Define no concrete policy, policy representation, task/source-class
vocabulary, duration, threshold, comparison rule, grace period, score, grade,
traffic light, or quality gate. Missing exact policy or applicability basis
fails closed; it cannot become a Satisfied freshness claim.

### Clock/reference provenance and derivation

Preserve clock/reference identity and revision where available, responsible
environment, timezone/offset, precision, resolution, uncertainty, skew,
synchronization limitation, conversions, source, and claim scope. Never
silently replace missing or conflicting clock provenance with a local clock,
record time, file metadata, or network response time.

Require every Derived Source to preserve a finite, closed, caller-supplied,
frozen chain of exact upstream source identities/revisions/categories,
observations, temporal coordinates, transformations, responsible roles,
parameters where material, order, input/output relations, omissions,
redactions, aggregation, uncertainty, adverse/restricted conditions, claims,
evidence, and limitations.

Missing material inputs or transformations, cycles, source conflicts,
unsupported mechanisms, restricted dependencies, or insufficient provenance
block dependent successful claims. Derivation transfers no governing authority
and proves no authenticity, integrity, completeness, freshness, applicability,
or semantic preservation.

### Conditions, outcomes, and authority

Keep these logical information-condition states separate: Specified, Assessed
None, Not Assessed, Missing, Inaccessible, Conflicting, Restricted, and
Unverifiable.

Assessed None is not Missing. Not Assessed is not Assessed None. Inaccessible
is not absent. Restricted is not proof. Unverifiable is not Not Satisfied.
These states allocate no serialized values or portable diagnostic vocabulary.

Where broader CNTX evaluation occurs under a separately authorized contract,
retain the ARCH-024 outcomes Satisfied, Not Satisfied, Unverifiable, and Not
Evaluated per exact dimension. Do not aggregate categories, conditions, or
outcomes into pass/fail, valid, traffic light, score, grade, badge, threshold,
quality gate, recommendation, approval, certification, release fitness,
deployment fitness, or consequential authority.

Fix the logical assertion `automaticAuthority: false`. This is a semantic
non-authority statement, not a JSON property created by this ADR.

### Dependency and activation boundary

Define no Required or Optional Extension Module Definition Dependencies and no
Profile Subject for this Accepted Definition.

Consequential use of this Accepted Definition still requires a separately
Accepted declaration/activation representation and one exact, closed,
caller-supplied, offline-first, frozen governing context under ARCH-030 and
ARCH-031. Repository,
URL, package, installation, processor, product, cache, or prior-execution
presence activates nothing.

A later Profile may only select or narrow capabilities in exact pinned Accepted
inputs. It cannot invent, weaken, reinterpret, repair, or extend this
Definition. Composition with other modules has no implicit precedence and must
remain non-conflicting and order-independent.

### Fail-closed boundary

Keep missing, ambiguous, duplicate, conflicting, unknown, unsupported,
inaccessible, restricted, adverse, insufficient, blocked, non-executed, and
unverifiable conditions visible and separate.

Block dependent successful claims on source identity/revision conflict,
unknown category/version, missing authoritative source, insufficient
provenance, absent or wrong policy pins, policy-applicability ambiguity,
temporal-coordinate conflict, clock/reference insufficiency, digest
insufficiency, incomplete or cyclic derivation, required restricted
information, evaluator-capability gaps, security/privacy conflict, resource
blockage, non-executed prerequisites, or missing authority.

Prohibit silent resolution through discovery, retrieval, network access,
redirects, registry/catalog/cache state, mutable aliases, newest/latest,
substitution, coercion, defaulting, repair, retry, fallback, order,
implementation preference, popularity, majority, consensus, score, or ranking.

### Representation and implementation boundary

Create no concrete JSON property or shape, declaration syntax, media type,
Serialization Binding, Definition/Profile/Artifact instance, Schema Identifier
or Version, `$id`, Schema Resource, assertion, manifest, testcase, fixture,
rule, evaluation-record representation, diagnostic vocabulary, policy,
algorithm, clock service, resolver, Tool/Implementation Identity or Version,
dependency, validator, runner, library, SDK, CLI, API, workflow, CI, runtime,
product, service, execution, output, evidence instance, release, publication,
support, certification, hosting, or deployment.

Concrete representation, schemas/cases, evaluation rules, Tool/Implementation
capability versions, implementation, practice, and evidence remain separately
governed phases.

## Consequences

Positive consequences:

- exact source role, identity, revision, provenance, and availability remain
  independently assessable;
- publication/revision, observation/retrieval, record-production, and
  valid-through times cannot be silently conflated;
- freshness requires an exact applicable policy and clock/reference basis;
- digest claims require an explicit algorithm and exact subject boundary;
- derived material retains upstream and transformation traceability;
- model recollection remains non-governing;
- missing, inaccessible, conflicting, restricted, and unverifiable conditions
  remain visible; and
- technical output never acquires automatic authority.

Costs and limitations:

- callers bear the cost of supplying complete exact pins, provenance, policies,
  temporal context, derivation, and limitations;
- the Definition itself proves no source authenticity, integrity, freshness,
  applicability, completeness, correctness, safety, trust, or fitness;
- timestamps without clock/reference provenance and policy evaluation prove no
  freshness;
- digests without algorithm, exact subject boundary, and verification evidence
  prove no integrity or authenticity;
- restricted evidence may leave dependent claims Unverifiable;
- model recollection may be stale, incomplete, or wrong;
- no implementation or adversarial execution evidence exists; and
- candidate preparation and review are non-independent.

## Alternatives not selected

### Create a Profile first

Not selected because a Profile cannot invent a capability absent from its exact
pinned Accepted Core and Extension Module inputs.

### Add provenance and freshness properties directly to Core `1.0.0`

Not selected because the ten Accepted Core Schema Versions and Core Artifact
JSON Binding are immutable, and an additive optional capability must not
reinterpret or repair them.

### Treat source URL or repository presence as authority

Not selected because location and availability establish neither identity,
exact revision, authenticity, acceptance, applicability, support, nor trust.

### Treat any timestamp as proof of freshness

Not selected because the four temporal coordinates, clock/reference
provenance, uncertainty, applicability, and exact policy evaluation are
separate requirements.

### Select a digest algorithm or freshness threshold here

Not selected because concrete algorithms, canonicalization, policies,
thresholds, schemas, rules, and processing mechanisms require later separate
authority and evidence.

### Use model recollection as a governing source

Not selected because model recollection may be stale, incomplete, or wrong and
cannot substitute for an exact authoritative source.

### Collapse all conditions into one pass/fail result

Not selected because missing, inaccessible, conflicting, restricted,
unverifiable, and non-executed conditions have different meaning and evidence
consequences.

## Protected predecessors and historical integrity

Preserve ARCH-001 through ARCH-037, ADR-0001 through ADR-0037, all nine
Accepted artifact contracts, all ten Accepted Schema Resources and historical
Test Manifests, exact `203/38/165`, `957/948/9`, and `9/1` inventories, all
thirteen integrity rules, Tool/Implementation identities and Version `1.0.0`
pins, Package E and practice evidence, immutable prerelease and Release
objects, protected repository settings, limitations, adverse/restricted
evidence, and every historical authority record unchanged.

## Non-decisions and non-execution

This ADR creates no sixth repository path, Profile, concrete representation,
schema, Schema Resource, testcase, rule, Tool/Implementation Version,
dependency, Python, code, runner, execution, evidence instance, workflow, CI,
setting change, release, tag, GitHub Release, publication, distribution,
support, certification, hosting, deployment, correction, withdrawal,
deprecation, supersession, or follow-on authority.

It performs no retrieval, network access, discovery, redirect following,
policy evaluation, digest verification, clock verification, transformation,
validation, testing, evidence production, release action, or deployment.

## Authority boundary

This ADR is Accepted through attributable EIGENAAR / Final Authority exact-head
acceptance comment `5252557346` on candidate commit
`e6700258c584deaabf028e8d339680567ed1715f` and tree
`664f00045fc7dcfb26ff2d9cf12c5787c0524493`. Issue-contract acceptance,
candidate preparation, repository presence, status promotion, static
validation, Ready-for-review, mergeability, transparent non-independent
ARCHITECT review, technical access, and implementation recognition do not by
themselves integrate the decision, allocate or activate its Identifier or
Version, or grant consequential authority. Separately governed integration to
`main` is required for the exact integration, allocation, and activation
effects.

Work stops at a new attributable EIGENAAR / Final Authority gate for the exact
reviewed promotion head. Integration, completion, issue closure, branch
cleanup, and every later phase require separate express authority.
