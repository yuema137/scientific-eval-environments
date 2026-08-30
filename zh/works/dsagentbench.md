# DSAgentBench (2026)

> [English](../../works/dsagentbench.md) | **简体中文**

> **首次公开：** 2026-08-11 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.10366)

## Overview

DSAgentBench 是一个 benchmark，评估 agent 能否在真实计算机环境中自动化完整的端到端数据科学工作流，需要协同使用 notebook、IDE、终端、浏览器与数据库等工具。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.10366
- **Venue:** arXiv preprint（2026 年 8 月 11 日提交）

## Summary

DSAgentBench 面向长 horizon、贴近真实的数据科学实践，覆盖数据整理、探索、建模、可视化与验证。作者称它是首个评估 agent 能否在真实计算机环境中自动化完整数据科学工作流的 benchmark，与既有 benchmark 形成对比——后者缺少真实计算机交互，也不检验完整的端到端工作流。每个任务都要求让决策基于中间输出、并协同使用多种工具，且配一个确定性评估器。在 15 个闭源与开源模型上的实验揭示：当前 agentic 系统与真实数据科学工作流之间存在很大能力差距。

## Tasks

275 个多样任务，覆盖整条数据科学生命周期（数据整理、探索、建模、可视化与验证）。每个任务都要求让决策基于中间输出，并在真实操作环境中协同使用 notebook、IDE、终端、浏览器与数据库等工具。详细的任务构造方法与按阶段的任务拆分：TODO(reference)。

## Domains

在真实计算机/操作环境（notebook、IDE、终端、浏览器、数据库）中开展的通用数据科学工作流。摘要未逐一列举各任务的具体科学或应用领域；按领域的构成：TODO(reference)。

## Evaluation

每个任务都含一个确定性评估器，验证分析正确性、可视化输出与模型性能，而不只是检查代码能否执行。报告结果：在 15 个闭源与开源模型中，最强的 agent Claude-4.6-Sonnet 达到 56.70% 的任务成功率，而所有开源 agent 均低于 1%；报告的失败模式包括工具编排、OS grounding 与多步推理。完整的指标定义与按模型结果：TODO(reference)。

## Typical Duration

作者将其描述为长 horizon、多阶段、多工具的工作流。每任务的具体轨迹长度、wall-clock 时间或 token 预算：TODO(reference)。

## Main Contribution

作者将 DSAgentBench 呈现为首个评估 agent 能否在真实计算机环境中自动化完整端到端数据科学工作流的 benchmark，捕捉了以往 benchmark 遗漏的数据科学实践的多阶段、多工具特性，并为任务配上对分析正确性、可视化输出与模型性能的确定性评估器。

## Key Design Ideas

- 在真实计算机环境中执行，协同使用 notebook、IDE、终端、浏览器与数据库，而非孤立的代码片段。
- 覆盖整条数据科学生命周期：数据整理、探索、建模、可视化与验证。
- 任务要求让决策基于中间输出，并进行多步工具编排。
- 用确定性评估器验证分析正确性、可视化输出与模型性能，而非仅检查代码执行。

## Strengths

- 在真实计算环境中评估完整、长 horizon 的数据科学工作流，而非单步或仅代码的任务（摘要）。
- 对分析正确性、可视化输出与模型性能的确定性评估，提供了超越执行成功的客观评分（摘要）。
- 覆盖 15 个闭源与开源模型的广泛实证研究（摘要）。

## Limitations

- Repository note: 摘要未说明任务在数据科学生命周期各阶段或应用领域上的分布、任务构造出处，或确切的评估器指标；这些需全文核验。
- Repository note: 报告的评估提到一个模型（"Claude-4.6-Sonnet"），其标识符除摘要文本外无法对照一手来源核验；完整模型列表与配置需全文。

## Related Works

- [DSBench](./dsbench.md) —— 更早的数据科学 agent benchmark，聚焦数据分析与建模任务；DSAgentBench 将设定扩展到真实计算机环境中的完整端到端工作流。
