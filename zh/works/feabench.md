# FEABench (2025)

> [English](../../works/feabench.md) | **简体中文**

## Overview

FEABench 评估 LLM 与 LLM agent 能否用有限元分析（FEA）端到端地求解物理、数学与工程问题：对自然语言问题描述进行推理，并通过 API 操作 COMSOL Multiphysics® 计算出答案。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.06260>
- **Code:** <https://github.com/google/feabench>
- **Venue:** NeurIPS 2024 Workshops（Mathematical Reasoning and AI；Open-World Agents）

## Summary

FEABench 把专业仿真软件本身作为评估面：解题意味着通过 API 调用驱动 COMSOL Multiphysics®，而不是给出闭式答案。论文还设计了一个 agent，它通过 API 与软件交互、检查软件输出，并借助工具在多轮迭代中改进解答。表现最好的策略生成的 API 调用有 88% 可执行。

## Tasks

以自然语言给出的多物理场问题，通过 API 操作 COMSOL Multiphysics® 端到端求解；agentic 设定下对照软件反馈迭代 API 调用。具体任务数为 TODO(reference)。

## Domains

基于有限元分析的多物理场仿真，覆盖物理、数学与工程问题。

## Evaluation

- 对生成的 API 调用与计算答案的综合评估方案；API 调用可执行率是主要指标之一。
- **报告。** 表现最好的策略生成的 API 调用有 88% 可执行。

## Typical Duration

对照 FEA 软件反馈的「交互—检查—改进」迭代循环；单任务预算为 TODO(reference)。

## Main Contribution

把物理仿真评估搬到真实的专业软件上：所测的是端到端操作工业级 FEA 工具的能力，而不是模仿其输出的能力。

## Key Design Ideas

- 软件 API 即动作空间，评估捕捉的是工具操作能力，而不只是物理知识。
- 对照软件输出迭代改进，使设定是 agentic 的，而非一次性代码生成。
- API 调用可执行率提供客观、可自动检查的进度信号。

## Strengths

- 用的是真实工业仿真软件，而非专门搭建的沙箱。
- 88% 的可执行率与困难得多的端到端求解形成对照，指出难点真正所在。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — 同样评估操作专业仿真软件（OpenFOAM），带物理收敛性检查。
- [Frontier-Eng](./frontier-eng.md) — 同样让 agent 在交互预算内对照工业级仿真器循环迭代。
- [SimulCost](./simulcost.md) — 同样是物理仿真评估，聚焦资源成本下的参数调优。
