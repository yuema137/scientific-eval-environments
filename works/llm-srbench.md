# LLM-SRBench (2025)

> **English** | [简体中文](../zh/works/llm-srbench.md)

## Overview

LLM-SRBench is a benchmark of 239 challenging problems for scientific equation discovery with LLMs, designed to prevent trivial memorization: LSR-Transform recasts common physical models into less common mathematical representations, and LSR-Synth introduces synthetic, discovery-driven problems requiring data-driven reasoning.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.10415>
- **Code:** <https://github.com/deep-symbolic-mathematics/llm-srbench>
- **Dataset:** <https://huggingface.co/datasets/nnheui/llm-srbench>
- **Venue:** ICML 2025 (oral)

## Summary

Equation-discovery evaluations built on well-known equations reward recall of famous formulas rather than discovery. LLM-SRBench closes that gap with two problem classes across four scientific domains: LSR-Transform, which starts from common physical models but demands reasoning in unfamiliar mathematical representations, and LSR-Synth, whose synthetic problems have no memorizable answer at all. Evaluating state-of-the-art discovery methods with open and closed LLM backbones, the best-performing system reaches only 31.5% symbolic accuracy.

## Tasks

239 equation-discovery problems in two classes (LSR-Transform and LSR-Synth) across four scientific domains; systems recover governing equations from data.

## Domains

Four scientific domains; the abstract does not name them.

## Evaluation

- **Symbolic accuracy** of recovered equations against ground truth.
- **Reported.** The best-performing system so far achieves only 31.5% symbolic accuracy.

## Typical Duration

Iterative equation-search runs per problem; budgets are method-dependent and TODO(reference).

## Main Contribution

An equation-discovery benchmark whose construction makes memorization structurally unrewarding, turning symbolic regression with LLMs into a measured discovery capability.

## Key Design Ideas

- Transforming known models into unfamiliar representations severs the shortcut from recall to answer.
- Synthetic discovery-driven problems guarantee a memorization-free subset.
- A single symbolic-accuracy metric keeps heterogeneous discovery methods comparable.

## Strengths

- Method-agnostic: benchmarks discovery systems rather than one modeling family.
- The 31.5% ceiling documents how far LLM-based discovery stands from reliable equation recovery.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [NewtonBench](./newtonbench.md) — Also guards law discovery against memorization, via counterfactual shifts of canonical laws.
- [DiscoverPhysics](./discoverphysics.md) — Also scores discovered laws, adding interactive experimentation and explanation judging.
- [MaD Physics](./mad-physics.md) — Also infers governing laws from data, under priced observation budgets.
