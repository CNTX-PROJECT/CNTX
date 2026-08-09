# ADR-0032: CNTX Extension Module and Profile executable schema and validation/conformance boundary

- **Status:** Proposed
- **Date:** 2026-08-09
- **Issue:** [#106](https://github.com/CNTX-PROJECT/CNTX/issues/106)
- **Creation authority comment:** [5230742345](https://github.com/CNTX-PROJECT/CNTX/issues/106#issuecomment-5230742345)
- **Decision:** ARCH-032 — CNTX Extension Module and Profile Executable Schema
  and Validation/Conformance Boundary

## Context

Accepted ARCH-028 orders Extension Module/Profile decisions dependency-first.
ARCH-029 defines Definition identities and versions. ARCH-030 defines exact
dependencies, explicit activation, finite closure, composition, and fail-closed
conflicts. ARCH-031 defines Definition Schema Families, key-or-`None` schema
participation, future standalone resources, graph alignment, packages,
identity-preserving bundles, and a frozen logical Governing Declaration Set.

No Accepted decision yet defines how a future concrete Definition Schema
Resource participates in prerequisite-ordered validation; how schema-local
results relate to Definition, declaration, package, validator, implementation,
or broader conformance; what future cases must cover; or how output and
Portable Conformance Evidence preserve failures and limitations. Tooling and
implementation cannot safely precede that boundary.

## Decision

Define one conceptual Extension Module/Profile executable-schema and
validation/conformance boundary.

Require every consequential evaluation to use one closed, frozen, and
exactly-pinned context containing the complete Core inputs, active Definition
Set, authoritative Definition sources/revisions/provenance, dependencies,
Profile Subjects, one declaration per active key, exact Schema Resource
key-or-`None` bindings, resource sources/revisions, closed package, finite
acyclic resource graph, evaluator capabilities and limits, limitations,
adverse/unknown/unsupported conditions, restricted-evidence boundaries,
observation time, claimant, and attributable authority.

Prohibit ambient governing state, mutable aliases, automatic discovery or
network retrieval, hidden caches, installation/product inference, prior-success
fallback, and ordering-based meaning.

Keep the following dimensions separate: Core, Definition, Definition Schema
Resource, Governing Definition Declaration, Governing Declaration Set,
Definition Package, executable schema, schema-local result, Artifact Contract
and Artifact Instance, validator, implementation, interoperability,
compatibility/support, security/privacy, certification, release, and final
human authority. No dimension substitutes for another.

Order evaluation through explicit prerequisites:

1. supply and exact pins;
2. frozen-context completeness;
3. Definition source/revision/provenance consistency;
4. activation and Definition graph consistency;
5. declaration and Declaration Set conformance;
6. package completeness;
7. Schema Resource key-or-`None` binding;
8. resource identity, dialect, source, revision, and capability;
9. resource graph and reference direction;
10. standalone/bundled equivalence;
11. executable schema evaluation only for a later concrete Accepted governing
    resource;
12. Module/Profile composition without implicit precedence;
13. failure, blocked, unsupported, limitation, and non-execution recording;
14. output/evidence relation; and
15. exact-dimension conformance claims.

Preserve `Satisfied`, `Not Satisfied`, `Unverifiable`, and `Not Evaluated` for
broader CNTX validation dimensions. Keep JSON Schema validity and Flag, Basic,
Detailed, or Verbose output bounded to schema-local evaluation. They cannot
establish Definition, contract, Artifact Instance, validator, implementation,
interoperability, compatibility, support, security/privacy, certification,
release, approval, or authority.

Require future concrete Definition Schema work to include cases for positive
behavior, material negative assertions, wrong identities/versions/sources,
missing versus explicit `None`, dependency and Profile Subject errors,
prohibited reference directions, cycles, duplicates, multiple versions,
source conflicts, linked/bundled equivalence, unsupported capabilities,
unknown requirements, order dependence, composition conflicts, Core weakening,
resource limits, adverse/restricted evidence, blocked conditions, and Not
Evaluated behavior. ARCH-032 creates no concrete case.

Fail closed on missing, ambiguous, conflicting, unsupported, unverifiable,
resource-blocked, order-dependent, security/privacy-ambiguous, or
evidence-insufficient governing conditions. Do not resolve through order,
specificity guesses, newest/latest/latest-wins, popularity, implementation
preference, cache, prior success, majority, consensus, score, ranking,
coercion, defaulting, repair, substitution, or fallback.

Preserve ARCH-024 validation-output and ARCH-025 Portable Conformance Evidence
boundaries. Evidence supports review and decision but performs neither.

Treat all Definitions, resources, declarations, packages, bundles, targets,
outputs, and evidence as untrusted. Require later implementations to bound
resource consumption, malicious identities/provenance, reference expansion,
disclosure, minimization, least privilege, restricted evidence, and
unknown/unsupported mechanisms without selecting a concrete control here.

After separate acceptance and integration, permit only read-only reassessment
and preparation of a distinct Tooling and Implementation Boundary decision.
Select no implementation technology or repository and reserve no later ARCH
number or public object.

## Consequences

Positive consequences:

- future executable Definition Schema evaluation has an exact governing
  context and prerequisite order;
- schema-local validity cannot silently become broader conformance;
- declaration, package, resource, validator, and implementation claims remain
  independently reviewable;
- blocked, unsupported, Unverifiable, and Not Evaluated states remain visible;
- future synthetic cases have a complete minimum responsibility set;
- linked and identity-preserving bundled evaluation must remain equivalent;
- output and evidence remain traceable without becoming approval; and
- tooling cannot precede its governing specification or final human authority.

Costs and limitations:

- callers must supply complete exact inputs and provenance;
- no ambient discovery, mutable selection, repair, or fallback is available;
- no concrete Definition, schema, declaration, test, validator, or output
  protocol exists;
- no implementation executes this model;
- no interoperability, compatibility, support, security/privacy,
  certification, or release claim is proven; and
- additional separately governed decisions remain necessary before practical
  tooling can be selected or built.

## Alternatives not selected

### Treat schema validity as Definition conformance

Not selected because an executable schema is a bounded representation and
cannot replace authoritative Definition semantics, activation, provenance, or
authority.

### Infer governing resources from availability

Not selected because repository, package, registry, cache, network, or
installation presence does not establish exact governing intent or trust.

### Collapse all phases into one valid result

Not selected because prerequisite failure, blocked execution, unsupported
capability, uncertainty, and distinct conformance dimensions would be lost.

### Let dependency order establish precedence

Not selected because graph order identifies prerequisites only; Core
sovereignty and conjunctive Profile semantics forbid implicit override order.

### Build a validator now

Not selected because no concrete Definition Schema Resource, serialized
declaration, package representation, validation-output protocol, or practical
implementation boundary has been Accepted.

## Non-decisions

This ADR creates no concrete Extension Module/Profile, child Definition or
Schema Identifier/Version, namespace, `$id`, Schema Resource, schema file,
assertion, case, target representation, declaration field/token, package or
Artifact Instance, media type, Serialization Binding, portable output
vocabulary, custom dialect/vocabulary, dynamic reference, resolver, registry,
catalog, cache, bundler, mirror, redirect, network behavior, validator, runner,
suite, canonical JSON, digest, signature, verification, attestation,
certification, API, CLI, workflow, automation, runtime/provider/product work,
private/reference implementation, release, publication, distribution,
deployment, settings mutation, correction, withdrawal, reassessment, ARCH-033,
or follow-on authority.

## Authority boundary

This ADR is Proposed. Creation authority, repository presence, validation, and
transparent non-independent ARCHITECT review do not grant acceptance.

Separate attributable EIGENAAR / Final Authority exact-head acceptance,
status-only promotion, and governed integration are required before this
decision becomes Accepted or any tooling-boundary preparation may follow.
