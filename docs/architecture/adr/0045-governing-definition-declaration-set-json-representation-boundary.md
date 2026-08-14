# ADR-0045: CNTX Governing Definition Declaration and Frozen Governing Declaration Set JSON Representation Boundary

- **Status:** Accepted
- **Date:** 2026-08-14
- **Issue:** [#151](https://github.com/CNTX-PROJECT/CNTX/issues/151)
- **Issue-contract acceptance comment:** [5286906192](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5286906192)
- **Exact-head candidate-acceptance comment:** [5290871158](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5290871158)
- **Baseline:** commit `1d9e4667d68cce6e0289464c821bcd95e1d355ae`, tree `3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`
- **Accepted candidate:** commit `a92cb298a5106db27f0c6b720a5faa3b6571ddf1`, complete tree `1a68548638f0ff570639a051bbca65e778642ca4`
- **Accepted promotion:** commit `c7b8c5cc793516197726344e7d30c12d0a86f514`, complete tree `ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`
- **Integration:** [PR #152](https://github.com/CNTX-PROJECT/CNTX/pull/152), public `main` commit `0bccbb39a56044be3a9c7236dd828b1d1959e7ce`, complete tree `ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`
- **Integration-completion comment:** [5292133876](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5292133876)
- **Tree equality:** the Accepted promotion tree and integrated `main` tree are identical; the promotion-to-integration diff is empty
- **Issue state:** #151 is `closed/completed`
- **Decision:** Accepted and integrated ARCH-045 — CNTX Governing Definition Declaration and Frozen Governing Declaration Set JSON Representation Boundary

## Context

Accepted ARCH-030 requires one explicit, caller-supplied, closed, finite, and
frozen activation context for every consequential use of Extension Modules or
Profiles. Accepted ARCH-031 defines one logical Governing Definition
Declaration for every active Definition key and one frozen Governing
Declaration Set equal to the complete active Definition Set. Its 21 declaration
responsibilities and 11 set invariants deliberately allocate no serialized
members or concrete representation.

ARCH-032 keeps declaration/set conformance separate from package, schema,
validation output, evidence, and authority. ARCH-033 requires concrete
declaration representation before concrete Tool/Implementation work. Issue
#151 and attributable EIGENAAR / Final Authority issue-contract acceptance
comment `5286906192` authorized one documentation-only representation candidate
and a stop before exact-head candidate acceptance. Attributable exact-head
acceptance comment `5290871158` accepts only the candidate commit and complete
tree recorded above. Separately authorized status-only promotion produced
commit `c7b8c5cc793516197726344e7d30c12d0a86f514` and complete tree
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`. It established Accepted status
without a semantic decision change and did not itself authorize integration.
The later governed integration and issue completion are recorded below.

## Accepted decision

Define one closed JSON-compatible representation model with:

1. one reusable fourteen-member `GoverningDefinitionDeclaration` record for
   one exact active Definition key; and
2. one six-member `GoverningDeclarationSet` root containing exactly one
   declaration for every and only active Definition key in one exact frozen
   governing context.

### Declaration root

Require exactly:

1. `definition`;
2. `definitionSource`;
3. `activationRoles`;
4. `requiredDependencies`;
5. `optionalDependencies`;
6. `profileSubjects`;
7. `schemaResource`;
8. `packageAndContextProvenance`;
9. `capabilities`;
10. `processingLimitations`;
11. `claimScope`;
12. `conditions`;
13. `authority`; and
14. `lifecycleTraceability`.

Map every ARCH-031 responsibility exactly once: Definition category,
Identifier, and Version; Definition source, revision, and provenance;
activation roles; separate Required and Optional dependencies; Profile
Subjects; exact Schema Resource key or explicit `None`; resource source,
revision, and provenance; supplied package/context provenance; capabilities;
processing limitations; compatibility/conformance claim scope; separate
unknown, unsupported, adverse, unresolved, and restricted-evidence conditions;
attributable declaring/governing authority; and correction, withdrawal,
deprecation, and supersession traceability.

Use one closed `schemaResource` discriminator. `present` carries the complete
Schema Identifier and Version key plus exact authoritative source, revision,
and provenance. `none` carries no resource values and means that no governing
executable Definition Schema Resource exists for that key in this frozen
context. Missing, unknown, inaccessible, unsupported, failed resolution,
omission, JSON `null`, empty string, repository/package presence, mutable alias,
substitution, repair, or fallback cannot replace either state.

### Declaration Set root

Require exactly:

1. `governingContext`;
2. `activationRoots`;
3. `explicitlyActiveOptionalDependencies`;
4. `declarations`;
5. `conditions`; and
6. `authority`.

Preserve all eleven ARCH-031 invariants: completeness for every root; complete
Required closure; only separately explicitly active Optional dependencies;
Profiles as separate roots; one declaration for every and only active key;
duplicate-free membership; at most one active Version per Identifier; exact
source/revision consistency; exactly one Schema Resource key or `None` per
active key; one closed value frozen throughout consequential evaluation; and
visibility of every limitation, conflict, unknown, unsupported condition,
adverse evidence, and restricted-evidence boundary.

The complete root contains no self-asserted valid, approved, accepted,
complete, conformant, release-ready, deployment-ready, score, grade, badge,
traffic-light, recommendation, aggregate-outcome, or serialized
`automaticAuthority` member. The continuing semantic assertion is
`automaticAuthority: false`.

### Finite closed representation

Require closed objects, non-blank bounded strings, exact keys, separate
condition categories, duplicate-free declared collections, and finite limits.
General strings and opaque references are at most 2,048 characters;
identifiers, Versions, revisions, labels, and compact references are at most
512; general collections contain at most 64 items; role collections one
through 32; lifecycle collections at most 32; and condition collections at
most 128.

These are representation bounds only. They prove no runtime resource,
security, availability, interoperability, conformance, evidence, approval, or
authority property.

## Placement and separation

Keep the declaration set outside every existing CNTX Artifact Instance. Add no
member to the Common Artifact Envelope, any of the nine artifact-specific
payloads, any existing Core Artifact JSON document, or Core Artifact JSON
Binding Version `1.0.0`.

`GoverningDefinitionDeclaration` and `GoverningDeclarationSet` are shape labels,
not allocated Artifact Types or identities. JSON-compatible selects member
names and logical shapes only. It allocates no declaration/set Identity or
Version, schema identity/version, `$id`, media type, canonical bytes,
Serialization Binding, package/bundle, storage, transport, API, or executable
behavior.

## Failure and authority boundary

Keep declaration/set mismatch, missing or extra active keys, incomplete
Required closure, implicit Optional activation, Profile dependency, duplicate
key, multiple active Versions for one Identifier, source/revision conflict,
Schema Resource state mismatch, unresolved/prohibited/cyclic edge, unsupported
capability, insufficient provenance, restricted evidence, security/privacy
conflict, unbounded input, and mutation during evaluation separately visible
and fail closed.

No order, specificity, newest/latest, popularity, majority, consensus, ranking,
implementation preference, cache, previous success, substitution, repair, or
fallback resolves them silently.

Representation conformance proves only conformance to the documented shape. It
does not prove Definition acceptance, active-set correctness, source
authenticity, dependency correctness, schema validity, package completeness,
compatibility, interoperability, truth, safety, security, privacy, permission,
support, certification, release fitness, deployment fitness, or final
authority.

## Consequences

- One exact documentation model now exists for later separate declaration/set
  conformance, package, schema, binding, output/evidence, and tooling decisions.
- All 21 declaration responsibilities and 11 set invariants remain explicit
  without adding a Core Artifact or authority-bearing record.
- Required and Optional dependencies, Profile Subjects, Schema Resource
  `present`/`none`, conditions, claim scopes, attribution, and lifecycle
  history remain separate.
- Caller-supplied, offline-first, closed, frozen, and fail-closed processing
  remains mandatory for any later consequential phase.
- No executable validation, conformance verdict, package, Tool support,
  execution, evidence, release, or deployment is created.

## Alternatives not selected

### Embed declarations in existing Core artifacts

Not selected because it changes Accepted Core Artifact meaning, creates
extension-to-Core dependency, and requires separate Artifact Contract, schema,
and Serialization Binding decisions.

### Infer the set from repository, package, installation, or Tool state

Not selected because ambient or mutable state cannot create identity,
activation, provenance, acceptance, or authority.

### Use omitted or `null` schema bindings

Not selected because missing, unknown, inaccessible, unsupported, failed
resolution, and explicit `None` are materially different states.

### Add self-asserted completion or approval booleans

Not selected because a supplied value cannot prove its own completeness,
validity, acceptance, conformance, release fitness, or authority.

### Define package, schema, binding, output/evidence, or tooling now

Not selected because each depends on the representation and remains a separate
ARCH-033 lifecycle gate with its own identity/version, scope, validation,
review, and attributable authority.

## Non-decisions

This Accepted decision allocates no declaration/set Identity or Version,
Artifact Type, Core member, media type, canonical bytes, Schema Identifier or
Version, `$id`, Schema Resource, assertion, case, package/bundle, manifest,
Serialization Binding, resolver, registry, catalog, cache, API, SDK, CLI,
library, validator, Validation Output, diagnostic vocabulary, Portable
Conformance Evidence, Tool/Implementation Identity or Version, dependency,
configuration, interface, code, execution, evidence, workflow, CI, aggregate
result, automatic authority, release, support, certification, hosting, or
deployment.

## Accepted lifecycle and integrated state

Issue-contract acceptance comment `5286906192` authorized this documentation
candidate only. Candidate preparation, Markdown/link validation, review, Draft
state, repository presence, and mergeability did not accept ARCH-045. Exact-head
acceptance comment `5290871158` accepted only candidate commit/tree
`a92cb298a5106db27f0c6b720a5faa3b6571ddf1` /
`1a68548638f0ff570639a051bbca65e778642ca4`. The preceding Proposed status
allocated or activated nothing. Exact-head acceptance and status-only promotion
established Accepted status only and made no semantic representation change.

At the Accepted promotion stage, work stopped before separate integration
authority for promotion commit/tree
`c7b8c5cc793516197726344e7d30c12d0a86f514` /
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`. Ready transition, integration,
merge, issue closure, branch cleanup, and all later phases remained separately
governed. This historical stop remains part of the decision provenance.

The later public integration-completion record
[5292133876](https://github.com/CNTX-PROJECT/CNTX/issues/151#issuecomment-5292133876)
records an expected-head-pinned squash merge of that exact promotion head
through [PR #152](https://github.com/CNTX-PROJECT/CNTX/pull/152). Integrated
public `main` is commit
`0bccbb39a56044be3a9c7236dd828b1d1959e7ce`, with sole parent
`1d9e4667d68cce6e0289464c821bcd95e1d355ae`, and complete tree
`ed4e8bb0cb6479d88064d5c8330cf7fa1a3208c4`. That tree is exactly equal to the
Accepted promotion tree, the promotion-to-integration diff is empty, and issue
#151 is `closed/completed`.

The former task branch
`codex/arch-045-governing-declaration-set-json-representation` is absent from
the current local, origin-tracking, and live public-remote views. This records
present state only; it does not reconstruct, replace, or retroactively grant
historical cleanup authority. Issue #151 contains no separate public
cleanup-authority comment after the integration-completion record's explicit
cleanup stop.

Integration and issue completion create no package/bundle, schema/cases,
Serialization Binding, Validation Output, Portable Conformance Evidence,
Tool/Implementation, execution, evidence, aggregate result, automatic
authority, release, support, certification, hosting, deployment, or later-phase
authority.
