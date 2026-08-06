# ADR-0007: Common Artifact Envelope schema language and dialect

## Status

Accepted.

This ADR records the accepted, documentation-only architecture decision approved under issue #38. Owner / Final Authority acceptance of the exact reviewed candidate head is recorded in issue comment `5208113396`. On merge and publication to `main`, ADR-0007 becomes an accepted repository decision under repository governance.

## Context

Accepted ARCH-005 places schema-language and dialect selection after representation obligations and schema identity/version policy but before composition, packaging, and executable schema structure. Accepted ARCH-006 allocates one technology-neutral logical Common Artifact Envelope schema identity and reserves `1.0.0` only as the initial accepted executable version target.

CNTX needs one fixed, publicly specified schema-processing model so later composition and executable-definition decisions do not inherit an unspecified implementation default. The language decision must preserve the separation between dialect identity, schema-resource identity, Schema Version, Document Status, artifact Serialization Bindings, validation, and authority.

At the issue #38 baseline, the official [JSON Schema specification index](https://json-schema.org/specification) identifies 2020-12 as the current published version. [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core) defines the dialect, vocabulary, data-model, identity, and reference mechanisms; [JSON Schema Validation 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation) defines the standard validation and annotation vocabularies.

## Decision

CNTX adopts [the Common Artifact Envelope Schema Language and Dialect](../common-artifact-envelope-schema-language-dialect.md) as ARCH-007 with these constraints:

1. The future executable Common Artifact Envelope definition will use **JSON Schema**.
2. Its fixed dialect will be the **JSON Schema Draft 2020-12 Core and Validation dialect** identified by `https://json-schema.org/draft/2020-12/schema`.
3. Every future standalone schema document root must declare that exact dialect through `$schema`; implicit, moving-latest, implementation-default, or silent fallback behavior is prohibited.
4. The selected dialect uses exactly its seven published standard vocabularies: Core, Applicator, Unevaluated, Validation, Meta-Data, Format-Annotation, and Content.
5. The initial Common Artifact Envelope definition will use no custom CNTX dialect, custom vocabulary, unknown normative keyword, JSON Hyper-Schema dialect, or Format-Assertion vocabulary.
6. `format` remains annotation-only. Optional implementation behavior that treats it as an assertion cannot define portable CNTX conformance.
7. JSON Schema's JSON-compatible instance data model is selected for structural evaluation, but no physical artifact Serialization Binding or canonicalization is selected.
8. `$schema` identifies the dialect. `$id` is selected as the standard Core mechanism for a future schema-resource canonical URI, but this decision assigns no concrete `$id`, URI namespace, version placement, resolver, registry, or publication location.
9. The accepted ARCH-006 logical Schema Identifier and conditional `1.0.0` target remain unchanged. No executable schema or active Schema Version is created.
10. `$defs`, `$ref`, anchors, dynamic references, schema-resource boundaries, bundling, composition, packaging, publication, and distribution remain a separate next decision.
11. A future dialect upgrade or vocabulary-profile change requires a separately accepted decision and compatibility, version, processor, migration, and security/privacy assessment.
12. Dialect recognition, schema validity, artifact validity, contract conformance, approval, authority, integration, release, and deployment remain distinct.

## Consequences

- Later schema decisions receive one explicit and reproducible language-processing target.
- Tooling cannot silently choose a different JSON Schema draft or treat a future release as an automatic upgrade.
- Standard processors can recognize the language surface without CNTX-specific normative keywords.
- The official vocabulary set and annotation-only `format` behavior provide a precise interoperability baseline.
- Schema-language selection constrains structural evaluation to the JSON-compatible data model without preselecting artifact serialization.
- Future resource identity can use the standard `$id` mechanism while concrete identity/version URI design remains separately reviewable.
- Composition, packaging, publication, validation tooling, and executable content still require later authority and evidence.

## Rejected alternatives

### Use an unspecified or moving latest dialect

Rejected because schema meaning could change without a CNTX architecture decision or version assessment.

### Use Draft 2019-09 or an older dialect

Rejected because 2020-12 is the current published baseline at the task revision and an older dialect would create avoidable migration debt.

### Use draft-next behavior or feature proposals

Rejected because unpublished behavior is not a fixed interoperability target.

### Create a custom CNTX dialect or vocabulary

Rejected because no accepted requirement justifies the interoperability, processor-support, governance, and security burden.

### Select Format-Assertion

Rejected because portable format requirements have not been defined and the resulting custom vocabulary profile would create premature processor obligations.

### Select JSON Hyper-Schema

Rejected because hypermedia and interaction behavior is outside the bounded Common Artifact Envelope language decision.

### Treat the language as an artifact Serialization Binding

Rejected because structural evaluation and artifact serialization are different architecture layers.

### Decide composition and packaging now

Rejected because resource topology, references, bundling, URI layout, and distribution require a separate decision before executable schema work.

### Treat the combined Architect/Implementer review as final approval

Rejected because issue #38 permits transparent operational role combination but preserves sole human final authority and the exact-head decision gate.

## Follow-up decisions

The next candidate decision should define Common Artifact Envelope composition and packaging while preserving ARCH-007 if accepted. Only after that separate decision may a bounded executable Common Artifact Envelope schema be considered.

No follow-up task, executable schema, concrete `$id`, reference graph, resource layout, package, publication, artifact Serialization Binding, validator, Layer 5 mechanism, implementation, merge, release, or deployment is authorized by this ADR.
