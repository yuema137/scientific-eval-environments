# A Framework for Evaluating Agentic Skills at Scale (2026)

> **English** | [简体中文](../zh/works/a-framework-for-evaluating-agentic-skills-at-scale.md)

> **First appeared:** 2026-06-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.17819)

## Overview

An evaluation methodology that lets a skill author turn a skill into realistic executable tasks with scoring rubrics, applied at scale to roughly 500 real-world agent skills and 1,000 generated tasks across 19 agent–model configurations.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent-skill evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.17819>
- **Code:** <https://huggingface.co/datasets/tesslio/task-evals-for-skills>
- **Venue:** arXiv preprint, 2026

## Summary

The paper's premise is that agent skills — structured, reusable knowledge artifacts that augment LLM agents — have been adopted in industry faster than any reusable methodology for evaluating an individual skill. The framework is a five-stage pipeline: extract usage scenarios from the skill's content, engineer an environment that satisfies its execution dependencies, generate realistic tasks with custom rubrics, validate them for executability and rubric leakage, then run solver agents with and without the skill and grade against hidden rubrics. Applied at scale, it shows that models vary widely in how closely they adhere to the instructions encoded in a skill, and that skill access substantially changes model behaviour relative to a no-skill baseline.

## Tasks

Approximately 1,000 realistic executable tasks generated from approximately 500 unique real-world skills, each task carrying task-completion and instruction-following rubrics derived from the skill's content. Around 38,000 valid trajectories were collected. Every task is solved twice — once without skill access and once with explicit notification that the relevant skill is installed. A clustering analysis assigns skills to 15 content clusters, the largest being Web & UI Design (14.3%), Machine Learning & AI (13.6%), Testing/QA (10.2%), Finance & Crypto (9.9%) and Infrastructure & DevOps (8.3%); Scientific Computing accounts for 7.5%.

## Domains

The skill corpus is explicitly cross-domain but, by the authors' own account, biased toward software-engineering content because that is where most publicly released skills currently live. A Scientific Computing cluster covers 7.5% of skills, which is not enough for the evaluated tasks to be characterised as a science or engineering domain suite; no canonical domain is assigned.

## Evaluation

- Two rubric families per task: instruction-following (adherence to the preferences encoded in the skill) and goal completion (correctness of the produced output). Individual rubric items are scored 1–10 and normalised to 100 points per category, with an overall score as a weighted average.
- The headline quantity is the skill delta — the difference between the with-skill and without-skill scores for the same task and model.
- Grading is LLM-as-judge: Sonnet 4.6 in a Claude Code harness acts as the sole judge across all experiments, scoring against hidden rubrics with access to solver logs.
- **Reported.** Relative gains from skill access range from 5.5 to 22 points depending on the model; per-model and per-cluster values beyond this range are TODO(reference).

## Typical Duration

No step or token cap is reported. Per-scenario monetary cost is reported as an analysis dimension; exact figures are TODO(reference).

## Main Contribution

A reusable, author-facing methodology for evaluating a single skill — rather than a fixed benchmark — together with a released dataset of generated executable tasks and rubrics that makes cross-model skill evaluation reproducible.

## Key Design Ideas

- Tasks and rubrics are derived from the skill's own content, so the evaluation targets what that skill claims to do.
- Explicit environment-engineering stage that resolves execution dependencies, catalogued into a fixed set of categories.
- A validation agent checks executability, consistency, and the absence of rubric leakage into the task statement.
- Separating instruction-following from goal completion, which exposes models that succeed at the task while ignoring the skill's prescribed procedure.
- Paired with-skill / without-skill runs on identical tasks as the unit of measurement.

## Strengths

- Scale: roughly 500 skills, 1,000 tasks and 19 agent–model configurations, spanning proprietary and open-source models.
- The two-rubric split makes a specific and otherwise invisible failure mode measurable — following the letter of the task while ignoring the skill.
- The generated task-and-rubric dataset is publicly released.

## Limitations

- The with-skill condition discloses skill relevance to the agent; in real usage a skill may be installed but never selected.
- Evaluation depends on a single judge model (Sonnet 4.6), and the authors flag judge bias as a concern, particularly on aesthetic or stylistic criteria.
- The dataset is biased toward software-engineering domains.
- Skills requiring hard-to-reproduce environments (databases, MCP servers, multi-turn interaction, pre-populated state) are filtered out, excluding a non-trivial slice of real-world skills.
- Repository note: the framework itself carries no short name, so the card is filed under a truncated-title slug.

## Related Works

- [Skill-Use](./skill-use.md) — Also separates triggering/compliance facets of skill use, on a curated fixed suite rather than generated tasks.
- [SkillAudit](./skillaudit.md) — Also generates per-skill evaluations from the skill package, adding cost and safety dimensions.
- [SkillEvolBench](./skillevolbench.md) — Evaluates skill formation from experience rather than the value of an authored skill.
- [SkillSV](./skillsv.md) — Attributes a skill's measured lift to its internal units.
