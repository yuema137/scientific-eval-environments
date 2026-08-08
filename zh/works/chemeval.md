# ChemEval (2024)

> [English](../../works/chemeval.md) | **简体中文**

## Overview

ChemEval 是面向 LLM 的多层级化学评估，围绕化学科研人员的实际需求构建：化学能力分为 4 个递进层级，在 42 个不同任务上考察 LLM 的 12 个能力维度，任务来自开源数据与化学专家的手工设计。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.13989>
- **Code:** <https://github.com/USTC-StarTeam/ChemEval>
- **Dataset:** <https://huggingface.co/datasets/Ooo1/ChemEval>
- **Project:** <https://ustc-starteam.github.io/ChemEval/>
- **Venue:** ICLR 2026（据官方仓库；arXiv 元数据未载明发表信息）

## Summary

ChemEval 把化学能力组织为 4 个递进层级，在 42 个任务上评估 LLM 的 12 个维度，数据由开源来源与专家手工设计的任务组成，以保证任务具有实际价值。对 12 个主流 LLM 做零样本与少样本评估后，论文发现能力呈分裂态势：GPT-4、Claude-3.5 等通用模型长于文献理解与指令遵循，却在需要深入化学知识的任务上不足；化学专用模型则正好相反。

## Tasks

42 个化学任务，覆盖 4 个递进层级与 12 个能力维度（arXiv 版本）；零样本与少样本提示下的静态问答/任务评估。官方仓库描述的 ICLR 2026 版本扩展为 13 个维度下的 62 个文本与多模态任务。

## Domains

化学——能力层级围绕化学科研人员的需求设计，从文献理解到深入的化学知识。

## Evaluation

- 零样本与少样本评估，配有精选示例与精心设计的提示词。
- **报告。** 通用 LLM（GPT-4、Claude-3.5）长于文献理解与指令遵循，但在需要深入化学知识的任务上落后；专用 LLM 化学能力更强，文献理解则较弱。

## Typical Duration

单轮任务；无交互式或 agent 设定。

## Main Contribution

一套以科研人员需求为出发点的化学能力分类法——用递进层级与显式维度取代扁平题库——从而让「通用 vs 专用」模型的取舍显形。

## Key Design Ideas

- 层级是递进的：分类法本身编码了「某些化学能力以另一些为前提」。
- 专家设计的任务把评估锚定在从业者的真实需要上，而非易于抓取的数据上。
- 维度彼此分开，使通用/专用的取舍呈现为能力画像，而非单一分数。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。arXiv 版本与 ICLR 版本存在差异（42 任务/12 维度 vs 62 任务/13 维度，且标题有改动）；上文数字均注明了来源版本。

## Strengths

- 层级/维度结构产出的能力画像可直接用于模型选型。
- 用统一协议在 12 个模型上系统记录了通用与专用模型的分野。

## Related Works

- [ChemBench](./chembench.md) — 同样是广覆盖的化学能力测量，以人类基线而非层级结构见长。
- [ChemCoTBench](./chemcotbench.md) — 同样超越扁平化学问答，走分步化学操作的路线。
- [PhySciBench](./physcibench.md) — 同样是专家策划、按任务类别组织的化学评估，偏深度研究一侧。
