# Agent Instructions

## Purpose and hard boundaries

CNTX is a public, model-, vendor-, runtime-, and domain-agnostic foundation for bounded, verifiable collaboration. Do not introduce product logic, private implementations, secrets, personal data, credentials, production configuration, provider-specific assumptions, or private project context unless an approved task expressly authorizes it.

## Source of truth and precedence

Apply sources in this order:

1. The current approved issue or task contract.
2. This repository-level `AGENTS.md`.
3. Approved architecture and governance documents.
4. Current repository state and tests.
5. Non-binding discussion and context.

Higher-authority safety and platform instructions remain controlling. If instructions conflict, follow the higher-precedence instruction and report the conflict.

## Working rules

- Inspect the relevant repository state before editing.
- Use minimal context and least privilege; read or change only what the task requires.
- Create small, scoped branches and draft pull requests from the approved base.
- Change only explicitly allowed paths; do not silently broaden scope or perform broad refactors.
- Follow the approved branch, commit, validation, and evidence requirements.
- Record validation commands, results, assumptions, risks, and incomplete work in the final report or pull request.

## Safety and privacy

Never place private context, secrets, credentials, personal data, production configurations, exploitable security details, or copied private project material in public files, commits, pull requests, issues, or comments.

## Stop conditions

Stop and report when required authority, scope, path permission, architecture, security/privacy handling, validation expectations, or repository state is uncertain or conflicts with the task. Do not invent architecture, bypass review, merge autonomously, or claim completion without evidence.
