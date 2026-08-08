# CMT-Benchmark (2025)

> [English](../../works/cmt-benchmark.md) | **简体中文**

## Overview

CMT-Benchmark 是由专家研究者构建的凝聚态理论 benchmark，含 50 道达到专家自身研究水平的问题，对照专家提供的真值做机器判分，包括通过正规排序对非对易算符做符号化处理。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.05228>
- **Dataset:** <https://huggingface.co/datasets/JVRoggeveen/cmt_benchmark>
- **Venue:** ICLR 2026

## Summary

CMT-Benchmark 横跨凝聚态理论的解析与计算方法——Hartree-Fock、精确对角化、量子/变分蒙特卡洛、DMRG 与统计力学——覆盖量子多体系统与经典统计力学。解答对照专家真值程序化检验，判分方法可跨任务泛化，包括对非对易算符做正规排序后的符号比较。

## Tasks

50 道凝聚态理论问题，横跨 Hartree-Fock、精确对角化、量子/变分蒙特卡洛、DMRG 与统计力学。

## Domains

凝聚态理论：量子多体系统、经典统计力学、计算物理方法。

## Evaluation

- 对照专家提供的真值做程序化检验，机器判分可跨任务泛化——包括经正规排序的非对易算符符号化处理。
- **报告。** 最佳模型 GPT-5 解出 30% 的问题；17 个模型的平均为 11.4±2.1%；18 道题无任何模型解出，26 道至多被一个模型解出。

## Typical Duration

单题的理论与计算推导；非交互式 agent 设定。

## Main Contribution

把专家研究者水平的凝聚态理论变为可机器判分，并证明大多数问题没有任何受评前沿模型能够解出。

## Key Design Ideas

- 问题由专家研究者按其自身工作的水平编写，而非改编自课程作业。
- 基于正规排序的符号判分解决了通用检查器无法处理的非对易算符比较问题。
- 未解出问题数（18 道无人解出、26 道至多一人）被作为一等结果报告。

## Strengths

- 在通常需要专家人工判分的难度上实现机器判分。
- 极大的提升空间，按题目而非仅按平均值记录。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [CMPhysBench](./cmphysbench.md) — 同样是凝聚态评估，但为研究生水平、520+ 题并带部分得分。
- [PRBench](./prbench.md) — 同样是专家锚定的物理评估，通过复现已发表论文。
- [Hard2Verify](./hard2verify.md) — 同样在前沿难度上使用专家产出的真值，面向数学证明步骤验证。
