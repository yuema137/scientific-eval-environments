# Aviary (2024)

> [English](../../works/aviary.md) | **简体中文**

> **首次公开：** 2024-12-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2412.21154)

## Overview

Aviary 是一个面向 language agent 的可扩展 gymnasium，将 agent 形式化为在 language-grounded 部分可观测马尔可夫决策过程（POMDP）中求解的策略。它实现五个环境，其中三个为科学环境——DNA 构建操作（分子克隆）、科学文献研究与蛋白质工程——提供可复用的多步科学任务环境。本仓库为这些科学评估环境而收录它；论文的训练框架贡献是与本仓库范围相邻的 agent 构建工作（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)
- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.21154>
- **Code:** <https://github.com/Future-House/aviary>

## Summary

Aviary 将 language agent 形式化为在 language-grounded 部分可观测马尔可夫决策过程中行动的策略，并提供一个可扩展的环境 gymnasium 供其运行。它实现五个环境，其中三个为具挑战性的科学环境，聚焦 DNA 构建操作（分子克隆）、通过科学文献访问回答研究问题，以及蛋白质（稳定性）工程，均强调与当代生物学研究相关的多步推理。论文报告，由开源、非前沿 LLM 支撑的 language agent 能在多个任务上以至多 100× 更低的推理成本匹敌并超越前沿 LLM agent 与人类专家。

## Tasks

五个环境——两个非科学（**GSM8K** 小学数学；**HotpotQA** 基于 Wikipedia 的多跳问答）与三个科学环境：**SeqQA / 分子克隆**（DNA 构建操作；500 训练 / 约 140 测试题）、**LitQA2 / PaperQA**（从文献中回答研究问题；248 题，49 题留出测试）、**Protein Stability**（在 megascale 稳定性数据集的 40 个蛋白上提出稳定化突变）。

## Domains

分子生物学（分子克隆、蛋白质工程）与科学文献研究，另有两个非科学推理环境（GSM8K 数学、HotpotQA 多跳问答）。

## Evaluation

agent 作为 language-grounded POMDP 环境中的策略行动，每个环境提供一个终局奖励：

- **SeqQA 与 LitQA2**（多选）：正确 +1、错误 −1、“unsure” +0.1——稀疏的终局奖励；准确率为头号指标，多样本推理用 majority@k。
- **Protein Stability**：二元奖励——所提突变的 Rosetta ΔΔG < 0（稳定化）记 1，否则 0；以通过率报告。
- **GSM8K**：正确 +1、非法工具调用 −1、其余 0。**HotpotQA**：正确 +1、其余 0。

报告：经 expert iteration 训练的 Llama-3.1-8B agent 在 SeqQA 上达 0.89 准确率（多数投票；单样本 ≈0.86），匹敌或超过 Claude 3.5 Sonnet（≈0.87）；在 LitQA2 上两者均超过此前最佳 0.67，Claude 3.5 Sonnet 经多数投票达 0.89。成本：Claude 每条 SeqQA trajectory ≈$0.07，而 Llama-8B agent ≈$0.00066（约 100× 更便宜），人类 PhD 承包者每题 $4–$12。

## Typical Duration

每个环境至多 rollout 10 步，PaperQA / LitQA2 例外，允许至多 18 步。

## Main Contribution

论文陈述的贡献是作为 language agent gymnasium 的 Aviary，以及使小模型 agent 能匹敌前沿 agent 与人类专家的训练 / 推理时计算方法。在本仓库中，其在范围内的贡献是 Aviary 的科学环境作为可复用的评估环境。

## Key Design Ideas

- 将 agent 形式化为 language-grounded 部分可观测 MDP 上的策略。
- 在一个抽象下承载多个环境的可扩展 gymnasium。
- 三个科学环境（分子克隆、文献研究、蛋白质工程），强调多步推理。
- 通过在线训练与推理时计算扩展展示了强的成本–性能权衡（至多 100× 更低推理成本）。

## Strengths

- 在统一 agent 抽象下提供可复用、可扩展的科学任务环境。
- 科学环境根植于当代生物学研究问题。
- 报告了一个引人注目的成本–性能结果，重构了前沿对开源的比较。

## Limitations

- Repository note: 论文的主要框架是*训练* language agent（在线训练、推理时计算扩展）——属于本仓库以评估为核心的范围之外的 agent 构建工作。此处为 Aviary 的科学环境作为评估环境而收录，而非为训练方法。
- Repository note: 已发布代码已偏离论文中的五个环境（仓库现打包 GSM8K、HotpotQA、LFRQA、一个 Notebook 环境与 LAB-Bench，其中 LitQA 并入 LAB-Bench）。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样评估 agent 在科学任务上的能力，但作为专家验证任务的固定 benchmark，而非可扩展的训练兼评估 gymnasium。
- [SciAgentArena](./sciagentarena.md) — 同为面向 agent 的交互式科学研究环境，跨尺度进行逐步验证。
