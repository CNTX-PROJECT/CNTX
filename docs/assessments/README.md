# CNTX Public-Core assessments

Assessments apply fixed CNTX criteria to one exact revision and evidence basis.
Start here when you want to inspect **what was evaluated, what was observed,
and what remained uncertain** at a specific point in history.

## How this area fits

`Exact subject + evidence → separate dimension outcomes → limitations and uncertainty → separate human decision`

| Looking for… | Open… |
| --- | --- |
| The three historical assessment records | [Assessment records](#assessment-records) |
| Evidence added after an assessment gap | [Remediation evidence](../remediation/README.md) |
| Release policy, decision, publication, and verification | [Release policy](../release/README.md) |

Assessment outcomes stay dimension-specific. They do not combine into an
automatic pass/fail, score, recommendation, approval, or current universal
truth.

This directory contains bounded, version- and revision-pinned assessment
records that apply Accepted CNTX governance and architecture without replacing
their normative meaning.

## Lifecycle and authority

An assessment record identifies its exact immutable subject, evidence basis,
inclusions, exclusions, outcomes, limitations, uncertainty, adverse evidence,
review provenance, and authority boundary. It remains Proposed until separately
accepted through the governed issue, exact-head review, human decision, and
integration lifecycle.

An Accepted assessment record means only that its exact recorded assessment was
accepted as a historical, attributable evaluation. It does not make its subject
normative, approve a release, authorize an action, or create a universal current
state. Every consequential use requires freshness verification and separate
authority.

## Assessment records

| Assessment | Status | Exact subject | Bounded result |
| --- | --- | --- | --- |
| [ASSESS-001 — Initial Public-Core Release Readiness Assessment](assess-001-initial-public-core-release-readiness.md) | **Accepted** | Commit `8e75448dd5eeb1c70fd17a71a165bf9500cccc3b`, tree `6aeb56b33f09c3696d5c4dbdb7ee0a87fb4582af` | Six separate ARCH-026 readiness-dimension outcomes; no aggregate result or release authority |
| [ASSESS-002 — Second Public-Core Release Readiness Assessment](assess-002-second-public-core-release-readiness.md) | **Accepted** | Commit `ef66ab5884794ec2742478ed1f195ebb9ffeeb95`, tree `8987a2272b475faf9f091c221fd151ab85c233b9` | Four `Satisfied`, one `Unverifiable`, and one `Not Satisfied` dimension outcome; no aggregate result or release authority |
| [ASSESS-003 — Final Public-Core Release Readiness Reassessment](assess-003-final-public-core-release-readiness.md) | **Accepted** | Commit `109e6f293b150f48572cd747fab446c141d57193`, tree `446b408e27d3ebd3f6616658c61ccd9db4af8978` | Five `Satisfied` and one `Unverifiable` dimension outcome; responsibility 10 remains separately `Not Satisfied`; no aggregate result or release authority |

ASSESS-002 is Accepted under issue #84, attributable EIGENAAR / Final
Authority creation-authority comment `5226063673`, and exact-head acceptance
comment `5226177600`. It evaluates the exact new subject and Accepted
REMEDIATE-001 evidence without modifying ASSESS-001. Its Accepted status
records this exact historical assessment and grants no release authority.

ASSESS-003 is Accepted under issue #88, attributable EIGENAAR / Final
Authority creation-authority comment `5226762612`, and exact-head acceptance
comment `5226852273`. It evaluates the exact new subject and Accepted
REMEDIATE-002 decision basis without modifying either predecessor assessment
or remediation source. Its Accepted status records the exact historical
assessment and grants no aggregate readiness result, final release decision,
release action, or consequential authority.

Issue #80 remains closed and untouched. It may be reconsidered only after
ASSESS-003 is separately accepted, integrated, completed, synchronized, and
cleaned up, and only when a new attributable EIGENAAR decision authorizes that
action.

## Non-aggregate boundary

Assessment outcomes remain dimension-specific. This directory defines no
universal `ready`, pass/fail, traffic light, score, grade, badge, threshold,
checklist result, rubric, quality gate, majority, consensus, latest-wins,
ranking, or automatic conflict resolution.

Assessment, review, acceptance, release approval, release decision, version,
tag, publication, compatibility, support, certification, distribution,
deployment, implementation, and final human authority remain separate.

## Public and private boundary

Assessment records must not disclose secrets, credentials, personal data,
production configuration, private project context, restricted vulnerability
details, or private implementation. Missing or restricted evidence remains
explicitly `Unverifiable`, `Not Evaluated`, limited, or blocked rather than
being silently inferred.
