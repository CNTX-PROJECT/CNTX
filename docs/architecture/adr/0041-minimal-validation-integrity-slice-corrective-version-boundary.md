# ADR-0041: CNTX Minimal Validation and Integrity Slice Corrective Version Boundary

- **Status:** Proposed
- **Date:** 2026-08-12
- **Issue:** [#141](https://github.com/CNTX-PROJECT/CNTX/issues/141)
- **Issue-contract acceptance comment:** [5262502160](https://github.com/CNTX-PROJECT/CNTX/issues/141#issuecomment-5262502160)
- **Baseline:** commit `97d72439bcad31c144352091cb74eaac342f0ae3`,
  tree `831c8e953de06a1dd8b124904779653df43543fa`
- **Decision:** ARCH-041 — CNTX Minimal Validation and Integrity Slice
  Corrective Version Boundary

## Context

The integrated Minimal Validation and Integrity Slice has bounded successful
Windows execution evidence. Later read-only reassessment established that all
21 repository-file pins in the four historical practice invocations match
CRLF-transformed checkout bytes rather than the exact LF Git blobs. It also
established that the existing cross-platform path-safety test expects
`file:stream` to be rejected everywhere while Implementation Version `1.0.0`
rejects colon-bearing path segments only on Windows.

The same reassessment confirmed that the Accepted `1.0.0` acquisition lock
contains one Windows-only binary wheel, the implementation requires exact
CPython `3.13.14`, GitHub Actions is disabled, and the repository has no
workflow. Runtime portability and CI introduce distinct identity/version,
dependency, settings, security, evidence, and cost decisions. They must not be
silently folded into a narrow defect correction.

The historical invocations, matrix, output, review, evidence, limitations,
completion records, and issue-#126 pins are immutable. Rewriting them would
misrepresent the exact bytes and environment used during historical execution.

## Decision

Propose one corrective boundary with seven responsibilities.

### Preserve immutable history

Keep Tool Version `1.0.0`, Implementation Version `1.0.0`, the original lock,
the four invocations, scenario matrix, output, reviews, evidence, limitations,
completion records, and all seven issue-#126 frozen pins unchanged. Historical
Windows evidence remains valid only for its exact supplied and materialized
bytes and governed environment; it creates no general portability claim.

### Pin exact Git-blob bytes

Require every new repository-file SHA-256 pin under the corrective version to
cover the exact bytes of the named Git blob in an exact caller-supplied
commit/tree, without checkout conversion, newline transformation,
normalization, serialization, canonicalization, re-encoding, repair, fallback,
or ambient platform behavior.

Record exact repository, commit, tree, path, Git blob identity where
available, byte length, SHA-256, and observation method. Location, branch,
filename, working tree, cache, or current directory cannot replace the
immutable blob subject.

### Propose Implementation Version `1.0.1`

Keep the existing Implementation Identity:

`https://github.com/CNTX-PROJECT/CNTX/implementations/minimal-validation-integrity-slice/python-jsonschema`

Propose only corrective Implementation Version `1.0.1` under that identity.
Tool Version remains `1.0.0`; no new Tool Identity or Version is created.
Proposed status, candidate presence, review, Ready state, repository presence,
or mergeability does not allocate or activate `1.0.1`.

### Bound one behavior correction

Permit `1.0.1` to differ behaviorally from `1.0.0` only by rejecting a colon
in every caller-supplied relative path segment on every supported host. Retain
all other existing path, root, symlink, junction, network, strict-JSON,
configuration, resource, and fail-closed controls. Do not silently alter
immutable Version `1.0.0`.

### Add new revisioned inputs

Require a later separately authorized implementation candidate to add one new
corrective lock revision and one new four-scenario invocation/matrix revision
set. Preserve the four scenario purposes, thirteen rule identities/versions,
separate expected outcome patterns, limitations, adverse/restricted evidence,
non-aggregation, and `automaticAuthority: false`.

Use new identifiers/revisions and exact new implementation source pins. Pin
the ten historical Schema Resources, ten historical Test Manifests, and new
lock over exact Git-blob bytes. Do not replace or relabel historical objects.

### Keep portability separate

Do not change exact CPython `3.13.14`, the five Accepted dependency versions,
or existing Windows acquisition artifacts within the bounded corrective
proposal. Linux/macOS artifacts, source distributions, multi-platform wheels,
a broader runtime rule, or portability claims require a later separate
identity/version and acquisition decision.

### Keep CI and Phase 4A3.2 separate

Create no workflow and change no setting. A later CI decision must separately
govern Actions enablement, least privilege, triggers, forks, immutable action
pins, platform/runtime matrix, dependency acquisition, network use, secrets,
retention, failure meaning, limitations, costs, and final-human authority.

Keep Phase 4A3.2 not started until the corrective version lifecycle reaches
separately governed completion and a fresh read-only reassessment authorizes
the next proposal.

## Consequences

Positive consequences:

- immutable execution and evidence history remains truthful;
- new pins have a platform-independent immutable repository-byte subject;
- the path-safety test and proposed implementation behavior have one explicit
  cross-platform invariant;
- exact Tool and Implementation version semantics remain separate;
- new execution inputs cannot silently replace prior evidence subjects; and
- portability, CI, and Phase 4A3.2 remain independently governable.

Costs and limitations:

- the existing four invocations remain non-reproducible from untransformed Git
  blobs and must be understood as historical Windows subjects;
- the corrective proposal remains Windows-bound and exact-runtime-bound;
- new lock and invocation revisions are required before new execution;
- CI remains absent and Actions remains disabled;
- static documentation review proves no corrected implementation, execution,
  determinism, performance, compatibility, security, support, release fitness,
  or deployment fitness; and
- preparation, interpretation, validation, publication, and review are
  non-independent.

## Alternatives not selected

### Rewrite or repin historical invocations

Not selected because this would change immutable evidence inputs and obscure
the bytes actually used.

### Patch behavior under Version `1.0.0`

Not selected because the path rule and digest subject are
compatibility-significant Implementation semantics.

### Weaken the non-Windows test

Not selected because colon-bearing repository paths may later be materialized
on Windows and the existing expectation expresses the safer invariant.

### Combine portability and CI with the correction

Not selected because each adds independent platform, acquisition, settings,
security, evidence, and cost decisions.

### Continue directly to Phase 4A3.2

Not selected because confirmed defects in the current validation basis should
be bounded before new Module Schema Resource work depends on it.

## Protected predecessors and historical integrity

Preserve ARCH-001 through ARCH-040, ADR-0001 through ADR-0040, all Artifact
Contracts, identities, versions, schemas, tests, rules, tools,
implementations, locks, invocations, matrices, outputs, evidence, limitations,
releases, settings, issue/PR/review records, and historical authority
unchanged.

## Non-decisions and non-execution

Proposed status creates no `.gitattributes`, repin, lock, invocation, matrix,
Python change, testcase change, schema, Schema Resource, rule, Tool or
Implementation activation, dependency acquisition, install, runner execution,
output, evidence instance, workflow, CI, Actions enablement, settings change,
tag, release, publication, support, certification, hosting, deployment,
Phase 4A3.2 start, or later-phase authority.

It performs no conversion, governed hashing, installation, network access,
validation, testing, execution, evidence production, release, or deployment.

## Authority boundary

Issue #141 and issue-contract acceptance comment `5262502160` govern this
Proposed documentation candidate. Candidate presence, Draft PR state,
transparent non-independent COMMENT review, Ready state, repository presence,
or mergeability does not accept, integrate, allocate, activate, execute,
release, or authorize ARCH-041 or Implementation Version `1.0.1`.

Candidate acceptance, status promotion, merge, integration, issue closure,
branch cleanup, correction implementation, execution, evidence, portability,
CI, settings changes, and Phase 4A3.2 require later separate attributable
EIGENAAR / Final Authority authority at the applicable exact subject.
