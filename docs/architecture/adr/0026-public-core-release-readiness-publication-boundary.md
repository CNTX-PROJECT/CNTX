# ADR-0026: Public-core release readiness and publication boundary

- **Status:** Proposed
- **Date:** 2026-08-08
- **Issue:** [#78](https://github.com/CNTX-PROJECT/CNTX/issues/78)
- **Decision:** ARCH-026 — CNTX Public-Core Release Readiness and Publication Boundary

## Context

CNTX Public Core has nine Accepted artifact contracts, ten Accepted executable
Schema Resources, Core Artifact JSON Binding Version `1.0.0`, a closed Schema
Resource resolution boundary, an Accepted Validation and Validation Output
Contract, and an Accepted Portable Conformance Evidence Boundary.

ARCH-021 identifies Public-Core Release Readiness and Publication as the next
separately governed decision after portable conformance evidence. ARCH-025
intentionally does not decide release readiness, support, certification,
publication, or any release action.

Without an explicit boundary, completion of the Accepted foundation, a passing
schema evaluation, synthetic fixtures, a merged commit, repository visibility,
a favorable review, or a portable evidence set could be misrepresented as
release readiness or publication authority. A tag could be conflated with a
release, an Accepted version with a supported version, or a mutable branch with
an exact release subject. Security, privacy, legal, disclosure, documentation,
compatibility, support, limitation, and final-authority responsibilities could
also be collapsed into one automated `ready` result.

## Decision

Define a documentation-only Public-Core Release Readiness and Publication
Boundary.

Release readiness is a bounded, evidence-backed, dimension-preserving
assessment of one exact release subject against one exact frozen release basis.
It is not a universal repository property and does not itself authorize a
release or publication action.

The release subject is exact immutable included material with explicit
exclusions. The frozen basis preserves exact Accepted identities, versions,
source bindings, dependency and Schema Resource closure, validation context,
Portable Conformance Evidence, limitations, security/privacy/legal inputs,
publication conditions, and historical provenance. Mutable aliases, `latest`,
hidden state, implicit caches, automatic discovery, retrieval, or network
access cannot complete or alter it.

Every assessment keeps six dimensions separate:

1. governance and authority;
2. specification and normative sources;
3. artifact representation and Schema Resources;
4. validation and Portable Conformance Evidence;
5. security, privacy, legal, and disclosure; and
6. publication, compatibility, support, and claims.

No dimension substitutes for another, and no universal aggregate `ready`
result is defined.

For one consequential release decision, the logical release basis makes ten
responsibilities reviewable: exact subject; inclusion/exclusion; Accepted
identity/version/source closure; dependency/resource closure; documentation,
policy, license, and notice; validation and portable evidence; limitations and
unsupported or conflicting material; security/privacy/legal/disclosure;
publication/compatibility/support/change boundaries; and a separate
attributable final decision identifying any authorized actions.

These are logical responsibilities, not fields, a manifest, package,
serialization, checklist, rubric, score, threshold, quality gate, protocol,
tool, or workflow.

ARCH-024 outcomes and six conformance dimensions remain distinct. ARCH-025
portable evidence remains exactly scoped, version-bound, provenance-bearing,
offline-first, and limitation-preserving. Validation or evidence is an input to
assessment, not proof of complete readiness and not approval, certification,
release authority, or publication authority.

Missing, inaccessible, ambiguous, conflicting, mutable, wrong-version,
unsupported, restricted, materially limited, Not Satisfied, Unverifiable, Not
Evaluated, blocked, or unreproducible inputs remain visible and block positive
claims that depend on them. Favorable evidence cannot suppress adverse
evidence or limitations.

Public release material preserves least privilege, least disclosure,
minimization, provenance, public/private separation, applicable licenses and
notices, and responsible disclosure. Technical access and repository
visibility grant no authority to collect, process, disclose, publish,
distribute, or deploy material.

Readiness assessment, approval, release, release version, tag, publication,
distribution, supported-version claim, compatibility claim, certification,
and deployment remain separate. Contract Definition Version, Schema Version,
Binding Version, Artifact Revision, commit, tag, release version, publication
revision, implementation version, and support status are not interchangeable.

Publication requires a separate attributable decision identifying the exact
subject and basis, channel, audience, material, permitted claims, security and
disclosure limits, responsible actions, corrections or withdrawal boundaries,
explicit exclusions, and stop conditions. Repository presence, merge to
`main`, Accepted status, issue closure, or a hosted preview is not publication
by itself.

Evidence producer, validator, evaluator, reviewer, recommendation author,
decision maker, publisher, distributor, operator, support provider, and
EIGENAAR / Final Authority responsibilities remain separate. Majority,
consensus, lack of objection, successful automation, or technical capability
cannot replace a separately attributable final decision.

There is no latest-wins, majority, consensus, weighted vote, score, grade,
threshold, checklist result, rubric, quality gate, certification status,
optimization, ranking, or automatic conflict resolution for readiness or
authority.

Assessments, decisions, releases, publications, support claims, corrections,
withdrawals, deprecations, and supersessions remain historically attributable.
Later evidence or state does not silently overwrite or retroactively approve
an earlier record.

The repository remains unreleased and pre-alpha. This decision performs no
current-state readiness assessment, creates no supported release line, and
authorizes no release, tag, publication, distribution, support, certification,
or deployment.

## Consequences

Positive consequences:

- foundation completion cannot silently become release approval;
- readiness remains exact, version-bound, evidence-backed, and separated into
  six dimensions;
- documentation, evidence, limitations, security/privacy/legal, publication,
  compatibility, and support gaps remain visible;
- release, tag, publication, support, certification, distribution, and
  deployment remain separately governed;
- mutable aliases, hidden state, and automatic network access cannot complete
  a release basis; and
- final human authority and historical provenance remain explicit.

Tradeoffs:

- release decisions may remain unavailable when material inputs are incomplete,
  restricted, conflicting, unsupported, or Unverifiable;
- assessors must preserve exact sources, versions, evidence, limitations, and
  exclusions;
- no single metric or automation can decide readiness; and
- concrete records, tooling, channels, packaging, signing, support,
  certification, and deployment require later separate decisions.

## Alternatives rejected

- Foundation completion, merge, or repository visibility means ready or
  published: conflates architecture and repository lifecycle with release
  authority.
- One boolean, score, grade, threshold, checklist, or quality gate: collapses
  six dimensions, limitations, uncertainty, and authority.
- CI, validator, fixtures, review, or portable evidence approves release:
  evidence and automation do not grant authority.
- Majority, consensus, no objection, or a favorable recommendation decides:
  final authority must be separately attributable.
- `main`, `latest`, mutable aliases, or network discovery define the subject:
  the subject and basis must be immutable, exact, closed, and reproducible.
- Tag equals release or supported version: these are separate identities,
  actions, and claims.
- Concrete manifest, package, release record, version policy, compatibility
  matrix, support policy, signing, or publication mechanism now: the conceptual
  boundary must precede those independently governed choices.
- Assess current readiness now: creating the boundary and applying it are
  separate governed tasks.

## Security, privacy, legal, and non-authority

Release subjects, evidence, diagnostics, documentation, schemas, resources,
references, and publication inputs remain untrusted. Least privilege, least
disclosure, minimization, provenance, restricted-source boundaries,
public/private separation, and final human authority remain mandatory.

Public material must not expose secrets, credentials, personal data,
production configuration, private paths or context, restricted content,
exploitable non-public vulnerability detail, provider configuration, host or
network detail, or private implementation material.

Potential vulnerabilities remain governed by
[SECURITY](../../../SECURITY.md). Release timing cannot override responsible
disclosure. Legal, license, privacy, regulatory, and policy conclusions remain
separate reviewable claims; this decision gives no legal advice, compliance
certification, or disclosure permission.

This decision grants no truth, completeness, compatibility, support,
certification, approval, release, tag, publication, distribution, deployment,
execution, merge, issue-closure, or follow-on authority.

## Deferred scope

Deferred and unauthorized: changes to Accepted sources; current readiness
assessment or finding; release recommendation or approval; release record,
manifest, package, bill of materials, identity/version policy, or tag;
supported-version or compatibility claim; support policy; certification;
distribution; hosted publication; deployment; concrete field, schema,
manifest, media type, serialization, canonical bytes, digest, signature,
timestamp, trust, transparency, supply-chain attestation, archive, installer,
update mechanism, resolver, registry, catalog, cache, network access,
validator/publication implementation, API, CLI, runner, suite, score, badge,
rubric, checklist, quality gate, automated assessment/approval/release,
workflow, runtime, provider/product work, private/reference implementation, or
any consequential action.

## Review and continuing gate

The candidate must receive one transparent non-independent COMMENT review on
its exact head and then stop. Creation, validation, review, repository
presence, Draft state, and mergeability do not grant acceptance.

Only a later separate attributable EIGENAAR / Final Authority acceptance of
the exact reviewed candidate may authorize a status-only Proposed-to-Accepted
promotion. No promotion, Ready transition, merge, issue closure, branch
cleanup, assessment, release, tag, support claim, publication, distribution,
or deployment is authorized now.

## References

- [ARCH-026](../public-core-release-readiness-publication-boundary.md)
- [ARCH-001](../core-contract.md)
- [ARCH-002](../contract-identity-versioning.md)
- [ARCH-003](../artifact-contract-schema-architecture.md)
- [ARCH-009](../common-artifact-envelope-executable-schema.md)
- [ARCH-021](../public-core-completion-boundary-roadmap.md)
- [ARCH-022](../core-artifact-serialization-binding.md)
- [ARCH-023](../schema-resource-resolution-catalog-boundary.md)
- [ARCH-024](../validation-and-validation-output-contract.md)
- [ARCH-025](../portable-conformance-evidence-boundary.md)
- [Artifact contract index](../../contracts/README.md)
- [Schema Resource index](../../../schemas/README.md)
