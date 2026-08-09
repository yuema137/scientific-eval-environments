# MaScQA (2023)

> [English](../../works/mascqa.md) | **简体中文**

## Overview

MaScQA 是探测大语言模型材料科学知识的问答数据集：650 个取自印度 GATE 工程考试的高难度问题，分为四类；GPT-4 达到约 62% 准确率，且大多数错误是概念性而非计算性的。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.09115>
- **Code:** <https://github.com/M3RG-IITD/MaScQA>
- **Venue:** Digital Discovery, 2024（据官方仓库；arXiv 元数据无发表信息）

## Summary

MaScQA 从 GATE（研究生工程能力考试）试卷中策划出 650 个材料科学与冶金问题，覆盖 14 个主题、四种题型。GPT-3.5 与 GPT-4 在零样本与链式思维提示下作答，GPT-4 最好、约 62% 准确率。真正的要点在错误分析：概念性错误约占 64%，计算性错误约 36%，把短板定位在材料理解而非算术上。

## Tasks

650 个源自 GATE 的材料科学与冶金问题，四种题型、14 个主题；零样本与链式思维提示下的静态问答。

## Domains

材料科学——本科/研究生水平的材料科学与冶金工程知识，取自标准化工程考试。

## Evaluation

- 650 个问题上的准确率，配一套把概念性与计算性错误分开的错误分类。
- **报告。** GPT-4 最好、约 62% 准确率；概念性错误约 64% vs 计算性约 36%。

## Typical Duration

单轮问答；无交互式设定。

## Main Contribution

一次早期、以考试为依据的 LLM 材料知识测量，其错误分析表明缺口是概念性的——后续材料问答工作以之为基础。

## Key Design Ideas

- GATE 考试来源把难度锚定在公认的专业标准上。
- 四种题型把回忆与多步问题求解分开。
- 概念/计算错误的划分让失败模式具诊断性。

## Strengths

- 材料知识问答的干净、被广泛复用的参照，公开发布。
- 错误分类比单一准确率更有洞见。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、全文与官方仓库编写（2026 年 8 月）；数据集恰为 650 个问题（有时引用的「1,038」是误标）。Digital Discovery 发表由仓库声明，arXiv 元数据未载明。
- 仅评测现成的 GPT-3.5/GPT-4；原论文未覆盖更新的模型。

## Related Works

- [MatSciBench](./matscibench.md) — 同样是材料知识评估，扩展到 1,340 个含图像的大学水平推理问题。
- [OpenXRD](./openxrd.md) — 同样是专家策划的材料问答，专于晶体学。
- [MaCBench](./macbench.md) — 同样是材料/化学评估，在多模态设定中。
