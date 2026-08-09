# SciCode (2024)

> [English](../../works/scicode.md) | **简体中文**

## Overview

SciCode 是由科学家整理的科研编码 benchmark：80 个高难度主问题分解为 338 个子问题，构建过程汇集了 16 个自然科学子领域的科学家与 AI 研究者的输入，主领域涵盖数学、物理、化学、生物与材料科学。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.13168>
- **Code:** <https://github.com/scicode-bench/SciCode>
- **Dataset:** <https://huggingface.co/datasets/SciCode1/SciCode>
- **Project:** <https://scicode-bench.github.io/>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks（据官方仓库）

## Summary

SciCode 的问题来自真实科研：每个主问题自然分解为若干子问题，各自混合知识回忆、推理与代码合成，另有可选的科学背景描述来控制提供多少领域知识。评估对照科学家标注的金标准解与测试用例执行。在最接近真实的设定下，受评模型中表现最好的 Claude 3.5 Sonnet 只解出 4.6% 的主问题。

## Tasks

80 个科研编码主问题，分解为 338 个子问题，横跨 16 个自然科学子领域；每个子问题混合知识回忆、推理与代码合成，配可选背景描述。

## Domains

16 个自然科学子领域，点名的主领域为数学、物理、化学、生物与材料科学。

## Evaluation

- 在子问题与主问题两级，对照科学家标注的金标准解与测试用例执行评估。
- **报告。** 受评模型中最好的 Claude 3.5 Sonnet 在最接近真实的设定下只解出 4.6% 的主问题。

## Typical Duration

每个主问题为多子问题的代码生成回合；非交互式 agent 设定。

## Main Contribution

把科学家整理的科研代码作为评估对象，其分解结构显示：模型即使具备子问题能力，也难以把它们组合成完整的科研解答。

## Key Design Ideas

- 问题由科学家出题并标注，难度反映科研实践而非考试惯例。
- 主问题/子问题的分解把「组合失败」与「单元失败」分开。
- 可选背景描述使所提供的领域知识成为实验变量。

## Strengths

- 金标准解与测试来自 16 个子领域的一线科学家。
- 4.6% 的真实设定得分立起了一个早期而可信的科研编码基线。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。这些来源未给出问题在各子领域的分布。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样是专家验证、源自真实科研的代码任务，统一为可执行 Python 程序。
- [NatureBench](./naturebench.md) — 同样以已发表研究的标准要求 coding agent，通过对标 SOTA。
- [MDArena](./mdarena.md) — 同样是源自科研的科学计算，容器化于单一模拟模态。
