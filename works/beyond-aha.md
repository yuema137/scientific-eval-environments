# Beyond 'Aha!': Toward Systematic Meta-Abilities Alignment in Large Reasoning Models (2026)

> **English** | [简体中文](../zh/works/beyond-aha.md)

## Overview

Beyond 'Aha!' explicitly aligns deduction, induction, and abduction as reusable meta-abilities before domain-specific reinforcement learning, rather than relying on outcome RL to elicit them incidentally.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — evaluates general reasoning transfer across benchmark tasks rather than an agent performing a scientific or research workflow.

## Links

- **Paper:** <https://aclanthology.org/2026.findings-acl.1981/>
- **Venue:** Findings of ACL 2026

## Summary

The paper constructs self-verifiable synthetic tasks for deduction, induction, and abduction, aligns each ability separately, merges the resulting parameter states, and then applies domain-specific RL. Evaluation across math, coding, and science tests whether explicitly trained reasoning primitives provide a more stable starting point than waiting for self-correction, backtracking, or verification to emerge unpredictably from outcome reward.

## Tasks

Three synthetic diagnostic training sets and seven unseen evaluation benchmarks spanning mathematics, coding, and science, including MATH-500, historical AIME, AIME 2024, and LiveCodeBench.

## Domains

General reasoning post-training across math, coding, and science benchmarks; not a scientific-agent workflow.

## Evaluation

Pass@1 on seven unseen benchmarks, meta-ability-specific diagnostics, parameter-merging comparisons, and gains from subsequent domain RL for 7B and 32B models.

## Typical Duration

No fixed per-example wall-clock budget is reported.

## Main Contribution

An evaluation-driven test of whether explicit, reusable cognitive primitives can provide a transferable foundation for later reasoning optimization.

## Key Design Ideas

- Train each meta-ability on automatically generated, self-verifiable tasks.
- Merge separately aligned abilities before domain-specific RL.

## Strengths

- Evaluates held-out transfer across three task families rather than one dataset.
- Separates primitive alignment, parameter merging, and downstream RL through staged experiments.

## Limitations

- Meta-abilities are capability targets rather than explicit per-step actions in an interactive policy.
- The three-way taxonomy is authored and may omit other useful cognitive operations.
- Benchmark transfer does not by itself demonstrate causal modularity or fault localization in agents.

## Related Works

- [MetaAct-RL](./metaact-rl.md) — uses explicit reasoning operations as sequential actions.
- [CoLA](./cola.md) — learns latent actions without naming their cognitive meaning.
