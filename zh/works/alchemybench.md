# AlchemyBench (2025)

> [English](../../works/alchemybench.md) | **简体中文**

## Overview

AlchemyBench 是 LLM 驱动材料合成的端到端 benchmark，建立在 17,000 条经专家核验的开放文献合成配方之上：模型预测原料与设备、生成合成流程、预测表征结果，由专家水准的 LLM-as-a-Judge 框架判分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.16457>
- **Venue:** arXiv preprint (cs.CL), 2025

## Summary

论文题为「Towards Fully-Automated Materials Discovery via Large-Scale Synthesis Dataset and Expert-Level LLM-as-a-Judge」。AlchemyBench 把 17,000 条经专家核验的合成配方变成端到端预测 benchmark。给定目标，模型预测原料与设备、生成合成流程、预测表征结果。由于自由文本配方难以精确匹配判分，该 benchmark 配了一个 LLM-as-a-Judge 评估框架，作者称其与专家评判有很强的统计一致性。

## Tasks

对 17,000 条专家核验配方的端到端合成预测：原料与设备预测、合成流程生成、表征结果预测；静态预测，非交互。

## Domains

材料科学——无机材料合成规划，从前体与设备选择到流程与预期表征。

## Evaluation

- 对自由文本预测的 LLM-as-a-Judge 判分，作者称与专家评判有很强的统计一致性。
- **报告。** 摘要无数值头条；贡献是数据集加经验证的 judge 框架。

## Typical Duration

单回合的端到端合成预测；无交互式设定。

## Main Contribution

一个配方级规模的合成规划 benchmark，配一个对照专家验证过的 judge——让精确匹配行不通的自由文本合成预测变得可判分。

## Key Design Ideas

- 配方级规模的专家核验数据把任务锚定在真实合成实践上。
- 把任务分为原料/设备、流程、表征三部分，给出部分得分结构。
- 用一个经专家一致性验证的 LLM judge 处理开放式输出。

## Strengths

- 支撑端到端任务的大型专家核验配方语料。
- judge 所报告的专家一致性针对合成判分的核心难题。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；论文在审、无正式发表信息，arXiv 页面无法核实代码/数据集 URL。该 benchmark 依赖 LLM-as-a-Judge；其专家一致性为定性报告。

## Related Works

- [ChemCensor / CREED](./chemcensor.md) — 同样是合成相关（逆合成）评估，多个合法答案使精确匹配失效。
- [AutoDFT / VASPBench](./vaspbench.md) — 同样是材料工作流评估，在计算而非合成一侧。
- [Materials Hypothesis Generation](./materials-hypothesis.md) — 同样是 LLM 驱动的材料发现，处于假说而非合成阶段。
