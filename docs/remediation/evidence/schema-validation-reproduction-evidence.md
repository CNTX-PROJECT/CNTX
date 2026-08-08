# Schema Validation Reproduction Evidence

## Classification, subject, and authority boundary

**Evidence Status:** Proposed.

**Frozen subject:** public baseline `45663112f8e253a1748543041afa9b7064b1eabc`, tree `e5b8403f64624357b8a2f9ddcc3110c3a170c456`.

**Governing task:** [REMEDIATE-001 issue #82](https://github.com/CNTX-PROJECT/CNTX/issues/82).

This is public, documentation-only reproduction evidence for all unchanged synthetic schema cases. It is logical evidence aligned with ARCH-024 and ARCH-025. It is not a canonical Portable Conformance Evidence Artifact Instance, Validation Output identity or schema, validation protocol, portable diagnostic vocabulary, certification, implementation-conformance claim, release recommendation, approval, or decision.

ARCHITECT operated both evaluators. Their implementations are diverse, but their execution is not independent human reproduction. One successful cycle cannot prove universal validator, Artifact Instance, interoperability, implementation, or release conformance.

## Frozen inputs and method

- Ten exact Accepted JSON Schema Draft 2020-12 Schema Resources were supplied by the caller from the frozen Git tree.
- Ten unchanged non-normative case manifests declared 203 cases: 38 expected valid and 165 expected invalid.
- The State Snapshot manifest's declared RFC 6901 `baseInstance` plus ordered `add`, `remove`, and `replace` construction operations were materialized mechanically before evaluation; the other manifests supplied direct `instance` values.
- No schema, manifest, instance, expected result, default, coercion, or repair was changed.
- No automatic network Schema Resource resolution, implicit discovery, hidden cache, mutable alias, fallback, or format assertion was used.
- Package acquisition used the public package registries before the frozen evaluations. Schema evaluation then used only caller-supplied local resources.

## Evaluator records

| Responsibility | Python evaluator | JavaScript evaluator |
| --- | --- | --- |
| Evaluator | `Python jsonschema` `4.26.0` | `Ajv` `8.20.0` |
| Runtime | `CPython` `3.13.14` | `Node.js` `v24.14.0` |
| Dialect | `JSON Schema Draft 2020-12` | `JSON Schema Draft 2020-12` |
| Format configuration | FormatChecker not supplied; format remains annotation-only | validateFormats=false; format remains annotation-only |
| Caller-supplied resources | 10 | 10 |
| Automatic network resolution | disabled | disabled |
| Case construction | direct instance or mechanically applied declared operations | direct instance or mechanically applied declared operations |

Python installed distributions were `jsonschema 4.26.0`, `attrs 26.1.0`, `jsonschema-specifications 2025.9.1`, `referencing 0.37.0`, and `rpds-py 2026.6.3`. The Ajv temporary lock resolved `ajv 8.20.0`, `fast-deep-equal 3.1.3`, `fast-uri 3.1.5`, `json-schema-traverse 1.0.0`, and `require-from-string 2.0.2`.

Temporary harness SHA-256 values:

- Python: `8885B6E1BC2F390268ECCACCE157F6CA5168D0DFF0A794BE45FA4419332B8965`.
- JavaScript: `C59AC0881A5A6344DF6A197082908F87797BF6BADB7FAD42AA0A76B96EEDC73C`.

Temporary full-result JSON SHA-256 values before environment cleanup:

- Python: `B92E6EE1A12EC67CC27689D66D9B6B7E3EC517E78D13800E8C28932066DF4DDA`.
- Ajv: `28949805860B1C0E5B94EBC9B0D536DD45FA9102ECEAE8705A0A6A54E22030B2`.

The result hashes provide provenance for the complete temporary machine-readable
outputs used to construct this Markdown ledger. They do not allocate a
Validation Output identity, serialization, media type, registry entry, or
canonical evidence object, and the temporary result files are not distributed.

## Reproduction commands

The paths below are role placeholders, not machine-specific locations. A reproducer must create fresh isolated directories, place the embedded harnesses there, supply the exact frozen repository, and preserve the recorded configuration.

```text
python -m pip install --disable-pip-version-check --no-input --target <temporary-python-environment>/packages jsonschema==4.26.0
PYTHONPATH=<temporary-python-environment>/packages python <temporary-python-environment>/evaluate.py <repository-root> <temporary-python-environment>/result.json
npm install --prefix <temporary-ajv-environment> --no-audit --no-fund --save-exact ajv@8.20.0
node <temporary-ajv-environment>/evaluate.js <repository-root> <temporary-ajv-environment>/result.json
```

## Aggregate observed results

| Measure | Python jsonschema | Ajv |
| --- | ---: | ---: |
| Manifests | 10 | 10 |
| Cases | 203 | 203 |
| Expected valid | 38 | 38 |
| Expected invalid | 165 | 165 |
| Actual valid | 38 | 38 |
| Actual invalid | 165 | 165 |
| Matches expected | 203 | 203 |
| Unexpected | 0 | 0 |
| Cross-evaluator validity mismatches | 0 | 0 |

Both evaluators matched all 203 declared expected-validity values and each other. This observation is bounded to these exact resources, cases, versions, runtimes, configurations, and harnesses. It does not convert the non-normative manifests into normative requirements and does not establish an aggregate readiness result.

## Per-manifest summary

| Manifest | Cases | Expected valid | Expected invalid | Python unexpected | Ajv unexpected | Cross mismatch |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 31 | 11 | 20 | 0 | 0 | 0 |
| `tests/schemas/context-packet/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/decision-record/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/execution-result/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/project-charter/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/review-record/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 20 | 3 | 17 | 0 | 0 | 0 |
| `tests/schemas/task-contract/1.0.0/cases.json` | 16 | 3 | 13 | 0 | 0 | 0 |
| `tests/schemas/workstream/1.0.0/cases.json` | 16 | 3 | 13 | 0 | 0 | 0 |

## Complete case ledger

`V` means valid and `I` means invalid. Diagnostics are bounded JSON Schema keyword categories, not a portable error vocabulary.

| Manifest | # | Case | Expected | Python | Ajv | Agreement | Diagnostic category | Keywords |
| --- | ---: | --- | :---: | :---: | :---: | :---: | --- | --- |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 0 | valid project charter envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 1 | valid workstream envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 2 | valid task contract envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 3 | valid context packet envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 4 | valid execution result envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 5 | valid evidence bundle envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 6 | valid review record envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 7 | valid decision record envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 8 | valid state snapshot envelope | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 9 | valid complete evidence capabilities | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 10 | valid zero components semantic versions | V | V | V | yes | none | none |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 11 | invalid missing artifact type | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 12 | invalid unknown artifact type | I | I | I | yes | assertion-failure | `enum` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 13 | invalid blank artifact identifier | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 14 | invalid artifact pin missing revision | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 15 | invalid contract pin missing version | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 16 | invalid semantic version with leading zero | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 17 | invalid semantic version with prerelease | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 18 | invalid null provenance placeholder | I | I | I | yes | assertion-failure | `type` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 19 | invalid empty provenance array | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 20 | invalid incomplete artifact reference | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 21 | invalid unknown reference kind | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 22 | invalid duplicate provenance entries | I | I | I | yes | assertion-failure | `uniqueItems` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 23 | invalid empty digest array | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 24 | invalid digest blank method | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 25 | invalid digest missing subject | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 26 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 27 | invalid authority field | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 28 | invalid lifecycle field | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 29 | invalid extension field | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/common-artifact-envelope/1.0.0/cases.json` | 30 | invalid nested unknown pin property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 0 | valid minimal assessed reference-only packet | V | V | V | yes | none | none |
| `tests/schemas/context-packet/1.0.0/cases.json` | 1 | valid fully specified Unicode packet with mixed included and reference-only sources | V | V | V | yes | none | none |
| `tests/schemas/context-packet/1.0.0/cases.json` | 2 | valid packet with optional common provenance and digest evidence | V | V | V | yes | none | none |
| `tests/schemas/context-packet/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 4 | invalid missing payload | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 5 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 6 | invalid Artifact Type and governing Contract and Schema coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 7 | invalid incomplete Common Artifact Envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 8 | invalid missing governing Task Contract pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 9 | invalid embedded governing Task Contract | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 10 | invalid missing payload responsibility | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 11 | invalid unknown payload and nested property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 12 | invalid selected source missing reference relevance and revision context | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 13 | invalid unknown content treatment token | I | I | I | yes | assertion-failure | `enum` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 14 | invalid blank ordinary string | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 15 | invalid empty and duplicate required collections | I | I | I | yes | assertion-failure | `minItems`, `uniqueItems` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 16 | invalid declaration set | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 17 | invalid null and wrong type | I | I | I | yes | assertion-failure | `type` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 18 | invalid approval access retrieval ranking prompt workflow execution configuration extension and runtime fields | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/context-packet/1.0.0/cases.json` | 19 | invalid embedded Project Charter Workstream Execution Result and peer artifact | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 0 | valid minimal bounded affirmative decision with separated authority timing and no downstream effect | V | V | V | yes | none | none |
| `tests/schemas/decision-record/1.0.0/cases.json` | 1 | valid qualified conditional decision with exact result evidence review pins uncertainty dissent and separate integration authority | V | V | V | yes | none | none |
| `tests/schemas/decision-record/1.0.0/cases.json` | 2 | valid amendment and supersession with peer conflict resolution restricted basis distinct timing and preserved history | V | V | V | yes | none | none |
| `tests/schemas/decision-record/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 4 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 5 | invalid wrong artifact type | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 6 | invalid wrong governing contract coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 7 | invalid wrong governing schema coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 8 | invalid missing decision authority and decision maker responsibility | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 9 | invalid blank maker and incomplete authority separation | I | I | I | yes | assertion-failure | `pattern`, `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 10 | invalid malformed approved revision and approval provenance | I | I | I | yes | assertion-failure | `minLength`, `pattern`, `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 11 | invalid malformed decision boundary question and bundled unrelated decision | I | I | I | yes | assertion-failure | `additionalProperties`, `pattern` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 12 | invalid missing state snapshot relationship category | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 13 | invalid empty rationale basis and governing source declaration | I | I | I | yes | assertion-failure | `minItems`, `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 14 | invalid collapsed timing and missing temporal applicability | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 15 | invalid malformed evidence declaration and input as approval | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 16 | invalid malformed peer change relation and latest wins rule | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 17 | invalid automatic downstream effect and execution engine property | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 18 | invalid missing mandatory security privacy access disclosure and restricted basis responsibility | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/decision-record/1.0.0/cases.json` | 19 | invalid composite unknown null duplicate embedded score confidence priority voting majority consensus signature workflow runtime and implementation shape | I | I | I | yes | assertion-failure | `additionalProperties`, `uniqueItems` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 0 | valid minimal insufficiency bundle with explicit missing evidence | V | V | V | yes | none | none |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 1 | valid direct supporting and contradictory evidence with opaque pins | V | V | V | yes | none | none |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 2 | valid derived and redacted evidence with provenance and lifecycle traceability | V | V | V | yes | none | none |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 4 | invalid additional root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 5 | invalid wrong Evidence Bundle Artifact Type | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 6 | invalid wrong governing Contract Definition coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 7 | invalid wrong governing Schema coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 8 | invalid missing governing Task Contract pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 9 | invalid blank governing Task Contract revision | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 10 | invalid empty reviewable subjects | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 11 | invalid reviewable subject without exact revision | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 12 | invalid specified evidence with empty items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 13 | invalid assessed-none evidence with items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 14 | invalid unknown representation treatment | I | I | I | yes …3177 tokens truncated…ority boundary | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 15 | invalid claim traceability without claim reference | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 16 | invalid empty claim evidence traceability | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 17 | invalid missing mandatory security privacy access disclosure and retention responsibility | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 18 | invalid additional payload property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/evidence-bundle/1.0.0/cases.json` | 19 | invalid nested blank duplicate null embedded authority workflow runtime and implementation shape | I | I | I | yes | assertion-failure | `additionalProperties`, `oneOf`, `pattern`, `type`, `uniqueItems` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 0 | valid minimal stopped result with assessed absence | V | V | V | yes | none | none |
| `tests/schemas/execution-result/1.0.0/cases.json` | 1 | valid fully specified Unicode result with mixed claims | V | V | V | yes | none | none |
| `tests/schemas/execution-result/1.0.0/cases.json` | 2 | valid result with optional common provenance and digest evidence | V | V | V | yes | none | none |
| `tests/schemas/execution-result/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 4 | invalid missing payload | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 5 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 6 | invalid Artifact Type and governing Contract and Schema coordinates | I | I | I | yes | assertion-failure | `const`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 7 | invalid incomplete Common Artifact Envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 8 | invalid missing or incomplete governing Task Contract pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 9 | invalid Context Packet pin declaration and embedded Context Packet | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 10 | invalid missing payload responsibility | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 11 | invalid unknown payload and nested property | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 12 | invalid malformed provenance entry | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 13 | invalid treatment check outcome and criteria assessment tokens | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `enum`, `oneOf`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 14 | invalid blank ordinary string | I | I | I | yes | assertion-failure | `pattern`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 15 | invalid empty and duplicate required collections | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf`, `required`, `uniqueItems` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 16 | invalid statement artifact pin and check claim declarations | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 17 | invalid null and wrong type | I | I | I | yes | assertion-failure | `oneOf`, `required`, `type` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 18 | invalid approval acceptance merge release deployment workflow execution access mutation extension runtime and product fields | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/execution-result/1.0.0/cases.json` | 19 | invalid embedded governing peer and downstream artifacts | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 0 | valid minimal assessed project charter | V | V | V | yes | none | none |
| `tests/schemas/project-charter/1.0.0/cases.json` | 1 | valid fully specified unicode project charter | V | V | V | yes | none | none |
| `tests/schemas/project-charter/1.0.0/cases.json` | 2 | valid project charter with common provenance and digest evidence | V | V | V | yes | none | none |
| `tests/schemas/project-charter/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 4 | invalid missing payload | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 5 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 6 | invalid wrong artifact type | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 7 | invalid wrong governing contract identifier and version | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 8 | invalid wrong governing schema identifier and version | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 9 | invalid incomplete common artifact instance pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 10 | invalid missing required purpose | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 11 | invalid unknown payload and nested properties | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 12 | invalid blank purpose and empty desired outcomes | I | I | I | yes | assertion-failure | `minItems`, `pattern` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 13 | invalid duplicate principles and wrong purpose type | I | I | I | yes | assertion-failure | `type`, `uniqueItems` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 14 | invalid null declaration and empty declaration object | I | I | I | yes | assertion-failure | `oneOf`, `required`, `type` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 15 | invalid specified declaration missing items | I | I | I | yes | assertion-failure | `const`, `oneOf`, `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 16 | invalid specified declaration with empty items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 17 | invalid none declaration with items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 18 | invalid unknown declaration disposition | I | I | I | yes | assertion-failure | `const`, `oneOf`, `required` |
| `tests/schemas/project-charter/1.0.0/cases.json` | 19 | invalid forbidden approval execution and extension fields | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/review-record/1.0.0/cases.json` | 0 | valid minimal inconclusive single-subject review with no recommendation | V | V | V | yes | none | none |
| `tests/schemas/review-record/1.0.0/cases.json` | 1 | valid execution-result and evidence-bundle review with supporting and adverse findings | V | V | V | yes | none | none |
| `tests/schemas/review-record/1.0.0/cases.json` | 2 | valid peer comparison with dissent redaction loss later evidence and correction traceability | V | V | V | yes | none | none |
| `tests/schemas/review-record/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 4 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/review-record/1.0.0/cases.json` | 5 | invalid wrong artifact type | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/review-record/1.0.0/cases.json` | 6 | invalid wrong contract coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/review-record/1.0.0/cases.json` | 7 | invalid wrong schema coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/review-record/1.0.0/cases.json` | 8 | invalid missing review authority specialty and reviewer | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 9 | invalid blank reviewer reference | I | I | I | yes | assertion-failure | `pattern` |
| `tests/schemas/review-record/1.0.0/cases.json` | 10 | invalid execution authority specified with empty items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf` |
| `tests/schemas/review-record/1.0.0/cases.json` | 11 | invalid empty reviewable subjects | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/review-record/1.0.0/cases.json` | 12 | invalid subject without exact revision | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 13 | invalid missing state snapshot relationship category | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 14 | invalid empty findings | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/review-record/1.0.0/cases.json` | 15 | invalid finding without distinct interpretation | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 16 | invalid evidence finding traceability without local finding reference | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 17 | invalid empty specified recommendations with approval property | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf` |
| `tests/schemas/review-record/1.0.0/cases.json` | 18 | invalid missing mandatory security privacy access disclosure and retention | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/review-record/1.0.0/cases.json` | 19 | invalid prohibited embedded artifact score severity confidence approval voting workflow and runtime shape | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `type`, `uniqueItems` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 0 | valid minimal fully pinned bounded orientation after reported integration | V | V | V | yes | none | none |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 1 | valid partial stopped state with unpinned source uncertainty and separate continuation authority | V | V | V | yes | none | none |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 2 | valid correction and supersession with stale assessments restricted omission and bounded handoff | V | V | V | yes | none | none |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 4 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 5 | invalid wrong artifact type | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 6 | invalid wrong governing Contract Definition coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 7 | invalid wrong governing Schema coordinates | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 8 | invalid missing derivation authority classification and non-authority responsibility | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 9 | invalid authoritative classification and malformed authority boundary | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 10 | invalid missing governing conflict precedence boundary | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 11 | invalid source has neither exact revision nor complete pinning limitation | I | I | I | yes | assertion-failure | `const`, `oneOf`, `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 12 | invalid collapsed temporal coordinates and unsupported freshness token | I | I | I | yes | assertion-failure | `enum`, `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 13 | invalid empty selected minimum context | I | I | I | yes | assertion-failure | `minItems` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 14 | invalid malformed reported completion claim separation | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 15 | invalid evidence input represented as approval proof | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 16 | invalid missing peer State Snapshot relationship category | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 17 | invalid malformed verification gap and remaining action declarations | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required`, `type` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 18 | invalid peer dependency encodes latest-wins and omits non-automatic effect | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/state-snapshot/1.0.0/cases.json` | 19 | invalid composite unknown blank duplicate null embedded and implementation shape | I | I | I | yes | assertion-failure | `additionalProperties`, `oneOf`, `pattern`, `type`, `uniqueItems` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 0 | valid minimal assessed task contract | V | V | V | yes | none | none |
| `tests/schemas/task-contract/1.0.0/cases.json` | 1 | valid fully specified unicode task contract | V | V | V | yes | none | none |
| `tests/schemas/task-contract/1.0.0/cases.json` | 2 | valid task contract with common provenance and digest evidence | V | V | V | yes | none | none |
| `tests/schemas/task-contract/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 4 | invalid missing payload | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 5 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 6 | invalid wrong artifact type and governing definition pins | I | I | I | yes | assertion-failure | `const` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 7 | invalid incomplete common artifact instance pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 8 | invalid incomplete governing Project Charter and Workstream pins | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 9 | invalid missing required payload member and unknown nested property | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 10 | invalid blank strings empty arrays duplicate items and wrong type | I | I | I | yes | assertion-failure | `minItems`, `pattern`, `type`, `uniqueItems` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 11 | invalid null and empty declaration objects | I | I | I | yes | assertion-failure | `oneOf`, `required`, `type` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 12 | invalid specified declarations missing and empty items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf`, `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 13 | invalid none declaration with items and unknown disposition | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 14 | invalid forbidden approval permission workflow and lifecycle status fields | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/task-contract/1.0.0/cases.json` | 15 | invalid embedded governing peer and downstream artifacts | I | I | I | yes | assertion-failure | `additionalProperties` |
| `tests/schemas/workstream/1.0.0/cases.json` | 0 | valid minimal assessed workstream | V | V | V | yes | none | none |
| `tests/schemas/workstream/1.0.0/cases.json` | 1 | valid fully specified unicode workstream | V | V | V | yes | none | none |
| `tests/schemas/workstream/1.0.0/cases.json` | 2 | valid workstream with common provenance and digest evidence | V | V | V | yes | none | none |
| `tests/schemas/workstream/1.0.0/cases.json` | 3 | invalid missing envelope | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 4 | invalid missing payload | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 5 | invalid unknown root property | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 6 | invalid wrong artifact type and governing definition pins | I | I | I | yes | assertion-failure | `const`, `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 7 | invalid incomplete common artifact instance pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 8 | invalid incomplete governing Project Charter pin | I | I | I | yes | assertion-failure | `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 9 | invalid missing required payload member and unknown nested properties | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 10 | invalid blank strings empty arrays duplicate items and wrong type | I | I | I | yes | assertion-failure | `minItems`, `minLength`, `pattern`, `required`, `type`, `uniqueItems` |
| `tests/schemas/workstream/1.0.0/cases.json` | 11 | invalid null and empty declaration objects | I | I | I | yes | assertion-failure | `oneOf`, `required`, `type` |
| `tests/schemas/workstream/1.0.0/cases.json` | 12 | invalid specified declarations missing and empty items | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `minItems`, `oneOf`, `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 13 | invalid none declaration with items and unknown disposition | I | I | I | yes | assertion-failure | `additionalProperties`, `const`, `oneOf`, `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 14 | invalid blank declared state and forbidden approval execution extension and runtime fields | I | I | I | yes | assertion-failure | `additionalProperties`, `pattern`, `required` |
| `tests/schemas/workstream/1.0.0/cases.json` | 15 | invalid embedded Project Charter peer Workstream and Task Contract artifacts | I | I | I | yes | assertion-failure | `additionalProperties`, `required` |

## Embedded Python harness

```python
import copy
import json
import platform
import sys
from importlib import metadata
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def pointer_tokens(pointer: str):
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ValueError(f"invalid JSON Pointer: {pointer}")
    return [token.replace("~1", "/").replace("~0", "~") for token in pointer[1:].split("/")]


def materialize_instance(manifest, case):
    if "instance" in case:
        return case["instance"]
    instance = copy.deepcopy(manifest["baseInstance"])
    for operation in case["operations"]:
        tokens = pointer_tokens(operation["path"])
        parent = instance
        for token in tokens[:-1]:
            parent = parent[int(token)] if isinstance(parent, list) else parent[token]
        terminal = tokens[-1]
        if operation["op"] == "remove":
            if isinstance(parent, list):
                parent.pop(int(terminal))
            else:
                del parent[terminal]
        elif operation["op"] == "replace":
            if isinstance(parent, list):
                parent[int(terminal)] = copy.deepcopy(operation["value"])
            else:
                parent[terminal] = copy.deepcopy(operation["value"])
        elif operation["op"] == "add":
            value = copy.deepcopy(operation["value"])
            if isinstance(parent, list):
                parent.append(value) if terminal == "-" else parent.insert(int(terminal), value)
            else:
                parent[terminal] = value
        else:
            raise ValueError(f"unsupported operation: {operation['op']}")
    return instance


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: evaluate.py REPOSITORY_ROOT OUTPUT_JSON")

    root = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    schema_paths = sorted((root / "schemas").glob("*/1.0.0/schema.json"))
    manifest_paths = sorted((root / "tests" / "schemas").glob("*/1.0.0/cases.json"))

    schemas = [(path, load_json(path)) for path in schema_paths]
    resources = [(schema["$id"], Resource.from_contents(schema)) for _, schema in schemas]
    registry = Registry().with_resources(resources)
    schema_by_id = {schema["$id"]: (path, schema) for path, schema in schemas}

    results = []
    for manifest_path in manifest_paths:
        manifest = load_json(manifest_path)
        schema_id = manifest["schemaId"]
        schema_path, schema = schema_by_id[schema_id]
        validator = Draft202012Validator(schema, registry=registry)
        for index, case in enumerate(manifest["cases"]):
            errors = sorted(
                validator.iter_errors(materialize_instance(manifest, case)),
                key=lambda error: (list(error.absolute_path), list(error.absolute_schema_path)),
            )
            actual = not errors
            keywords = sorted({str(error.validator) for error in errors})
            results.append(
                {
                    "manifest": manifest_path.relative_to(root).as_posix(),
                    "schema": schema_path.relative_to(root).as_posix(),
                    "schemaId": schema_id,
                    "caseIndex": index,
                    "caseName": case["name"],
                    "expectedValid": bool(case["valid"]),
                    "actualValid": actual,
                    "matchesExpected": actual == bool(case["valid"]),
                    "diagnosticCategory": "none" if actual else "assertion-failure",
                    "keywords": keywords,
                    "errorCount": len(errors),
                }
            )

    distribution_names = [
        "jsonschema",
        "attrs",
        "jsonschema-specifications",
        "referencing",
        "rpds-py",
    ]
    record = {
        "evaluator": "Python jsonschema",
        "evaluatorVersion": metadata.version("jsonschema"),
        "runtime": "CPython",
        "runtimeVersion": platform.python_version(),
        "implementation": platform.python_implementation(),
        "dialect": "JSON Schema Draft 2020-12",
        "formatConfiguration": "FormatChecker not supplied; format remains annotation-only",
        "automaticNetworkResolution": False,
        "callerSuppliedResourceCount": len(resources),
        "manifestCount": len(manifest_paths),
        "caseCount": len(results),
        "expectedValidCount": sum(item["expectedValid"] for item in results),
        "expectedInvalidCount": sum(not item["expectedValid"] for item in results),
        "actualValidCount": sum(item["actualValid"] for item in results),
        "actualInvalidCount": sum(not item["actualValid"] for item in results),
        "matchesExpectedCount": sum(item["matchesExpected"] for item in results),
        "unexpectedCount": sum(not item["matchesExpected"] for item in results),
        "dependencies": {name: metadata.version(name) for name in distribution_names},
        "results": results,
    }
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Embedded JavaScript harness

```javascript
const fs = require("fs");
const path = require("path");
const Ajv2020 = require("ajv/dist/2020").default;
const packageInfo = require("ajv/package.json");

function loadJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function resourcePaths(root, subtree) {
  return fs.readdirSync(path.join(root, subtree), { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => path.join(root, subtree, entry.name, "1.0.0", subtree === "schemas" ? "schema.json" : "cases.json"))
    .filter((filePath) => fs.existsSync(filePath))
    .sort();
}

function relative(root, filePath) {
  return path.relative(root, filePath).split(path.sep).join("/");
}

function pointerTokens(pointer) {
  if (pointer === "") return [];
  if (!pointer.startsWith("/")) throw new Error(`invalid JSON Pointer: ${pointer}`);
  return pointer.slice(1).split("/").map((token) => token.replace(/~1/g, "/").replace(/~0/g, "~"));
}

function materializeInstance(manifest, testCase) {
  if (Object.prototype.hasOwnProperty.call(testCase, "instance")) return testCase.instance;
  const instance = JSON.parse(JSON.stringify(manifest.baseInstance));
  for (const operation of testCase.operations) {
    const tokens = pointerTokens(operation.path);
    let parent = instance;
    for (const token of tokens.slice(0, -1)) parent = parent[Array.isArray(parent) ? Number(token) : token];
    const terminal = tokens[tokens.length - 1];
    if (operation.op === "remove") {
      if (Array.isArray(parent)) parent.splice(Number(terminal), 1);
      else delete parent[terminal];
    } else if (operation.op === "replace") {
      parent[Array.isArray(parent) ? Number(terminal) : terminal] = JSON.parse(JSON.stringify(operation.value));
    } else if (operation.op === "add") {
      const value = JSON.parse(JSON.stringify(operation.value));
      if (Array.isArray(parent)) {
        if (terminal === "-") parent.push(value);
        else parent.splice(Number(terminal), 0, value);
      } else parent[terminal] = value;
    } else {
      throw new Error(`unsupported operation: ${operation.op}`);
    }
  }
  return instance;
}

function main() {
  if (process.argv.length !== 4) {
    throw new Error("usage: node evaluate.js REPOSITORY_ROOT OUTPUT_JSON");
  }

  const root = path.resolve(process.argv[2]);
  const output = path.resolve(process.argv[3]);
  const schemaPaths = resourcePaths(root, "schemas");
  const manifestPaths = resourcePaths(root, path.join("tests", "schemas"));
  const schemas = schemaPaths.map((schemaPath) => [schemaPath, loadJson(schemaPath)]);
  const schemaById = new Map(schemas.map(([schemaPath, schema]) => [schema.$id, [schemaPath, schema]]));
  const ajv = new Ajv2020({
    allErrors: true,
    strict: false,
    validateFormats: false,
    addUsedSchema: true,
  });
  for (const [, schema] of schemas) {
    ajv.addSchema(schema, schema.$id);
  }

  const results = [];
  for (const manifestPath of manifestPaths) {
    const manifest = loadJson(manifestPath);
    const [schemaPath] = schemaById.get(manifest.schemaId);
    const validate = ajv.getSchema(manifest.schemaId);
    if (!validate) {
      throw new Error(`caller-supplied schema unavailable: ${manifest.schemaId}`);
    }
    manifest.cases.forEach((testCase, caseIndex) => {
      const actualValid = Boolean(validate(materializeInstance(manifest, testCase)));
      const errors = validate.errors ? JSON.parse(JSON.stringify(validate.errors)) : [];
      const keywords = [...new Set(errors.map((error) => error.keyword))].sort();
      results.push({
        manifest: relative(root, manifestPath),
        schema: relative(root, schemaPath),
        schemaId: manifest.schemaId,
        caseIndex,
        caseName: testCase.name,
        expectedValid: Boolean(testCase.valid),
        actualValid,
        matchesExpected: actualValid === Boolean(testCase.valid),
        diagnosticCategory: actualValid ? "none" : "assertion-failure",
        keywords,
        errorCount: errors.length,
      });
    });
  }

  const record = {
    evaluator: "Ajv",
    evaluatorVersion: packageInfo.version,
    runtime: "Node.js",
    runtimeVersion: process.version,
    implementation: "V8 JavaScript runtime",
    dialect: "JSON Schema Draft 2020-12",
    formatConfiguration: "validateFormats=false; format remains annotation-only",
    automaticNetworkResolution: false,
    callerSuppliedResourceCount: schemas.length,
    manifestCount: manifestPaths.length,
    caseCount: results.length,
    expectedValidCount: results.filter((item) => item.expectedValid).length,
    expectedInvalidCount: results.filter((item) => !item.expectedValid).length,
    actualValidCount: results.filter((item) => item.actualValid).length,
    actualInvalidCount: results.filter((item) => !item.actualValid).length,
    matchesExpectedCount: results.filter((item) => item.matchesExpected).length,
    unexpectedCount: results.filter((item) => !item.matchesExpected).length,
    results,
  };
  fs.writeFileSync(output, JSON.stringify(record, null, 2) + "\n", "utf8");
}

main();
```

## Adverse evidence, limitations, and non-claims

- No mismatch, processing failure, or unexpected validity was observed, but absence in this bounded cycle does not prove absence across other implementations or inputs.
- Both runs were operated by ARCHITECT in one environment and are not independent human reproduction.
- Package registries and runtime distributions were external supply dependencies during setup; no package or runtime is supplied by CNTX.
- The committed record contains the method, complete harness source, versions, aggregate results, and all case outcomes, but not a canonical serialized Validation Output or Portable Conformance Evidence object.
- Diagnostic keyword categories are implementation observations and cannot be treated as a stable portable vocabulary.
- No validator, runner, dependency manifest, virtual environment, `node_modules`, workflow, API, CLI, resolver, cache, or executable harness is committed.
- This evidence performs no acceptance, readiness recommendation, release approval, publication, support commitment, certification, or deployment.

## Reproduction and correction boundary

A later reproducer must pin the exact Git tree, evaluator and runtime versions, dependency closure, ten caller-supplied resources, harness hashes, and format configuration. Any later difference must remain visible with its environment and evidence; it must not overwrite this historical record or silently change schemas, manifests, expected outcomes, or Accepted decisions.

This evidence is Proposed until separately accepted. Its integration would supply materially new executed evidence for a later ASSESS-002, but would not authorize or predetermine that reassessment.
