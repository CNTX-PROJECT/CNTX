# Contributing to CNTX

CNTX welcomes small, inspectable contributions that begin with an agreed
scope. You do not need to understand the whole specification before proposing
one bounded improvement.

## Contribution route

`Discuss or open an issue → agree the scope → change only that scope → validate → open a Draft PR → respond to review → wait for a human decision`

| Your contribution changes… | Read first… |
| --- | --- |
| Architecture, contracts, or public meaning | [Governance](GOVERNANCE.md) and the [architecture index](docs/architecture/README.md) |
| JSON representation | The governing [contract](docs/contracts/README.md), [schema](schemas/README.md), and [tests](tests/README.md) |
| Public documentation | The relevant source page and its exact current links |
| Security or privacy handling | [Security policy](SECURITY.md) and private maintainer guidance |

The safest useful contribution is usually the smallest one that can be
reviewed independently. A submitted change grants no merge, release, or scope
authority.

## Start with scope

For non-trivial work, start with an issue or an approved task contract. Keep each branch and pull request small, scoped, and reviewable. Follow [AGENTS.md](AGENTS.md) in all agent-assisted work.

Do not assume authority to make architectural, security, privacy, release, or scope decisions. Architectural changes require explicit approval under [GOVERNANCE.md](GOVERNANCE.md).

## Prepare a contribution

1. Inspect the relevant repository state and approved scope before editing.
2. Change only the paths and behavior authorized by that scope.
3. Add or update documentation when a public contract, behavior, or decision changes.
4. Run the relevant tests and validations, and record commands, results, assumptions, and evidence in the pull request.
5. Link the issue or approved task and explain the changed paths, risks, and reviewer needs.

Never commit or disclose secrets, credentials, personal data, private project-specific context, production configuration, or copied private material.

## Sign-off and review

Contributors should describe that they have authority to submit their work and any applicable licensing terms. CNTX does not currently claim a Contributor License Agreement (CLA) or Developer Certificate of Origin (DCO); do not imply that either is configured. All changes remain subject to human review and approval.
