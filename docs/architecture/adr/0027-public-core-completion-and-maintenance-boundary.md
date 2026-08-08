# ADR-0027: CNTX Public-Core completion and maintenance boundary

- **Status:** Accepted
- **Date:** 2026-08-08
- **Issue:** [#96](https://github.com/CNTX-PROJECT/CNTX/issues/96)
- **Decision:** ARCH-027 — CNTX Public-Core Completion and Maintenance Boundary

## Context

ARCH-021 named the completed contract-and-schema foundation and ordered five
remaining Public-Core decision layers. ARCH-022 through ARCH-026 later defined
those layers. ASSESS-001 through ASSESS-003, REMEDIATE-001 and REMEDIATE-002,
DECIDE-001, RELEASE-001, and VERIFY-001 then applied separate evidence,
decision, publication, and verification lifecycles.

CNTX Public Core `0.1.0-prealpha.1` is now an immutable GitHub prerelease of an
exact subject, and VERIFY-001 is an Accepted point-in-time verification. The
initial specification and prerelease roadmap has therefore reached a real
completion boundary.

Without a later decision, that completion could be understated as merely the
end of one task, or overstated as repository archival, a supported product, a
maintenance promise, production readiness, universal conformance, or runtime
completion. Future correction, withdrawal, release, extension, implementation,
and hosting work also needs an explicit common governance boundary.

## Decision

Record that the completed work through Accepted VERIFY-001 is named the
**completed initial CNTX Public-Core specification and prerelease cycle**.

Keep that completion distinct from:

- repository archival, locking, deletion, or total project closure;
- supported-version, maintenance, SLA, or compatibility commitments;
- security/privacy/legal/compliance certification;
- implementation, runtime, provider, product, hosted-publication, and
  deployment completion; and
- completion of optional Extension Module or Profile architecture.

Define the post-completion state as a **quiescent, event-driven maintenance
boundary**. No task, monitoring duty, support service, update cadence,
correction, withdrawal, release, or implementation is automatically active.
Future consequential work requires a new exact baseline, subject, scope,
issue/contract, evidence, attributable authority, review, validation,
acceptance, integration, completion, and any cleanup decision.

Preserve ARCH-021 as historical Accepted architecture. Record only that its
five remaining-layer categories were subsequently addressed by ARCH-022
through ARCH-026 and their separately governed application phases. Do not
rewrite ARCH-021 history or silently supersede it.

Preserve every Accepted predecessor, the exact immutable release objects,
historical issues and pull requests, evidence limitations, the public/private
boundary, and final human authority.

## Completed cycle

The completed initial cycle includes:

1. public governance and architecture through ARCH-026;
2. nine Artifact Contracts;
3. ten active Schema Versions `1.0.0` and ten synthetic test manifests;
4. nine Contract Definition identity/version/source bindings;
5. Core Artifact JSON Binding Version `1.0.0`;
6. Accepted resolution, validation/output, PCE, and release-readiness
   boundaries;
7. Accepted ASSESS-001/-002/-003 and REMEDIATE-001/-002;
8. Accepted DECIDE-001;
9. immutable prerelease publication under RELEASE-001; and
10. Accepted VERIFY-001.

## Maintenance-change classes

Future work must distinguish at least:

- normative correction;
- non-normative documentation correction;
- security or privacy correction;
- withdrawal, deprecation, and supersession;
- new assessment or release cycle;
- Extension Module or Profile architecture;
- validator, resolver, or conformance tooling;
- API, CLI, workflow, runtime, provider, or product implementation; and
- hosted publication, external distribution, or deployment.

Naming a class does not authorize it. Every consequential change requires its
own governed lifecycle and visible compatibility, security, privacy,
provenance, correction, withdrawal, and historical-integrity treatment where
applicable.

## Immutable historical boundary

Preserve without mutation:

- Release Identity `CNTX Public Core Release`;
- Release Version `0.1.0-prealpha.1`;
- lightweight tag `v0.1.0-prealpha.1` directly targeting commit
  `109e6f293b150f48572cd747fab446c141d57193`;
- release-subject tree
  `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- immutable GitHub Release ID `367290932` and node ID
  `RE_kwDOTsnR984V5Go0`;
- zero custom assets;
- historical issues #80, #92, and #94 and PRs #93 and #95; and
- the Accepted release and verification sources.

Generated archives remain derived channel representations. Their time-bound
VERIFY-001 hashes are not canonical identities, normative digests, manifests,
signatures, or attestations.

## Evidence and non-claim boundary

Completion does not resolve:

- `Unverifiable` security/privacy/legal/disclosure readiness;
- `Not Evaluated` new independent specialist evidence in VERIFY-001;
- non-independent evaluator and archive operation;
- absence of canonical PCE and Validation Output Artifact Instances;
- absence of universal validator, implementation, interoperability,
  compatibility, support, or certification claims;
- unverifiable exact archive mode and metadata preservation; or
- absence of an aggregate VERIFY-001 outcome.

`0.1.0-prealpha.1` remains unsupported pre-alpha material. This decision
creates no support policy, SLA, maintenance duration, compatibility guarantee,
production-readiness claim, security/privacy/legal/compliance certification,
fitness, warranty, or absence claim.

## Rationale

The decision recognizes substantial completed work while preserving the exact
limits of the evidence and release. A quiescent boundary prevents maintenance
from becoming an implied service and prevents technical access or repository
state from silently authorizing future changes.

Keeping implementation, runtime, provider, product, hosting, and deployment
outside the Public-Core completion claim preserves the model-, vendor-,
runtime-, provider-, product-, storage-, transport-, and domain-agnostic
foundation.

## Consequences

- The initial Public-Core specification and prerelease cycle may be described
  as complete once this exact decision is separately accepted and integrated.
- The repository may remain open and governed without an active work phase.
- No supported release line, maintenance promise, or automatic follow-on task
  exists.
- Future consequential changes have a common exact-governance gate.
- ARCH-021 remains historically correct and unchanged.
- Existing limitations, adverse/restricted evidence, and non-claims remain
  visible.

## Rejected alternatives

Rejected: declaring the entire CNTX project, every implementation, or every
possible future layer complete; archiving or locking the repository as an
automatic effect; treating prerelease publication as a support promise;
creating an indefinite maintenance obligation; treating GitHub `latest`, a
mutable alias, or latest-wins as authority; silently rewriting ARCH-021;
automatically initiating correction, withdrawal, a new release, Extension/
Profile work, implementation, hosted publication, or deployment; and treating
private orientation or technical access as authority.

## Security and privacy

No completion or maintenance label grants access, permission, disclosure,
authenticity, trust, approval, or authority. Private context, credentials,
secrets, personal data, production configuration, private paths, restricted
evidence, and private implementation details remain outside public sources.

Future work must preserve minimization, provenance, exact scope,
least-privilege access, visible limitations, and the existing disclosure
boundary.

## Non-decisions and deferred scope

This decision performs no correction, withdrawal, deprecation, supersession,
reassessment, new version, tag, Release, asset, package, manifest, custom
archive, BOM, SBOM, canonical digest, signature, attestation, certification,
support commitment, compatibility guarantee, Extension Module/Profile,
Artifact Instance, validator, resolver, registry, catalog, cache, bundler,
mirror, redirect, API, CLI, workflow, automation, runtime, provider, product,
private/reference implementation, hosted publication, distribution,
deployment, repository archival, locking, or deletion.

## Authority boundary

This ADR is Accepted. Creation authority, repository presence, validation, and
transparent non-independent ARCHITECT review did not grant acceptance.
Attributable EIGENAAR / Final Authority exact-head acceptance is recorded in
issue comment `5228459221`; separately authorized governed integration adopts
the exact decision.

Acceptance adopts only the completion and maintenance boundary. It does
not execute project closure, maintenance, correction, withdrawal,
implementation, publication, deployment, or another phase.
