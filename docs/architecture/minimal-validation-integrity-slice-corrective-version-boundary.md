# CNTX Minimal Validation and Integrity Slice Corrective Version Boundary (ARCH-041)

## Status and authority

**Document Status: Accepted.**

This documentation-only decision is Accepted under [issue
#141](https://github.com/CNTX-PROJECT/CNTX/issues/141) and attributable
EIGENAAR / Final Authority issue-contract acceptance comment
[5262502160](https://github.com/CNTX-PROJECT/CNTX/issues/141#issuecomment-5262502160).
Exact-head candidate acceptance is recorded in comment
[5262723710](https://github.com/CNTX-PROJECT/CNTX/issues/141#issuecomment-5262723710)
on candidate commit `89f7a46319fd64e517e160b03b390e90bf1534ed` and tree
`2c519280a71491d3484bfebfc809f7e50e3bed50`, prepared directly from public
baseline commit
`97d72439bcad31c144352091cb74eaac342f0ae3` and tree
`831c8e953de06a1dd8b124904779653df43543fa`.

The preceding Proposed status, issue-contract acceptance, candidate
preparation, branch or repository presence, validation, Draft state, review,
Ready state, or mergeability did not accept, integrate, allocate, activate,
execute, or release ARCH-041 or Implementation Version `1.0.1`. Exact-head
candidate acceptance establishes Accepted document status only. Status
promotion, branch or repository presence, Ready state, review, and
mergeability do not integrate or activate the decision. Later separately
governed integration to `main` is required to allocate and activate only the
exact corrective Implementation Version `1.0.1`; no correction code, pin,
invocation, evidence, CI, or Phase 4A3.2 authority is created.

## Purpose

The integrated Minimal Validation and Integrity Slice has bounded successful
Windows execution evidence, but later read-only reassessment identified two
concrete correction subjects:

1. all 21 repository-file SHA-256 values pinned by the four historical
   practice invocations match CRLF-transformed checkout bytes and none match
   the exact LF bytes of the named Git blobs; and
2. the existing cross-platform path-safety test expects `file:stream` to be
   rejected everywhere, while Implementation Version `1.0.0` rejects a colon
   in a path segment only on Windows.

The reassessment also confirmed two separate boundaries: the Accepted
Implementation Version `1.0.0` acquisition set contains a Windows-only binary
wheel and requires exact CPython `3.13.14`, while GitHub Actions remains
disabled and the repository contains no workflow. Those facts are not silent
instructions to change the Accepted runtime, dependencies, settings, or
workflow policy.

ARCH-041 therefore defines a narrow corrective version boundary. It keeps
immutable history intact, defines exact Git-blob bytes as the subject of new
repository-file pins, proposes only Implementation Version `1.0.1`, bounds one
path-safety behavior correction, and requires new revisioned inputs rather
than overwriting earlier records. Runtime portability and CI remain separate
future governance decisions.

## Governing predecessors

This decision is subordinate to and changes none of:

- ARCH-001 through ARCH-040 and ADR-0001 through ADR-0040;
- CONTRACT-001 through CONTRACT-009;
- all ten Accepted Core Schema Resources and twenty historical schema/test
  JSON files;
- ARCH-024 validation outcomes and non-aggregation;
- ARCH-033 tooling and implementation boundaries;
- ARCH-034 Validation Execution Record;
- ARCH-035 Validation Evidence and Reproduction Package;
- ARCH-036 Test Manifest and thirteen Cross-Record Integrity Rules;
- ARCH-037 Concrete Tool and Implementation Contract;
- Accepted Tool Version `1.0.0` and Accepted Implementation Version `1.0.0`;
- the four historical practice invocations, their scenario matrix, outputs,
  evidence, reviews, limitations, completion records, and all seven issue-#126
  frozen byte/SHA-256 pins;
- immutable prerelease `0.1.0-prealpha.1`, its tag, Release, verification, and
  completion history;
- repository settings, ruleset `20518984`, Actions-disabled state, tags,
  Releases, evidence, and historical Git/GitHub objects; and
- adverse/restricted-evidence, non-execution, non-aggregation,
  `automaticAuthority: false`, and sole final-human-authority boundaries.

If this Accepted document could be read as changing an Accepted predecessor,
the predecessor controls and the proposed effect is blocked.

## Corrective decision

### 1. Preserve immutable `1.0.0` history

Tool Version `1.0.0`, Implementation Version `1.0.0`, their exact source
revisions, the original dependency lock, four historical practice
invocations, scenario matrix, outputs, reviews, evidence, limitations, and
completion records remain immutable historical objects.

The existing invocation and matrix JSON files MUST NOT be edited, moved,
renamed, deleted, repinned, or presented as if their executions used LF
Git-blob pins. Their observed Windows executions remain evidence only for the
exact materialized bytes and environments recorded at that time. They do not
prove general cross-platform reproduction.

The seven frozen issue-#126 byte/SHA-256 pins remain exact historical
integrity anchors. ARCH-041 neither corrects nor supersedes them.

### 2. Pin exact repository blob bytes in new revisions

Every new repository-file SHA-256 pin created under the corrective version
MUST be calculated over the exact bytes of the named Git blob in one exact
caller-supplied commit/tree. Checkout conversion, newline transformation,
Unicode normalization, serialization, canonicalization, re-encoding, repair,
fallback, cache state, or ambient platform behavior MUST NOT alter the digest
subject.

Each new pin subject MUST identify:

- the exact repository;
- commit and tree;
- repository-relative path;
- Git blob object identity where available;
- byte length;
- SHA-256 value; and
- observation method.

A location, mutable branch, working tree, current directory, filename, cache,
or transformed checkout is not an immutable blob identity. A later
`.gitattributes` decision may govern new working-tree materialization but
cannot redefine historical digest subjects or convert old values into
Git-blob digests.

### 3. Accept only the corrective Implementation Version `1.0.1` target

The unchanged Implementation Identity is:

`https://github.com/CNTX-PROJECT/CNTX/implementations/minimal-validation-integrity-slice/python-jsonschema`

ARCH-041 accepts corrective Implementation Version `1.0.1` as the exact
integration target under that same identity. It creates no new Tool Identity
or Tool Version; Tool Version remains `1.0.0`.

Accepted status alone does not allocate or activate Version `1.0.1`.
Allocation and activation require this exact-head candidate acceptance plus
later separately authorized governed integration to `main`. Issue presence,
candidate presence, review, Ready state, branch presence, repository presence,
mergeability, or a version-shaped string cannot allocate, activate, execute,
release, support, or certify it.

### 4. Bound the path-safety correction

The Accepted corrective Implementation Version `1.0.1` target may differ behaviorally from
Version `1.0.0` only by rejecting a colon in any caller-supplied relative path
segment on every supported host. This aligns implementation behavior with the
existing cross-platform test expectation for `file:stream`.

The correction MUST retain every existing fail-closed rejection of empty,
NUL-containing, absolute, drive, share, current, parent, root-escaping,
symbolic-link, junction, case-ambiguous, device, alternate-data-stream, or
otherwise unsafe paths. It MUST NOT weaken another path, root, symlink,
junction, network, strict-JSON, configuration, resource, or fail-closed
control.

This is compatibility-significant Implementation behavior and therefore MUST
NOT be silently applied under immutable Version `1.0.0`.

### 5. Add new corrective revisions instead of overwriting history

A later separately authorized implementation candidate must add, not replace:

1. one corrective dependency-lock revision naming Implementation Version
   `1.0.1`; and
2. one new four-scenario invocation and scenario-matrix revision set.

The new invocation revisions must preserve the separate coherent, dangling,
restricted, and minimal purposes; all thirteen rule identities and versions;
the four separate expected outcome patterns; adverse/restricted evidence;
limitations; non-execution boundaries; exact roles; non-aggregation; and
`automaticAuthority: false`.

They must use new invocation identifiers/revisions, reference exact new
implementation source commit/tree pins, and use exact Git-blob pins for the
ten historical Schema Resources, ten historical Test Manifests, and the new
corrective lock. They must not replace, relabel, or claim execution of the
historical invocation objects.

ARCH-041 creates no lock, invocation, matrix, execution, validation output, or
evidence instance.

### 6. Keep runtime and dependency portability separate

ARCH-041 does not change exact CPython `3.13.14`, the five Accepted dependency
versions, or the existing Windows acquisition artifact set for this bounded
corrective `1.0.1` proposal.

Linux or macOS artifacts, source distributions, multi-platform wheel sets, a
broader runtime rule, compatibility claims, or a portable Implementation
Version require a later separate identity/version and dependency-acquisition
decision. Portability cannot be inferred from the path-safety correction,
repository-byte pin rule, repository presence, or review.

### 7. Keep CI and Phase 4A3.2 separate

ARCH-041 creates no workflow and changes no repository setting. Any future CI
proposal must separately govern at least:

- Actions enablement and least privilege;
- trigger and fork boundaries;
- immutable action pins;
- platform/runtime matrix;
- dependency acquisition and network use;
- secret handling;
- output and evidence retention;
- failure meaning and limitations;
- cost/resource controls; and
- final-human authority.

Phase 4A3.2 Module Schema Resource work remains not started. The corrective
version lifecycle must reach separately authorized completion before a fresh
read-only reassessment can determine whether Phase 4A3.2 may begin.

## Compatibility and historical meaning

Implementation Version `1.0.0` and the Accepted `1.0.1` target remain distinct exact
subjects. A consumer cannot substitute one for the other, infer a version from
the Tool Version, or treat a newer number as proof of greater correctness,
portability, support, security, or fitness.

New Git-blob pins do not retroactively invalidate, rewrite, or improve the old
Windows evidence. The historical evidence remains bounded by its exact input
bytes, acquisition set, runtime, execution context, output, review, and stated
limitations. The new revisions, when later created and executed under separate
authority, would constitute new subjects and new evidence.

No aggregate pass/fail, score, traffic light, grade, badge, threshold,
approval, certification, release fitness, deployment fitness, or
consequential authority may be derived from the corrective boundary or from
the four separate practice outcomes.

## Security, privacy, and adverse information

Exact Git-blob pinning is an integrity subject rule only. A digest match does
not prove authenticity, provenance, safety, correctness, completeness,
applicability, currentness, permission, trust, support, or authority.

New revision records must remain public-safe and minimally disclose only the
information required to identify their exact subjects, methods, limitations,
and outcomes. Credentials, tokens, private keys, personal/private data, local
absolute paths, restricted material, private project context, and ambient
provider-specific assumptions are prohibited.

Restricted evidence remains represented through public-safe metadata and
limitations. Missing, inaccessible, conflicting, restricted, or unverifiable
information must remain visible and fail closed for dependent favorable
claims; it cannot be repaired by defaulting, inference, recollection, or
silence.

## Validation and evidence boundary

Static validation of an ARCH-041 documentation candidate may prove only its
exact path scope, text encoding, link integrity, protected-file identity,
repository inventory, and stated historical counts. It cannot prove corrected
code, exact future pins, cross-platform installation, execution, determinism,
performance, security, compatibility, supportability, release fitness, or
deployment fitness.

Preparation, interpretation, validation, publication, and review are
non-independent. The current Linux reproduction used an out-of-contract
runtime and establishes only its observed failure/error boundary. The prior
Windows evidence remains bounded to its exact governed environment.

Any later correction implementation, invocation, execution, evidence,
portability, or CI task requires its own exact baseline, allowlist, versions,
inputs, validation, limitations, review, and attributable final-human gate.

## Alternatives not selected

### Rewrite the four historical invocations

Not selected because it would destroy source-preserving history and make old
execution appear to have used different bytes.

### Recalculate pins in place under Version `1.0.0`

Not selected because the digest subject and observable path behavior are
compatibility-significant Implementation semantics. A silent in-place change
would blur exact identity/version/evidence boundaries.

### Relax the path-safety test on non-Windows hosts

Not selected because a repository path may later be materialized on Windows,
and the existing test already expresses the safer cross-platform invariant.

### Make `1.0.1` portable at the same time

Not selected because platform artifacts, runtime breadth, acquisition,
compatibility, and evidence introduce a larger independent decision surface.

### Add CI as the correction

Not selected because CI would observe behavior but cannot define the corrected
version, repair immutable pins, choose dependencies, or create final authority.
Actions is also an independently governed repository setting.

### Continue directly to Phase 4A3.2

Not selected because the active validation basis contains confirmed
reproduction and path-safety defects that should be bounded before new Module
Schema Resource work relies on it.

## Explicit non-decisions and non-execution

Accepted ARCH-041 creates no `.gitattributes`, historical-file edit, repin,
dependency lock, invocation, matrix, Python change, testcase change, schema,
Schema Resource, rule, Tool or Implementation activation, dependency
acquisition, installation, execution, output, evidence instance, workflow, CI,
Actions enablement, setting change, tag, release, GitHub Release, publication,
distribution, support, certification, hosting, deployment, H2.4 completion,
Phase 4A3.2 start, or later-phase authority.

It performs no checkout conversion, hashing of a new governed subject, path
validation, dependency installation, network access, runner invocation, test
execution, evidence production, review decision, merge, release, or
deployment.

## Final-human authority and stopgate

The controlling assertion remains `automaticAuthority: false`. A document,
issue, branch, commit, PR, review, tool, test, digest, CI result, model output,
majority, consensus, or mergeability state cannot become final authority.

Issue #141, issue-contract acceptance comment `5262502160`, and exact-head
candidate-acceptance comment `5262723710` govern this Accepted decision.
Acceptance is bound to candidate commit
`89f7a46319fd64e517e160b03b390e90bf1534ed` and tree
`2c519280a71491d3484bfebfc809f7e50e3bed50`. The preceding Proposed status,
candidate preparation, branch or repository presence, validation, Draft PR
state, transparent non-independent COMMENT review, Ready state, and
mergeability allocated or activated nothing.

Status promotion does not integrate or activate ARCH-041 or Implementation
Version `1.0.1`. Merge, integration, issue closure, branch cleanup, correction
implementation, execution, evidence, portability, CI, settings changes, and
Phase 4A3.2 each require later separate attributable EIGENAAR / Final
Authority authority at the applicable exact subject.

## References

- [Concrete Validation and Integrity Tool and Implementation Contract](concrete-tool-implementation-contract.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Test Manifest and Cross-Record Integrity Rules](test-manifest-cross-record-integrity-rules.md)
- [Validation Execution Record](validation-execution-record.md)
- [Validation Evidence and Reproduction Package](validation-evidence-reproduction-package.md)
- [Extension Module and Profile Tooling and Implementation Boundary](extension-module-profile-tooling-implementation-boundary.md)
- [Epistemic Provenance and Freshness Module JSON Representation Boundary](epistemic-provenance-freshness-extension-module-json-representation-boundary.md)
- [ADR-0041](adr/0041-minimal-validation-integrity-slice-corrective-version-boundary.md)
- [Roadmap](../../ROADMAP.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
