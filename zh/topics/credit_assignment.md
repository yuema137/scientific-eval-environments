# Credit Assignment

## Definition

在评估语境下，credit assignment 是把一条 trajectory 的成功或失败**归因**到具体步骤、子目标或中间输出的问题——而不是把成功当作 trajectory 整体的一个无结构属性。在 benchmark 中，credit-assignment 机制表现为密集中间奖励、部分得分或分步打分——即使最终结果只是一个二值信号，它们也能保留更细的信号。

## Motivation

长 horizon 与开放式任务产出的 trajectory 中，单一的终态信号——通过还是失败——粒度太粗，无法作为有用信号。两条失败的 trajectory 可以在**哪里**出错上有差异；两条成功的 trajectory 可以在成功是由稳健的中间推理挣来、还是仅由一次幸运的最后一步得到而有差异。Credit assignment 是评估阶段刻意保留这种更细信号的设计承诺。

Credit assignment 与 [Skill Hierarchy](./skill_hierarchy.md) 相关但不同。Skill hierarchy 问**agent 拥有哪些 subskill**；credit assignment 问**trajectory 的哪一步驱动了结果**。许多 benchmark 同时对两者做出贡献。

## Existing Approaches

- **通过子目标进展给部分得分。** [AgentBoard](../works/agentboard.md) 按标注子目标的完成比例给分——即使 trajectory 在最后失败，只要它取得了中间进展，仍能得到非零分。
- **阈值下的分级部分奖励。** [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) 把任务分解为带分级奖励的子任务，并在可配置阈值下聚合（0.95 部分奖励、1.0 完美奖励），使指标能区分"几乎解出"和"毫无进展"。
- **沿 trajectory 的多维度部分得分。** [FinTrace](../works/fintrace.md) 在 4 个维度（action correctness、execution efficiency、process quality、output quality）下用 9 个指标评分整条 trajectory，因此一条 trajectory 可以在某些维度上成功、在另一些维度上失败。
- **效用函数式部分得分。** [TRACE](../works/trace.md) 用 hierarchical trajectory utility 联合评价 accuracy、efficiency、evidence grounding、reasoning quality——把它们视为互补的"分数来源"，而不是彼此替代。

## Comparison

| Benchmark | Year | Credit 信号 | Credit 的 trajectory 单位 | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | 已完成标注子目标的比例 | Per subgoal | [→](../works/agentboard.md) |
| Long-Horizon-Terminal-Bench | 2026 | 分级子任务奖励 + 阈值聚合 | Per subtask，带权重 | [→](../works/long-horizon-terminal-bench.md) |
| FinTrace | 2026 | 9 指标 × 4 维度 | Per trajectory，每维度 | [→](../works/fintrace.md) |
| TRACE | 2026 | 覆盖 accuracy / efficiency / grounding / reasoning 的 hierarchical utility | Per trajectory，每分量 | [→](../works/trace.md) |

## Open Questions

- **在哪里分配 credit。** Per subgoal（AgentBoard）、per 分级子任务（Long-Horizon-Terminal-Bench）、per trajectory 维度（FinTrace、TRACE）——每种选择都反映了一种关于"trajectory 由什么构成"的理论。它们在聚合后是否等价，还是各自揭示不同的模型行为？
- **加权。** 阈值聚合（Long-Horizon-Terminal-Bench）与效用函数（TRACE）都需要权重。如何选择权重才能让 credit-assigned 分数在跨 benchmark 时可比？
- **对 judge 的依赖。** 像 "reasoning quality" 这样的 trajectory 级维度通常需要模型或人类 judge。Judge 本身的可靠性是否是 credit-assignment 指标的瓶颈？

## Related Works

- [AgentBoard](../works/agentboard.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [FinTrace](../works/fintrace.md)
- [TRACE](../works/trace.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
