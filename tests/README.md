# CNTX synthetic schema tests

This directory is the navigation point for the fixed synthetic cases that
exercise the ten Accepted Core Schema Resources and the separate Proposed
ARCH-042 Module Definition Schema Resource candidate.

## What exists today

| Item | Count |
| --- | ---: |
| Accepted Core manifests | 10 |
| Historical Core cases | 203: 38 expected valid and 165 expected invalid |
| Historical Core manifest forms | 9 direct and 1 operation-based |
| Proposed Module manifests | 1 |
| Proposed ARCH-042 cases | 48: 8 expected valid and 40 expected invalid |
| Proposed ARCH-042 manifest forms | 1 direct |

`Accepted schema → fixed input case → fixed expected validity → separately governed execution`

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
| Epistemic Provenance and Freshness Module Definition Schema (Proposed) | [cases.json](schemas/extension-modules/epistemic-provenance-freshness/1.0.0/cases.json) |

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
gate. The Proposed ARCH-042 `48/8/40` inventory is separate and likewise forms
no aggregate pass/fail, score, badge, conformance claim, approval, or authority.
Its presence or evaluation does not expand the supported input set of the
minimal validation and integrity Tool.
