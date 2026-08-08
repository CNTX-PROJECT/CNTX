# CNTX Public-Core Release Identity and Version Policy

## Status and authority

**Policy Status:** Proposed.

**Frozen preparation baseline:** public commit
`91f55fc53e78ff847b27d036cafb1e25b34b5a81`, tree
`a739a5d5d0259e3a6a74ddb54a98c5d4ba4b6b75`.

**Governing task:** [REMEDIATE-002 issue #86](https://github.com/CNTX-PROJECT/CNTX/issues/86),
with attributable EIGENAAR / Final Authority creation authority in comment
`5226346595`.

This policy is a documentation-only proposal. It does not allocate an active
Release Version, create or move a tag, select a final release subject, approve
a release, create a GitHub Release, publish, distribute, support, certify, or
deploy anything.

It remains subordinate to the Accepted identity/version separation in
ARCH-002 and the Accepted release-readiness and publication boundary in
ARCH-026.

## Logical Release Identity

The proposed stable logical identity of the release family is:

> `CNTX Public Core Release`

The identity denotes the public-core release family. It is separate from:

- repository, organization, project, branch, commit, tree, and tag identity;
- Architecture, ADR, Contract Definition, Schema, Serialization Binding,
  Artifact Instance, assessment, remediation, evidence, and release-record
  identities and versions;
- release lifecycle status, support status, compatibility claims,
  implementation identity, provider identity, and publication channel; and
- any product, runtime, deployment, private implementation, or reference
  implementation.

No value from another identity or version dimension silently determines this
Release Identity or a Release Version.

Release Version is specifically separate from Contract Definition Version,
Schema Version, Binding Version, Artifact Revision, commit, tag, publication
revision, support status, and implementation version.

## Version syntax and meaning

A Release Version uses Semantic Versioning `MAJOR.MINOR.PATCH`, optionally
with a prerelease identifier. Version precedence and syntax follow
[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); this policy
adds CNTX release-governance boundaries but does not modify that specification.

For later, separately authorized version selection:

- `MAJOR` denotes intentionally incompatible public-core release change once
  a stable line exists;
- `MINOR` denotes compatible public-core capability within an applicable
  stable release line;
- `PATCH` denotes a compatible correction within an applicable release line;
- a prerelease identifier denotes instability and lower precedence than the
  associated normal version; and
- every selected version must bind to one exact, immutable public commit and
  tree through a separate release decision and record.

Version-number shape alone never proves compatibility, conformance,
correctness, support, security, privacy, legal sufficiency, fitness, or release
readiness. Those require their own evidence and attributable decisions.

## Prospective first prerelease target

The proposed decision input for a possible first prerelease is:

- Release Version: `0.1.0-prealpha.1`
- tag representation: `v0.1.0-prealpha.1`

Both `0.x` and `prealpha` communicate deliberate instability and non-support,
not readiness, compatibility, fitness, or release approval. The numeric suffix permits
ordered future pre-alpha candidates if separately governed. A later candidate
must use a new higher prerelease identifier; a published or historically used
version or tag must never be silently reused for different content.

These values are prospective only. They are not active, accepted release
state, a reserved Git object, or authorization to create or move a tag. At the
time of this proposal, CNTX has no tag or GitHub Release.

## Instability and compatibility boundary

Before a stable `1.0.0` release, public definitions, schemas, policies,
packaging, and release composition may change incompatibly between release
versions. A prerelease consumer must pin the exact Release Version and exact
published subject and must not rely on mutable aliases such as `latest`.

No prerelease creates a supported line, compatibility guarantee, migration
promise, maintenance period, security-update commitment, service level,
production-readiness claim, or fitness warranty. Compatibility is assessed
only within the explicit scope of a separately governed release decision and
its evidence.

## Selection and activation lifecycle

A Release Version becomes active only after all of the following are separately
and attributably governed:

1. an exact immutable release subject and complete inclusion/exclusion set;
2. a release-readiness assessment of that subject and evidence;
3. a separate EIGENAAR / Final Authority release decision naming the exact
   version, subject commit/tree, publication set, tag, channel, limitations,
   and permitted consequential actions;
4. creation and verification of the authorized immutable tag and release
   record; and
5. execution and read-back of only the authorized publication action.

Candidate drafting, review, acceptance, integration, assessment, final
decision, version selection, tag creation, GitHub Release creation,
publication, correction, withdrawal, support, and deployment are separate
events. An assessment, remediation record, accepted policy, repository state,
Draft pull request, review, merged commit, or version-like text does not
substitute for any of these gates.

## Historical integrity, correction, and withdrawal

A released version and its tag must remain bound to the originally authorized
subject. Corrections use a new release version or an additive, attributable
notice; they do not rewrite or move historical tags. Withdrawal or
deprecation preserves the original record, states the exact reason and scope
that may be publicly disclosed, and requires separate authority.

No correction, withdrawal, tag operation, release operation, or publication
is authorized by this Proposed policy.

## Non-authority

This policy grants no release recommendation, approval, decision, release
record, manifest, package, archive, BOM, SBOM, digest, signature, attestation,
certification, supported-version claim, compatibility guarantee, support
service, security/privacy/legal/compliance claim, publication, distribution,
deployment, implementation, stable `1.0.0` release, release date, or follow-on
authority.
