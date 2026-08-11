# CNTX synthetic schema tests

This directory is the navigation point for the fixed synthetic cases that
exercise the ten Accepted Core Schema Resources.

## What exists today

| Item | Count |
| --- | ---: |
| Versioned test manifests | 10 |
| Total cases | 203 |
| Expected valid | 38 |
| Expected invalid | 165 |
| Direct manifest forms | 9 |
| Operation-based manifest forms | 1 |

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

Open the [schema index](../schemas/README.md) for the governing resources or the
[minimal validation and integrity slice](../tools/minimal-validation-integrity-slice/README.md)
for the bounded local tool path.

## Evidence and authority boundary

These manifests are synthetic, non-normative validation inputs with fixed
expected results. Their presence, parseability, execution, or matched result
does not prove source truth, semantic correctness, complete conformance,
security, production readiness, approval, certification, release fitness,
deployment fitness, or final-human authority. Results remain individual; the
`203/38/165` inventory is not an aggregate score or quality gate.
