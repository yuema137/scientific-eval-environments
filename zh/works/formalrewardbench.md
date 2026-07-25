# FormalRewardBench (2026)

## Overview

FormalRewardBench 是一个评估 reward model 能否在正确与错误的 Lean 4 证明之间做出正确偏好的 benchmark。它包含 250 个 preference pair，每一对将一个经形式化验证的正确证明与由五种专家设计的错误注入策略之一生成的错误变体配对。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.10141>
- **Code:** <https://github.com/GGLAB-KU/formal_rewardbench>

## Summary

FormalRewardBench 针对 reinforcement learning with verifiable rewards 中稀疏的 credit assignment 问题：一次已取得实质进展但在最后一步失败的证明尝试，与一个完全错误的方法获得同样的零奖励。作者认为这种稀疏性促使人们转向能够超越二值验证来判断证明质量的学习式 reward model，但比较这类 reward model 通常需要昂贵的 RL 训练消融实验。他们将 FormalRewardBench 作为首个面向 Lean 4 形式化定理证明的 reward model 评估 benchmark 提出，并在 frontier LLM、judge LLM、通用 LLM 与专用定理证明模型上运行。

## Tasks

250 个 preference pair，五种错误注入策略各采样 50 个：最小单点变异、自然语言辩护、Python 代码注入、强制 LLM 错误、冗长错误证明。定理陈述取自 MiniF2F，即 488 道以 Lean 4 形式化的奥赛级问题，来自 AMC、AIME 与 IMO 竞赛。正确证明来自 DeepSeek-Prover-V2-671B，错误变体以 Claude Opus 4.5 作为提示模型生成，候选须通过语法有效性、类型检查失败与非平凡性过滤后再行采样。

## Domains

Lean 4 中的形式化数学：奥赛级代数、数论与组合数学。

## Evaluation

- **Pointwise 准确率。** 模型独立为每个证明打分；当正确证明获得的分数高于错误证明获得的分数时，该样本计为正确。
- **Pairwise 准确率（位置一致）。** 模型直接比较两个证明，只有在两种呈现顺序下判断都正确时，该样本才计为正确。
- **Position bias 分析。** 分别报告正确证明在前与正确证明在后两种顺序下的准确率，并给出一致性与作答一致率。
- **分策略结果。** 按五种错误注入策略分别报告 pairwise 准确率，呈现出以 Python 代码注入最易、冗长错误证明与强制 LLM 错误最难的难度梯度。
- **报告。** Claude Opus 4.5 表现最佳，pointwise 70.1%、pairwise 59.8%；专用定理证明模型中最强的 Gödel-Prover-V2-32B 为 pairwise 24.4%，DeepSeek-Prover-V2-7B 为 pointwise 13.7%、pairwise 9.4%。最佳模型在冗长错误证明上达到 60%，在强制 LLM 错误上达到 50%。作者报告多数模型的表现处于或低于随机 baseline。

## Typical Duration

面向完整证明的单轮偏好判断；不存在交互 horizon 或多步 rollout。未说明：论文未给出逐条目的 wall-clock、步数或 token 预算。

## Main Contribution

一个由专家设计的错误注入构建的 250 对 Lean 4 preference pair benchmark，使形式化定理证明的 reward model 无需昂贵的 RL 训练消融实验即可直接比较。

## Key Design Ideas

- 通过向经形式化验证的正确证明合成注入错误来控制难度。
- 五种针对不同 reward model 弱点的错误注入策略：最小单点变异、自然语言辩护、Python 代码注入、强制 LLM 错误、冗长错误证明。
- 对经由 Lean 的那几种策略，由 Lean 类型检查器给出客观偏好标签——正确证明通过检查，错误变体则无法通过。
- 配对使用 pointwise 与 pairwise 两套协议，其中 pairwise 准确率要求在两种呈现顺序下判断一致。

## Strengths

- 由类型检查器导出的标签给出确定性的 ground truth，无需人工偏好标注。
- 各错误策略彼此分离，因此分类别结果可定位 reward model 易受哪一种失败模式影响。
- 在同一协议下覆盖 frontier、judge、通用与证明专用模型，暴露出仅评估单一模型族无法揭示的 generation–evaluation gap。

## Limitations

- Repository note: 判断针对完整证明且为单轮——论文声明其不考虑 process-level 或逐步评估，因此 credit 被赋予一个完整证明，而非单个 tactic 步骤。
- Repository note: 标签主要依赖自动验证，作者仅人工检查了 250 对中的 50 对；所有样本均为 Lean 4 下的 MiniF2F 问题，未评估向其他证明助手的迁移。

## Related Works

- [AgentBoard](./agentboard.md) — 同样出于单一二值结果过于粗糙的动机，但对 trajectory 内部标注的子目标给分，而非把一个完整证明作为单一单元打分。
- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — 同样针对稀疏的二值端到端任务奖励，但通过分级子任务提供密集部分得分，而非评测能给出更密集信号的 reward model。
- [TRACE](./trace.md) — 同样把学习式 judge 置于打分的核心，但将 judge 用作评判 trajectory 的工具，而非把 judge 本身作为被评估对象。
