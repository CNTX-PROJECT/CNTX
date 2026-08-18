# How OPENCNTX works

OPENCNTX solves one practical problem: large or mixed project history makes it
hard to give an AI tool only the information needed for the current task.

## The simple idea

1. You state one goal.
2. You choose allowed local files.
3. OPENCNTX builds a bounded text package.
4. It records hashes and budgets.
5. You inspect and verify the package.
6. You decide whether to share it.

![Selected local files become a small reviewable package before any external sharing](../assets/docs/opencntx-overview.svg)

## What “any model” means

OPENCNTX produces ordinary text and JSON files. You may use those files with
ChatGPT, Claude, Gemini, a local model, another provider, or no AI tool at all,
as long as the chosen tool accepts the input format.

It does **not** mean that OPENCNTX:

- calls every model;
- guarantees compatibility with every interface;
- chooses the best provider;
- sends files over the network;
- verifies an AI answer.

## Two layers

### Core layer

`init`, `pack`, and `verify` create and check one context package directly from
a project directory.

### Workspace layer

The optional workspace stores supplied sources, chapters, tasks, playbooks,
roles, approvals, and evidence as readable local records. It can select a
small context set for one approved task.

## Three kinds of evidence

- **Bytes:** the exact stored or selected content.
- **Digests:** SHA-256 values that reveal changed bytes.
- **Decisions:** explicit OWNER approvals bound to exact objects.

None of these proves that a statement is true. They make the process easier to
inspect and reproduce.

## Why it stays local

Local-first behavior keeps selection and review under your control. OPENCNTX
has no network client, account system, cloud database, or provider SDK. The
boundary changes only when you deliberately move output elsewhere.

## Next pages

- [Getting started](getting-started.md)
- [Context packages](context-packets.md)
- [Workspace](workspace.md)
- [OWNER flow](owner-flow.md)
- [Security](security.md)

[Documentation home](README.md)
