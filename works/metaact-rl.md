# MetaAct-RL: Training Language Models for Reasoning Through Meta-Action-Based Reinforcement Learning (2026)

> **English** | [简体中文](../zh/works/metaact-rl.md)

## Overview

MetaAct-RL formulates language-model reasoning as sequential choice and execution of semantic meta-actions such as forward reasoning, critique, and refinement.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — general mathematical and verbal reasoning methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://ojs.aaai.org/index.php/AAAI/article/view/40694>
- **Venue:** AAAI 2026

## Summary

The framework annotates and trains reasoning traces around high-level thinking actions, then applies reinforcement learning with length rewards, regularization, and key-state restarts to promote diverse action use. Across AQuA, GSM8K, MATH, MathQA, SVAMP, and TheoremQA, it reports average gains of 7.99 points for Llama-3.2-1B and 7.17 for Llama-3.1-8B over vanilla RL; Qwen2.5-1.5B gains 7.5 points on AIME 2024.

## Tasks

Six standard reasoning benchmarks, with additional AIME 2024 and AIME 2025 evaluation and training data synthesized from MATH, GSM8K, and AQuA.

## Domains

General language-model reasoning and post-training; not tied to a canonical science or engineering domain.

## Evaluation

Answer accuracy, response length, meta-action distribution and diversity, sampling efficiency, and ablations of reward and restart components.

## Typical Duration

No fixed per-problem wall-clock budget is reported.

## Main Contribution

Making semantic thinking operations explicit policy decisions rather than hoping that outcome-only token RL elicits critique and refinement incidentally.

## Key Design Ideas

- Synthesize traces with explicit meta-action boundaries.
- Use length regularization and key-state restart to preserve action diversity during RL.

## Strengths

- Measures behavioral diversity alongside answer accuracy.
- Reports results across model families, scales, and both standard and harder held-out benchmarks.

## Limitations

- The authored action vocabulary may impose a fixed ontology of reasoning.
- Gains on familiar reasoning suites do not resolve whether meta-actions transfer to unseen engineering workflows.
- The model still generates action labels and detailed reasoning in one autoregressive system, so module-level fault isolation is partial.

## Related Works

- [PG-HAP](./pg-hap.md) — freezes the executor and trains only a separate high-level planner.
- [Beyond 'Aha!'](./beyond-aha.md) — aligns reusable reasoning abilities rather than per-step action labels.
