# Repository Constitution

You are the long-term maintainer of this repository.

This repository is **NOT** a benchmark implementation.

It is an **open knowledge base documenting scientific evaluation environments** — the design space of how AI agents are evaluated on scientific and long-horizon tasks.

Its purpose is to organize existing knowledge about:

- scientific benchmarks
- evaluation methodologies and metrics
- evaluation frameworks and diagnostic protocols
- trajectory evaluation
- resource-aware evaluation
- scientific workflows
- evaluation-focused RL work on agents
- benchmark design

The repository must remain **objective**. It must **not** contain discussion about any future benchmark the maintainers are working on. It should stand as a useful, standalone reference for anyone working on scientific evaluation.

---

## Repository Organization

The repository has **only two primary knowledge layers**.

### Layer 1 — Works

Directory: `works/`

- **Flat directory.** Every documented work lives directly under `works/` as a single Markdown file — no per-category sub-folders. Each work appears in exactly one place.
- Cards are **factual references**. They answer *"What is this work?"* — not *"How does it compare to everything else?"* Synthesis belongs in topic pages, not cards.
- Cards must be **lightweight**. Do not let a card grow into a literature review.

**"Works" is broader than "benchmarks."** The directory holds cards for benchmarks, evaluation methodologies, evaluation frameworks (diagnostic overlays, trace-analysis systems, ground-truth generation toolkits), evaluation-focused RL contributions, surveys, and position papers. Non-benchmark works keep the same card structure — sections that do not apply are filled with `N/A` and a short note (e.g., `N/A — survey paper`).

**Card template:**

- Overview
- **Topics** *(metadata block — bulleted list of topic pages this work belongs to)*
- Links
- Summary
- Tasks
- Domains
- Evaluation
- Typical Duration
- Main Contribution
- Key Design Ideas
- Strengths
- Limitations
- Related Works

The `Topics` block is not just navigation for readers — it is the **internal index** used to keep topic pages in sync. When a new topic page is added, its `Topics` entry on each relevant card is how a maintainer finds the cards to link. When a card is updated, its `Topics` block tells the maintainer which topic pages may need synchronization.

**Do NOT include** sections such as:

- Gap to Our Work
- Comparison with Our Framework
- Our Positioning
- Any other section that positions a work against a maintainer's own project

**Template stability.** Once the card template is established, avoid changing its structure. Consistency across cards is more valuable than optimizing individual pages. New evaluation dimensions should extend **topic pages**, not card fields.

**Repository Notes discipline.** Any observation that is not stated by the paper or official project must be prefixed `Repository note:`. Repository Notes must be conservative:

- Allowed: maintenance observations, factual synthesis across multiple papers, repository-specific organizational notes, observations that are direct consequences of what the paper describes.
- Not allowed: speculative critique, opinion about the field, extrapolations from the paper's results to settings the paper does not evaluate, judgment calls about what the authors *should* have done.

If an observation cannot be reasonably supported by the cited literature, it should not appear as a Repository Note.

### Layer 2 — Topics

Directory: `topics/`

Each topic summarizes one important evaluation direction and acts as a **literature review**.

**Canonical topic taxonomy.** The repository organizes topics around this fixed set:

| # | Topic | File |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | `long_horizon_evaluation.md` |
| II | Scientific Agent Benchmarks | `scientific_agents.md` |
| III | Trajectory Evaluation | `trajectory_evaluation.md` |
| IV | Skill Hierarchy | `skill_hierarchy.md` |
| V | Credit Assignment | `credit_assignment.md` |
| VI | Resource-aware Evaluation | `resource_aware_evaluation.md` |
| VII | Survey | `survey.md` |

Skill Hierarchy and Credit Assignment are **two independent topics**. Do not merge them.

Adding a new canonical topic is a structural decision that requires updating this table.

**Filename convention within the taxonomy:**

- Evaluation-direction topics use the `_evaluation.md` suffix (`trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`).
- Broader topics use natural names (`scientific_agents.md`, `skill_hierarchy.md`, `credit_assignment.md`, `survey.md`).

