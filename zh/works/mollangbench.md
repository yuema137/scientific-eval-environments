# MolLangBench (2025)

> [English](../../works/mollangbench.md) | **简体中文**

> **首次公开：** 2025-05-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.15054)

## Overview

MolLangBench 评测语言提示下的分子结构识别、编辑与生成，输入横跨线性字符串、分子图像与分子图：识别任务由化学信息学工具自动构造，编辑与生成任务由专家标注——最强模型 GPT-5 在生成任务上仍跌到 43.0%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.15054>
- **Code:** <https://github.com/TheLuoFengLab/MolLangBench>
- **Dataset:** <https://huggingface.co/datasets/ChemFM/MolLangBench>
- **Venue:** ICLR 2026

## Summary

MolLangBench 覆盖对分子结构「读—改—写」的完整回路：识别结构特征、按指令编辑分子、按规格生成分子，输入形式包括 SMILES 类字符串、图像与图。识别任务由化学信息学构造（抗泄漏且可自动检验）；编辑与生成由专家标注。GPT-5 在识别与编辑上分别达到 86.2% 与 85.5%，在生成上只有 43.0%。

## Tasks

三族任务——结构识别、编辑、生成——覆盖线性字符串、分子图像与分子图；静态单轮任务。实例数量为 TODO(reference)——摘要未载明。

## Domains

化学——化学信息学：经由自然语言接口的分子结构识别与操作。

## Evaluation

- 按任务计准确率；识别类答案由化学信息学工具构造，天然可验证。
- **报告。** GPT-5：识别 86.2%、编辑 85.5%、生成 43.0%。

## Typical Duration

单轮任务；无交互式设定。

## Main Contribution

在同一个 benchmark 上排出识别→编辑→生成的梯度，表明前沿模型「读结构、局部改结构」远好于「从头构造结构」。

## Key Design Ideas

- 自动构造的识别任务提供了抗泄漏、无 judge 的底层。
- 同一批分子以字符串、图像、图三种形式出现，分离出表示形式的影响。
- 专家标注只用在真正需要它的任务（编辑与生成）上。

## Strengths

- 识别与生成之间的差距（86% vs 43%）干净地定位了前沿短板。
- ICLR 2026 录用在 arXiv 页面本身可核实；代码与数据全公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；任务数量在这些来源中未载明，仍为 TODO(reference)。

## Related Works

- [MolecularIQ](./moleculariq.md) — 同样是符号可验证的结构推理，全部任务限定在图上可检验。
- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — 同样是语言驱动的分子编辑与生成，采用一对多评估。
- [MolPuzzle](./molpuzzle.md) — 同样是多模态结构任务，面向基于谱图的解析。
