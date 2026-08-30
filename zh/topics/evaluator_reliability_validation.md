# Evaluator Reliability & Validation

> [English](../../topics/evaluator_reliability_validation.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Evaluator 也是一套 measurement system，不是 oracle。LLM judge 给一条 trajectory 打了 8/10，下一步真正该问的是：它和 expert 是否一致？能不能把更好的 run 排在前面？换个 wording 或 candidate order，结果会不会变？

可以拿 100 条 expert-labeled trajectory，让 judge 全部打一次分，再分别看 false pass、false failure，并交换展示顺序重测。这是在用 judge 排 agent 或提供 reward 之前，先评价 judge 自己。即便这批数据上一致性很高，也不能保证 agent 改变行为、开始钻 judge 空子以后仍然可靠。

## Definition

这个 topic 研究给 agent 打分的 evaluator 是否准确、校准良好、经得住分布变化，而且真的适合后续用途。Evaluator 不只包括 LLM judge，也包括确定性 verifier、专家 rubric、reward model 和混合系统。

## Motivation

Agent 的分数是否可信，取决于 evaluator。它在简单样例上同意人类，并不表示它能稳定地给 agent 排名、提供可靠 reward，或抵抗位置、文风、长度和 trajectory 分布变化。因此，evaluator 本身也需要 ground truth、误差分析和压力测试。

## Existing Approaches

- **专家标注的 trajectory。** [AgentRewardBench](../works/agentrewardbench.md) 与 [MobileJudgeBench](../works/mobilejudgebench.md) 分别用 web 和 mobile agent 的专家结果检验自动 judge。
- **成对偏好。** [Plan-RewardBench](../works/plan-rewardbench.md) 交换候选顺序，测试 evaluator 能否从易混淆的工具 trajectory 中选出较优者。
- **需要 skill 知识的判断。** [SkillTV-Bench](../works/skilltv-bench.md) 检查 judge 能否验证依赖特定 skill 的执行过程。
- **混合验证。** [AgentLens](../works/agentlens.md) 把形式化检查、多个 judge 维度和带证据的文字审查结合起来。
- **领域校准。** [AstroVisBench](../works/astrovisbench.md)、[PSE-Bench](../works/pse-bench.md) 和 [FIRE-Bench](../works/fire-bench.md) 都报告科学输出 judge 与人类专家的一致程度。

## Comparison

| Work | 被检验的 evaluator | Ground truth | 可靠性信号 | 下游验证 |
|---|---|---|---|---|
| AgentRewardBench | web-agent 的 LLM 与规则 evaluator | 专家 trajectory 标签 | 多 benchmark 上的 precision、recall 与一致性 | Agent 评估 |
| MobileJudgeBench | 六种 mobile judge 方法 × 五个 backbone | 931 条人工标注 trajectory | 分类指标、排名相关、成功率误差 | Agent 排名与 on-policy reward |
| Plan-RewardBench | Reward model 与 LLM judge | 经验证的成对偏好 | 交换顺序后的 pairwise accuracy | 无 |
| SkillTV-Bench | LLM-as-a-Judge 与 Agent-as-a-Judge | 需要 skill 知识的 trajectory 标签 | Judge accuracy 与 best-of-N 选择 | Trajectory 选择 |
| AgentLens | 混合 judge 与形式化 verifier | 可执行检查和审查证据 | 多维质量指数 | Coding agent 诊断 |
| AstroVisBench | 多模态可视化 judge | 专业天文学家标注 | 排名相关与标注者一致性 | Judge 选择 |

## Open Questions

- 哪些 judge 指标真能预测排名、reward 和部署决策是否可靠？
- Evaluator 的不确定性应如何传递到 leaderboard 和统计比较？
- 没有完整 oracle 时，怎样测 verifier 的覆盖范围与漏判面？
- Pairwise、pointwise、rubric 和确定性 evaluator 各自在什么条件下失效？
- 怎样抵抗 reward hacking、文风偏差、contamination 和针对 evaluator 的自适应优化？

## Related Works

- [AgentRewardBench](../works/agentrewardbench.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [AgentLens](../works/agentlens.md)
- [AstroVisBench](../works/astrovisbench.md)
- [PSE-Bench](../works/pse-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
