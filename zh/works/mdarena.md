# MDArena (2026)

> [English](../../works/mdarena.md) | **简体中文**

## Overview

MDArena 是评估 coding agent 在真实分子动力学（MD）工作流上表现的 benchmark，包含 50 个容器化任务，来源于进行中的研究项目，覆盖 29 个分子体系与 14 种研究方案。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.02642>
- **Venue:** arXiv preprint (physics.chem-ph, cs.AI), 2026

## Summary

MDArena 指出：尽管 coding agent 在自动化科学工作流上被寄予厚望，它们在真实分子动力学任务上的可靠性仍缺乏刻画。该 benchmark 把真实的生物分子模拟工作——轨迹分析、体系搭建、自由能计算与增强采样——打包为容器化任务，用严格成功率与过程级部分得分共同计分。

## Tasks

50 个容器化任务，来源于进行中的研究项目，覆盖 29 个分子体系与 14 种研究方案。任务类别包括轨迹分析、体系搭建、自由能计算与增强采样方法。

## Domains

生物分子模拟与计算化学，包括膜蛋白体系与炼金术式（alchemical）自由能计算。

## Evaluation

- **Strict-Pass@1** 为主指标。
- **正确性与过程奖励指标**在二元成功之外刻画部分进展。
- **报告。** 评估六种模型配置；Codex GPT-5.5（extra-high reasoning）以 24/50（48%）领先，Codex GPT-5.5（Medium）为 21/50，OpenCode Gemini Flash 3.5 为 20/50。

## Typical Duration

容器化模拟工作流；单任务 wall-clock 为 TODO(reference)。

## Main Contribution

用真实、容器化的分子动力学工作流刻画 coding agent 在实际生物分子模拟（而非合成练习）上的可靠性。

## Key Design Ideas

- 任务取自进行中的研究项目，而非为 benchmark 专门编写。
- 容器化使异构的 MD 工具链成为可复现的评估面。
- 严格成功之外辅以过程奖励指标，为部分进展计分。

## Strengths

- 任务来源真实：29 个分子体系与 14 种研究方案来自进行中的研究。
- 留有大量提升空间——最佳配置仅解决 48% 的任务。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — 同样以执行为根基评估仿真领域的科学计算，但面向流体力学而非分子动力学。
- [ScienceAgentBench](./scienceagentbench.md) — 同样从真实研究提取可执行科学任务，但覆盖数据驱动发现学科而非单一仿真模态。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样是容器化科学工作流，由社区贡献并覆盖五大领域分组。
