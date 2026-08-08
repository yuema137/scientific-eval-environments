# PhysGym (2025)

> **English** | [简体中文](../zh/works/physgym.md)

## Overview

PhysGym is a benchmark suite and simulation platform for LLM-based agents in interactive physics discovery: agents actively probe simulated environments, gather data sequentially under constraints, and formulate hypotheses about underlying physical laws — with sophisticated control over how much prior knowledge the agent is given.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.15550>
- **Code:** <https://github.com/principia-ai/PhysGym>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks (per the official repository)

## Summary

PhysGym's distinctive axis is prior-knowledge control: the same discovery problem can be posed at four levels of provided priors (L1–L4 per the official repository), so the benchmark can separate what an agent discovers from what it was told. The suite comprises 97 curated physics problems (sourced from PHYBench, per the official repository) run as interactive simulations with limited experimental budgets, and provides standardized evaluation protocols and metrics for assessing hypothesis accuracy and model fidelity.

## Tasks

97 curated physics problems (official repository) posed as interactive simulation episodes: probe the environment, gather data sequentially under a limited experimental budget (100 experiments per the repository), and submit hypotheses about the governing physical laws, at four controlled levels of prior knowledge.

## Domains

Physics discovery over interactive simulations of physical laws; problems are sourced from the PHYBench problem set.

## Evaluation

- Standardized protocols and metrics for hypothesis accuracy and model fidelity.
- **Reported (official repository).** Performance degrades as priors are removed — e.g., o4-mini falls from 62.89% at L1 to 31% at L4.

## Typical Duration

Sequential interactive episodes bounded by a limited experimental budget (100 experiments per the official repository).

## Main Contribution

Makes prior knowledge an experimentally controlled variable of physics-discovery evaluation, so discovery ability can be measured separately from recall of supplied context.

## Key Design Ideas

- Four prior-knowledge levels turn "how much was the agent told" into a benchmark axis.
- Sequential data gathering under constraints keeps the setting genuinely interactive rather than one-shot.
- Reusing vetted PHYBench problems anchors the simulations in an existing validated problem set.

## Strengths

- The L1→L4 degradation curve quantifies how much apparent capability is carried by supplied priors.
- Platform design supports controlled comparisons across agents and knowledge conditions.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [MaD Physics](./mad-physics.md) — Also interactive physics discovery under budget constraints, with fidelity-priced observations.
- [DiscoverPhysics](./discoverphysics.md) — Also agentic law discovery in simulated worlds, with deliberately non-standard physics.
- [PHYBench](./phybench.md) — The problem source PhysGym builds its interactive environments from.
