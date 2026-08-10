# CNTX visual identity

This guide defines the public CNTX house style used by repository-facing
documentation. It is a presentation system, not a normative architecture,
identity-allocation mechanism, product interface, certification mark, or
trademark policy.

## Brand idea

The CNTX mark combines three ideas:

- an explicit outer boundary for scoped work;
- connected context and evidence points;
- a central diamond representing attributable human authority.

The geometry is deliberately abstract. It does not represent a particular AI
model, vendor, runtime, provider, product, platform, or domain.

## Core palette

| Token | Hex | Use |
| --- | --- | --- |
| CNTX Violet | `#8B5CF6` | Primary accent, paths, active labels |
| CNTX Purple | `#5B21B6` | Depth, secondary accent |
| Ink | `#111018` | Text and geometry on light backgrounds |
| Night | `#09070F` | Dark canvas |
| Paper | `#FAF9FC` | Light canvas |
| White | `#FFFFFF` | Text and geometry on dark backgrounds |

Use white and purple on dark backgrounds. Use near-black and purple on light
backgrounds. Purple must remain an accent rather than a substitute for all
contrast.

## Typography

- Use the platform's modern sans-serif UI stack for headings and prose.
- Use a monospace face only for exact identities, versions, status tokens,
  paths, hashes, commands, and machine-readable values.
- Prefer short headings, plain language, sentence case, and generous spacing.
- Do not place essential prose inside raster images.

## Logo assets

| Context | Asset |
| --- | --- |
| Dark background | [`cntx-logo-dark.svg`](../assets/brand/cntx-logo-dark.svg) |
| Light background | [`cntx-logo-light.svg`](../assets/brand/cntx-logo-light.svg) |

Keep clear space around the mark equal to at least the width of its central
diamond. Do not rotate, stretch, recolor, add shadows, add gradients, or merge
the mark with a provider or product logo.

## Illustration and diagrams

Use bounded geometric modules, explicit narrow paths, evidence markers, and a
visibly separate human-decision point. Diagrams should explain one relationship
at a time, carry useful alternative text, and remain readable without color.

Avoid robots, brains, faces, magic effects, autonomous-authority metaphors,
provider imagery, photorealistic agents, and decorative complexity. CNTX should
look calm, exact, open, and inspectable.

The compact homepage roadmap uses the paired
[`cntx-roadmap-light.svg`](../assets/brand/cntx-roadmap-light.svg) and
[`cntx-roadmap-dark.svg`](../assets/brand/cntx-roadmap-dark.svg) assets. It shows
evidence-based phase order, not a promised delivery date or automatic
authorization for the next phase.

## Labels and discoverability

Recommended descriptive labels are:

`AI collaboration` · `context engineering` · `task delegation` ·
`human-in-the-loop` · `evidence` · `governance` · `JSON Schema` ·
`multi-agent systems` · `vendor-neutral specification`

Labels describe the public subject. They must not imply implementation,
certification, support, production readiness, compatibility, or approval.

## Accessibility

- Maintain at least 4.5:1 contrast for normal text.
- Never rely on purple alone to communicate status or direction.
- Provide text equivalents for every explanatory image.
- Preserve a logical reading order outside diagrams.
- Use the light/dark asset pairs through the HTML `picture` element.

## Provenance

The two collaboration hero illustrations were generated from original
project-specific prompts and selected as public presentation assets. The logo,
status labels, and explanatory diagrams are deterministic project-local SVGs.
All assets are subordinate to the repository license and governance.
