# RE-Bench (2024)

> [English](../../works/re-bench.md) | **简体中文**

## Overview

RE-Bench（Research Engineering Benchmark，v1）在前沿 AI R&D 能力上对照人类专家评测语言模型 agent：7 个带参考解的开放式 ML 研究工程环境，加上 61 位人类专家 71 次 8 小时尝试的数据——2 小时预算下 agent 得分是人类的 4 倍，但到 32 小时人类反超到 2 倍。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.15114>
- **Code:** <https://github.com/metr/ai-rd-tasks>
- **Venue:** arXiv preprint (cs.LG), 2024

## Summary

RE-Bench（出自 METR）意在于真实 AI R&D 上对照人类专家评估 agent。其 7 个开放式 ML 研究工程环境——编写并优化代码、自定义核、微调脚本——对照强参考解评分，并发布 61 位人类专家 71 次 8 小时尝试的数据（82% 取得非零分，24% 达到或超过参考）。其标志性结果是时间预算对比：2 小时预算下最强 AI agent 得分是专家的 4 倍，但到 32 小时人类达到最强 agent 的 2 倍——且有一例 agent 写出了比任何人类专家都快的自定义 Triton 核。

## Tasks

7 个开放式 ML 研究工程环境（代码/核优化、微调）；agent 与人类在 2/8/32 小时预算下对照参考解评分。交互式 agent 化、长 horizon。

## Domains

AI 与机器学习研究——AI R&D / 研究工程：在开放式研究任务上优化代码与模型。

## Evaluation

- 时间预算下对照参考解的 best-of-k 评分；与人类专家数据直接对照。
- **报告。** 2h 时 agent 为专家 4 倍；32h 时人类为最强 agent 2 倍；82% 专家尝试非零，24% 达到/超过参考。

## Typical Duration

显式多小时时间预算（2/8/32 小时）下的长 horizon 回合。

## Main Contribution

一个以人类为锚、带时间预算的前沿 AI R&D benchmark——不仅测量 agent 能否做研究工程，还测量其速度与上限随时间与专家相比如何。

## Key Design Ideas

- 带参考解的开放式优化任务测量真实的 R&D 进展。
- 大规模人类专家数据（71 次尝试）实现直接、校准的对照。
- 时间预算扫描暴露「agent 快、人类可扩展」的动态。

## Strengths

- 最严谨的「人类 vs agent」AI R&D 对照之一，环境、人类数据与轨迹全开源。
- 时间预算的发现是被广泛引用的能力轨迹结果。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv 元数据无发表信息（METR 是机构）。摘要称 7 个环境，而仓库列出 8 个任务族——此处用摘要数字。

## Related Works

- [MLRC-Bench](./mlrc-bench.md) — 同样是以人类为锚的 ML 研究评估，考竞赛任务。
- [MLGym](./mlgym.md) — 同样是开放式 AI 研究任务，在 Gym 环境中。
- [MLAgentBench](./mlagentbench.md) — 同样是「提升指标」的 ML 实验，但无人类专家对照。
