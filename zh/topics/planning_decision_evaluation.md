# Planning & Decision-Making Evaluation

> [English](../../topics/planning_decision_evaluation.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

Planning & Decision-Making Evaluation 衡量的是：面对当时已知的状态、目标、约束、可用工具和证据，agent 能否选出合理的动作、动作序列或计划。它涵盖完整计划生成、约束满足、工具与动作选择、依据反馈重新规划、识别不可行任务，以及相对于其他有效方案评价计划质量。

## Motivation

端到端成功把规划、执行、工具操作、感知、状态跟踪和恢复揉在一起。一次运行失败，不能直接证明计划本身有问题；同样，一步动作即便局部成功，相对于更好的选择仍可能付出很高的机会成本。规划专项评估把决策本身变成可观察对象：agent 下一步应当做什么，这个选择为什么合理，状态变化后又应如何修改计划？

它不同于 long-horizon evaluation，后者描述任务需要多长的连续交互；也不同于 trajectory evaluation，后者评价已经产生的动作序列。规划任务可以像 [NATURAL PLAN](../works/natural-plan.md) 一样不调用工具、一次回答完成；长 trajectory 也可能因为与规划无关的原因失败；而 trajectory 指标未必判断每一步在当时信息条件下是否明智。

## Existing Approaches

相关文献从受控的计划有效性逐渐走向更现实、面向 agent 的决策：

- **形式化、可验证的规划。** [PlanBench](../works/planbench.md) 把经典规划领域转成自然语言，用形式化 planner 和 validator 评价计划生成、成本最优性、状态推断与重新规划；其混淆版本还检验模型究竟在遵循转移规则，还是在套用熟悉词汇模式。
- **自然语言约束规划。** [NATURAL PLAN](../works/natural-plan.md) 将所需的航班、地图和日历信息全部放进上下文，去掉工具执行这一混淆因素，同时改变城市、参与者、日程与约束数量。
- **现实约束下的工具化规划。** [TravelPlanner](../works/travelplanner.md) 要求 agent 从封闭的多工具 sandbox 检索信息，制定同时满足环境、常识和明确用户约束的行程，并分别报告分项约束通过率与完整计划可行率。
- **面向 agent 的规划诊断。** [Agent Planning Benchmark](../works/agent-planning-benchmark.md) 明确区分整体计划和基于反馈的一至三步决策，再分别加入无关工具、带替代项的坏工具，以及逻辑上无解的任务。
- **以执行结果为依据的具身规划。** [LoTa-Bench](../works/lota-bench.md) 在 simulator 中执行语言模型的计划并按目标完成度评分；[Embodied Agent Interface](../works/embodied-agent-interface.md) 则依据 simulator 状态定位 affordance 与规划错误。
- **参考计划与过程比较。** [AISE-Bench](../works/aise-bench.md) 计算生成计划与人工 gold plan 的图编辑距离；[SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) 为实现规划提供经过验证的 ground truth；[RigorBench](../works/rigorbench.md) 将 planning fidelity 与工程结果分开计分。
- **计划与 trajectory 偏好。** [Plan-RewardBench](../works/plan-rewardbench.md) 要求 evaluator 在两条易混淆的工具 trajectory 中选出更优者，其中设有单轮与多轮 planning split。这条路线评价的是计划的 judge，而不是 planner 本身。
- **科学项目规划。** [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) 固定研究目标，用专家与模型 panel 评价真实物理和天文项目 proposal 中的方法、资源、可行性、时间安排和风险。

## Comparison

| Work | 规划对象 | 信息与反馈 | 有效性或质量信号 | 是否隔离执行 | 反事实替代方案 |
|---|---|---|---|---|---|
| PlanBench | 完整形式化计划；重新规划后的后缀 | 明确动作模型、初态与目标；重规划时给改变后的状态 | solver / validator 正确性与成本最优性 | 是 | 一类任务有最优成本参考 |
| NATURAL PLAN | 自然语言行程或日程 | 所有工具信息随上下文给出；没有实时反馈 | 与标准计划 exact match | 是 | 否 |
| TravelPlanner | 以工具信息为依据的多日行程 | 工具检索与环境反馈 | 确定性的环境、常识、硬约束与最终通过率 | 否 | 否 |
| Agent Planning Benchmark | 整体计划或后续 1–3 步 | 整体模式给完整任务；逐步模式给 trajectory 前缀和反馈 | 正确性、分级 rubric、E1–E6 错误 | 是；另测下游迁移 | 有替代工具和拒绝情形，但无穷举 regret 指标 |
| LoTa-Bench | 可执行的具身计划 | simulator 观察 | 执行后的目标满足度 | 否 | 否 |
| Embodied Agent Interface | 具身 agent 各模块的决策 | simulator 状态与 affordance | 基于状态的规划错误诊断 | 否 | 否 |
| AISE-Bench | 工具/API 计划图 | 每题 query 与工具环境 | 与标注 gold plan 的图编辑距离 | 部分 | 一条标注参考计划 |
| SWE-RPG | 需求与实现计划 | repository issue 与代码上下文 | 对齐已验证规划 ground truth，并结合可执行 patch 检查 | 部分 | 否 |
| RigorBench | 工程计划及执行中的遵循情况 | repository 状态与执行 trajectory | planning-fidelity 分项，与结果分开报告 | 否 | 否 |
| Plan-RewardBench | 一对工具 trajectory | 完整对话、工具、调用和输出记录 | gold pairwise preference | 评价 judge，不执行环境 | 每对一个易混淆替代项 |
| AI's Capability in Assisting Scientific Research II | 一页研究 proposal | 固定的专家撰写标题、背景和目标 | 人类与 LLM rubric 分数 | 是 | 每个项目含一份人类与三份模型 proposal |

## Open Questions

- **反事实决策质量与 regret。** 合法动作仍可能让全局结果变差。如果无法穷举分支，也没有可信 simulator，如何估计选择 `a_t` 而非最佳备选动作所付出的机会成本 `V(s_t, a_t*) - V(s_t, a_t)`？
- **决策时的信息边界。** 事后 judge 很容易偷看动作发生后才出现的观察。benchmark 如何严格限定 agent 在时刻 `t` 能看到的信息，同时又合理利用后续结果作为证据？
- **规划与执行归因。** 好计划可能执行失败，差计划也可能靠恢复成功。什么样的干预或配对运行设计，才能识别 planner 对结果的因果贡献？
- **多个有效计划。** exact match 和单一 gold plan 距离会误罚正当替代方案，开放式 rubric judge 又可能不稳定。怎样表达一组或一个分布的有效计划，同时不让验证变得不可处理？
- **不可逆变化下的重新规划。** 现有测试常注入坏工具或状态变化；真实科学与工程工作还会改变证据、预算、安全边界和后续选择价值。评估需要区分审慎调整与来回摇摆。
- **资源感知的动作选择。** Resource-aware evaluation 问花了多少；planning evaluation 问为什么把资源花在这个动作上，而不是另一个。联合 benchmark 需要估计考虑成本后的决策价值，又不能把成本和任务质量压进一个不透明总分。
- **长 horizon 中局部合理选择的累计影响。** 一条序列可能每一步都没有明显错误，最后却走向差结果。如何评价局部说得通、但累计战略效果有害的决策，仍是开放问题。

## Related Works

- [PG-HAP](../works/pg-hap.md) — 对 high-level reasoning action 做逐步 policy selection。
- [HiPER](../works/hiper.md) — 把 high-level subgoal planning 与 low-level execution 分开。
- [PTA-GRPO](../works/pta-grpo.md) — 同时优化短 plan guidance 与详细 reasoning。
- [PlanBench](../works/planbench.md) — 形式化计划生成、最优性、验证与重新规划。
- [NATURAL PLAN](../works/natural-plan.md) — 工具信息随上下文提供的自然语言约束规划。
- [TravelPlanner](../works/travelplanner.md) — 多类约束下的现实工具规划。
- [Agent Planning Benchmark](../works/agent-planning-benchmark.md) — 整体、基于反馈、稳健性与不可行性诊断。
- [LoTa-Bench](../works/lota-bench.md) — 在 simulator 中执行的具身规划。
- [Embodied Agent Interface](../works/embodied-agent-interface.md) — 依据状态定位具身规划失败。
- [AISE-Bench](../works/aise-bench.md) — 对照 gold plan graph 评价工具学习中的规划。
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) — repository issue 解决中的经验证实现规划 ground truth。
- [RigorBench](../works/rigorbench.md) — 与工程结果分开计分的 planning fidelity。
- [Plan-RewardBench](../works/plan-rewardbench.md) — 含专项 planning split 的工具 trajectory 成对评价。
- [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) — 以专家 rubric 评价真实科研项目计划。
