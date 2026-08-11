# ADR-0039: CNTX Context Packet Epistemic Provenance and Freshness Profile Definition

- **Status:** Proposed
- **Date:** 2026-08-11
- **Issue:** [#130](https://github.com/CNTX-PROJECT/CNTX/issues/130)
- **Issue-contract acceptance comment:** [5254030218](https://github.com/CNTX-PROJECT/CNTX/issues/130#issuecomment-5254030218)
- **Decision candidate:** ARCH-039 — CNTX Context Packet Epistemic Provenance
  and Freshness Profile Definition

## Context

The Accepted Context Packet Contract Definition requires a bounded Derived
artifact for one exact approved Task Contract revision. The Accepted ARCH-038
Epistemic Provenance and Freshness Extension Module Definition supplies
logical capabilities for source categories, identity/revision, provenance,
temporal coordinates, freshness-policy pins, clock/reference provenance,
digest meaning, derivation, visible information conditions, fail-closed
outcomes, non-aggregation, and final-human authority.

ARCH-028 through ARCH-033 require a Profile to use exact pinned Accepted
Profile Subjects. A Profile may only select or narrow capabilities already
present in those subjects. It cannot invent, extend, weaken, repair, default,
override, or silently substitute a governing capability or Definition Version.

No concrete Profile currently narrows the Accepted ARCH-038 capabilities for
Context Packet source selection and freshness claims. The dependency-first
Phase 4A2 candidate is therefore one documentation-only Profile Definition.
It creates no representation, schema, policy instance, rule, tooling,
implementation, execution, or evidence.

## Proposed decision

Propose exactly one member of the CNTX Profile Definition Family:

- local name: `context-packet-epistemic-provenance-freshness`;
- Profile Definition Identifier:
  `https://github.com/CNTX-PROJECT/CNTX/profile-definitions/context-packet-epistemic-provenance-freshness`;
- proposed initial Profile Definition Version: `1.0.0`;
- category: Profile Definition only; and
- lifecycle status: Proposed.

The Identifier is opaque and version independent. Version remains a separate
exact pin. Proposed status, issue acceptance, candidate preparation, branch or
repository presence, validation, review, Ready-for-review, mergeability, URL
availability, implementation recognition, or product use allocates or
activates nothing. Exact-head attributable acceptance plus separately governed
integration would be required to allocate and activate this exact Identifier
and Version. No Profile instance or other identity/version is created or
reserved.

### Exact Profile Subjects

Propose exactly these two Profile Subjects:

1. Context Packet Contract Definition Identifier
   `https://github.com/CNTX-PROJECT/CNTX/contract-definitions/context-packet`,
   Contract Definition Version `1.0.0`;
2. Epistemic Provenance and Freshness Extension Module Definition Identifier
   `https://github.com/CNTX-PROJECT/CNTX/extension-module-definitions/epistemic-provenance-freshness`,
   Extension Module Definition Version `1.0.0`.

The Profile has no Profile dependency, creates no Extension Module dependency,
selects no other Core contract, and cannot make Core depend on this Profile.
Subjects are logical exact identified/versioned bases, not schema references,
Artifact Instance relations, retrieval instructions, permissions,
compatibility claims, or support claims.

### Narrowing-only responsibilities

For one Context Packet under one exact approved Task Contract revision,
require logically that:

1. every material source has an explicit bounded claim role and one or more
   separately declared applicable ARCH-038 source categories;
2. every material source has exact identity and revision/version, or an
   explicit unfavorable condition explaining why a reliable exact pin cannot
   be established;
3. availability, provenance, authenticity, integrity, freshness,
   applicability, completeness, validation, evidence, acceptance, authority,
   support, release, and deployment remain separate;
4. Source Publication/Revision Time, Observation/Retrieval Time, Record
   Production Time, and optional Valid-Through Time remain separate;
5. every asserted temporal coordinate preserves source, reference, timezone or
   offset, precision, uncertainty, and clock/reference provenance;
6. every consequential freshness/currentness claim pins exact policy identity
   and version, task/source class, assessment reference time, temporal and
   clock basis, evidence, individual outcome, limitations, adverse/restricted
   information, non-execution, claimant, and authority;
7. missing or ambiguous exact applicable policy makes a dependent favorable
   freshness claim `Unverifiable` or `Not Evaluated`, never `Satisfied`;
8. every material digest claim preserves explicit algorithm, value, exact
   subject boundary or separately governed canonicalization, comparison
   procedure, provenance, outcome, evidence, and limitations;
9. every material Derived Source preserves a finite closed derivation chain
   with exact upstream and transformation identities/revisions, order,
   omissions, loss, uncertainty, adverse/restricted conditions, claim
   boundary, evidence, and limitations;
10. Model Recollection Source remains visible, non-governing, possibly stale,
    incomplete, or wrong and cannot replace a Governing Source;
11. Specified, Assessed None, Not Assessed, Missing, Inaccessible, Conflicting,
    Restricted, and Unverifiable remain distinct;
12. unknown or unsupported categories, versions, policies, temporal or digest
    mechanisms, derivations, evaluator capabilities, or resources remain
    visible and fail closed for every dependent favorable claim;
13. required restricted sources are represented publicly only through minimum
    authorized public-safe metadata and restricted content is never copied or
    treated as favorable evidence;
14. multiple applicable Profile constraints apply conjunctively, without
    override, implicit precedence, order dependence, repair, or fallback;
15. every result preserves exact subject, dimension, governing sources and
    pins, policy, evidence, times, limitations, adverse/restricted information,
    non-execution, claimant, review context, and authority; and
16. `automaticAuthority: false` and attributable final-human authority remain
    fixed.

### Sovereignty, conflicts, and outcomes

Prohibit this Profile from inventing, extending, weakening, replacing,
reinterpreting, repairing, coercing, defaulting, or overriding either exact
Profile Subject or another governing Accepted source. It cannot make a
Core-invalid representation Core-valid, neutralize a conflict, silently select
another version, or turn adverse, restricted, missing, insufficient,
unsupported, or unverifiable information into proof.

Keep `Satisfied`, `Not Satisfied`, `Unverifiable`, and `Not Evaluated` separate
per exact subject and dimension when a later authorized evaluation applies.
Create no aggregate pass/fail, valid result, traffic light, score, grade,
badge, threshold, quality gate, recommendation, approval, certification,
release fitness, deployment fitness, or consequential authority.

### Closed supply and fail-closed boundary

Require an exact, closed, caller-supplied, frozen, offline-first governing
context for any future consequential use. Repository, URL, package,
installation, implementation, product, cache, or prior execution presence
activates nothing.

Keep missing, ambiguous, conflicting, unknown, unsupported, inaccessible,
restricted, adverse, insufficient, blocked, non-executed, and unverifiable
conditions visible. Prohibit silent resolution through discovery, network
retrieval, redirects, registry/catalog/cache state, mutable aliases,
newest/latest, substitution, coercion, defaulting, repair, retry, fallback,
order, implementation preference, popularity, majority, consensus, score, or
ranking.

### Representation and implementation boundary

Create no property, value, enum, payload shape, declaration syntax, media type,
Serialization Binding, Profile instance, Artifact Instance, schema Identifier
or Version, `$id`, Schema Resource, assertion, manifest, testcase, fixture,
policy identity or instance, threshold, digest algorithm, canonicalization,
clock service, derivation serialization, rule, diagnostic vocabulary,
Tool/Implementation Identity or Version, dependency, library, SDK, CLI, API,
workflow, CI, runtime, provider, product, service, execution, output, evidence
instance, release, publication, support, certification, hosting, or deployment.

Concrete representation, schemas and cases, policies, rules, tooling,
implementation, practice, and evidence remain separately governed.

## Consequences

Positive consequences:

- Context Packet source roles, categories, exact pins, provenance, and
  unfavorable conditions remain independently assessable;
- temporal coordinates, clock/reference provenance, policies, and digests
  cannot be silently conflated;
- freshness needs an exact applicable policy and bounded evidence;
- derivations preserve closed upstream and transformation provenance;
- model recollection remains visible and non-governing;
- adverse and restricted information remains visible; and
- technical outcomes never acquire aggregate or automatic authority.

Costs and limitations:

- callers must supply exact roles, pins, provenance, policies, temporal and
  clock bases, derivations, evidence, limitations, and authority;
- the Profile proves no authenticity, integrity, freshness, applicability,
  completeness, correctness, safety, trust, minimality, or execution fitness;
- timestamps without clock/reference provenance and exact policy evaluation
  prove no freshness;
- digests without explicit algorithm, exact subject boundary, and verification
  evidence prove no integrity or authenticity;
- restricted evidence may leave claims Unverifiable;
- model recollection may be stale, incomplete, or wrong;
- preparation and review are non-independent; and
- no representation, schema, policy, rule, implementation, adversarial
  execution, or evidence instance exists.

## Alternatives not selected

### Add fields directly to the Context Packet schema

Not selected because this phase defines a logical Profile only. It cannot
change the Accepted Context Packet Contract Definition, Core Schema Version
`1.0.0`, or Core Artifact JSON Binding.

### Extend ARCH-038 instead of creating a Profile

Not selected because ARCH-038 defines reusable additive capability. The
Context Packet-specific selection and narrowing belongs in a separate exact
Profile with exact Profile Subjects.

### Treat timestamps, URLs, digests, or repository presence as sufficient

Not selected because those facts prove neither exact revision, authenticity,
integrity, freshness, applicability, acceptance, support, nor authority
without their separately required context and evidence.

### Use a default freshness threshold or digest algorithm

Not selected because concrete policies, thresholds, algorithms,
canonicalization, representations, rules, and processing require later
separate authority and evidence.

### Allow model recollection to fill missing source information

Not selected because model recollection may be stale, incomplete, or wrong and
cannot replace an exact governing source or favorable evidence.

### Collapse all conditions and outcomes into pass/fail

Not selected because information conditions and individual evaluation outcomes
carry distinct meaning, provenance, limitations, and claim effects.

## Protected predecessors and historical integrity

Preserve ARCH-001 through ARCH-038, ADR-0001 through ADR-0038, all nine
Accepted artifact contracts, all ten Accepted Schema Resources and historical
Test Manifests, exact `203/38/165`, `957/948/9`, and `9/1` inventories, all
thirteen integrity rules, Tool/Implementation identities and Version `1.0.0`
pins, Package E and practice evidence, immutable prerelease and Release
objects, repository settings, limitations, adverse/restricted evidence, and
every historical authority record unchanged.

## Non-decisions and non-execution

This Proposed ADR creates no Profile instance, property, representation,
schema, Schema Resource, testcase, rule, policy instance,
Tool/Implementation Version, dependency, Python, code, runner, execution,
evidence instance, workflow, CI, setting change, release, tag, GitHub Release,
publication, distribution, support, certification, hosting, deployment,
acceptance, status promotion, Ready transition, merge, issue closure, branch
cleanup, or follow-on authority.

It performs no retrieval, network access, policy evaluation, digest
verification, clock verification, transformation, validation, testing,
evidence production, release action, or deployment.

## Authority boundary

This ADR and ARCH-039 remain Proposed. Issue-contract acceptance comment
`5254030218`, candidate preparation, repository presence, static validation,
mergeability, transparent non-independent ARCHITECT review, technical access,
and implementation recognition do not grant acceptance, integration,
Identifier allocation, Version activation, or consequential authority.

Work stops at a new attributable EIGENAAR / Final Authority gate bound to the
exact reviewed candidate commit and tree. Status promotion, Ready-for-review,
merge, integration, issue closure, branch cleanup, and every representation,
schema, policy, rule, implementation, execution, evidence, release,
publication, support, certification, hosting, deployment, or later phase
requires separate express authority.
