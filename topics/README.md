# Topics

> **English** | [简体中文](../zh/topics/README.md)

Literature-review pages, one per canonical evaluation-research direction.

Topic pages are the **evaluation-research axis** — one of the repository's three co-equal entry points, alongside the field axis in [`../domains/`](../domains/) and the research-activity axis in [`../activities/`](../activities/). They answer three questions: **what do we evaluate, how do we evaluate it, and how is evaluation used to improve agents?**

```
Topic  →  Representative works  →  Original papers
```

## Canonical topic taxonomy

The set of topics is fixed. Adding a new topic requires updating [`../AGENT.md`](../AGENT.md).

| # | Topic | File | Related works |
|---|---|---|---|
| I | [General Long-Horizon Agent Benchmarks](./long_horizon_evaluation.md) | `long_horizon_evaluation.md` | 58 |
| II | [Scientific Agent Benchmarks](./scientific_agents.md) | `scientific_agents.md` | 246 |
| III | [Planning & Decision-Making Evaluation](./planning_decision_evaluation.md) | `planning_decision_evaluation.md` | 11 |
| IV | [Trajectory Evaluation](./trajectory_evaluation.md) | `trajectory_evaluation.md` | 57 |
| V | [Skill Hierarchy](./skill_hierarchy.md) | `skill_hierarchy.md` | 43 |
| VI | [Credit Assignment](./credit_assignment.md) | `credit_assignment.md` | 22 |
| VII | [Resource-aware Evaluation](./resource_aware_evaluation.md) | `resource_aware_evaluation.md` | 21 |
| VIII | [Evaluator Reliability & Validation](./evaluator_reliability_validation.md) | `evaluator_reliability_validation.md` | 8 |
| IX | [Benchmark Design, Validity & Contamination](./benchmark_design_validity_contamination.md) | `benchmark_design_validity_contamination.md` | 11 |
| X | [Skill Learning & Evolution](./skill_learning_evolution.md) | `skill_learning_evolution.md` | 5 |
| XI | [Agent Harnesses & Scaffolding](./agent_harnesses_scaffolding.md) | `agent_harnesses_scaffolding.md` | 7 |
| XII | [Evaluation-Driven Data Curation](./evaluation_driven_data_curation.md) | `evaluation_driven_data_curation.md` | 3 |
| XIII | [Evaluation-Driven Post-Training](./evaluation_driven_post_training.md) | `evaluation_driven_post_training.md` | 4 |
| XIV | [Survey](./survey.md) | `survey.md` | 9 |

Skill Hierarchy and Credit Assignment are independent topics.

**Topics are not mutually exclusive.** A work may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. Cross-topic membership is the intended pattern, not an exception.

## Filename conventions

- **Evaluation-direction topics** may use the `_evaluation.md` suffix where it reads naturally: `trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`.
- **Broader research themes** use natural names: `scientific_agents.md`, `skill_learning_evolution.md`, `agent_harnesses_scaffolding.md`, `survey.md`.

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
