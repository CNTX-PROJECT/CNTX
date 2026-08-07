# ADR-0025: Portable conformance evidence boundary

- **Status:** Proposed
- **Date:** 2026-08-08
- **Issue:** [#76](https://github.com/CNTX-PROJECT/CNTX/issues/76)
- **Decision:** ARCH-025 — CNTX Portable Conformance Evidence Boundary

## Context

CNTX Public Core has nine Accepted artifact contracts, ten Accepted executable
Schema Resources, Core Artifact JSON Binding Version `1.0.0`, a closed Schema
Resource resolution boundary, and an Accepted Validation and Validation Output
Contract. ARCH-024 defines frozen governing context, six separate conformance
dimensions, phase outcomes, diagnostics, limitations, fail-closed behavior,
and future output responsibilities, but intentionally defines no Portable
Conformance Evidence or Conformance Claim artifact.

ARCH-021 requires a separate Portable Conformance Evidence Boundary before
release-readiness claims about interoperability or implementation conformance.
ARCH-003 already defines a Conformance Claim as Evidentiary and non-
authoritative. CONTRACT-006 and ARCH-017 define the canonical Evidence Bundle,
but artifact/schema conformance does not make any bundle automatically
sufficient for a conformance claim.

Without a separate boundary, one successful schema evaluation, validation
output, fixture, self-attestation, bundle, or tool result could be generalized
beyond its exact subject, versions, requirements, capabilities, environment,
limitations, or evidence coverage. Hidden state, `latest`, network retrieval,
favorable-evidence selection, scores, or unresolved conflicts could also
silently define portability or certification.

## Decision

Define a documentation-only Portable Conformance Evidence Boundary.

Portable Conformance Evidence is a bounded, provenance-bearing logical
evidence set that enables an independent consumer to assess one or more exactly
scoped Conformance Claims against exact Accepted requirements and versions,
using disclosed governing context and limitations, without hidden private
implementation state, mutable aliases, automatic network access, or an
authority inference.

Logical portability means interpretable and reassessable from supplied
evidence and exact offline governing sources. It does not require identical
bytes, one format or package, automatic retrieval, authenticity, integrity,
trust, certification, approval, release readiness, or unrestricted disclosure.

Every consequential claim identifies its exact subject/revision or supplied-
representation boundary, separately claimed conformance dimensions, exact
Contract/Schema/Binding/resource/source versions, scope and exclusions,
claimant boundary, and self-attested/reproduced/reviewed status.

The evidence set supports twelve logical responsibility categories: exact
claim and subject; conformance dimensions; governing pins; frozen ARCH-024
context; all phase outcomes; failures/diagnostics/limitations; evaluator
capabilities and material conditions; evidence-item provenance and treatment;
claim/evidence/requirement traceability; coverage/gaps/adverse evidence;
reproduction boundaries and results; and security/privacy/disclosure
limitations. These are not concrete fields or a serialization.

Evidence may conceptually support, qualify, contradict, or show insufficient
support for a claim. Unfavorable, missing, blocked, Unverifiable, Not
Evaluated, adverse, contradictory, or restricted evidence remains visible.
Copies and transformations do not become independent corroboration. Conflicts
remain explicit; there is no latest-wins, majority, consensus, score, rank, or
automatic resolution.

An ARCH-024 validation output may be necessary evidence but is not a complete
portable evidence set. Evidence Bundle, validation output, Portable
Conformance Evidence, Conformance Claim, Review Record, Decision Record,
certification, and release record remain separate.

Consumers use exact governing sources supplied under existing offline-first
boundaries. Hidden state, mutable aliases, implicit caches, automatic
discovery/retrieval/network, and undeclared environment assumptions cannot
support a positive portable claim. Missing, inaccessible, ambiguous,
conflicting, wrong-version, unsupported, or restricted material evidence makes
the affected claim limited, unsupported, or Unverifiable.

Reproduction preserves material inputs, governing context, capabilities,
method, environment, limitations, and deviations. A reproduced result is new
evidence, not retroactive proof or replacement. No canonical bytes, digest,
signature, timestamp, authenticity, integrity, chain-of-custody, or trust
mechanism is selected.

The six ARCH-024 conformance dimensions remain separate. Normative-contract
evidence addresses non-schema requirements; schema evidence remains exact-
resource/context-bound; Artifact Instance and binding evidence remain exact-
revision/version-bound; validator and implementation evidence require declared
applicable responsibility and capability scopes. One run, fixture, manifest,
self-attestation, validator, or implementation cannot certify a broader scope.

Claimant, evidence producer, evaluator, reproducer, reviewer, decision maker,
and EIGENAAR / Final Authority responsibilities remain separate contextual
responsibilities, not new canonical roles. Evidence, reproduction, and review
grant no approval, authority, certification, release, publication, or
deployment.

Evidence changes and corrections remain provenance-distinguishable. Later
evidence does not silently overwrite or retroactively authorize earlier
claims, reviews, decisions, or actions.

## Consequences

Positive consequences:

- conformance claims remain exactly scoped and version-bound;
- validation output remains usable within a larger evidence boundary;
- non-schema responsibilities, coverage gaps, adverse evidence, and
  limitations stay visible;
- independent assessment does not depend on hidden state or automatic network
  access;
- reproduction and conflict remain provenance-preserving; and
- evidence, review, decision, certification, release, and authority remain
  distinct.

Tradeoffs:

- positive claims may remain unavailable with incomplete, restricted,
  unsupported, or unreproducible evidence;
- consumers must receive exact governing sources and sufficient context;
- one passing validation run is not universally sufficient; and
- concrete formats, tools, suites, certification, and release decisions remain
  later work.

## Alternatives rejected

- Validation output alone: insufficient claim scope, coverage, provenance,
  adverse evidence, reproduction, and disclosure context.
- Schema success proves complete conformance: non-schema requirements remain.
- Evidence Bundle conformance proves sufficient portable evidence: artifact
  conformance and evidence sufficiency remain separate.
- All evidence embedded: conflicts with least disclosure and restricted-source
  boundaries.
- Hidden cache, `latest`, or automatic retrieval: weakens exact versioning,
  reproducibility, determinism, privacy, and failure attribution.
- Score, badge, threshold, or certification: collapses distinct dimensions,
  scopes, evidence quality, uncertainty, and authority.
- One run or self-attestation certifies a validator/implementation: coverage
  and independence remain unproven.
- Automatic evidence conflict resolution: requires separate review or decision
  authority.
- Concrete protocol, schema, suite, API, or CLI now: the conceptual boundary
  must precede those independently governed choices.

## Security, privacy, and non-authority

Evidence, claims, outputs, schemas, resources, diagnostics, references, and
reproduction materials remain untrusted input. Least privilege, least
disclosure, minimization, provenance, restricted-source boundaries, and
public/private separation remain mandatory.

Technical access grants no collection, retention, processing, disclosure, or
publication authority. Public content must not expose secrets, credentials,
personal data, production configuration, private paths/context, restricted
content, provider configuration, or private implementation details.

Redaction, sanitization, omission, aggregation, or restricted availability
remains visible and cannot silently create support or success. When necessary
evidence cannot be disclosed or reassessed, the affected claim remains
limited, unsupported, or Unverifiable.

Portable evidence grants no truth, completeness, authenticity, integrity,
trust, approval, acceptance, decision, authority, permission, execution,
merge, certification, release, publication, or deployment.

## Deferred scope

Deferred and unauthorized: changes to Accepted sources; Artifact Instance;
Evidence Bundle instance; Portable Conformance Evidence instance; Conformance
Claim artifact; identifier/version allocation; concrete fields, schema,
manifest, package, media type, serialization, or canonical JSON; portable
diagnostic/support vocabulary; validator, API, CLI, test runner, suite,
fixture expansion, coverage threshold, score, grade, badge, certification,
accreditation, compliance service, compatibility matrix, supported-version
claim, release-readiness decision, resolver/registry/catalog/cache/bundler/
network implementation, digest, canonicalization, signature, verification,
encryption, timestamp service, trust store, chain of custody, automated
collection/search/ranking/corroboration/conflict resolution, redaction/access/
retention mechanisms, workflow, runtime, provider/product work,
private/reference implementation, release, tag, publication, or deployment.

## Review and continuing gate

The candidate requires one transparent non-independent COMMENT review on its
exact head and then stops. Creation, validation, review, repository presence,
Draft state, and mergeability do not grant acceptance.

Only later separate attributable EIGENAAR / Final Authority acceptance of the
exact reviewed candidate may authorize status-only promotion. This proposal
authorizes no Ready transition, promotion, merge, issue closure, branch
cleanup, release-readiness decision, implementation, release, publication,
deployment, or later roadmap layer.

## References

- [ARCH-025](../portable-conformance-evidence-boundary.md)
- [ARCH-003](../artifact-contract-schema-architecture.md)
- [ARCH-008](../common-artifact-envelope-schema-composition-packaging.md)
- [ARCH-017](../evidence-bundle-executable-schema.md)
- [ARCH-021](../public-core-completion-boundary-roadmap.md)
- [ARCH-022](../core-artifact-serialization-binding.md)
- [ARCH-023](../schema-resource-resolution-catalog-boundary.md)
- [ARCH-024](../validation-and-validation-output-contract.md)
- [CONTRACT-006](../../contracts/evidence-bundle-contract.md)
