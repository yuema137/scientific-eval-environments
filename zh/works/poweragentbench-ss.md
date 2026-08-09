# PowerAgentBench-SS (2026)

> [English](../../works/poweragentbench-ss.md) | **简体中文**

## Overview

PowerAgentBench-SS 评测电力系统稳态研究中的 agentic AI：agent 获得公开算例数据、动作约束、工具 API 与验证预算，须检视电网算例、调用仿真器、筛选预想故障、提出满足约束的缓解措施并留下可审计的证据链——而一个隐藏评估器会重算物理有效性并为提交的报告打分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.18789>
- **Venue:** arXiv preprint (eess.SY), 2026

## Summary

电网分析恰是不能相信 agent 自我报告的场景：PowerAgentBench-SS 因此把一切都重算一遍。其试点在 IEEE 39 节点系统的运行点变体上做基于直流潮流的 N-2 热稳定越限搜索，agent（三个本地 Ollama 模型加一个 OpenAI API agent）经 LLM JSON 命令适配器接入。评分词汇异常丰富——submitted recall、evidence-backed recall、found recall、false-safe 罚分、severity regret、residual violation score、动作成本、工具使用效率与工作流诊断——设计意图正是证明「只看求解器」或「只看答案」的评估并不充分。

## Tasks

agentic 的稳态电网研究：算例检视、工具选择、仿真器调用、预想故障筛选与缓解提议，在验证预算内进行；试点为 IEEE 39 节点系统运行点变体上的、基于直流潮流的 N-2 热稳定越限搜索。

## Domains

电力系统运行与规划：稳态分析与 N-2 预想故障筛选。

## Evaluation

- 隐藏评估器重算物理有效性并为报告打分：submitted/evidence-backed/found recall、false-safe 罚分、severity regret、residual violation score、动作成本、工具使用效率与工作流诊断。
- **报告。** 证明「只看求解器」或「只看答案」的评估不充分；数值结果为 TODO(reference)。

## Typical Duration

每个电网算例为验证预算下的多步工具调用研究。

## Main Contribution

每条论断都被重新推导的电网 agent 评估：隐藏评估器的重算、false-safe 罚分与 severity regret，把没有依据的「一切正常」报告变成被计分的失败模式。

## Key Design Ideas

- 基于重算的判分默认 agent 可能提交未经验证的论断——并动手去查。
- false-safe 罚分把危险的错误（漏报真实越限）罚得比误报更重。
- 验证预算使验证工作本身成为受配给的资源。

## Strengths

- 在本仓库记录的工程 agent benchmark 中，面向安全的指标体系最为丰富。
- 在标准 IEEE 测试系统上可复现的试点。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [gwBenchmarks](./gwbenchmarks.md) — 同样不信任 agent 自我报告并施加外部评估，在引力波科学中。
- [Frontier-Eng](./frontier-eng.md) — 同样是硬性可行性约束与预算下的工程优化。
- [StructureClaw](./structureclaw.md) — 同样是涉及安全的工程工作流，配严格的断言式验证。
