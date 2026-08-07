# CNTX Validation and Validation Output Contract (ARCH-024)

## Status and authority

**Document Status:** Accepted.

This document is an Accepted, documentation-only architecture decision governed
by [issue #74](https://github.com/CNTX-PROJECT/CNTX/issues/74) and recorded by
[ADR-0024](adr/0024-validation-and-validation-output-contract.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in
issue comment `5222505304`. EIGENAAR / Final Authority acceptance of the exact
reviewed candidate is recorded in issue comment `5222756874`. Governed
integration to `main` adopts this exact decision. Creation, repository
presence, validation, and a transparent non-independent review did not grant
acceptance.

This decision remains subordinate to Accepted architecture, artifact
contracts, executable schemas, the Accepted Core Artifact JSON Binding, the
Accepted Schema Resource Resolution and Catalog Boundary, repository
governance, security and privacy boundaries, controlling sources, and final
human authority. It changes none of those sources.

Within this document, **MUST** and **MUST NOT** express mandatory requirements,
**SHOULD** and **SHOULD NOT** express strong recommendations, and **MAY**
express permission. These terms express requirement strength only within this
Accepted decision.

## Purpose and decision boundary

CNTX Public Core has nine Accepted artifact contracts, ten Accepted JSON
Schema Draft 2020-12 Schema Resources, an Accepted Core Artifact JSON Binding,
and an Accepted closed Schema Resource resolution boundary. Those sources do
not yet define one bounded contract for validation inputs, phases, outcomes,
failure attribution, warnings, limitations, reproducibility, or validation-
output responsibilities.

This decision therefore defines:

1. the exact logical context required for a consequential validation run;
2. six distinct conformance dimensions;
3. logical validation phases and their dependencies;
4. four conceptual outcome categories;
5. failure-layer, error, warning, limitation, and diagnostic boundaries;
6. the relationship to JSON Schema Draft 2020-12 output;
7. fail-closed claim rules;
8. reproducibility and output responsibilities;
9. validator- and implementation-conformance non-proof boundaries; and
10. security, privacy, resource, disclosure, and non-authority limits.

This decision is not a validator, validation-output schema, portable error
vocabulary, severity model, universal conformance result, Artifact Instance,
Conformance Claim, evidence protocol, API, CLI, tool, implementation, release,
publication, or deployment.

## Governing traceability

| Governing source | Constraint preserved by this decision |
| --- | --- |
| [ARCH-001](core-contract.md) and [ADR-0001](adr/0001-public-core-boundaries.md) | Final human authority, bounded work, evidence-before-claims, security/privacy, and the public/private boundary remain unchanged. |
| [ARCH-002](contract-identity-versioning.md) and [ADR-0002](adr/0002-contract-identity-versioning.md) | Identity, version, status, location, provenance, implementation, digest, acceptance, and authority remain separate dimensions. |
| [ARCH-003](artifact-contract-schema-architecture.md) and [ADR-0003](adr/0003-artifact-contract-schema-layering.md) | Normative contracts, executable schemas, validation, evidence, review, decision, and implementation remain separate layers. |
| [ARCH-007](common-artifact-envelope-schema-language-dialect.md) and [ADR-0007](adr/0007-common-artifact-envelope-schema-language-dialect.md) | JSON Schema Draft 2020-12 and the selected standard vocabulary profile remain fixed; Format-Annotation remains selected and Format-Assertion remains unselected. |
| [ARCH-008](common-artifact-envelope-schema-composition-packaging.md) and [ADR-0008](adr/0008-common-artifact-envelope-schema-composition-packaging.md) | Exact static references, identity-preserving bundles, offline-first supply, no automatic network access, and fail-closed unresolved resources remain mandatory. |
| [ARCH-009](common-artifact-envelope-executable-schema.md) through [ARCH-020](state-snapshot-executable-schema.md), with their ADRs | The ten Accepted Schema Versions `1.0.0`, their assertions, identities, reference topology, synthetic cases, and version lines remain unchanged. |
| [ARCH-021](public-core-completion-boundary-roadmap.md) and [ADR-0021](adr/0021-public-core-completion-boundary-roadmap.md) | Validation and validation-output responsibilities precede validator or conformance tooling and remain separate from portable evidence and release readiness. |
| [ARCH-022](core-artifact-serialization-binding.md) and [ADR-0022](adr/0022-core-artifact-serialization-binding.md) | Core Artifact JSON Binding Version `1.0.0`, its governing inputs, and its distinct transport, byte, syntax, binding, schema, and contract failure layers remain unchanged. |
| [ARCH-023](schema-resource-resolution-catalog-boundary.md) and [ADR-0023](adr/0023-schema-resource-resolution-catalog-boundary.md) | Exact Schema Resource keys, a frozen caller-supplied context, complete transitive closure, no automatic network access, and fail-closed resolution remain prerequisites. |
| [CONTRACT-001 through CONTRACT-009](../contracts/README.md) | Validation changes no contract purpose, authority boundary, artifact relationship, provenance, lifecycle, security, privacy, or final-human-authority meaning. |

## Terminology

| Term | Meaning in this decision | Not implied |
| --- | --- | --- |
| **Validation run** | One bounded evaluation attempt over one frozen logical context. | An allocated identity, Artifact Instance, persistent record, approval, or authority. |
| **Validation context** | The target, exact governing pins, resolved resources, provenance, processor capabilities, and material limitations fixed for one run. | Retrieval authority, trust, acceptance, mutation permission, or a concrete object format. |
| **Validation phase** | One logically distinct part of evaluation with explicit prerequisites and one outcome. | A required implementation process, API method, CLI step, or serialized section. |
| **Conformance dimension** | One separately governed question about contract, schema, Artifact Instance, binding, validator, or implementation behavior. | A universal result or proof of another dimension. |
| **Outcome category** | One conceptual classification of a phase as Satisfied, Not Satisfied, Unverifiable, or Not Evaluated. | A concrete token, field, code, severity, or aggregate `valid` value. |
| **Assertion failure** | An evaluated applicable requirement was not satisfied. | Parser failure, processor failure, unavailable evidence, or non-execution. |
| **Processing failure** | Evaluation could not complete because required processing failed or was unsupported. | An assertion about the target being false. |
| **Warning** | Advisory information that does not change an outcome. | Repair, waiver, approval, authority, or permission to continue. |
| **Limitation** | A material bound, unsupported capability, assumption, omission, redaction, or evidence constraint affecting interpretation. | Automatic failure, success, or permission to conceal an outcome. |
| **Validation output** | The logical responsibilities for preserving inputs, phase outcomes, diagnostics, limitations, and blocked conditions. | A schema, format, Artifact Instance, media type, API response, or persistent report. |

## Exact validation-context responsibilities

A consequential validation run MUST receive or identify, as applicable:

1. the target artifact representation;
2. the supplied representation boundary and available provenance;
3. exact Core Artifact JSON Binding Identity and Binding Version `1.0.0`;
4. exact artifact-specific Schema Identifier and Schema Version;
5. the exact entry Schema Resource;
6. the complete ARCH-023-resolved transitive Schema Resource closure;
7. governing Accepted Schema Resource provenance;
8. exact Contract Definition Identifier;
9. exact Contract Definition Version;
10. exact Accepted contract source binding;
11. declared Artifact Type; and
12. evaluator implementation identity, evaluator version, supported
    capabilities, unsupported capabilities, and material resource limitations
    when known.

These are logical responsibilities only. This decision assigns no concrete
field name, property, JSON shape, schema, identifier syntax, serialization,
API parameter, CLI option, repository file, or persistence model.

Artifact Identity, Artifact Revision, Contract Definition Identity/Version,
Schema Identity/Version, Serialization Binding Identity/Version, validation-
run identity, validator identity, implementation identity, status, location,
provenance, digest, authority, approval, applicability, trust, and acceptance
MUST remain separate dimensions.

A repository path, filename, branch, mutable alias, `latest`, cache key,
retrieval coordinate, display title, successful HTTP response, local object
identity, or validator default MUST NOT replace an exact governing input.

## Frozen validation context

During one validation run, the following MUST remain fixed:

- target representation;
- governing Binding Identity and Version;
- governing Schema Identifier and Version;
- complete resolved Schema Resource closure;
- Contract Definition Identifier, Version, and source binding;
- declared Artifact Type;
- evaluator capability declaration;
- applicable resource limitations; and
- all provenance used in the claim.

Validation MUST NOT silently retrieve resources, use automatic network access,
select `latest`, refresh a cache, follow a redirect, substitute a resource,
change a governing version, select another contract, infer a missing
identifier, mutate the target, coerce a value, insert a default, repair
malformed input, discard a failure, broaden disclosure, or change context
between phases.

If context changes, the result belongs to a distinct validation run and MUST
NOT be represented as the same evaluation.

## Separate conformance dimensions

| Dimension | Exact question | Boundary |
| --- | --- | --- |
| **Normative-contract conformance** | Does the exact subject satisfy every applicable normative responsibility of the exact Contract Definition Identifier/Version and Accepted source binding that can be reliably assessed from the supplied context and evidence? | Schema success cannot establish this dimension; non-machine-verifiable responsibilities remain separate. |
| **Executable-schema conformance** | Does the parsed JSON instance satisfy the assertions of the exact applicable Schema Version under JSON Schema Draft 2020-12 using the exact resolved Schema Resource closure and selected vocabulary behavior? | Establishes no contract, truth, provenance, authority, approval, trust, or implementation conformance. |
| **Artifact Instance conformance** | Can the exact identified Artifact Instance revision, its governing pins, and its available provenance be shown to satisfy every applicable Artifact-Instance responsibility? | Cannot be claimed from an anonymous, mutated, or insufficiently pinned representation. |
| **Serialization Binding conformance** | Does the supplied representation satisfy Core Artifact JSON Binding Version `1.0.0`, including document, UTF-8, BOM, duplicate-name, JSON-syntax, and binding requirements? | Establishes no executable-schema or normative-contract conformance. |
| **Validator conformance** | Does a validator implementation correctly implement applicable Accepted validation, binding, schema, resolution, and output responsibilities across sufficient governed evidence? | One artifact result cannot certify a validator. |
| **Implementation conformance** | Does a broader implementation satisfy every applicable CNTX requirement within an exact supported scope and version set? | Validator conformance cannot establish broader implementation conformance; neither grants certification, release, or deployment. |

No dimension MUST be treated as a synonym or proof of another. No dimension
proves truth, completeness, provenance, authenticity, trust, approval,
acceptance, decision, permission, access, disclosure, authority, unbounded
interoperability, or support for an untested or unpinned version.

## Logical validation phases and dependencies

| Order | Logical phase | Required boundary |
| --- | --- | --- |
| 1 | Supplied-document and byte-acquisition boundary | Transport before this boundary remains external. |
| 2 | Byte/encoding and JSON parsing | Bytes must be available; UTF-8, BOM, duplicate-name, and JSON-syntax requirements remain distinct. |
| 3 | Core Artifact JSON Binding evaluation | Binding prerequisites must be evaluated before a positive binding claim. |
| 4 | Governing-input verification | Exact binding, schema, contract, Artifact Type, resource, and provenance pins must be available as applicable. |
| 5 | Schema Resource closure resolution | The exact ARCH-023 frozen resource context and complete transitive closure are prerequisites. |
| 6 | JSON Schema Draft 2020-12 evaluation | Only the parsed JSON instance and exact resolved schema context are evaluated. |
| 7 | Separately evaluable normative-contract assessment | Schema results do not substitute for contract responsibilities or evidence. |
| 8 | Validation-claim/output assembly | Every earlier outcome, failure, warning, limitation, and unverifiable condition is preserved. |

An implementation MAY optimize physical execution, but it MUST preserve these
semantic dependencies and separately report phase outcomes. A failed
prerequisite MUST NOT become a failure or success of a phase that could not
validly run.

## Conceptual outcome categories

Every applicable phase MUST receive one conceptual outcome category.

### Satisfied

Every evaluated applicable requirement for the phase was met.

### Not Satisfied

At least one evaluated applicable requirement for the phase failed.

### Unverifiable

A missing, ambiguous, conflicting, unavailable, policy-blocked, access-
blocked, unsupported, or insufficient required input, provenance item,
capability, or evidence prevents a reliable determination.

### Not Evaluated

The phase did not run because of a failed prerequisite, authorized stop,
governing policy boundary, unsupported execution, insufficient authority, or
established non-applicability. The reason MUST remain visible.

These names are conceptual categories. This decision assigns no serialized
token, enumeration, property, code, schema, media type, or API representation.

## Outcome aggregation and claims

There is no universal aggregate boolean `valid` across CNTX conformance
dimensions.

A positive conformance claim for one dimension requires:

1. every applicable prerequisite phase to be Satisfied;
2. every applicable requirement in the dimension to be Satisfied;
3. no applicable Not Satisfied result;
4. no material applicable Unverifiable condition;
5. no required Not Evaluated phase; and
6. every non-applicable phase to be justified by an Accepted governing source.

Not Satisfied, Unverifiable, and Not Evaluated MUST remain distinct and MUST
NOT suppress each other when several conditions occur.

A failed schema assertion does not convert a binding result into failure. A
binding or parsing failure does not establish schema nonconformance. Schema
success does not convert an unverified contract responsibility into success.

Warnings MUST NOT upgrade or downgrade an outcome, repair an assertion,
resolve missing evidence, replace a governing input, or authorize a positive
claim.

## Failure-layer preservation

At least these failure layers MUST remain separately attributable:

1. transport or external document-boundary failure;
2. byte, UTF-8, or BOM failure;
3. JSON syntax or duplicate-name failure;
4. Serialization Binding failure;
5. missing, ambiguous, conflicting, unavailable, unsupported, or unverifiable
   governing input;
6. Schema Resource resolution failure;
7. executable-schema assertion failure;
8. executable-schema processing or capability failure;
9. normative-contract nonconformance;
10. normative-contract unverifiability; and
11. output-assembly or evidence-preservation failure.

No failure layer may be guessed, silently retried under different governing
inputs, collapsed into an unrelated layer, replaced with a default, treated as
schema success or failure when schema evaluation did not validly run, treated
as contract success, or represented as authority, approval, trust, or
acceptance.

## Errors, warnings, limitations, and diagnostics

An assertion failure MUST remain distinct from parser failure, binding
failure, resolution failure, processor failure, unsupported capability,
missing evidence, unverifiability, and non-execution.

A warning is advisory only and MUST NOT change the applicable outcome or
authorize continuation.

Material limitations include supported and unsupported dialect/vocabulary
capabilities, resource bounds, unsupported input characteristics, unavailable
provenance, redacted or omitted diagnostics, assumptions, incomplete evidence,
disabled features, blocked disclosure, and non-machine-verifiable
responsibilities. A material limitation MUST NOT be silently omitted when it
affects interpretation, reproducibility, or the availability of a positive
claim.

This decision selects no portable error identifier, diagnostic code, severity
scale, warning code, message vocabulary, message text, localization,
diagnostic ordering, path serialization, output field, output schema, output
media type, API response, CLI exit code, or universal result object.

## Relationship to JSON Schema Draft 2020-12 output

For the executable-schema phase, applicable JSON Schema Draft 2020-12
distinctions among assertions, annotations, applicators, instance locations,
keyword relative locations, absolute keyword locations when available, nested
results, and errors or annotations MUST be preserved.

The standard Flag, Basic, Detailed, and Verbose output forms remain schema-
evaluation forms under their governing specification. This decision:

- does not redefine those forms;
- does not create a fifth JSON Schema output form;
- does not require one form as portable CNTX output;
- does not adopt the standard output-validation schema as a complete CNTX
  validation-output contract;
- does not convert annotations into assertion failures;
- does not activate Format-Assertion;
- preserves the Accepted Format-Annotation choice;
- does not treat `default` as permission to mutate an instance; and
- does not treat a bare Flag result as sufficient evidence for a
  consequential CNTX conformance claim.

A bare Flag result represents only the executable-schema phase's boolean
assertion result. It lacks the governing contract, binding, resource closure,
provenance, limitations, blocked conditions, and other phase outcomes required
for a broader CNTX claim.

## Fail-closed behavior

At minimum:

- malformed or unavailable bytes prevent parsing;
- invalid UTF-8, a prohibited BOM, duplicate names, or JSON syntax failure
  prevent a positive binding claim;
- parsing or binding failure leaves schema evaluation Not Evaluated rather
  than schema Not Satisfied;
- missing, wrong, ambiguous, conflicting, unavailable, substituted, or
  unresolved Schema Resources leave schema evaluation Not Evaluated or
  Unverifiable rather than schema Not Satisfied;
- unsupported dialect or required vocabulary is Unverifiable;
- a false schema assertion establishes only executable-schema Not Satisfied;
- successful schema evaluation establishes only executable-schema Satisfied;
- a contract responsibility that cannot be reliably evaluated from the frozen
  context cannot be claimed Satisfied;
- incomplete or unverifiable provenance blocks a claim that depends on it;
- warnings, defaults, coercion, fallback, recovery, mutation, or repair do not
  create success; and
- redaction does not silently convert an unverifiable result into success.

Permissive parser behavior, implementation-specific recovery, cache content,
network lookup, latest-version selection, or best-effort assumption MUST NOT
create a positive claim.

## Reproducibility and validation-output responsibilities

A future consequential validation output or conformance claim MUST be able to
identify, as applicable:

1. exact target subject;
2. represented Artifact Instance Identifier and Revision when available;
3. supplied-representation boundary and available provenance;
4. exact Binding Identity and Version;
5. exact Schema Identifier and Version;
6. exact entry Schema Resource;
7. complete transitive Schema Resource closure;
8. all canonical Schema Resource keys;
9. governing Accepted Schema Resource provenance;
10. exact Contract Definition Identifier and Version;
11. exact Accepted contract source binding;
12. declared Artifact Type;
13. frozen validation context;
14. evaluator implementation and version when known;
15. supported and unsupported capabilities;
16. material resource limits;
17. every phase outcome;
18. every material assertion failure;
19. every processing failure;
20. every warning;
21. every limitation;
22. every blocked or unresolved condition;
23. every Unverifiable condition;
24. every Not Evaluated phase and reason; and
25. any redaction or omission affecting interpretation.

These are logical responsibilities only. No concrete fields or serialization
are selected.

The same exact inputs, governing context, supported capabilities, and
conformant evaluation semantics MUST yield the same phase outcomes. Diagnostic
wording, ordering, localization, implementation-internal traces,
serialization, whitespace, object-member ordering, and output bytes need not
match.

No byte-identity claim exists because this decision selects no
canonicalization, digest, signature, timestamp, or byte-preservation
mechanism.

## Validation-output classification boundary

A logical validation output is not automatically a CNTX Artifact Instance,
Evidence Bundle, Review Record, Decision Record, State Snapshot, Conformance
Claim, approval record, certification, release record, or authority record.

This decision allocates no output identity, output version, Artifact Instance
Identifier, Artifact Revision, schema, binding, media type, canonical JSON,
filename, repository path, persistence mechanism, retention policy, archive,
transport, registry entry, or publication location.

Portable Conformance Evidence remains a separate later roadmap decision.

## Validator- and implementation-conformance boundary

A single validation run, output, test manifest, fixture result, or synthetic
case MUST NOT prove validator conformance.

Validator conformance requires separately governed evidence covering the
applicable standards and Accepted CNTX responsibilities across a sufficient
declared scope. This decision defines no evidence protocol, test suite,
certification, coverage threshold, badge, score, grade, supported-version
claim, or reference validator.

Validator conformance cannot prove broader implementation conformance.
Implementation conformance cannot be inferred from repository presence,
schema validity, one passing artifact, one validator, one implementation
claim, one release, one provider, one runtime, one deployment, or self-
attestation alone.

This decision creates no conformance tooling, validator implementation,
reference implementation, certification authority, accreditation,
compatibility matrix, supported-version registry, release gate, or
implementation-claim protocol.

## Security, privacy, and resource boundary

Artifact representations, schemas, resources, annotations, diagnostics, and
validation outputs remain untrusted input.

Implementations MUST be able to bound resource use, but this decision selects
no concrete byte, collection, string, numeric, schema-count, recursion,
reference-depth, instance-depth, time, memory, process, sandbox, filesystem,
network-policy, threat-response, or denial-of-service threshold.

Without separate governing permission, diagnostics and outputs MUST NOT expose
raw artifact values not needed for interpretation, secrets, credentials,
personal data, production configuration, private filesystem paths, private
project context, restricted source content, provider configuration, private
implementation details, internal network information, access tokens, or trust
material.

Locations, opaque references, bounded summaries, and explicit redaction or
omission notices SHOULD be preferred over copying sensitive values. Material
redaction or omission MUST be disclosed, MUST NOT silently change an outcome,
MUST NOT create a positive claim, and MUST NOT imply disclosure authority.

Validation grants no access, retrieval permission, network permission,
disclosure permission, truth, completeness, provenance, authenticity,
integrity, confidentiality, trust, approval, acceptance, decision, authority,
permission, execution authority, release authority, or deployment authority.

## Consequences

Positive consequences:

- exact governing context prevents silent version and resource substitution;
- phase separation prevents parser, binding, resolution, schema, and contract
  failures from being conflated;
- separate outcomes expose failure, unverifiability, and non-execution;
- conformance dimensions prevent schema success from becoming a universal
  claim;
- output responsibilities make consequential claims reproducible without
  prematurely selecting fields or serialization;
- standard JSON Schema output semantics remain usable within the schema phase;
  and
- security, privacy, and non-authority boundaries constrain diagnostics and
  disclosure.

Tradeoffs:

- callers must supply exact governing inputs and a complete frozen context;
- positive claims may remain unavailable when evidence or capabilities are
  insufficient;
- implementations cannot use a single convenience boolean for all CNTX
  conformance; and
- portable diagnostics, output formats, tooling, evidence, certification, and
  release claims remain separate work.

## Alternatives rejected

- One universal `valid` boolean: it collapses distinct conformance dimensions
  and blocked conditions.
- Schema success means contract conformance: schemas do not encode every
  normative responsibility.
- Parse or resolution failure means schema invalid: the schema phase did not
  validly run.
- Warnings repair or waive failure: warnings are advisory only.
- Default insertion or coercion: validation does not authorize target
  mutation.
- Bare JSON Schema Flag as complete CNTX output: it lacks governing context,
  phase outcomes, provenance, and limitations.
- A custom JSON Schema output form: standard schema semantics remain intact,
  while CNTX responsibilities are defined separately.
- Concrete output fields now: serialization and portable evidence remain
  separately governed.
- One successful artifact certifies a validator or implementation: evidence
  is insufficient and scope remains unproven.
- Automatic retrieval or latest-version fallback: governing resources remain
  exact, frozen, caller-supplied, and offline-first.

## Deferred and unauthorized scope

Deferred and unauthorized: changes to any Accepted architecture, ADR,
contract, schema, test, identity, version, Binding Version `1.0.0`, or resource
resolution boundary; Artifact Instance; identifier generation; revision
sequencing; Validation Run, Validation Output, or Validator Identity/Version;
concrete output fields, schema, media type, canonical JSON, portable error or
severity vocabulary, universal result object, validator implementation, API,
CLI, Portable Conformance Evidence, Conformance Claim artifact, test runner,
conformance suite, certification, score, badge, threshold, supported-version
claim, resolver, registry, catalog implementation, cache, bundler, mirror,
redirect, automatic retrieval, network access, digest, canonicalization,
signature, verification, encryption, timestamp service, trust store,
chain-of-custody, redaction/sanitization algorithm, retention/archive/disposal
mechanism, code generation, migration, template, form, checklist, rubric,
prompt, workflow, engine, scheduler, orchestrator, runtime, provider/product
work, private/reference implementation, release, tag, hosted publication, or
deployment.

## Acceptance and continuing gate

The candidate received one transparent non-independent COMMENT review on its
exact head and then stopped. Creation, validation, review, repository presence,
Draft state, and mergeability did not grant acceptance. EIGENAAR / Final
Authority separately accepted the exact reviewed candidate in issue comment
`5222756874`; governed integration adopts exactly this decision. Acceptance and
integration authorize no Portable Conformance Evidence, validator or
conformance tooling, implementation, release, publication, deployment, or
another roadmap layer.

## References

- [ARCH-003](artifact-contract-schema-architecture.md)
- [ARCH-007](common-artifact-envelope-schema-language-dialect.md)
- [ARCH-008](common-artifact-envelope-schema-composition-packaging.md)
- [ARCH-009](common-artifact-envelope-executable-schema.md)
- [ARCH-021](public-core-completion-boundary-roadmap.md)
- [ARCH-022](core-artifact-serialization-binding.md)
- [ARCH-023](schema-resource-resolution-catalog-boundary.md)
- [Contract index](../contracts/README.md)
- [Schema Resource index](../../schemas/README.md)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/)
- [JSON Schema Draft 2020-12 Core](https://json-schema.org/draft/2020-12/draft-bhutton-json-schema-01)
- [JSON Schema Draft 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation)
