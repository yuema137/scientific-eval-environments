# MolPuzzle (2024)

> [English](../../works/molpuzzle.md) | **简体中文**

> **首次公开：** 2024-07-03 · **来源：** [官方代码库首次提交](https://github.com/KehanGuo2/MolPuzzle/commit/11e5f4c4c12f3a150291f58f52a8c595ededb6da)

## Overview

MolPuzzle 把分子结构解析做成三阶段的多模态「拼图」——分子理解、谱图解读、分子构建——共 200 个解析实例、23,678 条数据样例；GPT-4o 的最终结构与真值精确匹配率仅 1.4%，远低于人类。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper (OpenReview):** <https://openreview.net/forum?id=t1mAXb4Cop>
- **Project:** <https://kehanguo2.github.io/Molpuzzle.io/>
- **Code:** <https://github.com/KehanGuo2/MolPuzzle>
- **Dataset:** <https://huggingface.co/datasets/kguo2/MolPuzzle_data>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks Track, 2024（据官方项目页；论文无 arXiv 版本）

## Summary

论文题为「Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation」。MolPuzzle 按化学家的实际工作流拆解结构解析：第一阶段从分子式推出不饱和度、芳环与官能团；第二阶段解读 IR、质谱、¹H-NMR 与 ¹³C-NMR 谱图；第三阶段把收集到的约束组装成分子。在众多 LLM 与视觉-语言模型中 GPT-4o 表现最好，但最终结构与真值精确匹配的比例只有 1.4%，仍明显低于人类基线。

## Tasks

200 个分子结构解析实例，拆为三个阶段，各阶段共收集 23,678 条数据样例；多模态（谱图以图像给出）但为静态问答式——非交互。

## Domains

化学——分析化学与有机化学：基于 IR、MS、¹H-NMR、¹³C-NMR 谱学的结构解析。

## Evaluation

- 最终结构的精确匹配准确率，加上各阶段单独评估；全部阶段配有人类基线。
- **报告。** GPT-4o 优于其他模型，但真值结构的精确匹配率仅 1.4%，低于人类。

## Typical Duration

分阶段的单回合拼图；每个阶段是一个有界的问答步骤，输出喂给下一阶段。

## Main Contribution

把经典的「谱图推结构」考题变成分阶段的多模态 benchmark，使失败可以定位到理解、解读还是构建环节。

## Key Design Ideas

- 三阶段拆解对应人类工作流，各阶段分数因此具有诊断意义。
- 多模态谱图逼迫模型做真正的跨模态化学，而非文本模式匹配。
- 最终阶段用结构精确匹配，不留部分得分的含糊空间。

## Strengths

- 1.4% 与人类水平之间的落差，是前沿模型在化学领域已记录到的最悬殊短板之一。
- 项目页、代码与数据集全套公开。

## Limitations

- Repository note: 卡片依据官方项目页编写（2026 年 8 月）；论文无 arXiv 版本，校验期间 OpenReview 元数据不可达，各阶段细节与是否为 spotlight 均有待核实。

## Related Works

- [MolQuest](./molquest.md) — 同样是谱图到结构的解析，被重铸为交互式多轮 agent 任务。
- [ChemIQ](./chemiq.md) — 同样含 NMR 结构解析，采用不借助工具的简答形式。
- [MolLangBench](./mollangbench.md) — 同样考结构识别与构建，通过语言提示驱动。
