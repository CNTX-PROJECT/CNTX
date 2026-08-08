# VERIFY-001 — CNTX Public Core 0.1.0-prealpha.1 post-publication verification

## Document status and authority

- Document status: **Accepted** under issue #94 and attributable EIGENAAR /
  Final Authority exact-head acceptance comment `5228226589`.
- Verification identifier: `VERIFY-001`.
- Public issue: [#94](https://github.com/CNTX-PROJECT/CNTX/issues/94).
- Attributable EIGENAAR / Final Authority creation comment:
  [`5228074838`](https://github.com/CNTX-PROJECT/CNTX/issues/94#issuecomment-5228074838).
- Created and technically reviewed by: `ARCHITECT`.
- Independence: not independent. The same ARCHITECT operated the read-only
  retrieval and comparison procedure and prepared this record.

This record is a documentation-only, point-in-time verification of an already
published channel representation. It is not an assessment, release approval,
certification, support claim, compatibility guarantee, correction,
withdrawal, or new publication authority.

## Frozen verification context

| Responsibility | Exact value |
| --- | --- |
| Repository | `CNTX-PROJECT/CNTX` |
| Creation baseline commit | `6304b3f047cf60e35c09b229467f53b62f905711` |
| Creation baseline tree | `b336b3a390779c1f617f2dfff4defbdeb0457ca6` |
| Release identity | `CNTX Public Core Release` |
| Release version | `0.1.0-prealpha.1` |
| Tag | `v0.1.0-prealpha.1` |
| Exact release subject commit | `109e6f293b150f48572cd747fab446c141d57193` |
| Exact release subject tree | `446b408e27d3ebd3f6616658c61ccd9db4af8978` |
| Subject inventory | 111 paths; 5752 UTF-8/LF bytes |
| Subject inventory SHA-256 | `A8C70DED3596BD4F74F3FDC24B1806A97B53361394BE611C065B1C90F9869BBE` |
| RELEASE-001 issue | [#92](https://github.com/CNTX-PROJECT/CNTX/issues/92) |
| RELEASE-001 PR | [#93](https://github.com/CNTX-PROJECT/CNTX/pull/93) |

The result terms below are local to this document: `Observed Match`,
`Observed Mismatch`, `Unverifiable`, and `Not Evaluated`. No aggregate result
is defined or inferred.

## Verification results

| Control | Result | Evidence |
| --- | --- | --- |
| Repository and synchronized `main` | `Observed Match` | Local, remote-tracking, remote, and GitHub `main` were all `6304b3f047cf60e35c09b229467f53b62f905711`; the local tree was `b336b3a390779c1f617f2dfff4defbdeb0457ca6` and the worktree was clean before mutation. |
| Immutable-releases setting | `Observed Match` | Repository endpoint returned `enabled=true`. No setting mutation was performed. |
| Lightweight tag identity and target | `Observed Match` | `refs/tags/v0.1.0-prealpha.1` resolved as object type `commit` directly to `109e6f293b150f48572cd747fab446c141d57193`. |
| Exact subject tree and inventory | `Observed Match` | Subject tree, 111 paths, 5752-byte inventory representation, inventory SHA-256, and all-`100644` Git mode set matched the frozen context. |
| GitHub Release identity and flags | `Observed Match` | Release database ID `367290932`, node ID `RE_kwDOTsnR984V5Go0`, title `CNTX Public Core 0.1.0-prealpha.1`, `draft=false`, `prerelease=true`, `latest=false`, and `immutable=true`. |
| Release provenance and channel boundary | `Observed Match` | URL `https://github.com/CNTX-PROJECT/CNTX/releases/tag/v0.1.0-prealpha.1`; author `Cintao66` / user ID `44348655`; created `2026-08-08T14:26:06Z`; published `2026-08-08T20:01:41Z`; zero custom assets; no discussion. |
| Release body and Accepted source | `Observed Match` | Published body was 5916 UTF-8 bytes with SHA-256 `449CF4A6A585490419BBBE47AD34C5C431FF51E55B2194175AB75784614B2BE0`, byte-equal to integrated Git blob `b1bc97e3bede5e655f20d325dc6657c8019b03ec` at `docs/release/releases/0.1.0-prealpha.1.md`. |
| RELEASE-001 lifecycle | `Observed Match` | PR #93 was merged to commit `6304b3f047cf60e35c09b229467f53b62f905711` at `2026-08-08T20:00:16Z`; issue #92 was `closed/completed` at `2026-08-08T20:02:57Z` with three comments, including completion comment `5227882228`; the public RELEASE-001 task branch was absent. |
| Historical issue #80 | `Observed Match` | Issue #80 remained `closed/not_planned` with exactly four comments. No mutation was performed. |
| Main governance ruleset | `Observed Match` | Ruleset `20518984`, `SETTINGS-001 main governance`, remained `active`. |
| Generated tarball HTTP retrieval | `Observed Match` | One request returned HTTP 200, resolved to the GitHub codeload URL, and downloaded 362342 bytes. |
| Generated tarball entry safety | `Observed Match` | 165 accepted entries: 54 directories and 111 regular files; one top-level directory; zero unsafe, link, or special entries. |
| Generated tarball path and content equivalence | `Observed Match` | 111/111 files compared; no missing or extra path; zero Git-blob or byte mismatch. |
| Generated zipball HTTP retrieval | `Observed Match` | One request returned HTTP 200, resolved to the GitHub codeload URL, and downloaded 511003 bytes. |
| Generated zipball entry safety | `Observed Match` | 165 accepted entries: 54 directories and 111 regular files; one top-level directory; zero unsafe, link, or special entries. |
| Generated zipball path and content equivalence | `Observed Match` | 111/111 files compared; no missing or extra path; zero Git-blob or byte mismatch. |
| Git mode preservation through generated archives | `Unverifiable` | The subject Git tree records only `100644`. The tarball exposed file mode `000664`; the zipball exposed `000000` through its external attributes. Path and byte equivalence were established, but archive metadata cannot prove exact Git mode preservation. |
| Timestamp, compression, and transport-metadata equivalence | `Unverifiable` | Generated archives have channel- and format-specific metadata that is not part of the exact Git tree. It was not treated as release identity or normative content. |
| New security/privacy/legal specialist evidence | `Not Evaluated` | VERIFY-001 did not rerun scanners, obtain private vulnerability content, or perform specialist or legal review. The Accepted `Unverifiable` security/privacy/legal/disclosure boundary remains unchanged. |

There were no observed path or content mismatches in either generated archive.
The two `Unverifiable` archive-metadata controls and the `Not Evaluated`
specialist-evidence control remain visible and are not converted into a
favorable aggregate outcome.

## GitHub Release evidence

The GitHub Releases API read-back returned:

- database ID `367290932` and node ID `RE_kwDOTsnR984V5Go0`;
- tag name `v0.1.0-prealpha.1` and API `target_commitish` value `main`;
- direct Git-reference target independently verified as exact commit
  `109e6f293b150f48572cd747fab446c141d57193`;
- title `CNTX Public Core 0.1.0-prealpha.1`;
- `draft=false`, `prerelease=true`, `latest=false`, and `immutable=true`;
- author `Cintao66`, user ID `44348655`;
- created timestamp `2026-08-08T14:26:06Z` and published timestamp
  `2026-08-08T20:01:41Z`;
- zero custom assets and no discussion;
- generated tarball URL
  `https://api.github.com/repos/CNTX-PROJECT/CNTX/tarball/v0.1.0-prealpha.1`;
- generated zipball URL
  `https://api.github.com/repos/CNTX-PROJECT/CNTX/zipball/v0.1.0-prealpha.1`.

The mutable-looking API `target_commitish` label does not override the
separately read Git reference. The verification subject remains the exact
commit and tree pinned above.

## Archive retrieval evidence

### Tool and runtime versions

- Git: `git version 2.55.0.windows.3`.
- GitHub CLI: `gh version 2.97.0 (2026-07-31)`.
- curl: `curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP`.
- Python: `Python 3.13.14`.
- PowerShell: `5.1.26100.8972`.

### Retrieval observations

| Format | Retrieval time UTC | Requested URL | HTTP | Resolved URL | Bytes | Time-bound SHA-256 |
| --- | --- | --- | --- | --- | ---: | --- |
| tarball | `2026-08-08T20:51:06.5571371Z` | `https://api.github.com/repos/CNTX-PROJECT/CNTX/tarball/v0.1.0-prealpha.1` | 200 | `https://codeload.github.com/CNTX-PROJECT/CNTX/legacy.tar.gz/refs/tags/v0.1.0-prealpha.1` | 362342 | `06B3E3618C86C5D5CCB3109ACE3669B2A51C83B320AA047C13B675EC61A8F007` |
| zipball | `2026-08-08T20:51:07.3007934Z` | `https://api.github.com/repos/CNTX-PROJECT/CNTX/zipball/v0.1.0-prealpha.1` | 200 | `https://codeload.github.com/CNTX-PROJECT/CNTX/legacy.zip/refs/tags/v0.1.0-prealpha.1` | 511003 | `1EFEB1BB60A76B465B93A8E4AF3905F22447EDD6D90CCB48F0F886946F443749` |

Each URL was retrieved once with no retry, fallback, mirror, or cache-based
substitution. These archive hashes identify only the bytes obtained at those
times. They are non-canonical and do not define a digest contract, release
identity, or normative publication set.

### Entry-safety and extraction observations

Both archives exposed the same generated top-level directory:
`CNTX-PROJECT-CNTX-109e6f2`. Only this one directory component was stripped
from comparison paths.

Before extraction, the inline procedure rejected any absolute,
drive-qualified, parent-traversing, duplicate, link, device, or unexpected
special entry. It then created each destination beneath the unique temporary
root, opened regular files individually, and never used an unrestricted
`extractall` operation. Both formats contained 54 directory entries and 111
regular files, with zero unsafe, link, or special entry.

### Executed commands and comparison procedure

The downloads used the following command form once per approved URL:

```text
curl.exe -L --fail --silent --show-error --output <unique-temp-file> --write-out "%{http_code}|%{url_effective}|%{size_download}|%{time_total}" <approved-api-url>
```

The comparison used Python standard-library `tarfile` and `zipfile` readers
and Git plumbing. The executed inline procedure was equivalent to these exact
ordered operations:

```text
1. git ls-tree -r -z --full-tree 109e6f293b150f48572cd747fab446c141d57193
2. Decode every tree path as UTF-8 and retain its mode, type, and blob object ID.
3. Recreate the canonical inventory bytes as ordinal paths joined by LF plus a final LF.
4. Verify the subject tree, 111 path count, 5752 byte count, inventory SHA-256, blob-only entries, and the all-100644 Git mode set.
5. Open the downloaded archive without extraction.
6. Normalize only slash direction for safety inspection; reject empty, absolute, drive-qualified, parent-traversing, duplicate, link, device, or special entries.
7. Require exactly one shared first path component.
8. For every regular file, remove only that first component, resolve its destination, require containment in the unique extraction root, and copy bytes through an exclusive new-file handle.
9. Enumerate extracted regular files by ordinal repository-relative path.
10. Compare the extracted path set with the exact Git-tree path set.
11. For every shared path, calculate SHA-1 over "blob <length>\0<bytes>" and compare it with the exact Git blob ID.
12. Independently compare extracted bytes with `git cat-file blob <object-id>` output.
13. Record archive SHA-256, entry counts, root, missing/extra paths, blob mismatches, byte mismatches, exposed archive modes, and limitations.
```

This procedure performed no network Schema Resource resolution, evaluator
execution, content repair, or archive normalization beyond the one generated
top-level directory.

### Archive comparison ledger

| Evidence | tarball | zipball |
| --- | ---: | ---: |
| Archive entries | 165 | 165 |
| Directory entries | 54 | 54 |
| Regular-file entries | 111 | 111 |
| Unsafe entries | 0 | 0 |
| Link entries | 0 | 0 |
| Special entries | 0 | 0 |
| Extracted files | 111 | 111 |
| Expected files | 111 | 111 |
| Compared files | 111 | 111 |
| Missing paths | 0 | 0 |
| Extra paths | 0 | 0 |
| Git-blob mismatches | 0 | 0 |
| Byte mismatches | 0 | 0 |
| Exposed file-mode values | `000664` | `000000` |

## Exact release-subject inventory

The following ordinal path list is the complete 111-path inventory used for
both comparisons:

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

## Temporary-environment disposition

The downloads and extracted trees existed only under the unique temporary
root `cntx-verify001-8983fc2d885b41f29205122503296d32` in the operating
system temporary directory. After this evidence was written, that exact root
was eligible for targeted deletion. No archive, extraction, dependency,
virtual environment, `node_modules`, runner, script, executable harness, or
temporary result is part of the repository candidate.

## Limitations, adverse evidence, and restricted evidence

- Generated source archives are GitHub channel derivatives. Their byte hashes
  may change independently of the Git subject and are not canonical.
- Archive permissions, timestamps, owners, compression metadata, and transport
  headers do not reproduce all Git or repository-host metadata.
- The tag direct target and extracted bytes were checked, but this does not
  create a signature, attestation, trust chain, SBOM, manifest, or proof of
  third-party retrieval.
- ARCHITECT performed both archive comparisons in one Windows environment.
  There was no independent human or platform reproduction.
- No private vulnerability report content was accessed. No code-scanning,
  external scanner, penetration test, independent security/privacy/legal
  specialist review, or legal-completeness review was performed.
- The Accepted security/privacy/legal/disclosure readiness result remains
  `Unverifiable`. Publication does not convert it to `Satisfied`.
- The release remains an unsupported pre-alpha publication. This record makes
  no compatibility, support, production-readiness, security, privacy, legal,
  compliance, fitness, warranty, certification, accreditation, or absence
  claim.

No observed mismatch was hidden or resolved. The metadata limitations above
remain explicit.

## Protected state and non-actions

The following baseline blobs were recorded before the candidate and protected
outside any explicitly allowed bounded status/navigation update:

- RELEASE-001 execution source:
  `bee559d975f64a475bf4277d430999544667ae57`;
- integrated release-notes source:
  `b1bc97e3bede5e655f20d325dc6657c8019b03ec`.

VERIFY-001 performed no immutable-setting mutation; tag creation, movement,
deletion, force-update, or replacement; Release edit, deletion, replacement,
or creation; issue #80, issue #92, or PR #93 mutation; generated-notes,
discussion, asset, package, archive, manifest, digest-contract, signature,
attestation, certification, correction, withdrawal, support, compatibility,
publication, distribution, implementation, hosted-publication, or deployment
action.

It created no Artifact Instance, canonical Portable Conformance Evidence,
canonical Validation Output, validator, resolver, registry, catalog, cache,
bundler, mirror, redirect, API, CLI, workflow, automation, runtime, provider,
or product mechanism. It authorizes no `VERIFY-002`, `ARCH-027`, or other
follow-on phase.

## Lifecycle and stop

The creation phase may produce one Proposed candidate, one Draft PR, and one
transparent non-independent exact-head COMMENT review. It then stops for
separate attributable EIGENAAR / Final Authority exact-head acceptance.

This Accepted record is derived verification evidence. It does not replace the
authoritative Git objects, GitHub objects, issue authority, Accepted sources,
or final-human decision, and it grants no further authority.
