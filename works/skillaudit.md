# SkillAudit (2026)

> **English** | [简体中文](../zh/works/skillaudit.md)

> **First appeared:** 2026-06-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.22613)

## Overview

SkillAudit is an end-to-end evaluation framework that takes an arbitrary agent skill package as input and automatically produces a multi-dimensional deployment report covering utility, efficiency/cost, and safety — replacing fixed task suites with tasks constructed from the skill artifact itself.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — evaluation methodology for general agent skills; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.22613>
- **Code:** <https://github.com/SkillAudit/skillaudit>
- **Project:** <https://skillaudit.github.io/>
- **Venue:** arXiv preprint, 2026

## Summary

The framework argues that fixed suites conflate a skill's marginal contribution with backbone model strength and miss the skill's value when tasks fall outside its intended scope. SkillAudit therefore generates capability-aligned tasks directly from the skill package, runs them in isolated sandboxes to collect execution evidence, and combines rule-based checks with LLM judging to produce auditable per-skill reports. Utility and efficiency rest on a baseline-comparison principle — matched with-skill and no-skill runs sharing identical instruction, inputs, environment, and criteria — while safety uses a two-stage paradigm of static semantic analysis followed by dynamic runtime verification.

## Tasks

Tasks are generated per skill rather than drawn from a suite. Each audited skill yields three representative scenarios, and each scenario compiles into a matched pair of utility tasks (with-skill and no-skill); each identified risk probe becomes one additional with-skill risk task. The reported run retains 643 valid scenarios in the Codex / GPT-5.4 configuration. The audited corpus is 226 top-ranked real-world skill packages collected from public skill repositories, spanning 23 occupational categories.

## Domains

General agent-skill packages spanning 23 occupational categories from public skill marketplaces. No canonical science or engineering domain is targeted; the evaluated object is the skill artifact, not a domain task.

## Evaluation

- **Utility:** pass-rate gain (PRG) between the matched with-skill and no-skill runs.
- **Efficiency/cost:** Efficiency Gain (relative saving in agent execution time) and Cost Gain (relative saving in effective input tokens), each clipped to [-1, 1] and combined into an Efficiency-Cost Gain (ECG).
- **Safety:** an aggregated score in [10, 100] from confidence-weighted penalties over static and dynamic findings, bucketed as Pass (100), Caution (80–99), Risky (<80).
- **Reported.** 17 of 226 skills (7.5%) are flagged Risky; the static scanner produces 83 high-severity, 59 medium-severity and 99 low-severity findings across the 226 skills in the Codex / GPT-5.4 configuration.
- Six agent–model configurations are used for utility and efficiency (Codex/GPT-5.4, Codex/GPT-5.1, Claude Code/Sonnet 4.6, Claude Code/Sonnet 4, OpenCode/GPT-5.4, OpenCode/Sonnet 4.6); safety is evaluated on three of them.

## Typical Duration

N/A — no per-task step or token cap is reported; execution time is measured as an outcome (Efficiency Gain) rather than imposed as a budget.

## Main Contribution

Reframing skill evaluation from "how does this task suite score?" to "is this specific skill worth deploying?", with an automated pipeline that turns a skill package into its own evaluation and reports utility, cost, and safety together.

## Key Design Ideas

- Tasks are synthesised from the skill's own documentation and bundle, so coverage follows the skill's declared scope rather than a fixed suite's.
- Matched with-skill / no-skill task pairs isolate the skill's marginal contribution from backbone strength.
- Docker-based isolated sandboxes collect execution evidence, which is then judged rather than trusted.
- Two-stage safety detection pairs static semantic analysis with dynamic runtime verification, so declared behaviour and observed behaviour are both checked.
- Delivery through a browser extension surfaces the audit at discovery time, when the adoption decision is actually made.

## Strengths

- Treats cost and safety as first-class reporting dimensions alongside utility rather than as post-hoc statistics.
- Applied at ecosystem scale to real published skills, producing a concrete prevalence figure for risky packages.
- Intermediate trajectories and evaluation artifacts are open-sourced, making individual audits inspectable.

## Limitations

- The authors note coverage of only 226 public skills and a small set of agent–model configurations.
- Single matched runs per condition, so run-to-run variance is not captured.
- Safety checks are limited to scanner- and probe-covered patterns and therefore cannot speak to uncovered risks.
- Repository note: the generated-task pipeline means two audits of different skills are not scored on comparable tasks, so per-skill utility numbers rank a skill against its own no-skill baseline rather than against other skills.

## Related Works

- [SkillSV](./skillsv.md) — Also asks what a skill is worth, by attributing value to its internal units rather than auditing it end to end.
- [Skill-Use](./skill-use.md) — Evaluates agents on a fixed suite of real skills, the paradigm SkillAudit argues against.
- [SkillEvolBench](./skillevolbench.md) — Concerns whether skills can be formed from experience; SkillAudit concerns whether an existing skill should be adopted.
- [HarnessOpt-Bench](./harnessopt-bench.md) — Also meters resource use inside a trusted execution environment while scoring an agent-surrounding artifact.
