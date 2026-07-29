# ProcessBench (2024)

> [English](../../works/processbench.md) | **简体中文**

## Overview

ProcessBench 是一个用于衡量识别数学推理中错误步骤能力的 benchmark，其中 judge 必须返回逐步解答中最早出现错误的步骤索引，或判定所有步骤均正确。它包含 3,400 个测试用例，取自四个数学数据集、以竞赛与奥林匹克级别的问题为主，每个用例将一道数学问题与一份模型生成的解答配对，该解答的错误位置由人类专家标注。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.06559>
- **Code:** <https://github.com/QwenLM/ProcessBench>
- **Venue:** ACL 2025

## Summary

ProcessBench 针对的局限在于：现有的推理过程评估 benchmark 或者所覆盖的问题对近期语言模型而言已经过于简单，或者只标注最终答案的正确性而不标注具体的错误步骤。该 benchmark 将竞赛与奥林匹克级别的数学问题同模型生成的逐步解答配对，解答中最早出现错误的位置由人类专家标注，并在其上评估两类 judge：process reward models (PRMs) 与被提示为 critic model 的通用语言模型。在四个子集上平均，o1-mini 达到 87.9 F1，最好的开源模型 QwQ-32B-Preview 达到 71.5，最好的现有开源 PRM 达到 42.1。

## Tasks

3,400 个测试用例，分为四个子集——GSM8K 400 个，MATH、OlympiadBench、Omni-MATH 各 1,000 个——每个用例将一道数学问题与一份模型生成的逐步解答配对。解答来自 Qwen 与 LLaMA 系列的十二个开源生成模型，并在标注前由 Qwen2.5-72B-Instruct 重新格式化为统一的段落级步骤。采样在最终答案正确与错误之间保持平衡——GSM8K 各 200 个，其余三个子集各 500 个——但专家标注发现，GSM8K 中最终答案正确的解答有 3.5% 含有过程错误，MATH 为 18.8%，OlympiadBench 为 32.2%，Omni-MATH 为 51.8%。

## Domains

数学推理，从 GSM8K 中的小学水平问题到 MATH、OlympiadBench、Omni-MATH 中的竞赛与奥林匹克级别问题。

## Evaluation

- **Earliest-error index.** 给定一个问题和一份包含 n 个步骤的解答，judge 输出索引 i ∈ {−1, 0, …, n−1}，其中 −1 表示所有步骤都正确，非负值则定位最早出现错误的步骤。
- **F1 score.** 在每个子集上分别计算错误样本与正确样本上的准确率，二者取调和平均，从而在过度批判与无法识别错误之间取得平衡。
- **Two judge families.** 对 process reward model，评分方式是从其逐步正确性预测中提取最早被判为错误的步骤，输出标量分数的 PRM 先经阈值二值化；通用语言模型则被提示逐步批判该解答，并以 boxed 形式返回索引作为最终答案。
- **Reported (Table 3, average over the four subsets).** o1-mini 87.9，QwQ-32B-Preview 71.5，GPT-4o-0806 61.9，作者微调的 Qwen2.5-Math-7B-PRM800K 56.5，以及作为最强现有开源 PRM 的 Skywork-PRM-7B 42.1。开源模型在八次采样的多数投票下评估，GPT-4o-0806 采用贪心解码，o1-mini 采用单次采样。

## Typical Duration

对单份静态解答的一次性评分，而非交互式 rollout；解答的平均步数随子集与标签落在 5.1–8.9 步之间。未说明：论文未给出 judge 的 wall-clock、步数或 token 预算，但协议固定了开源模型在八次采样上的多数投票。

## Main Contribution

一个包含 3,400 个用例的 benchmark，用于识别数学推理中最早出现的错误步骤，由竞赛与奥林匹克级别的问题、模型生成的解答以及专家的步骤级错误标注构建，并同时应用于 process reward model 与被提示的 critic model。

## Key Design Ideas

- 最早错误索引的输出格式，一种单整数协议，process reward model 与被提示的 critic model 都可在其下评分。
- 问题难度超出 GSM8K 与 MATH，提升到竞赛与奥林匹克级别的来源，并使用十二个不同的解答生成模型以获得解答多样性。
- 在标注前由 Qwen2.5-72B-Instruct 重新格式化解答以统一步骤粒度，并丢弃重新格式化后最终答案发生变化的解答。
- 三名标注者一致的要求，在无法达成共识时增加到五名标注者，否则丢弃该样本，整体丢弃率约 30%。

## Strengths

- 在自然生成的解答上进行专家标注，给出的错误位置不依赖于合成的错误注入流程。
- 单整数的输出格式使 process reward model 与被提示的通用语言模型可以在同一尺度上比较。
- 对最终答案正确与错误的解答进行平衡采样，使正确的最终答案建立在错误步骤之上的比例可被直接测量，从而把过程质量与结果正确性区分开。

## Limitations

- Repository note: 论文指出，错误位置的标签在更难的奥林匹克级别问题上可能仍不准确，并且因标注者无法达成一致而被丢弃的那约 30% 的解答，可能使问题分布偏向专家能够解决的情形。
- Repository note: 被评判的单位是一份静态的、预先生成的文本解答，而非 agent trajectory，因此最早错误索引定位的是单份解答内部的推理错误，不涉及工具调用、环境状态或跨轮次的动作。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在最终任务成功率之下进行评分，但它沿着标注的 subgoal 跟踪多轮环境交互中的进展，而不是在静态解答中定位单一的最早错误步骤。
- [TRACE](./trace.md) — 同样评估推理过程而不只是最终答案，但它在连续的质量维度上为整条 trajectory 评分，而不是把判定归结为单一的、由专家标注的错误索引。
