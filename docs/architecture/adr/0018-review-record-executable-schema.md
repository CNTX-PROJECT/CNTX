# ADR-0018: Review Record executable schema definition

- **Status:** Proposed
- **Date:** 2026-08-07
- **Issue:** [#62](https://github.com/CNTX-PROJECT/CNTX/issues/62)
- **Decision:** ARCH-018 — Review Record Executable Schema Definition

## Context

ARCH-010 allocates the Review Record logical Schema Identity, closed
full-artifact container, exact Common Artifact Envelope dependency, and
inactive initial version target. ARCH-011 allocates the exact CONTRACT-007
Definition Identifier and Version. CONTRACT-007 defines the Evidentiary,
specialist-authored, bounded, and non-self-approving Review Record meaning.

After Accepted Evidence Bundle Schema Version `1.0.0`, the dependency-first
rollout permits a separately governed Review Record executable-schema
candidate. The decision translates only CONTRACT-007 responsibilities, remains
structurally evaluative, preserves authority separation and final human
authority, and introduces no artifact-specific schema dependency or
implementation mechanism.

## Proposed decision

Adopt, subject to separate exact-head EIGENAAR / Final Authority acceptance,
one JSON Schema Draft 2020-12 Schema Resource at
`schemas/review-record/1.0.0/schema.json` with canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/review-record/1.0.0`.

The Proposed resource:

- evaluates a closed root with exactly `envelope` and `payload`;
- references the exact Accepted Common Artifact Envelope once;
- specializes only the Review Record Artifact Type and governing Contract and
  Schema coordinates;
- separates opaque Review Authority and Execution Authority traceability;
- requires exact reviewable-subject declarations and nine explicit
  artifact-relationship categories;
- requires a closed sixteen-property CONTRACT-007 payload;
- keeps observation, interpretation, finding, rationale, evidence use,
  uncertainty, dissent, and recommendation structurally distinct;
- represents recommendations as non-authoritative specified-or-none input;
- uses only closed statement, artifact-pin, recommendation, finding, and
  traceability structures;
- keeps all internal references fragment-local; and
- remains Proposed and inactive until separate exact-head acceptance and
  governed integration.

## Rationale

The proposal makes a complete Review Record structurally evaluable while
preserving the boundary between specialist assessment and consequential human
decision. Separate authority pins prevent review authority from silently
replacing execution authority. Opaque subject, evidence, peer-review, decision,
and state references retain traceability without coupling executable artifact
schemas. Closed objects and explicit absence expose omissions and reject
silent extensions. Exact-version static composition supports deterministic
offline validation.

## Consequences and tradeoffs

- Sixteen CONTRACT-007 responsibility groups become mandatory structural
  coordinates if the candidate is later accepted.
- Specialist findings and recommendations remain Evidentiary and cannot become
  approval, rejection, acceptance, integration, release, deployment, or merge.
- Specialty, independence, coverage, depth, methods, uncertainty, dissent,
  evidence use, and historical correction remain declarations that require
  human semantic review.
- Opaque references preserve technology neutrality but do not prove existence,
  integrity, authority, relevance, or referential correctness.
- The resource cannot prove reviewer qualification, subject truth, evidence
  authenticity, finding correctness, review quality, completeness,
  independence, sufficiency, safety, decision validity, or final approval.
- Offline validation requires explicit local registration of the Accepted
  Common Artifact Envelope resource.

## Rejected alternatives

Rejected: open or flat roots; copied, moving, or dynamic common references;
embedded or schema-referenced governing, subject, result, evidence, peer-review,
decision, state, or downstream artifacts; merged review and execution
authority; implicit subjects or unreviewed scope; one untyped
observation/interpretation/finding/recommendation field; universal outcomes,
verdicts, pass/fail states, severity, confidence, scoring, grades, weights,
thresholds, rubrics, checklists, approval states, reviewer ranks, or specialty
taxonomies; automatic review, retrieval, finding generation, recommendation,
synthesis, corroboration, conflict resolution, voting, consensus, routing,
redaction, retention, decision, approval, lifecycle, workflow, or runtime
behavior; network-dependent resolution; null or fabricated absence; canonical
JSON assumptions; and review or schema validity as acceptance.

## Validation

The candidate requires strict duplicate-free JSON and UTF-8 checks, official
Draft 2020-12 schema checking, isolated `jsonschema 4.25.1`, exact local
registration of the Common Artifact Envelope, required missing-resource
failure, all twenty expected fixture outcomes, exact root/constants/sixteen-
property payload, authority-separation, subject, relationship, finding,
evidence, declaration, recommendation, closure, lexical, collection, and
reference-graph assertions, twenty-eight protected-blob checks, link and
privacy/security scans, exact eight-path scope, exact one-commit state,
GitHub read-back, and one transparent non-independent exact-head COMMENT
review.

## Security and privacy

Fixtures are synthetic and public-safe. The schema records declarations only;
it grants no review, evidence, collection, access, disclosure, retention, or
decision permission and implements no security, privacy, redaction, encryption,
verification, credential, independence, or enforcement mechanism. Secrets,
credentials, personal data, private paths, production configuration,
restricted content, and private implementation details remain forbidden.

## Authority and conformance boundary

The Proposed resource is Evidentiary and non-self-approving. Schema validity
proves only structural satisfaction of this exact candidate under the
registered common resource. It grants no review or execution authority,
specialist qualification, source truth, evidence authenticity, finding
correctness, review quality, recommendation authority, decision authority,
acceptance, integration, release, deployment, or merge permission.

## Deferred scope and continuing gate

Deferred and unauthorized: Artifact Instances and revision mechanisms;
reviewer identity allocation and specialty/accreditation systems;
artifact-specific schema references; retrieval, review, scoring, verification,
access, disclosure, retention, recommendation, synthesis, voting, decision,
approval, lifecycle, workflow, release, deployment, or merge mechanisms;
Serialization Binding; canonical JSON; validator/output contracts; resolver,
registry, catalog, cache, bundler, network access; conformance tooling,
runtime, implementation, provider, product, release, tag, hosted publication,
deployment; and Decision Record or later schemas.

Creation-contract approval is not candidate acceptance. After the transparent
non-independent exact-head COMMENT review, work stops for separate attributable
EIGENAAR / Final Authority acceptance of the exact candidate head.
