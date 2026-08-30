# UniClawBench (2026)

> [English](../../works/uniclawbench.md) | **简体中文**

> **首次公开：** 2026-07-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.08768)

## Overview

UniClawBench 是面向 proactive agent 的通用 benchmark，围绕五个模型能力组织任务，并通过 executor / supervisor / user 三方闭环 agent 模拟，在实时 Docker 容器中进行评估。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.08768>

## Summary

UniClawBench 面向能在真实环境中操作日常工具、辅助用户的 proactive agent。任务在实时 Docker 容器中运行，配有分步 checkpoints；评估以闭环方式进行——由 executor、supervisor 和 user agent 共同模拟多轮反馈，且评分标准对被评估的 agent 隐藏。

## Tasks

400 个双语真实世界任务。

## Domains

跨平台的 proactive-agent 任务。任务构建按能力驱动而非按领域切分。

## Evaluation

- 能力驱动，沿五个轴：Skill Usage、Exploration、Long-Context Reasoning、Multimodal Understanding、Cross-Platform Coordination。
- 实时 Docker 环境，带 step 级 checkpoints。
- 闭环模拟：executor + supervisor + user agent。
- 评分标准对被评 agent 隐藏。

## Typical Duration

多轮交互 + checkpoints，任务本身为长 horizon。论文摘要未给出具体单任务时长。

## Main Contribution

一个能力导向、基于闭环模拟的 proactive-agent benchmark，评分标准对被评 agent 隐藏。

## Key Design Ideas

- 五个显式能力轴作为组织原则。
- 每任务的 Docker 实时环境。
- 多 agent 闭环模拟（executor + supervisor + user）。
- 隐藏评分标准以降低 gaming 风险。

## Strengths

- 能力驱动的设计能揭示 agent 在何处薄弱，而不仅是它是否失败。
- 隐藏评分标准降低了针对评估过程优化的泄漏风险。
- 覆盖 400 个双语任务。

## Limitations

- Repository note: 闭环模拟依赖模拟 agent 的保真度；模拟质量约束评估质量。

## Related Works

- [Agents' Last Exam](./agents-last-exam.md) — 同样面向真实世界 proactive-agent 任务，但以行业专家工作流而非能力分类为 grounding。
- [AgentBoard](./agentboard.md) — 同样是能力导向的多轮评估，但粒度在子目标（subgoal）进展。
