# LABBench2 (2026)

> [English](../../works/labbench2.md) | **简体中文**

> **首次公开：** 2026-02-04 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2604.09554)

## Overview

LABBench2 是面向生物学研究 AI 系统的改进版 benchmark：近 1,900 个任务在更真实的情境中重演 LAB-Bench 的能力类别——从 PDF、图片与生物信息学文件中作答——相对 LAB-Bench 造成各子任务上 26–46% 的模型准确率下滑。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)
- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.09554>
- **Code:** <https://github.com/EdisonScientific/labbench2>
- **Dataset:** <https://huggingface.co/datasets/futurehouse/labbench2>
- **Venue:** arXiv preprint (cs.AI, cs.CL, cs.LG), 2026

## Summary

LAB-Bench 所测的能力自 2024 年以来已大幅提升，LABBench2 因此以更高的真实度重建套件：子任务（据官方仓库）包括 cloning、dbqa2、图像与 PDF 变体的 figqa2 / tableqa2、litqa3、patentqa、protocolqa2、seqqa2、sourcequality、suppqa2 与 trialqa，任务植根于研究者实际经手的材料。真实度的提升带来实打实的难度跃升——各子任务上模型准确率差异为 −26% 至 −46%——为下一代模型重新留出提升空间。

## Tasks

近 1,900 个任务，子任务族覆盖文献、数据库、图表（图像与 PDF 变体）、协议、序列、克隆、专利、来源质量与临床试验记录；静态，配公开的评估 harness。

## Domains

生物学研究实践：分子生物学与克隆、基因组序列、协议、文献与专利、临床试验记录。

## Evaluation

- 经发布的评估 harness 按子任务族计算准确率。
- **报告。** 相对 LAB-Bench，各子任务上模型准确率差异为 −26% 至 −46%。

## Typical Duration

在真实材料（PDF、图片、数据文件）上的单任务作答；非交互式环境。

## Main Contribution

量化了所测「生物学能力」中有多少其实是题目格式带来的便利：能力类别不变、只恢复真实情境，模型就要付出最多 46 个百分点。

## Key Design Ideas

- 真实材料（PDF、图片、原始文件）取代事先消化好的题干。
- 与 LAB-Bench 的子任务连续性使难度跃升可直接归因于真实度。
- 新任务族（专利、来源质量、试验）把覆盖面扩展到研究判断力。

## Strengths

- 在一个成熟参考套件上做受控的真实度升级。
- −26% 至 −46% 的下滑直接量化了 benchmark 形式带来的通胀。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [LAB-Bench](./lab-bench.md) — 其能力类别被 LABBench2 加固的前代套件。
- [GAIA](./gaia.md) — 同样以真实多来源情境对抗 benchmark 饱和，面向通用助手。
- [BixBench](./bixbench.md) — 同样把真实性放在首位的生物学评估，走开放式分析而非加固问答。
