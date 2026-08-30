# MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions (2025)

> **English** | [简体中文](../zh/works/ma-rlhf.md)

> **First appeared:** 2024-10-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2410.02743)

## Overview

MA-RLHF replaces token-level policy updates with macro-actions made from token sequences or higher-level language constructs, testing whether coarser temporal abstraction improves RLHF credit assignment and learning efficiency.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — general LLM alignment methodology; no scientific or research activity is directly evaluated.

## Links

- **Preprint:** <https://arxiv.org/abs/2410.02743>
- **Paper:** <https://proceedings.iclr.cc/paper_files/paper/2025/hash/429d69979c22b06d6baa65caf3ab1e10-Abstract-Conference.html>
- **Code:** <https://github.com/ernie-research/MA-RLHF>
- **Venue:** ICLR 2025

## Summary

Standard RLHF treats every subword token as an action, leaving delayed sequence rewards far from the decisions they must credit. MA-RLHF groups adjacent tokens into macro-actions under a semi-Markov formulation. Across summarization, dialogue, question answering, and program synthesis, the paper reports parity with vanilla RLHF in roughly 1.7–2× less training time and gains that persist with additional training.

## Tasks

Preference optimization on text summarization, dialogue generation, question answering, and program synthesis, using Gemma-family models from 2B to 27B parameters.

## Domains

General language-model alignment and reinforcement learning; not tied to a canonical scientific or engineering domain.

## Evaluation

Task-specific quality and reward metrics, training curves and time-to-parity against token-level RLHF, plus robustness checks across macro-action construction, temperature, and rejection sampling.

## Typical Duration

Not reported as a fixed per-example duration; the paper compares end-to-end training time and convergence.

## Main Contribution

An empirical test of temporal granularity in RLHF showing that tokenization need not determine the policy's decision granularity.

## Key Design Ideas

- Aggregate token log-probabilities and advantages at macro-action boundaries.
- Compare fixed-length and learned semantic grouping without adding inference cost.

## Strengths

- Holds the underlying language-generation setting close to standard RLHF.
- Reports learning speed as well as terminal task quality across several model sizes.

## Limitations

- A macro-action can be only a larger token chunk; semantic decision structure is not guaranteed.
- The study measures efficiency and downstream task quality, not compositional OOD strategy transfer.
- It does not separate high-level strategy choice from low-level generation in a modular planner–executor architecture.

## Related Works

- [CoLA](./cola.md) — learns rather than manually groups the action representation.
- [HiPER](./hiper.md) — introduces an explicit subgoal/execution hierarchy for interactive agents.
