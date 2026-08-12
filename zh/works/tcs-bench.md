# TCS-Bench (2026)

> [English](../../works/tcs-bench.md) | **简体中文**

## Overview

TCS-Bench 是一个评估大语言模型在研究级理论计算机科学（TCS）证明生成上的 benchmark，每个任务要求模型为取自顶级 TCS 会议论文的一条目标结论产出自包含的证明。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.09538
- **Venue:** arXiv preprint, 2026

## Summary

TCS-Bench 从顶级理论计算机科学会议——FOCS、STOC 与 SODA——2020 至 2026 年发表的论文中汇集定理证明任务。每个任务提供推导一条目标陈述自包含证明所需的上下文，模型按能否产出正确证明计分。由于评判研究级证明本身就很困难，作者构建了一个自动化验证 agent，并将其对齐人类专家判断，报告与专家标签的一致性超过 90%。

## Tasks

300 个定理证明任务。每个任务给出一条目标陈述以及推导其自包含证明所需的上下文，抽取自 FOCS、STOC 与 SODA 的论文（2020–2026）。构建流水线先解析 LaTeX 抽取陈述，经一次基于 LLM 的分析构建依赖图，通过迭代式的章节裁剪与 LLM 压缩组装上下文，再施加结构性与语义性的质量过滤。

## Domains

研究级理论计算机科学（对 FOCS、STOC 与 SODA 结论的定理证明）。证明生成任务在本质上是数学性的。

## Evaluation

生成的证明由一个自动化验证 agent 检查。参考验证器对 Gemini 3.1 Flash 发起四次调用并施加多数投票：当四个判定中至少三个判为正确时，候选证明记为正确。该验证器针对一个由人类专家标注的 100 条证明集（报告为 50 正确、50 错误）作对齐，在其上达到超过 90% 的准确率。所报模型在该 benchmark 上的准确率：GPT 5.6 Pro 68%、Colosseum（跨模型选择）67.7%、Gemini 3.1 DeepThink 52%、Opus 5 32.77%、Gemini 3.1 Pro 30.3%。

## Typical Duration

TODO(reference) — 所查来源未报告标准化的每任务 token 预算或 wall-clock 时间。

## Main Contribution

一个含 300 个研究级 TCS 定理证明任务的 benchmark，整理自顶级会议论文（FOCS、STOC、SODA；2020–2026），并配一套经过验证的自动化证明验证系统，其在标注校准集上与人类专家判断的一致性超过 90%。

## Key Design Ideas

- **研究级源材料。** 任务派生自 FOCS、STOC 与 SODA 收录论文中的证明，而非教科书或竞赛题目。
- **自包含的任务构建。** 一条流水线——LaTeX 陈述抽取、LLM 构建依赖图、经章节裁剪与压缩的上下文组装、质量过滤——产出携带推导目标证明所需上下文的任务。
- **对齐专家的自动化验证器。** 正确性由一个 agent 判定，它发起四次 Gemini 3.1 Flash 调用并按 4 取 3 多数投票，针对一个 100 条的人类专家标注集作对齐。

## Strengths

- 面向近期发表的顶会 TCS 结论进行研究级证明生成，而非标准化的考试式题目（论文）。
- 将其自动化评分器对齐人类专家判断，在 100 条证明标注集上报告超过 90% 的准确率（论文）。
- 评估了一系列当代前沿模型，最强者达到 68% 准确率，表明仍有可观的提升空间（论文）。

## Limitations

- 作者指出最强模型（68%）与满分之间尚有差距，说明多步数学推理仍有很大提升空间（论文）。
- Repository note: 正确性依赖一个基于 LLM 的验证 agent；尽管在 100 条集上对齐至超过 90% 的专家一致性，研究级证明的自动化评分仍留有残余错误率。

## Related Works

TODO(reference)
