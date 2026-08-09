# EmbodiedBench (2025)

> **English** | [简体中文](../zh/works/embodiedbench.md)

## Overview

EmbodiedBench evaluates multimodal LLMs as vision-driven embodied agents at scale: 1,128 testing tasks across four environments, from high-level household semantics down to atomic navigation and manipulation actions, organized into six capability subsets — the best model, GPT-4o, scores only 28.9% on average.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2502.09560>
- **Project:** <https://embodiedbench.github.io>
- **Venue:** ICML 2025

## Summary

EmbodiedBench spans the full vertical of embodied competence: EB-ALFRED and EB-Habitat for high-level semantic tasks, EB-Navigation and EB-Manipulation for low-level atomic action, with six curated capability subsets probing commonsense reasoning, complex instruction understanding, spatial awareness, visual perception, and long-term planning. Evaluating 24 leading proprietary and open-source MLLMs shows a consistent split: models handle high-level tasks but struggle with low-level manipulation, capping even GPT-4o at 28.9% average.

## Tasks

1,128 interactive testing tasks across four environments; the MLLM acts as the full vision-driven agent from instruction to action. Simulation only.

## Domains

Embodied household simulation — outside the repository's science/engineering domain axis; documented for its evaluation methodology.

## Evaluation

- Task success across environments plus six capability-subset breakdowns.
- **Reported.** Best model GPT-4o at 28.9% average across 24 MLLMs; high-level competence, low-level manipulation weakness.

## Typical Duration

Interactive episodes from high-level household tasks to atomic navigation/manipulation steps.

## Main Contribution

A vertically integrated measurement showing that MLLM embodied competence is top-heavy — semantic planning outruns the perception-action grounding beneath it.

## Key Design Ideas

- Pairing high-level and atomic-action environments in one benchmark localizes where the stack breaks.
- Capability subsets are curated, not post-hoc, so the six dimensions are separately measurable.
- 24-model coverage makes the high-vs-low split a population finding, not a model quirk.

## Strengths

- The largest venue-verified MLLM embodied evaluation at its release, with a maintained public stack.
- The 28.9% ceiling gave the field a concrete, oft-cited capability marker.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project page (August 2026); environment implementation details await full-paper validation.
- Simulation-only; no physical robot platform.

## Related Works

- [LoTa-Bench](./lota-bench.md) — Also execution-scored embodied planning, for text-side LLM planners.
- [EmbodiedEval](./embodiedeval.md) — Also interactive MLLM embodied evaluation, across 125 diverse 3D scenes.
- [PARTNR](./partnr.md) — Also large-scale embodied evaluation, focused on human-robot collaboration.
