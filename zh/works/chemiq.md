# ChemIQ (2025)

> [English](../../works/chemiq.md) | **简体中文**

> **首次公开：** 2025-05-12 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.07735)

## Overview

ChemIQ 用 816 道有机化学简答题测量 LLM 的化学智力——含 NMR 结构解析——全部直接作答、不借助工具：推理模型在最高推理档位下答对 50–57%，非推理模型只有 3–7%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.07735>
- **Code:** <https://github.com/oxpig/ChemIQ>
- **Venue:** Journal of Chemical Information and Modeling, 2026（据官方仓库；arXiv 元数据未载明发表信息）

## Summary

论文题为「Assessing the Chemical Intelligence of Large Language Models」。ChemIQ 的 816 道题全部为构造式简答——不设选择题、不允许外部工具——覆盖从 SMILES/IUPAC 表示操作到基于一维与二维 ¹H/¹³C NMR 的结构解析。推理模型（o3-mini、Gemini Pro 2.5、DeepSeek R1）在最高推理档位下达到 50–57%，非推理模型仅 3–7%；Gemini Pro 2.5 对不超过 10 个重原子的分子约 90% 能生成正确 SMILES，且有一例解出了 25 个重原子的结构。

## Tasks

816 道有机化学简答题，分 8 个类别，直接作答、不借助工具；静态构造式作答格式。

## Domains

化学——有机化学：分子表示（SMILES/IUPAC）、反应问题与基于 NMR 的结构解析。

## Evaluation

- 无 judge 的程序化判分：整数题精确匹配、IUPAC 名经 OPSIN 解析验证、反应与 NMR 答案做规范 SMILES 匹配、原子映射按无序元组匹配。
- **报告。** 推理模型最高档位 50–57% vs 非推理模型 3–7%；Gemini Pro 2.5 对 10 个重原子以内的分子约 90% 生成正确 SMILES。

## Typical Duration

单轮简答；明确非 agent 设定（不允许工具）。

## Main Contribution

对「推理模型在化学上的跃升」的干净测量：构造式作答、无工具、程序化验证，推理与非推理模型的差距约达一个数量级。

## Key Design Ideas

- 构造式作答消除了选择题的猜测下限。
- 每类答案都有规范检查器（OPSIN、规范 SMILES），全程不需要 LLM judge。
- NMR 解析考察多约束的结构推断，而非知识回忆。

## Strengths

- 3–7% 到 50–57% 的对比是科学领域里记录得最鲜明的推理档位效应之一。
- 题目、判分脚本与模型输出全部公开；题集仍在扩充（新增二维 NMR 题）。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、论文全文与官方仓库编写（2026 年 8 月）；JCIM 发表信息由仓库 BibTeX 声明，arXiv 元数据未载明。
- 设计上不允许工具——测量的是模型内在的化学推理，而非工具增强下的实践能力。

## Related Works

- [ChemBench](./chembench.md) — 同样面向专家水准的化学问答，覆盖面更广并配有化学家基线。
- [MolPuzzle](./molpuzzle.md) — 同样是基于谱图的结构解析，做成分阶段的多模态 benchmark。
- [QCBench](./qcbench.md) — 同样是无 judge 的化学评估，考定量计算而非结构。
