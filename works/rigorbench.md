# RigorBench (2026)

> **English** | [简体中文](../zh/works/rigorbench.md)

## Overview

RigorBench is a benchmark that scores autonomous AI coding agents on **engineering process discipline** — how a solution was reached — rather than on outcome correctness alone. It decomposes process discipline into seven separately scored pillars, computes them from the full execution trajectory, and aggregates them into a composite RigorScore.

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose coding-agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.22678> (v2, 29 June 2026 — this card describes v2, whose task count and pillar count differ from v1)
- **Code:** <https://github.com/MeherBhaskar/RigorBench>
- **Venue:** arXiv preprint (cs.SE), 2026

## Summary

The paper surveys nine existing AI coding benchmarks (HumanEval, MBPP, SWE-bench, BigCodeBench, DevBench, Terminal-Bench, ProjDevBench, AgentBench, LiveCodeBench) and reports that none measure planning quality, verification behaviour, recovery strategy, abstention appropriateness, or codebase health — a gap the authors call the *lab-to-production gap*. RigorBench addresses it with three design decisions: a seven-pillar scoring framework, a task suite whose five categories each stress specific pillars, and a trajectory-based scoring pipeline that parses states (codebase snapshots) and actions (agent operations) rather than only the final artifact. The evaluation holds the foundation model fixed and varies the agentic harness, so that what is measured is the harness's contribution to process quality. The authors present the work explicitly as an *exploratory* study validating the scoring methodology rather than a settled benchmark.

## Tasks

100 tasks, 20 in each of five categories: **Plan-Then-Build** (multi-file feature requests; primary pillars PF, ATI; medium–hard), **Verify-Or-Die** (subtle bugs behind obvious-looking solutions; VC, RE; medium), **Doom Loop Gauntlet** (first attempts designed to fail; RE; hard), **Know When to Fold** (impossible or intentionally ambiguous tasks; AQ; variable difficulty), and **Don't Break the Build** (multi-step refactors with checkpoints; ATI, PF; hard). Tasks were authored to three principles — *discriminative* (different discipline levels produce different process traces), *measurable* (the trajectory carries enough signal for automated scoring), and *realistic* (reflecting professional software-engineering patterns). Each task ships a starter repository; the appendix examples span an empty Node.js/Express skeleton, a Python date library with 12 passing and 8 hidden edge-case tests, a Rust hash-verification module with 3/10 nondeterministically failing tests, a provably impossible sorting-algorithm specification, and a Django project with 8 models, 15 views and 47 passing tests. Full task specifications, starter repositories, and scoring rubrics are stated to be in the benchmark release.

## Domains

Software & systems engineering: feature implementation, bug diagnosis and repair, multi-step refactoring, and test authoring over starter repositories in Node.js, Python, Rust, and Django. No science domain is evaluated.

## Evaluation

- **Seven pillars, each normalized to [0, 1].** Planning Fidelity (PF, weight 0.15) = 0.30 × plan-artifact creation + 0.35 × decomposition quality (4-point rubric) + 0.35 × plan–execution alignment (Kendall τ between planned and executed steps). Verification Coverage (VC, 0.15) = 0.35 × test-creation rate + 0.30 × coverage delta + 0.35 × requirements traceability (recall over requirements). Recovery Efficiency (RE, 0.20) = 0.30 × f(recovery-attempt count) + 0.35 × strategy diversity + 0.35 × (1 − token-waste ratio), with f(RAC) = 1/(1 + λ·RAC), λ = 0.2. Abstention Quality (AQ, 0.10), scored only on impossible/ambiguous tasks, covers correct abstention, false confidence, and clarification seeking. Atomic Transition Integrity (ATI, 0.10) = 0.40 × build health + 0.40 × test-suite stability + 0.20 × commit hygiene. Test Assertion Density (TAD, 0.20) = min(1.0, meaningful_asserts / max(1, test_functions) / 5.0). Exploration Efficiency (EE, 0.10) = files_modified / (files_read + files_modified).
- **Composite.** RigorScore = 0.15 × PF + 0.15 × VC + 0.20 × RE + 0.10 × AQ + 0.10 × ATI + 0.20 × TAD + 0.10 × EE. Weights come from a pilot survey of ten staff-level software engineers and are flagged as preliminary; a ±50% sensitivity analysis left the rank order of the evaluated harnesses invariant.
- **Trajectory pipeline.** Execution is instrumented to capture agent-generated text, file diffs, command executions and outputs, per-action token consumption, and timestamps; scoring proceeds in three stages — trajectory parsing, automated signal extraction (planning artifacts, test events, recovery cycles, abstention signals, health checkpoints), and pillar scoring against published rubrics.
- **Anti-gaming validation.** Plan-artifact credit requires a dedicated planning document of at least 50 non-whitespace characters containing task-relevant terms; test-creation linkage requires tests in standard locations that import and invoke the modified modules; build health and test stability are checked by running build and test commands in the isolated Docker environment after each file modification.
- **Judging.** Qualitative sub-metrics (e.g. decomposition quality, commit hygiene) use Gemini 3.1 Pro (`gemini-3.1-pro-preview`, thinking_level "high") as LLM judge; objective metrics are verified programmatically.
- **Outcome score, measured separately.** Task-specific correctness criteria (test pass rate, feature completeness, absence of regressions) are scored independently of process, enabling a process–outcome correlation analysis.
- **Reported results (Table III, mean ± SD over 100 tasks).** Agent-Rigor 0.53 ± 0.08 RigorScore / 0.83 ± 0.05 outcome; Superpowers 0.41 ± 0.09 / 0.70 ± 0.06; Agent-Skills 0.39 ± 0.09 / 0.72 ± 0.06; Baseline ReAct 0.40 ± 0.09 / 0.64 ± 0.05. All four systems run on the same foundation model, Gemini 3.5 Flash (thinking_level "medium"). The unrounded nine-metric table reports RigorScore 0.527 (Agent-Rigor), 0.410 (Superpowers), 0.395 (Baseline), 0.387 (Agent-Skills) over ≈410 runs.
- **Process–outcome relationship.** The linear fit is Outcome = 0.26 + 1.07 × RigorScore, but within-harness task-level correlation is non-significant (r = 0.12 for Agent-Rigor, r = 0.05 for Baseline), which the authors read as process discipline being a macro-level capability differentiator rather than a task-level predictor.

