# MaCBench (2024)

> [English](../../works/macbench.md) | **简体中文**

## Overview

MaCBench 探测多模态（视觉-语言）模型在化学与材料研究中的局限，覆盖三个核心方面——数据抽取、实验理解、结果解读：模型在仪器识别与标准化数据抽取上近乎完美，但在空间推理、跨模态信息综合与多步逻辑推断上存在根本性局限。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.16955>
- **Code:** <https://github.com/lamalab-org/MaCBench>
- **Dataset:** <https://huggingface.co/datasets/jablonkagroup/MaCBench>
- **Venue:** arXiv preprint (cs.LG, cond-mat.mtrl-sci), 2024

## Summary

MaCBench 评估视觉-语言模型能否承担化学与材料研究中的视觉工作：认读仪器与实验场景、从图表中抽取数据、解读实验结果。模型近乎完美地识别设备、抽取标准化数据，却在空间推理、跨模态信息综合与多步逻辑推断上暴露根本性局限——感知过关，整合失灵。该 benchmark 运行在 ChemBench 评估管线上，并维护公开排行榜。

## Tasks

多模态（图像 + 文本）的化学与材料任务，分三个方面：数据抽取、实验理解、结果解读；静态 VLM 评估。任务数量为 TODO(reference)——摘要与仓库均未载明。

## Domains

化学与材料科学——论文标题与研究范围对两者均有明确命名，材料一侧也体现在其 cond-mat.mtrl-sci 分类上。

## Evaluation

- 经 ChemBench 管线在多模态任务上计准确率，按三个方面分别拆分。
- **报告。** 设备识别与标准化数据抽取近乎完美；空间推理、跨模态信息综合与多步逻辑推断存在根本性局限。

## Typical Duration

单轮多模态问题；无交互式设定。

## Main Contribution

定位科学工作的视觉-语言瓶颈：当前模型能看懂实验室图像，却还不能跨模态、跨步骤地推理——而后者才是「做科学」区别于「读科学」的部分。

## Key Design Ideas

- 抽取/理解/解读的三分法按整合深度为任务排序。
- 复用 ChemBench 管线，与纯文本的姊妹 benchmark 保持判分一致。
- 消融数据集分离出驱动失败的视觉属性。

## Strengths

- 少数直接面向 VLM（而非文本模型）的化学/材料评估之一。
- 感知与整合的对比给出了一条精确的能力边界。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；任务数量在这些来源中未载明，仍为 TODO(reference)。arXiv 元数据与官方仓库均未载明发表信息。

## Related Works

- [ChemBench](./chembench.md) — 纯文本的姊妹 benchmark，MaCBench 运行在它的评估管线上。
- [ChemX](./chemx.md) — 同样是化学/材料数据抽取，在 agent 式文档处理层面。
- [MolPuzzle](./molpuzzle.md) — 同样是多模态化学评估，对象是谱图而非实验室影像。
