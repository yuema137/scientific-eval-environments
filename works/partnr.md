# PARTNR (2024)

> **English** | [简体中文](../zh/works/partnr.md)

## Overview

PARTNR benchmarks planning and reasoning in embodied multi-agent tasks — human-robot collaboration in household activities — at unmatched scale: 100,000 natural-language tasks spanning 60 houses and 5,819 unique objects in Habitat 3.0, with LLM planners analyzed across planning, perception, and skill execution.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.00081>
- **Code:** <https://github.com/facebookresearch/partnr-planner>
- **Project:** <https://aihabitat.org/partnr/>
- **Venue:** ICLR 2025 (per the official repository; arXiv metadata carries no venue)

## Summary

PARTNR generates its 100,000 tasks semi-automatically with LLMs, using simulation in the loop for grounding and verification, then turns the tables and evaluates LLMs as collaborative planners. The headline findings are humbling: paired with real human partners, LLM agents need 1.5x as many steps as two humans collaborating — and 1.1x more than a single human working alone. On the model side, fine-tuning smaller LLMs on planning data matches models 9 times larger while running 8.6x faster at inference.

## Tasks

100,000 natural-language human-robot collaboration tasks (constraint-free, spatial, temporal, and heterogeneous types) across 60 houses and 5,819 objects in Habitat 3.0; LLM planners coordinate with simulated or real human partners. Simulation only, with human-in-the-loop evaluation.

## Domains

Embodied household simulation (Habitat) — outside the repository's science/engineering domain axis per its scope line; documented for its evaluation methodology.

## Evaluation

- Analysis across planning, perception, and skill-execution axes; human-in-the-loop comparisons against human-human collaboration.
- **Reported.** LLM + real human: 1.5x the steps of two humans, 1.1x a single human; fine-tuned small planners match 9x-larger models at 8.6x faster inference.

## Typical Duration

Multi-step collaborative episodes with a concurrent (simulated or real) human partner.

## Main Contribution

Measuring whether an LLM planner actually helps a human — the collaboration-overhead finding that an LLM partner is currently worse than working alone.

## Key Design Ideas

- LLM-generated, simulation-verified task generation buys scale without unverified tasks.
- Real-human pairing converts "collaboration" from a simulated construct into a measured cost.
- Task types isolate spatial, temporal, and heterogeneous constraint handling.

## Strengths

- Orders of magnitude larger than prior embodied-collaboration benchmarks, with grounded verification.
- The 1.1x-vs-single-human result is a rare, decision-relevant negative finding.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the ICLR 2025 venue is stated by the repository, not arXiv metadata.
- Simulation-only robots; findings about physical deployment are out of scope.

## Related Works

- [RoCo / RoCoBench](./rocobench.md) — Also LLM multi-robot collaboration, with dialog between robot agents and real-arm demos.
- [VIKI-Bench](./viki-bench.md) — Also embodied multi-agent cooperation, hierarchically decomposed across robot embodiments.
- [EmbodiedBench](./embodiedbench.md) — Also large-scale embodied MLLM evaluation, single-agent.
