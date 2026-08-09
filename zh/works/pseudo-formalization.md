# Pseudo-Formalization (2026)

> [English](../../works/pseudo-formalization.md) | **简体中文**

## Overview

Pseudo-Formalization（PF）是一种评估方法论，它把自然语言数学证明改写为若干自包含模块——每个模块陈述自身的前提、结论与证明——再对每个模块独立检查。它在奥林匹克竞赛级与研究级数学上接受评估，并发布 ArxivMathGradingBench，包含 35 篇 arXiv 研究论文以及作者事后披露的 40 处错误。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2605.20531>
- **Code:** <https://github.com/Slim205/pseudo-formalization>

## Summary

Pseudo-Formalization 认为，可靠的证明验证是训练与评估 AI 系统进行高难度数学推理的瓶颈：Lean 之类语言中的完全形式化证明无歧义且模块化，因而易于检查，但多数证明——尤其是 AI 系统写出的证明——两种性质都不具备，而表达现代研究数学所需的形式化库仍远未完备。作者定义了一种证明格式，其每个模块都以自然语言陈述前提、结论与证明，并把它与 Block Verification（BV）配对：由一个 LLM 把证明翻译为该格式，逐模块独立验证，再由一个 calibrator 模型在可配置的严格度阈值下聚合各模块的报告。PF+BV 在奥林匹克与研究级数学上于错误发现的 precision 与 recall 上 Pareto 支配 LLM-as-judge baseline，论文并发布 ArxivMathGradingBench 作为其研究级测试集。

## Tasks

两个 benchmark。Hard2Verify 提供由 frontier AI 模型在 80 道奥林匹克与 Putnam 级题目上生成的 200 份证明，并配有 step 级二元正确性标注。本文引入的 ArxivMathGradingBench 收录 35 篇数学研究论文、合计 40 处已知错误，其构建方式是向 arXiv API 查询 2025-01-01 至 2025-07-30 之间的全部数学投稿，用正则筛选同时含更正类词与 lemma、theorem 或 proposition 提及的修订评论，再用 GPT-5.4 nano 对留存条目分类，最后剔除非宽松许可论文与误报，把 100 个候选缩减到 35 个。

## Domains

数学证明验证：奥林匹克与 Putnam 竞赛题目，以及取自 arXiv 数学类目的已发表研究数学。

## Evaluation

- **Step-level precision and recall.** 在 Hard2Verify 上，预测为错误的 step 下标在整个数据集上汇总为 TP、FP 与 FN 计数，并据此计算错误 step 上的 precision 与 recall。
- **Proof-level precision and recall.** 同一组计数，在把"任一 step 被标记即判该证明为错误"的映射应用之后重新计算。
- **Coverage and false errors per proof.** Coverage 是每个 ground-truth 错误都被标记出来的有缺陷证明所占比例；false errors per proof 是不匹配任何标注错误的预测的平均数量。
- **Error-location matching.** 在 ArxivMathGradingBench 上，验证器接收论文 PDF 并返回一份错误位置列表，再由 GPT-5.4 mini 判断每个返回位置是否匹配某个 ground-truth 位置，因为论文没有天然的 step 概念。
- **报告结果。** 主要结果使用 GPT-5.4 mini，并另行扫过 GPT-5.4 nano 与 full。在 Hard2Verify 上，PF+BV 与 LLM-as-judge baseline 都找回约 90% 的错误 step，且 PF+BV 在 k = 8 时每份证明少标记 60% 的虚假 step。在 ArxivMathGradingBench 上，二者在 k = 8 时都有约 50% 的标注错误未被捕获，其中 PF+BV 达到更高的 recall、发出更少的虚假告警，并在更大比例的论文上覆盖了全部标注错误。未报告人类 baseline。

## Typical Duration

验证开销以计算预算而非时长报告：每个条目 k = 8 次独立运行，在 Hard2Verify 上每次 rollout 为 64K 输入 / 26K 输出 token，在 ArxivMathGradingBench 上每次 rollout 为 213K 输入 / 96K 输出 token，API 总成本分别为 $264.24 与 $165.68。未说明：论文未给出每任务的 wall-clock 或步数预算。

## Main Contribution

一种把自然语言论证分解为陈述前提、结论与证明的自包含模块的证明格式，配以独立检查每个模块的 Block Verification 算法，以及一个由作者已更正的 arXiv 论文构建的研究级验证 benchmark。

## Key Design Ideas

- 每个模块都以自然语言陈述自身前提、结论与证明的证明模块，由一张调用有向无环图（DAG）与一片作用域继承森林组织起来。
- 按逆拓扑序进行的 block 验证，使每个模块在假定其子模块正确的前提下接受检查。
- 一个独立的 calibrator 模型，在自然语言描述的严格度阈值下把逐模块错误报告聚合为最终判定。
- 对 k 次并行运行做悲观聚合，并扫过 k 以刻画 precision–recall 的工作点曲线。

## Strengths

- 模块局部的检查让每次验证调用都处于短上下文区间，而不必一次性容纳整份证明。
- 从作者自己的 arXiv 修订评论中挖掘出的错误标注，无需新的专家标注即可提供研究级 ground truth。
- 每个阶段都调用现成模型且不做微调，因此所报告的增益可归因于证明格式本身，而非某个训练过的验证器。

## Limitations

- Repository note: Ground truth 只覆盖作者在修订评论中披露的错误位置，因此真实但未被标注的错误会被计为 false positive——论文据此把其 precision 值报告为下界、把 false positive 计数报告为上界。
- Repository note: Precision 与 recall 以随 k 变化的曲线形式发布，而非列表化的点值，且 ArxivMathGradingBench 只有 35 篇论文，因此与其他 trajectory 级评估之间的数值比较建立在一个从图上读出的小样本之上。

## Related Works

- [TRACE](./trace.md) — 同样对推理 trajectory 的中间步骤而非仅最终答案打分，但走的是面向 deep-research agent 的认知质量维度，而不是逐条比对证明模块与其所述前提。
- [T-Eval](./t-eval.md) — 同样把评估分解到端到端任务成功率之下，但沿 tool-use 能力子过程展开，而非沿前提–结论证明模块展开。
- [AgentBoard](./agentboard.md) — 同样以人工编写的标注给中间进展打分，但用的是面向交互式任务的手工标注 subgoal，而非从作者 arXiv 修订评论中挖掘的错误位置。
