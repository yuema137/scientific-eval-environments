# ScienceAgentBench (2024)

## Overview

ScienceAgentBench 是一个评估 language agent 在数据驱动科学发现工作流中单个任务的 benchmark。它从四个学科的 44 篇同行评审论文中提取 102 个任务，将每个任务的目标输出统一为一个自包含的 Python 程序，并对生成的程序、执行结果与成本进行评分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.05080>
- **Venue:** ICLR 2025

## Summary

ScienceAgentBench 主张：在宣称端到端自动化科学发现之前，应在科学工作流中的单个任务上对 agent 进行严格评估。为确保科学真实性与现实相关性，它从四个学科的 44 篇同行评审论文中提取 102 个任务，并邀请九位领域专家进行验证。每个任务的目标输出被统一为一个自包含的 Python 程序文件，并用一组指标考察生成的程序、执行结果与成本。每个任务经过标注者与领域专家的多轮人工验证，benchmark 还提出两种策略以缓解数据污染问题。

## Tasks

从四个科学学科的 44 篇同行评审论文中提取 102 个任务。每个任务的目标输出被统一为一个自包含的 Python 程序文件。学科名称：TODO(reference)——摘要未说明。

## Domains

数据驱动的科学发现，跨四个学科（具体学科：TODO(reference)）。

## Evaluation

- 每个任务的目标输出统一为一个自包含的 Python 程序。
- 一组指标考察生成的程序、执行结果与成本。
- 由标注者与领域专家进行多轮人工验证。
- 提出两种策略以缓解数据污染问题。
- 报告：每个任务三次尝试下，表现最佳的 agent 独立求解 32.4% 的任务，在提供专家知识时为 34.3%。OpenAI o1-preview（direct prompting + self-debug）达到 42.2%，但成本超过其他 LLM 的 10 倍。

## Typical Duration

TODO(reference)：摘要未说明单任务时长或 token 预算。

## Main Contribution

一个经严格验证的数据驱动科学发现 benchmark：以真实论文中提取、专家验证的任务与统一的 Python 程序输出目标，评估 agent 在单个科学工作流任务上的能力，而非假定端到端自动化。

## Key Design Ideas

- 任务从真实同行评审论文中提取，并由领域专家验证以确保科学真实性。
- 统一的目标输出（自包含的 Python 程序）使异构科学任务可比较地打分。
- 评估覆盖生成的程序、执行结果与成本，而非单一准确率指标。
- 两种显式的数据污染缓解策略。
- 在五个开源与专有 LLM 上、三种 agent 框架下评估：direct prompting、OpenHands CodeAct 与 self-debug。

## Strengths

- 以出版物为基础、专家验证的任务，为科学发现评估提供生态效度。
- 统一的 Python 程序输出使得跨学科的、基于执行的可比较打分成为可能。
- 在报告准确率的同时报告成本，揭示推理时计算的权衡（o1-preview 以 >10 倍成本达到 42.2%）。
- 显式的数据污染缓解增强 benchmark 完整性。

## Limitations

- Repository note: 最佳 agent 求解率偏低（独立 32.4%，含专家知识 34.3%）表明该 benchmark 远未饱和——就 headroom 而言是优点，但超出通过/失败的单任务诊断信号并非其重点。
- Repository note: 范围是以 Python 程序表达的数据驱动发现；无法归约为程序产物的科学任务不在其范围内。

## Related Works

- [NatureBench](./naturebench.md) — 同样将科学任务锚定到同行评审论文，但以与已发表 SOTA 比较打分，而非执行统一的 Python 程序。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样采用基于执行的验证科学计算工作流，但用容器化 pytest 而非统一的 Python 程序输出。
- [AIRS-Bench](./airs-bench.md) — 同样面向研究科学任务，但评估端到端研究生命周期而非单个工作流任务。
