# SKILL-KD (2026)

> **English** | [简体中文](../zh/works/skill-kd.md)

> **First appeared:** 2026-07-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.28048)

## Overview

SKILL-KD is a method that improves a frozen, weaker student agent by writing textual skill patches from the difference between the student's failed run and a stronger teacher's run on the same task. Skills built from the student's own failures may not reveal what it lacks, and a teacher's successful run may be too implicit to copy. SKILL-KD extracts the actionable difference as a patch, reruns the student on that task, and commits the patch only if the rerun succeeds, revising it up to three times otherwise; a consolidation step then decides whether each accepted patch is added, merged into an existing rule, or skipped. The resulting skill file is tested on held-out splits of five benchmarks in two student–teacher settings.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities


N/A — Skill-distillation method evaluated on general-purpose agent tasks (search QA, spreadsheets, document VQA, ALFWorld) with one math benchmark as a test bed; no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.28048>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

For one training task, a consolidation agent receives the frozen student's failed trajectory, the teacher's trajectory, the current skill library, and an edit history, and proposes a patch with four fields (title, content, why, trace); only title and content are shown to the agents, while why and trace stay in an audit-only history. The patch is applied, the student reruns the task, and a task evaluator scores the trajectory in [0, 1]; a score of 1 commits the patch, and otherwise a revised patch replaces it, for up to n = 3 adaptive rounds. Patches that never lead to success are not written to the library or history. Drift-Aware Skill Consolidation then uses trace links to past edits to classify existing rules as cover, partial, or unrelated and commits add, modify, delete, or skip. The acceptance test is success on the same training task, so it does not by itself show that a patch generalizes.

## Tasks

N/A as a benchmark — SKILL-KD is a skill-distillation method. Benchmarks (train/validation/test):

- SearchQA 400/200/1400; SpreadsheetBench 80/40/280; DocVQA 107/53/374; LiveMath 35/18/124; ALFWorld 39/18/134. Benchmarks without official partitions use a 2:1:7 ratio.
- Group 1 (same model family): Qwen3.5-4B student, Qwen3.7-plus teacher.
- Group 2 (different families): Qwen3.6-35B-A3B student, ChatGPT-5.5 teacher.

Skills are built only from the training split; the validation split is used only by baselines that need it.

## Domains

General-purpose agent tasks (search QA, spreadsheet manipulation, document VQA, text-based embodied tasks) plus mathematics problem solving (LiveMath).

## Evaluation

- **Inside the loop.** Trace for one training task: student fails (score < 1) → patch proposed from student-vs-teacher difference → student reruns with the patch → evaluator score 1 → patch committed and passed to consolidation; score < 1 → revised patch, up to 3 rounds.
- **Held-out.** Each benchmark's native hard-success or exact-match score on the test split, from a single evaluation run.
- **Reported (average over five benchmarks).** Group 1: No Skill 43.5, best baseline SkillOpt 63.5, SKILL-KD 66.8. Group 2: No Skill 57.9, SkillOpt 68.6, SKILL-KD 74.6. Other baselines: EvoSkill, Trace2Skill, SkillGen. ALFWorld rises from 30.6 to 86.6 (Group 1) and 59.7 to 96.3 (Group 2).
- **Acquisition ablation (Group 1 average).** Student-only 60.1 (96 rules), teacher-only 58.3 (80 rules), batch 59.4 (46 rules), pairwise without adaptive rounds 59.0 (85 rules), SKILL-KD 66.8 (38 rules, 3,010 words).
- **Consolidation ablation (Group 1).** Without consolidation, SpreadsheetBench drops from 24.3 to 14.6 and LiveMath from 54.8 to 27.4.
- **Adaptive rounds (Group 1, training-set cumulative success).** n = 0: 58.9; n = 1: 67.7; n = 2: 70.8; n = 3: 72.7.

## Typical Duration

TODO(reference) — token and cost figures are not reported. Students run locally on four NVIDIA A100 80GB GPUs; teacher and consolidation models are accessed through APIs.

## Main Contribution

The authors propose using skills as an explicit medium for knowledge transfer from a stronger to a weaker agent: contrasting the two agents' trajectories on the same task, verifying each patch by rerunning the student, and consolidating patches with trace-linked histories to limit drift.

## Key Design Ideas

- Contrastive input: the student's failure and the teacher's trajectory on the same task.
- Rerun-and-commit gate: only patches that make the student succeed are stored.
- Audit fields (why, trace) are kept out of the agent prompt but used during consolidation.
- Drift-Aware Skill Consolidation prefers updating partially overlapping rules and adds a rule only for a new reusable trigger.
- The full skill file is loaded into the prompt rather than retrieved.

## Strengths

- Ablations separate student-only, teacher-only, batch, and pairwise acquisition, and the consolidation step, on the same benchmarks.
- Two student–teacher settings, same-family and cross-family.
- Produces a smaller skill file (38 rules) than the ablated variants while scoring higher.

## Limitations

- The acceptance test is success on the same training task; generalization is measured only on the held-out splits afterward.
- Teacher-failed rollouts still produced 38.5% of accepted patches on average, so the teacher trajectory is not always a correct reference.
- Single evaluation run per score; no variance reported.
- The full skill file is placed in the prompt, so prompt length grows with the library.
- Repository note: the paper has no dedicated limitations section; the points above come from reported results. Card compiled from the arXiv abstract and the v1 HTML full text (November 2026); the paper has been revised to v4 and numbers may differ in later versions.

## Related Works

- [SkillGen](./skillgen.md) — Also gates skills on rerun outcomes and appears as a baseline; it contrasts an agent's own successes and failures instead of a teacher's run.
- [MIND-Skill](./mind-skill.md) — Also verifies skills by having an agent re-execute the task using only the skill.
- [SkillMisevo-Bench](./skillmisevo-bench.md) — Studies how a persistent skill library can accumulate harmful procedures, a risk related to the drift SKILL-KD's consolidation targets.
- [SkillEvolBench](./skillevolbench.md) — Measures whether written skills survive on held-out, shifted tasks.
