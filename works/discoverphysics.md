# DiscoverPhysics (2026)

> **English** | [简体中文](../zh/works/discoverphysics.md)

## Overview

DiscoverPhysics is an agentic benchmark for out-of-the-box scientific thinking: the agent must discover the laws of motion of a simulated world whose physics deliberately deviates from our own — screened gravity, hidden particle species, modified force laws — by proposing rounds of experiments and analyzing raw trajectory data.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.26087>
- **Code:** <https://github.com/SampsonML/DiscoverPhysics>
- **Venue:** arXiv preprint (stat.ML, cs.LG), 2026

## Summary

Each of 22 worlds is generated on demand by an N-body simulator with deliberately non-standard physics. The agent proposes several rounds of experiments, observes raw trajectory data, and ultimately submits both a natural-language explanation of the world's physics and a Python implementation of the inferred law. Scoring runs on two complementary axes: trajectory MSE on held-out particles, and an LLM-judged explanation score against an expert-written rubric assessing conceptual understanding. Across eleven frontier models, the strongest agents pass only half of the worlds and consistently fail where latent structure must be uncovered; good predictive accuracy does not guarantee high explanation quality.

## Tasks

22 counterfactual simulated worlds (e.g., modified gravity, extra dimensions, dark-matter-like hidden species per the official repository's world types), each requiring iterative experiment proposal, observation of raw N-body trajectory data, and submission of an explanation plus a Python law implementation.

## Domains

Classical mechanics and N-body dynamics with astrophysics-flavored counterfactuals (modified gravity, dark-matter-like particles, cosmological expansion analogues).

## Evaluation

- **Trajectory MSE** on held-out particles (predictive fidelity).
- **LLM-judged explanation score** against an expert-written rubric (conceptual understanding).
- **Reported.** Eleven frontier models evaluated; the strongest agents pass only half of the worlds and consistently fail on those where latent structure must be uncovered; open-source models lag substantially behind commercial models.

## Typical Duration

Several rounds of proposed experiments per world; per-world budgets are TODO(reference).

## Main Contribution

Separates predicting a world from understanding it: paired trajectory-fidelity and rubric-judged explanation scores expose agents that fit the data without uncovering the latent physics.

## Key Design Ideas

- Deliberately non-standard physics makes memorized laws not merely useless but misleading.
- Requiring both a natural-language explanation and executable Python code forces understanding to be stated twice, in different representations.
- On-demand world generation from an N-body simulator keeps evaluation contamination-resistant.

## Strengths

- Directly measures the failure mode that matters for discovery: models that predict well while explaining wrongly.
- Consistent failures on latent-structure worlds locate a specific capability gap.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [NewtonBench](./newtonbench.md) — Also counterfactual law discovery over simulated systems, scored by symbolic equivalence rather than paired prediction/explanation.
- [Gravity-Bench-v1](./gravity-bench.md) — Also gravitational-physics discovery with out-of-distribution variants, under an observation budget.
- [MaD Physics](./mad-physics.md) — Also infers altered physical laws from budgeted interaction with simulated systems.
