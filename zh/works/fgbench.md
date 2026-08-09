# FGBench (2025)

> [English](../../works/fgbench.md) | **简体中文**

## Overview

FGBench 在官能团粒度上评估分子性质推理：62.5 万个生成的推理问题，标注了是 245 个官能团中的哪一个驱动了性质差异；另设 7,000 个精选子集用于评测最先进的 LLM。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.01055>
- **Code:** <https://github.com/xuanliugit/FGBench>
- **Dataset:** <https://huggingface.co/datasets/xuan-liu/FGBench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

FGBench 问的不只是模型能否预测分子性质，而是它能否说清「为什么」——并把原因定位到官能团。数据集含 62.5 万个性质推理问题，覆盖 245 个官能团，分三种设定：单官能团影响、多官能团相互作用、分子间直接对比，同时包含回归与分类任务。在 7,000 个精选问题上的评测显示，当前 LLM 在官能团层面的性质推理上明显吃力。

## Tasks

62.5 万个分子性质推理问题（245 个官能团；单影响、相互作用、分子对比三种设定）；7,000 个精选子集作为 LLM benchmark。静态问答，含回归与分类目标。

## Domains

化学——官能团层面的构效关系，动机是分子设计与药物发现。

## Evaluation

- 对照数据集标签做回归与分类评分，官能团标注支持推理层面的分析。
- **报告。** 当前 LLM 在官能团层面的性质推理上明显吃力；摘要未给出单一头条数字。

## Typical Duration

单轮问题；无交互式设定。

## Main Contribution

把性质预测评估从「整分子答案」转向「官能团定位的推理」，并以数据生成框架把这一格式扩展到 62.5 万个问题。

## Key Design Ideas

- 官能团正是化学家实际使用的解释单元——benchmark 直接考这套语言。
- 相互作用问题把「可加性推理」与「真正的多官能团理解」区分开。
- 生成框架加精选评测子集，把训练规模的数据与 benchmark 质量解耦。

## Strengths

- 细粒度归因：失败可定位到具体官能团与相互作用类型。
- NeurIPS Datasets and Benchmarks 录用经核实，代码与数据公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；回归/分类框架之外的指标细节有待全文校验。

## Related Works

- [MolecularIQ](./moleculariq.md) — 同样以结构为根基的化学推理，在分子图上做符号验证。
- [ChemCoTBench](./chemcotbench.md) — 同样把化学推理拆成可检验的单元，粒度在操作层面。
- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — 同样是性质敏感的分子任务，方向是生成。
