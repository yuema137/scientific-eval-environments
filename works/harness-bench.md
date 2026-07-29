# Harness-Bench (2026)

## Overview

Harness-Bench is a diagnostic benchmark for measuring configuration-level *harness effects* — how the system layer surrounding a model (context management, tools, state, permissions, tracing, recovery) changes agent performance. It fixes external task conditions while varying the harness around each model backend, scoring 5,194 execution trajectories over 106 sandboxed offline tasks.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.27922>
- **Project:** <http://www.harness-bench.ai/>
- **Code:** <https://github.com/Qihoo360/harness-bench>

## Summary

Harness-Bench argues that existing benchmarks either abstract away execution, compare complete agent systems, or hold the harness fixed, leaving the execution layer unmeasured. Framing an agent as Model + Harness, it evaluates a factorial matrix of 6 configurable harnesses (OpenClaw, NanoBot, Hermes, ZeroClaw, NullClaw, Moltis) × 8 API model backends over a shared task suite, budget, timeout, and evaluator, while preserving each harness's native prompting, tool interface, state management, and recovery behavior (5,088 trajectories, plus 106 from Codex reported separately as a model-bound coding agent). Each run records final artifacts, a reconstructed execution trace, usage statistics, and validator outputs, and results are interpreted as configuration-level diagnostics of model–harness pairings rather than causal decompositions of individual harness mechanisms.

## Tasks

106 sandboxed, offline, end-to-end agent tasks constructed from practical agent-use patterns across 8 workflow categories: Software Engineering & Codebase Maintenance (22), Workspace, Tool Use & Multimodal Operations (15), Data, BI & Finance Analytics (14), Knowledge, Evidence & Retrieval (13), Office & Business Communication (12), Vertical Professional Workflows (12), Long-running Autonomy & State Adaptation (11), and SRE, DevOps & Release Ops (7). Every candidate task is manually reviewed and retained only if it satisfies four criteria: realism, solvability, oracle-checkability, and integrity (agents cannot gain credit by reading hidden answers, modifying protected fixtures, or bypassing constraints).

## Domains

General-purpose executable agent workflows: software engineering, data analysis, workspace and tool operations, evidence-grounded knowledge work, office communication, professional verticals, long-running state adaptation, and DevOps.

## Evaluation

- Per task, TaskScore = Security · Completion · Process, with Security ∈ {0, 1} zeroed by explicit permission or security violations, Completion measured by task-specific deterministic validators where possible (rubric-based judgment otherwise), and Process = (Robustness + ToolUse + Consistency) / 3 assessed from the reconstructed execution trace via LLM-based process rubrics (claude-sonnet-4.6 as a fixed external judge across all trajectories).
- The multiplicative aggregate is intentionally conservative — high credit requires completion, no security violation, and reliable execution — and completion, security, robustness, tool use, consistency, token usage, and turns are also reported separately.
- Reference artifacts, hidden answers, and evaluator scripts are never exposed to the agent; each run starts from a fresh sandbox with fixed initial state, budget, and timeout.
- Reported results: among configurable harnesses, NanoBot scores highest (76.2 aggregate) and OpenClaw lowest (52.4) — a 23.8-point gap on the same tasks and model-backend pool; Codex reaches 80.4 as a model-bound reference. NanoBot achieves its top score while using fewer tokens (68.7K average) than several lower-scoring harnesses. Stronger model backends show lower cross-harness variance. Among failed trajectories, recurring symptoms are contract/format violations (36.4%), tool/recovery failures (24.6%), evidence/grounding gaps (14.6%), artifact-commitment failures (11.1%), and state/continuation failures (9.3%).

## Typical Duration

Multi-turn sandboxed workflows; average turns per harness range from 5.0 (OpenClaw, Codex) to 22.6 (Hermes), with average token usage from 68.7K to 175.1K per task across harnesses.

## Main Contribution

Making the harness a primary axis of evaluation: a shared-protocol benchmark in which external task conditions are fixed and the execution layer varies, producing evidence that agent capability should be reported at the model–harness configuration level rather than attributed to the base model alone.

## Key Design Ideas

- Agent = Model + Harness: complete harness configurations are evaluated as they natively execute, not forced into a common internal runtime.
- Factorial model × harness matrix under identical tasks, sandboxes, budgets, timeouts, and evaluators.
- Four evidence streams per run — final workspace state, execution trace, usage statistics, validator outputs — supporting process diagnostics, permission checks, cost analysis, and failure analysis beyond completion scores.
- Security as a binary gate multiplying the score, so permission violations zero out otherwise-successful runs.
- Failure analysis framed as *execution drift* / *execution alignment*: identifying where plausible model reasoning decouples from tool feedback, workspace state, evidence, or verifiable output contracts.

## Strengths

- Isolates an evaluation dimension — the execution layer — that prior benchmarks conflate with the model or the full agent system.
- Conservative multiplicative scoring plus separately reported per-dimension metrics preserve diagnostic signal.
- Sandboxed offline tasks with integrity review reduce benchmark drift and make runs reproducible and independently scorable.
- Fully released code and data.

## Limitations

The paper's own limitations note that the benchmark covers controlled, sandboxed offline workflows — trading away live services, user feedback, changing external state, and long-term production memory; that observed differences are configuration-level effects, not causal attributions to individual harness mechanisms; and that some process-level scores rely on rubric-based or LLM-assisted assessment, so scores are diagnostic measurements under a fixed protocol rather than guarantees of deployment performance or safety.

## Related Works

- [AgentLens](./agentlens.md) — Also combines LLM-judged process dimensions with objective checks into a single trajectory quality score; AgentLens reviews individual coding runs, while Harness-Bench compares execution stacks.
- [AgentBench](./agentbench.md) — Compares model backends under a fixed execution setup; Harness-Bench inverts the design by fixing external task conditions and varying the harness.
