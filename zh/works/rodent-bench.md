# Rodent-Bench (2026)

> [English](../../works/rodent-bench.md) | **简体中文**

> **首次公开：** 2026-02-20 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.18540)

## Overview

Rodent-Bench 评测多模态 LLM 标注啮齿类行为视频的能力，覆盖多种神经科学范式——社交互动、理毛、抓挠、僵直——视频长 10–35 分钟；结论是当前没有模型强到能充当标注助手。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.18540>
- **Venue:** arXiv preprint (cs.CV), 2026

## Summary

行为标注是啮齿类神经科学中一个耗费人力的瓶颈，Rodent-Bench 检验多模态 LLM 能否帮上忙。它在真实啮齿类行为视频上评测 Gemini-2.5-Pro、Gemini-2.5-Flash 与 Qwen-VL-Max，覆盖多种范式（社交互动、理毛、抓挠、僵直），视频长 10 至 35 分钟，含两个 benchmark 版本。按逐秒准确率、宏 F1、平均精度均值、互信息与 Matthews 相关系数评分，没有模型强到能充当助手，尤其在时间分割、长序列与细微行为状态上吃力。

## Tasks

对真实啮齿类行为视频做时间分割与行为分类，覆盖多种范式；长录像（10–35 分钟）；两个 benchmark 版本。静态多模态标注。视频/实例数量为 TODO(reference)——摘要未载明。

## Domains

神经科学与认知科学——行为神经科学：啮齿类行为视频标注（社交、理毛、抓挠、僵直范式）。

## Evaluation

- 逐秒准确率、宏 F1、平均精度均值、互信息与 Matthews 相关系数，覆盖三个 MLLM。
- **报告。** 没有模型强到能充当助手；在部分数据集（如理毛）上有一般表现；在时间分割、长序列与细微状态上吃力。

## Typical Duration

对 10–35 分钟录像的逐视频标注；静态（无交互）。

## Main Contribution

对「多模态 LLM 作为啮齿类神经科学行为标注助手」的真实检验——表明当前模型正好在该任务所需的时间、长上下文与细粒度辨别上力有不逮。

## Key Design Ideas

- 长真实录像（10–35 分钟）考的是时间与长上下文处理，而非单帧。
- 五个指标刻画超越帧准确率的分割质量。
- 多种范式覆盖神经科学标注真正需要的行为。

## Strengths

- 真实啮齿类行为数据，覆盖真正不同的范式。
- 「尚不能充当助手」是具体、影响决策的结论，指标丰富。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；视频/实例数量与各模型数字在正文中，arXiv 页面无法确认代码 URL。arXiv 元数据无发表信息。

## Related Works

- [BrainBench (EEG)](./brainbench-eeg.md) — 同样是多模态神经科学数据分析，对象是 EEG 信号而非行为视频。
- [SpatialBench](./spatialbench.md) — 同样是对真实生物数据的可验证分析，在空间转录组学。
- [BioXArena](./bioxarena.md) — 同样是 agent 端到端分析多模态生物数据。
