# Credit Assignment

> [English](../../topics/credit_assignment.md) | **简体中文** · [← 全部 topics](./README.md)

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
- **对 credit 信号本身的元评估。** [QVal](../works/qval.md) 以「各方法的逐步分数能在多大程度上按 reference policy 的 Q 值排序候选动作」为标准，考察 21 种稠密监督方法，从而把步骤级 credit 信号本身——而非 agent——作为评估对象。
- **前沿证明上的专家步骤标签。** [Hard2Verify](../works/hard2verify.md) 由数学专家为 200 份前沿模型的奥赛解答逐一标注全部 1,860 个步骤，评分规则不向后传递 credit——只要某一步所依赖的更早步骤有误，该步即失去 credit。
- **由构造得到的决定性步骤标签。** [Who&When Pro](../works/who-and-when-pro.md) 在精确重放的成功前缀上注入单个错误，覆盖 12,326 条失败轨迹，因此失败的 credit 由构造而非标注落到唯一的 agent、步骤与错误模式上。
- **把逐步评判者本身放上考台。** [CUARewardBench](../works/cuarewardbench.md) 用 272 条已标注 computer-using agent 轨迹上的 346 条专家步骤正确性标签来给视觉语言奖励模型打分，从而把步骤级 credit 信号的可靠性由假定变为实测量。
- **步骤级奖励模型评测。** [ToolPRMBench](../works/toolprmbench.md) 把工具使用 agent 的轨迹转换为取自四个源 benchmark 的 987 个强制选择步骤样例，并按「能否在正确动作与貌似合理的错误动作之间选对」对 17 个 LLM、通用 PRM 与工具专用 PRM 排名。
- **逐步错误定位。** [ProcessBench](../works/processbench.md) 要求评判者在 3,400 份专家标注的数学解答上返回最早出错的步骤索引，并发现最终答案正确的 Omni-MATH 解答中仍有 51.8% 含有过程错误。
- **按错误类型细分的步骤 credit。** [PRMBench](../works/prmbench.md) 用九个注入式错误子类考察过程级奖励模型，使模型的 credit 信号按失败模式而非按聚合的步骤准确率来诊断。
- **考察那些本可稠密化 credit 的奖励模型。** [FormalRewardBench](../works/formalrewardbench.md) 在 250 对偏好数据上测试学得的 reward model 是否更偏好经过验证的 Lean 4 证明而非注入错误的变体，从而把 credit 信号本身——而非评分工具——作为被测对象。
- **Computer-use 评判者的标准化评测。** [OSReward](../works/osreward.md) 以多阶段人工标注的裁决为跨平台 computer-use 奖励模型打分，发现最先进的评判模型存在系统性的宽松偏差（leniency bias），并证明在其 OS-Shepherd-100K 数据上训练的 9B/35B 开源评判者能以约三十到六十分之一的成本达到前沿商业评判者的水平。
- **定位、归因、修复。** [SearchAuditor](../works/searchauditor.md) 在 1,243 条专家标注的失败搜索轨迹上端到端地考察审计者——定位关键错误步骤、归因到搜索特有的根因、再对照带评分 rubric 的参考修复打分——最强基线的端到端通过率仅有 26.6%。
- **深入 skill 内部的 credit。** [SkillSV](../works/skillsv.md) 把 credit assignment 从轨迹步骤移进 agent skill 的内部：在 skill 编译出的单元、依赖与层级结构上做结构感知的 Shapley 估值，并用成对删除与长度中性填充把内容价值与上下文成本区分开。
- **错误生命周期归因。** [TRAJDEBUG](../works/trajdebug.md) 在 TrajErrBench 的 486 条人工标注失败轨迹上追踪每个错误的解决状态与最终影响，让失败的 credit 落在真正决定失败的那个错误上，而不是落在 agent 事后已恢复的错误上。

## Comparison

| Benchmark | Year | Credit 信号 | Credit 的 trajectory 单位 | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | 已完成标注子目标的比例 | Per subgoal | [→](../works/agentboard.md) |
| Long-Horizon-Terminal-Bench | 2026 | 分级子任务奖励 + 阈值聚合 | Per subtask，带权重 | [→](../works/long-horizon-terminal-bench.md) |
| FinTrace | 2026 | 9 指标 × 4 维度 | Per trajectory，每维度 | [→](../works/fintrace.md) |
| TRACE | 2026 | 覆盖 accuracy / efficiency / grounding / reasoning 的 hierarchical utility | Per trajectory，每分量 | [→](../works/trace.md) |
| Gaia2 | 2026 | write 动作与最小 oracle 序列的匹配（consistency / causality / timing / completeness） | 每一个改变状态的动作 | [→](../works/gaia2.md) |
| QVal | 2026 | 方法评分与 reference policy Q 值的对齐程度 | 每个 state–action 对 | [→](../works/qval.md) |
| Hard2Verify | 2025 | 专家的二元步骤标签；首错索引 | 每个证明步骤 | [→](../works/hard2verify.md) |
| Who&When Pro | 2026 | 由受控错误注入得到的 golden agent / 步骤 / 错误模式标签 | 每一步；每条轨迹一个决定性步骤 | [→](../works/who-and-when-pro.md) |
| CUARewardBench | 2025 | 每个关键动作的专家二元正误标签，用于给 VLM 奖励模型打分 | 272 条已标注轨迹上选出的 346 个关键动作 | [→](../works/cuarewardbench.md) |
| ToolPRMBench | 2026 | 在正确动作与貌似合理的错误动作之间强制选择的准确率 | 单个决策步骤 | [→](../works/toolprmbench.md) |
| ProcessBench | 2024 | 专家标注的最早出错步骤索引 | 静态解答内的推理步骤 | [→](../works/processbench.md) |
| PRMBench | 2025 | 步骤级 validity + redundancy 评分；negative F1 与 PRMScore | 静态解答过程中的单个推理步骤 | [→](../works/prmbench.md) |
| FormalRewardBench | 2026 | 在已验证证明与注入错误变体之间的偏好判定 | 整份证明；无步骤级 credit | [→](../works/formalrewardbench.md) |
| OSReward | 2026 | 奖励模型裁决对照多阶段人工标注；Multi 变体给出细粒度的效率与对齐评分 | 整条 computer-use 轨迹，另有分维度评分 | [→](../works/osreward.md) |
| SearchAuditor | 2026 | 专家标注的关键步骤、搜索特有根因与带评分 rubric 的修复 | 失败搜索轨迹中的关键步骤 | [→](../works/searchauditor.md) |
| SkillSV | 2026 | 对 skill 编译单元的结构感知 Shapley 价值 | 每个 skill 单元，而非轨迹步骤 | [→](../works/skillsv.md) |
| TRAJDEBUG | 2026 | 错误生命周期：发生、解决状态、最终影响 | 失败轨迹中的每个错误 | [→](../works/trajdebug.md) |

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
- [OSReward](../works/osreward.md)
- [SearchAuditor](../works/searchauditor.md)
- [SkillSV](../works/skillsv.md)
- [TRAJDEBUG](../works/trajdebug.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
