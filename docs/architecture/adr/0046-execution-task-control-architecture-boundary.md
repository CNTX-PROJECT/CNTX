# ADR-0046: CNTX Execution and Task Control Architecture Boundary

- **Status:** Proposed
- **Date:** 2026-08-14
- **Issue:** [#155](https://github.com/CNTX-PROJECT/CNTX/issues/155)
- **Issue-contract acceptance comment:** [5297998742](https://github.com/CNTX-PROJECT/CNTX/issues/155#issuecomment-5297998742)
- **Baseline:** commit `255e781daf8d691c769c84a71dfdb3bd5b95ad4c`, complete tree `558f87c5ce31500624a7d0a3839b368611735729`, 208 paths
- **Decision:** Proposed ARCH-046 — CNTX Execution and Task Control Architecture Boundary

## Context

CNTX already separates exact Task Contract authority, Context Packet,
Execution Result, evidence, review, decision, and compact state. ARCH-033 keeps
Tool/Implementation identity, version, capability, configuration, dependency,
environment, input, output, evidence, conformance, support, release,
deployment, and authority distinct. ARCH-037 allocates one bounded concrete
Tool/Implementation pair only for the exact minimal validation and integrity
slice.

The next public roadmap milestone needs a conceptual boundary for describing
work complexity and later task-control responsibilities without generalizing
that slice, choosing participants, introducing a representation, or granting
execution authority.

Issue #155 and attributable EIGENAAR / Final Authority issue-contract
acceptance comment `5297998742` authorize one documentation-only Proposed
candidate and a stop before exact-head candidate acceptance. They do not
accept ARCH-046 or any candidate commit/tree.

## Proposed decision

Define one conceptual Execution and Task Control Architecture Boundary with:

1. one exact approved Task Contract Artifact Revision as the controlling task-
   level authority;
2. exactly four descriptive complexity classes: `light`, `moderate`, `heavy`,
   and `complex`;
3. complexity rationale, applicable scope, and uncertainty kept separate from
   risk, consequence, authority, priority, urgency, cost, duration, evidence,
   capability, routing, selection, and approval;
4. exactly 27 separate participant/control dimensions spanning Tool,
   Implementation, Model, Skill, executor, capability, configuration,
   dependency, environment, context, output, diagnostics, evidence,
   conformance, interoperability, compatibility, security/privacy, resources,
   support, certification, release, deployment, and final-human authority;
5. exactly twelve conceptual task-control responsibility groups: governing
   task/authority; objective/lifecycle; complexity; participants/capabilities;
   context/frozen inputs; actions/resources/interactions/side effects;
   dependencies/interfaces/conditions; configuration/environment/limits;
   checkpoints/controlled continuation; stop/escalation;
   output/evidence/review; and human consequential gates; and
6. minimum justified context, least privilege, exact pins, caller-supplied
   closed finite frozen input, offline-first processing, visible conditions,
   fail-closed stops, non-aggregation, evidence/review separation, and final
   human authority.

The continuing semantic assertion is `automaticAuthority: false`.

## Required separations

The four complexity classes are descriptive planning context, not risk,
safety, authority, permission, priority, resource, quality, score, rank,
verdict, participant selection, routing, scheduling, retry, review, approval,
release, or deployment classes. A `light` task may carry severe consequences;
a `complex` task may remain low consequence.

Participant identities or revisions do not establish availability,
authenticity, capability, suitability, access, execution, evidence,
conformance, support, release fitness, deployment fitness, or authority. The
existing ARCH-037 Tool and Implementation identities/versions remain
unchanged and bounded to their Accepted supported set.

The twelve groups are conceptual responsibilities, not JSON members, schema
properties, state codes, workflow steps, permission rules, API operations,
prompts, or UI fields. Their listed order creates no execution order,
precedence, authorization, or default.

## Closed and fail-closed boundary

Later consequential task control uses only exact, caller-supplied, finite,
closed, source/revision-aware, frozen governing input. Ambient workspace,
memory, profile, history, cache, network, discovery, mutable aliases,
installed packages, participant availability, and prior results are not
implicit input or authority.

Missing, conflicting, stale, revoked, inaccessible, unauthorized, restricted,
adverse, unsupported, unbounded, or unverifiable required input; exceeded
limits; undeclared side effects; material dependency change; missing evidence;
and security/privacy uncertainty remain visible and fail closed. No newest/
latest, ranking, popularity, majority, model score, cost, speed, provider,
implementation preference, repair, substitution, retry, or fallback resolves
them silently.

## Representation and implementation non-decision

Allocate no Task Control Artifact Type, record, root, field, member, token,
state, transition, identifier/version, participant registry, schema, case,
package/bundle, media type, Binding, API, protocol, prompt, template, policy,
permission, access-control, scoring, routing, scheduling, retry, checkpoint,
state-machine, orchestration, Tool/Implementation, model/skill selection,
runtime, workflow, CI, code, execution, output, evidence instance, release,
support, certification, hosting, deployment, or authority.

The ARCH-033 dependency-first order remains controlling. Team or multiple-
principal authority, temporary context, a real vertical slice, adapters,
portability/CI, reassessment, release, and deployment remain separate later
gates.

## Consequences

- CNTX gains one provider-, model-, runtime-, and domain-neutral conceptual
  vocabulary for later exact execution/task-control design.
- Complexity, participant references, capability, context, output, evidence,
  risk, consequence, review, decision, and authority remain independently
  traceable.
- The exact Task Contract stays controlling; neither metadata nor technical
  necessity can amend or broaden it.
- Checkpoint, delegation, concurrency, parallelism, retry, resume, replay,
  idempotency, cancellation, and compensation are recognized only as later
  responsibilities, with no mechanism or automatic transition selected.
- Individual outcomes remain non-aggregated and final consequential authority
  remains human.

## Lifecycle and current stop

The architecture source and this ADR remain Proposed. Candidate preparation,
validation, review, Draft state, repository presence, and mergeability do not
accept or integrate ARCH-046 and allocate or activate nothing.

After one candidate commit, one push, one Draft PR, complete validation, and
one transparent non-independent `COMMENTED` review bound to the exact
candidate commit and tree, work stops before separate attributable exact-head
candidate acceptance. Status-only promotion, Ready, integration, merge,
closure, synchronization, cleanup, representation, implementation, execution,
release, and deployment remain separately governed.
