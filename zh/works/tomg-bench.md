# Speak-to-Structure / TOMG-Bench (2024)

> [English](../../works/tomg-bench.md) | **简体中文**

## Overview

Speak-to-Structure（S²-Bench，最初名为 TOMG-Bench）评估 LLM 在开放域自然语言驱动的分子生成上的能力：分子编辑（MolEdit）、分子优化（MolOpt）、定制生成（MolCustom）三类任务——指令允许多个合法分子，答案按是否满足指令来检验，而非对照单一参考。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.14642>
- **Code:** <https://github.com/phenixace/S2-TOMG-Bench>
- **Dataset:** <https://huggingface.co/datasets/phenixace/S2-TOMG-Bench>
- **Venue:** KDD 2026

## Summary

文本到分子的评估大多是一对一：一条指令对应唯一参考答案。Speak-to-Structure 把它改成一对多——开放式指令下，任何满足要求的分子都算对——覆盖编辑、优化与定制生成三类任务。初版（TOMG-Bench）每类任务下设三个子任务、各 5,000 个测试样本；当前版本报告了对 31 个 LLM 的全面评测。论文还配套了大规模指令微调数据集 OpenMolIns，它让 Llama3.1-8B 在该 benchmark 上超过 GPT-4o 与 Claude-3.5。

## Tasks

三族开放域分子生成任务——MolEdit、MolOpt、MolCustom——按「是否满足指令」做一对多评估；初版共九个子任务、每个 5,000 个测试样本。静态单轮生成。

## Domains

化学——自然语言驱动的分子设计：编辑、性质优化与从头定制生成。

## Evaluation

- 对开放式生成结果做指令满足性检验（一对多），而非与单一参考做字符串匹配。
- **报告。** 31 个 LLM 参评；经 OpenMolIns 指令微调的 Llama3.1-8B 在 S²-Bench 上超过 GPT-4o 与 Claude-3.5。

## Typical Duration

每条指令单轮生成；无交互式设定。

## Main Contribution

让一对多评估成为文本驱动分子生成的默认范式——测模型是否满足化学约束，而不是能否复现一个被记住的参考答案。

## Key Design Ideas

- 开放域指令解除了「单一参考」对合法新分子的惩罚。
- 编辑/优化/生成的划分把局部结构操作与全局设计分开。
- 配套的 OpenMolIns 数据集证明 benchmark 揭示的差距是可训练的。

## Strengths

- 31 个模型的覆盖面，外加一个排行榜规模的公开数据集。
- 从 v1（2024）到更名后的正式版（KDD 2026），可以看到持续的维护。

## Limitations

- Repository note: 卡片依据 arXiv 摘要（v1 与 v4）及官方仓库编写（2026 年 8 月）。论文在版本间改过标题——TOMG-Bench（v1，2024）改为 Speak-to-Structure/S²-Bench（v4，2026）；每子任务 5,000 样本的数字出自 v1 摘要。

## Related Works

- [MolLangBench](./mollangbench.md) — 同样是语言提示的分子操作，识别任务由化学信息学工具验证。
- [ChemCoTBench](./chemcotbench.md) — 同样考分子编辑与优化，评估深入到推理步骤层面。
- [ChemCensor / CREED](./chemcensor.md) — 同样用「多个合法答案」的评估取代单参考精确匹配，在逆合成方向。
