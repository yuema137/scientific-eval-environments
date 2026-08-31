# Planning & Decision-Making Evaluation

> [English](../../topics/planning_decision_evaluation.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

最终结果不能说明 agent 一开始选的 plan 好不好。好 plan 可能因为工具崩溃而失败，差 plan 也可能靠昂贵的重试硬救回来。Planning evaluation 要把「当时掌握这些信息时，为什么选这一步」单独拿出来测。

比如一次训练的效果变差了。Agent 可以马上改 learning rate，也可以先做一个低成本诊断，区分问题来自数据漂移还是优化失败。两种动作都合法，但预期收益和机会成本不一样。这个 topic 研究怎样给这次选择和后续 replanning 打分。它不负责判断任务够不够长，也不只是事后描述 trajectory。

## 定义

Planning evaluation 先把决策时可用的信息固定下来，再问 agent 选的下一步或整份 plan 是不是合理。Evaluator 可以检查约束，比较其他可行方案，测 tool selection，验证完整 plan，也可以看 agent 收到 feedback 后会不会 replanning，遇到无解任务能不能承认无解。

## 为什么重要

端到端成功把 planning、execution、perception、tool use、state tracking 和 recovery 混在了一起。好 plan 可能在执行时失败，差 plan 也可能靠重试撑到成功。就算一步在局部上成功，它也可能错过了价值高得多的另一步。Planning evaluation 要把选择本身分离出来：下一步应该做什么，当时这个选择是不是说得通，新 evidence 出现后又该怎样改。

它不等于任务很长，也不等于给 trajectory 打分。[NATURAL PLAN](../works/natural-plan.md) 不用工具，一次回答就可以测 planning。一条很长的 run 可能因为与 plan 无关的原因失败，trajectory metric 也可能只描述过程，并不判断每一步在当时是不是最好选择。

## 现有方法

相关文献从受控的计划有效性逐渐走向更现实、面向 agent 的决策：

- **形式化、可验证的规划。** [PlanBench](../works/planbench.md) 把经典规划领域转成自然语言，用形式化 planner 和 validator 评价计划生成、成本最优性、状态推断与重新规划；其混淆版本还检验模型究竟在遵循转移规则，还是在套用熟悉词汇模式。
- **自然语言约束规划。** [NATURAL PLAN](../works/natural-plan.md) 将所需的航班、地图和日历信息全部放进上下文，去掉工具执行这一混淆因素，同时改变城市、参与者、日程与约束数量。
- **现实约束下的工具化规划。** [TravelPlanner](../works/travelplanner.md) 要求 agent 从封闭的多工具 sandbox 检索信息，制定同时满足环境、常识和明确用户约束的行程，并分别报告分项约束通过率与完整计划可行率。
- **面向 agent 的规划诊断。** [Agent Planning Benchmark](../works/agent-planning-benchmark.md) 明确区分整体计划和基于反馈的一至三步决策，再分别加入无关工具、带替代项的坏工具，以及逻辑上无解的任务。
- **以执行结果为依据的具身规划。** [LoTa-Bench](../works/lota-bench.md) 在 simulator 中执行语言模型的计划并按目标完成度评分；[Embodied Agent Interface](../works/embodied-agent-interface.md) 则依据 simulator 状态定位 affordance 与规划错误。
- **参考计划与过程比较。** [AISE-Bench](../works/aise-bench.md) 计算生成计划与人工 gold plan 的图编辑距离；[SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) 为实现规划提供经过验证的 ground truth；[RigorBench](../works/rigorbench.md) 将 planning fidelity 与工程结果分开计分。
- **计划与 trajectory 偏好。** [Plan-RewardBench](../works/plan-rewardbench.md) 要求 evaluator 在两条易混淆的工具 trajectory 中选出更优者，其中设有单轮与多轮 planning split。这条路线评价的是计划的 judge，而不是 planner 本身。
- **科学项目规划。** [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) 固定研究目标，用专家与模型 panel 评价真实物理和天文项目 proposal 中的方法、资源、可行性、时间安排和风险。

## 方法对比

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

## 还没解决的问题

- **反事实决策质量与 regret。** 合法动作仍可能让全局结果变差。如果无法穷举分支，也没有可信 simulator，如何估计选择 `a_t` 而非最佳备选动作所付出的机会成本 `V(s_t, a_t*) - V(s_t, a_t)`？
- **决策时的信息边界。** 事后 judge 很容易偷看动作发生后才出现的观察。benchmark 如何严格限定 agent 在时刻 `t` 能看到的信息，同时又合理利用后续结果作为证据？
- **规划与执行归因。** 好计划可能执行失败，差计划也可能靠恢复成功。什么样的干预或配对运行设计，才能识别 planner 对结果的因果贡献？
- **多个有效计划。** exact match 和单一 gold plan 距离会误罚正当替代方案，开放式 rubric judge 又可能不稳定。怎样表达一组或一个分布的有效计划，同时不让验证变得不可处理？
- **不可逆变化下的重新规划。** 现有测试常注入坏工具或状态变化；真实科学与工程工作还会改变证据、预算、安全边界和后续选择价值。评估需要区分审慎调整与来回摇摆。
- **资源感知的动作选择。** Resource-aware evaluation 问花了多少；planning evaluation 问为什么把资源花在这个动作上，而不是另一个。联合 benchmark 需要估计考虑成本后的决策价值，又不能把成本和任务质量压进一个不透明总分。
- **长 horizon 中局部合理选择的累计影响。** 一条序列可能每一步都没有明显错误，最后却走向差结果。如何评价局部说得通、但累计战略效果有害的决策，仍是开放问题。

## 相关工作

- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) — repository issue 解决中的经验证实现规划 ground truth。
- [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) — 以专家 rubric 评价真实科研项目计划。
- [RigorBench](../works/rigorbench.md) — 与工程结果分开计分的 planning fidelity。
- [AISE-Bench](../works/aise-bench.md) — 对照 gold plan graph 评价工具学习中的规划。
- [Agent Planning Benchmark](../works/agent-planning-benchmark.md) — 整体、基于反馈、稳健性与不可行性诊断。
- [PG-HAP](../works/pg-hap.md) — 对 high-level reasoning action 做逐步 policy selection。
- [Plan-RewardBench](../works/plan-rewardbench.md) — 含专项 planning split 的工具 trajectory 成对评价。
- [HiPER](../works/hiper.md) — 把 high-level subgoal planning 与 low-level execution 分开。
- [PTA-GRPO](../works/pta-grpo.md) — 同时优化短 plan guidance 与详细 reasoning。
- [Embodied Agent Interface](../works/embodied-agent-interface.md) — 依据状态定位具身规划失败。
- [NATURAL PLAN](../works/natural-plan.md) — 工具信息随上下文提供的自然语言约束规划。
- [LoTa-Bench](../works/lota-bench.md) — 在 simulator 中执行的具身规划。
- [TravelPlanner](../works/travelplanner.md) — 多类约束下的现实工具规划。
- [PlanBench](../works/planbench.md) — 形式化计划生成、最优性、验证与重新规划。
