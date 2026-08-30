# PTA-GRPO: Plan Then Action, High-Level Planning Guidance Reinforcement Learning for LLM Reasoning (2025)

> [English](../../works/pta-grpo.md) | **简体中文**

> **首次公开：** 2025-10-02 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2510.01833)

## 概览

PTA-GRPO 从 chain-of-thought trace 中提炼简短 high-level guidance，再用 RL 同时优化 plan quality 与细粒度 reasoning。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — 通用数学 reasoning 方法，没有直接评价科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2510.01833>
- **Venue:** arXiv preprint, 2025

## 摘要

第一阶段把详细 solution trace 总结成 analytic plan，用 plan–reasoning pair 做 SFT。第二阶段加入 guidance-aware GRPO，同时奖励最终答案与 high-level plan 质量。这里的层级是「先给 plan，再生成 token-level reasoning」，不是两个模块分别在不同环境时间尺度上行动。

## 任务

十个数学 reasoning benchmark；主要结果表包括 MATH-500、AIME 2024、AIME 2025 和 AMC 2023，覆盖 Qwen 与 Llama model family。

## 领域

通用数学 reasoning 与语言模型 post-training。它研究通用 reasoning 方法，不是数学研究活动，因此不映射到 Mathematics domain。

## 评估

跨 benchmark answer accuracy、plan-quality reward、不同 model 下的一致性，以及 SFT plan guidance 与 RL objective ablation。

## Typical Duration

没有报告固定的逐题时间或 token budget。

## 主要贡献

在一个 post-training objective 中，分别监督简短 global guidance 与详细 local reasoning。

## Key Design Ideas

- 把详细 chain 提炼成简短 analytic guidance。
- 在 GRPO 中同时优化 guidance quality 与 final correctness。

## Strengths

- 覆盖多个 model 与 benchmark。
- Ablation 分开检验 plan supervision 与 guidance-aware RL。

## 局限

- Plan 来自 solution trace，可能把 dataset-specific template 一起提炼进去。
- Plan quality 由 learned reward 判断，不是 executable validity。
- 实验以数学 IID benchmark 为主，没有 interactive 或 compositional transfer。

## Related Works

- [PG-HAP](./pg-hap.md)
- [MetaAct-RL](./metaact-rl.md)
