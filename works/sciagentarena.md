# SciAgentArena (2026)

## Overview

SciAgentArena is a systematic benchmark for evaluating AI agents in real-world scientific research scenarios across scales. It provides roughly 200 tasks with stepwise verification in an interactive, agent-agnostic environment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12736>
- **Project:** <https://sciagentarena.github.io/>

## Summary

Titled *Benchmarking AI Agents for Addressing Scientific Challenges Across Scales*, SciAgentArena addresses the fact that AI agents' practical capabilities in real research settings remain poorly understood. It provides an interactive, agent-agnostic environment with roughly 200 tasks constructed from real-world scientific research scenarios across multiple domains, using stepwise verification. It reports that agents perform well on structured data-analysis workflows but struggle with novel insights, self-directed exploration, and open-ended questions, and it catalogs common failure modes.

## Tasks

Approximately 200 tasks with stepwise verification, constructed from real-world scientific research scenarios across multiple domains and scales. Exact domain inventory and per-domain counts: TODO(reference) — not specified on the abstract page.

## Domains

Multiple scientific-research domains across scales. Specific disciplines: TODO(reference).

## Evaluation

- Interactive, agent-agnostic environment supporting diverse AI agents.
- Stepwise verification of agent progress.
- Reported qualitative finding: strong on structured data-analysis workflows; weak on novel insights, self-directed exploration, and open-ended questions.

## Typical Duration

Multi-step scientific-research workflows. Per-task duration: TODO(reference) — not stated on the abstract page.

## Main Contribution

A systematic, agent-agnostic benchmark for measuring AI-agent progress on real scientific-research scenarios across scales, with stepwise verification and an explicit account of where agents currently succeed and fail.

## Key Design Ideas

- Real-world scientific research scenarios spanning multiple scales.
- Stepwise verification rather than only terminal outcome scoring.
- Agent-agnostic, interactive environment supporting diverse agents.
- Explicit failure-mode analysis (novel insight, self-directed exploration, open-ended questions).

## Strengths

- Stepwise verification gives finer-grained signal than terminal success alone.
- Agent-agnostic design supports comparison across diverse agent implementations.
- Reports concrete strengths/weaknesses rather than a single score.

## Limitations

- Repository note: The specific scientific domains, scales, and per-domain task counts are not stated on the abstract page and are marked `TODO(reference)` pending verification from the paper or project.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also assesses agents on data-driven scientific tasks, but grades a unified Python-program output rather than stepwise verification across scales.
- [AIRS-Bench](./airs-bench.md) — Also targets research-science tasks, evaluating an end-to-end research lifecycle.
