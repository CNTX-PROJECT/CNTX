# CNTX Minimal Validation and Integrity Slice

**Current Status:** Integrated bounded implementation Version `1.0.0`;
[issue #122](https://github.com/CNTX-PROJECT/CNTX/issues/122) is
closed/completed and PR [#123](https://github.com/CNTX-PROJECT/CNTX/pull/123)
is merged.

This directory contains one bounded implementation of the Accepted Tool and
Implementation contracts in ARCH-037. It was installed, tested, and executed
only in separately authorized isolated temporary environments; those
environments and dependencies were cleaned up afterward. Repository presence
does not install or support it and establishes no broader correctness,
conformance, support, certification, release, deployment, or final-human
authority.

## Exact target

| Dimension | Exact value |
| --- | --- |
| Tool Identity | `https://github.com/CNTX-PROJECT/CNTX/tools/minimal-validation-integrity-slice` |
| Tool Version | `1.0.0` |
| Implementation Identity | `https://github.com/CNTX-PROJECT/CNTX/implementations/minimal-validation-integrity-slice/python-jsonschema` |
| Implementation Version | `1.0.0` |
| Runtime | CPython `3.13.14` |
| Direct dependency | `jsonschema 4.26.0` |
| Resolved dependencies | `attrs 26.1.0`, `jsonschema-specifications 2025.9.1`, `referencing 0.37.0`, `rpds-py 2026.6.3` |

The Tool and Implementation identities are opaque identifiers, not network
locations or publication channels.

### Proposed corrective Implementation Version 1.0.1

Accepted issue [#143](https://github.com/CNTX-PROJECT/CNTX/issues/143) and
attributable issue-acceptance comment
[`5263430981`](https://github.com/CNTX-PROJECT/CNTX/issues/143#issuecomment-5263430981)
govern one Proposed, non-executed corrective candidate. Its source-first
commit/tree is `1d28b2df55db86b82d23c011eba809a484559272` /
`ac73860d2908efa9ec4eaf5b7e814de44fd2beb1`.

The source delta only rejects a colon in every caller-supplied relative path
segment on every supported host and changes only `IMPLEMENTATION_VERSION` from
`1.0.0` to `1.0.1`. Tool Identity, Tool Version `1.0.0`, Implementation
Identity, all other source behavior, tests, schemas, rules, records, outputs,
and historical evidence remain unchanged.

[`requirements-1.0.1.lock`](requirements-1.0.1.lock) is a new separate lock
revision. It retains exact CPython `3.13.14` and the same five historical
dependency artifacts. The new
[`corrective-1.0.1` practice revision](practice/cross-record-integrity/corrective-1.0.1/scenario-matrix.json)
uses exact LF Git-blob pins from the source-first commit/tree. Neither subject
overwrites its historical `1.0.0` predecessor.

This candidate has not acquired or installed dependencies and has not imported
or executed the implementation, tests, schemas, cases, invocations, rules, or
runner. The retained Windows acquisition set establishes no Linux, macOS, or
multi-platform portability. Static preparation creates no execution evidence,
aggregate verdict, support, release, deployment, CI, or automatic authority.

## Capability boundary

The source implements the following separately observable responsibilities:

- strict UTF-8 JSON parsing with BOM, duplicate-member, comment, invalid-number,
  trailing-data, JSON5, YAML, and XML rejection;
- role-relative path resolution beneath caller-approved roots;
- exact registration of ten caller-supplied Schema Resources Version `1.0.0`;
- static `$ref` closure inside only that registered set;
- Draft 2020-12 schema checking without a `FormatChecker`;
- nine direct Test Manifests and one operation-based State Snapshot manifest;
- exact inventory `203/38/165` and separate expected/actual case observations;
- thirteen separately evaluated Cross-Record Integrity Rules Version `1.0.0`;
- four separate rule outcomes: `satisfied`, `not-satisfied`, `unverifiable`,
  and `not-evaluated`;
- bounded Validation Execution Record, Validation Evidence and
  Reproduction Package, and Cross-Record Integrity Evaluation Record content;
- deterministic JSON and human-readable presentation; and
- visible diagnostics, warnings, limitations, blocked conditions,
  non-execution, adverse/restricted-evidence boundaries, and
  `automaticAuthority: false`.

The implementation does not discover inputs, contact a network, install or upgrade
dependencies, mutate the subject repository, repair data, use mutable aliases,
produce a universal verdict, review, approve, accept, certify, release, host,
or deploy anything.

## Closed invocation representation

Each invocation is a strict JSON object containing exactly these root
properties and no others:

1. `invocation`;
2. `tool`;
3. `implementation`;
4. `implementationSource`;
5. `validationSubject`;
6. `governingContext`;
7. `evaluatorContext`;
8. `dependencyLock`;
9. `configuration`;
10. `environment`;
11. `schemas`;
12. `manifests`;
13. `rules`;
14. `subjectRecords`;
15. `resourceLimits`;
16. `output`;
17. `executionWindow`;
18. `evidenceItems`;
19. `reproductionProcedures`;
20. `expectedInventory`;
21. `requestedOperations`;
22. `phaseApplicability`;
23. `adverseEvidence`;
24. `restrictedEvidence`;
25. `retentionAndCleanup`;
26. `claimBoundary`;
27. `roles`;
28. `network`; and
29. `automaticAuthority`.

The implementation-source commit/tree and validation-subject commit/tree are
independent exact pins. `schemas` contains exactly ten identity/version/path/
SHA-256 mappings. `manifests` contains exactly ten key/schema/version/path/
SHA-256/construction mappings. `rules` contains the thirteen Accepted Rule
Identity/Version pairs exactly once; supplied order creates no meaning and
results are presented by identity. `expectedInventory` is exactly
`10/10/9/1/203/38/165/13`. `requestedOperations` contains the four closed slice
operations and `phaseApplicability` explicitly marks all eight phases
applicable. `subjectRecords` is one closed set of at most 256 records. `output`
contains two distinct role-relative paths beneath the exact caller-approved
output root. Adverse evidence, restricted-evidence references, and retention/
cleanup declarations remain separate. The network object must be exactly
`{"automaticAccess": false, "state": "prohibited"}` and `automaticAuthority`
must be exactly `false`.

There is no default invocation and no ambient configuration. Current working
directory, environment variables, adjacent files, caches, previous output,
host locale, current time, or `main` cannot supply a missing value.

## Dependency lock and acquisition boundary

[`requirements.lock`](requirements.lock) is a closed TOML acquisition manifest
for exactly five wheel artifacts. It pins each name, version, filename, Python/
ABI/platform tag, byte length, SHA-256 digest, and public origin. The candidate
lock was prepared by read-only comparison of public GitHub lockfiles; no wheel
was downloaded and no dependency was installed.

The separate corrective [`requirements-1.0.1.lock`](requirements-1.0.1.lock)
retains the exact five artifact blocks and exact runtime from the historical
lock while identifying Implementation Version `1.0.1`. It is also an
acquisition manifest, not acquisition authority, and remains specifically a
Windows acquisition set.

Before any future installation, Gate E3 must authorize exact commands and the
acquired bytes must match every lock field. A later acquisition phase must not
resolve dependencies, follow unapproved redirects, substitute a mirror, use
credentials, select another artifact, or upgrade anything. Installation must
use only an already verified local wheel directory, `--no-index`,
`--no-deps`, and `--require-hashes` or an equivalently strict separately
reviewed mechanism inside a newly created temporary environment outside the
repository.

The CPython executable identity, build, architecture, and SHA-256 digest remain
Gate E3 evidence inputs. The lock does not prove artifact authenticity,
availability, installability, safety, or compatibility.

## Exact initial resource ceilings

The implementation encodes the accepted initial ceilings from issue #122, including
exactly 10 Schema Resources, 10 manifests, 203 cases, and 13 rules; 4 MiB per
JSON input and 64 MiB total JSON input; depth 128 and 1,000,000 parsed nodes;
4,096 `$ref` occurrences; 300 seconds wall and CPU time; 1 GiB process memory;
128 MiB retained output/evidence; and exactly two future frozen executions.

Input sizes, parsed nodes/depth, counts, references, output size, and boundary
checks are represented in source. Strong process memory, CPU, handle, process,
thread, and operating-system network enforcement requires exact Gate E3
environment evidence. The implementation must report a stronger guarantee as
`unverifiable` or `not-evaluated` when the environment cannot prove it.

## Historical Gate E3 execution procedure

The steps below describe the bounded procedure that was later separately
authorized and executed. Repeating it still requires its own exact authority;
no invocation may rely on the current working directory or an ambient cache.

1. Verify the CPython executable and the five acquired wheel byte lengths and
   SHA-256 digests against `requirements.lock` using a standard-library-only
   verification script in a temporary directory.
2. Create one new isolated environment outside the repository with the exact
   CPython `3.13.14` executable.
3. Install only the five verified local wheels with network access and
   dependency resolution disabled.
4. Run `test.py` under `python -I` with exact source and output roots.
5. Run `run.py` under `python -I` twice, each time with a new isolated
   environment and the same frozen invocation and subject inputs.
6. Compare every declared deterministic observation while retaining declared
   volatile environment differences.
7. Copy only separately authorized public-safe evidence to an exact output
   destination.
8. remove the isolated environments, wheel staging, caches, temporary output,
   and processes after exact target verification, or retain a visible cleanup
   limitation.

Clean Gate E3 evidence recorded two 29-test runs and two runner executions with
exact agreement across all `203/38/165` cases. The temporary execution roots,
environments, wheels, caches, and outputs were removed after public-safe
inventory evidence was retained. Exact absolute execution roots remained
private; public evidence uses only role-relative references. The frozen
zero-`subjectRecords` invocation made the thirteen integrity rules inapplicable,
so all remained separately `not-evaluated` rather than satisfied.

## Completed cross-record practice slice

The [bounded cross-record integrity practice slice](practice/cross-record-integrity/README.md)
contains four full, strict JSON invocations and one frozen expected-outcome
matrix under completed issue #124 and merged PR #125.

The scenarios use `8/9/10/1` synthetic public-safe subject records. Together
they make every Accepted Cross-Record Integrity Rule Version `1.0.0`
applicable at least once and keep `satisfied`, `not-satisfied`, `unverifiable`,
and `not-evaluated` separate. Two separately authorized isolated environments
executed all four scenarios. The actual outcomes matched the frozen expected
matrix exactly: `13 satisfied`; `12 satisfied / 1 not-satisfied`; `11 satisfied
/ 2 unverifiable`; and `7 satisfied / 6 not-evaluated`. These observations
create no aggregate verdict, broader conformance, acceptance, certification,
release, deployment, or authority claim.

## Output and authority boundary

The machine-readable output keeps invocation/context pins, phase results,
per-case observations, inventory, per-rule observations, diagnostics,
limitations, blocked/non-executed conditions, candidate records, claims, and
authority separate. The short summary contains descriptive counts only. A
process exit code is operational transport information, not a CNTX pass/fail.

No output is automatically canonical Validation Output, Portable Conformance
Evidence, an Evidence Bundle, Review Record, Decision Record, certification,
release evidence, deployment evidence, or final-human authority. Only an
attributable EIGENAAR / Final Authority decision can accept later work under
repository governance.
