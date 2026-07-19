# AgentAtlas (2026)

## Overview

AgentAtlas 是面向 LLM agent 的诊断词汇与审计协议，应用在 15 个已有 agent benchmark 之上。它把评估从"仅结果排行榜"重构为对**每次控制决策**的质量和**每条 trajectory** 的质量，提供一个六路控制决策分类以及一个失败分类。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/html/2605.20530v1>

## Summary

AgentAtlas 本身不是任务套件——它是一个诊断框架：一个控制决策类型分类、一个失败分类，以及一个可叠加在既有 agent benchmark 上的审计协议。论文把该框架应用在 15 个 agent benchmark 上，并通过在 8 个模型上对 1,342 个合成 item 的评估来演示测量挑战。

## Tasks

在 8 个模型上评估 1,342 个合成 item。底层任务基座是 15 个既有 agent benchmark——审计协议叠加于其上。

## Domains

由被审计的 15 个 benchmark 所覆盖的环境——codebase、browser、operating system、calendar、file、tool ecosystem。

## Evaluation

- 六路控制决策类型分类。
- 失败分类。
- 审计框架叠加在底层 benchmark 之上。
- 在 8 个模型上评估 1,342 个合成 item。

## Typical Duration

取决于被审计的底层 benchmark；AgentAtlas 本身不固定 horizon。

## Main Contribution

把 agent 评估重构为一个诊断词汇与审计协议——将结果成功与控制决策质量、trajectory 质量分离——并通过在 15 个既有 agent benchmark 上应用、以 1,342 个 item 的具体测量来演示这一重构。

## Key Design Ideas

- 六路控制决策类型作为跨异质 benchmark 的共享词汇。
- 失败分类，用于在二值 pass/fail 之外分类 agent 错误。
- 审计协议作为已有 benchmark 之上的覆盖层，而不是新任务套件。
- 跨 benchmark 适用（应用在 15 个 benchmark 上）。

## Strengths

- 提供跨异质 agent benchmark 的共享词汇。
- 覆盖式设计使其继承已有 benchmark 的任务，而不必新建套件。
- 在 1,342 个 item 上的显式测量为框架主张提供了 grounding。

## Limitations

- Repository note: AgentAtlas 是叠加在既有 benchmark 之上的框架，而非独立的任务套件；其覆盖继承所审计 benchmark 的覆盖。

## Related Works

- [Insights Generator](./insights-generator.md) — 同样是 trace 级诊断贡献而非任务套件；Insights Generator 侧重自动化的语料级假设检验，AgentAtlas 侧重共享的诊断词汇。
- [AgentBoard](./agentboard.md) — 同样在最终任务结果之下做拆分；AgentBoard 沿任务子目标做拆分，AgentAtlas 跨 benchmark 沿控制决策类型做拆分。
