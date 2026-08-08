# DECIDE-001 — CNTX Public-Core Final Release Decision

## Status and authority

- Decision sequence: `DECIDE-001`.
- Logical Decision Identity: `CNTX Public-Core Final Release Decision`.
- Document status: **Accepted**.
- Selected disposition: **Approve**.
- EIGENAAR / Final Authority: Cintao66.
- Creation authority: issue #90 and attributable authority comment
  `5227058548`.
- Exact-head acceptance: attributable EIGENAAR / Final Authority comment
  `5227236796` on reviewed commit
  `bce48cd19bc35f4c75c8cf40b5b1a3689a5bc716` and tree
  `34435fdf39451915f04946460a67dd7fc3fdab8f`.
- Review boundary: one transparent, explicitly non-independent exact-head
  `COMMENT` review by ARCHITECT.

This Accepted document records the attributable Final Release Decision for
only the exact assessed subject. It satisfies the final-human-decision gate for
that subject and grants no authority to create or move a tag, create a GitHub
Release, publish, distribute, support, correct, withdraw, or deploy anything.
Every consequential release action remains subject to separate attributable
EIGENAAR / Final Authority authorization.

## Exact creation baseline and assessed release subject

The governing creation baseline for this Accepted record is:

- public repository: `CNTX-PROJECT/CNTX`;
- creation commit: `47eaa9f1b0a597a6b873cb0d25700115ee2acdb8`;
- creation tree: `049f5aba5f893c6fafaa1b4ac4b4db38cdd04585`;
- creation-baseline tracked files: 112.

The exact release subject assessed by Accepted ASSESS-003 is separately and
immutably pinned as:

