# CNTX Public-Core Completion and Maintenance Boundary (ARCH-027)

## Status and authority

**Document Status:** Proposed.

This document is a Proposed architecture decision governed by
[issue #96](https://github.com/CNTX-PROJECT/CNTX/issues/96) and recorded by
[ADR-0027](adr/0027-public-core-completion-and-maintenance-boundary.md).
Attributable EIGENAAR / Final Authority creation authority is recorded in
issue comment `5228385928`.

Creation, repository presence, validation, and transparent non-independent
review do not grant acceptance. This proposal becomes Accepted only after
separate attributable EIGENAAR / Final Authority acceptance of its exact
reviewed revision and governed integration to `main`.

## Purpose and decision boundary

Accepted VERIFY-001 completes the initial CNTX Public-Core specification and
prerelease cycle. That completion must be stated precisely without expanding
it into project archival, supported-version status, a maintenance promise,
implementation or runtime completion, hosted-publication completion, or
deployment.

This proposal therefore:

1. names the exact completed initial Public-Core cycle;
2. keeps separate completion categories separate;
3. records the later completion of the remaining-layer roadmap established by
   ARCH-021 without rewriting ARCH-021 history;
4. defines a quiescent, event-driven, non-active maintenance boundary;
5. classifies possible future changes behind new governance gates;
6. preserves immutable release history, evidence limitations, the
   public/private boundary, and final human authority; and
7. authorizes no maintenance or other follow-on action.

This decision is documentation-only. It creates no correction, withdrawal,
release object, support commitment, implementation, hosted publication, or
deployment.

## Exact decision basis

This proposal was prepared on exact public baseline
`a30dd2eff01f5e6d51454560b8149d307809db01` and tree
`1179ed6ec3af272d5147c9e392f10153b9be6387`.

The controlling Accepted basis includes:

- ARCH-001 through ARCH-026 and ADR-0001 through ADR-0026;
- CONTRACT-001 through CONTRACT-009;
- one Accepted Common Artifact Envelope Schema Version `1.0.0`;
- nine Accepted artifact-specific Schema Versions `1.0.0`;
- nine active Contract Definition Identifier/Version/source-binding sets;
- ten synthetic schema test manifests;
- Core Artifact JSON Binding Version `1.0.0`;
- the Accepted Schema Resource Resolution and Catalog Boundary;
- the Accepted Validation and Validation Output Contract;
- the Accepted Portable Conformance Evidence Boundary;
- the Accepted Public-Core Release Readiness and Publication Boundary;
- Accepted ASSESS-001, ASSESS-002, and ASSESS-003;
- Accepted REMEDIATE-001 and REMEDIATE-002;
- Accepted DECIDE-001 with disposition `Approve`;
- Accepted RELEASE-001 and its separately authorized publication execution;
  and
- Accepted VERIFY-001.

This proposal changes none of those sources, their status, identifiers,
versions, evidence, limitations, or authority.

## Completed initial Public-Core cycle

The **completed initial CNTX Public-Core specification and prerelease cycle**
comprises:

1. public governance, authority, privacy, identity, versioning, provenance,
   artifact-family, lifecycle, and architecture foundations;
2. nine Accepted Public-Core Artifact Contracts;
3. the Common Artifact Envelope and nine artifact-specific executable JSON
   Schema resources;
4. exact Contract Definition, Schema, and Binding identities and versions;
5. the Core Artifact JSON Serialization Binding;
6. the Schema Resource Resolution and Catalog Boundary;
7. the Validation and Validation Output Contract;
8. the Portable Conformance Evidence Boundary;
9. the Public-Core Release Readiness and Publication Boundary;
10. three separately governed readiness assessments;
11. two separately governed remediation evidence and policy phases;
12. one attributable Final Release Decision;
13. immutable publication of CNTX Public Core Release Version
    `0.1.0-prealpha.1`; and
14. Accepted point-in-time post-publication verification of the exact release
    subject and channel representations.

This is a completed specification-and-prerelease cycle. It is not an assertion
that every possible CNTX layer, implementation, service, use case, or future
change is complete.

## Completion-category separation

Completion claims must continue to name their category.

| Category | Current boundary | Not implied |
| --- | --- | --- |
| Governance and architecture | Initial Public-Core governance and ARCH-001 through ARCH-026 are Accepted. | Repository archival, future-change authority, or implementation. |
| Contract and schema foundation | Nine contracts, ten active Schema Versions, and their tests are Accepted. | Artifact Instance truth, approval, runtime behavior, or universal conformance. |
| Portable representation and resource supply | Core Artifact JSON Binding and frozen caller-supplied Schema Resource boundaries are Accepted. | Canonical JSON, network discovery, registry service, or transport/storage implementation. |
| Validation and conformance evidence | Validation/output and Portable Conformance Evidence boundaries are Accepted; bounded reproduction evidence exists. | Canonical output/evidence artifacts, universal validator or implementation conformance, certification, or independent reproduction. |
| Release decision and publication | One exact subject was approved and published as immutable prerelease `0.1.0-prealpha.1`. | Supported-version status, compatibility guarantee, production readiness, or future-release authority. |
| Post-publication verification | VERIFY-001 is Accepted as a point-in-time, document-local verification. | Aggregate verification, continuing monitoring, mode/metadata proof, or security/privacy/legal completion. |
| Maintenance | A quiescent governance boundary is defined by this proposal. | A maintenance promise, active task, support service, SLA, or automatic action. |
| Runtime, provider, product, and deployment | Outside the completed Public-Core specification boundary unless separately introduced. | A requirement that one privileged implementation or product define CNTX. |

## Relationship with ARCH-021

ARCH-021 remains an Accepted historical decision. At its 2026-08-07 subject,
it correctly named the completed contract-and-schema foundation and ordered
five then-remaining decision layers:

1. Artifact Serialization Binding architecture;
2. Schema Resource resolution and catalog boundary;
3. Validation and validation-output contract;
4. Portable conformance evidence boundary; and
5. Public-Core release-readiness and publication boundary.

Those layers were later addressed by ARCH-022 through ARCH-026. Their
application was then evaluated and advanced through ASSESS-001/-002/-003,
REMEDIATE-001/-002, DECIDE-001, RELEASE-001, and VERIFY-001 under separate
authority gates.

This proposal records that later state. It does not modify ARCH-021, rewrite
its historical context, or imply that later evidence and outcomes existed when
ARCH-021 was accepted.

## Quiescent maintenance boundary

After completion of the initial cycle, the Public Core enters a **quiescent,
event-driven maintenance boundary**.

At this boundary:

- no public task, issue, branch, or pull request is automatically active;
- no continuing monitoring, validation, verification, or reassessment duty is
  created;
- no update cadence, response time, maintenance duration, end-of-life date,
  service level, or support service is promised;
- Release Version `0.1.0-prealpha.1` remains unsupported pre-alpha material;
- no mutable alias, `latest` designation, or latest-wins authority is created;
- no correction, withdrawal, supersession, release, or implementation is
  triggered automatically; and
- future consequential work starts only after a new exact governance gate is
  satisfied.

`Maintenance boundary` names the governance required if future work is
proposed. It does not promise that such work will be performed.

## Future change categories and gates

### Normative correction

A correction that changes Accepted meaning, requirement, identity, version,
schema assertion, expected validity, binding rule, assessment outcome,
decision, release record, or verification conclusion is normative. It requires
an exact affected-subject analysis, compatibility and provenance treatment,
new attributable authority, and a complete governed lifecycle.

### Non-normative documentation correction

Spelling, navigation, formatting, broken-link, or other non-semantic repair
must still identify exact paths and prove that Accepted meaning and protected
objects are unchanged. Classification as non-normative is not self-authorizing.

### Security or privacy correction

Security or privacy work must follow the disclosure and public/private
boundaries. Restricted evidence must not be exposed to justify a public
change. Access to restricted information and authority to change public
sources remain separate.

### Withdrawal, deprecation, and supersession

Withdrawal, deprecation, and supersession are distinct lifecycle effects. A
future action must identify the exact affected release/source/object, reasons,
replacement or absence of replacement, historical availability, user-facing
limitations, correction relationship, and final authority. None is automatic.

### New assessment or release cycle

A later assessment or release cycle requires a newly frozen subject, current
evidence, explicit limitations, a release decision, a selected version, and
separately authorized execution and verification. This decision creates no
rolling release line or supported-version policy.

### Extension Module or Profile architecture

Extension Module and Profile mechanisms remain optional and absent. Before
introducing them, separate Accepted architecture must define identity,
authority, compatibility, conflict, unknown-mechanism, privacy, resolution,
and conformance boundaries.

### Validator, resolver, and conformance tooling

Any executable validator, resolver, registry, catalog, test runner, or
conformance tool remains implementation work. It must not silently redefine
the Accepted contracts, schemas, binding, resolution boundary, validation
contract, or evidence boundary.

### API, CLI, workflow, runtime, provider, and product work

These remain outside the completed Public-Core specification boundary unless
separately introduced. No public or private implementation becomes normative
merely because it can process CNTX material.

### Hosted publication, distribution, and deployment

The current GitHub prerelease is the recorded channel representation of its
exact subject. A hosted site, mirror, registry, package feed, alternate
distribution, or deployment requires its own identity, provenance, security,
privacy, correction, withdrawal, and authority treatment.

### Common gate for consequential future change

Before any consequential future change begins, its governing authority must
identify at least:

1. repository and exact baseline/tree;
2. exact subject and affected Accepted sources or objects;
3. exact allowed paths and prohibited scope;
4. issue or task contract;
5. evidence, limitations, uncertainty, and adverse/restricted evidence;
6. branch, commit, PR, review, and validation requirements;
7. attributable acceptance and integration gates;
8. completion, closure, synchronization, and any cleanup authority; and
9. correction, withdrawal, compatibility, support, security, privacy, and
   historical-integrity consequences where applicable.

No category or gate in this document authorizes its own execution.

## Immutable release and historical integrity

The completed initial cycle retains the following exact historical release
objects:

- Release Identity: `CNTX Public Core Release`;
- Release Version: `0.1.0-prealpha.1`;
- lightweight tag: `v0.1.0-prealpha.1`;
- release-subject commit:
  `109e6f293b150f48572cd747fab446c141d57193`;
- release-subject tree:
  `446b408e27d3ebd3f6616658c61ccd9db4af8978`;
- GitHub Release database ID: `367290932`;
- GitHub Release node ID: `RE_kwDOTsnR984V5Go0`;
- prerelease and immutable channel flags; and
- zero custom assets.

The tag, Release, Release body, generated source-archive URLs, issues #80,
#92, and #94, PRs #93 and #95, and their Git/GitHub provenance remain
historical objects. This decision does not edit, move, delete, replace,
relabel, or recreate them.

GitHub-generated archives remain derived channel representations. Their
VERIFY-001 hashes remain time-bound, non-canonical evidence and create no
normative digest contract, manifest, signature, attestation, or expanded
release subject.

## Evidence and limitation preservation

Completion preserves, without resolving:

- the Accepted `Unverifiable` security/privacy/legal/disclosure outcome;
- `Not Evaluated` new independent specialist evidence in VERIFY-001;
- the absence of independent human reproduction for the two evaluator runs
  and archive checks operated by ARCHITECT;
- the absence of canonical Portable Conformance Evidence and canonical
  Validation Output Artifact Instances;
- the absence of portable diagnostic, severity, warning, or support
  vocabularies;
- the absence of universal validator, implementation, Artifact Instance,
  interoperability, compatibility, support, certification, or accreditation
  claims;
- the `Unverifiable` exact Git-mode and timestamp/compression/transport-
  metadata equivalence boundaries; and
- the absence of an aggregate VERIFY-001 outcome.

Completed work, favorable evidence, and immutable publication do not turn
missing, adverse, restricted, uncertain, or unverifiable evidence into proof.

## Security, privacy, and public/private boundary

No completion or maintenance label grants access, permission, disclosure,
authenticity, trust, approval, or authority. Secrets, credentials, personal
data, production configuration, private paths, restricted material, private
project context, and private implementation details remain outside public CNTX
sources.

Private orientation, memories, reports, and notes remain subordinate to public
authoritative sources. Possession of private or restricted evidence does not
grant authority to expose it or mutate public records.

Future work must apply data minimization, exact scope, provenance,
least-privilege access, visible limitation handling, and the existing
disclosure boundary.

## Support, compatibility, and non-claim boundary

CNTX Public Core `0.1.0-prealpha.1` remains unsupported pre-alpha material.
This decision creates no:

- supported-version line;
- maintenance period or end-of-life date;
- update or correction promise;
- response-time or service-level commitment;
- compatibility matrix or guarantee;
- production-readiness claim;
- security, privacy, legal, or compliance certification;
- fitness, warranty, merchantability, or absence claim; or
- obligation to publish a later release.

## Non-decisions and prohibited effects

This decision does not define or execute a maintenance action, correction,
withdrawal, deprecation, supersession, reassessment, new release version, tag,
Release, asset, manifest, package, archive, BOM, SBOM, canonical digest,
canonical JSON, signature, attestation, certification, support policy,
compatibility matrix, Extension Module, Profile, Artifact Instance, validator,
resolver, registry, catalog, cache, bundler, mirror, redirect, API, CLI,
workflow, automation, engine, scheduler, orchestrator, runtime, provider,
product, private/reference implementation, hosted site, separate publication,
distribution, deployment, repository archival, repository locking, or
repository deletion.

It changes no repository setting, tag, Release, issue, pull request, Accepted
source, schema, test, identity, version, evidence record, assessment outcome,
decision, or verification result.

## Lifecycle and final human authority

This Proposed document does not approve itself. Creation authority is not
acceptance. Validation, review, mergeability, technical access, and repository
presence grant no consequential authority.

Only separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision, followed by separately authorized status promotion and
governed integration, can make this decision Accepted. Even then, acceptance
would adopt the completion and maintenance boundary only; it would not execute
project closure, maintenance, correction, withdrawal, implementation,
publication, deployment, or another phase.

## References

- [Public Core Completion Boundary and Remaining Layer Roadmap](public-core-completion-boundary-roadmap.md)
- [Core Artifact Serialization Binding](core-artifact-serialization-binding.md)
- [Schema Resource Resolution and Catalog Boundary](schema-resource-resolution-catalog-boundary.md)
- [Validation and Validation Output Contract](validation-and-validation-output-contract.md)
- [Portable Conformance Evidence Boundary](portable-conformance-evidence-boundary.md)
- [Public-Core Release Readiness and Publication Boundary](public-core-release-readiness-publication-boundary.md)
- [Release documentation](../release/README.md)
- [VERIFY-001 post-publication verification](../release/verify-001-public-core-0.1.0-prealpha.1-post-publication.md)
- [Governance](../../GOVERNANCE.md)
- [Security policy](../../SECURITY.md)
- [ADR-0027](adr/0027-public-core-completion-and-maintenance-boundary.md)
- [Issue #96](https://github.com/CNTX-PROJECT/CNTX/issues/96)
