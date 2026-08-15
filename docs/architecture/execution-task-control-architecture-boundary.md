# CNTX Execution and Task Control Architecture Boundary (ARCH-046)

## In ordinary language

CNTX needs a stable way to describe how demanding a task is and which exact
tools, implementations, models, skills, or people participate without turning
those descriptions into permission, risk, correctness, or approval.

Accepted ARCH-046 defines that conceptual boundary. The exact approved Task
Contract still controls what may happen. This decision does not create a task-
control record, choose a participant, run anything, or approve a result.

| Quick view | Meaning |
| --- | --- |
| **Status** | Accepted documentation-only conceptual architecture decision; integration pending |
| **Controlling authority** | One exact approved Task Contract Artifact Revision |
| **Complexity** | Exactly `light`, `moderate`, `heavy`, or `complex`, separate from risk and authority |
| **Participants** | 27 distinct reference/control dimensions, with no identity or capability allocation |
| **Task control** | Twelve conceptual responsibility groups, not fields, states, workflow, or code |
| **Not created** | Artifact Type, representation, schema, algorithm, Tool/Implementation, model/skill selection, execution, evidence, approval, release, deployment, or authority |

### Reading route

- [Status and authority](#status-and-authority)
- [Four complexity classes](#exact-four-work-complexity-classes)
- [Participant dimensions](#separate-participant-reference-dimensions)
- [Twelve task-control groups](#exact-twelve-conceptual-task-control-responsibility-groups)
- [Fail-closed controls](#closed-offline-first-and-fail-closed-boundary)
- [Representation and implementation boundary](#representation-identity-implementation-and-later-layer-boundary)
- [Accepted lifecycle and integration stop](#accepted-lifecycle-and-integration-stop)

This visitor layer is non-normative and adds no requirement beyond the
complete Accepted decision below.

## Status and authority

**Document Status:** Accepted; not integrated.

This decision is governed by
[issue #155](https://github.com/CNTX-PROJECT/CNTX/issues/155). Attributable
EIGENAAR / Final Authority acceptance of the exact issue contract is recorded
in issue comment
[5297998742](https://github.com/CNTX-PROJECT/CNTX/issues/155#issuecomment-5297998742).
The accepted issue body contains exactly 34,282 Unicode characters, 34,328
UTF-8 bytes, and SHA-256
`65e12417356511214087a8ea8e1db716aa0aca0a53a73d8bb4e4c2ad32aab5d0`.

The exact accepted public baseline is commit
`255e781daf8d691c769c84a71dfdb3bd5b95ad4c`, complete tree
`558f87c5ce31500624a7d0a3839b368611735729`, with exactly 208 tracked paths.
The issue contract authorizes one documentation-only candidate with two added
and three modified paths and contractually designates 203 baseline paths as
protected. Because the two additions have no baseline objects and only three
existing paths change, the complete candidate comparison additionally proves
all 205 unchanged baseline paths byte-for-byte and mode-for-mode identical.
This stronger proof changes no allowlist or authority boundary.

Attributable EIGENAAR / Final Authority exact-head acceptance is recorded in
PR comment
[5298435115](https://github.com/CNTX-PROJECT/CNTX/pull/156#issuecomment-5298435115),
bound only to candidate commit
`d8ce562b7d4cf3cb10188216e706f6d4dbebe53a` and complete tree
`375345f27d6b122349b8cb7ba4eda5749d372856`.

Issue-contract acceptance authorized candidate preparation, validation, one
candidate commit, one push, one Draft pull request, one transparent non-
independent `COMMENTED` review, and a mandatory stop. It did not accept
ARCH-046 or any candidate commit/tree. The exact-head comment above and this
separately authorized status-only promotion establish Accepted status only.
They do not authorize integration, merge, closure, synchronization, cleanup,
representation, implementation, execution, release, or deployment.

## Purpose and exact decision boundary

ARCH-046 defines exactly one documentation-only conceptual boundary for later,
separately governed task execution controls. The decision:

1. keeps one exact approved Task Contract Artifact Revision as the controlling
   task-level authority;
2. defines exactly four descriptive work-complexity classes independently
   from risk, consequence, authority, priority, urgency, cost, duration,
   uncertainty, evidence, capability, routing, and approval;
3. keeps Tool, Implementation, Model, Skill, executor, capability,
   configuration, dependency, environment, context, output, evidence,
   conformance, support, release, deployment, and authority dimensions
   separate;
4. identifies exactly twelve conceptual task-control responsibility groups for
   later representation or implementation work;
5. preserves minimum justified context, least privilege, exact pins, closed
   caller-supplied frozen inputs, offline-first processing, visible conditions,
   fail-closed stops, non-aggregation, evidence/review separation, and final
   human authority; and
6. selects no concrete representation, member, token, state, transition,
   algorithm, threshold, schema, prompt, API, runtime, scheduler, orchestrator,
   workflow, implementation, or execution.

This is the smallest conceptual architecture step for the public roadmap's
“Execution and task controls” milestone. It does not begin team authority and
temporary context, a real vertical slice, adapters, portability/CI,
reassessment, release, or deployment.

## Accepted basis and precedence

ARCH-046 remains subordinate to and preserves:

- ARCH-001 through ARCH-003: explicit human authority, least privilege,
  minimum context, separate identity/version/status, architecture/schema
  layering, and no authority from validity or repository presence;
- all nine Accepted Artifact Contracts, especially the exact approved
  [Task Contract](../contracts/task-contract-artifact-contract.md), while
  keeping context, execution claim, evidence, review, decision, and compact
  state separate;
- ARCH-028 through ARCH-033: independent identity, capability, configuration,
  dependency, environment, input, output, evidence, conformance, support,
  release, deployment, and authority dimensions; exact frozen caller-supplied
  context; offline-first processing; visible fail-closed conditions; and the
  dependency-first future lifecycle;
- ARCH-034 through ARCH-037 and the bounded local validation and integrity
  slice without generalizing its exact Tool/Implementation identities,
  supported set, execution, or evidence;
- ARCH-038 through ARCH-045: exact Definition, representation, Schema
  Resource, case, governing-declaration, source/provenance/freshness,
  non-aggregation, fail-closed, adverse/restricted-evidence, and
  `automaticAuthority: false` boundaries; and
- all Accepted Binding, validation/evidence, release, completion, maintenance,
  settings, immutable-object, privacy, provenance, review, acceptance,
  integration, and lifecycle records.

If a proposed responsibility cannot be justified by those public sources or
the explicit roadmap outcome, it remains outside this decision.

## Exact four work-complexity classes

The conceptual boundary defines exactly these four descriptive classes:

1. `light`: one narrow, mechanically straightforward operation or check with
   limited internal dependency and interpretation load;
2. `moderate`: several bounded dependent steps or one contained interpretation
   problem within an established boundary;
3. `heavy`: broad or deep work with substantial known dependency, validation,
   evidence, or resource coordination while the governing architecture remains
   established; and
4. `complex`: work with interacting boundaries, dependencies, uncertainty, or
   trade-offs that requires explicit decomposition and architectural
   reasoning.

The class is accompanied conceptually by its rationale, applicable scope, and
uncertainty. It is descriptive planning context only. It is not:

- a risk, trust, safety, security, privacy, consequence, authority, permission,
  priority, urgency, cost, duration, token, energy, resource, capability,
  routing, participant-selection, quality, confidence, readiness, support,
  release, or deployment class;
- a score, grade, badge, traffic light, rank, threshold, percentage, aggregate
  result, verdict, recommendation, approval, certification, or Service Level;
- an executor, tool, implementation, model, skill, provider, runtime, or model-
  reasoning-tier selection;
- an instruction to split, route, schedule, parallelize, delegate, retry,
  resume, replay, escalate, review, merge, release, or deploy work; or
- evidence that the task is well bounded, authorized, feasible, complete,
  correct, safe, conformant, accepted, or integrated.

No class orders human importance or consequence. A `light` task may require
the strongest available security, privacy, review, or final-human gate. A
`complex` task may remain narrow and low consequence. A missing, disputed, or
uncertain class remains visible; no default or implementation-preferred class
is inferred.

## Separate participant-reference dimensions

The conceptual boundary distinguishes exactly these 27 dimensions:

1. Tool Identity;
2. Tool Version;
3. Implementation Identity;
4. Implementation Version;
5. Model Identity;
6. exact Model Version or revision;
7. Skill Identity;
8. exact Skill Version or revision;
9. bounded executor role or reference under the exact Task Contract;
10. capability claim;
11. configuration;
12. dependency set;
13. execution environment;
14. supplied governing inputs and minimum Context Packet;
15. output;
16. diagnostics;
17. evidence and provenance;
18. conformance claim;
19. interoperability claim;
20. compatibility claim;
21. security and privacy observations;
22. resource observations;
23. support state;
24. certification state;
25. release state;
26. deployment state; and
27. attributable authority and final-human decision.

One system or person may later participate in more than one dimension only
when every claimed role, exact identity/version or revision, governing source,
capability, input, output, evidence item, limitation, conflict, and authority
boundary is separately declared and evaluated.

An exact participant reference proves or grants no existence, availability,
authenticity, ownership, trust, current status, retrieval, access, disclosure,
installation, network authority, capability, suitability, correctness,
security, privacy, determinism, compatibility, interoperability, conformance,
support, release fitness, deployment fitness, assignment, selection, routing,
scheduling, delegation, execution, retry, review, recommendation, acceptance,
approval, integration, merge, release, deployment, or authority.

Provider-, repository-, URI-, package-, or channel-shaped identifiers remain
opaque identities. ARCH-046 allocates no Tool, Implementation, Model, Skill,
executor, capability, configuration, dependency, interface, or provider
identity/version. The exact ARCH-037 Tool and Implementation identities and
versions remain unchanged and bounded to their Accepted minimal validation and
integrity slice.

## Exact twelve conceptual task-control responsibility groups

A conforming future execution/task-control design must semantically address
all twelve groups below without treating them as a concrete record or fixed
field set:

1. **Governing task and authority** — one exact approved Task Contract Artifact
   Revision; governing Project Charter and Workstream context; exact authority
   source, approver, bounded delegation, executor responsibility, validity,
   revocation, supersession, and no retroactive authority.
2. **Objective and lifecycle boundary** — one coherent bounded objective,
   intended outcome, deliverables, non-goals, exclusions, acceptance criteria,
   current gate, and separate completion, closure, integration, merge, release,
   and deployment boundaries.
3. **Work complexity** — exactly one declared `light`, `moderate`, `heavy`, or
   `complex` class where required, plus rationale, applicable scope, and
   uncertainty, kept independent from every non-effect above.
4. **Participant references and capabilities** — exact Tool/Implementation/
   Model/Skill and executor references where applicable; their exact versions
   or revisions and provenance; separate claimed capabilities,
   non-capabilities, limitations, and authority boundaries.
5. **Context and frozen inputs** — the minimum justified Context Packet,
   authoritative sources, exact revisions/versions, provenance, supplied
   records/resources/declarations/packages where separately authorized, and
   one closed finite frozen input set.
6. **Actions, resources, interactions, and side effects** — permitted and
   forbidden actions, resources, paths, systems, data, tools, external
   interactions, access/disclosure/retention boundaries, and material side
   effects, all subordinate to the Task Contract.
7. **Dependencies, interfaces, and conditions** — exact dependencies and
   interfaces plus separate assumptions, constraints, risks, adverse facts,
   conflicts, unknowns, unsupported conditions, restricted evidence, and
   unresolved uncertainty.
8. **Configuration, environment, and limits** — exact configuration,
   dependencies, runtime/environment facts, resource and operation limits,
   budgets only where separately governed, observation boundaries, and
   unsupported or exceeded-limit behavior.
9. **Checkpoints and controlled continuation** — checkpoint, bounded
   delegation, concurrency, parallelism, ordering, retry, resume, replay,
   idempotency, cancellation, and compensation responsibilities only where the
   Task Contract requires them, without selecting a mechanism or automatic
   transition.
10. **Stop and escalation** — explicit ambiguity, authority, context,
    dependency, access, security/privacy, change, failure, conflict, resource,
    unsupported, blocked, revocation, expiration, and escalation conditions;
    none may be silently repaired or reclassified as success.
11. **Output, evidence, and review** — expected outputs, diagnostics, changed-
    resource and side-effect evidence, provenance, validation, failures,
    limitations, adverse/restricted evidence, non-execution, specialist-review
    scope/independence, dissent, uncertainty, and acceptance evidence, with no
    aggregate result.
12. **Human decision and consequential gates** — execution, evidence, review,
    recommendation, acceptance, approval, integration, merge, release,
    deployment, completion, closure, cleanup, correction, withdrawal,
    deprecation, and supersession remain separately attributable and
    traceable; final consequential authority remains human.

These are responsibility groups, not JSON members, schema properties, state
codes, workflow steps, permission rules, API operations, prompts, or UI
fields. Their order creates no execution order, precedence, authorization, or
default.

## Controlling Task Contract and minimum context

Only an explicitly approved exact Task Contract Artifact Revision grants task-
level authority for consequential use. Complexity, identity, assignment,
availability, capability, access, credentials, implementation state,
repository presence, automation, validation, review, previous success, or
technical necessity cannot create or broaden that authority.

The Task Contract remains controlling for objective, scope, actions,
resources, paths, systems, side effects, external interactions, executor,
delegation, dependencies, context, deliverables, evidence, acceptance,
security/privacy, stop/escalation, validity, amendment, integration, merge,
release, and deployment. Control metadata cannot amend or override it.

An approved Task Contract exists before authoritative Context Packet selection
or bounded execution. Only minimum justified task-relevant context may be
supplied. Exact sources/revisions and provenance remain visible. Unrelated
workstream, task, private, or historical material stays excluded by default.
Context relevance is not access, disclosure, retention, execution, or
authority.

A conflict with the exact Task Contract or a higher authority stops or
escalates processing without expansion, coercion, repair, substitution,
fallback, or retroactive approval.

## Closed, offline-first, and fail-closed boundary

Every governing input to later consequential task control is exact, caller
supplied, finite, closed, source/revision aware, and frozen for the applicable
execution or decision boundary. Ambient workspace, memory, profile, history,
cache, registry, network, discovery service, mutable alias, `latest`, installed
package, participant availability, and prior result are not implicit inputs or
authority sources.

ARCH-046 selects no discovery, retrieval, redirect, installation, package-
manager, network, cache, storage, transport, routing, scheduling, context-
selection, prompt-assembly, model-selection, skill-selection, retry,
parallelism, checkpoint, state-machine, policy, permission, sandbox,
enforcement, or orchestration mechanism.

Missing, additional, ambiguous, conflicting, stale, revoked, expired,
superseded, inaccessible, unauthorized, restricted, adverse, unsupported,
unbounded, or unverifiable required input remains separately visible and
fails closed. Exceeded or absent required limits, undeclared side effects,
material dependency change, missing evidence, inability to meet a stop
condition, and security/privacy uncertainty also fail closed.

No newest/latest, ordering, availability, popularity, majority, consensus,
ranking, model score, benchmark, cost, speed, previous success, provider,
implementation preference, default, coercion, repair, substitution, retry, or
fallback resolves a conflict or missing requirement silently.

## Checkpoint, delegation, concurrency, and retry boundary

This decision recognizes only that later exact task control may need
responsibilities for checkpoints, bounded delegation, ordering, concurrency,
parallelism, retry, resume, replay, idempotency, cancellation, and
compensation. It selects no state, token, transition, clock, timeout, count,
threshold, algorithm, queue, worker, scheduler, lock, lease, transaction,
protocol, storage, transport, or implementation.

No checkpoint proves completion or acceptance. No delegation transfers more
authority than its exact source. Concurrent or parallel work shares no scope,
context, evidence, acceptance, or authority unless the governing Task Contract
expressly establishes each relation. Failure, stop, timeout, or an adverse
result does not itself permit retry, resume, replay, fallback, or compensation.

A later mechanism must preserve the exact attempted action, inputs,
participant references, outputs, side effects, failure/stop reason, evidence,
and remaining authority. It cannot hide, overwrite, aggregate away, or
retroactively authorize an earlier attempt.

## Evidence, review, non-aggregation, and final authority

Task-control metadata and technical execution are not evidence of correctness
or authority by themselves. A later execution claim traces to the exact Task
Contract revision, minimum Context Packet, frozen inputs, exact participant
references, configuration/dependencies/environment, actions/resources/side
effects, limits, outputs, failures, non-execution, provenance, and limitations
appropriate to that claim.

Execution Result, evidence, validation, conformance claim, specialist review,
recommendation, human decision, integration, and compact state remain separate
records or responsibilities under their Accepted contracts. Evidence may be
incomplete, adverse, conflicting, restricted, or unavailable. Absence of
evidence is not evidence of success, safety, correctness, or authority.

Individual controls and outcomes remain separate. No universal or aggregate
`valid`, pass/fail, success, readiness, quality, safety, risk, trust,
conformance, compatibility, support, release, deployment, or approval result
is created. A complexity class is never an aggregate result.

Tools, implementations, models, skills, agents, authors, executors,
validators, reviewers, maintainers, credentials, repositories, dashboards,
automation, and planning artifacts have no final authority merely by
participating or producing output/evidence. Architecture, security/privacy,
acceptance, integration/merge, release, and deployment decisions retain the
applicable attributable human authority.

The continuing semantic assertion is `automaticAuthority: false`.

## Representation, identity, implementation, and later-layer boundary

ARCH-046 is conceptual architecture only. It creates no new Artifact Type,
Artifact Instance, Definition, record, payload, root, field, property, member,
machine-readable token/enumeration, schema family, or canonical
representation.

It allocates no Task Control Identifier/Version, participant registry,
Tool/Implementation/Model/Skill Identity or Version, capability identity,
configuration identity, dependency identity, interface identity, Schema
Identifier/Version, `$id`, package/bundle identity, output/evidence identity,
media type, protocol, API, URI contract, or Serialization Binding.

It creates no JSON/YAML/XML object, schema, case, fixed expected result,
manifest, package, bundle, resolver, registry, catalog, cache, mirror,
validator, library, SDK, CLI, API, prompt, template, model adapter, skill
adapter, runtime adapter, policy module, router, scheduler, queue, engine,
orchestrator, workflow, CI, state machine, access control, permission engine,
sandbox, service, product, code, dependency, lock, installation, invocation,
execution, output, diagnostic, evidence instance, review, decision, release,
support, certification, hosting, or deployment.

The ARCH-033 dependency-first order remains controlling for concrete
declaration/package/Binding/Validation Output/Portable Conformance Evidence,
Tool/Implementation, implementation/evidence, reassessment, and release work.
This conceptual decision reserves, skips, executes, or authorizes none of
those phases.

Team or multiple-principal authority, temporary context capsules, one real
vertical-slice test, adapters, portability/CI, adversarial reassessment,
release, and deployment remain separate later roadmap gates.

## Limitations, security, privacy, and restricted evidence

This boundary cannot prove that a task is correctly classified, well bounded,
feasible, safe, low risk, sufficiently resourced, assigned to a suitable
participant, supplied with complete context, executed correctly,
independently reviewed, conformant, accepted, approved, ready to integrate,
supported, releasable, or deployable.

Participant identities/revisions, capability declarations, complexity
rationale, Task Contract approval, context supply, validation, review, and
repository presence cannot prove external source content, authenticity,
availability, access, permission, trust, model/skill behavior, implementation
correctness, determinism, evidence sufficiency, or final authority.

Every later supplied source, context item, participant reference, input,
output, condition, and evidence reference is untrusted. A separately governed
implementation must bound document size, collection count, nesting, resource
use, diagnostics, logs, retention, disclosure, and failure handling.

Public records contain public-safe metadata only. Credentials, secrets,
personal data, private repository content, private context, restricted
evidence, production configuration, and exploitable detail do not belong in
CNTX Public Core. Restricted-evidence metadata cannot expose or replace the
restricted evidence. Missing, adverse, unsupported, unresolved, stale,
revoked, expired, superseded, and restricted conditions remain separate and
visible; they are not ignored, scored, ranked, defaulted, repaired, or
accepted by fallback.

No Tool, model, skill, schema, case, runner, scheduler, workflow, or other
mechanism is executed in this documentation-only decision. No prior execution
or evidence is reinterpreted as ARCH-046 validation.

## Accepted lifecycle and integration stop

Issue-contract acceptance comment `5297998742` authorized only this exact
documentation candidate, validation, one candidate commit, one push, one
Draft pull request, one transparent non-independent `COMMENTED` review, and
the mandatory exact-head stop.

Candidate preparation, Markdown/link validity, review, Draft state,
repository presence, and mergeability did not accept or integrate ARCH-046.
Attributable exact-head acceptance comment `5298435115` accepted only
candidate commit/tree `d8ce562b7d4cf3cb10188216e706f6d4dbebe53a` /
`375345f27d6b122349b8cb7ba4eda5749d372856`. The preceding Proposed status
allocated or activated nothing. Exact-head acceptance and status-only
promotion establish Accepted status only and make no semantic architecture
change.

Work stops before separate integration authority for the exact promotion head
and complete tree. Ready, integration, merge, issue closure, main
synchronization, branch cleanup, representation/schema work,
Tool/Implementation, model/skill selection, execution/evidence, team
authority/context, vertical slice, adapter, reassessment, release, support,
certification, hosting, and deployment each remain separately governed.

## References

- [Core Architecture Contract](core-contract.md)
- [Task Contract Artifact Contract](../contracts/task-contract-artifact-contract.md)
- [Extension Module and Profile Tooling and Implementation Boundary](extension-module-profile-tooling-implementation-boundary.md)
- [Concrete Validation and Integrity Tool and Implementation Contract](concrete-tool-implementation-contract.md)
- [Governing Definition Declaration and Frozen Governing Declaration Set JSON Representation Boundary](governing-definition-declaration-set-json-representation-boundary.md)
- [ADR-0033](adr/0033-extension-module-profile-tooling-implementation-boundary.md)
- [ADR-0037](adr/0037-concrete-tool-implementation-contract.md)
- [ADR-0045](adr/0045-governing-definition-declaration-set-json-representation-boundary.md)
- [ADR-0046](adr/0046-execution-task-control-architecture-boundary.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
