# Agents' Last Exam (2026)

> [English](../../works/agents-last-exam.md) | **简体中文**

> **首次公开：** 2026-06-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.05405)

## Overview

Agents' Last Exam (ALE) 是一个 frontier 长 horizon benchmark，由 250 多位行业专家共同设计，围绕美国职业分类（U.S. occupational taxonomy）中的实际专业工作流构建。它的目标是弥合 benchmark 表现与真实世界职业部署之间的差距。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.05405>

## Summary

ALE 被定位为一个"活的（living）"benchmark，持续吸纳新的工作流。它覆盖美国职业分类中的非物理性行业，任务由领域专家构造和验证。论文表明最难难度层在发布时刻意保持未饱和。

## Tasks

约 1,000+ 任务，分布在 13 个行业大类与 55 个子领域下。

## Domains

非物理性行业，遵循美国职业分类结构。

## Evaluation

面向长 horizon 真实任务的可测量结果。报告：最难难度层在发布时保持未饱和，平均 full pass rate 低于 1%。

## Typical Duration

长 horizon 多步任务。论文摘要未给出精确单任务时长。

## Main Contribution

一个由行业专家共同设计、以经济上有意义的专业工作流为基础的 frontier benchmark，旨在揭示 benchmark 得分与真实世界部署可用性之间的差距。

## Key Design Ideas

- 250+ 行业专家驱动的任务设计。
- 以美国职业分类为构建结构。
- "活的" benchmark 模式——持续吸纳新工作流。
- 显式难度层，最难层在发布时刻意未饱和。

## Strengths

- 直接由行业专家 grounding，生态效度强。
- 难度上留有余量——最难层对 frontier 模型仍开放。
- 覆盖 13 个行业大类与 55 个子领域。

## Limitations

- Repository note: 仅覆盖非物理性行业——结果不外推至具身或依赖硬件的工作流。

## Related Works

- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — 也是长 horizon，但限定在 terminal 环境而非职业分类。
