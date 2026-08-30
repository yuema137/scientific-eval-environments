# GeoNatureAgent Benchmark (2026)

> [English](../../works/geonatureagent-benchmark.md) | **简体中文**

> **首次公开：** 2026-06-11 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.12821)

## Overview

GeoNatureAgent Benchmark 是一个通过对生产级（production-style）API 的结构化工具调用来评估 LLM agent 环境地理空间分析能力的 benchmark。它包含 18 个类别共 93 个任务，运行于一个开放、可自托管的 API 之上，该 API 通过 16 个工具提供覆盖西班牙与葡萄牙的三种环境指标。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12821>
- **Code:** <https://github.com/gabrielireland/GeoNatureAgent_Benchmark>

## Summary

GeoNatureAgent Benchmark 认为环境科学家在数据整理上花费了不成比例的精力，而现有 benchmark 均未评估通过结构化工具调用操作真实地理空间 API 的 agent。作者将其定位为首个面向经由结构化工具调用使用生产级地理空间 API 的环境分析 agent 的 benchmark，并通过在西班牙 CO2 与侵蚀指标之外集成葡萄牙 BigEarthNet V2 土地覆盖展示了可扩展性。在三个 temperature 1.0 种子下评估的七个 LLM 中，Claude Sonnet 4 以 60.8% ± 0.8% 领先，成本–准确率 Pareto 前沿主要由开放权重模型占据，近值比较任务在所有模型上均为 0%。

## Tasks

93 个任务，分为 18 个类别，覆盖市镇分析、多轮对话、空间推理、跨指标综合、错误处理与恢复、排序、比较、多语言理解、栖息地分析与任务拒绝；错误处理任务被有意设计为不可解，以测试得体拒绝的能力。按类别（Table 1）：Tool selection 21、Cross-indicator 8、Interpretation 7、Habitat analysis 7，其余 14 个类别各含 1–6 个任务。每个任务给定自然语言查询（可含多轮历史）、期望的工具调用、必含 / 禁含（must-contain / must-not-contain）字符串、最大轮次预算、成本预算与领域专家提供的 ground truth；除这一逐任务规格外，论文未描述任务的编写过程。

## Domains

西班牙与葡萄牙范围内的环境地理空间分析：CO2 吸收适宜性（类别型，西班牙）、冲沟侵蚀概率（连续型）与 BigEarthNet V2 土地覆盖（类别型，葡萄牙）。

## Evaluation

- **逐案例二元通过。**每案例经八项机械式检查（mechanistic checks）评定，不使用 LLM-as-judge：期望的工具全部被调用、期望的动作全部生成、必含关键词出现、禁含关键词未出现、数值在容差内（默认 ±2 个百分点）、按要求生成图表、轮次预算未超出；成本检查仅记录，不计入二元能力得分。
- **部分得分诊断。**check score（每案例通过检查的比例）、tool F1、keyword coverage 与 cost utilization 作为二元指标的补充。
- **错误分类体系。**每个失败按固定优先级归因于第一个未通过的检查：工具缺失、图表缺失、数据错误、轮次超限、关键词缺失、出现禁含关键词。
- **报告结果。**在 Claude Sonnet 4、DeepSeek V3.2、GLM-5、Gemini 2.5 Pro、Qwen3-235B、GPT-OSS-120B 与 Llama 4 Scout 上：Claude Sonnet 4 以 60.8% ± 0.8% 领先（每案例 $0.127）；DeepSeek V3.2 达 56.3% ± 3.1%、每案例 $0.011——以低 11 倍的成本提供 Claude 93% 的能力——其余模型均未超过 51%；近值比较任务在所有模型上均为 0%，且准确率比通用 GIS benchmark 低 25–35 个百分点。论文未报告人类 baseline。

## Typical Duration

运行上限为 10 个 agent 循环轮次、每次模型调用 4,096 个输出 token；每个任务另带默认 $0.10 的每案例成本预算，仅记录、不作为门槛。未说明 wall-clock 限制。

## Main Contribution

一个通过对生产级、可自托管地理空间 API 的结构化工具调用来评估环境分析 agent 的 benchmark，将能力与每案例成本作为正交轴报告。

## Key Design Ideas

- 针对真实、可自托管的 16 工具地理空间 API（12 个主要操作加 4 个辅助工具）进行结构化工具调用，而非代码生成或模拟环境。
- 机器可检验的任务规格——期望的工具调用、必含 / 禁含字符串、数值容差、轮次与成本预算——使评分完全自动化。
- 有意不可解的错误处理任务与任务拒绝覆盖，以测试得体拒绝。
- 每个模型在 temperature 1.0 下取三个随机种子，暴露 tool-use 可靠性的运行间方差。

## Strengths

- 机械式检查避免了 LLM-judge 方差，同时仍覆盖多轮、多语言与跨指标行为。
- 能力与成本两条正交轴揭示出主要由开放权重模型占据的 Pareto 前沿。
- 可自托管 API 与公开 harness 支持复现与扩展，并已通过集成葡萄牙 BigEarthNet V2 土地覆盖得到演示。

## Limitations

- Repository note: 覆盖范围为两个国家与三个环境指标——任务套件向其他地区、指标类型或 API 的迁移仅由单次 BigEarthNet V2 扩展演示。
- Repository note: 18 个类别中若干类别任务极少（Comparison 2、Ranking 2、Temporal change 1），因此各类别层面的发现——包括近值比较 0% 这一结论——基于小样本。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样在真实科学数据分析任务（含地理信息科学）上评估 agent，但将输出统一为自包含的 Python 程序并以执行打分，而非对真实 API 的结构化工具调用。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样以确定性的程序化检查为科学工作流打分，但采用容器内 pytest 覆盖五大领域，而非针对地理空间 API 的工具调用与关键词检查。
- [SimulCost](./simulcost.md) — 同样将成本作为科学 agent 评估的一级维度，但计价的是物理仿真参数调优中的仿真时间与实验资源，而非 API 驱动分析的每案例美元成本。