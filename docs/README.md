# OPENCNTX documentation

This is the fastest way to find the right OPENCNTX page. You do not need to
read everything in order.

![OPENCNTX turns selected local files into a small package that you can review before sharing](../assets/docs/opencntx-overview.svg)

## I am new

1. [Install OPENCNTX](installation.md).
2. Follow [Getting started](getting-started.md).
3. Read [How it works](how-it-works.md) when you want the mental model.
4. Use the [FAQ](faq.md) or [Troubleshooting](troubleshooting.md) if something
   is unclear.

## I want a small context package

- [Core commands](core.md) explains `init`, `pack`, and `verify`.
- [Context packages](context-packets.md) explains `CONTEXT.md`,
  `manifest.json`, budgets, review, and drift.
- [Command reference](commands.md) lists every existing CLI path.

## I want a project workspace

- [Workspace](workspace.md) introduces the local directory and capture flow.
- [Chapters and catalog](chapters-and-catalog.md) explains revisions,
  dependencies, `CURRENT`, and the replaceable index.
- [Context navigation](context-navigation.md) explains hot, warm, and cold
  task context.
- [Media and derived text](media.md) explains safe registration of text that
  was already produced elsewhere.

## I manage approval and execution

- [Playbooks and roles](playbooks-and-roles.md) defines bounded methods and
  allowed actions.
- [OWNER flow](owner-flow.md) follows a task from proposal to accepted result.

## I need exact project information

- [Security](security.md) gives the safety model in plain language.
- [Platforms](platforms.md) records supported Python versions and CI evidence.
- [Public roadmap](roadmap.md) shows completed milestones without promising
  unapproved features.
- [Glossary](glossary.md) defines the fixed terms used across the project.
- [Brand guide](brand.md) lists official assets, colors, and usage rules.

## One product boundary

OPENCNTX creates local, explicit, verifiable files. It does not call an AI
model, choose a provider, upload context, run an agent, execute supplied
content, or replace human review. “Any model” means that you may use the
reviewed output with any tool that accepts text or files.

Use `opencntx --help` and the relevant nested `--help` route as the exact source
for command options. Use the root [Security Policy](../SECURITY.md) as the
canonical security boundary.

[Back to the project README](../README.md)
