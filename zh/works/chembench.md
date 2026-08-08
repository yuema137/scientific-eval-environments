# ChemBench (2024)

> [English](../../works/chembench.md) | **简体中文**

## Overview

ChemBench 追问的是大语言模型是否已是「超人化学家」：一套自动化评估框架，用 2,700 多个精心策划的问答对，把领先的开源与闭源 LLM 与人类化学家的专业水平直接对比——研究中最强的模型平均成绩超过了最强的人类化学家。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2404.01475>
- **Code:** <https://github.com/lamalab-org/chembench>
- **Project:** <https://chembench.lamalab.org>
- **Leaderboard:** <https://huggingface.co/spaces/jablonkagroup/ChemBench-Leaderboard>
- **Venue:** Nature Chemistry, 2025（据官方项目网站；arXiv 元数据未载明发表信息）

## Summary

论文题为「Are large language models superhuman chemists?」。ChemBench 策划了 2,700 多个覆盖化学知识与推理的问答对，用自动化框架为最先进的 LLM 评分，并与一组人类化学家对照。最强模型平均超过了研究中最强的化学家，但在一些基础任务上仍会出错，且给出过度自信的预测——作者将这一组合解读为能力惊人与安全隐忧并存，并认为它对化学教育有启示。

## Tasks

2,700 多个精心策划的化学知识与推理问答对；静态问答，不使用工具，自动评分。

## Domains

化学——以执业化学家为直接对照基准的化学知识与推理评估。

## Evaluation

- 自动化框架在策划问答对上为模型答案评分，配有人类化学家专家基线与置信度分析。
- **报告。** 最强模型平均超过研究中最强的人类化学家；模型在部分基础任务上仍会失手，且预测过度自信。

## Typical Duration

单轮问答；无交互式或 agent 设定。

## Main Contribution

一次大规模、以人类专家为基线的 LLM 化学能力测量，其框架成为可复用的基础设施——多模态的 MaCBench 就运行在同一条评估管线上。

## Key Design Ideas

- 2,700+ 的题量足以支撑按主题拆分的能力画像，而不只是一个总分。
- 招募真实化学家队列，把「超人」从修辞变成可测量的对比。
- 在准确率之外同步探测置信度，把过度自信单列为一种失败模式。

## Strengths

- 规模最大的专家基线化学评估之一，排行榜持续维护。
- 框架的生命力超过了论文本身：它是后续多模态评估的底座。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。Nature Chemistry 的发表信息由官方项目网站声明，arXiv 元数据未载明。
- 静态问答——测量的是不借助工具、不含多步实验/agent 工作流的化学能力。

## Related Works

- [MaCBench](./macbench.md) — 面向化学与材料的多模态（视觉-语言）扩展，运行在 ChemBench 管线上。
- [ChemEval](./chemeval.md) — 同样是广覆盖的化学能力评估，按递进层级组织。
- [ChemIQ](./chemiq.md) — 同样是专家水准的化学题目，聚焦有机化学并采用无 judge 的判分。
