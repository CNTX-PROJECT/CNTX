# ADR-0024: Validation and validation output contract

- **Status:** Proposed
- **Date:** 2026-08-08
- **Issue:** [#74](https://github.com/CNTX-PROJECT/CNTX/issues/74)
- **Decision:** ARCH-024 — CNTX Validation and Validation Output Contract

## Context

CNTX Public Core has nine Accepted artifact contracts, ten Accepted JSON
Schema Draft 2020-12 resources, Core Artifact JSON Binding Version `1.0.0`, and
an exact closed Schema Resource resolution boundary. The completion roadmap
requires a separate Validation and Validation Output decision before validator
or conformance tooling.

The existing sources deliberately keep byte/encoding, JSON syntax, binding,
governing-input, resource-resolution, executable-schema, and normative-
contract failures separate. Existing synthetic schema cases provide evidence
for their governed candidates but define no portable validator API, output
format, error vocabulary, severity model, or universal conformance result.

Without a separate contract, implementations could silently collapse distinct
failures, infer contract conformance from schema success, treat blocked phases
as success or failure, mutate inputs through defaults or coercion, omit
limitations, or emit irreproducible claims.

## Decision

Define a documentation-only Validation and Validation Output contract.

One consequential validation run uses one frozen logical context containing,
as applicable, the target representation and provenance, exact Core Artifact
JSON Binding Identity/Version, exact artifact-specific Schema
Identifier/Version, complete ARCH-023-resolved resource closure and
provenance, exact Contract Definition Identifier/Version/source binding,
declared Artifact Type, and known evaluator identity/version/capabilities and
material limitations.

The decision distinguishes six conformance dimensions:

1. normative-contract conformance;
2. executable-schema conformance;
3. Artifact Instance conformance;
4. Serialization Binding conformance;
5. validator conformance; and
6. implementation conformance.

No dimension proves another or establishes truth, completeness, provenance,
authority, approval, trust, unbounded interoperability, release, or
deployment.

Logical phases preserve supplied-document/byte boundaries, parsing, binding,
governing-input verification, exact resource closure, JSON Schema evaluation,
separate normative-contract assessment, and output assembly. Physical
optimization is allowed only when semantic dependencies and separate outcomes
remain intact.

Each applicable phase receives one conceptual outcome: Satisfied, Not
Satisfied, Unverifiable, or Not Evaluated. No universal aggregate `valid`
boolean is defined. A positive dimension claim requires every applicable
prerequisite and responsibility to be Satisfied with no material failure,
unverifiability, or required non-execution.

Assertion failures, processing failures, warnings, limitations, blocked
conditions, and non-execution remain distinct. Warnings are advisory and
cannot repair or override outcomes. No portable code, message, severity,
field, schema, media type, API response, or CLI behavior is selected.

JSON Schema Draft 2020-12 Flag, Basic, Detailed, and Verbose outputs remain
standard schema-evaluation forms. None becomes a complete CNTX output. The
accepted Format-Annotation choice remains unchanged, Format-Assertion remains
unselected, annotations are not assertion failures, and `default` grants no
mutation authority.

Validation is fail-closed. Parse, binding, governing-input, or resolution
failure leaves dependent schema evaluation Not Evaluated or Unverifiable; it
does not establish schema nonconformance. Schema false means only schema Not
Satisfied, and schema success means only schema Satisfied. Coercion, repair,
fallback, defaults, warnings, and redaction cannot create success.

Future consequential outputs must be able to identify exact governing inputs,
resource closure and provenance, frozen context, processor capabilities,
every phase outcome, material diagnostics, limitations, and every blocked,
unresolved, unverifiable, or non-evaluated condition. These are logical
responsibilities, not concrete fields or serialization.

## Consequences

Positive consequences:

- failures remain attributable to their actual phase;
- schema success cannot become a universal conformance claim;
- blocked, unsupported, and unverifiable conditions remain visible;
- exact context and phase evidence support reproducibility;
- standard JSON Schema output remains usable within its proper boundary; and
- diagnostics remain constrained by security, privacy, disclosure, and non-
  authority requirements.

Tradeoffs:

- callers must supply exact governing context;
- some positive claims remain unavailable when evidence is insufficient;
- no single convenience boolean represents all CNTX conformance; and
- portable formats, tooling, evidence, certification, and release claims
  require later separate decisions.

## Alternatives rejected

- Universal `valid`: collapses distinct dimensions and outcomes.
- Schema success proves contract conformance: not all normative requirements
  are executable-schema assertions.
- Prerequisite failure means schema invalid: schema evaluation did not run.
- Warning, coercion, default, fallback, or repair creates success: validation
  grants no mutation or waiver authority.
- Bare JSON Schema Flag as complete output: governing context, provenance,
  phases, and limitations are absent.
- Custom JSON Schema output form: no custom dialect or output mechanism is
  required.
- Concrete output schema now: portable evidence and serialization remain
  separate roadmap layers.
- One result proves validator or implementation conformance: evidence and
  declared scope are insufficient.

## Security, privacy, and non-authority

Artifacts, schemas, resources, annotations, diagnostics, and outputs remain
untrusted input. Resource use must be boundable, but this decision selects no
concrete limit or mechanism.

Without separate permission, diagnostics and outputs must not expose raw
values not needed for interpretation, secrets, credentials, personal data,
production configuration, private paths/context, restricted content,
provider configuration, or private implementation details. Material redaction
or omission remains disclosed and cannot change outcomes or imply disclosure
authority.

Validation grants no access, retrieval, disclosure, truth, completeness,
provenance, authenticity, integrity, confidentiality, trust, approval,
acceptance, decision, authority, execution, release, or deployment.

## Deferred scope

Deferred and unauthorized: changes to Accepted sources, identities, versions,
schemas, tests, Binding Version `1.0.0`, or ARCH-023; Artifact Instance;
Validation Run, Validation Output, or Validator identity/version; concrete
output fields/schema/media type; portable error/severity vocabulary; universal
result object; validator, API, CLI, Portable Conformance Evidence, Conformance
Claim, suite, certification, score, badge, supported-version claim, resolver,
registry, cache, bundler, network access, digest, canonicalization, signature,
verification, trust store, workflow, runtime, provider/product work,
private/reference implementation, release, publication, or deployment.

## Acceptance and continuing gate

This candidate must receive one transparent non-independent COMMENT review on
its exact head and then stop. Creation, validation, review, repository
presence, Draft state, and mergeability do not grant acceptance.

Only separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision may authorize a later status-only promotion or other
explicitly named lifecycle action. No follow-on roadmap layer is inferred.

## References

- [ARCH-024](../validation-and-validation-output-contract.md)
- [ARCH-003](../artifact-contract-schema-architecture.md)
- [ARCH-007](../common-artifact-envelope-schema-language-dialect.md)
- [ARCH-021](../public-core-completion-boundary-roadmap.md)
- [ARCH-022](../core-artifact-serialization-binding.md)
- [ARCH-023](../schema-resource-resolution-catalog-boundary.md)
- [Schema Resource index](../../../schemas/README.md)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/)
