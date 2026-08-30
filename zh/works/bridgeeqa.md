# BridgeEQA (2025)

> [English](../../works/bridgeeqa.md) | **简体中文**

> **首次公开：** 2025-11-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2511.12676)

## Overview

BridgeEQA 是面向桥梁检测的具身问答 benchmark：2,200 组开放词汇问答对，以专业检测报告为依据，覆盖 200 个真实桥梁场景。agent 必须在一座结构的众多视角之间收集视觉证据，按标准化的状态评定量表作答，并引用支持其判断的图像。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2511.12676>
- **Code:** <https://github.com/drags99/bridge-eqa>
- **Venue:** CVPR 2026（项目页 <https://drags99.github.io/bridge-eqa/> 所述）；arXiv 预印本，2025

## Summary

作者提出 *Inspection EQA*（检测式具身问答）作为情节记忆型具身问答的一类问题，认为基础设施检测恰好提供了通用 EQA benchmark 所缺的东西：第一人称视角影像、可作依据的专业报告，以及标准化的评价量表。BridgeEQA 用真实的桥梁检测数据把它实例化，论文还提出 Image Citation Relevance，用于衡量模型引用的图像是否真的支持它给出的答案。对当前最先进视觉语言模型的评测暴露出明显的性能差距；论文进而提出 Embodied Memory Visual Reasoning (EMVR)，把检测式 EQA 表述为场景图上的马尔可夫决策过程，表现优于各基线。

## Tasks

2,200 组开放词汇问答对，覆盖 200 个真实桥梁场景，共含 9,586 张图像，平均每个场景 47.93 张；这些桥梁分布在佛蒙特州的 73 个镇。问题由 Gemini 视觉语言模型从 Vermont Agency of Transportation 的检测报告中自动抽取，依据是检测员记录以及这些记录明确引用的照片。报告的问题分四类：聚合型（38.5%）、比较型（27.2%）、关系型（21.3%）与空间型（17.5%）。问答对经自动检查筛选，指标包括忠实度（0.997）、答案相关性（0.997）、可回答性（0.996）与检测员相关性（0.980），并对随机子集做人工复核，检查视觉覆盖与图像质量。

## Domains

土木与结构工程：在役公路桥梁的检测与状态评估，答案与各州交通机构通用的 National Bridge Inventory 0–9 状态评定量表对齐。影像与推理都取自专业的结构检测实务，而非一般的室内外场景理解。

## Evaluation

- **Answer Correctness** —— 以 LLM-as-a-judge 把回答与依据报告的 ground truth 对比，沿用 OpenEQA 的协议。
- **Condition Rating Accuracy** —— NBI 0–9 量表上的精确匹配准确率与 ±1 以内准确率；之所以设 ±1 带宽，是因为专家检测员之间通常也只能一致到一个评定等级之内。
- **Image Citation Relevance** —— 由 VLM-as-a-judge（Gemini 2.5 Flash）在 0.0–1.0 区间上比较 agent 引用的图像与参考图像并打分，同时惩罚过度选取；该指标与人工标注的 Spearman 相关系数为 0.817。
- **报告。** 五种方法（多帧 VLM、带场景图的 Socratic LLM、带场景图的多帧 VLM、仅用场景图的 EMVR、图像加场景图的 EMVR）在三个闭源视觉语言模型（Gemini 2.5 Flash Lite、Gemini 2.5 Flash、Grok 4 Fast）上运行。answer correctness 分布在 0.484–0.648，Image Citation Relevance 在 0.687–0.889。在 Grok 4 Fast 上，EMVR 相对多帧 VLM 基线在 ±1 以内的状态评定准确率上提升 9.3 个百分点，Image Citation Relevance 提升 20.2 个百分点，answer correctness 提升 7.2 个百分点。

## Typical Duration

N/A — 论文未报告单个 episode 的步数上限、wall-clock 预算或 token 预算。每个 episode 在平均含 47.93 张图像的单桥场景图上运行。

## Main Contribution

提出 Inspection EQA 作为情节记忆型具身问答的一类问题，发布 BridgeEQA 作为其首个 benchmark，提出 Image Citation Relevance 作为证据引用的评价指标，并表明在情节场景图上做马尔可夫决策过程建模（EMVR）能补上直接多帧提示所留下的一部分差距。

## Key Design Ideas

- 把问题锚定在本就存在、且本就自带公认答案标准的文档上——专业检测报告与 NBI 状态量表——而不是自己编写合成问题。
- 证据与答案一并计分：agent 即便给出正确的状态评定，若引用的是无关图像，也会被 Image Citation Relevance 扣分。
- 状态评定采用 ±1 带宽，使评分贴合检测员之间真实的一致程度，而不苛求人类专家自己都做不到的精确。
- 把一座桥的多视角图像集合当作有待导航的情节记忆，形式化为场景图上的 MDP，而不是当成一叠平铺的图像喂给长上下文模型。
- 在用 judge 指标为系统排序之前，先用三名人类标注者对它做校验。

## Strengths

- 场景、图像与答案标准都来自一个真实的州级检测项目，任务分布并非由 benchmark 设计者编造。
- 三条独立的评分轴（答案文本、工程状态判断、证据引用）能让「答对了但理由不对」显形。
- 引用指标经人工标注校准，而不是想当然地认为可靠。
- 对比覆盖五种方法变体与三个模型的交叉组合，把场景图表示的贡献与导航策略的贡献区分开。

## Limitations

- 只评测了闭源模型：作者报告开源 VLM 无法稳定遵循所需的结构化输出与函数调用格式。
- ground truth 问答对由 Gemini 模型从报告中自动生成，人工只复核了随机子集，因此 benchmark 的标注部分继承了某个模型对源文档的理解。
- 三项主要指标中有两项由模型评判（LLM-as-a-judge 与 VLM-as-a-judge），且其中一个 judge 与受评模型出自同一家族。
- 所有场景都来自单一的州级检测项目（Vermont Agency of Transportation），报告惯例与桥梁总体因此谈不上多样。
- Repository note: 该 benchmark 考的是从影像出发的状态评估；它不评测定量结构分析、荷载评级或任何下游的养护决策。

## Related Works

- [StructureClaw](./structureclaw.md) — 另一项把 agent 工作台与可执行结构工程 benchmark 配对的土木工作，但靠求解器一致性而非检测结论来验证。
- [DrafterBench](./drafterbench.md) — 同样以土木工程交付物为受评工件，落在图纸而非检测影像上。
- [PE Civil Bench](./pe-civil-bench.md) — 用执业资格考试式的题目而非现场证据来衡量土木工程胜任力。
