# ChemCost (2026)

> **English** | [简体中文](../zh/works/chemcost.md)

> **First appeared:** 2026-05-08 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.07251)

## Overview

ChemCost asks whether agents can price a reaction: 1,427 evaluable reactions grounded to a frozen pricing snapshot of 2,261 chemicals and 230,775 supplier quotes, where an agent must ground chemical identities, retrieve quotes, select valid purchasable packs, normalize quantities, and compute cost — the strongest agents reach only 50.6% accuracy within 25% relative error on clean inputs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.07251>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Costing a synthesis is a mundane but unforgiving chemistry task: every step — identity grounding, quote retrieval, pack selection, quantity normalization, arithmetic — must succeed. ChemCost freezes a pricing snapshot so ground truth is exact and judge-free, evaluates frontier, open-weight, and chemistry-specialized LLM agents, and diagnoses failures stage by stage. Best agents hit 50.6% accuracy within 25% relative error on clean inputs and degrade substantially under controlled noise injections that perturb chemical aliases, quantity expressions, missing fields, and formatting.

## Tasks

1,427 evaluable reaction-pricing tasks over a frozen snapshot (2,261 chemicals, 230,775 supplier quotes); interactive tool-using episodes covering grounding, retrieval, procurement selection, and cost computation, plus noise-injected robustness views.

## Domains

Chemistry — chemical procurement and cost estimation as part of practical synthesis planning.

## Evaluation

- Exact, judge-free ground truth from the frozen snapshot; scalar cost scoring with stage-level diagnosis of grounding, retrieval, procurement, and arithmetic failures.
- **Reported.** Strongest agents: 50.6% accuracy within 25% relative error on clean inputs, with substantial degradation under realistic noise.

## Typical Duration

Multi-step tool-using episodes per reaction (ground → retrieve → select → normalize → compute).

## Main Contribution

Making economic reasoning about chemistry itself the measured task — with a frozen market snapshot that gives cost questions the exact ground truth they never have in the live world.

## Key Design Ideas

- Freezing the pricing snapshot converts a moving-target task into a reproducible benchmark.
- Stage-level diagnosis attributes failure to the pipeline step, not just the final number.
- Noise-injected views measure robustness to exactly the messiness real procurement data has.

## Strengths

- Judge-free scalar ground truth in a domain (pricing) where verification is usually impossible.
- The clean-vs-noisy gap quantifies brittleness that clean-benchmark scores hide.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond the abstract await full-paper validation. No code or dataset release is verifiable from the paper's arXiv page.

## Related Works

- [EcoAgent-Bench](./ecoagent-bench.md) — Also economic decision-making by agents, over priced actions and budgets.
- [SDBench](./sdbench.md) — Also scores agents on a cost dimension, along the accuracy-versus-cost frontier.
- [SMDD-Bench](./smdd-bench.md) — Also multi-step molecular tasks with resource limits, via oracle-call budgets.
