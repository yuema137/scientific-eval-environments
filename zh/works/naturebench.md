# NatureBench (2026)

## Overview

NatureBench 评估 AI coding agent 是否能匹敌 Nature-family 科学出版物的已发表 SOTA——被作者框定为一次从"复现"走向"方法论发现"的评估尝试。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.24530>

## Summary

NatureBench 从同行评审的 Nature-family 论文中蒸馏任务，追问 coding agent 是否能达到甚至超越已发表 SOTA。该 benchmark 同时考察跨学科的科学覆盖，以及要匹敌一份真实出版物结果所需的深度。

## Tasks

90 个从同行评审的 Nature-family 论文中蒸馏出的任务。

## Domains

来自 Nature-family 论文的跨学科科学问题。

## Evaluation

- 与每个蒸馏任务对应的已发表 SOTA 进行比较。
- 报告：最强模型仅在 17.8% 的任务上超越已发表结果。
- 作者观察：agent 的成功往往来自将科学问题重构为常规的预测任务，而非真正的方法论创新。

## Typical Duration

TODO(reference): 摘要未给出每任务时长。

## Main Contribution

将 benchmark 难度锚定在顶级科学出版物的已发表 SOTA 上——提供一个与真实研究产出对齐的门槛，而非由人工挑选的玩具任务。

## Key Design Ideas

- 任务源自 Nature-family 出版物，给出一个真实的 SOTA 参照。
- 单个 benchmark 内的跨学科覆盖。
- 显式区分 "匹敌 SOTA" 与 "发现"。

## Strengths

- SOTA 锚点使难度直接与已发表科学结果绑定。
- 揭示了一个显著缺口（最强模型 17.8%），且参照是硬指标。
- 作者观察揭示了一个独立的评估关注点（问题重构）。

## Limitations

- Repository note: 蒸馏自 Nature-family 出版物——覆盖会受该系列刊物编辑偏好塑形。

## Related Works

- [AIRS-Bench](./airs-bench.md) — 同样面向研究生命周期，但围绕自建任务集组织，而非以已发表 SOTA 为锚点。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样面向科学，但聚焦容器化可执行验证。
