# PG-HAP: Policy-Guided Stepwise Action Planning for Controllable LLM Reasoning (2026)

> [English](../../works/pg-hap.md) | **简体中文**

## 概览

PG-HAP 训练一个轻量 policy，逐步选择 high-level reasoning action，同时让 executor LLM 完全保持冻结。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — 通用数学与 commonsense reasoning 方法，没有直接评价科学或研究活动。

## Links

- **Paper:** <https://aclanthology.org/2026.findings-acl.2024/>
- **Code:** <https://github.com/john1226966735/PG-HAP>
- **Venue:** Findings of ACL 2026

## 摘要

Planner 可选 Analysis、Decomposition、Reasoning、Knowledge Recall、Code Generation/Refinement、Verification 和 Final Answer。Action-dependency mask 阻止无效或重复 transition，action-diversity reward 则防止所有问题坍缩成同一模板。Qwen2.5 executor 保持冻结，因此结果能更干净地反映 high-level policy 的作用。

## 任务

五个数学与常识 reasoning benchmark，包括 MATH、GSM8K、SVAMP、CommonsenseQA 和 StrategyQA；主实验使用冻结的 3B/7B executor。

## 领域

通用语言模型 reasoning，不对应某个 canonical 科学或工程领域。

## 评估

Answer accuracy、action-sequence distribution、structural redundancy、sequence collapse，以及 dependency masking 和 diversity reward 的 ablation。

## Typical Duration

没有报告固定的逐题时间或 token budget。

## 主要贡献

用一个 planner–executor 对照实验说明：不改 executor，只改 high-level action selection，也能改善 reasoning。

## Key Design Ideas

- 冻结 executor，只训练小型 action-selection policy。
- 限制 legal transition，并奖励 batch 内的 sequence diversity。

## Strengths

- Frozen executor 让性能变化可以更明确地归因给 planner。
- 显式 action trace 能暴露 final accuracy 看不到的重复和 collapse。

## 局限

- Action set 与 legal-transition graph 由人设计。
- 五个 benchmark 上减少 template collapse，不等于已经证明广泛 OOD transfer。
- Planner 优化 terminal correctness，没有 intermediate action 最优性的 ground truth。

## Related Works

- [MetaAct-RL](./metaact-rl.md)
- [HiPER](./hiper.md)
