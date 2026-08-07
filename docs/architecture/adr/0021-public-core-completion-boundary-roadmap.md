# ADR-0021: Public Core completion boundary and remaining layer roadmap

- **Status:** Proposed
- **Date:** 2026-08-07
- **Issue:** [#68](https://github.com/CNTX-PROJECT/CNTX/issues/68)
- **Decision:** ARCH-021 — CNTX Public Core Completion Boundary and Remaining Layer Roadmap

## Context

Accepted ARCH-001 through ARCH-020 establish CNTX Public Core governance,
authority, privacy, identity, versioning, provenance, artifact semantics,
contract definitions, schema layering, the Common Artifact Envelope, and nine
artifact-specific executable schemas. The repository now contains ten active
Schema Versions `1.0.0`: one common-envelope resource and one for each of the
nine canonical artifacts.

That boundary is substantial but incomplete. The executable schemas constrain
the JSON data model, while no Accepted decision yet defines a portable artifact
Serialization Binding, deterministic schema-resource supply boundary,
validation/output contract, portable conformance evidence boundary, or
release-readiness decision. Runtime and product implementation are later,
separate layers and need not define completion of the public specification.

Without an explicit boundary, the completed schema foundation could be
mistaken for full interoperability or release-readiness, or its completion
could be understated because no runtime exists.

## Decision

Record the current state as the **completed CNTX Public Core
contract-and-schema foundation**, comprising:

- Accepted ARCH-001 through ARCH-020 and ADR-0001 through ADR-0020;
- Accepted CONTRACT-001 through CONTRACT-009;
- one active Common Artifact Envelope Schema Version `1.0.0`;
- nine active Contract Definition Identifier/Version/source-binding sets;
- nine active artifact-specific Schema Versions `1.0.0`;
- ten executable schema resources; and
- ten corresponding synthetic test manifests.

Do not equate that boundary with portable artifact interoperability,
implementation, runtime, product, release, publication, deployment, or
production readiness.

Order the remaining public-core decision layers as follows:

1. Artifact Serialization Binding architecture;
2. schema-resource resolution and catalog boundary;
3. validation and validation-output contract;
4. portable conformance evidence boundary; and
5. public-core release-readiness and publication boundary.

Every layer retains a separate governance lifecycle. This decision grants no
authority to create or implement any layer.

Extension Module and Profile mechanisms remain optional and non-blocking while
the base public core introduces no extension/profile negotiation, discovery,
compatibility, inheritance, resolution, or conformance claim.

Workflow, orchestration, scheduling, state-transition engines, runtime
services, provider adapters, product logic, user interfaces, private or
reference implementations, deployment infrastructure, hosted services, and
domain-specific extensions remain outside the required public-core
specification-completion boundary unless separately introduced.

## Dependency ordering

- A Serialization Binding decision precedes portable Artifact Instance
  validation because executable schemas do not define a complete byte,
  character, document, file, or stream representation.
- A schema-resource supply and failure boundary precedes deterministic
  multi-resource validator claims.
- A validation and validation-output contract precedes normative validator or
  conformance tooling.
- Portable conformance evidence precedes release-readiness claims about
  interoperability or implementation conformance.

The recommended next decision category after separate acceptance and
integration of ARCH-021 is CNTX Core Artifact Serialization Binding
Architecture. No ARCH number, issue, branch, path, representation choice, or
creation authority is allocated to it here.

## Rationale

The boundary recognizes completed work without turning structural schema
validity into contract conformance, interoperability, authority, approval, or
release-readiness. Dependency ordering prevents implementation choices from
silently defining missing public contracts and allows the public core to remain
model-, vendor-, runtime-, provider-, product-, storage-, transport-, and
domain-agnostic.

Keeping runtime and product layers outside the required public-core completion
definition permits a specification release without forcing one privileged
implementation. Requiring applicable binding and conformance decisions before
implementation conformance claims still protects portability and verifiability.

## Consequences and tradeoffs

- The contract-and-schema foundation may be described as complete, but CNTX
  remains unreleased and pre-alpha.
- Existing executable schemas and synthetic cases remain Accepted and active,
  but they do not become a portable artifact binding or complete conformance
  suite.
- Future validator work cannot treat current candidate-validation procedures
  as a normative portable output contract.
- A release-readiness decision is deferred until its applicable prerequisites
  are Accepted and integrated.
- Optional Extension Module/Profile architecture may be deferred while no
  extension/profile claims are introduced.
- Runtime and product implementations may remain outside the public repository,
  but cannot claim CNTX conformance without satisfying applicable future
  public contracts.

## Rejected alternatives

Rejected: declaring CNTX fully complete or release-ready at the executable-
schema boundary; requiring a runtime or product before the public specification
can ever be complete; treating JSON Schema resource serialization as the
artifact Serialization Binding; treating existing candidate-validation scripts
or libraries as a portable validator contract; assuming network resolution,
latest resources, or a registry; making optional Extension Module/Profile work
an unconditional blocker; assigning the next ARCH number or preselecting a
format, media type, encoding, canonicalization, resolver, validator, API, CLI,
tool, implementation, release, or deployment.

## Security and privacy

Future representation, resource supply, validation output, conformance
evidence, publication, and implementation work remains subject to the Accepted
public/private boundary. No completion claim grants access, disclosure,
authenticity, trust, authority, approval, or permission. Secrets, credentials,
personal data, production configuration, private paths, restricted content,
private project context, provider assumptions, and private implementation
details remain forbidden in public artifacts.

## Authority and conformance boundary

This decision is Proposed. Creation, validation, repository presence, and a
transparent non-independent review grant no acceptance. Only separately
attributable EIGENAAR / Final Authority acceptance of the exact reviewed
revision can authorize status promotion.

Schema validity does not establish contract conformance, portable artifact
representation, truth, approval, interoperability, implementation conformance,
release-readiness, release, publication, deployment, merge permission, or
follow-on authority.

## Deferred scope

Deferred and unauthorized: concrete serialization; JSON artifact binding;
canonical JSON; media type; charset; encoding; ordering; whitespace; Unicode;
number and duplicate-name rules; canonicalization; digest; signature;
verification; trust; Artifact Instances; identifier generation; revision
sequencing; Extension Module/Profile mechanisms; resolver; registry; catalog
implementation; cache; bundler; mirror; network; validator; validation-output
fields; conformance tooling; code generation; migration; templates; forms;
checklists; rubrics; prompts; API; CLI; workflow; engine; scheduler;
orchestrator; runtime; provider or product work; private or reference
implementation; supported-version claim; release; tag; hosted publication; and
deployment.

## Supersession and continuing authority

If Accepted, this decision may be changed or superseded only through a new
governed decision that identifies the affected completion categories,
dependencies, sources, compatibility consequences, and authority. Acceptance
would authorize no next roadmap candidate, implementation, release,
publication, deployment, or other follow-on action automatically.
