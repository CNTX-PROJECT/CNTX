# ADR-0017: Evidence Bundle executable schema definition

- **Status:** Accepted
- **Date:** 2026-08-07
- **Issue:** [#60](https://github.com/CNTX-PROJECT/CNTX/issues/60)
- **Owner acceptance:** issue comment `5217888146`
- **Decision:** ARCH-017 — Evidence Bundle Executable Schema Definition

## Context

ARCH-010 allocates the Evidence Bundle logical Schema Identity, closed
full-artifact container, Common Artifact Envelope dependency, and inactive
initial version target. ARCH-011 allocates the exact CONTRACT-006 Definition
Identifier and Version. CONTRACT-006 defines the Evidentiary, bounded, and
non-self-approving Evidence Bundle meaning.

After Accepted Execution Result Schema Version `1.0.0`, the dependency-first
rollout permits a separately governed Evidence Bundle executable-schema
decision. The decision translates only CONTRACT-006 responsibilities,
remains structurally evaluative, preserves final human authority, and
introduces no artifact-specific schema dependency or implementation mechanism.

## Decision

Adopt one JSON Schema Draft 2020-12 Schema Resource at
`schemas/evidence-bundle/1.0.0/schema.json` with canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/evidence-bundle/1.0.0`.

The resource:

- evaluates a closed root with exactly `envelope` and `payload`;
- references the exact Accepted Common Artifact Envelope once;
- specializes only the Evidence Bundle Artifact Type and governing Contract
  and Schema coordinates;
- represents the governing Task Contract through one opaque Artifact
  Instance/Revision pin;
- represents eight artifact-relationship categories through specified-or-none
  opaque pin declarations without artifact-specific schema references;
- requires a closed fifteen-property CONTRACT-006 payload;
- uses closed reviewable-subject, Evidence Item, claim-traceability, statement,
  and artifact-pin structures;
- permits only bounded representation-treatment tokens;
- keeps all internal references fragment-local; and
- is Accepted; governed integration to `main` activates the exact resource.

## Rationale

The decision makes a complete Evidence Bundle structurally evaluable while
preserving the boundary between evidence claims and consequential human
decisions. Opaque pins and references retain traceability without coupling
executable artifact schemas. Closed objects and explicit absence expose
omissions and reject silent extensions. Exact-version static composition
supports offline deterministic validation.

## Consequences and tradeoffs

- Fifteen CONTRACT-006 responsibility groups become mandatory structural
  coordinates in the Accepted schema.
- Evidence treatments remain representation claims and cannot become
  algorithms, quality grades, weights, permissions, or approval protocols.
- Opaque references preserve technology neutrality but require human semantic
  review.
- The resource cannot prove source existence, authenticity, provenance,
  relevance, independence, completeness, coverage, reproducibility,
  sufficiency, correctness, authority, acceptance, integration, release,
  deployment, or merge permission.
- Offline validation requires explicit local registration of the common
  resource.

## Rejected alternatives

Rejected: open or flat roots; copied, moving, or dynamic common references;
embedded or schema-referenced governing, subject, context, result, peer,
review, decision, state, or downstream artifacts; unrestricted evidence
collection; universal scoring, confidence, grading, weighting, or thresholds;
automatic retrieval, selection, ranking, deduplication, corroboration,
conflict resolution, verification, redaction, retention, decision, approval,
lifecycle, workflow, or runtime behavior; network-dependent resolution; null
or fabricated absence; canonical JSON assumptions; and review or schema
validity as acceptance.

## Validation

The resource requires strict duplicate-free JSON and UTF-8 checks,
official Draft 2020-12 schema checking, isolated `jsonschema 4.25.1`, exact
local registration of the Common Artifact Envelope, required missing-resource
failure, all twenty expected fixture outcomes, exact
root/constants/fifteen-property payload, reference-graph assertions,
twenty-four protected-blob checks, link and privacy/security scans, exact
eight-path scope, committed-state checks, GitHub read-back, and one transparent
non-independent exact-head COMMENT review.

## Security and privacy

Fixtures are synthetic and public-safe. The schema records declarations only;
it grants no collection, access, disclosure, retention, or approval permission
and implements no security, privacy, redaction, encryption, verification, or
enforcement mechanism. Secrets, credentials, personal data, private paths,
production configuration, restricted content, and private implementation
details remain forbidden.

## Authority and conformance boundary

The resource is Evidentiary and non-self-approving. Schema validity proves only
structural satisfaction of this exact schema under the registered
common resource. It grants no task authority, source truth, provenance,
authenticity, relevance, independence, completeness, coverage,
reproducibility, sufficiency, correctness, acceptance, integration, release,
deployment, or merge permission.

## Deferred scope and continuing gate

Deferred and unauthorized: Artifact Instances and revision mechanisms;
artifact-specific schema references; collection, retrieval, scoring,
verification, access, disclosure, retention, or conflict-resolution
mechanisms; validator/output contracts; approval, lifecycle, workflow,
release, deployment, or merge engines; Serialization Binding; canonical JSON;
resolver, registry, catalog, cache, bundler, network access, tooling, runtime,
implementation, product, release, tag, hosted publication, deployment; and
Review Record or later schemas.

Owner / Final Authority acceptance of the exact reviewed candidate is recorded
in issue comment `5217888146`. Governed integration to `main` activates exactly
Evidence Bundle Schema Version `1.0.0`. No Review Record or later schema is
automatically authorized.
