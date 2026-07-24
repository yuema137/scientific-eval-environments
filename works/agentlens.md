# AgentLens (2026)

## Overview

AgentLens is a production-assessed benchmark for interactive code agents that evaluates whole interaction trajectories rather than final pass/fail outcomes, pairing formal verification with LLM-written trajectory reviews and side-by-side comparisons. It releases an initial fold of 16 Java coding scenarios, each run under a relaxed default user and a mildly adversarial toxic user for 32 trajectories per evaluated agent.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.06624>
- **Code:** <https://github.com/agent-lens/agent-lens-bench>

## Summary

AgentLens argues that most code-agent benchmarks reduce a run to a single pass/fail bit, whereas the people who use these agents experience the entire trajectory — how the agent follows instructions, uses tools, verifies its own work, recovers from mistakes, and communicates. It evaluates the whole trajectory, pairing formal verification where an objective check exists with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. The authors use it not only to rank models but to diagnose model behavior, compare successive versions of their own agent, and catch product regressions in a nightly evaluation pipeline.

## Tasks

An initial fold of 16 coding-agent scenarios, each run under a relaxed default persona and a mildly adversarial toxic persona for 32 trajectories per evaluated agent. Scenarios come from two sources: workflows elicited in developer interviews about recently performed work, and production-derived scenarios constructed from anonymized usage summaries that were clustered in the spirit of Clio and matched to open-source projects. Representative task families include unit testing and test refactoring, legacy database-logic migration, and API documentation and DTO cleanup.

## Domains

Java coding-assistant work over real open-source repositories: unit testing, database-logic migration, and API documentation in Spring Boot projects.

## Evaluation

- **Formal verification.** Objective checks — tests, regular-expression matches, repository-state assertions, build-task execution, and static-analysis validators (Table 1) — applied wherever they exist; a scenario passes only if every one of its verifiers passes, and the run also records the fraction of individual verifiers that passed.
- **Trajectory review along five dimensions.** LLM judges score each trajectory on EndResult, InstructionCompliance, Pitfalls, Pleasantness, and ToolCalls, each on a small ordinal scale, and write a short review that cites numbered evidence pointers back into the trajectory.
- **Quality Index (QI).** A single aggregate index is the unweighted mean of the five judge metrics together with formal verification, each mapped to [0, 100].
- **Side-by-side reviews.** A pairwise judge compares two trajectories for the same scenario along one dimension, emitting a winner (A1 / A2 / Tie), a relative severity, and short evidence.
- **Deterministic telemetry.** Hard per-run statistics — interaction cost, cache hit rate, latency, termination reason, generation-token throughput, and per-tool success rates — collected independently of any judgment.
- **Reported (Table 6).** Across 17 agent configurations spanning two harnesses (Explyt AI Agent and Claude Code), Explyt AI Agent with Opus 4.7 leads at QI 81.5, ahead of Claude Code with Opus 4.7 at 76.2, GPT-5.5 at 73.0, and Sonnet 4.6 at 70.2, down to Kimi K2.6 at 28.1 (flagged for provider-side tool-parser instability); single-run reviews use GPT-5.4 as the judge, and no human performance baseline is reported.

## Typical Duration

The paper states no per-task step or token cap. Termination telemetry in the example run reports shows agent responses timing out after 900 seconds and whole scenarios after 1,200 seconds, and the paper notes that a single full run with Opus 4.7 can exceed $100.

## Main Contribution

A production-assessed benchmark for interactive code agents that evaluates complete interaction trajectories through a protocol combining formal verification with LLM judge reviews, and supports side-by-side model comparison, feature evaluation, and nightly regression detection for a deployed coding assistant.

## Key Design Ideas

- Whole interaction trajectories as the evaluation unit — user messages, agent replies, tool calls, file edits, command executions, verification attempts, and final repository state.
- Formal verification paired with LLM-written trajectory reviews, so an objective check (where one exists) comes with a readable, evidence-linked explanation of the score.
- LLM-simulated users instantiated as distinct personas — a relaxed default and a mildly adversarial toxic user — to probe robustness under cooperative and under sparse, adversarial feedback.
- A production CI pipeline that runs the fold on a schedule, compares each candidate against an anchor run, and flags statistically significant changes as potential regressions.

## Strengths

- Trajectory-level scoring surfaces failure modes a single pass/fail bit hides — misleading validation, unsafe tool use, unpleasant interaction — and attaches evidence pointers to each.
- Pairing formal verification with LLM reviews blunts reward hacking, since an agent can satisfy a green check while the review still records brittle shortcuts or skipped validation.
- Written reviews and side-by-side comparisons make the benchmark useful beyond ranking, for diagnosis, feature comparison, and regression detection on a deployed agent.

## Limitations

- Repository note: The released fold is Java-only and covers a specific class of coding-assistant tasks — 16 scenarios and 32 persona-paired trajectories — so scores characterize interactive coding behavior rather than general model capability.
- Repository note: The benchmark was originally built around the authors' own coding assistant (Explyt AI Agent), which tops the leaderboard, and the LLM-judge protocol's validity rests on internal pairwise-annotation experience rather than a published human-agreement study.

## Related Works

- [TRACE](./trace.md) — Also scores whole trajectories through a multi-dimensional utility, but for deep-research agents via a hierarchical, correctness-gated function rather than for interactive coding assistants via an unweighted quality index over LLM-judge dimensions and formal verification.
- [FinTrace](./fintrace.md) — Also a holistic trajectory-level evaluation aggregating several quality dimensions, but on long-horizon financial tool use scored as nine metrics across four dimensions rather than on interactive coding scored by five LLM-judge dimensions paired with formal verification.