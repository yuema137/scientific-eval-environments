# QMP-Bench (2026)

> [English](../../works/qmp-bench.md) | **简体中文**

> **首次公开：** 2026-03-31 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2604.00149)

## Overview

QMP-Bench 是含 100 个研究级、端到端量子多体模拟任务的 benchmark，任务提取自 21 种高影响力期刊。配套的 PhysVEC 多 agent 框架属于 agent 构建工作，与本仓库的评估重心相邻（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.00149>
- **Venue:** arXiv preprint (physics.comp-ph), 2026

## Summary

QMP-Bench 追问 AI 系统能否复现已发表的量子多体研究结果：100 个任务均为提取自 21 种高影响力期刊的端到端模拟问题，既要求代码正确，也要求结果在物理上成立。论文将 benchmark 与 PhysVEC 配对——一个通过编程验证器与科学验证器强制自我验证与纠错的多 agent 框架，在每一步产出可解释的证据与纠错；论文报告 PhysVEC 在 QMP-Bench 各场景上显著优于现有 LLM 基线，并具有良好的推理时扩展性。

## Tasks

100 个研究级、端到端量子多体模拟任务，提取自 21 种高影响力期刊。

## Domains

量子多体物理及其计算模拟方法。

## Evaluation

- 编程验证器检验代码正确性；科学验证器检验基于物理原理的有效性。
- **报告。** PhysVEC 在 QMP-Bench 各场景上显著优于现有 LLM 基线，推理时扩展性良好；具体数字为 TODO(reference)。

## Typical Duration

每个任务为端到端模拟工作流；单任务预算为 TODO(reference)。

## Main Contribution

把 agent 评估锚定到已发表的量子多体结果上，并把验证拆分为「代码正确」与「物理成立」两层，而非单一的通过信号。

## Key Design Ideas

- 任务提取自已发表的期刊结果，真值就是文献实际确立的结论。
- 双验证器把「代码跑对了」与「物理是对的」分开。
- 逐步验证产出可解释的证据，而不只是终局裁决。

## Strengths

- 任务来源覆盖 21 种期刊，达到研究级。
- 验证器拆分能把失败定位到软件层或物理层。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码或数据集发布。
- Repository note: 论文的第二项贡献 PhysVEC 属于 agent 实现，超出本仓库范围；本卡片记录其 benchmark。

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — 同样是专家级凝聚态/量子多体评估，但为 50 道机器判分的理论问题而非端到端模拟。
- [PRBench](./prbench.md) — 同样端到端复现已发表物理研究，覆盖 11 个子领域并带专家评分标准。
- [MDArena](./mdarena.md) — 同样是源自真实研究的容器化模拟工作流，面向分子动力学而非量子多体。
