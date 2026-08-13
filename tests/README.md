# CNTX synthetic schema tests

This directory is the navigation point for the fixed synthetic cases that
exercise the ten Accepted Core Schema Resources, the separate Accepted and
integrated ARCH-042 Module Definition Schema Resource, and the Accepted and
integrated ARCH-044 Profile Definition Schema Resource.

## What exists today

| Item | Count |
| --- | ---: |
| Accepted Core manifests | 10 |
| Historical Core cases | 203: 38 expected valid and 165 expected invalid |
| Historical Core manifest forms | 9 direct and 1 operation-based |
| Accepted Module manifests | 1 |
| Accepted ARCH-042 cases | 48: 8 expected valid and 40 expected invalid |
| Accepted ARCH-042 manifest forms | 1 direct |
| Accepted Profile manifests | 1 |
| Accepted ARCH-044 cases | 72: 11 expected valid and 61 expected invalid |
| Accepted ARCH-044 manifest forms | 1 operation-based |

`Governed schema resource or candidate → fixed input case → fixed expected validity → separately governed execution`

## Choose a manifest

| Schema subject | Synthetic cases |
| --- | --- |
| Common Artifact Envelope | [cases.json](schemas/common-artifact-envelope/1.0.0/cases.json) |
| Project Charter | [cases.json](schemas/project-charter/1.0.0/cases.json) |
| Workstream | [cases.json](schemas/workstream/1.0.0/cases.json) |
| Task Contract | [cases.json](schemas/task-contract/1.0.0/cases.json) |
| Context Packet | [cases.json](schemas/context-packet/1.0.0/cases.json) |
| Execution Result | [cases.json](schemas/execution-result/1.0.0/cases.json) |
| Evidence Bundle | [cases.json](schemas/evidence-bundle/1.0.0/cases.json) |
| Review Record | [cases.json](schemas/review-record/1.0.0/cases.json) |
| Decision Record | [cases.json](schemas/decision-record/1.0.0/cases.json) |
| State Snapshot | [cases.json](schemas/state-snapshot/1.0.0/cases.json) |
| Epistemic Provenance and Freshness Module Definition Schema (Accepted and integrated) | [cases.json](schemas/extension-modules/epistemic-provenance-freshness/1.0.0/cases.json) |
| Context Packet Epistemic Provenance and Freshness Profile Definition Schema (Accepted and integrated) | [cases.json](schemas/profiles/context-packet-epistemic-provenance-freshness/1.0.0/cases.json) |

Open the [schema index](../schemas/README.md) for the governing resources or the
[minimal validation and integrity slice](../tools/minimal-validation-integrity-slice/README.md)
for the bounded local tool path.

## Evidence and authority boundary

These manifests are synthetic, non-normative validation inputs with fixed
expected results. Their presence, parseability, execution, or matched result
does not prove source truth, semantic correctness, complete conformance,
security, production readiness, approval, certification, release fitness,
deployment fitness, or final-human authority. Results remain individual; the
historical Core `203/38/165` inventory is not an aggregate score or quality
gate. The Accepted ARCH-042 `48/8/40` inventory is separate and likewise forms
no aggregate pass/fail, score, badge, conformance claim, approval, or authority.
Its successful candidate execution remains bound only to candidate commit/tree
`d10fb23bdec7c13bb1154bd538d8e691d486fcce` /
`071a9909efcee1d4d74d7ff65b0b05da30e73875`. Separately governed PR #146
integrated the Accepted resource at commit/tree
`9f482043f76c792f6c2e1e96eb4a535ee26b3a99` /
`7b2f45791e3b7bff7e856f26fff9b22598c06709`, under integration-authority
comment `5271035681` and completion comment `5271254252`; issue #145 is
closed/completed and the task branch is absent locally and publicly. Status
promotion and integration were not new executions or evidence instances and
did not expand the minimal Tool's supported input set.

The Accepted ARCH-044 `72/11/61` operation-based manifest contains one complete
`baseInstance`; each named case deep-copies it and applies only ordered RFC 6901
`add`, `remove`, or `replace` operations before separate evaluation. These are
deterministic test mechanics, not a Profile representation, patch protocol,
migration, runtime, or implementation contract. The new manifest changes the
construction inventory from `10 direct / 1 operation-based` to `10 direct / 2
operation-based`. Its cases were fixed before validation. The final authorized
local run evaluated each case exactly once and matched all `72/72` expectations
(`11 valid / 61 invalid`) with zero mismatches. That validation is local, non-
governing, non-independent, and bound only to candidate commit/tree
`7420e5d179ab965bfda58780df4f41a08a0b62de` /
`56d1808cb95f3dd5a0b5d84f2a8e440891dff5e6`. Accepted status, deterministic
materialization, schema validity, case expectations, validation, Ready state,
review, or mergeability does not integrate or activate the resource, expands no
Tool support, and creates no new execution/evidence instance, aggregate result,
certification, release gate, deployment gate, or authority.

Issue-contract acceptance comment `5279967413` governed the Proposed candidate,
as supplemented only by source-preserving correction addenda `5280408320` and
`5280832992`. The first corrects the baseline link inventory to `1489 Markdown /
27 HTML` and `1297 local / 219 external`. The second corrects only the
evaluation-responsibility count from sixteen to seventeen while preserving the
exact seventeen Accepted ARCH-043 members. Neither changes any case, expected
boolean, operation, schema assertion, status, execution boundary, or lifecycle
authority. Exact-head candidate-acceptance comment `5285702199` establishes the
Accepted decision for the unchanged candidate; the status-only promotion was
not a new execution and governed integration remained separate. Later
integration-authority comment `5286010813` authorized merged PR #150 at public
`main` commit/tree `1d9e4667d68cce6e0289464c821bcd95e1d355ae` /
`3feeb1ce8ce2c0a7b45b88e42c9d668fc856d367`. Completion comment `5286062635`
records issue #149 closed/completed and the task branch absent locally and
publicly. Integration preserved all accepted schema/case bytes, all historical
lifecycle and execution/evidence pins, all 12 Schema Resources, and the
separate Core `203/38/165`, Module `48/8/40`, and Profile `72/11/61`
inventories. It created no Tool support or new execution/evidence claim.
