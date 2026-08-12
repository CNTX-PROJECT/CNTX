# Bounded cross-record integrity practice slice

Status: **Integrated non-normative practice fixtures with bounded execution
evidence**.

These four strict JSON invocations form the smallest public-safe scenario
set that can make all thirteen Accepted Cross-Record Integrity Rules Version
1.0.0 applicable at least once while keeping the four outcomes separate.

- `01-coherent-chain.json`: eight accessible records; all thirteen outcomes are
  expected `satisfied`.
- `02-dangling-reference.json`: the coherent chain plus one supporting record
  with one dangling reference; only `reference-resolves-exactly-once` is
  expected `not-satisfied`.
- `03-restricted-reference.json`: the coherent chain plus one accessible
  source and one restricted target with `content: null`; exactly
  `supplied-record-exists` and `reference-resolves-exactly-once` are
  expected `unverifiable`.
- `04-inapplicable-minimal.json`: one accessible Task Contract record; six
  rule families are genuinely inapplicable and expected `not-evaluated`.

The machine-readable expected matrix is in
[scenario-matrix.json](scenario-matrix.json). It remains the frozen,
statically derived pre-execution matrix; its embedded pre-execution status is
historical input provenance, not current project lifecycle state. Later
separately authorized executions in two isolated environments matched that
matrix exactly. Expected and actual outcomes remain distinct and prove no
broader conformance, acceptance, approval, certification, release, deployment,
or final-human authority.

Every record digest is SHA-256 over canonical UTF-8 JSON of its `content`
value using sorted keys and compact separators. Restricted content is absent;
the digest for that record covers canonical JSON `null`.

Known implementation limitation: the existing invocation validator rejects a
missing or blank identity, version, or revision before
`identity-version-revision-complete` can produce `not-satisfied`. These
fixtures preserve that boundary and do not modify the runner.

No fixture is a new Definition, Representation, Schema Resource, Artifact Type,
Artifact Instance, canonical Validation Output, Portable Conformance Evidence,
Evidence Bundle, Review Record, Decision Record, certification, release
evidence, or authority record. `automaticAuthority` remains false. Issue #124
is closed/completed and PR #125 is merged after bounded execution and evidence.
That completed lifecycle grants no reusable execution authority, supported
dependency installation, aggregate verdict, release, certification, hosting,
deployment, or final-human authority.

## Proposed corrective 1.0.1 revision

The [`corrective-1.0.1` revision](corrective-1.0.1/scenario-matrix.json) adds
four new invocations beneath a new path. It does not overwrite or reinterpret
the historical matrix, invocations, outputs, evidence, reviews, or completion
records above.

Accepted issue [#143](https://github.com/CNTX-PROJECT/CNTX/issues/143) and
attributable issue-acceptance comment
[`5263430981`](https://github.com/CNTX-PROJECT/CNTX/issues/143#issuecomment-5263430981)
govern the new revision. Every invocation pins corrective Implementation
Version `1.0.1`, exact implementation-source and validation-subject commit/tree
`1d28b2df55db86b82d23c011eba809a484559272` /
`ac73860d2908efa9ec4eaf5b7e814de44fd2beb1`, the separate
`requirements-1.0.1.lock`, and all twenty schema/test repository files by
SHA-256 over their exact LF Git-blob bytes.

The new matrix retains record counts `8/9/10/1`, the same thirteen Rule
Identities at Version `1.0.0`, and the same four separate expected patterns:
`13 satisfied`; `12 satisfied / 1 not-satisfied`; `11 satisfied / 2
unverifiable`; and `7 satisfied / 6 not-evaluated`. These are non-aggregate
expected observations, not a score, verdict, badge, threshold, conformance,
approval, certification, release fitness, deployment fitness, or authority.

The corrective revision is `proposed-not-executed`. No dependency was acquired
or installed and no implementation, test, schema, case, invocation, rule, or
runner was executed. Exact CPython `3.13.14` and the retained Windows
acquisition set establish no Linux, macOS, or multi-platform portability.
Execution, evidence, review of execution, integration, support, release,
deployment, CI/Actions, and any Phase 4A3.2 step require later separate
authority. `automaticAuthority` remains false.
