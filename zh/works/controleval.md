# ControlAgent / ControlEval (2024)

> [English](../../works/controleval.md) | **简体中文**

## Overview

ControlEval 是含 500 个、目标各异的控制系统设计任务的 benchmark，随 ControlAgent 一同发布——一个多 agent LLM 系统（中央、任务专用与 Python 计算 agent），通过迭代整定控制器参数自动完成控制设计，并胜过 LLM 基线与传统「工具箱+人工」基线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.19811>
- **Code:** <https://github.com/ControlAgent/ControlAgent>
- **Venue:** arXiv preprint (eess.SY), 2024

## Summary

控制系统设计是迭代的：提出控制器、检查调节时间与相位裕度、再整定。ControlAgent 用协作的 LLM agent 自动化这一循环——一个中央 agent、若干任务专用设计 agent、一个 Python 计算 agent，外加历史/反馈模块。它在 ControlEval 上评估——含 500 个控制任务，横跨一阶/二阶稳定与不稳定系统、含时滞系统与高阶系统，每个都有具体设计目标（调节时间、相位裕度稳健性）。ControlAgent 在各系统类型上维持高成功率，并胜过仅 LLM 与「工具箱+人工」基线。

## Tasks

500 个控制系统设计任务（ControlEval），横跨一阶/二阶稳定与不稳定系统、含时滞系统与高阶系统，各有具体设计判据；agent 迭代整定控制器——agent 化，非静态问答。

## Domains

电气工程——控制系统设计：为满足稳定性与性能规格而做控制器综合与整定。

## Evaluation

- 对照设计判据的平均成功率（ASR）与 agent 成功率（AgSR），并与仅 LLM 及传统「工具箱+人工」基线对照。
- **报告。** ControlAgent 在各系统类型上维持高成功率（如在含时滞一阶系统上以 97.2% 位列第二），胜过基线。

## Typical Duration

每个控制任务一段迭代式多 agent 设计回合，含反馈驱动的重整定。

## Main Contribution

用协作 LLM agent 端到端自动化控制系统设计——并配一个 500 任务的 benchmark（ControlEval），对照真实控制规格而非自由文本答案来评分。

## Key Design Ideas

- Python 计算 agent 把 LLM 锚定在真实的控制论计算上。
- 历史/反馈模块编码了控制工程师所用的迭代重整定循环。
- ControlEval 的任务分类覆盖经典系统类别、难度分级。

## Strengths

- 在成熟工程学科中胜过「工具箱+人工」基线，是很强的标杆。
- ControlEval 的 500 个按规格判分的任务使控制设计可客观评分。

## Limitations

- Repository note: 该论文的头号贡献是 ControlAgent 框架；ControlEval 是其配对 benchmark，本卡片以 benchmark 为中心。ControlEval 数据集位于 ControlAgent 仓库内（无单独发布）；arXiv 元数据无发表信息。

## Related Works

- [AnalogXpert](./analogxpert.md) — 同样是面向电气设计任务的 LLM agent，在模拟电路拓扑综合。
- [ElecBench](./elecbench.md) — 同样是电气领域的决策 benchmark，考电网调度。
- [Frontier-Eng](./frontier-eng.md) — 同样是仿真器下的迭代工程优化，覆盖更广的工程任务。
