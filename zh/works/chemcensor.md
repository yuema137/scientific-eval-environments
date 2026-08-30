# ChemCensor / CREED (2026)

> [English](../../works/chemcensor.md) | **简体中文**

> **首次公开：** 2026-02-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.03554)

## Overview

ChemCensor 是单步逆合成的评估方法学：用化学合理性指标取代「对照单一真值的 Top-K 精确匹配」；同一套验证器还生成了 CREED——数百万条经验证的反应记录，用于 LLM 训练。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.03554>
- **Venue:** arXiv preprint (cs.LG), 2026

## Summary

论文题为「When Single Answer Is Not Enough: Rethinking Single-Step Retrosynthesis Benchmarks for LLMs」，其观察是：逆合成允许多组合法的前体，因此对照单一记录答案的 Top-K 准确率量错了对象。论文贡献一套 benchmark 框架，用新的化学合理性指标 ChemCensor 评估通用与化学专用 LLM，并发布 CREED——数百万条经 ChemCensor 验证的反应记录；用 CREED 训练的模型在该 benchmark 下超过 LLM 基线。

## Tasks

单步逆合成：给定目标分子，提出合理的前体组合；静态预测，按合理性而非精确匹配评估。评估集规模为 TODO(reference)——摘要未载明。

## Domains

化学——合成规划与药物发现：单步逆合成的评估。

## Evaluation

- ChemCensor 化学合理性评分，强调合理性而非与单一记录真值的精确匹配。
- **报告。** 摘要未给出头条数字；CREED 训练的模型在该 benchmark 下超过 LLM 基线。

## Typical Duration

单轮预测；无交互式设定。

## Main Contribution

诊断并修复一处评测指标的失真：当任务是多对一时，精确匹配 Top-K 会惩罚化学上合法的答案；换成合理性指标后，排名与训练的优化目标都随之改变。

## Key Design Ideas

- 评估指标兼任数据验证器——给模型打分的合理性检查，同样用于大规模过滤训练记录。
- 合理性评分接纳全部合法前体空间，而不只是恰好被记录下来的那一组。
- 指标与数据集配对形成闭环：更好的评估直接产出更好的训练信号。

## Strengths

- 在评估设计层面解决了逆合成排行榜上的一个公认失真。
- 百万量级的验证数据集证明该指标可以作为自动过滤器运转。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要之外的细节有待全文校验。论文 arXiv 页面上无法核实任何代码或数据集发布，arXiv 元数据亦未载明发表信息。

## Related Works

- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — 同样用一对多评估取代单参考匹配，在分子生成方向。
- [FukuyamaBench](./fukuyamabench.md) — 同样是反应类推理的评估，深入到机理层面。
- [FormalRewardBench](./formalrewardbench.md) — 同样研究评估信号能否「收合法、拒非法」。
