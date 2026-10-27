# PhysRSI-eval (2026)

> **English** | [简体中文](../zh/works/physrsi-eval.md)

> **First appeared:** 2026-10-19 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.26848)

## Overview

PhysRSI-eval measures physical recursive self-improvement: whether an LLM agent controlling a simulated dual-arm robot gets better at a manipulation task by revising its own code, tools, skills, and notes after failed attempts. Each of 18 RoboDojo tasks gets a first attempt and up to 17 refinement rounds, each round a full physical attempt. Five axes score the run: first-attempt performance, efficiency of the gain, success, budget, and improvement from failure. The paper then relates each axis to public benchmark scores and tests, by ablation, which parts of the persistent workspace carry the improvement.

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — general-purpose robot-manipulation benchmark; the evaluated agents perform dual-arm manipulation, not a scientific or research activity.

## Links

- **Paper:** [Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](https://arxiv.org/abs/2610.26848), 2026 technical report (Galbot Team).
- **Full text:** <https://arxiv.org/html/2610.26848v1>
- **Code:** <https://github.com/PhysRSI-Eval/PhysRSI-Eval-code> (Apache-2.0 reference implementation of the evaluation loop with a Codex client; the README states it covers four of the 18 tasks, from the generalization study)
- **Project:** <https://physrsi-eval.github.io/>
- **Venue:** arXiv preprint (cs.RO), 2026

## Summary

Round K0 is an in-context attempt with shared robot tools and no workspace, run three times per task. From K1 to K17 the agent makes one physical attempt per round from a persistent workspace of policy code, tools, skills, and notes. After each round it receives the native score, a success flag, and the failure reason, then revises the workspace with robot actions disabled. A chain stops at the first native success. Robot actions are target-pose calls of at most 5 cm translation and 0.35 rad rotation, each executed for 1–5 control steps and returning a state JSON and three camera images. GPT systems run in Codex CLI and Claude systems in Claude Code.

## Tasks

18 dual-arm manipulation tasks from RoboDojo, three from each of six difficulty strata (D1–D6) ranked by official success rate, covering RoboDojo's five categories (Precision, Long-Horizon, Memory, Open, Generalization). Examples include `insert_key`, `pour_liquid_into_cup`, `push_T`, `play_Xylophone`, and `organize_table`. Rounds run 300–1300 steps at 25 Hz. The main evaluation uses layout 0, seed 0, and one improvement chain per task. The paper does not state how many tasks RoboDojo contains in total.

## Domains

Robotics: dual-arm manipulation in RoboDojo simulation, controlled through agent-written policy code that issues end-effector target poses. No physical-robot experiments are reported.

## Evaluation

- **Axes:** A1 First-Attempt Performance is the mean K0 score. A2 Efficiency is the mean gain over rounds 1 to H−1 relative to the terminal gain. A3 Success is the mean partial-credit score from the round that first reaches 90% of the gain onward. A4 Budget is the mean unused share of the physical budget on solved tasks; time, tokens, and money are excluded. A5 Improvement is the fraction of tasks failed at K1 that are solved later. The aggregate is 100 times the equal-weight mean of A1–A5.
- **Grading:** each task's native RoboDojo grader gives a score in [0, 1] and a success criterion with tiered partial scores. The paper describes no LLM or VLM judge.
- **Systems:** GPT-6 Astra, GPT-6.1 Sol, GPT-6 Sol, GPT-5.6 Sol, Claude Opus 5.5, and Claude Sonnet 5.5 on all 18 tasks; Gemini 4 on 10 tasks with one K0 run per task, excluded from the association analyses.
- **Results (Table 1, A1–A5):** GPT-6 Astra 0.3676 / 0.8594 / 0.8509 / 0.8429 / 0.7500, solving 15 tasks by K17; GPT-5.6 Sol 0.0120 / 0.2247 / 0.1037 / 0.3013 / 0.0556, solving 1. The text gives the aggregate range across the four GPT systems as 13.9–73.4. Claude Opus 5.5 solves 13 tasks and Claude Sonnet 5.5 11. No system solves `insert_key`, `store_tools_in_toolbox`, or `swap_blocks`.
- **Association with public benchmarks:** 17 public benchmark scores are converted to ranks and grouped into Spatial, Harness, Perception, and Coding. Over six systems, Spatial correlates with A1 at Spearman ρ = 0.94 and Perception with A3 and A5 at ρ = 0.94; Coding has ρ ≤ 0.37 on every axis. After Benjamini–Hochberg adjustment the smallest q is 0.11, and the paper treats the associations as candidate bottlenecks (the "Physical Barrel Hypothesis"), not causal requirements.
- **Workspace ablation (GPT-6 Astra, six tasks, two chains each):** late-round (K4–K6) success is 15/36 with the full loop, 3/36 without history, 5/36 without grader feedback, and 12/36 without earlier images.
- **Transfer:** frozen K6 workspaces solve 25/60 attempts on unseen layouts with no revision or feedback. In three first-run cases, a workspace from another task moves the first success earlier (for example Cover Blocks, Sonnet 5.5, from K9 to K1).

## Typical Duration

Up to 4,200 s of reasoning per round and a revision window of 1,800 s (GPT systems) or 600 s (Claude systems), for at most 17 refinement rounds per task. Token counts, dollar costs, and total wall-clock time are not reported.

## Main Contribution

Defines a five-axis profile of physical self-improvement under a fixed interaction budget, separating a good first attempt from the ability to improve after failure. Ablations of the persistent workspace show which retained information drives late-round success.

## Key Design Ideas

- Count every refinement round as a full physical attempt with native grading, so improvement is measured in executed behavior rather than in revised code.
- Keep the first attempt, the speed of the gain, and the recovery of initially failed tasks as separate axes, because a system can rank differently on each.
- Freeze workspaces and move them to unseen layouts or other tasks to test whether what was learned transfers.

## Strengths

- The ablation removes history, grader feedback, and earlier images separately, and success drops from 15/36 to 3/36 when history is removed.
- Transfer is tested on unseen layouts with frozen workspaces, apart from in-task improvement.
- The authors report the small-sample limits of the association analysis, including that no correlation survives multiple-comparison adjustment.

## Limitations

- The authors list six systems, one improvement chain per task, and no independent validation of the capability scores. K0 repeats do not estimate variability across full chains.
- The authors note that Budget and Improvement are computed on conditional task sets that differ across systems.
- The ablation and frozen-workspace tests cover only GPT-6 Astra and six tasks, and cross-task transfer rests on three cases.
- GPT-6 Astra solves 15 tasks in the main run and 13 in a run without "supplementary hints"; the paper does not describe the hints.
- The paper reports Gemini 4 as run "through K20" while the main protocol sets H = 17, and does not state which round its profile uses.
- Repository note: the project page labels A4 "Stability" and lists A4 and A5 values that differ from Table 1 of the paper (for example 0.8405 and 0.7349 for GPT-6 Astra, against 0.8429 and 0.7500); this card follows the paper.

## Related Works

- [RobotAgentBench](./robotagentbench.md) — Also tests recursive self-improvement of coding agents in robot control, as one configuration in a household benchmark.
- [EmbodiedCLBench](./embodiedclbench.md) — Also measures learning from earlier attempts in embodied tasks, through in-context trajectories or written skill summaries.
- [CaP-X](./cap-x.md) — Coding agents writing robot-control programs, compared across abstraction tiers rather than across refinement rounds.
