# CORE-Bench (2024)

> [English](../../works/core-bench.md) | **简体中文**

## Overview

CORE-Bench（Computational Reproducibility Agent Benchmark）测量 AI agent 能否用论文自带的代码与数据重现已发表研究的结果：270 个任务，基于计算机科学、社会科学与医学三个学科的 90 篇论文，分三档难度。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.11363>
- **Code:** <https://github.com/siegelz/core-bench>
- **Venue:** arXiv preprint, 2024

## Summary

CORE-Bench 瞄准计算可复现性——用研究自己发布的代码与数据重现其结果——这项对科学过程根本、却出乎意料困难的真实任务。任务分三档难度，含纯语言与视觉-语言两种形式，并配有快速、可并行的评估系统，比顺序评估每轮节省数天。基线（通用的 AutoGPT 与任务专用的 CORE-Agent，各配 GPT-4o 与 GPT-4o-mini）在最难档上最高只有 21% 的准确率。

## Tasks

270 个任务，来自三个学科的 90 篇科学论文，分三档难度，含纯语言与视觉-语言两种形式；agent 基于每篇论文提供的代码与数据工作。

## Domains

计算机科学、社会科学与医学——任务所取材论文的三个学科。

## Evaluation

- 重现结果的准确率，由快速、可并行的评估系统校验。
- **报告。** 最好的 agent 在最难档上仅达 21% 准确率。

## Typical Duration

基于论文提供的代码与数据的多步重现工作流；预算为 TODO(reference)。

## Main Contribution

把研究自动化的下限——用已发表工作自身的代码与数据重跑它——单独划分出来，并表明连这个下限都远未被攻克。

## Key Design Ideas

- 基于论文提供的代码与数据工作，把可复现性与重新发明区分开。
- 三档难度衡量 agent 获得多少脚手架。
- 可并行的评估使反复的 agent 比较切实可行。

## Strengths

- 直接对应一项真实且要紧的科学实践。
- 跨学科覆盖，而非单领域测试台。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [PaperBench](./paperbench.md) — 同样聚焦复现，但对照作者评分标准从零开始，而非基于提供的工件。
- [EXP-Bench](./exp-bench.md) — 同样端到端重现已发表实验，按阶段由 LLM judge 评分。
- [AutoMat](./automat.md) — 同样从论文与工件出发做论断复现，在计算材料科学领域。
