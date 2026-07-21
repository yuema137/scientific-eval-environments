# SciAgentArena (2026)

## Overview

SciAgentArena 是一个系统性 benchmark，用于在跨尺度的真实世界科学研究场景中评估 AI agent。它在一个交互式、agent-agnostic 的环境中提供约 200 个带逐步验证的任务。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12736>
- **Project:** <https://sciagentarena.github.io/>

## Summary

论文题为 *Benchmarking AI Agents for Addressing Scientific Challenges Across Scales*，SciAgentArena 针对 AI agent 在真实研究场景中的实际能力仍不清楚这一问题。它提供一个交互式、agent-agnostic 的环境，含约 200 个从真实世界科学研究场景构造、跨多个领域的任务，采用逐步验证。它报告 agent 在结构化数据分析工作流上表现良好，但在新颖洞见、自主探索与开放式问题上表现挣扎，并编目了常见失败模式。

## Tasks

约 200 个带逐步验证的任务，从跨多个领域与尺度的真实世界科学研究场景构造。确切的领域清单与各领域计数：TODO(reference)——摘要页未说明。

## Domains

跨尺度的多个科学研究领域。具体学科：TODO(reference)。

## Evaluation

- 支持多样 AI agent 的交互式、agent-agnostic 环境。
- 对 agent 进展的逐步验证。
- 报告的定性发现：在结构化数据分析工作流上强；在新颖洞见、自主探索与开放式问题上弱。

## Typical Duration

多步的科学研究工作流。单任务时长：TODO(reference)——摘要页未说明。

## Main Contribution

一个系统性、agent-agnostic 的 benchmark，用于衡量 AI agent 在跨尺度真实科学研究场景上的进展，采用逐步验证，并显式说明 agent 当前在何处成功与失败。

## Key Design Ideas

- 跨多个尺度的真实世界科学研究场景。
- 逐步验证而非仅终态结果打分。
- agent-agnostic、交互式的环境，支持多样 agent。
- 显式的失败模式分析（新颖洞见、自主探索、开放式问题）。

## Strengths

- 逐步验证提供比仅终态成功更细粒度的信号。
- agent-agnostic 设计支持跨多样 agent 实现的比较。
- 报告具体的强弱项而非单一分数。

## Limitations

- Repository note: 具体的科学领域、尺度与各领域任务计数在摘要页未说明，标注为 `TODO(reference)`，待从论文或项目核实。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样评估 agent 在数据驱动科学任务上的能力，但对统一的 Python 程序输出打分，而非跨尺度的逐步验证。
- [AIRS-Bench](./airs-bench.md) — 同样面向研究科学任务，评估端到端研究生命周期。
