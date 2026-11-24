# OSWorld-Pro (2026)

> **English** | [简体中文](../zh/works/osworld-pro.md)

> **First appeared:** 2026-09-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.24890)

## Overview

OSWorld scores a computer-use agent by checking the final machine state with a task-specific script, so a failed run says nothing about how far the agent got or which action went wrong. OSWorld-Pro splits each task into an ordered list of dependent subgoals and has an LLM judge label, step by step, which subgoal the agent is pursuing and whether it is completed. The task score then depends on reaching every feasible subgoal, and the step labels expose where and why progress stalled.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities


N/A — General desktop computer-use benchmark across Linux applications and distributions; no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2609.24890>

## Summary

Each of 305 tasks is decomposed into sequentially dependent subgoals (2,814 in total), first by DeepSeek-V4-Pro and then manually corrected by an annotation vendor, with each subgoal tagged to one application. After an agent runs, a GPT-5.6-Sol judge reads the full trajectory (screenshots with each pyautogui action overlaid, plus the agent's reasoning and action descriptions) and labels every step with its targeted subgoal, feasibility, progression, and completion. A task counts as solved when all subgoals that human annotators marked feasible are completed. The judge is validated against 67,264 human labels; it matches humans closely on target and completion labels but is weaker on feasibility and progression.

## Tasks

305 tasks in three categories: Diversity (117 tasks; under-represented applications such as Videos, Archive Manager, and LibreOffice Draw), Coordination (109 tasks; at least four applications per task), and Robustness (79 tasks; Linux distributions and desktop environments beyond Ubuntu, such as Fedora, Alpine, AlmaLinux, bspwm, Xfce, and LXQt). Tasks were generated with the ProCUA-SFT approach (Kimi-K2.6 for Robustness tasks). Tasks with unclear goals, safety concerns, or non-sequential subgoals were removed; tasks with infeasible subgoals were kept, following OSWorld. Subgoals average 9.2 per task (range 2 to 27).

Example (Diversity): install the Kid3 audio tagger from the KDE website, then add an album name and release year to an MP3 file. Subgoals: download Kid3 (Chrome), install it (Terminal), open the MP3 (Kid3), add the album name (Kid3), add the release year (Kid3).

## Domains

General desktop computer use across Linux applications (browser, terminal, office, media, file and archive tools) and multiple Linux distributions and window managers.

## Evaluation

- **Step labels.** For each step the judge assigns the targeted subgoal(s), whether the subgoal is feasible, whether the step makes progress, and whether the subgoal is completed. A subgoal is completed if at least one step labels it completed.
- **Task score.** Headline metric: percentage of tasks in which all human-marked feasible subgoals are completed. A secondary task-level measure is the percentage of subgoals completed. In the Kid3 example, an agent that installs Kid3 and sets the album name but never sets the year completes 4 of 5 subgoals and does not count as solving the task.
- **Judge validation (Macro-F1, judge vs. human).** Target 97.0, feasibility 61.9, progression 74.7, completion 94.3; subgoal-level 1−MAE 94.1, task-level 1−MAE 93.0. A second human reviewer scores 91.6 on feasibility and 94.1 on progression. Annotator-reviewer Cohen's κ: 0.987 (target), 0.847 (feasibility), 0.869 (progression), 0.940 (completion).
- **Efficiency.** Table 2 also reports steps, output tokens, and token cost per model.
- **Reported results.** 14 models are listed. The abstract cites Claude Opus 5 at 75.7% overall against 83.4% on OSWorld; Table 2 lists Claude Opus 4.8 Max at 77.7% overall. The strongest open-weight model listed, Qwen 3.8 Flash Next, scores 55.1%. Minimax M3 scores 75.2% on OSWorld and 28.9% on OSWorld-Pro.

## Typical Duration

Observed trajectories average 55.1 steps, with a maximum of 149. The paper does not state a step or time budget per task.

## Main Contribution

A process-based computer-use benchmark with over 300 tasks, over 2,800 subgoals, and more than 67,000 human annotations, scored by LLM judges at the subgoal level, together with process-level failure modes such as subgoal-irrelevant actions and click errors.

## Key Design Ideas

- Keep only tasks whose subgoals are sequentially dependent, so subgoal completion order measures how far the agent advanced.
- Tag each subgoal with a single application, so failures can be localized to an application in multi-application tasks.
- Retain infeasible subgoals and label feasibility, so the benchmark also measures whether an agent stops pursuing an impossible subgoal.
- Have one judge call read the entire trajectory, with actions drawn onto screenshots, instead of judging steps in isolation.

## Strengths

- Large human-annotation base (67,264 labels, more than 5,000 person-hours reported) with high inter-annotator κ on all four label types.
- Process labels support action-type diagnoses: for example, in the per-action-type breakdown, Claude models score at least 89.2% on keyboard and 84.1% on scroll actions while no other model reaches 80% on either, and steps per completed subgoal range from 4.9 (GPT-5.6-Sol) to 21.2 (Minimax M3).
- Robustness tasks move outside the Ubuntu setup that OSWorld uses.

## Limitations

- The judge is weaker on feasibility (61.9 Macro-F1) and progression (74.7) than on target and completion; the paper attributes this to label subjectivity and notes that higher reasoning effort can over-predict feasibility.
- Only GPT-5.6 models handled full-trajectory judge payloads; other judge models hit payload or context errors.
- Tasks with non-sequential subgoals were excluded by design.
- Repository note: The abstract (Claude Opus 5, 75.7%) and Table 2 (Claude Opus 4.8 Max, 77.7%) name different top performers.
- Repository note: No code or data release link appears on the arXiv page or in the paper text read for this card. TODO(reference)

## Related Works

- [OSWorld](./osworld.md) — The base environment whose final-state checking OSWorld-Pro replaces with subgoal-level judging.
- [OSWorld-Science](./osworld-science.md) — Also extends OSWorld, but to scientific software rather than to process-level scoring.
- [AgentBoard](./agentboard.md) — Also measures progress below task success through subgoals, with automatic progress rates rather than an LLM judge validated against human labels.
- [AgentProcessBench](./agentprocessbench.md) — Also labels individual agent steps, but for tool-use trajectories and to evaluate step verifiers.
