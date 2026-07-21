# AgentBench (2023)

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

8 distinct interactive environments spanning reasoning and decision-making tasks. Exact list of the 8 environments: TODO(reference) — not enumerated in the abstract.

## Domains

Interactive agent environments across multiple task types (coding/operating-system-style, knowledge/database, game, web, and household-style environments). Precise environment inventory: TODO(reference).

## Evaluation

- Multi-round interaction within each environment, scored per environment on task-specific success.
- Both commercial (API-based) and open-source LLMs evaluated under the same protocol.

## Typical Duration

Multi-round interactive episodes per environment. Per-task step/time budgets: TODO(reference) — not stated in the abstract.

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

- Repository note: The exact set of eight environments is not enumerated in the abstract and is marked `TODO(reference)` pending verification from the paper.

## Related Works

- [SWE-bench](./swe-bench.md) — Also a general agent benchmark, but specialized to software-engineering issue resolution rather than spanning eight environments.
- [GAIA](./gaia.md) — Also evaluates general assistant capability, but via a single unified question-answering surface rather than multiple environments.
