# ADR-0001: Public Core Boundaries

## Status

**Accepted.** Final human approval has been granted under [GOVERNANCE.md](../../../GOVERNANCE.md). On merge and publication to `main`, ADR-0001 is published as an accepted architecture decision.

## Context

CNTX needs a public foundation for bounded, verifiable collaboration without exposing private implementations or prematurely selecting technology. Context overload undermines focus, reliability, reviewability, privacy, and cost control when all work is placed in one accumulated context. The public core therefore needs stable conceptual boundaries before future schemas, validators, runtimes, adapters, or reference implementations are considered.

## Decision

CNTX public core owns the normative conceptual contracts, invariants, authority model, lifecycle semantics, provenance rules, and extension boundaries described by the [core architecture contract](../core-contract.md). Its lifecycle is: `intent → decomposition → approved task contract → context selection → bounded execution → evidence → specialist review → human decision → integration → compact state update`.

The public core remains independent of specific models, providers, runtimes, storage systems, transports, industries, and private implementations. It excludes secrets, private project data, production configurations, and domain-specific implementation details. It does not yet include executable schemas, validators, orchestration, routing, APIs, CLIs, workflows, or adapters. Future implementations are permitted only as conforming layers around the public core and MUST NOT redefine final human authority, provenance, privacy boundaries, or lifecycle semantics.

## Consequences

Architecture documentation can establish shared conceptual constraints without claiming runtime functionality. Future implementation proposals MUST demonstrate conformance to the core contract and receive the authority required by governance. The public core remains portable across collaboration patterns, but implementation choices and operational details remain deliberately deferred.

## Rejected alternatives

- Starting with a provider-specific runtime, because it would make a public foundational contract dependent on a particular integration.
- Starting with the private reference implementation, because private context and implementation concerns do not define the public core.
- Placing all context in one global project brain, because it conflicts with minimal task-scoped context and context isolation.
- Allowing agents to infer authority and scope implicitly, because consequential work requires explicit, reviewable boundaries.

## Follow-up decisions

Future accepted decisions may address identifiers and versioning, field-level schemas, lifecycle state-machine details, validation rules, trust levels and risk classes, context selection algorithms, storage and serialization formats, adapter interfaces, policy evaluation, and conformance testing. They MUST not preselect a technology or provider without an approved decision.
