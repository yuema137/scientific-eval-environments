# ChemCoTBench (2025)

> [English](../../works/chemcotbench.md) | **简体中文**

## Overview

ChemCoTBench 把化学评估从问答推进到「模块化化学操作」：添加、删除、取代等操作把分子变换拆成透明的分步工作流——1,495 个样本覆盖 22 个任务，集中在分子性质优化与化学反应预测两大类。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.21318>
- **Code:** <https://github.com/IDEA-XL/ChemCoTBench/>
- **Dataset:** <https://huggingface.co/datasets/OpenMol/ChemCoTBench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

论文题为「Beyond Chemical QA: Evaluating LLM's Chemical Reasoning with Modular Chemical Operations」。ChemCoTBench 把化学问题分解为作用在分子上的显式操作序列，使推理链本身成为可评估对象，而不只看最终答案。Benchmark 含 1,495 个样本、22 个化学任务，围绕分子性质优化与反应预测，并附带推理分类法与基线评估；配套的 ChemCoTDataset 提供 22,000 条链式思维训练数据。

## Tasks

1,495 个 benchmark 样本、22 个化学任务（据论文全文），分为分子性质优化与化学反应预测两族，以分步模块化操作工作流的形式作答；静态推理，非交互式。

## Domains

化学——分子优化与反应预测，论文声明的应用方向是药物设计与反应工程。

## Evaluation

- 在标注的操作工作流上做结构化评估，配有推理分类法与基线评估；步骤级结构使中间推理可以被检验。
- **报告。** 摘要未给出头条数字；据全文约 20 个模型参评，覆盖推理型、通用型与生物分子专用型三类。

## Typical Duration

单回合的分步推理；无环境交互。

## Main Contribution

把化学问题求解重铸为模块化操作序列，让原本不透明的端到端预测变成中间步骤可评估的工作流。

## Key Design Ideas

- 以操作（加/删/换）为推理单元，正对应化学家实际编辑分子的方式。
- 推理分类法把操作层面的失败与计划层面的失败区分开。
- 配套的 ChemCoTDataset（22K 条）使这一格式不仅可测，也可训练。

## Strengths

- 步骤级可评估性正中「只看答案的化学问答」的要害。
- NeurIPS Datasets and Benchmarks 录用经核实，代码与数据公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、论文全文与官方仓库编写（2026 年 8 月）；任务数与样本数出自论文全文而非摘要。

## Related Works

- [ChemEval](./chemeval.md) — 同样把化学评估结构化到扁平问答之上，走能力层级而非操作路线。
- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — 同样评估分子编辑与优化，从开放域自然语言指令出发。
- [FukuyamaBench](./fukuyamabench.md) — 同样是步骤结构化的反应推理，深入到基元机理层面。
