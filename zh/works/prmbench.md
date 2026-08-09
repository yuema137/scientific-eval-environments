# PRMBench (2025)

> [English](../../works/prmbench.md) | **简体中文**

## Overview

PRMBench 是一个 benchmark，用于评估过程级奖励模型（PRMs）在多步推理链上的细粒度错误检测能力。它包含 6,216 个问题与 83,456 个 step 级标签，分布在 simplicity、soundness、sensitivity 三大类之下的九个错误子类中。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://aclanthology.org/2025.acl-long.1230/>
- **Project:** <https://prmbench.github.io/>
- **Code:** <https://github.com/ssmisya/PRMBench>
- **Venue:** ACL 2025

## Summary

PRMBench 认为，尽管语言模型会产生多种不同类型的推理错误，现有 benchmark 仍只关注 step 正确性，因而无法系统地评估 PRM。它构建了 6,216 个测试实例与 83,456 个 step 级标签，并将其组织为 simplicity、soundness、sensitivity 三个评估大类——再细分为九个子类。在 25 个受评模型上——涵盖开源 PRM 以及被提示作为 critic model 的开源与闭源 LLM——最佳总分为 68.8，人类标注者为 83.8。

## Tasks

6,216 个测试实例，携带 83,456 个 step 级标签，平均每个实例 13.4 个 step。每个实例由一个问题与一段逐步求解过程构成，其中特定 step 带有 ground-truth 负标签。实例分布在九个子类中——simplicity 之下的 non-redundancy 与 non-circular logic；soundness 之下的 empirical soundness、step consistency、domain consistency 与 confidence invariance；sensitivity 之下的 prerequisite sensitivity、deception resistance 与 multi-solution consistency——除 multi-solution consistency 为 165 个外，各子类各有 750–758 个实例。

## Domains

基于 PRM800K 衍生问题的数学推理，并在附录中由覆盖物理、化学与生物的 PRMBench-STEM 加以扩展。

## Evaluation

- **Step 级二分类。** 每个受评模型为每一 step 赋予一个 step 级有效性分数与一个 step 级冗余分数，并由该模型自身的阈值将这些分数转换为逐 step 的二元预测。
- **Negative F1。** 在负标签 step 上计算的 F1 分数，用作错误检测性能的直接度量。
- **PRMScore。** 将 negative F1 与 F1 加权求和得到的归一化分数，权重被设定为最大化模型之间的区分度；随机猜测的得分为 50.0。
- **人类 baseline。** 三名持有学士学位的标注者，每人负责由每个子类抽取 50 个实例构成的 450 样本 mini-test set 中的三个子类子集。
- **报告结果。** Gemini-2.0-thinking-exp-1219 在 25 个受评模型中以 68.8 的总分领先，人类为 83.8，而 Qwen2.5-Math-PRM-72B 是最强的开源 PRM，得分 68.2；o1-mini 与 DeepSeek-R1 在 394 样本子集而非完整数据集上评测，PRMBench 与 Best-of-N 评测之间的平均 Somers' D 相关性为 −0.05。

## Typical Duration

对平均 13.4 个 step 的固定求解过程进行单次评分，不存在交互循环。未说明：论文未给出每实例的 wall-clock、step 或 token 预算；成本仅作为将 o1-mini 与 DeepSeek-R1 限制在 394 样本子集上的理由出现。

## Main Contribution

一个细粒度的过程级 benchmark，将 PRM 错误检测拆解为 simplicity、soundness、sensitivity 之下的九个子类，并同时发布了自动化评估框架与可定制的数据生成系统。

## Key Design Ideas

- simplicity、soundness、sensitivity 三个评估大类——再细分为九个错误子类，使结果按错误类型而非整体 step 正确率呈现。
- 在 PRM800K 上进行错误注入：从其训练集与测试集中选出完全正确的解答，再由 GPT-4o 依照针对每一目标错误类别的提示改写。
- 采用 style-controlled 的数据构建，以使评估样本保持一致难度并缓解混杂变量。
- 一个不含错误 step 的 multi-solution consistency 子集，由 QwQ-32B-Preview 生成的其他正确解题路径构成。

## Strengths

- 按错误类型的分辨能力把 PRM 的弱点定位到具体的失效模式，而不是压缩成单一的 step 正确率数字。
- 通过扰动已验证正确的 PRM800K 解答获得精确的 ground-truth step 标签，且对 10% 实例的人工复核报告了超过 92% 的改写正确性合格率。
- 与 Best-of-N 结果之间接近零的 Somers' D 表明，该 benchmark 在 outcome 级选择准确率无法区分的维度上区分了模型。

## Limitations

- Repository note: 主 benchmark 的全部实例均源自 PRM800K 及其数学问题；物理、化学与生物的覆盖位于单独构建的 PRMBench-STEM 扩展中，且仅在附录中报告。
- Repository note: 错误 step 由提示 GPT-4o 改写正确解答合成而来，因此错误分布是类别专属提示所诱导的分布，而非从观察到的模型失败中采样得到的分布。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在端到端任务成功率之下衡量进展，但归因的是 agent 在交互式环境中的 subgoal 链，而非静态求解轨迹中的单个推理 step。
- [TRACE](./trace.md) — 同样评估中间推理而不只看最终答案，但直接对 agent trajectory 打分，而非把打分模型本身作为受评对象。
