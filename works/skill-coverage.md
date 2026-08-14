# Skill Coverage (2026)

> **English** | [简体中文](../zh/works/skill-coverage.md)

## Overview

Skill Coverage is a trajectory-based test-adequacy metric for reusable agent skills: it compiles a skill's natural-language instructions into semi-structured behavior constraints and checks, per constraint, whether an agent trajectory covered it and whether the observed behavior passed or failed.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — general-purpose agent-skill evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.20659>
- **Venue:** arXiv preprint, 2026

## Summary

Task outcomes do not reveal which parts of a reusable skill were exercised, nor whether the agent followed the relevant instructions when they were. Skill Coverage fills that gap by extracting skill behavior constraints — semi-structured statements of expected agent behavior under particular conditions — and evaluating agent trajectories against them, yielding a coverage figure plus Pass/Fail verdicts on the covered constraints. Applied to SkillsBench, it shows that leaderboard trajectories exercise well under half of a skill's constraints, and that the Fail verdicts are actionable enough to repair skills and recover previously failed tasks.

## Tasks

N/A — a metric and analysis framework rather than a task suite. It is applied to the existing SkillsBench benchmark and to the agent trajectories on that benchmark's leaderboard.

## Domains

Agent skills as structured artifacts for general-purpose LLM agents; the framework is not scoped to any science or engineering field, so no canonical domain is assigned.

## Evaluation

- **Constraint extraction.** Natural-language skill instructions are translated into semi-structured behavior constraints specifying expected agent behavior under particular conditions.
- **Coverage.** For each constraint, whether an agent trajectory covers it.
- **Verdict.** For covered constraints, a Pass or Fail judgement based on the observed agent behavior.
- **Reported.** Agent trajectories on the SkillsBench leaderboard cover only 38.66 to 45.51% of the extracted skill behavior constraints on average. Re-running the same tasks with skills strengthened only by emphasizing the original instructions the agent failed to follow yields an average 16.0% recovery rate of the failed tasks across the five agent-model rows.

## Typical Duration

N/A — post-hoc analysis over trajectories produced by an existing benchmark run.

## Main Contribution

Transfers the software-testing notion of test adequacy to agent skills: coverage over a skill's extracted behavior constraints serves both as a measure of whether a skill has been adequately tested and as a fine-grained diagnostic signal for skill-use behavior.

## Key Design Ideas

- Skill instructions are compiled into semi-structured, conditionally scoped constraints rather than checked as free text.
- Coverage and correctness are separated: a constraint may be uncovered, covered-and-passed, or covered-and-failed.
- The repair loop changes no skill content, only emphasis on instructions the agent already failed to follow — isolating the diagnostic value of the Fail labels from any added knowledge.

## Strengths

- Explains *why* a skill helped or did not, at the granularity of individual instructions.
- Diagnostic value is demonstrated by an intervention (task recovery), not asserted.
- Constraint-level Fail labels give a concrete edit target for skill authors.

## Limitations

- Constraint extraction from natural-language instructions is itself an automated step whose fidelity bounds the metric.
- Validated on a single host benchmark (SkillsBench) and its leaderboard trajectories.
- Repository note: card compiled from the arXiv abstract and metadata (August 2026); a project website is mentioned in the abstract but its URL is TODO(reference).

## Related Works

- [SkillSV](./skillsv.md) — Also decomposes a skill into internal units for per-unit assessment, via Shapley valuation rather than trajectory coverage.
- [Skill-Use](./skill-use.md) — Also scores procedural compliance with a skill, per task facet rather than per extracted constraint.
- [SkillJuror](./skilljuror.md) — Also reads trajectory evidence about skill uptake, comparing organizational layouts rather than measuring instruction coverage.
- [AgentBoard](./agentboard.md) — Also replaces a single success number with a process-level progress signal, over annotated subgoals rather than skill constraints.
