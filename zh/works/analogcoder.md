# AnalogCoder (2024)

> [English](../../works/analogcoder.md) | **简体中文**

## Overview

AnalogCoder 是首个通过 Python 代码生成来设计模拟电路的免训练 LLM agent，采用反馈增强的自纠正流程与可复用的电路工具库；在一个精选的模拟电路设计任务 benchmark 上，它成功设计出 20 个电路——比标准 GPT-4o 多 5 个。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.14918>
- **Code:** <https://github.com/laiyao1/AnalogCoder>
- **Venue:** AAAI 2025（Oral）（据官方仓库；arXiv 元数据无发表信息）

## Summary

模拟电路设计难以套用数字硬件那套代码生成配方，AnalogCoder 以免训练方式应对：一个 LLM agent 生成构建模拟电路的 Python 代码，经反馈增强的自纠正流程与领域专用提示迭代，并把可复用的模块化子电路存入工具库。在一个精选的模拟设计任务 benchmark（官方仓库 24 个任务）上，它成功设计出 20 个电路——比标准 GPT-4o 多 5 个。

## Tasks

在一个精选任务集（官方仓库 24 个任务）上做模拟电路设计；agent 生成并自纠正构建电路的 Python 代码——agent 化，非静态问答。

## Domains

电气工程——模拟电路设计：经由代码生成的拓扑构建。

## Evaluation

- Pass@1 / Pass@5，按解出任务数排名（官方仓库指标）。
- **报告。** AnalogCoder 成功设计 20 个电路，比标准 GPT-4o 多 5 个。

## Typical Duration

每个电路一段「生成-自纠正」的迭代回合。

## Main Contribution

首个面向模拟电路设计的免训练 agent 方法——配一个可复用任务 benchmark 与一个把已解子电路变成基础模块的工具库。

## Key Design Ideas

- 借反馈与领域提示实现免训练，规避稀缺的模拟训练数据。
- 电路工具库把已解子电路复用为模块化组件。
- 生成 Python 代码把设计锚定在可执行、可检验的表示上。

## Strengths

- 无需微调即在「解出电路数」上胜过 GPT-4o。
- 随 agent 一同提供可复用的精选 benchmark。

## Limitations

- Repository note: 该论文的头号贡献是 AnalogCoder agent；精选任务集是其配对 benchmark，本卡片以 benchmark 为中心。24 个任务数、Pass@k 指标与 AAAI 2025 Oral 发表信息由官方仓库声明，arXiv 元数据未载明。

## Related Works

- [AnalogXpert](./analogxpert.md) — 同样是面向模拟设计的 LLM agent，聚焦拓扑综合、benchmark 更大。
- [MMCircuitEval](./mmcircuiteval.md) — 同样含模拟电路评估，为多模态问答而非设计。
- [ControlAgent / ControlEval](./controleval.md) — 同样是面向电气设计任务的 LLM agent，在控制系统。
