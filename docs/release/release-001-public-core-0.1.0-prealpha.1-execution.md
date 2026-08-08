# RELEASE-001 — CNTX Public Core 0.1.0-prealpha.1 Publication Execution

## Status and authority

- Execution sequence: `RELEASE-001`.
- Logical execution identity: `CNTX Public Core 0.1.0-prealpha.1 Publication`.
- Document status: **Accepted**.
- Public repository: `CNTX-PROJECT/CNTX`.
- Governing issue: [#92](https://github.com/CNTX-PROJECT/CNTX/issues/92).
- Attributable EIGENAAR / Final Authority creation comment: `5227437332`.
- Exact-head acceptance comment: `5227815201`, accepting reviewed commit
  `0b5aeae93d4e46e7110d307772e867c12d6db8f5` and tree
  `3c3a9a5d1e3c16bed7e77fffe9a740f4b758e924`.
- Review boundary: one transparent, explicitly non-independent exact-head
  `COMMENT` review by ARCHITECT.

This document defines a bounded future publication transaction. Its Accepted
status, repository presence, validation, review, or later integration does not
execute that transaction. Immutable releases remain disabled, the intended tag
is absent, and no GitHub Release exists during candidate creation and review.

## Exact creation baseline and release subject

The documentation candidate is prepared on exactly:

- creation baseline commit:
  `aadd93129686dc910f2241e535b06671c6ffa663`;
- creation baseline tree:
  `ce178b75af0584d6c0ec6212f8ec9eddd074036d`; and
- creation-baseline tracked files: 113.

The separately assessed and approved release subject is immutably pinned as:

- subject commit: `109e6f293b150f48572cd747fab446c141d57193`;
- subject tree: `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- subject tracked paths: 111; and
- complete path-inventory SHA-256:
  `A8C70DED3596BD4F74F3FDC24B1806A97B53361394BE611C065B1C90F9869BBE`.

The documentation baseline is not the release subject. A future tag must point
directly to the exact subject commit above. The RELEASE-001 documentation
created after that subject is governance and execution evidence and is not
silently added to the 111-path release source tree.

## Governing Accepted basis

This execution plan is subordinate to and preserves:

1. Accepted [ARCH-026 Public-Core Release Readiness and Publication
   Boundary](../architecture/public-core-release-readiness-publication-boundary.md);
2. Accepted [ASSESS-003 Final Public-Core Release Readiness
   Reassessment](../assessments/assess-003-final-public-core-release-readiness.md);
3. Accepted REMEDIATE-001 [validation reproduction
   evidence](../remediation/evidence/schema-validation-reproduction-evidence.md);
4. Accepted REMEDIATE-002 [security, privacy, legal, and disclosure due
   diligence](../remediation/evidence/security-privacy-legal-disclosure-due-diligence.md);
5. Accepted [Public-Core Release Identity and Version
   Policy](public-core-release-identity-version-policy.md);
6. Accepted [Publication, Compatibility, Support, and Change
   Policy](publication-compatibility-support-and-change-policy.md);
7. Accepted [DECIDE-001 Final Release
   Decision](decide-001-public-core-final-release-decision.md), disposition
   `Approve` only for the exact subject;
8. public [Governance](../../GOVERNANCE.md); and
9. public [Security](../../SECURITY.md).

Nothing in this plan changes an Accepted source, assessment outcome, evidence
record, limitation, or authority boundary.

## Selected release identity and channel

- Release Identity: `CNTX Public Core Release`.
- Release Version: `0.1.0-prealpha.1`.
- Lightweight tag: `v0.1.0-prealpha.1`.
- Git reference: `refs/tags/v0.1.0-prealpha.1`.
- Exact tag target: `109e6f293b150f48572cd747fab446c141d57193`.
- GitHub Release title: `CNTX Public Core 0.1.0-prealpha.1`.
- Repository: `CNTX-PROJECT/CNTX`.
- Release flags: `draft=false`, `prerelease=true`, `latest=false`.
- Release body source:
  [`docs/release/releases/0.1.0-prealpha.1.md`](releases/0.1.0-prealpha.1.md).

The release is unsupported pre-alpha material for review and experimentation.
It creates no supported line, compatibility guarantee, production-readiness
claim, certification, warranty, service level, or deployment.

## Exact prospective publication set

Only these channel objects are in scope for later separately authorized
execution:

1. one lightweight Git tag on the exact subject commit;
2. one immutable GitHub Release record for the verified pre-existing tag;
3. the hosting-platform-generated `.zip` and `.tar.gz` source archives for
   that tag; and
4. the exact reviewed Markdown release body from the path named above.

The generated archives are derived channel representations. They are not new
normative sources and do not expand the exact 111-path subject.

Explicitly excluded are custom assets, custom archives, packages, manifests,
BOMs, SBOMs, digests, signatures, attestations, installers, registries,
mirrors, hosted sites, discussions, mutable `latest` aliases, support services,
correction or withdrawal actions, runtimes, and deployments.

## Frozen preconditions for later execution

Every precondition must be established again immediately before a later
authorized execution. Historical observations in this Accepted document do
not satisfy that future check.

1. Local, remote-tracking, remote, and GitHub `main` must equal the exact
   integrated Accepted RELEASE-001 documentation head authorized at that time.
2. The integrated execution and release-notes files must be byte-equal to the
   exact reviewed and Accepted candidate except for the authorized status-only
   promotion.
3. Subject commit and tree must resolve to the exact pinned objects.
4. `refs/tags/v0.1.0-prealpha.1` must be absent locally and remotely.
5. A GitHub Release for `v0.1.0-prealpha.1` must be absent.
6. The repository must have zero conflicting release or tag object.
7. Immutable releases must still be disabled before their separately
   authorized enablement.
8. Repository identity, authentication scope, issue state, PR integration,
   ruleset, and all non-action boundaries must match the execution authority.
9. The release body must be read from the exact integrated Accepted source,
   without generated notes, substitution, templating, or transformation.
10. No private, restricted, secret, credential, personal, vulnerability, local
    path, or provider-private material may be present.

Any mismatch stops the transaction before mutation.

## Later execution sequence — not authorized by this candidate

The following commands are a reviewed prospective sequence, not current
authority. Exact-head EIGENAAR / Final Authority acceptance must separately
authorize every consequential step before use.

### 1. Enable and verify repository-wide immutable releases

Prospective mutation:

```powershell
gh api --method PUT repos/CNTX-PROJECT/CNTX/immutable-releases
```

Required immediate read-back:

```powershell
gh api repos/CNTX-PROJECT/CNTX/immutable-releases
```

The returned state must report `enabled=true`. If it does not, stop. This plan
grants no authority to disable the setting later.

### 2. Create exactly one lightweight tag reference

Prospective mutation:

```powershell
gh api --method POST repos/CNTX-PROJECT/CNTX/git/refs `
  -f ref='refs/tags/v0.1.0-prealpha.1' `
  -f sha='109e6f293b150f48572cd747fab446c141d57193'
```

Required immediate read-back:

```powershell
gh api repos/CNTX-PROJECT/CNTX/git/ref/tags/v0.1.0-prealpha.1
```

The reference must be exactly `refs/tags/v0.1.0-prealpha.1`; its object type
must be `commit`; and its object SHA must be the exact subject commit. No
annotated tag object, alternate target, force update, movement, or deletion is
allowed.

### 3. Create exactly one GitHub prerelease

Prospective mutation from the synchronized Accepted documentation worktree:

```powershell
gh release create v0.1.0-prealpha.1 `
  --repo CNTX-PROJECT/CNTX `
  --verify-tag `
  --title 'CNTX Public Core 0.1.0-prealpha.1' `
  --notes-file 'docs/release/releases/0.1.0-prealpha.1.md' `
  --prerelease `
  --latest=false
```

There is no Draft Release intermediate state, no generated notes, no asset
argument, and no implicit tag creation.

### 4. Read back the complete publication state

At minimum, later verification must read and record:

- immutable-releases state;
- tag ref name, object type, and target SHA;
- release database ID and immutable URL;
- release tag, target, title, and exact body bytes;
- `draft`, `prerelease`, and `latest` state;
- creation and publication timestamps as observed channel evidence;
- author identity as channel provenance, not release authority;
- asset count exactly zero;
- generated source archive URLs;
- exact subject commit/tree and 111-path inventory proof;
- issue, authority, PR, integrated documentation commit/tree, and execution
  provenance; and
- preserved unsupported and non-claim boundaries.

## Partial failure and no-rollback boundary

Every unexpected state, response, timeout, race, moved head, existing object,
wrong target, disabled immutable setting, body mismatch, flag mismatch, extra
asset, or partial result causes an immediate stop with observable state
preserved.

Without new attributable authority there is no automatic retry, tag movement,
tag deletion, alternate tag, Release edit or deletion, immutable-setting
disablement, alternate subject, correction, withdrawal, or improvised rollback.
A partial result must be reported exactly and may require a new decision.

## Evidence and limitation preservation

Accepted REMEDIATE-001 remains the bounded validation/PCE basis:

- 203 unchanged synthetic cases, 38 expected valid and 165 expected invalid;
- 203/203 expected-result matches for Python `jsonschema 4.26.0`;
- 203/203 expected-result matches for Ajv `8.20.0`;
- zero unexpected results and zero cross-evaluator validity mismatches;
- exact caller-supplied ten-resource context and no automatic network
  resolution; and
- complete case ledger and evaluator/runtime/configuration/harness/result-hash
  provenance.

ARCHITECT operated both implementation-diverse evaluators in one environment.
There was no independent human reproduction. The evidence creates no canonical
Portable Conformance Evidence Artifact Instance, canonical Validation Output,
universal validator or Artifact Instance conformance, implementation
conformance, interoperability claim, certification, or accreditation.

Accepted REMEDIATE-002 and ASSESS-003 limitations remain visible: no
code-scanning analysis, independent security/privacy/legal specialist review,
penetration test, legal-completeness proof, or public access to private
vulnerability content exists. Mutable repository settings are time-bound
platform evidence. Responsibility 8 and security/privacy/legal/disclosure
remain `Unverifiable`.

## Security, privacy, support, and claims

The public [Security policy](../../SECURITY.md) remains the responsible-
disclosure route. It is not a support channel and creates no remediation-time
commitment. Private vulnerability details, secrets, credentials, personal
data, production configuration, and restricted evidence must not enter public
release objects.

This publication plan makes no supported-version, compatibility, maintenance,
response-time, service-level, production-readiness, security, privacy, legal,
compliance, reliability, performance, availability, fitness, warranty,
certification, accreditation, or absence claim.

## Correction, withdrawal, and historical integrity

A later correction or withdrawal is a separate attributable lifecycle. It must
preserve the original subject, tag, Release record, notes, limitations, and
channel evidence and must not rewrite history. This RELEASE-001 plan authorizes
no correction, withdrawal, tag mutation, Release mutation, mirror action, or
exceptional security removal.

## Candidate validation and lifecycle stop

Before exact-head review, validation must prove exact five-path scope, one
candidate commit, expected repository inventory `115/89/20`, unchanged
architecture/ADR/contract/schema/test inventory `26/26/9/10/10`, all JSON
parseable, 203-case `38/165` preservation, schema-reference counts
`957/948/9`, exact protected Git objects, complete path appendix, valid
relative Markdown links, UTF-8 without BOM, final LF, mode `100644`, targeted
public-safety scans, exact GitHub read-back, zero tags, zero Releases, disabled
immutable releases, unchanged ruleset `20518984`, and unchanged issue #80.

After exactly one transparent non-independent COMMENT review on the exact
candidate head, work stops for separate attributable EIGENAAR / Final
Authority acceptance. No Ready transition, Accepted promotion, merge, issue
closure, branch cleanup, setting mutation, tag, GitHub Release, publication,
distribution, `VERIFY-001`, `ARCH-027`, implementation, hosted publication, or
deployment is authorized by this Accepted plan alone.

## Appendix A — exact 111-path release-subject inventory

The following code block is the complete ordinally sorted UTF-8/LF path
inventory for commit `109e6f293b150f48572cd747fab446c141d57193` and tree
`446b408e27d3ebd3f6616658c61ccd9db4af8978`. Including one final LF, it is
5752 bytes and has SHA-256
`A8C70DED3596BD4F74F3FDC24B1806A97B53361394BE611C065B1C90F9869BBE`.

```text
.github/CODEOWNERS
.github/ISSUE_TEMPLATE/bug_report.yml
.github/ISSUE_TEMPLATE/config.yml
.github/ISSUE_TEMPLATE/feature_request.yml
.github/PULL_REQUEST_TEMPLATE.md
AGENTS.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
GOVERNANCE.md
LICENSE
NOTICE
README.md
SECURITY.md
docs/architecture/README.md
docs/architecture/adr/0001-public-core-boundaries.md
docs/architecture/adr/0002-contract-identity-versioning.md
docs/architecture/adr/0003-artifact-contract-schema-layering.md
docs/architecture/adr/0004-common-artifact-envelope-schema-boundary.md
docs/architecture/adr/0005-common-artifact-envelope-representation-boundary.md
docs/architecture/adr/0006-common-artifact-envelope-schema-identity-version-policy.md
docs/architecture/adr/0007-common-artifact-envelope-schema-language-dialect.md
docs/architecture/adr/0008-common-artifact-envelope-schema-composition-packaging.md
docs/architecture/adr/0009-common-artifact-envelope-executable-schema.md
docs/architecture/adr/0010-artifact-specific-schema-family-container-boundary.md
docs/architecture/adr/0011-contract-definition-identity-version-binding.md
docs/architecture/adr/0012-project-charter-executable-schema.md
docs/architecture/adr/0013-workstream-executable-schema.md
docs/architecture/adr/0014-task-contract-executable-schema.md
docs/architecture/adr/0015-context-packet-executable-schema.md
docs/architecture/adr/0016-execution-result-executable-schema.md
docs/architecture/adr/0017-evidence-bundle-executable-schema.md
docs/architecture/adr/0018-review-record-executable-schema.md
docs/architecture/adr/0019-decision-record-executable-schema.md
docs/architecture/adr/0020-state-snapshot-executable-schema.md
docs/architecture/adr/0021-public-core-completion-boundary-roadmap.md
docs/architecture/adr/0022-core-artifact-serialization-binding.md
docs/architecture/adr/0023-schema-resource-resolution-catalog-boundary.md
docs/architecture/adr/0024-validation-and-validation-output-contract.md
docs/architecture/adr/0025-portable-conformance-evidence-boundary.md
docs/architecture/adr/0026-public-core-release-readiness-publication-boundary.md
docs/architecture/artifact-contract-schema-architecture.md
docs/architecture/artifact-specific-schema-family-container-boundary.md
docs/architecture/common-artifact-envelope-executable-schema.md
docs/architecture/common-artifact-envelope-representation-boundary.md
docs/architecture/common-artifact-envelope-schema-boundary.md
docs/architecture/common-artifact-envelope-schema-composition-packaging.md
docs/architecture/common-artifact-envelope-schema-identity-version-policy.md
docs/architecture/common-artifact-envelope-schema-language-dialect.md
docs/architecture/context-packet-executable-schema.md
docs/architecture/contract-definition-identity-version-binding.md
docs/architecture/contract-identity-versioning.md
docs/architecture/core-artifact-serialization-binding.md
docs/architecture/core-contract.md
docs/architecture/decision-record-executable-schema.md
docs/architecture/evidence-bundle-executable-schema.md
docs/architecture/execution-result-executable-schema.md
docs/architecture/portable-conformance-evidence-boundary.md
docs/architecture/project-charter-executable-schema.md
docs/architecture/public-core-completion-boundary-roadmap.md
docs/architecture/public-core-release-readiness-publication-boundary.md
docs/architecture/review-record-executable-schema.md
docs/architecture/schema-resource-resolution-catalog-boundary.md
docs/architecture/state-snapshot-executable-schema.md
docs/architecture/task-contract-executable-schema.md
docs/architecture/validation-and-validation-output-contract.md
docs/architecture/workstream-executable-schema.md
docs/assessments/README.md
docs/assessments/assess-001-initial-public-core-release-readiness.md
docs/assessments/assess-002-second-public-core-release-readiness.md
docs/contracts/README.md
docs/contracts/context-packet-contract.md
docs/contracts/decision-record-contract.md
docs/contracts/evidence-bundle-contract.md
docs/contracts/execution-result-contract.md
docs/contracts/project-charter-contract.md
docs/contracts/review-record-contract.md
docs/contracts/state-snapshot-contract.md
docs/contracts/task-contract-artifact-contract.md
docs/contracts/workstream-contract.md
docs/release/README.md
docs/release/public-core-release-identity-version-policy.md
docs/release/publication-compatibility-support-and-change-policy.md
docs/remediation/README.md
docs/remediation/assess-001-release-readiness-evidence-remediation.md
docs/remediation/assess-002-release-decision-basis-remediation.md
docs/remediation/evidence/publication-compatibility-support-position.md
docs/remediation/evidence/schema-validation-reproduction-evidence.md
docs/remediation/evidence/security-privacy-legal-disclosure-due-diligence.md
docs/remediation/evidence/security-privacy-legal-disclosure-review.md
schemas/README.md
schemas/common-artifact-envelope/1.0.0/schema.json
schemas/context-packet/1.0.0/schema.json
schemas/decision-record/1.0.0/schema.json
schemas/evidence-bundle/1.0.0/schema.json
schemas/execution-result/1.0.0/schema.json
schemas/project-charter/1.0.0/schema.json
schemas/review-record/1.0.0/schema.json
schemas/state-snapshot/1.0.0/schema.json
schemas/task-contract/1.0.0/schema.json
schemas/workstream/1.0.0/schema.json
tests/schemas/common-artifact-envelope/1.0.0/cases.json
tests/schemas/context-packet/1.0.0/cases.json
tests/schemas/decision-record/1.0.0/cases.json
tests/schemas/evidence-bundle/1.0.0/cases.json
tests/schemas/execution-result/1.0.0/cases.json
tests/schemas/project-charter/1.0.0/cases.json
tests/schemas/review-record/1.0.0/cases.json
tests/schemas/state-snapshot/1.0.0/cases.json
tests/schemas/task-contract/1.0.0/cases.json
tests/schemas/workstream/1.0.0/cases.json
```
