# Hard2Verify (2025)

> [English](../../works/hard2verify.md) | **简体中文**

## Overview

Hard2Verify 是一个 benchmark，用于评估 step-level verifier 为最新开放式 Olympiad 数学题的 frontier 模型证明逐步打分的能力。它包含针对 80 道竞赛题的 200 份模型生成解答中的 1,860 个专家标注步骤，由超过 500 小时的人力投入产生。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.13744>
- **Code:** <https://github.com/SalesforceAIResearch/Hard2Verify>
- **Venue:** ACL 2026

## Summary

Hard2Verify 认为现有的 step-level 验证 benchmark 尚未触及 frontier，它们依赖简单题或短答案题，以及人工撰写或合成注入错误的解答，而非自然产生的 frontier 模型错误。作者从十场近期 Olympiad 中筛选出 80 道题，用 GPT-5、Gemini 2.5 Pro 和 Claude Sonnet 4 为每道题各采样一份解答，并请数学专家在严格评分标准下标注最终保留的 200 份回答的每一个步骤，任何由先前错误推导而来的步骤一律判为错误。在被评测的 29 个 generative critic 与 process reward model 中，GPT-5 在步骤级正确性上以 86.53 Balanced Accuracy 领先，但在首个错误定位上仅为 70.61；除少数突出者外，开源 verifier 落后于闭源模型。

## Tasks

针对 80 道题的 200 份模型生成解答，共 1,860 个标注步骤；题目取自 2024 年及以后的十场 Olympiad，其中包括 IMO Shortlist、Putnam、EGMO 和 USAMO。解答来自 GPT-5（high reasoning）、Gemini 2.5 Pro 和 Claude Sonnet 4（Thinking），使用统一的考试式证明 prompt，禁用网页搜索与代码解释器，每个模型对每道题各产出一份解答；78.5% 的样本为开放式。官方竞赛解答经 MathPix 从 PDF 解析为 LaTeX，依赖图像的题目被排除，输出退化或仅含少量冗长密集步骤的回答在标注前被过滤。

## Domains

开放式竞赛数学：英文、纯文本的 Olympiad 式证明题，排除依赖图像的题目。

## Evaluation

- **Step-Level.** 验证器为解答的每一个步骤输出二元的正确 / 错误标签；PRM 的步骤分数通过在随机抽取的 100 份回答子集上调好的阈值转换为二元标签。
- **Response-Level.** 只有当一份回答中的每个步骤都被标为正确时，该回答才算正确，从而由步骤标签导出结果级判定。
- **ErrorID.** 验证器输出第一个包含错误的步骤索引，若无错误则输出 −1；对 PRM 则取第一个低于正确性阈值的步骤。
- **Balanced Accuracy and Balanced F1.** 验证器 true positive rate 与 true negative rate 的算术平均与调和平均；前者反映两种模式下的平均表现，后者惩罚不平衡的表现。
- **Reported (Table 2).** GPT-5 在三项任务上均领先，Step-Level、Response-Level 与 ErrorID 的 Balanced Accuracy 分别为 86.53、89.69 和 70.61；gpt-oss-120B 是最强的开源权重 verifier，Step-Level 与 ErrorID 的 Balanced Accuracy 为 78.10 和 63.97；在 ErrorID Balanced F1 上，Qwen2.5-Math-PRM-72B 为 37.28，Llama-3.3-70B-Instruct 为 2.50。

## Typical Duration

对固定回答的单次验证，而非交互式 rollout，所有被评测的 verifier 输出上限为 32K token。论文未给出验证器的单实例 wall-clock 预算；在人工一侧，每份回答平均耗时 90 分钟评分与 63 分钟复核，最长的一份用时达 4 小时。

## Main Contribution

一个由最新开放式 Olympiad 题目上自然产生的 frontier 模型解答构建的人工标注 step-level 验证 benchmark，并在步骤级、回答级与首个错误定位三项任务上评测了 29 个 generative critic 与 process reward model。

## Key Design Ideas

- 题目取自 2024 年及以后的 Olympiad，优先选取开放式证明题，使 verifier 无法退回到已知的 ground-truth 最终答案。
- 回答从 frontier 生成模型采样后不作编辑，因此 verifier 面对的错误自然产生，而非注入到正确解答中或取自人工撰写的证明。
- 严格评分，不给予"Error Carried Forward"的宽免——任何包含错误或由先前错误推导而来的步骤都判为错误，援引论证不充分的先前结论的主张也不得分。
- 由 52 位数学专家进行四轮标注，其中 35 位至少拥有数学或相关领域的研究生学位，包括一轮标注与三轮复核。

## Strengths

- 对自然产生的 frontier 模型错误进行评分，使错误分布贴近 verifier 在实际应用场景中遇到的情形，而非贴近注入错误的分布。
- 将 true positive rate 与 true negative rate 分开报告，暴露出那些 true negative rate 塌陷至接近零而 true positive rate 逼近一的 verifier，这是原始一致率会掩盖的模式。
- 由同一层标注导出三项任务，使步骤级、回答级与首个错误定位能力可以在完全相同的数据上比较。

## Limitations

- Repository note: 80 道题与 200 份解答——论文自陈该 benchmark 规模不大，并提示这可能给测得的性能带来一定方差。
- Repository note: 被评判的对象是为静态解答文本打分的 verifier，而非在环境中行动的 agent；credit 被分配给证明步骤，而非具有下游后果的动作。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在最终任务成功之下分配 credit，但依据的是交互环境中标注的子目标，而非静态证明文本上的专家步骤标签。
- [TRACE](./trace.md) — 同样逐步而非仅按结果为 trajectory 打分，但评判的是产出该 trajectory 的 agent，而非为其打分的 verifier。
- [FinTrace](./fintrace.md) — 同样评估中间过程质量而不只看最终答案，但采用的是多维度的金融工作流指标，而非数学中的二元逐步正确性。
