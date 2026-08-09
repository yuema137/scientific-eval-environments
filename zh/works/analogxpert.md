# AnalogXpert (2024)

> [English](../../works/analogxpert.md) | **简体中文**

## Overview

AnalogXpert 是把电路设计专长注入大语言模型、自动完成模拟拓扑综合的 LLM agent：以 SPICE 代码表示拓扑，通过链式思维与上下文学习把设计分解为模块选择与模块连接，在含 30 个真实与 2,000 个合成案例的 benchmark 上达到 40% / 23% 的成功率，而 GPT-4o 仅 3%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.19824>
- **Venue:** arXiv preprint (cs.AR), 2024

## Summary

AnalogXpert 把模拟设计师的工作流编码进 LLM agent：模拟拓扑以 SPICE 代码表示，子电路库缩小设计空间，任务被分解为模块选择与模块连接两个子任务，用链式思维与上下文学习处理，再以查错策略做增量纠错。在一个专建的 30 个真实 + 2,000 个合成设计案例 benchmark 上，它在合成上达 40%、真实上达 23% 的成功率，远高于 GPT-4o 在两者上的 3%。

## Tasks

在 30 个真实 + 2,000 个合成案例上做模拟拓扑综合；agent 选择模块并连接（以 SPICE 代码），带迭代查错——agent 化，非静态问答。

## Domains

电气工程——模拟与混合信号设计：电路拓扑综合。

## Evaluation

- 单次正确性：合成案例由自动结构规则程序检查；真实案例由人工评审核对所有块与连接是否与需求完全一致。
- **报告。** AnalogXpert 合成 40%、真实 23% 成功率，对比 GPT-4o 两者均 3%。

## Typical Duration

每个设计一段「模块选择-模块连接」的多步回合，带查错。

## Main Contribution

把模拟设计专长——子电路库与「先选后连」的分解——编码进 LLM agent，并配一个足够大（2,000+ 案例）以可靠测量拓扑综合的 benchmark。

## Key Design Ideas

- 以 SPICE 代码表示拓扑，给 LLM 一个可执行目标。
- 分解为模块选择与模块连接，契合模拟设计师的工作方式。
- 查错步骤增量纠正结构错误，而非一次成型。

## Strengths

- 大规模合成集加真实设计，使拓扑成功可测量而非轶事。
- 40%/23% 对 3% 的差距表明是专长编码而非纯规模带来提升。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与全文编写（2026 年 8 月）；arXiv 元数据无发表信息，arXiv 页面无法核实任何官方代码/数据集仓库。

## Related Works

- [AnalogCoder](./analogcoder.md) — 同样是面向模拟设计的 LLM agent，走免训练的 Python 代码生成。
- [MMCircuitEval](./mmcircuiteval.md) — 同样含模拟电路评估，为多模态问答。
- [EEE-Bench](./eee-bench.md) — 同样含模拟在内的 EE 设计评估，为多模态问题求解。