**Topic page template:**

- **Definition** — concise definition of the topic.
- **Motivation** — why this topic matters.
- **Existing Approaches** — representative work.
- **Comparison** — comparison table(s) using dimensions specific to this topic.
- **Open Questions** — current challenges and future directions.
- **Related Works** — links to work cards in `works/`.

There is **no global comparison matrix**. Each topic owns its own comparison dimensions.

---

## Relationship Between Works and Topics

**Topics are not mutually exclusive.** A work may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. Do not force a work into a single topic to "keep things tidy" — cross-topic membership is the intended pattern, not an exception.

- Work pages document **individual projects** (facts).
- Topic pages **synthesize** across works.
- A work **belongs to multiple topics**. That mapping is expressed twice, redundantly on purpose:
  - in the card's `Topics` metadata block, and
  - in each topic page's `Related Works` section.

Example mappings from the canonical taxonomy:

```
TRACE                  → trajectory_evaluation, long_horizon_evaluation
Terminal-Bench Science → scientific_agents, long_horizon_evaluation
CostBench              → resource_aware_evaluation
AgentBoard             → trajectory_evaluation, skill_hierarchy
```

**Topic pages are the primary entry point.** A reader interested in a research direction should start from `topics/`, follow links into `works/`, and from there to the original papers:

```
Topic  →  Representative works  →  Original papers
```

---

## Documentation Principles

- Documentation comes first.
- Prefer Markdown.
- Keep files reasonably small.
- Avoid duplication.
- Prefer **linking** over **copying**.

The repository should feel like a technical handbook rather than research notes.

---

## References

Zero tolerance for fabricated references.

Every claim added to the repository must be verified. There are **two distinct levels of verification**, and both are required:

### Link validation

Verify the following against the actual source:

- paper title
- URL (paper, project, code)
- venue
- publication year

### Content validation

Verify the following **from the original paper or official project only** — never from secondary sources or summaries:

- benchmark statistics
- task counts
- evaluation metrics
- reported numbers
- benchmark settings

If a statistic cannot be verified from the primary source, use `TODO(reference)` instead of guessing. **Never infer numbers from secondary sources** (blog posts, tweets, other summaries).

Preferred primary sources:

- arXiv
- OpenReview
- ACL Anthology
- Nature
- Science
- Official GitHub repositories
- Official project websites
- Workshop / conference proceedings (NeurIPS workshops, etc.)

**Correctness is always more important than completeness.**

---

## Bilingual Documentation

Maintain both English and Chinese versions.

**English is always the canonical version.**

Chinese pages mirror the English tree under `zh/` (`zh/works/`, `zh/topics/`).

**Cadence.** English and Chinese documentation must not diverge for long. The working cycle is:

1. Finish one batch of English pages.
2. Review.
3. Synchronize the corresponding Chinese pages.
4. Only then begin the next English batch.

Do not postpone Chinese translation until the whole repository is complete.

Translation rules:

- work names remain in English
- paper titles remain in English
- project names remain in English
- proper nouns remain in English
- technical terminology may remain in English where appropriate

Translate explanations naturally, not literally.

---

## Scope

**In scope:**

- Scientific evaluation environments
- Benchmark landscape
- Evaluation methodology and metrics
- Evaluation frameworks and diagnostic protocols
- Scientific workflows
- Trajectory evaluation
- Resource-aware evaluation
- Benchmark design
- **Evaluation-focused RL work on agents** — reward design for agents, credit-assignment methods, off-policy evaluation of agent trajectories, and similar contributions whose focus is *evaluating* agents.

**Out of scope (for now):**

- Pure RL algorithm development
- Policy optimization and training procedures
- Agent implementation
- Multi-agent systems
- Memory systems

The distinction between in-scope and out-of-scope RL work is the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

---

## Goal

The final repository should read like a well-organized technical handbook.

- Work cards provide **factual documentation**.
- Topic pages provide **synthesis** and serve as the primary entry point.

Together they should give any reader a clear understanding of the current scientific evaluation landscape.
