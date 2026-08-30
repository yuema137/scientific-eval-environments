# HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents (2026)

> [English](../../works/hiper.md) | **简体中文**

> **首次公开：** 2026-02-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.16165)

## 概览

HiPER 把 interactive LLM-agent policy 分成提出 subgoal 的高层 planner 与执行环境 action 的低层 executor，并在两层分别分配 RL credit。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 使用通用 household 与 web-shopping agent task，没有评价科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2602.16165>
- **Venue:** arXiv preprint, 2026

## 摘要

Flat agent RL 只有一个时间尺度，要把稀疏 terminal reward 传过很长的 action sequence。HiPER 让高层 policy 先提出 subgoal，再由 executor 用多个环境 action 完成它。Hierarchical Advantage Estimation 在每个 subgoal 内聚合 return，并协调 planner 与 executor 的更新。

## 任务

使用 Qwen2.5-1.5B-Instruct 和 7B-Instruct 完成 ALFWorld 与 WebShop 的 interactive text-agent task。

## 领域

通用 embodied household 与 web interaction，没有 canonical 科学或工程领域映射。

## 评估

Task success、训练稳定性与效率、按 horizon 的表现，以及 hierarchical policy 和 advantage estimation 的 ablation。论文报告 7B 模型在 ALFWorld 达 97.4%，WebShop 达 83.3%。

## Typical Duration

Episode 是可变长度多轮交互，没有统一 wall-clock 时长。

## 主要贡献

在 multi-turn LLM-agent post-training 中，把 temporal action abstraction 与分层 credit assignment 直接连起来。

## Key Design Ideas

- 每个 high-level subgoal 跨越多个 low-level action。
- 在 subgoal segment 内聚合 return，并协调更新两层 policy。

## Strengths

- 直接评价 long-horizon interactive agent，不只做静态 reasoning。
- 同时给出 credit estimator 的理论与实证分析。

## 局限

- 只覆盖两个通用模拟环境。
- Subgoal 质量主要由最终 task success 反推，没有独立标注。
- Planner 与 executor 的接口会产生新的 grounding error，需要单独诊断。

## Related Works

- [PG-HAP](./pg-hap.md)
- [MA-RLHF](./ma-rlhf.md)
