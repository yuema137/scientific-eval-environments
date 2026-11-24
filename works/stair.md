# STAIR: Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents (2026)

> **English** | [简体中文](../zh/works/stair.md)

> **First appeared:** 2026-07-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.29658)

## Overview

STAIR converts a coding agent's earlier issue-repair trajectories into multi-level plan trees and injects selected nodes into the agent's prompt when it repairs a new issue. Repository-level repair agents normally treat each issue from scratch, and experience-reuse methods pass along either raw trajectories or one level of summary. STAIR changes what is stored and retrieved: each past repair becomes a tree running from concrete diagnostic steps up to project-agnostic strategies and general principles, and nodes are selected across those levels. The paper tests the change on SWE-bench Verified with Pass@1, and its ablation compares raw trajectories, each single abstraction level, and the mixed hierarchy on the same instances.

## Topics


- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities


N/A — Experience-reuse method evaluated on general software bug repair (SWE-bench Verified); no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.29658>
- **Venue:** arXiv preprint, July 2026

## Summary

For a target issue, STAIR retrieves resolved issues from the same repository that were created before the target (ranked by embedding similarity and filtered by an LLM relevance verifier) and runs the Lingxi repair scaffold on them with its own knowledge reuse disabled. Each trajectory is split into localization, planning, and execution-and-verification stages; GPT-5 then repeatedly groups nodes and abstracts each group into a parent until at most two roots remain, giving low-level (artifact-specific sub-goals), medium-level (project-agnostic investigation strategies), and high-level (cross-project principles) views. Every node records repair intent, key actions, applicable conditions, and common pitfalls. At repair time, nodes are scored by textual similarity, filtered by an LLM verifier, ordered by their original execution sequence, and rewritten by an LLM into a per-stage plan that the repair agent receives in its prompt.

## Tasks

N/A — method paper; it introduces no new task suite. Experiments use SWE-bench Verified: 500 instances from 12 Python repositories. In total, 479 similar historical trajectories were retrieved and abstracted. The ablation uses a 125-instance subset (92 medium/hard, 33 easy).

## Domains

Software & Systems: repository-level bug repair in Python projects.

## Evaluation

One instance runs as follows: the issue report goes to the base agent together with STAIR's per-stage plans; the agent produces a patch; the patch is scored by the benchmark's provided tests, and Pass@1 counts the instance as resolved if those tests pass. The paper also reports average steps and tokens per instance.

Reported results:

- **Main (Lingxi + STAIR):** 81.2% Pass@1 with MiniMax M2.5 (High Reasoning) and 79.2% with GPT-5 (High Reasoning); Lingxi alone reaches 74.6% and 75.6% with the same backbones.
- **Transfer to mini-SWE-agent v2 (MiniMax M2.5), no code changes:** 379/500 (75.8%) without plans versus 405/500 (81.0%) with plans; average steps 60.45 → 58.18; tokens per instance 1,244,923 → 1,179,885.
- **Gain/regression analysis:** Lingxi + STAIR versus Lingxi (MiniMax) gains 43 and regresses 10 instances (net +33); mini-SWE-agent v2 with plans gains 33 and regresses 7 (net +26). Manual labelling of the changes reached Cohen's kappa 0.85. Of 17 regressions, 8 were plan-related (incomplete coverage) and 9 execution errors.
- **Abstraction-level ablation (125 instances, MiniMax M2.5):** full hierarchy 100/125 (80.0%); raw trajectories 72/125 (57.6%); low-level only 80/125 (64.0%); medium-level only 76/125 (60.8%); high-level only 73/125 (58.4%).

## Typical Duration

10–15 minutes per instance. Per-instance cost is $0.84 (MiniMax M2.5) and $1.60 (GPT-5); preprocessing costs about $0.44 per source trajectory, about $211 in total.

## Main Contribution

A hierarchical abstraction of past repair trajectories into reusable plans, with evidence that mixing abstraction levels resolves more issues than any single level or raw trajectories, and that the plans transfer to a structurally different agent.

## Key Design Ideas

- Segment each trajectory by repair stage (localization, planning, execution-and-verification) before abstraction.
- Build the hierarchy bottom-up with an LLM grouping operator and an abstraction operator, repeated until at most two roots remain.
- Use one node schema at every level: repair intent, key actions, applicable conditions, common pitfalls.
- Select nodes across levels rather than committing to one granularity, then adapt them into an issue-specific plan.
- Restrict historical issues to those created before the target issue to prevent temporal leakage.
- Inject plans through the prompt only, so a different agent can consume them without code changes.

## Strengths

- The ablation directly compares the same pipeline at each abstraction level and at none (paper).
- Transfer to mini-SWE-agent v2 tests whether plans depend on the agent that produced them (paper).
- Reports both gained and regressed instances with manually labelled causes, not only net Pass@1 (paper).
- Reports monetary and preprocessing cost (paper).

## Limitations

- The authors note that abstraction quality depends on LLM generation and input length, and that the LLM plan-compatibility filter may discard useful plans or keep inapplicable ones.
- Only SWE-bench Verified (Python) and two LLMs were tested; plan quality may depend on the base agent that produced the trajectories (paper).
- Pass@1 relies on the provided tests, so behaviorally incorrect patches can pass (paper).
- The acronym STAIR is not expanded in the paper, and no code or replication URL is given.
- Repository note: the ablation runs on a 125-instance subset and reports no cost figures per variant.

## Related Works

- [SWE-bench](./swe-bench.md) — source of the SWE-bench Verified instances used for evaluation.
- [Trace2Tower](./trace2tower.md) — also abstracts past trajectories into multi-level skills and compares levels, in household and web-shopping environments.
- [Agent Workflow Memory](./agent-workflow-memory.md) — induces reusable sub-routines from past web-agent trajectories, at one main granularity.
