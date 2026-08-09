# RealPDEBench (2026)

> [English](../../works/realpdebench.md) | **简体中文**

## Overview

RealPDEBench 是把真实世界测量数据与配对数值模拟整合在一起的科学机器学习 benchmark——论文称其为此类中的首个——包含五个数据集、三类任务、八项指标与十个基线。其评估对象是科学 ML 模型而非 LLM agent（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.01829>
- **Code:** <https://github.com/AI4Science-WestlakeU/RealPDEBench>
- **Dataset:** <https://huggingface.co/datasets/AI4Science-WestlakeU/RealPDEBench>
- **Project:** <https://realpdebench.github.io/>
- **Venue:** ICLR 2026 (oral)

## Summary

RealPDEBench 直指复杂物理系统科学 ML 的一个瓶颈：真实测量数据昂贵稀缺，模型几乎都在模拟数据上训练与验证，这既限制了评估，也阻碍了 sim-to-real 迁移研究。该 benchmark 提供五个带配对模拟数据的真实测量数据集，覆盖不同的复杂物理系统；定义三类任务，支持真实数据与模拟数据的对比以及弥合两者的方法研究；并用横跨数据导向与物理导向的八项指标评分。在十个基线上的实验揭示了模拟数据与真实数据之间的显著差异，同时表明用模拟数据预训练能稳定提升精度与收敛速度。

## Tasks

五个带配对数值模拟的真实测量数据集——流固耦合、受控圆柱、圆柱、翼型与燃烧（据官方项目页）——以及三类任务，支持真实与模拟数据的对比和弥合方法的研发。

## Domains

复杂物理系统：流固耦合、圆柱与翼型绕流、燃烧，配有成对的真实测量与数值模拟数据。

## Evaluation

- 八项指标横跨**数据导向**（据官方项目页，如 RMSE、相对 L₂）与**物理导向**（如 Fourier 误差、动能）两类。
- 十个基线：最先进模型、预训练 PDE 基础模型与一种传统方法。
- **报告。** 模拟数据与真实数据之间存在显著差异；用模拟数据预训练能稳定提升精度与收敛速度。

## Typical Duration

N/A——在固定数据集上离线训练与评估模型；非交互式 agent 设定。

## Main Contribution

通过把昂贵的真实测量与同一物理系统的数值模拟在共享任务与指标下配对，使科学 ML 的 sim-to-real 差距本身成为可度量对象。

## Key Design Ideas

- 每个真实数据集都配有成对的模拟数据集，真实-模拟对比是内建能力而非事后补充。
- 物理导向指标与数据导向指标并列，物理合理性被计入评分，而不只是逐点误差。
- 基线池刻意从预训练 PDE 基础模型一路覆盖到传统方法，锚定方法谱系的两端。

## Strengths

- 昂贵的真实测量数据——论文点名的领域瓶颈资源——正是该 benchmark 的核心资产。
- 配对设计直接支持 sim-to-real 迁移研究，而不只是记录差距。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目页编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: RealPDEBench 评估的是科学 ML 代理模型（surrogate model），而非 LLM agent；收录于此是因为其评估方法学——真实/模拟配对划分与物理导向指标——与科学 agent 的验证方式直接相关。

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — 同样以物理为根基验证流体力学能力，但面向 LLM 与 coding agent 而非代理模型。
- [SimulCost](./simulcost.md) — 同样把评估建立在物理仿真器上，但增加的是成本意识而非真实测量数据。
- [MaD Physics](./mad-physics.md) — 同样评估物理系统演化的预测，但在模拟环境中，而 RealPDEBench 贡献的是真实测量数据。
