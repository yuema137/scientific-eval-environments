# SUPER (2024)

> [English](../../works/super.md) | **简体中文**

## Overview

SUPER 评测 agent 搭建并执行研究仓库中的任务：45 个带专家解的端到端问题、152 个针对具体挑战的子问题、602 个自动生成问题，来自真实的 ML/NLP GitHub 仓库——最强模型（GPT-4o）端到端只解出 16.3%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.07440>
- **Code:** <https://github.com/allenai/super-benchmark>
- **Venue:** EMNLP 2024

## Summary

复现研究意味着让别人的仓库真正跑起来，SUPER（出自 AI2）评测的正是这件事：agent 须搭建并执行来自真实 ML/NLP 研究仓库（GitHub 野外）的任务——解决依赖、修复错误、运行代码以复现结果。它含 45 个带专家解的端到端问题、152 个隔离具体搭建挑战的子问题、602 个自动生成问题。最强模型 GPT-4o 端到端只解出 16.3%（场景 46.1%），表明真实世界的复现对 agent 而言仍然很不稳定。

## Tasks

搭建并执行真实研究仓库中的任务：45 个端到端问题、152 个子问题、602 个自动生成问题；agent 配置环境、解决错误、运行代码。交互式 agent 化、长 horizon。

## Domains

AI 与机器学习研究——研究复现：搭建并执行 ML/NLP 研究仓库。

## Evaluation

- 端到端解出率，加场景/子问题（landmark）成功率。
- **报告。** GPT-4o 端到端解出 16.3%，场景 46.1%。

## Typical Duration

每个任务一段长 horizon 的「仓库搭建-执行」回合。

## Main Contribution

把研究复现的「搭建并执行」瓶颈——让真实研究代码跑起来这一不起眼却决定性的步骤——隔离为可评分的 agent benchmark。

## Key Design Ideas

- 真实「野外」GitHub 仓库捕捉复现真正面对的杂乱。
- 端到端/子问题/自动生成的划分给出分级难度与规模。
- 专家解锚定 45 个端到端问题。

## Strengths

- 瞄准决定研究可用性的复现步骤，AI2 公开发布。
- 16.3% 端到端上限是复现前沿的清晰标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；EMNLP 2024 未见于 arXiv Comments（论文于 EMNLP 2024 发表）。

## Related Works

- [ML-Bench](./ml-bench.md) — 同样是仓库级 ML 任务，覆盖代码生成与 agent 执行。
- [ResearchCodeBench](./researchcodebench.md) — 同样是研究代码评估，考实现论文贡献。
- [MLR-Bench](./mlr-bench.md) — 同样是 ML 研究自动化，覆盖全流程。
