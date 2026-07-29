# Credit Assignment

> [English](../../topics/credit_assignment.md) | **简体中文**

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
- **对照 oracle DAG 的动作级 credit。** [Gaia2](../works/gaia2.md) 只为改变状态的 write 动作计功，并对照一条最小 oracle 序列在四个维度上检查——consistency、causality、timing 与 completeness——同时让 read 动作不限次数且不受惩罚。在 450 条人工标注 trajectory 上，该验证器达到 0.98 一致性，而仅用 LLM judge 的基线为 0.72。
- **对 credit 信号本身的元评估。** [QVal](../works/qval.md) 不看下游训练效果，而是问一个稠密监督信号能否像强 reference policy 的 Q 值那样排序候选动作；它以此比较七个方法学家族的 21 个方法，并发现简单的 prompting baseline 一致优于文献中较新的方法。
- **前沿证明上的专家步骤标签。** [Hard2Verify](../works/hard2verify.md) 以 500 余小时专家标注为奥赛级数学解答逐步打标，用来给 29 个验证器打分，并指出真正区分它们的是首错定位而非逐步标注。
- **由构造得到的决定性步骤标签。** [Who&When Pro](../works/who-and-when-pro.md) 精确重放成功回合的前缀、只替换一个动作再让其走向失败，从而使「哪一步坏事」的标签由构造而来、可在 12,326 条轨迹的规模上机器校验。
- **把逐步评判者本身放上考台。** [CUARewardBench](../works/cuarewardbench.md) 用 272 条轨迹级与 346 条步骤级专家标注，考察 7 个视觉语言模型分别作为结果奖励模型与过程奖励模型的表现，并以 precision 与 NPV 而非 accuracy 为主指标，因为这两类错误的代价并不对称。
- **面向工具使用的过程奖励模型评测。** [ToolPRMBench](../works/toolprmbench.md) 用 984 个强制选择的步骤级测试点考察 17 个过程奖励模型，并按错误来源分开报告——离线扰动出的孤立错误与真实失败回合中自然出现的错误。
- **逐步错误定位。** [ProcessBench](../works/processbench.md) 要求评判者返回最早出错的步骤索引；它给出了一个关键量化——即便最终答案正确，仍有相当比例的解答含有真实的步骤错误，且比例随题目难度上升。
- **按错误类型细分的步骤 credit。** [PRMBench](../works/prmbench.md) 以 6,216 个实例、83,456 条步骤标签，在 Simplicity / Soundness / Sensitivity 三大类下分出 9 个子类考察 25 个评判者，使评判者的失败模式可被分离，而非压成单一的步骤准确率。
- **形式化内核给出的偏好标签。** [FormalRewardBench](../works/formalrewardbench.md) 用 250 对 Lean 4 偏好数据考察 reward model；对经由 Lean 的那几种构造策略，正确与错误证明的标签由类型检查器确定性给出。该工作明确只做整份证明层面的判定，不涉及逐步评估。

## Comparison

| Benchmark | Year | Credit 信号 | Credit 的 trajectory 单位 | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | 已完成标注子目标的比例 | Per subgoal | [→](../works/agentboard.md) |
| Long-Horizon-Terminal-Bench | 2026 | 分级子任务奖励 + 阈值聚合 | Per subtask，带权重 | [→](../works/long-horizon-terminal-bench.md) |
| FinTrace | 2026 | 9 指标 × 4 维度 | Per trajectory，每维度 | [→](../works/fintrace.md) |
| TRACE | 2026 | 覆盖 accuracy / efficiency / grounding / reasoning 的 hierarchical utility | Per trajectory，每分量 | [→](../works/trace.md) |
| Gaia2 | 2026 | write 动作与最小 oracle 序列的匹配（consistency / causality / timing / completeness） | 每一个改变状态的动作 | [→](../works/gaia2.md) |
| QVal | 2026 | 与强 reference policy 的 Q 值的排序一致性（Spearman ρ） | 单个 state 上的候选 action | [→](../works/qval.md) |
| Hard2Verify | 2025 | 专家逐步标注；首错定位准确率 | 每个证明步骤 | [→](../works/hard2verify.md) |
| Who&When Pro | 2026 | 由注入构造的决定性步骤标签 | 每条失败轨迹的单个决定性步骤 | [→](../works/who-and-when-pro.md) |
| CUARewardBench | 2025 | 专家标注的轨迹成功与步骤正确性；precision / NPV | 轨迹整体与单个步骤 | [→](../works/cuarewardbench.md) |
| ToolPRMBench | 2026 | 强制选择的步骤级测试点，按错误来源分层 | 每个工具调用步骤 | [→](../works/toolprmbench.md) |
| ProcessBench | 2024 | 最早出错步骤的索引（或判定全对） | 每个解答步骤 | [→](../works/processbench.md) |
| PRMBench | 2025 | 9 个子类的类型化步骤标签，由注入构造 | 每个解答步骤 | [→](../works/prmbench.md) |
| FormalRewardBench | 2026 | Lean 类型检查器给出的偏好标签 | 整份证明（明确不做逐步） | [→](../works/formalrewardbench.md) |

## Open Questions

- **在哪里分配 credit。** Per subgoal（AgentBoard）、per 分级子任务（Long-Horizon-Terminal-Bench）、per trajectory 维度（FinTrace、TRACE）——每种选择都反映了一种关于"trajectory 由什么构成"的理论。它们在聚合后是否等价，还是各自揭示不同的模型行为？
- **加权。** 阈值聚合（Long-Horizon-Terminal-Bench）与效用函数（TRACE）都需要权重。如何选择权重才能让 credit-assigned 分数在跨 benchmark 时可比？
- **对 judge 的依赖。** 像 "reasoning quality" 这样的 trajectory 级维度通常需要模型或人类 judge。Judge 本身的可靠性是否是 credit-assignment 指标的瓶颈？

## Related Works

- [AgentBoard](../works/agentboard.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [FinTrace](../works/fintrace.md)
- [TRACE](../works/trace.md)
- [Gaia2](../works/gaia2.md)
- [QVal](../works/qval.md)
- [Hard2Verify](../works/hard2verify.md)
- [Who&When Pro](../works/who-and-when-pro.md)
- [CUARewardBench](../works/cuarewardbench.md)
- [ToolPRMBench](../works/toolprmbench.md)
- [ProcessBench](../works/processbench.md)
- [PRMBench](../works/prmbench.md)
- [FormalRewardBench](../works/formalrewardbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
