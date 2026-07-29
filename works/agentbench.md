# AgentBench (2023)

> **English** | [简体中文](../zh/works/agentbench.md)

## Overview

AgentBench is a multi-dimensional benchmark that evaluates LLMs as agents across 8 distinct interactive environments, assessing reasoning and decision-making abilities over multi-round interaction.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.03688>
- **Code:** <https://github.com/THUDM/AgentBench>
- **Venue:** ICLR 2024

## Summary

AgentBench responds to the need to quantitatively evaluate LLMs as agents on challenging tasks in interactive environments. It assembles 8 distinct environments that probe an LLM-as-agent's reasoning and decision-making across multi-round interaction, and evaluates both API-based commercial models and open-source models. The study reports a substantial capability gap between top commercial LLMs and open-source models, and identifies long-term reasoning, decision-making, and instruction-following as primary bottlenecks.

## Tasks

Eight interactive environments, grouped by grounding: **code-grounded** — Operating System (bash on Linux), Database (SQL on MySQL), Knowledge Graph; **game-grounded** — Digital Card Game, Lateral Thinking Puzzles, House-Holding (built on ALFWorld); **web-grounded** — Web Shopping (built on WebShop), Web Browsing (built on Mind2Web).

## Domains

Interactive agent tasks across operating systems, databases, knowledge graphs, games, embodied household simulation, and the web.

## Evaluation

- **Per-environment metrics.** Each environment uses a metric suited to it: Success Rate (Operating System, Database, House-Holding), Answer F1 (Knowledge Graph), reward / win-rate (Digital Card Game, Web Shopping), Game Progress — fraction of plot points reached (Lateral Thinking Puzzles), and Step Success Rate (Web Browsing).
- **Overall Score via per-task normalization.** Because the eight metrics live on different scales, each task's scores are normalized before averaging: a fixed per-task weight — the reciprocal of the mean score of all evaluated models on that task — rescales every task's cross-model average to 1.0; each model's per-task score is multiplied by that weight, and the weighted scores are averaged across the eight tasks. The weights are frozen so future models are scored reproducibly.
- **Reported.** GPT-4 leads with an overall score of 4.01; the strongest open-source model (CodeLlama-34b) reaches 0.96. Averaged over models, API-based commercial LLMs score 2.15 vs. 0.51 for open-source — roughly a 4× gap. Primary failure modes: weak long-term reasoning, decision-making, and instruction-following.

## Typical Duration

Multi-round interaction whose length varies by environment — the most interactive (House-Holding, Digital Card Game, Lateral Thinking Puzzles) run to several tens of turns, while Operating System, Database, and Web Shopping episodes are shorter. Hard per-task round caps are not separately tabulated.

## Main Contribution

A systematic multi-environment benchmark that quantitatively evaluates LLM-as-agent reasoning and decision-making, surfacing a large commercial-vs-open-source gap and concrete capability bottlenecks.

## Key Design Ideas

- Eight heterogeneous environments under one evaluation harness for breadth of agentic capability.
- Multi-round interaction rather than single-shot response.
- Uniform evaluation across commercial and open-source models.
- Diagnoses bottlenecks: long-term reasoning, decision-making, instruction-following.

## Strengths

- Breadth across eight distinct environments in a single benchmark.
- Directly compares commercial and open-source models under one protocol.
- Identifies actionable capability bottlenecks rather than a single leaderboard number.

## Limitations

- Repository note: Six of the eight environments are built on or adapted from prior datasets (ALFWorld, WebShop, Mind2Web); AgentBench's own contribution is the unified harness, the three code-grounded environments, and the normalized cross-environment scoring, not all task content.

## Related Works

- [SWE-bench](./swe-bench.md) — Also a general agent benchmark, but specialized to software-engineering issue resolution rather than spanning eight environments.
- [GAIA](./gaia.md) — Also evaluates general assistant capability, but via a single unified question-answering surface rather than multiple environments.