- subject commit: `109e6f293b150f48572cd747fab446c141d57193`;
- subject tree: `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- subject tracked files: 111.

The creation baseline is not substituted for the assessed release subject.
This Accepted decision applies only to the exact subject commit and tree above.
A different or later subject requires a new exact assessment and authority
cycle.

## Governing sources

The complete governing basis is bounded to exactly these six sources:

1. Accepted [ARCH-026 Public-Core Release Readiness and Publication
   Boundary](../architecture/public-core-release-readiness-publication-boundary.md);
2. Accepted [ASSESS-003 Final Public-Core Release Readiness
   Reassessment](../assessments/assess-003-final-public-core-release-readiness.md);
3. Accepted [Public-Core Release Identity and Version
   Policy](public-core-release-identity-version-policy.md);
4. Accepted [Publication, Compatibility, Support, and Change
   Policy](publication-compatibility-support-and-change-policy.md);
5. public [Governance](../../GOVERNANCE.md); and
6. public [Security](../../SECURITY.md).

Repository presence, document status, assessment results, technical
validation, review, or access does not replace attributable final-human
authority.

## Preserved ASSESS-003 results

This Accepted decision preserves Accepted ASSESS-003 without amendment.

### Six separate readiness dimensions

| Readiness dimension | Accepted ASSESS-003 outcome |
| --- | --- |
| Governance and authority readiness | `Satisfied` |
| Specification and normative-source readiness | `Satisfied` |
| Artifact representation and Schema Resource readiness | `Satisfied` |
| Validation and Portable Conformance Evidence readiness | `Satisfied` |
| Security, privacy, legal, and disclosure readiness | `Unverifiable` |
| Publication, compatibility, support, and claim readiness | `Satisfied` |

### Ten separate release-basis responsibilities

| Responsibility | Accepted ASSESS-003 outcome before an Accepted decision |
| --- | --- |
| 1 | `Satisfied` |
| 2 | `Satisfied` |
| 3 | `Satisfied` |
| 4 | `Satisfied` |
| 5 | `Satisfied` |
| 6 | `Satisfied` |
| 7 | `Satisfied` |
| 8 | `Unverifiable` |
| 9 | `Satisfied` |
| 10 — separate attributable final-human decision | `Not Satisfied` |

There is no aggregate readiness result, pass/fail, traffic light, score,
grade, badge, threshold, checklist verdict, rubric, quality gate, ranking,
majority, consensus, latest-wins result, recommendation, approval, or automatic
decision. Accepted ASSESS-003 remains unchanged, including its responsibility
10 outcome. The attributable Accepted Final Release Decision separately
satisfies responsibility 10 for only the exact subject identified above.

## Preserved validation and Portable Conformance Evidence basis

The complete Accepted REMEDIATE-001 evidence basis remains unchanged:

- all 203 synthetic cases are unchanged;
- 38 cases are expected valid and 165 are expected invalid;
- Python `jsonschema 4.26.0` produced 203/203 expected-result matches;
- Ajv `8.20.0` produced 203/203 expected-result matches;
- there were zero unexpected results and zero cross-evaluator validity
  mismatches;
- evaluation used the exact caller-supplied ten-Schema-Resource context;
- no automatic network resolution, hidden cache, mutable alias, coercion,
  defaulting, repair, or fallback was used; and
- the complete case ledger and evaluator, runtime, dependency, configuration,
  command, harness, and result-hash provenance remain preserved.

ARCHITECT operated both implementation-diverse evaluators in one environment.
The evidence therefore is not independent human reproduction. It creates no
canonical Portable Conformance Evidence Artifact Instance, canonical
Validation Output, portable diagnostic vocabulary, universal validator or
Artifact Instance conformance, implementation conformance, interoperability
claim, certification, accreditation, score, grade, badge, or quality gate.

## Adverse evidence, limitations, and restricted evidence

The Accepted REMEDIATE-002 and ASSESS-003 boundaries remain visible:

- no code-scanning analysis was available;
- no independent security, privacy, or legal specialist review was performed;
- private-vulnerability content was not available for public assessment;
- repository settings are mutable, time-bound platform observations rather
  than immutable normative proof;
- GitHub Actions, Dependabot security updates, non-provider-pattern scanning,
  and validity checks were disabled in the recorded observation;
- no penetration test, legal review service, external scanner, or private
  evidence review was performed; and
- no legal-completeness, compliance, security, privacy, production-readiness,
  fitness, warranty, or absence proof exists.

Restricted or unavailable evidence is not treated as favorable evidence.
Missing, adverse, conflicting, uncertain, or materially limited evidence is
not suppressed by other positive results.

## Accepted disposition — Approve

The EIGENAAR approves only the exact assessed subject for an unsupported
pre-alpha release under this bounded basis:

- Release Identity: `CNTX Public Core Release`;
- selected Release Version: `0.1.0-prealpha.1`;
- intended tag representation: `v0.1.0-prealpha.1`;
- intended later channel: one future separately authorized GitHub Release in
  `CNTX-PROJECT/CNTX`, marked as prerelease;
- intended audience: review and experimentation; and
- support posture: unsupported pre-alpha.

The word **Approve** in this Accepted record is the attributable Final Release
Decision for only the exact assessed subject. It has no direct consequential
release-execution effect.

Governed integration of this exact Accepted decision establishes that:

1. the integrated decision becomes the attributable Final Release Decision for
   only the exact assessed subject;
2. responsibility 10 becomes satisfied for only that subject;
3. the security/privacy/legal/disclosure dimension remains `Unverifiable` and
   is not converted to `Satisfied`;
4. Release Version `0.1.0-prealpha.1` is selected for that subject;
5. `v0.1.0-prealpha.1` is fixed as its intended tag representation; and
6. only preparation of a separate RELEASE-001 execution contract becomes an
   eligible next phase.

Acceptance and integration of DECIDE-001 do not create or move a tag,
create a GitHub Release, create a release record, publish, distribute, support,
correct, withdraw, or deploy anything.

## Prospective publication-set boundary

The bounded prospective publication set contains only:

1. one immutable Git tag on the exact assessed subject;
2. one GitHub Release record marked prerelease;
3. hosting-platform-generated source archives associated with that tag; and
4. release notes that identify the exact subject, version, tag, channel,
   unsupported posture, limitations, non-claims, responsible-disclosure
   guidance, and correction/withdrawal boundaries.

It excludes custom assets, packages, manifests, archives beyond the hosting-
platform-generated source archives, BOMs, SBOMs, digests, signatures,
attestations, installers, registry publications, hosted sites, mutable
`latest` aliases, runtimes, support services, and deployments.

## Compatibility, support, and claim boundary

This Accepted decision makes no universal, prior-version, future-version,
implementation, interoperability, or support-compatibility guarantee. It
creates no supported-version claim, SLA, maintenance duration, response
target, warranty, certification, accreditation, compliance statement,
production-readiness claim, or support service.

The release remains explicitly prospective, pre-alpha, unstable, unsupported,
and intended for review and experimentation. No consumer reliance or fitness
for a particular purpose is established.

## Security, privacy, legal, and disclosure boundary

The `Unverifiable` outcome is preserved exactly. This Accepted approval is a
bounded human decision under visible limitations; it does not
assert that security, privacy, legal, disclosure, compliance, or absence-of-
findings requirements are universally or independently satisfied.

Responsible disclosure remains governed by the public Security source.
Public records must not disclose private vulnerability content, secrets,
credentials, personal data, production configuration, or restricted evidence.

## Issue #80 historical disposition

Issue #80 has been reconsidered after completed ASSESS-002 and ASSESS-003. It
remains historical `closed/not_planned` with exactly four existing comments.
It is not reopened, commented on, replaced, edited, relabeled, or otherwise
mutated. DECIDE-001 is a new authority surface and does not retroactively
reactivate the terminated umbrella.

## Correction, withdrawal, and immutable history

Any later correction or withdrawal must be additive, attributable, scoped to
an exact immutable release subject, and separately authorized. It must not
rewrite Accepted assessments, evidence, decisions, tags, release records, or
historical limitations to appear as though an earlier state never existed.

No correction, withdrawal, tag mutation, release-record mutation, or support
action is authorized by this Accepted decision.

## Non-execution and authority separation

Creation, validation, repository presence, a clean review, acceptance, or
integration of this decision is separate from release execution. This
decision creates no Artifact Instance, Decision Record Artifact Instance,
canonical Portable Conformance Evidence, canonical Validation Output, schema,
field model, serialization, media type, canonical JSON, digest, signature,
attestation, validator, resolver, registry, catalog, cache, bundler, API, CLI,
workflow, automation, implementation, runtime, provider or product work,
package, manifest, BOM, SBOM, certification, publication, distribution,
support service, correction, withdrawal, or deployment.

No technical actor, evaluator, reviewer, automation, majority, consensus, or
repository state may substitute for the EIGENAAR / Final Authority.

## Accepted decision and release-execution gate

The exact reviewed candidate received attributable EIGENAAR / Final Authority
acceptance in comment `5227236796`. Governed integration establishes this
record as the Accepted Final Release Decision for only the exact assessed
subject and makes preparation of a separate RELEASE-001 execution contract the
next eligible candidate phase.

This Accepted decision does not execute RELEASE-001 and authorizes no direct
tag creation or movement, GitHub Release, release record, publication,
distribution, implementation, support, correction, withdrawal, VERIFY-001,
ARCH-027, or deployment. Each such phase or action remains separately gated.
