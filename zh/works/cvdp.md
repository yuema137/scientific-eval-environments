# CVDP (2025)

> [English](../../works/cvdp.md) | **简体中文**

> **首次公开：** 2025-06-17 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2506.14074)

## Overview

CVDP（Comprehensive Verilog Design Problems）是 NVIDIA 面向 LLM 与 agent 的下一代 RTL 设计与验证 benchmark：783 个问题、13 个任务类别——RTL 生成、验证、调试、规格对齐与技术问答——兼有非 agent 与 agent 两种格式，最先进的模型在代码生成上 pass@1 不超过 34%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.14074>
- **Code:** <https://github.com/NVlabs/cvdp_benchmark>
- **Dataset:** <https://huggingface.co/datasets/nvidia/cvdp-benchmark-dataset>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

CVDP 把碎片化的 RTL benchmark 格局整合为一套综合套件：783 个问题、13 个任务类别，横跨 RTL 生成、验证、调试、规格对齐与技术问答。关键在于每个问题都有非 agent 格式（单次、固定输入输出）与 agent 格式（多步、与工具和仓库交互）两种，从而同一任务同时测量模型与 agent。最先进的模型在代码生成上 pass@1 不超过 34%，其中 agent 化任务尤其困难。框架运行在基于 Docker 的开源仿真镜像上（cocotb、Icarus Verilog、Yosys、Verilator），保留参考解以抑制污染，并已被 Si2 LLM Benchmarking Coalition 采纳。

## Tasks

783 个问题 / 13 个类别（RTL 生成、验证、调试、规格对齐、技术问答），兼有非 agent 与 agent 格式；既有静态生成，也有交互式工具/仓库 agent。

## Domains

电气工程——数字设计与验证：综合的 RTL 设计、调试与验证。

## Evaluation

- pass@1，在容器化仿真环境中用开源工具与模型评分基础设施判分。
- **报告。** 最先进的模型在代码生成上 pass@1 不超过 34%；agent 化任务尤其困难。

## Typical Duration

非 agent 任务单次完成；agent 任务为多步、与工具/仓库交互的回合。

## Main Contribution

一个横跨设计、验证与调试、并在同一批任务上同时评测模型与 agent 的综合 RTL benchmark，配有污染控制与业界采纳。

## Key Design Ideas

- 非 agent/agent 双格式，在同一任务上分别测量模型与 agent。
- 保留参考解加部分发布策略，抑制训练污染。
- 容器化的开源 EDA 栈使评估可复现。

## Strengths

- 按任务类别覆盖最广的 RTL benchmark，出自 NVIDIA，框架与数据集公开。
- SOTA 上限低（pass@1 ≤34%）留下清晰可测的空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv 元数据无发表信息（ICLAD'25 的说法未核实）。公开发布省略了部分数据点并保留参考解。

## Related Works

- [VerilogEval](./verilogeval.md) — 同样是 RTL 生成评估，范围更窄、以仿真判分。
- [FVEval](./fveval.md) — 同样是硬件验证评估，聚焦形式验证。
- [RTLLM](./rtllm.md) — 同样是设计级 RTL 生成，不含验证与 agent 化范围。
