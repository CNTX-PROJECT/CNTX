# ADR-0019: Decision Record executable schema definition

- **Status:** Proposed
- **Date:** 2026-08-07
- **Issue:** [#64](https://github.com/CNTX-PROJECT/CNTX/issues/64)
- **Decision:** ARCH-019 — Decision Record Executable Schema Definition

## Context

ARCH-010 allocates the Decision Record logical Schema Identity, closed
full-artifact container, exact Common Artifact Envelope dependency, and inactive
initial version target. ARCH-011 allocates the exact CONTRACT-008 Definition
Identifier and Version. CONTRACT-008 defines an attributable, bounded,
consequential Decision Record under final human authority.

After Accepted Review Record Schema Version `1.0.0`, the dependency-first
rollout permits a separately governed Decision Record executable-schema
proposal. The proposal must translate only CONTRACT-008 responsibilities,
preserve authority and approval provenance without claiming to verify them,
preserve source and historical traceability through opaque pins, and introduce
no artifact-specific schema dependency or implementation mechanism.

## Decision

Propose one JSON Schema Draft 2020-12 Schema Resource at
`schemas/decision-record/1.0.0/schema.json` with canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/decision-record/1.0.0`.

The resource:

- evaluates a closed root with exactly `envelope` and `payload`;
- references the exact Accepted Common Artifact Envelope once;
- specializes only the Decision Record Artifact Type and governing Contract and
  Schema coordinates;
- records one exact Decision Authority pin and an opaque human decision-maker
  reference while separating decision, preparation, review, publication,
  administration, and execution authority;
- records the exact Decision Record revision represented as approved plus
  attributable approval and governing-authority provenance, without proving
  pin equality or approval validity;
- requires one coherent decision boundary, question, opaque disposition,
  outcome statement, and excluded or separately approvable decisions;
- requires a closed seventeen-property CONTRACT-008 payload;
- requires nine exact specified-or-none artifact-relationship categories;
- keeps evidence, review, recommendations, uncertainty, dissent, and unresolved
  questions separate and explicitly non-approving;
- separates seven opaque temporal coordinates and seven separately authorized
  consequential-action categories;
- separates amendment, correction, revocation, supersession, dependency,
  conflict, unresolved conflict, and authorized-resolution provenance;
- preserves role, external-record, security/privacy, restricted-basis,
  historical, and follow-on-authority boundaries;
- uses only closed statement, opaque-value, artifact-pin, downstream-boundary,
  peer-decision, external-record, and responsibility structures;
- keeps all internal references fragment-local; and
- remains Proposed and inactive unless separately accepted and integrated.

## Rationale

The proposal makes a complete Decision Record structurally evaluable while
preserving the boundary between evidentiary input, preparation, review, and an
attributable consequential decision. Exact opaque authority and approval pins
retain provenance without turning the schema into an identity, credential,
signature, verification, or authorization system.

Closed objects and explicit absence expose omissions and reject silent
extensions. Separate downstream-action categories prevent a recorded decision
from silently performing acceptance, integration, release, deployment,
publication, merge, or execution. Exact-version static composition supports
deterministic offline validation.

## Consequences and tradeoffs

- Seventeen CONTRACT-008 responsibility groups are mandatory structural
  coordinates in the candidate.
- The Decision Authority pin, human decision-maker reference, approved-revision
  pin, approval references, and authority traceability remain declarative and
  require external human-governed verification.
- Outcome dispositions remain opaque; interoperability cannot depend on a
  universal verdict, status, severity, confidence, score, or priority taxonomy.
- Evidence, reviews, recommendations, uncertainty, and dissent remain inputs
  that neither individually nor collectively approve the decision.
- Governing sources and related artifacts remain opaque exact references;
  existence, integrity, applicability, authenticity, access, and correctness
  are not proved.
- Amendment, correction, revocation, supersession, dependencies, conflicts, and
  resolutions remain explicit and historical, without automatic precedence or
  lifecycle mutation.
- Offline validation requires explicit local registration of the Accepted
  Common Artifact Envelope resource.

## Rejected alternatives

Rejected: open or flat roots; copied, moving, dynamic, or network-resolved
common references; embedded or artifact-schema-referenced governing, evidence,
review, peer, state, or downstream artifacts; implicit authority, self-approval,
or signature-as-approval; merged authority roles; bundled decisions; universal
outcome, status, verdict, pass/fail, severity, confidence, score, grade,
priority, weight, threshold, voting, majority, consensus, ranking, latest-wins,
or implementation taxonomies; automatic retrieval, reasoning, recommendation,
decision, approval, conflict resolution, state transition, integration,
publication, release, deployment, merge, execution, workflow, or runtime
behavior; null or fabricated absence; canonical JSON assumptions; and schema
validity as acceptance.

## Validation

The resource requires strict duplicate-free JSON and UTF-8 checks, official
Draft 2020-12 schema checking, isolated `jsonschema 4.25.1`, exact local
registration of the Common Artifact Envelope, required missing-resource
failure, all twenty expected fixture outcomes, exact root/constants/seventeen-
property payload, authority-separation, approved-revision, relationship, timing,
downstream, change, external-record, declaration, closure, lexical, collection,
and reference-graph assertions, thirty-two protected-blob checks, link and
privacy/security scans, exact eight-path scope, exact one-commit state, GitHub
read-back, and one transparent non-independent exact-head COMMENT review.

## Security and privacy

Fixtures are synthetic and public-safe. The schema records declarations only;
it allocates no identity or authority, grants no permission, verifies no
approval, retrieves no source, and implements no access, disclosure, redaction,
sanitization, encryption, retention, archival, disposal, signature,
verification, timestamp, trust, or chain-of-custody mechanism. Secrets,
credentials, personal data, private paths, production configuration, restricted
content, provider-specific assumptions, and private implementation details
remain forbidden.

## Authority and conformance boundary

The Proposed resource is non-self-approving. Schema validity proves only
structural satisfaction of this exact candidate under the registered common
resource. It grants no contract conformance, source truth, identity, authority,
approval, decision correctness, legal effect, acceptance, integration, release,
deployment, publication, merge permission, execution, or follow-on authority.

Creation, validation, review, repository presence, or a Draft pull request does
not accept or activate Schema Version `1.0.0`. A separate attributable EIGENAAR
/ Final Authority acceptance and separately governed integration are mandatory.

## Deferred scope and continuing gate

Deferred and unauthorized: Artifact Instances and revision mechanisms;
authority, decision-maker, identity, credential, delegation, approval,
signature, verification, trust, timestamp, digest, encoding, canonicalization,
encryption, retrieval, resolver, registry, catalog, cache, bundler, network,
reasoning, recommendation, scoring, voting, consensus, conflict-resolution,
state, lifecycle, workflow, consequential-action, access, disclosure, redaction,
sanitization, retention, archival, disposal, and chain-of-custody mechanisms;
State Snapshot or later schemas; Serialization Binding; canonical artifact JSON;
Extension Module/Profile mechanisms; validator/output implementations;
conformance tooling; runtime, private or reference implementation, provider,
product, release, tag, hosted publication, and deployment.

The authorized candidate workflow stops after one transparent non-independent
exact-head COMMENT review. No status promotion, Ready-for-review transition,
merge, issue closure, activation, or branch cleanup is authorized by this ADR.
