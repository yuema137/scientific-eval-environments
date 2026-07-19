# TRACE (2026)

## Overview

TRACE (Trajectory-Aware Comprehensive Evaluation) 是面向 deep research agent 的评估框架：通过 hierarchical utility function 对整条推理 trajectory 打分，并通过测量"成功所需最少引导"来量化 agent 的潜在能力。论文同时发布 DeepResearch-Bench，一个可控复杂度的配套 benchmark。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.21230>
- **Venue:** WWW 2026

## Summary

TRACE 论文指出：Pass@1 类评估在 deep research agent 上会造成 "high-score illusion"——只看最终答案而忽略推理质量与过程效率。TRACE 提出两部分评估：一个 hierarchical trajectory utility function，联合评价 accuracy、efficiency、evidence grounding 与 reasoning quality；以及一个 scaffolded-capability assessment，量化成功所需的最少引导。论文同时发布 DeepResearch-Bench，一个可控复杂度的配套 benchmark。

## Tasks

DeepResearch-Bench，具有可控的任务复杂度分级。精确任务数：TODO(reference)。

## Domains

Deep research agent 任务：web search、evidence collection、retrieval、reasoning、report generation。

## Evaluation

- **Hierarchical Trajectory Utility Function** — 对 accuracy、process efficiency、evidence grounding、reasoning quality 的联合评分。
- **Scaffolded Capability Assessment** — 通过测量成功所需的最少引导，量化 agent 的潜在能力。
- 将评估重构为揭示 accuracy / efficiency / robustness 之间的 trade-off，而非单一 Pass@1。

## Typical Duration

长 horizon、多步的研究工作流，涉及反复的 retrieval、reasoning 与 synthesis。

## Main Contribution

明确主张 trajectory 应是 deep research agent 的一等评估对象，并给出效用函数评分 + scaffolded-capability 协议来落地这一主张。

## Key Design Ideas

- Trajectory 作为一等评估对象，而不是副产品。
- Hierarchical utility function 把多个质量维度合并入单一评分。
- Scaffolded-capability assessment 测量 agent 需要的引导量，而不是假设 Pass@1 代表能力。
- DeepResearch-Bench 的可控复杂度使评估可校准。

## Strengths

- 通过测量引导依赖，把能力与 Pass@1 分开。
- 联合效用函数揭示单指标排行榜掩盖的 trade-off。
- 可控复杂度使评估可校准。

## Limitations

- Repository note: Hierarchical utility 中的 reasoning quality 与 evidence grounding 需要 judge（模型或人）参与评分。

## Related Works

- [FinTrace](./fintrace.md) — 同样做多维 trajectory 评估，但面向金融而非 deep research。
- [AgentBoard](./agentboard.md) — Trajectory 评估基于子目标进展率，而非 hierarchical utility function。
