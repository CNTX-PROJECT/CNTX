# ADR-0012: Project Charter executable schema definition

## Status

**Proposed.**

This ADR records the Proposed decision governed by
[issue #48](https://github.com/CNTX-PROJECT/CNTX/issues/48). Creation authority
is recorded in issue comment `5210055148`. The candidate requires disclosed
exact-head review and separate human Owner / Final Authority acceptance before
it can become Accepted.

## Context

ARCH-010 allocates the Project Charter artifact-specific logical Schema
Identity and inactive `1.0.0` target, fixes a closed root with required
`envelope` and `payload`, and permits only the exact Accepted Common Artifact
Envelope root as an initial external dependency. ARCH-011 provides the exact
Project Charter Contract Definition Identifier and Version. CONTRACT-001
defines the payload responsibilities but intentionally did not select fields
or syntax.

The next dependency-first step is one independently governed executable
Project Charter definition. It must make CONTRACT-001 responsibilities
structurally reviewable without inventing approval, implementation, binding,
or downstream-artifact authority.

## Decision

CNTX proposes one standalone JSON Schema Draft 2020-12 Schema Resource:

- logical identity: **CNTX Public Core Schema Family / Project Charter
  Artifact**;
- `$id`:
  `https://github.com/CNTX-PROJECT/CNTX/schemas/project-charter/1.0.0`;
- Schema Version: `1.0.0`;
- repository path: `schemas/project-charter/1.0.0/schema.json`.

The root is a closed object with exactly required `envelope` and `payload`.
`envelope` statically references the complete Accepted Common Artifact
Envelope Schema Version `1.0.0` and overlays only exact Project Charter
constants for Artifact Type, governing Contract, and governing Schema.

The closed payload requires exactly:

- purpose;
- desired outcomes and success direction;
- included scope, boundaries, and non-goals;
- governing principles;
- material constraints;
- governance context and final-authority role;
- assumptions, dependencies, risks, and unresolved uncertainty;
- public and restricted-information boundaries;
- downstream expectations; and
- review, amendment, supersession, and retirement conditions.

Absence-sensitive categories use one closed declaration set: either
`specified` with one or more unique non-blank items, or `none` without items.
That local disposition is not lifecycle, approval, authority, or runtime state.

Exactly one external `$ref` is permitted. All other reuse remains under root
`$defs` with fragment-local references. No nested resource, public anchor,
dynamic reference, artifact-to-artifact dependency, custom vocabulary,
Format-Assertion, default, or unknown normative keyword is selected.

## Rationale

The decision follows the accepted dependency direction and preserves three
independent review units: the common envelope, the Project Charter contract,
and the Project Charter executable schema. Exact constants prevent an instance
validated under this resource from silently claiming another Artifact Type,
Contract Definition, or Schema Definition.

Closed structures expose every public-core semantic addition to versioned
review. The declaration-set model makes assessed absence explicit without
requiring fabricated placeholder content. Broad non-blank strings preserve
domain independence and defer unsupported lexical policies.

## Consequences

If later accepted and integrated, the exact resource can make a complete
Project Charter structurally schema-valid. It will not make that charter
contract-conformant, approved, authoritative, truthful, safe to disclose, or
actionable merely by validation.

The schema's exact payload surface becomes immutable for Schema Version
`1.0.0`. Later semantic changes require compatibility and version assessment.
The resource depends on preloading the exact common schema and permits no
automatic network retrieval.

No Workstream or other artifact-specific Schema Version is activated or
authorized by this decision.

## Rejected alternatives

- flatten envelope and payload;
- make either root member optional;
- allow unknown root, payload, or nested fields;
- copy or weaken the common schema;
- reference a common internal `$defs` member;
- use a mutable, relative, unversioned, `latest`, or dynamic common reference;
- identify the complete artifact with the common schema `$id`;
- create one monolithic or lockstep-versioned artifact schema family;
- use an arbitrary free-form payload;
- encode absence through blank values, empty arrays, null, or `N/A`;
- add approval, authority, lifecycle-status, execution, or runtime fields;
- require personal data for final authority;
- embed or executable-schema-reference downstream artifacts;
- treat the instance model as canonical JSON or another Serialization Binding;
- treat tests, schema validity, or operational review as acceptance; and
- automatically continue to the Workstream schema.

## Validation

Validation must strictly parse JSON with duplicate-key rejection, verify Draft
2020-12 meta-schema validity, preload the exact Accepted Common Artifact
Envelope under its canonical `$id` without network access, execute every
synthetic case, compare expected and actual validity, verify the complete
reference graph and closed property model, check UTF-8 and local links, prove
the exact eight-path scope and protected baseline blobs, and record the exact
temporary validator tool and version. No validator dependency or
implementation is committed.

## Security and privacy

The schema and tests contain only public-safe synthetic material. They must not
contain secrets, credentials, personal data, production configuration, private
paths, restricted source content, private project data, provider-specific
requirements, product logic, or private implementation detail.

HTTPS identifiers grant no automatic retrieval or trust. Schema validity
grants no authority, approval, access, disclosure, release, or deployment.

## Authority and conformance boundary

The same operational agent may prepare and review the candidate only under the
transparent non-independent arrangement recorded in issue #48. Review is
evidence, not final approval. Schema validity cannot prove CONTRACT-001
conformance, truth, completeness, applicable authority, valid approval, or
permission for consequential use.

## Deferred scope

Deferred are Project Charter instances, identifier generation, revision
sequencing, approval evidence, digests, signatures, verification, artifact
Serialization Bindings, canonical artifact JSON, downstream schemas,
artifact-to-artifact references, extensions, profiles, validators, validation
outputs, resolvers, registries, catalogs, caches, bundles, conformance tooling,
code generation, migration, APIs, CLIs, workflows, runtimes, providers,
products, private/reference implementations, releases, hosted publication, and
deployment.

## Continuing gate

The Proposed candidate must stop after one validated commit, one Draft PR, and
one disclosed non-independent exact-head COMMENT review. Separate attributable
Owner / Final Authority acceptance of the exact reviewed head is required
before status promotion or integration. No later artifact-specific schema is
automatically authorized.
