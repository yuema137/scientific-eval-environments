# Evaluator Reliability & Validation

> [English](../../topics/evaluator_reliability_validation.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Evaluator 也是一套 measurement system，不是 oracle。LLM judge 给一条 trajectory 打了 8/10，下一步真正该问的是：它和 expert 是否一致？能不能把更好的 run 排在前面？换个 wording 或 candidate order，结果会不会变？

可以拿 100 条 expert-labeled trajectory，让 judge 全部打一次分，再分别看 false pass、false failure，并交换展示顺序重测。这是在用 judge 排 agent 或提供 reward 之前，先评价 judge 自己。即便这批数据上一致性很高，也不能保证 agent 改变行为、开始钻 judge 空子以后仍然可靠。

## 定义

Evaluator 把一次 agent run 变成分数、排名或 reward。它可以是确定性 verifier、专家 rubric、reward model、LLM judge，也可以把几种方法组合起来。这个 topic 检查它能不能给出正确 verdict，能不能如实表达不确定性，换个无关的展示方式会不会变分，以及这个分数到了下游是不是真能用。

## 为什么重要

分数会把 evaluator 的错误一起带到下游。Judge 可能在简单样例上和专家一致，但一换 candidate order 就颠倒排名，或者偏爱长答案，遇到和 validation set 不同的 trajectory 就失灵。在用它排 leaderboard 或提供 training reward 之前，先得用专家 ground truth、calibration check 和压力测试来评价 evaluator 自己。

## 现有方法

- **专家标注的 trajectory。** [AgentRewardBench](../works/agentrewardbench.md) 与 [MobileJudgeBench](../works/mobilejudgebench.md) 分别用 web 和 mobile agent 的专家结果检验自动 judge。
- **成对偏好。** [Plan-RewardBench](../works/plan-rewardbench.md) 交换候选顺序，测试 evaluator 能否从易混淆的工具 trajectory 中选出较优者。
- **需要 skill 知识的判断。** [SkillTV-Bench](../works/skilltv-bench.md) 检查 judge 能否验证依赖特定 skill 的执行过程。
- **混合验证。** [AgentLens](../works/agentlens.md) 把形式化检查、多个 judge 维度和带证据的文字审查结合起来。
- **领域校准。** [AstroVisBench](../works/astrovisbench.md)、[PSE-Bench](../works/pse-bench.md) 和 [FIRE-Bench](../works/fire-bench.md) 都报告科学输出 judge 与人类专家的一致程度。

## 方法对比

| Work | 被检验的 evaluator | Ground truth | 可靠性信号 | 下游验证 |
|---|---|---|---|---|
| AgentRewardBench | web-agent 的 LLM 与规则 evaluator | 专家 trajectory 标签 | 多 benchmark 上的 precision、recall 与一致性 | Agent 评估 |
| MobileJudgeBench | 六种 mobile judge 方法 × 五个 backbone | 931 条人工标注 trajectory | 分类指标、排名相关、成功率误差 | Agent 排名与 on-policy reward |
| Plan-RewardBench | Reward model 与 LLM judge | 经验证的成对偏好 | 交换顺序后的 pairwise accuracy | 无 |
| SkillTV-Bench | LLM-as-a-Judge 与 Agent-as-a-Judge | 需要 skill 知识的 trajectory 标签 | Judge accuracy 与 best-of-N 选择 | Trajectory 选择 |
| AgentLens | 混合 judge 与形式化 verifier | 可执行检查和审查证据 | 多维质量指数 | Coding agent 诊断 |
| AstroVisBench | 多模态可视化 judge | 专业天文学家标注 | 排名相关与标注者一致性 | Judge 选择 |

## 还没解决的问题

- 哪些 judge 指标真能预测排名、reward 和部署决策是否可靠？
- Evaluator 的不确定性应如何传递到 leaderboard 和统计比较？
- 没有完整 oracle 时，怎样测 verifier 的覆盖范围与漏判面？
- Pairwise、pointwise、rubric 和确定性 evaluator 各自在什么条件下失效？
- 怎样抵抗 reward hacking、文风偏差、contamination 和针对 evaluator 的自适应优化？

## 相关工作

- [AgentRewardBench](../works/agentrewardbench.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [AgentLens](../works/agentlens.md)
- [AstroVisBench](../works/astrovisbench.md)
- [PSE-Bench](../works/pse-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
