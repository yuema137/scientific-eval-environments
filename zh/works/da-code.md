# DA-Code (2024)

> [English](../../works/da-code.md) | **简体中文**

> **首次公开：** 2024-10-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2410.07331)

## Overview

DA-Code 是面向 agent 的数据科学代码生成 benchmark：在可控、可执行的沙箱环境中做复杂的数据整理、分析与代码生成任务，即便当前最强 LLM 也只达到 30.5% 的准确率。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.07331>
- **Code:** <https://github.com/yiyihum/da-code>
- **Venue:** EMNLP 2024

## Summary

DA-Code 瞄准 agent 做数据科学时真正要写的代码：需要依据数据并规划的高难度数据整理、分析与建模任务，在可控的 Docker 沙箱中执行。配套的 DA-Agent 基线迭代地生成并运行数据科学代码。尽管胜过既有框架，最强 LLM 也只达到 30.5% 的准确率，表明 agent 式数据科学编码仍有很大空间。

## Tasks

agent 式数据科学编码任务——数据整理、分析与代码生成——在可控 Docker 沙箱环境中执行。确切任务数量为 TODO(reference)——摘要未载明。

## Domains

AI 与机器学习研究——数据科学：用于数据整理与分析的可执行代码生成。

## Evaluation

- 可控沙箱中基于执行的准确率，配 DA-Agent 基线。
- **报告。** 最强 LLM 只达到 30.5% 的准确率，高于既有框架但远未解决。

## Typical Duration

沙箱中每个任务一段迭代的「生成-执行」回合。

## Main Contribution

一个基于执行的数据科学编码 benchmark，要求真实的整理与分析代码而非答案——配沙箱验证。

## Key Design Ideas

- 可控可执行环境使正确性取决于运行代码，而非评判文本。
- 复杂的整理与分析需要依据数据并规划，而非一次性生成。
- DA-Agent 基线为任务确立具体参照。

## Strengths

- 在真实感数据科学编码上基于执行评分。
- 发表信息经核实（EMNLP 2024），仓库公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；确切任务数量摘要未载明，标为 TODO(reference)。

## Related Works

- [DSBench](./dsbench.md) — 同样是数据科学 agent 评估，覆盖分析与建模任务。
- [BLADE](./blade.md) — 同样是数据驱动科学分析，对照专家真值评估。
- [ML-Bench](./ml-bench.md) — 同样是以代码为中心的 ML 评估，在仓库级。
