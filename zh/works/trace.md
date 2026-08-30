# TRACE (2026)

> [English](../../works/trace.md) | **简体中文**

> **首次公开：** 2026-02-05 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.21230)

## Overview

TRACE (Trajectory-Aware Comprehensive Evaluation) 是面向 deep research agent 的评估框架：通过 hierarchical utility function 对整条推理 trajectory 打分，并通过测量"成功所需最少引导"来量化 agent 的潜在能力。论文同时发布 DeepResearch-Bench，一个可控复杂度的配套 benchmark。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2602.21230>
- **Venue:** WWW 2026

## Summary

TRACE 论文指出：Pass@1 类评估在 deep research agent 上会造成 "high-score illusion"——只看最终答案而忽略推理质量与过程效率。TRACE 提出两部分评估：一个 hierarchical trajectory utility function，联合评价 accuracy、efficiency、evidence grounding 与 reasoning quality；以及一个 scaffolded-capability assessment，量化成功所需的最少引导。论文同时发布 DeepResearch-Bench，一个可控复杂度的配套 benchmark。

## Tasks

DeepResearch-Bench 共 650 个任务，分三个子集：**TRACE-Core**（500 个任务，平均复杂度 C(q)=3.5，约 20% 含 "information trap"）、**TRACE-Robustness**（100 个任务，C(q)=4.2，全部含 trap）、**TRACE-Scaffolding**（50 个任务，C(q)=5.8，40% 含 trap）。复杂度是由 formalism 驱动合成得到的连续标量 C(q)，而非离散分级。

## Domains

Deep research agent 任务：web search、evidence collection、retrieval、reasoning、report generation。

## Evaluation

- **Hierarchical Trajectory Utility U(H)。** 最终答案的正确性作为硬性乘法门，作用在效率与认知质量的乘积之上——U(H) = 𝟙(答案正确) · E(H)^ω_E · C(H)^ω_C——因此答案错误会使整条效用归零。
  - **Process Efficiency E(H)** 奖励解决更复杂的任务，同时除以一个 trajectory 成本泛函，其中的 *Redundant Exploration Penalty* 按相邻观测 embedding 的余弦相似度，降权连续的无信息动作。
  - **Cognitive Quality C(H) = β·G_E + (1−β)·R_R** 结合 **Evidence Grounding** G_E（各原子主张 NLI 蕴含概率的几何平均，任一未被支撑的主张都会使其崩塌）与 **Reasoning Robustness** R_R（遭遇预设 information trap 后恢复所需步数的指数衰减）。
  - 全程采用几何平均是刻意为之：“研究过程的强度取决于其最薄弱的一环”。
- **Scaffolded Capability Assessment。** 借用 Vygotsky 的最近发展区，它揭示 oracle 解题 trajectory 的前 λ 比例，并报告 **λ_min**——期望成功率越过阈值 θ_succ（≈0.9）所需的最小提示比例（∈ [0,1]）。λ_min 越低，内在能力越强。
- **报告的 “high-score illusion”。** DeepSeek-V3.1-671B 的 Pass@1 最高（65.8%），但在头部模型中 trajectory utility 最低（0.65）；Gemini-2.5-pro 则为 Pass@1 75.4% / utility 0.88。Scaffolding λ̄_min：AgentFounder-30B 为 0.22，DeepSeek-V3.1 为 0.35，ReAct baseline 为 0.51。

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

- Repository note: 效用函数依赖模型组件——evidence grounding 用 NLI 模型、最终答案正确性用判定函数——因此评分继承了这些 judge 的可靠性。

## Related Works

- [FinTrace](./fintrace.md) — 同样做多维 trajectory 评估，但面向金融而非 deep research。
- [AgentBoard](./agentboard.md) — Trajectory 评估基于子目标进展率，而非 hierarchical utility function。
- [DeepResearch Bench](./deepresearch-bench.md) — 同样评估 deep research agent，但评价的是最终报告及其引用，而非 trajectory。Repository note: 它是一份独立的工作，只是与 TRACE 的配套任务集 "DeepResearch-Bench" 同名。