## Typical Duration

Each execution runs in an isolated Docker container with a fresh clone of the task repository, a 60-minute wall-clock timeout, and a 200K-token context budget. Mean total token consumption per task fell from approximately 42,500 tokens under the baseline to 37,400 under the upfront-planning-enforced condition, a 12% reduction. The full study comprises approximately 410 task executions across four systems.

## Main Contribution

The authors present RigorBench as the first benchmark designed to measure engineering process discipline in AI coding agents, contributing: a formalization of the process-discipline gap backed by a survey of nine existing benchmarks; a seven-pillar decomposition of process discipline with a composite RigorScore; trajectory-based scoring that analyzes the full execution path rather than the final artifact; exploratory evidence that an upfront-planning-enforced harness raises process quality 33% over a ReAct baseline and is associated with a 30% rise in outcome quality; and an open release of tasks, scoring rubrics, and trajectory analysis tools.

## Key Design Ideas

- Separate the *process* score from the *outcome* score and measure both on the same runs, making their correlation an object of study rather than an assumption.
- Hold the foundation model fixed across all evaluated systems so that differences are attributable to the harness rather than the model.
- Design task categories to target specific pillars — impossible and ambiguous tasks exist only so that abstention can be measured at all.
- Prefer programmatic signal extraction (build runs, test runs, file diffs, token accounting) over LLM judging wherever the metric admits it, restricting the judge to genuinely qualitative sub-metrics.
- Encode anti-gaming thresholds directly in the scorers (minimum plan length, test-to-module linkage) so that shallow compliance does not earn credit.
- Argue that trajectory evaluation is inherently harder to contaminate than outcome evaluation, and design tasks with multiple valid solution paths.

## Strengths

- Measures a dimension that outcome-only benchmarks structurally cannot see, with an explicit survey establishing that the gap exists across nine prior benchmarks.
- Every pillar is given an explicit sub-metric formula and weight, so the composite is reproducible rather than a rubric summary.
- Controlled comparison design: identical base model, identical container, identical timeout and token budget across all four systems.
- Weight sensitivity is tested (±50%) and reported, and the rank order is shown to be robust to the choice.
- The authors state the conflict of interest prominently and describe pre-registration-style safeguards: the 100 tasks and their deterministic evaluation rules were finalized before Agent-Rigor was executed, and competitor systems ran in their default public configurations.
- Negative and inconvenient findings are reported, including that the best-scoring harness is *worst* on Test Assertion Density (0.311 vs. 0.349 baseline) and that structured tool frameworks alone (Agent-Skills 0.387, Superpowers 0.410) barely move the baseline (0.395).

## Limitations

- 100 tasks (20 per category) is small relative to coding benchmarks with thousands of instances; the authors present the work as exploratory and plan to expand before claiming definitive benchmark status.
- **Construct bias and circularity.** Both co-authors are co-developers of Agent-Rigor, the highest-scoring harness, and one owns its public repository. The authors acknowledge that Agent-Rigor's Planning Fidelity advantage is "partly by construction" because the pillars measure behaviours it was architecturally designed to enforce, and call for independent replication.
- **LLM-as-judge circularity.** Qualitative sub-metrics rely on a single LLM judge with documented length and self-preference biases; no human validation of judge alignment was performed.
- **Compressed variance in two pillars.** Abstention Quality clusters at 0.56–0.57 across all harnesses because the 80 non-abstention tasks receive a default neutral 0.50; Recovery Efficiency is compressed because recovery in many tasks is effectively binary (immediate recovery or a loop that ends at timeout).
- Process–outcome correlation is significant only across harnesses, not across tasks within a harness, so the benchmark does not show that better process on a given task raises that task's success probability.
- Only one discipline framework (Agent-Rigor) is used as the disciplined condition, so results may not generalize to other frameworks such as AGENTS.md configurations or Cursor Rules.
- Abstention tasks include textbook-impossible problems (e.g. the Halting Problem) that the authors note are easily pattern-matched from pretraining, weakening them as tests of genuine epistemic humility.
- *Repository note:* the paper is dated June 2026 but twice states that results and agent configurations reflect the state of agents "as of June 2025"; the discrepancy is unexplained in the text.
- *Repository note:* the arXiv v1 abstract describes a 30-task suite and five pillars, while v2 describes 100 tasks and seven pillars. Any figures cited from this work should be version-qualified.

## Related Works

- [Harness-Bench](./harness-bench.md) — also isolates the harness layer by holding the task conditions fixed and varying the surrounding system.
- [Plan Compliance in Programming Agents](./from-plan-to-action.md) — measures whether coding agents follow a given plan, the closest existing analogue of the Planning Fidelity pillar.
- [AgentProcessBench](./agentprocessbench.md) — step-level process evaluation of agent trajectories, scored against human labels rather than pillar rubrics.
- [SWE-bench](./swe-bench.md) — the outcome-only coding benchmark RigorBench positions itself against.
