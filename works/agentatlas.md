# AgentAtlas (2026)

> **English** | [简体中文](../zh/works/agentatlas.md)

> **First appeared:** 2026-05-19 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.20530)

## Overview

AgentAtlas is a diagnostic vocabulary and audit protocol for LLM agents, applied on top of 15 existing agent benchmarks. It reframes evaluation from outcome-only leaderboards toward per-control-decision quality and per-trajectory quality, with a six-way control-decision taxonomy and a failure taxonomy.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/html/2605.20530v1>

## Summary

AgentAtlas is not a stand-alone task suite. It is a diagnostic framework: a classification of control-decision types, a failure taxonomy, and an audit protocol that can be layered on top of existing agent benchmarks. The paper applies the framework across 15 agent benchmarks and demonstrates measurement challenges through evaluation of 1,342 synthetic items across 8 models.

## Tasks

1,342 synthetic items evaluated across 8 models. Underlying task substrate: 15 existing agent benchmarks that the audit protocol is applied on top of.

## Domains

Agent behavior across the environments covered by the 15 audited benchmarks — codebases, browsers, operating systems, calendars, files, and tool ecosystems.

## Evaluation

- Six-way control-decision type classification.
- Failure taxonomy.
- Audit framework layered on top of underlying benchmarks.
- Evaluated on 1,342 synthetic items across 8 models.

## Typical Duration

Depends on the underlying benchmark being audited; AgentAtlas itself does not fix a horizon.

## Main Contribution

Reframes agent evaluation as a diagnostic vocabulary and audit protocol — separating outcome success from control-decision quality and trajectory quality — and demonstrates the reframing across 15 existing agent benchmarks with concrete measurements on 1,342 items.

## Key Design Ideas

- Six control-decision types as a shared vocabulary across heterogeneous benchmarks.
- Failure taxonomy for classifying agent errors beyond binary pass/fail.
- Audit protocol as an overlay on existing benchmarks rather than a new task suite.
- Cross-benchmark applicability (applied to 15 benchmarks).

## Strengths

- Provides a shared vocabulary that spans heterogeneous agent benchmarks.
- Overlay design inherits tasks from existing benchmarks rather than requiring a new suite.
- Explicit measurement on 1,342 items grounds the framework's claims.

## Limitations

- Repository note: AgentAtlas is a framework layered on existing benchmarks rather than a standalone task suite; its coverage inherits whatever the audited benchmarks cover.

## Related Works

- [Insights Generator](./insights-generator.md) — Also a trace-level diagnostic contribution rather than a task suite; Insights Generator emphasizes automated corpus-level hypothesis testing, AgentAtlas emphasizes a shared diagnostic vocabulary.
- [AgentBoard](./agentboard.md) — Also decomposes evaluation below end-task success; AgentBoard decomposes per task via subgoals, AgentAtlas decomposes per control-decision type across benchmarks.
