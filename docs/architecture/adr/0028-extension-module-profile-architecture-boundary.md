# ADR-0028: CNTX Extension Module and Profile architecture boundary

- **Status:** Accepted
- **Date:** 2026-08-09
- **Issue:** [#98](https://github.com/CNTX-PROJECT/CNTX/issues/98)
- **Creation authority comment:** [5228583661](https://github.com/CNTX-PROJECT/CNTX/issues/98#issuecomment-5228583661)
- **Exact-head acceptance comment:** [5228762336](https://github.com/CNTX-PROJECT/CNTX/issues/98#issuecomment-5228762336)
- **Decision:** ARCH-028 — CNTX Extension Module and Profile Architecture
  Boundary

## Context

Accepted ARCH-027 completed the initial CNTX Public-Core specification and
prerelease cycle and placed the repository on a quiescent, event-driven
maintenance boundary. It did not create Extension Module or Profile
mechanisms. It requires separate Accepted architecture before either category
can be introduced.

CNTX needs an architecture boundary before concrete identity, version,
composition, schema, declaration, conformance, tooling, or implementation work
could be considered. Without that boundary, an extension or profile could
silently weaken the Core, hide dependencies, introduce implicit precedence,
or confuse technical support with normative authority.

## Decision

Adopt separate optional categories for future Extension Modules and Profiles.

An Extension Module is a possible independently identity/version-bearing,
additive capability contract. It cannot alter, replace, weaken, or redefine the
Accepted Core.

A Profile is a possible independently identity/version-bearing constraint and
selection contract over exact pinned Core and optional module versions. It may
only select, require, or narrow capabilities; it cannot weaken, contradict,
replace, or invent them.

Preserve Core sovereignty. Extension Modules and Profiles are not Core
contracts, Schema Resources, Artifact Instances, Serialization Bindings,
validator configurations, implementation flags, products, deployments, or
release channels.

Require explicit opt-in and exact pins for future activation. Prohibit
inference, ambient state, repository presence, mutable aliases, `latest`,
latest-wins, automatic discovery, fallback, and automatic network access as
sources of activation or authority.

Keep identity, versioning, provenance, authority, dependency, activation,
declaration, composition, conflict, unknown/unsupported handling,
supply/resolution, compatibility, conformance/evidence, security/privacy, and
lifecycle responsibilities separate.

Require fail-closed handling for contradiction, collision, ambiguity, missing
dependencies, unknown mechanisms, unsupported capabilities, and insufficient
governing evidence. Create no implicit precedence, document-order rule,
ranking, scoring, majority, consensus, newest-wins, or automatic conflict
resolution.

Order later decisions dependency-first:

1. concrete identity and version policy;
2. dependency, activation, composition, and conflict;
3. Schema Resource, packaging, and declaration model;
4. executable schema and validation/conformance; and
5. separately authorized tooling or implementation.

This order authorizes none of those later phases.

## Core sovereignty

The Accepted Core remains independently meaningful and processable for its
stated scope. A future Extension Module or Profile cannot:

- edit an Accepted Core source;
- replace a Core identity or version;
- weaken a Core requirement or assertion;
- convert a Core-invalid representation to Core-valid;
- bypass a prerequisite or governing-input failure;
- turn missing or uncertain evidence into proof;
- change an assessment, decision, release, or verification outcome; or
- bypass attributable final human authority.

Conflict with the exact pinned Core must fail closed. Implementation behavior
cannot override normative Core semantics.

## Extension Module boundary

A future Extension Module may add only capabilities that later Accepted
architecture explicitly permits. It requires its own identity, version,
authoritative source, provenance, dependencies, compatibility treatment,
security/privacy handling, conformance scope, and lifecycle.

No Extension Module is allocated, activated, represented, validated, or
implemented here.

## Profile boundary

A future Profile may constrain only exact pinned inputs. It cannot create an
absent module capability, silently select a mutable version, infer support, or
grant acceptance or permission.

No Profile is allocated, activated, represented, validated, or implemented
here.

## Conflict and unknown handling

Future processing must expose and stop on material contradiction, collision,
ambiguous identity/version, undeclared dependency, missing authoritative
source, unsupported mechanism, or insufficient governing evidence.

No conflict is resolved by load order, document order, registration order,
lexical order, specificity guesses, latest version, popularity, cached state,
implementation preference, majority, consensus, ranking, scoring, or fallback.

Unknown and unsupported mechanisms remain visible. This decision allocates no
portable error, outcome, severity, or warning vocabulary.

## Supply, compatibility, and conformance

Accepted caller-supplied, offline-first, closed resolution boundaries remain
unchanged. Repository presence, URL availability, discovery, retrieval, cache,
or registry listing establishes no authority or trust.

Future compatibility claims must be scoped to exact identities, versions,
governing context, conformance dimensions, evidence, evaluator capabilities,
limitations, time, claimant, and authority.

Schema validity does not prove contract, implementation, interoperability,
security, privacy, support, certification, or release conformance. No aggregate
compatibility or conformance result is created.

## Security and privacy

Later work must address untrusted input, resource exhaustion, recursive
composition, dependency minimization, least privilege, provenance, restricted
evidence, disclosure, data minimization, correction, withdrawal, and the
public/private boundary.

No access, disclosure, trust, authenticity, security, privacy, legal, or
compliance authority is created.

## Consequences

Positive consequences:

- optional growth cannot silently redefine the Core;
- Extension Modules and Profiles remain distinct;
- activation requires explicit exact pins;
- dependency and conflict conditions remain visible;
- compatibility and conformance claims remain scoped; and
- executable work remains behind dependency-first decisions.

Costs and limitations:

- no Extension Module or Profile can yet be allocated or used;
- concrete identity/version and composition architecture still require later
  decisions;
- unknown or unsupported mechanisms may block dependent evaluation;
- no universal interoperability, compatibility, support, or certification is
  established; and
- no tooling or implementation is provided.

## Alternatives not selected

### Treat every extension as an unconstrained opaque field

Not selected because it would not define identity, authority, dependency,
conflict, compatibility, or conformance boundaries.

### Treat Profiles as Extension Modules

Not selected because additive capability and constraint/selection have
different authority and conflict responsibilities.

### Allow implementations to choose precedence

Not selected because implementation-specific load or processing order would
silently redefine public semantics.

### Use `latest` or automatic discovery

Not selected because mutable or ambient selection prevents exact governing
context and reproducible evidence.

### Define executable schemas immediately

Not selected because identity/version, activation, composition, conflict,
resource, and declaration decisions must precede executable schema work.

## Non-decisions

This ADR creates no concrete Extension Module or Profile, Identifier, Version,
version policy, dependency/compatibility range, precedence, declaration token,
field, vocabulary, `$id`, Schema Resource, executable schema, manifest,
package, catalog, registry, resolver, cache, bundler, validator, conformance
suite, canonical JSON, digest, signature, attestation, media type, or
Serialization Binding.

It creates no Artifact Instance, API, CLI, workflow, automation, runtime,
provider/product work, private/reference implementation, support service,
hosted publication, distribution, deployment, release, tag, GitHub Release,
maintenance action, correction, withdrawal, deprecation, supersession,
reassessment, ARCH-029, or follow-on authority.

## Authority boundary

This ADR is Accepted. Creation authority, repository presence, validation, and
transparent non-independent ARCHITECT review did not grant acceptance.
Separate attributable EIGENAAR / Final Authority acceptance of the exact
reviewed revision is recorded in issue comment `5228762336`; governed
integration makes the decision binding.

Acceptance adopts only this architecture boundary. It does not allocate,
activate, represent, validate, implement, publish, distribute, or deploy an
Extension Module or Profile or authorize a later phase.
