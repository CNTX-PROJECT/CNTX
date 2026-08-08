# CNTX Public-Core remediation evidence

This directory contains bounded, revision-pinned remediation-evidence records
created in response to Accepted assessment findings. Remediation evidence does
not rewrite an assessment, change an outcome, recommend or approve a release,
or authorize a later reassessment.

## Lifecycle and authority

A remediation dossier remains Proposed until the governed issue, exact-head
review, separate human acceptance, status promotion, and integration lifecycle
is complete. Repository presence, a passing evaluation, Draft pull-request
state, or ARCHITECT review grants no acceptance or consequential authority.

Accepted remediation means only that the exact evidence record was accepted
as a historical, attributable record. A later assessment must independently
pin its own immutable subject and evidence basis and preserve limitations,
adverse information, and unresolved conditions.

## Remediation records

| Record | Status | Frozen basis | Bounded result |
| --- | --- | --- | --- |
| [REMEDIATE-001 — ASSESS-001 Release-Readiness Remediation Evidence](assess-001-release-readiness-evidence-remediation.md) | **Accepted** | Public baseline `45663112f8e253a1748543041afa9b7064b1eabc`, tree `e5b8403f64624357b8a2f9ddcc3110c3a170c456`; Accepted ASSESS-001 subject `8e75448dd5eeb1c70fd17a71a165bf9500cccc3b` | Three gap-specific evidence records; no ASSESS-001 outcome change, aggregate result, recommendation, approval, or release authority |

## Evidence records

- [Schema Validation Reproduction Evidence](evidence/schema-validation-reproduction-evidence.md)
- [Security, Privacy, Legal, and Disclosure Review](evidence/security-privacy-legal-disclosure-review.md)
- [Publication, Compatibility, Support, and Claim Position](evidence/publication-compatibility-support-position.md)

## Separation and non-authority

Remediation, assessment, reassessment, review, acceptance, release approval,
release decision, version allocation, tagging, packaging, publication,
compatibility, support, certification, distribution, deployment, and final
human authority remain separate.

This directory supplies no Artifact Instance, canonical Portable Conformance
Evidence or Validation Output, validator, runner, API, CLI, workflow, release
record, manifest, package, supported-version claim, certification, or
implementation. It must not contain secrets, credentials, personal data,
private project context, restricted vulnerability details, production
configuration, or private implementation.
