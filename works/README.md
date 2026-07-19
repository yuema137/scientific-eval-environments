# Works

Factual reference cards for individual pieces of prior work.

**"Works"** is broader than "benchmarks." This directory holds a card for every piece of work the repository documents, including:

- **Benchmarks** — task suites with scoring protocols.
- **Methodologies** — evaluation methods, metrics, and protocols (LLM-jury, dense-reward grading, scaffolded-capability assessment, etc.).
- **Frameworks** — evaluation infrastructure that overlays existing benchmarks (diagnostic audit protocols, trace-analysis systems, ground-truth generation toolkits).
- **RL work on agents** — reinforcement-learning contributions whose focus is *evaluating* agents (reward design for agents, credit-assignment methods, off-policy evaluation of agent trajectories). Pure RL algorithm / training / policy-optimization work remains out of scope; see [`../AGENT.md`](../AGENT.md).
- **Reference papers** — surveys and position papers, tagged as such on the card.

Each work has **one** Markdown file directly under this directory — no per-category sub-folders. Filenames use kebab-case matching the work's canonical name (e.g., `terminal-bench-science.md`, `medhelm.md`, `trace.md`).

## What a card is (and is not)

A card answers: **"What is this work?"**

A card is **not** a literature review. Synthesis, comparisons, and design-space analysis live in [`../topics/`](../topics/).

Keep cards lightweight. If a comparison or analysis is worth writing, it belongs in a topic page.

## Card template

Copy this structure verbatim. Do not add sections. Do not remove sections (leave a section empty or write `N/A` with a note if the work does not have that surface — e.g., a survey card has `N/A — survey paper` under Tasks and Evaluation).

```markdown
# <Work Name> (<Year>)

## Overview

One or two sentences describing what the work is.

## Topics

- [<Topic Name>](../topics/<topic_file>.md)
- [<Topic Name>](../topics/<topic_file>.md)

## Links

- **Paper:** <verified URL>
- **Project:** <verified URL or omit>
- **Code:** <verified URL or omit>
- **Venue:** <verified venue or omit>

## Summary

Two to four sentences describing the work's overall design and goals.

## Tasks

Task count, task types, and how tasks were constructed. `N/A` with a note for
non-benchmark works (surveys, position papers).

## Domains

Scientific or application domains covered.

## Evaluation

How answers/trajectories are scored (deterministic verifiers, expert rubrics,
LLM judges, execution-based checks, etc.). `N/A` with a note for surveys and
position papers.

## Typical Duration

Expected trajectory length, wall-clock time, or token budget per task.

## Main Contribution

The work's stated novelty, in the authors' own framing.

## Key Design Ideas

Bulleted list of concrete design choices worth highlighting.

## Strengths

Bullet list. Cite the paper or project source where possible.

## Limitations

Bullet list. Cite the paper or project source where possible. Observations
made by this repository (not the authors) must be marked `Repository note:`.

## Related Works

- [<Other Work>](./<other-card>.md) — one-line reason for the relationship.
```

## Card rules

- **`Topics` is a metadata block, not decoration.** It is the internal index that keeps topic pages in sync. Every topic listed here must have a corresponding entry in that topic page's `Related Works` section, and vice versa. Only draw from the canonical topic taxonomy defined in [`../AGENT.md`](../AGENT.md).
- **No positioning.** Do not include "Gap to Our Work", "Comparison with Our Framework", or any section that frames a work against a maintainer's own project.
- **Two-level reference validation** before commit:
  - *Link validation*: title, URL, project, venue, year — verified against the actual source.
  - *Content validation*: statistics, task counts, metrics, reported numbers — verified from the **original paper or official project only**, never secondary sources. Unverifiable content becomes `TODO(reference)` — do not guess or infer from summaries.
- **Template stability.** Do not modify the template's structure to fit one card. Add new evaluation dimensions to topic pages instead.
- **Repository Notes are conservative.** Author-stated claims are unmarked. Anything the repository adds is prefixed `Repository note:`. Allowed: maintenance observations, cross-paper synthesis, direct consequences of what the paper describes. Not allowed: speculative critique, opinion, extrapolation to settings the paper does not evaluate. If an observation is not clearly supported by the cited literature, it does not belong in the card.
