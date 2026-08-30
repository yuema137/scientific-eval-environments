# HydroAgent (2026)

> [English](../../works/hydroagent.md) | **简体中文**

> **首次公开：** 2026-05-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.17792)

## Overview

HydroAgent 评测九个前沿 LLM agent 对业务化 CREST 分布式水文模型——美国国家气象局用于山洪预报——的参数率定能力，在流域面积 329–40,792 km² 的四个留出测站上以 Nash–Sutcliffe 效率（NSE）对照人类专家参照打分。论文配套的 RL 训练 agent 属于方法贡献（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.17792>
- **Venue:** arXiv preprint (cs.LG, physics.geo-ph), 2026

## Summary

率定分布式水文模型意味着读懂过程线特征，并把它们转译成高维参数调整，以在线 CREST 模拟作为反馈。九个前沿 agent 的二十轮最优 NSE 从 −0.16（GPT-5.4）到 0.75（Sonnet 4.6）不等，除 Opus 4.7 在一个测站外，没有模型达到人类专家参照。论文随后用 2,576 条专家率定轨迹对 Qwen3-4B 做监督微调，并以 NSE 为可验证奖励、用模拟器反馈做强化学习——该训练贡献不在本卡片范围内。

## Tasks

对业务化 CREST 模型在四个留出测站（329–40,792 km²）上的迭代率定：解读过程线行为、调整分布式参数、重新模拟；每站最多二十轮取最优。

## Domains

水文学与地球系统科学：径流模拟与业务化山洪预报基础设施。

## Evaluation

- 留出测站上的 Nash–Sutcliffe 效率（NSE），对照人类专家率定参照；NSE 同时充当配套训练工作的可验证奖励。
- **报告。** 九个前沿 agent 的 NSE 从 −0.16（GPT-5.4）到 0.75（Sonnet 4.6）；除 Opus 4.7 在一个测站外无模型达到专家参照。

## Typical Duration

迭代的「模拟-调整」率定回合，每站最多二十轮。

## Main Contribution

让前沿 agent 面对一个业务化预报模型和一把职业标尺——人工率定的专家结果——并发现差距是真实的：瓶颈在于特征解读与参数推理，而不是工具。

## Key Design Ideas

- 目标是业务运行中的模型（CREST/NWS），能力高低有直接的业务含义。
- NSE 为每次率定尝试给出无歧义、可由模拟验证的分数。
- 跨三个数量级流域面积的留出测站测的是迁移，而非背下来的流域。

## Strengths

- 在真正业务化的基础设施上与专家参照直接比较。
- −0.16 到 0.75 的分布表明在物理率定任务上模型选择起决定作用。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。
- Repository note: HydroAgent 的 RL 微调（2,576 条专家轨迹的 SFT + 以模拟器反馈为依据的 GRPO）属于训练贡献，超出本仓库范围；本卡片记录其 agent benchmark。

## Related Works

- [SimulCost](./simulcost.md) — 同样把仿真参数调优作为受评技能，带资源成本。
- [GeoNatureAgent Benchmark](./geonatureagent-benchmark.md) — 同样是环境领域的 agent 评估，配机制性检查。
- [Frontier-Eng](./frontier-eng.md) — 同样是对照专业仿真器、约束之下的迭代优化。
