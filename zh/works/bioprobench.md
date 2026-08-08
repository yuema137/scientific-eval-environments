# BioProBench (2025)

> [English](../../works/bioprobench.md) | **简体中文**

## Overview

BioProBench 是生物实验协议推理的语料与 benchmark：22,413 份人工撰写的协议（BioProCorpus）扩展为 523,784 个任务实例，覆盖五类任务——协议问答、步骤排序、错误纠正、协议生成与协议推理。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.07889>
- **Code:** <https://github.com/YuyangSunshine/bioprobench>
- **Dataset:** <https://huggingface.co/BioProBench>
- **Venue:** arXiv preprint (cs.CL)；据官方仓库为 ICML 2026

## Summary

湿实验协议是生物学推理与物理后果交汇的地方。BioProBench 把大规模人工撰写的协议语料转化为五类任务族来探查程序性理解，指标（据官方仓库）包括准确率、F1、步骤召回/精确率、Kendall's tau 与 BLEU。在 10 个主流 LLM 上，凡是需要深度推理、定量精确与安全意识的任务，表现都显著下滑。论文将 benchmark 与基线 agent ProAgent 配对。

## Tasks

由 22,413 份人工撰写协议派生的 523,784 个任务实例，覆盖五类任务：协议问答、步骤排序、错误纠正、协议生成与协议推理；静态评估。

## Domains

生物湿实验协议，覆盖 16 个生物学子领域（据官方仓库；子领域在已验证来源中未逐一列出）。

## Evaluation

- 据官方仓库按任务采用：准确率、F1、精确率/召回率、步骤召回/步骤精确率、Kendall's tau、精确匹配、BLEU、Brier 分数。
- **报告。** 10 个主流 LLM 在需要深度推理、定量精确与安全意识的任务上表现显著下滑。

## Typical Duration

单实例协议任务；非交互式 agent 设定。

## Main Contribution

语料规模的程序性生物学：52 万个实例检验模型是否理解实验步骤做什么、按什么顺序做、会怎样失败——这是任何实验室自动化 agent 都必须掌握的底层能力。

## Key Design Ideas

- 五类任务把程序性能力从识别（问答）、修复（纠错）一路分解到合成（生成）。
- 人工撰写的协议保证分布真实而非模板化。
- 顺序敏感的指标（Kendall's tau、步骤召回）把流程当作序列而非步骤集合来评分。

## Strengths

- 程序性生物学中无出其右的语料规模（2.2 万份协议、52 万实例）。
- 「推理/精确/安全」的弱点画像与实验室 agent 的风险直接相关。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。仓库以一个变体标题引用其 ICML 2026 录用。
- Repository note: 论文的基线 agent ProAgent 属于 agent 实现，超出本仓库范围；本卡片记录其语料与 benchmark。

## Related Works

- [SciGym](./scigym.md) — 同样面向实验生物学，但走交互式干实验的实验设计而非协议文本。
- [LAB-Bench](./lab-bench.md) — 其更广的生物学研究套件中同样包含协议推理（ProtocolQA）。
- [MDArena](./mdarena.md) — 同样评估由研究方案驱动的科学工作，以可执行模拟工作流呈现。
