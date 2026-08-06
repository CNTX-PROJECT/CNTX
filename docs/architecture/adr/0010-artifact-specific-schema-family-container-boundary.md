# ADR-0010: Artifact-Specific Schema Family and canonical artifact container boundary

## Status

Accepted.

This ADR records a documentation-only accepted decision governed by
[issue #44](https://github.com/CNTX-PROJECT/CNTX/issues/44). The Owner / Final
Authority separately accepted exact reviewed candidate head
`5e8d003ffd6d6f27cfb53201a6d55c570a7b99e4`.

## Context

ARCH-003 organizes common and artifact-specific definitions within a Schema
Family while preserving independent identity, ownership, review, and
versioning. ARCH-004 and ARCH-005 separate Common Artifact Envelope semantics
from artifact-specific payload and relationship meaning. ARCH-006 through
ARCH-008 establish logical identity, Draft 2020-12, standalone resources,
static exact-version references, and offline-first resolution. ARCH-009 creates
the Accepted Common Artifact Envelope Schema Version `1.0.0` but intentionally
evaluates only the envelope object and defers the complete artifact root.

All nine artifact-specific contracts were Accepted, but before this decision
no artifact-specific logical Schema Identity, executable resource, active
Schema Version, full artifact container, or payload schema existed. Without a
shared pre-executable boundary, later artifact schema tasks could choose
incompatible root shapes, copy the common envelope, use moving references,
conflate schema and contract identity, or create an accidental monolithic
family.

## Decision

Adopt the following Accepted architecture:

1. Organize the CNTX Public Core Schema Family as one Accepted Common Artifact
   Envelope identity plus nine separately governed artifact-specific logical
   Schema Identities, with future extensions, profiles, bindings, and tooling
   remaining separately governed.
2. Allocate one logical identity under `CNTX Public Core Schema Family` for
   each of Project Charter, Workstream, Task Contract, Context Packet,
   Execution Result, Evidence Bundle, Review Record, Decision Record, and State
   Snapshot artifacts.
3. Reserve `1.0.0` only as the inactive initial accepted Schema Version target
   for each identity; create no family-wide or lockstep version.
4. Define every future full-artifact root as one closed object with exactly two
   mandatory members: `envelope` and `payload`.
5. Evaluate the value at `/envelope` through a static, fragmentless `$ref` to
   exact Accepted Common Artifact Envelope Schema Version `1.0.0`:
   `https://github.com/CNTX-PROJECT/CNTX/schemas/common-artifact-envelope/1.0.0`.
6. Require each artifact-specific resource to constrain the envelope's
   `artifactType` to its exact Accepted canonical token without altering the
   common resource.
7. Treat `envelope.governingSchema` as the artifact-specific schema pin, not
   the common dependency, and preserve all identity/version dimensions.
8. Place artifact-specific contract-owned meaning at `/payload`; require a
   closed payload object in the later executable definition while deferring
   all payload fields and relationship mechanics.
9. Make the exact common envelope the only mandatory external Schema Resource
   dependency for initial artifact-specific resources; do not infer
   artifact-to-artifact schema references from contract dependencies.
10. Consider later executable-schema tasks in exact CONTRACT-001 through
    CONTRACT-009 order, each under a separate authority and acceptance gate.
11. Keep artifact-specific version lines independent and require explicit
    compatibility decisions when a common-envelope version changes.
12. Keep the logical object container distinct from any artifact Serialization
    Binding, transport, storage, runtime, or product.

## Rationale

One closed two-member root makes every complete Artifact Instance predictable
without moving artifact-specific meaning into the common layer. A direct exact
common reference preserves one immutable Accepted envelope definition, while
separate payload ownership preserves the nine contracts. Technology-neutral
identity allocations permit later concrete `$id` decisions without conflating
logical identity with URI, path, or publication. Independent version lines
avoid unrelated lockstep changes.

The canonical contract order is retained as a rollout discipline rather than
an automatic schema dependency graph. This preserves traceability and avoids
cycles or embedded authority copies.

## Consequences

Positive consequences:

- all nine future artifact schemas have stable logical identities;
- every complete artifact uses the same closed root;
- common envelope and artifact payload remain separately reviewable;
- exact static common-version pinning is mandatory;
- version evolution remains independent; and
- later executable tasks have a deterministic dependency order.

Costs and limitations:

- no artifact-specific executable schema or payload exists yet;
- closed roots require explicit versioned evolution;
- Contract Definition identity/version allocation may remain a prerequisite;
- common-envelope evolution requires compatibility review across dependants;
- extensions and profiles require a separate mechanism; and
- no binding, validator, resolver, runtime, release, or deployment is supplied.

## Rejected alternatives

- **Flat combined root** — rejected because it erases common/payload ownership.
- **Optional envelope or payload** — rejected because a complete artifact
  requires both regions.
- **Open root** — rejected because unknown members could add ungoverned
  semantics.
- **Copied common definitions** — rejected because they can drift or weaken.
- **Internal `$defs` references** — rejected because internal names are not a
  public compatibility surface.
- **Moving, relative, or dynamic common references** — rejected because exact
  Accepted dependencies must remain immutable and offline-controllable.
- **One monolithic artifact schema** — rejected because artifact identities,
  payloads, reviews, and versions remain separate.
- **Family-wide version** — rejected because meanings evolve independently.
- **Automatic artifact-to-artifact schema dependencies** — rejected because
  contract dependency does not imply executable embedding.
- **Container as Serialization Binding** — rejected because instance-model
  shape does not determine bytes, encoding, transport, or storage.
- **Concrete `$id` or executable payload now** — rejected as outside this
  documentation-only phase.
- **Review or validity as acceptance** — rejected because final authority
  remains human and exact-revision-bound.

## Security and privacy

The decision requires no secret, credential, personal data, private path,
production configuration, restricted source content, provider-specific value,
private project context, or implementation detail. Identifiers and references
grant no discovery, retrieval, disclosure, trust, execution, release, or
deployment permission. Automatic network retrieval remains disabled by
default.

## Validation and authority boundary

The accepted decision preserves the exact five-path scope, nine identity/token
allocations, inactive `1.0.0` targets, two-member closed root, exact common
`$ref`, independent versions, payload ownership, rollout order, UTF-8, links,
public/private constraints, and all Accepted governing sources.

DE ARCHITECT and the Bounded Implementer were the same operational agent under
the disclosed non-independent review arrangement in issue #44. The review PASS
was evidence, not acceptance. The Owner / Final Authority separately accepted
the exact reviewed candidate head.

## Deferred scope

Deferred and unauthorized work includes artifact-specific executable Schema
Resources and payloads; concrete `$id` values and repository schema files;
active artifact-specific Schema Versions; Contract Definition identity/version
allocation; Artifact Instance identifier generation or revision sequencing;
changes to Common Artifact Envelope Schema Version `1.0.0`; cross-artifact
schema resources or references; Extension Module/Profile mechanics;
Serialization Bindings; canonical JSON; digest, signature, or verification
mechanisms; bundles, registries, resolvers, validators, validation output,
conformance tooling, fixtures, code generation, migrations, APIs, CLIs,
workflows, runtimes, providers, products, private or reference implementations,
releases, tags, hosted publication, and deployment.

## Continuing gate

This ADR is Accepted. It creates no executable resource or active Schema
Version; all nine `1.0.0` values remain inactive initial accepted targets. The
exact-head Owner / Final Authority acceptance authorizes only the separately
enumerated status-promotion and governed-integration sequence. Project Charter
executable-schema work remains a separately authorized candidate.
