# ADR-0016: Execution Result executable schema definition

- **Status:** Accepted
- **Date:** 2026-08-07
- **Issue:** [#58](https://github.com/CNTX-PROJECT/CNTX/issues/58)
- **Owner acceptance:** issue comment `5217275706`
- **Decision:** ARCH-016 — Execution Result Executable Schema Definition

## Context

ARCH-010 allocates the Execution Result logical Schema Identity, closed
full-artifact container, Common Artifact Envelope dependency, and inactive
initial version target. ARCH-011 allocates the exact CONTRACT-005 Definition
Identifier and Version. CONTRACT-005 defines the Evidentiary, bounded, and
non-self-approving Execution Result meaning.

After Accepted Context Packet Schema Version `1.0.0`, the dependency-first
rollout permits a separately governed Execution Result executable-schema
decision. The decision translates only CONTRACT-005 responsibilities, remains
structurally evaluative, preserves final human authority, and introduces no
artifact-specific schema dependency or implementation mechanism.

## Decision

Adopt one JSON Schema Draft 2020-12 Schema Resource at
`schemas/execution-result/1.0.0/schema.json` with canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/execution-result/1.0.0`.

The resource:

- evaluates a closed root with exactly `envelope` and `payload`;
- references the exact Accepted Common Artifact Envelope once;
- specializes only the Execution Result Artifact Type and governing Contract and
  Schema coordinates;
- represents the governing Task Contract through one opaque Artifact
  Instance/Revision pin;
- represents used Context Packets through a specified-or-none opaque pin
  declaration without a Context Packet schema reference;
- requires a closed fourteen-property CONTRACT-005 payload;
- uses closed provenance entries, statement declarations, artifact-pin
  declarations, check claims, and criteria-assessment claims;
- permits only bounded treatment, check-outcome, and criteria-assessment
  tokens;
- keeps all internal references fragment-local; and
- is Accepted; governed integration to `main` activates the exact resource.

## Rationale

The decision makes the complete Execution Result structurally evaluable while
preserving the boundary between evidence claims and consequential human
decisions. Opaque pins retain traceability without coupling executable
artifact schemas. Closed objects and explicit absence expose omissions and
reject silent extensions. Exact-version static composition supports offline,
deterministic validation.

## Consequences and tradeoffs

- Fourteen CONTRACT-005 responsibility groups become mandatory structural
  coordinates.
- Check outcomes and criteria assessments are explicit claims but cannot become
  approval or validator-output protocols.
- Provenance treatments describe representation without implementing it.
- Opaque references preserve technology neutrality but require human semantic
  review.
- The resource cannot prove correctness, completeness, authority, contract
  conformance, acceptance, integration, release, deployment, or merge
  permission.
- Offline validation requires explicit local registration of the common
  resource.

## Rejected alternatives

Rejected: open or flat roots; copied, moving, or dynamic common references;
embedded or schema-referenced Task Contracts, Context Packets, peers, or
downstream artifacts; unrestricted logs; executable action/resource/path
languages; automatic validation or criteria satisfaction; approval, workflow,
state, release, deployment, or merge fields; automatic evidence/review/decision
creation; network-dependent resolution; null or fabricated absence; canonical
JSON assumptions; and review or schema validity as acceptance.

## Validation

The accepted resource requires strict duplicate-free JSON and UTF-8 checks, official
Draft 2020-12 schema checking, isolated `jsonschema 4.25.1`, exact local
registration of the Common Artifact Envelope, required missing-resource
failure, all twenty expected fixture outcomes, exact root/constants/payload,
reference-graph assertions, protected-blob checks, link and privacy/security
scans, exact eight-path scope, committed-state checks, GitHub read-back, and
one transparent non-independent exact-head COMMENT review.

## Security and privacy

Fixtures are synthetic and public-safe. The schema records declarations only;
it grants no access or disclosure permission and implements no security,
privacy, redaction, encryption, or enforcement mechanism. Secrets,
credentials, personal data, private paths, production configuration,
restricted content, and private implementation details remain forbidden.

## Authority and conformance boundary

The resource is Evidentiary and non-self-approving. Schema validity proves only
structural satisfaction of this exact schema under the registered common
resource. It grants no task authority, correctness, completion, criteria
satisfaction, acceptance, integration, release, deployment, or merge
permission.

## Deferred scope and continuing gate

Deferred and unauthorized: Artifact Instances and revision mechanisms;
artifact-specific schema references; execution/mutation/access mechanisms;
validator/output contracts; criteria, approval, lifecycle, workflow, release,
deployment, or merge engines; Serialization Binding; canonical JSON; resolver,
registry, cache, bundler, network access, tooling, runtime, implementation,
product, release, tag, hosted publication, deployment; and Evidence Bundle or
later schemas.

Owner / Final Authority acceptance of the exact reviewed candidate is recorded
in issue comment `5217275706`. Governed integration to `main` activates exactly
Execution Result Schema Version `1.0.0`. No Evidence Bundle or later schema is
automatically authorized.
