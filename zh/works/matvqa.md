# MatVQA (2025)

> [English](../../works/matvqa.md) | **简体中文**

## Overview

MatVQA 在材料科学的视觉-科学推理上考验多模态 LLM：1,325 个问题横跨四类结构-性质-性能推理任务，覆盖真实材料影像（显微、衍射图样），并迭代剔除文本捷径，使作答必须真正看图。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.18319>
- **Code:** <https://anonymous.4open.science/r/matvqa-1E01>
- **Venue:** arXiv preprint (cs.CE), 2025

## Summary

论文题为「Seeing Beyond Words」。MatVQA 瞄准材料专业能力中偏视觉的那部分：读懂显微与衍射影像，并跨结构、性质、性能做多步科学推理。其 1,325 个问题横跨四类结构-性质-性能推理任务，由自动化流水线（MArxivAgent）从材料文献生成，并迭代剔除文本捷径，使模型无法仅凭图注作答。对 17 个开源与闭源 MLLM 的评测暴露出当前多模态推理的显著缺口。

## Tasks

覆盖真实材料影像（显微、衍射）的 1,325 个视觉-科学问题，横跨四类结构-性质-性能推理任务；静态多模态问答。经 MArxivAgent 流水线生成并剔除捷径。

## Domains

材料科学——对显微与衍射影像的视觉表征推理，与结构-性质-性能关系相连。

## Evaluation

- 17 个 MLLM 上四类 SPP 推理任务的准确率；捷径剔除强制真正的视觉推理。
- **报告。** 当前多模态推理能力存在显著缺口；摘要无单一数值头条。

## Typical Duration

单轮多模态问题；无交互式设定。

## Main Contribution

一个抗捷径的材料影像视觉推理 benchmark——测量 MLLM 能否从「看到的」而非「图注告诉它的」进行推理。

## Key Design Ideas

- 迭代剔除文本捷径，迫使模型依赖图像。
- 结构-性质-性能的任务划分对应材料推理链。
- 自动化的文献派生生成（MArxivAgent）规模化地造题。

## Strengths

- 使用真实的显微与衍射影像，而非合成图。
- 抗捷径构造针对多模态科学 benchmark 的普遍弱点。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；参评模型名单与各模型数字在正文中。代码在匿名仓库；arXiv 元数据无发表信息。

## Related Works

- [MatCha](./matcha.md) — 同样是多模态材料表征评估，横跨四个研究阶段、21 个任务。
- [MatQnA](./matqna.md) — 同样是表征问答，按十种表征方法组织。
- [MaCBench](./macbench.md) — 同样是多模态的化学/材料评估，经 ChemBench 管线。
