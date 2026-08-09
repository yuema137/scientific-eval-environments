# TPBench (2025)

> [English](../../works/tpbench.md) | **简体中文**

## Overview

TPBench（Theoretical Physics Benchmark）是关于 AI 理论物理推理能力的数据集与研究：57 道从本科到研究级的全新问题，覆盖高能理论与宇宙学，答案可自动验证，且不出自任何公开题库。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.15815>
- **Project:** <http://tpbench.org>
- **Venue:** Machine Learning: Science and Technology, 2025

## Summary

TPBench 瞄准考试物理与理论研究者真实工作之间的鸿沟：57 道问题均为新作——不取自公开题库——难度从本科一路延伸到研究级，领域为高能理论与宇宙学。论文正面处理这一层级上的自动验证与判分难题，并分析受评模型（o3-mini、o1、DeepSeek-R1、GPT-4o 及 Llama、Qwen 系列）的常见失败模式。研究级问题大多未被受评模型解出，作者据此认为当前模型对研究者的助益仍然有限。

## Tasks

57 道全新理论物理问题，从本科到研究级，覆盖高能理论与宇宙学；静态解题，答案可自动验证。

## Domains

理论物理：高能理论与宇宙学。

## Evaluation

- 面向理论物理推导定制的自动验证与判分；附失败模式分析。
- **报告。** 研究级问题大多未被受评模型解出。

## Typical Duration

单题理论推导；非交互式 agent 设定。

## Main Contribution

把可自动验证的物理评估推进到真正新颖的研究级理论问题，公开题库污染从构造上被排除。

## Key Design Ideas

- 问题以「新作」为标准编写，表现无法来自对已知解的检索。
- 在同一理论领域内铺设从本科到研究级的难度阶梯。
- 把符号化理论答案的自动验证当作设计问题正面解决，而非事后补丁。

## Strengths

- 理论物理内部的难度阶梯，而非单一难度档。
- 分数之外附有失败模式分析。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — 同样是研究者水平、机器判分的物理，领域为凝聚态理论。
- [CritPt](./critpt.md) — 同样是防污染的研究级物理挑战，横跨 11 个以上子领域。
- [UGPhysics](./ugphysics.md) — 同样是系统化的物理解题评估，在本科广度上配有规则加模型的判分流水线。
