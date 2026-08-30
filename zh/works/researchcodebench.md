# ResearchCodeBench (2025)

> [English](../../works/researchcodebench.md) | **简体中文**

## Overview

ResearchCodeBench 评测 LLM 实现新颖机器学习研究代码的能力：212 个编码挑战，要求把 2024–2025 年顶尖研究论文的前沿贡献翻译成可执行代码——即便最强模型（Gemini-2.5-Pro）也只正确实现 37.3%。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.02314>
- **Code:** <https://github.com/PatrickHua/ResearchCodeBench>
- **Project:** <https://researchcodebench.github.io/>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

ResearchCodeBench 瞄准一项抗污染的能力：实现发表于多数训练截止之后的、极近期论文的新颖贡献。其 212 个编码挑战要求模型把 2024–2025 年顶尖 ML 论文的前沿贡献翻译成可执行代码。在 30 多个闭源与开源 LLM 上，即便最强也不足 40%：Gemini-2.5-Pro-Preview 领先、37.3%，其后是 o3（High）32.3% 与 o4-mini（High）30.8%。一个抗污染子集（据项目页为 20 篇中的 13 篇）隔离真正的新颖性。

## Tasks

212 个把近期（2024–2025）ML 论文新颖贡献翻译成可执行代码的编码挑战；静态代码生成。全集覆盖 20 篇论文，含 13 篇的抗污染子集（项目页）。

## Domains

AI 与机器学习研究——ML 研究代码实现：把近期论文贡献变成可运行代码。

## Evaluation

- 实现论文贡献的成功率，配污染与错误模式分析。
- **报告。** 最强模型不足 40%：Gemini-2.5-Pro 37.3%、o3（High）32.3%、o4-mini（High）30.8%。

## Typical Duration

单次代码实现挑战（静态，非交互 agent 循环）。

## Main Contribution

一个立足于时效性、具备污染控制的「实现新颖研究代码」benchmark——测量模型能否构建最新想法，而非回忆背下来的。

## Key Design Ideas

- 截止之后的 2024–2025 论文使记忆不可行，隔离真正的实现能力。
- 抗污染子集显式把新颖性与可能的泄漏分开。
- 以可执行代码判分，使正确性取决于贡献能否真正运行，而非能否被描述出来。

## Strengths

- 多数代码 benchmark 缺乏的新近性与污染控制。
- 模型覆盖广（30+），仓库与项目页公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；arXiv 元数据无发表信息。20 篇/13 篇子集的细节出自项目页而非摘要。

## Related Works

- [ML-Bench](./ml-bench.md) — 同样是 ML 代码评估，在仓库级而非论文贡献级。
- [SUPER](./super.md) — 同样是研究代码执行，聚焦仓库搭建与复现。
- [PaperBench](./paperbench.md) — 同样是从论文实现研究，在完整复现尺度。
