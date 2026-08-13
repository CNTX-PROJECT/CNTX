# ADR-0043: CNTX Context Packet Epistemic Provenance and Freshness Profile JSON Representation Boundary

- **Status:** Accepted
- **Date:** 2026-08-13
- **Issue:** [#147](https://github.com/CNTX-PROJECT/CNTX/issues/147)
- **Issue-contract acceptance comment:** [5273569440](https://github.com/CNTX-PROJECT/CNTX/issues/147#issuecomment-5273569440)
- **Exact-head acceptance comment:** [5277015423](https://github.com/CNTX-PROJECT/CNTX/issues/147#issuecomment-5277015423)
- **Baseline:** commit `9f482043f76c792f6c2e1e96eb4a535ee26b3a99`, tree `7b2f45791e3b7bff7e856f26fff9b22598c06709`
- **Accepted candidate:** commit `05e55ded2a7d0276ee9832b0bdff973b8b19b0d5`, tree `d8d5855b0c986f008da2b123cd21f2cd6c6f0b2b`
- **Decision:** Accepted ARCH-043 — CNTX Context Packet Epistemic Provenance and Freshness Profile JSON Representation Boundary

## Context

Accepted ARCH-039 defines one narrowing-only Profile Definition with exact
Identifier/Version `1.0.0` and exactly two subjects: Context Packet Contract
Definition `1.0.0` and Epistemic Provenance and Freshness Extension Module
Definition `1.0.0`. Accepted ARCH-040 defines the closed Module declaration
representation, and integrated ARCH-042 defines its separate Schema Resource.

ARCH-039 deliberately creates no representation. A possible later Profile
Definition Schema Resource cannot validate an undefined application target.
The representation must stay outside Core, reference rather than duplicate
ARCH-040, associate every exact selected Context Packet source without
assuming `sourceReference` uniqueness, and preserve non-aggregation and final-
human authority.

## Decision

Define one closed standalone JSON-compatible Profile application/declaration
record for one exact Context Packet Artifact Instance/Revision under one exact
approved Task Contract Artifact Instance/Revision.

The representation is governed only by Profile Definition Identifier
`https://github.com/CNTX-PROJECT/CNTX/profile-definitions/context-packet-epistemic-provenance-freshness`,
Version `1.0.0`, and its exact two Accepted subjects and authoritative source
revision pins. It allocates no second Profile identity/version and no separate
Representation identity/version.

### Closed root

Define exactly fourteen required closed root members:

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

All root and subordinate objects are closed. All root members are required.
Unknown members, extension bags, null/default repair, fallback, coercion, and
silent omission are prohibited. Conditional absence is explicit.

### Exact governing and target coordinates

Keep Profile Definition Identifier/Version/category/source revision, two exact
Profile Subject Identifier/Version/source revisions, application
identity/revision/supersession, target Context Packet identity/revision, and
governing approved Task Contract identity/revision separate and exact.

The Task Contract pin must equal the exact pin inside the target Context
Packet. Mismatch, absence, ambiguity, conflict, or missing approval remains
visible and blocks dependent favorable claims.

### Deterministic source association

`sourceAssociations` accounts for every exact target Context Packet
`payload.selectedSources.items` entry exactly once. Each association uses:

- one unique local association identity;
- zero-based `contextPacketSourceIndex` into the exact pinned packet revision;
- exact repeated `sourceReference` as a fail-closed equality check;
- explicit claim roles and only the six Accepted source categories;
- exact materiality and applicability boundaries;
- one exact ARCH-040 Module declaration identity/revision and exact
  representation-source revision; and
- provenance, temporal, policy, integrity, derivation, condition, limitation,
  and authority references.

The index is a packet-local locator only. It creates no precedence, stable
cross-revision identity, ranking, authority, or canonical serialization.
`sourceReference` alone is not assumed unique. Missing, duplicate, out-of-
range, mismatched, conflicting, or orphan associations fail closed.

### Narrowing, conditions, and evaluations

`selectedCapabilities` uses only the seventeen existing ARCH-040/042 dimension
tokens and must trace every narrowing to the exact Profile and one or both
subjects. It cannot invent or weaken a capability.

Reuse only the six existing source categories, eight information conditions,
and four ARCH-024 evaluation outcomes. Conditions and evaluations remain
separate. Missing, inaccessible, conflicting, restricted, adverse,
unsupported, or unverifiable information stays visible and blocks dependent
favorable claims.

`limitations` separates scope, minimality, source coverage, method, evidence,
access, security/privacy, resource, adverse, restricted, and unknown/
unsupported/non-executed limitations. `authority` keeps declaring, selecting,
supplying, applying, evaluating, reviewing, governing, and final-human roles
attributable and separate.

No member or result creates aggregation, scoring, approval, certification,
release fitness, deployment fitness, or authority. `automaticAuthority: false`
remains semantic and is not serialized.

### Core, supply, activation, and execution boundaries

Add no property to Context Packet, Task Contract, the Common Artifact
Envelope, any Core schema/contract/binding, or the ten-schema Tool supported
set. Core validity remains prerequisite; the Profile cannot repair Core.

Supply is exact, caller-supplied, frozen, bounded, identity preserving, and
offline first. No registry, discovery, network, redirect, alias, range,
`latest`, fallback, repair, substitution, downgrade, or ambient selection is
allowed.

The application references a separately governed activation context but is not
an activation root, generic declaration set, package, registry record, or
reusable activation syntax. Presence or validity activates nothing.

Create no schema identity/version, `$id`, media type, schema, case, policy
instance, rule, Tool/Implementation capability, code, execution, validation,
evidence, release, deployment, or later-phase authority.

## Consequences

Positive consequences:

- ARCH-039 receives one explicit target before separate schema design;
- every selected Context Packet source has one deterministic packet-local
  association without changing Core;
- the exact ARCH-040 declaration is reused rather than duplicated;
- conditions, outcomes, limitations, adverse/restricted information, and roles
  remain separate and inspectable; and
- aggregation and automatic authority remain prohibited.

Costs and limitations:

- the closed record is verbose and requires exact pins and explicit context;
- source indices are meaningful only inside one exact packet revision;
- no schema or implementation exists yet;
- design and review are non-independent; and
- representation completeness proves no truth, authenticity, integrity,
  freshness, applicability, correctness, security/privacy completeness,
  interoperability, conformance, support, release, deployment, or authority.

## Alternatives not selected

- Add members to Context Packet — rejected because Core `1.0.0` is immutable.
- Use `sourceReference` alone — rejected because uniqueness is not guaranteed.
- Hash selected-source entries — rejected because no canonicalization or digest
  mechanism is authorized.
- Embed ARCH-040 declarations — rejected because the Profile may narrow but
  cannot redefine the Module representation.
- Create a generic activation package — rejected as outside the one-record
  Profile application boundary.
- Collapse conditions/outcomes or score them — rejected by their separate
  meanings, non-aggregation, and final-human authority.
- Build the schema now — rejected because Phase 4A3.4 is separately governed.

## Protected history and non-execution

Preserve every Accepted architecture/ADR through ARCH-042, all contracts,
representations, eleven Schema Resources, 32 JSON files, cases, references,
pins, rules, Tool/Implementation behavior/evidence, settings, ruleset, tag,
immutable prerelease, H2.4, and authority records except the exact authorized
present-state correction for completed ARCH-042 integration.

This Accepted decision performs no retrieval, resolution, policy or time
evaluation, digest verification, transformation, validation, testing,
execution, evidence production, review decision, release, or deployment.

## Authority boundary

Issue `#147`, attributable issue-contract acceptance comment `5273569440`, and
attributable exact-head acceptance comment `5277015423` govern this decision.
The latter accepts candidate commit/tree
`05e55ded2a7d0276ee9832b0bdff973b8b19b0d5` /
`d8d5855b0c986f008da2b123cd21f2cd6c6f0b2b`. The preceding Proposed status,
candidate preparation, validation, Draft PR, transparent non-independent
`COMMENTED` review, rendering, and mergeability allocated or activated nothing.
Exact-head acceptance and this status-only promotion establish Accepted status
only; they do not integrate or activate ARCH-043.

Work stops at the separately governed integration gate. Ready transition,
second review, merge, issue closure, branch cleanup, schema work, Tool work,
release, deployment, Phase 4A3.4, Phase 4A3.5, and every later phase require
separate authority.
