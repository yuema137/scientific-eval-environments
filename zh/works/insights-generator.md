# Insights Generator (2026)

> [English](../../works/insights-generator.md) | **简体中文**

## Overview

Insights Generator 是一个面向 LLM agent 的**语料级 trace 诊断**多 agent 系统。它以在 trace 语料上"提出并验证假设"的方式回答诊断问题，产出带证据支撑的 insights 报告——自动化了原本需要人工逐条 trace 检视的工作。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.21347>

## Summary

Insights Generator 面向 LLM agent 失败的**自动诊断**。相比对单条 trace 逐一手工检视，它部署一个多 agent 系统，在整个 trace 语料上提出与检验假设。实施该系统建议的用户，其下游 agent 性能提升了 30.4 个百分点。

## Tasks

非任务套件。系统作用于任意 agent 任务产出的执行 trace 语料。

## Domains

通用 LLM-agent trace 诊断。

## Evaluation

- 诊断报告质量作为直接输出。
- 下游影响：实施建议的用户提升了 30.4 个百分点。

## Typical Duration

对 trace 语料的离线分析；不受任务时长约束。

## Main Contribution

一个自动化的多 agent 诊断系统，将 trace 语料转化为带证据支撑的 insights 报告，并展示对建议的采纳可带来可测量的下游提升（+30.4 pp）。

## Key Design Ideas

- 在 trace 语料上进行多 agent 假设提出与检验。
- 输出物是带证据支撑的 insights 报告。
- 语料级——而非逐条 trace——的分析。
- 以可测量的下游提升作为主要成功指标。

## Strengths

- 自动化本应人工完成、且难以扩展的 trace 检视。
- 报告具体的下游影响，而非仅诊断报告质量。
- 语料级分析揭示了逐条 trace 检视会遗漏的跨 trace 模式。

## Limitations

- Repository note: 非任务套件——其效用取决于所应用的 trace 语料。

## Related Works

- [AgentAtlas](./agentatlas.md) — 同样是诊断贡献而非任务套件；AgentAtlas 侧重共享词汇，Insights Generator 侧重自动化的假设检验。
