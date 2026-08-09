# Topics

> **English** | [简体中文](../zh/topics/README.md)

Literature-review pages, one per canonical evaluation direction.

Topic pages are the **methodology axis** — one of the repository's three co-equal entry points, alongside the field axis in [`../domains/`](../domains/) and the research-activity axis in [`../activities/`](../activities/). A reader interested in an evaluation methodology should start here and follow links into [`../works/`](../works/), then to the original papers:

```
Topic  →  Representative works  →  Original papers
```

## Canonical topic taxonomy

The set of topics is fixed. Adding a new topic requires updating [`../AGENT.md`](../AGENT.md).

| # | Topic | File | Related works |
|---|---|---|---|
| I | [General Long-Horizon Agent Benchmarks](./long_horizon_evaluation.md) | `long_horizon_evaluation.md` | 40 |
| II | [Scientific Agent Benchmarks](./scientific_agents.md) | `scientific_agents.md` | 156 |
| III | [Trajectory Evaluation](./trajectory_evaluation.md) | `trajectory_evaluation.md` | 29 |
| IV | [Skill Hierarchy](./skill_hierarchy.md) | `skill_hierarchy.md` | 10 |
| V | [Credit Assignment](./credit_assignment.md) | `credit_assignment.md` | 17 |
| VI | [Resource-aware Evaluation](./resource_aware_evaluation.md) | `resource_aware_evaluation.md` | 13 |
| VII | [Survey](./survey.md) | `survey.md` | 5 |

Skill Hierarchy and Credit Assignment are independent topics.

**Topics are not mutually exclusive.** A work may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. Cross-topic membership is the intended pattern, not an exception.

## Filename conventions

- **Evaluation-direction topics** use the `_evaluation.md` suffix: `trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`.
- **Broader topics** keep natural names: `scientific_agents.md`, `skill_hierarchy.md`, `credit_assignment.md`, `survey.md`.

## Topic page template

```markdown
# <Topic Name>

> **English** | [简体中文](../zh/topics/<topic_file>.md) · [← All topics](./README.md)

## Definition

Concise definition of the topic. One paragraph.

## Motivation

Why this topic matters for scientific evaluation. What problems does it
address? What would be missing without it?

## Existing Approaches

Representative work, grouped or ordered in whatever way best illuminates the
topic. Cite work cards from `../works/` rather than restating their factual
details.

## Comparison

A comparison table or matrix using dimensions that fit **this** topic — do
not try to reuse dimensions from other topics.

## Open Questions

Current challenges and future research directions. Mark clearly as forward-
looking rather than as established facts.

## Related Works

- [<Work Name>](../works/<work-card>.md) — one-line reason for inclusion.
```

## Topic page rules

- **Language switcher and breadcrumb.** Every page carries one quote line directly under the H1 combining the switcher and a link back to this index: `> **English** | [简体中文](../zh/topics/<file>.md) · [← All topics](./README.md)` on English pages, and `> [English](../../topics/<file>.md) | **简体中文** · [← 全部 topics](./README.md)` on the Chinese mirror.
- **No global comparison matrix.** Each topic owns its own dimensions. Do not link topic pages together through a shared table.
- **Synthesis, not summary.** A topic page should explain the design space of the topic, not restate individual work cards. When a work's details are needed, link to its card.
- **Related Works is the reverse index.** Every work listed here must include this topic in its card's `Topics` block, and vice versa. Keeping the two sides in sync is a maintenance responsibility.
- **Objective.** No comparison against any maintainer's own project.
- **References are verified.** Same two-level standard as work cards — link and content validation, `TODO(reference)` when a number cannot be verified from the primary source.
