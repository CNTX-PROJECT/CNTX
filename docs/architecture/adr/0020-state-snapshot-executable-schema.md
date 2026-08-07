# ADR-0020: State Snapshot executable schema definition

- **Status:** Proposed
- **Date:** 2026-08-07
- **Issue:** [#66](https://github.com/CNTX-PROJECT/CNTX/issues/66)
- **Exact-head acceptance:** pending separate attributable EIGENAAR / Final Authority action
- **Decision:** ARCH-020 — State Snapshot Executable Schema Definition

## Context

ARCH-010 allocates the State Snapshot logical Schema Identity, closed complete-
artifact container, exact Common Artifact Envelope dependency, and inactive
initial version target. ARCH-011 allocates the exact CONTRACT-009 Definition
Identifier and Version. CONTRACT-009 defines a Derived, non-authoritative,
non-evidentiary orientation artifact whose controlling sources, exact revisions
or pinning limitations, temporal boundaries, uncertainty, historical
provenance, and final human authority remain visible.

After Accepted Decision Record Schema Version `1.0.0`, the dependency-first
rollout permits a separately governed State Snapshot executable-schema
candidate. The candidate must translate only CONTRACT-009 responsibilities,
must keep authoritative sources controlling, and must introduce no retrieval,
freshness calculation, state, synchronization, workflow, access, or runtime
mechanism.

## Proposed decision

Propose one JSON Schema Draft 2020-12 Schema Resource at
`schemas/state-snapshot/1.0.0/schema.json` with canonical `$id`
`https://github.com/CNTX-PROJECT/CNTX/schemas/state-snapshot/1.0.0`.

The resource:

- evaluates a closed root with exactly `envelope` and `payload`;
- references the exact Accepted Common Artifact Envelope once;
- specializes only the State Snapshot Artifact Type and governing Contract and
  Schema coordinates;
- requires exact `Derived`, non-authoritative, and non-evidentiary boundaries;
- requires bounded orientation purpose, scope, audiences, and exclusions;
- preserves controlling sources, precedence, conflict visibility, and final
  human authority;
- requires every source to have an exact revision or an explicit exclusive
  pinning limitation;
- separates six opaque temporal coordinates and four contract-specific
  freshness classifications;
- preserves relevance, minimization, uncertainty, limitations, conflicts,
  omissions, incomplete work, stopped conditions, unresolved decisions, and
  verification gaps;
- separates reported state from completion, correctness, conformance,
  currentness, verification, evidence, review, decision, and integration;
- requires a closed eighteen-property CONTRACT-009 payload;
- requires nine specified-or-none artifact-relationship categories;
- requires exact represented-snapshot identity/revision and historical
  provenance without generating or comparing identity;
- separates dependency, replacement, correction, supersession, and conflict
  relations to exact peer State Snapshot revisions;
- preserves bounded handoff, security/privacy, restricted-context,
  non-automatic lifecycle, and follow-on-authority boundaries;
- keeps every internal schema reference fragment-local; and
- remains Proposed and inactive pending separate exact-head acceptance and a
  separately authorized status promotion and integration.

## Rationale

The candidate makes a complete State Snapshot structurally evaluable while
preserving the distinction between compact orientation and controlling source
state. Exact revision pins and explicit pinning limitations make provenance and
uncertainty visible without converting the schema into a resolver, registry,
retrieval system, digest verifier, or authority source.

Closed objects and explicit specified-or-none declarations expose omissions
and reject silent extensions. Separate temporal, freshness, claim, evidence,
review, decision, integration, uncertainty, stopped-work, peer-relation, and
handoff categories prevent compactness from erasing material boundaries.
Exact-version static composition supports deterministic offline validation.

## Consequences and tradeoffs

- Eighteen CONTRACT-009 responsibility groups are mandatory structural
  coordinates in the Proposed schema.
- Source identity, exact revisions, applicability, provenance, and limitations
  remain declarative and require external human-governed verification.
- An unpinned source is representable only through an explicit limitation and
  uncertainty effect; schema validity cannot decide whether it is acceptable.
- Six temporal coordinates remain opaque and separate; interoperability cannot
  assume a timestamp grammar or chronology.
- Four freshness tokens remain local to this contract and do not form a
  universal state or lifecycle taxonomy.
- Reported state and claims remain orientation, not proof. Evidence, review,
  decision, and integration references retain their independent meanings.
- Peer replacement, correction, supersession, and conflict remain explicit and
  historical, without latest-wins or automatic mutation.
- Offline validation requires explicit local registration of the Accepted
  Common Artifact Envelope resource.

## Rejected alternatives

Rejected: open or flat roots; copied, moving, dynamic, or network-resolved
common references; embedded or artifact-schema-referenced sources, governing
artifacts, evidence, reviews, decisions, peers, or downstream artifacts;
implicit authority; authoritative or evidentiary snapshots; self-approval;
unidentified mutable sources; silent missing revisions; collapsed timestamps;
universal freshness, status, outcome, pass/fail, severity, confidence, score,
grade, priority, weight, threshold, or lifecycle vocabularies; silent
uncertainty, omission, conflict, incomplete work, or stopped conditions;
implicit recency, latest-wins, replacement, merge, or conflict resolution;
automatic selection, retrieval, search, ranking, RAG, embedding,
summarization, freshness calculation, synchronization, state transition,
handoff, workflow, or runtime behavior; null or fabricated absence; canonical
JSON assumptions; and schema validity as truth or acceptance.

## Validation

The resource requires strict duplicate-free JSON and UTF-8 checks, official
Draft 2020-12 schema checking, isolated `jsonschema 4.25.1`, exact local
registration of the Common Artifact Envelope, required missing-resource
failure, all twenty expected fixture outcomes, exact
root/constants/eighteen-property payload, source pinning, temporal, freshness,
relationship, peer-relation, uncertainty, stop, handoff, closure, lexical,
collection, and reference-graph assertions, thirty-six protected-blob checks,
link and privacy/security scans, exact eight-path scope, exact one-commit state,
GitHub read-back, and one transparent non-independent exact-head COMMENT
review.

The test manifest uses one public-safe base instance plus ordered declarative
operations to materialize exactly three valid and seventeen invalid instances.
That fixture construction is non-normative test evidence, not an artifact
binding, patch protocol, migration, validator, or implementation contract.

## Security and privacy

Fixtures are synthetic and public-safe. The schema allocates no identity or
authority, grants no permission, verifies no source or claim, retrieves no
content, and implements no access, disclosure, redaction, sanitization,
encryption, retention, archival, disposal, signature, verification, timestamp,
trust, or chain-of-custody mechanism. Secrets, credentials, personal data,
private paths, production configuration, restricted content, provider-specific
assumptions, and private implementation details remain forbidden.

## Authority and conformance boundary

The Proposed resource is non-self-approving. Schema validity proves only
structural satisfaction of this exact resource under the registered common
resource. It grants no contract conformance, source identity, source truth,
freshness, absence, authority, evidence, approval, decision, task authority,
acceptance, integration, release, deployment, publication, merge permission,
or follow-on authority.

Creation, Draft PR publication, and a transparent non-independent review do not
accept or activate the resource. The workflow must stop after the exact-head
review for separate attributable EIGENAAR / Final Authority acceptance.

## Deferred scope and continuing authority boundary

Deferred and unauthorized: Artifact Instances and revision mechanisms;
authority, role, identity, credential, delegation, approval, signature,
verification, trust, timestamp, digest, encoding, canonicalization, encryption,
retrieval, resolver, registry, catalog, cache, bundler, network, selection,
search, ranking, RAG, embedding, summarization, transformation, freshness
calculation, latest-wins, conflict resolution, state, synchronization,
lifecycle, workflow, handoff automation, access, disclosure, redaction,
sanitization, retention, archival, disposal, and chain-of-custody mechanisms;
Serialization Binding; canonical artifact JSON; Extension Module/Profile
mechanisms; validator/output implementations; conformance tooling; migration;
templates; prompts; API; CLI; runtime; private or reference implementation;
provider; product; release; tag; hosted publication; and deployment.

No Ready transition, Accepted promotion, merge, issue closure, or branch
cleanup is authorized by this Proposed decision.
