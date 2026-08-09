# IdeaBench (2024)

> [English](../../works/ideabench.md) | **简体中文**

## Overview

IdeaBench 为研究想法生成评测 LLM：把 LLM 设定为特定领域的研究者、以人类研究者所用的同样上下文——有影响力论文的标题与摘要及其参考文献——为其提供依据，并用结合 GPT-4o 排序与相对「Insight Score」的两阶段框架评估所生成的想法。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.02429>
- **Venue:** arXiv preprint (cs.CL), 2024

## Summary

IdeaBench 把研究构思当作可评估任务：它把 LLM 以人类会有的上下文——有影响力论文的标题与摘要及其参考文献——设定为特定领域研究者，并要其生成新研究想法。评估分两阶段：GPT-4o 先按用户指定的质量指标（如新颖性与可行性）为想法排序，再由相对排名的「Insight Score」量化质量。IdeaBench 同时提供数据集与这一评估框架，作为跨模型比较构思的可复现方式。

## Tasks

以有影响力论文的标题/摘要及其参考文献为依据的研究想法生成；静态单轮生成，由两阶段框架评分。

## Domains

AI 与机器学习研究——研究构思：在科学上下文中生成新颖研究想法。

## Evaluation

- 两阶段：GPT-4o 按新颖性/可行性指标排序，再算相对「Insight Score」。
- **报告。** 摘要无单一头条数字；贡献是数据集加评估框架。

## Typical Duration

每个上下文单轮想法生成；无交互式设定。

## Main Contribution

一个可复现的「数据集加框架」，用于评测 LLM 研究构思——把模型基于真实研究上下文，并按新颖性与可行性而非临时审读为想法评分。

## Key Design Ideas

- 以有影响力论文与参考文献为依据，对应研究者真实的起点上下文。
- 「先排序、再 Insight Score」的两阶段设计把模糊的「想法质量」变成指标。
- 分开新颖性与可行性指标，避免把不同判据揉在一起。

## Strengths

- 研究想法生成最早的结构化 benchmark 之一，配明确评估协议。
- Insight Score 给出跨模型可比的相对度量。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；arXiv 页面无法核实发表信息与官方代码/数据集 URL（标为 TODO(reference)）；规模数字（模型、数据集大小）摘要未载明。

## Related Works

- [LiveIdeaBench](./liveideabench.md) — 同样是研究想法生成，从极简的单关键词上下文出发。
- [MLR-Bench](./mlr-bench.md) — 同样评估想法生成阶段，在完整研究流程内。
- [MLGym](./mlgym.md) — 同样演练假设/想法生成，作为 AI 研究循环的一环。
