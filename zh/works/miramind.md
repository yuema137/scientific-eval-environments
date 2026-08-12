# MiraMind (2025)

> [English](../../works/miramind.md) | **简体中文**

## Overview

MiraMind 是一个评估大语言模型心理健康推理的 benchmark，它不仅为任务结果评分，还评估把有限、主观的证据连向临床判断的显式推理轨迹的可靠性。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2512.09636
- **Venue:** Preprint (arXiv, cs.CL)

## Summary

MiraMind 把心理健康推理刻画为一个证据受限的判断问题：模型必须把有限、含糊的证据转化为解释、决定或论断，而这些结论在具体性、确定性、严重性与可操作性上都须由该证据支撑。该 benchmark 统一了跨 13 个数据集的六个任务族，覆盖评估性判断、诊断、干预、多步骤精神科问答、抽象概括与核实。除最终答案准确率外，它还沿可用性、逻辑结构与信息贡献三方面评估连接证据到判断的推理轨迹。对 20 个 LLM 的评估暴露出一种「克制落差」：模型判断的具体性或确定性超出了可用证据所能支撑的程度；作者还额外训练了一个专门针对证据到判断这一转化环节的 8B 模型 Mindora。

## Tasks

跨 13 个数据集的六个任务族（数据集名称沿用论文所报告）：

- **评估性判断（认知模式推理）：** 从简短的个人陈述中识别认知错误模式——CognitiveReframing、PatternReframe、Therapist Q&A。
- **诊断（心理状况推理）：** 从非正式的用户叙述中预测心理健康状况或严重程度标签——DepSign、SWMH、T-SID。
- **干预（治疗行动推理）：** 从来访者案例摘要中选择合适的咨询策略——PsyDTCorpusM、AnnoMIM。
- **多步骤（精神科问答）：** MHQA、MedQAM、MedMCQAM、PubMedQAM。
- **抽象概括（基于证据的精神科摘要）：** 从 Cochrane 精神科系统综述摘要中生成「Main Results」摘要——PSRS（新整理）。
- **核实（心理健康错误信息检测）：** 对在线心理健康论断是准确还是误导做二元分类——MentalMisinfo。

报告的样本量包括 PSRS 的 108 个测试样本（由精神科医生按 0–2 评分标准标注）与 AnnoMIM 的 133 个测试样本（真实的动机式访谈对话）。其余各数据集的训练/验证/测试规模见论文的数据集表。完整的各数据集规模表为 TODO(reference)。

## Domains

心理健康/精神病学与临床心理学——折并入 Medicine & Health 与 Neuroscience & Cognitive Science。证据来源涵盖非正式用户叙述（如 Reddit/Twitter 帖子）、咨询对话、精神科委员会式问答，以及 Cochrane 系统综述摘要。

## Evaluation

任务结果采用按任务族划分的指标：评估性判断与诊断用 Micro-F1，干预（多标签策略选择）用 Jaccard 相似度，抽象概括用对专家标注评分点的召回，核实用 Macro-F1。多步骤问答的指标为 TODO(reference)。

推理轨迹用 LLM-as-judge 协议沿三个维度评分：**可用性**（术语简约度、步骤充分性）、**逻辑结构**（逻辑连贯性、无关率、矛盾率）与**信息贡献**（信息量）。judge 在评分前会把每条轨迹切分为推理内容单元。作者报告了一项人工验证研究，其中 100 条轨迹由两名受训评估者独立标注。具体的 judge 模型为 TODO(reference)。

## Typical Duration

TODO(reference) —— 论文未报告标准化的每任务 wall-clock 时间或 token 预算。

## Main Contribution

一个「超越答案准确率」评估心理健康推理的统一 benchmark：它同时评估任务结果与显式推理轨迹的可靠性，并在各 LLM 中暴露出一种共有的「克制落差」——判断的具体性或确定性超出证据所支撑的程度。

## Key Design Ideas

- 把心理健康推理刻画为一个证据受限的判断问题，其中具体性、确定性、严重性与可操作性各自被支撑的程度本身即评估对象。
- 把结果评分与轨迹评分分离，使一个正确的最终答案不会掩盖背后从证据到判断的不可靠推理路径。
- 一套多维轨迹评分标准（可用性、逻辑结构、信息贡献），应用于 LLM 切分出的推理单元。
- 覆盖六个功能各异的任务族（评估性判断、诊断、干预、多步骤问答、抽象概括、核实），而非单一临床角色。
- 一个示范模型 Mindora（8B，基于 Qwen3-8B），经难例监督、结构化轨迹重写与一致性感知的 SFT–RL 目标后训练；报告在受评模型中取得最佳平均排名，并在全部六个任务族上优于其骨干模型。

## Strengths

- 评估推理轨迹而不只是最终答案，给出仅靠结果准确率会漏掉的可靠性信号。
- 覆盖广泛：六个任务族、13 个数据集，横跨多种心理健康推理角色与证据形式。
- 含对轨迹评判协议的人工标注验证（100 条轨迹，两名标注者）。
- 把跨模型的「克制落差」暴露为一个具体、共有的失败模式。

## Limitations

- 轨迹评分依赖 LLM-as-judge，会继承 judge 模型的偏差与可靠性局限。judge 模型身份与报告的 judge–人类一致性为 TODO(reference)。
- Repository note: 论文把一个评估 benchmark（MiraMind）与一个训练所得模型（Mindora）耦合在一起；benchmark 是评估贡献，而 Mindora 是训练示范，其增益是在该 benchmark 自身指标上报告的。
- Repository note: 编卡时在论文文本中未找到公开代码或数据发布 URL；若干构成数据集各带其自身的许可与访问条件。

## Related Works

TODO(reference) —— 相关的心理健康/医学推理 benchmark 与轨迹评估工作，待其成卡后链接。
