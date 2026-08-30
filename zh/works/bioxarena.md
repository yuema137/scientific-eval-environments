# BioXArena (2026)

> [English](../../works/bioxarena.md) | **简体中文**

> **首次公开：** 2026-05-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.15766)

## Overview

BioXArena 在多模态生物医学机器学习任务上评测 LLM agent：76 个端到端任务横跨 9 个领域——序列建模、单细胞分析、结构生物学、网络生物学、化学生物学、扰动动力学、表型-疾病建模、生物医学影像与文本整合学习——在标准化的 2 小时单 GPU 环境中运行。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [建模与预测](../activities/modeling_prediction.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.15766>
- **Code:** <https://github.com/mbzuai-ai4bio/BioXArena>
- **Dataset:** <https://huggingface.co/datasets/mbzuai-ai4bio/BioXArena-Data-Public>
- **Project:** <https://mbzuai-ai4bio.github.io/BioXArena-ProjectPage/>
- **Venue:** arXiv preprint (cs.CE), 2026

## Summary

BioXArena 的 agent 须编写可执行代码、训练预测模型，并针对私有测试样本生成提交——在取自一手生物医学来源的数据上跑完整的 ML 工程循环。统一评估框架用隐藏标签、留出判分器与归一化到 0–1 的生物学感知指标打分。在 11 种 agent 配置中，MLEvolve 配 Gemini-3.1-Pro 以 0.666 的平均分最高，GPT-5.4 以 0.636 次之，而没有任何一个 agent 在所有领域都占优。

## Tasks

76 个端到端生物医学 ML 任务，横跨 9 个领域；agent 在标准化的 2 小时单 GPU 预算内对私有测试样本建模并提交。

## Domains

九个生物医学领域：序列建模、单细胞分析、结构生物学、网络生物学、化学生物学、扰动动力学、表型-疾病建模、生物医学影像与文本整合学习。

## Evaluation

- 隐藏标签加留出判分器；生物学感知指标归一化到 0–1。
- **报告。** 11 种 agent 配置中最高平均分 0.666（MLEvolve 配 Gemini-3.1-Pro），次之 0.636（GPT-5.4）；没有 agent 在所有领域占优。

## Typical Duration

每个任务为 2 小时单 GPU 回合（标准化算力预算）。

## Main Contribution

以标准化算力与隐藏标签评估「agent 作为生物医学 ML 工程师」，用按领域归一化的指标把九个异质生物学领域放到同一刻度上比较。

## Key Design Ideas

- 私有测试标签堵上了公开生物医学数据集留下的泄漏通道。
- 固定的 2 小时/单 GPU 预算让效率成为被测对象的一部分。
- 生物学感知指标先保证每个领域的分数有意义，再做归一化。

## Strengths

- 单一协议下覆盖九种生物医学模态的广度。
- 「无全能 agent」的发现提醒人们不要只读单一排行榜。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [MedAgentGym](./medagentgym.md) — 同样是规模化沙箱执行的生物医学编码，面向逐任务可验证真值。
- [AIRS-Bench](./airs-bench.md) — 同样是端到端 ML 研究任务，只看结果的执行评分。
- [AstaBench](./astabench.md) — 同样是标准化环境的科学评估，带成本核算。
