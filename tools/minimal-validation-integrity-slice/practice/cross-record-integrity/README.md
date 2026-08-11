# Bounded cross-record integrity practice slice

Status: **Proposed non-normative practice fixtures — not executed**.

These four strict JSON invocations prepare the smallest public-safe scenario
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
[scenario-matrix.json](scenario-matrix.json). Expected outcomes are statically
derived. They are not observed execution results and prove no broader
conformance, acceptance, approval, certification, release, deployment, or
final-human authority.

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
evidence, or authority record. `automaticAuthority` remains false. Execution,
dependencies, output, evidence, review, acceptance, integration, release, and
deployment require later separate authority.
