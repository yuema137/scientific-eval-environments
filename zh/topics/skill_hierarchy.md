# Skill Hierarchy

> [English](../../topics/skill_hierarchy.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

Skill hierarchy 指把复杂的 agent 能力分解为一组更窄的能力或 subskill 的结构化集合，并配以对每个 subskill 分别打分的评估协议。这类 benchmark 共享一个设计承诺：单一聚合分数把太多东西混在一起——要理解 agent 能做什么、不能做什么，评估必须探查能力树的多个层次。

## Motivation

聚合排行榜掩盖了 agent 能力的形状。两个总分相同的 agent 可能在完全不同的 subskill 上失败，单指标排名无法告诉下游用户"哪一个 agent 更适合哪一类子任务"。Skill-hierarchy benchmark 通过产出**per-capability 画像**来解决这一问题。

Skill hierarchy 与 [Credit Assignment](./credit_assignment.md) 相关但不同。Skill hierarchy 问**agent 拥有哪些 subskill**；credit assignment 问**trajectory 的哪一步驱动了成功或失败**。两者可以合起来做——沿 trajectory 对每个 subskill 分别打分——但它们回答的是不同的问题。

## Existing Approaches

- **任务子目标分解。** [AgentBoard](../works/agentboard.md) 为每个任务标注一条子目标链，并报告进展率——实际上是 per-subgoal 的能力信号。
- **能力子过程分解（tool use）。** [T-Eval](../works/t-eval.md) 把 tool use 拆为 6 个子过程（instruction following / planning / reasoning / retrieval / understanding / review），在孤立任务上分别评估。
- **能力子过程分解（环境配置）。** [Enconda-bench](../works/enconda-bench.md) 把软件环境配置拆为 planning / error diagnosis / repair / execution。
- **以能力轴作为组织原则。** [UniClawBench](../works/uniclawbench.md) 围绕五个能力轴（Skill Usage、Exploration、Long-Context Reasoning、Multimodal Understanding、Cross-Platform Coordination）组织其 400 任务的 benchmark，并把这些轴作为主要报告维度。
- **跨 benchmark 的控制决策分类。** [AgentAtlas](../works/agentatlas.md) 不按任务或能力做分解，而是把 agent 的**控制决策**分成六类，覆盖 15 个 benchmark——提供的是跨任务可迁移的 skill-hierarchy 信号。
- **单一领域内的能力深度分层。** [CFDLLMBench](../works/cfdllmbench.md) 按*深度*而非按子过程来分解 CFD 能力：知识（CFDQuery）、数值与物理推理（CFDCodeBench）、实际工作流实现（FoamBench），各自是独立的任务集。由于这些层级在难度上是嵌套而非并列的，它给出的能力剖面更像一条天花板——很高的知识分数与近乎为零的端到端仿真成功率同时存在。
- **Tool-evolution 框架（越界归属）。** [GATE](../works/gate.md) 为覆盖完整性而纳入，但论文实际主题是面向 LLM 的图式 tool making，而非 skill 分解。详见卡片。

## Comparison

| Benchmark | Year | 分解粒度 | 轴 | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | 每任务的子目标链 | 任务特定（人工标注） | [→](../works/agentboard.md) |
| T-Eval | 2023 | 跨任务的能力子过程 | 6 个 tool-use 子过程 | [→](../works/t-eval.md) |
| Enconda-bench | 2025 | 跨任务的能力子过程 | 4 个环境配置子过程 | [→](../works/enconda-bench.md) |
| UniClawBench | 2026 | Benchmark 级组织轴 | 5 个 proactive-agent 能力 | [→](../works/uniclawbench.md) |
| AgentAtlas | 2026 | 每次控制决策（跨 benchmark 覆盖） | 6 类控制决策 | [→](../works/agentatlas.md) |
| GATE | 2026 | *Tool-evolution 框架，非 skill 分解——见卡片* | 层级化工具图 | [→](../works/gate.md) |
| CFDLLMBench | 2025 | 单一领域内的嵌套能力层级 | 3 个深度层级（知识 / 数值推理 / 工作流实现） | [→](../works/cfdllmbench.md) |

## Open Questions

- **任务特定 vs. 跨任务分解。** AgentBoard 对每个任务单独分解成子目标；T-Eval / Enconda-bench 则把能力本身分解成跨任务共享的子过程；AgentAtlas 跨 benchmark 按控制决策类型做分解。哪一种能给出更可迁移的能力画像？
- **轴的选择。** T-Eval 的 6 个、Enconda-bench 的 4 个、UniClawBench 的 5 个、AgentAtlas 的 6 个都是合理分解。是否存在一个规范化的最小集合，还是轴的选择必然依赖领域？
- **合成。** 给定 per-subskill 分数，如何合成为一个总体能力估计，同时不丢失当初做分解所提供的画像？
- **嵌入式 vs. 覆盖式分解。** Skill-hierarchy 信号应由底层 benchmark 内嵌产出（AgentBoard、T-Eval、Enconda-bench、UniClawBench 的方式），还是作为跨 benchmark 的覆盖层（AgentAtlas 的方式）？

## Related Works

- [AgentBoard](../works/agentboard.md)
- [T-Eval](../works/t-eval.md)
- [Enconda-bench](../works/enconda-bench.md)
- [UniClawBench](../works/uniclawbench.md)
- [AgentAtlas](../works/agentatlas.md)
- [GATE](../works/gate.md) — 为覆盖完整性而纳入；实际主题是面向 LLM 的 tool making，而非 skill-hierarchy 评估。
- [CFDLLMBench](../works/cfdllmbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
