# MolQuest (2026)

> [English](../../works/molquest.md) | **简体中文**

## Overview

MolQuest 把化学结构解析重铸为 agent 任务：在多轮交互设定中，模型必须主动规划实验步骤、整合 NMR、MS 等异质谱学来源，并迭代修正结构假设——最先进的模型也只有约 50% 的准确率。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.25253>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

分阶段的 benchmark 把谱图直接递到模型手里，MolQuest 却要模型自己去把谱图挣到手：结构解析被形式化为溯因推理的多轮循环——选择实验、读取所得谱图、修正结构假设。在这一 agent 式评估框架下，最先进的模型也只达到约 50% 的准确率，多数模型不到 30%。

## Tasks

多轮交互的结构解析回合：规划实验步骤、整合 NMR/MS 等谱学来源、迭代修正假设。实例数量为 TODO(reference)——摘要未载明。

## Domains

化学——分析化学：把谱学驱动的结构解析作为顺序实验推理来评估。

## Evaluation

- 在 agent 式多轮协议下评估最终解析结构的准确率。
- **报告。** SOTA 模型约 50% 准确率；多数其他模型低于 30%。

## Typical Duration

多轮交互回合，实验步骤由模型自主发起。

## Main Contribution

把解析评估从「解读给定的谱图」推进到「决定采集哪些谱图」——补上静态 benchmark 缺失的溯因与实验规划那一半能力。

## Key Design Ideas

- 实验选择是被测量的行为本身，而非由 benchmark 事先固定。
- 迭代假设修正奖励能够增量利用证据的模型。
- 溯因框架：目标是最能解释累积证据的结构。

## Strengths

- 与静态解析 benchmark 形成直接互补，补上了交互式规划这一维度。
- 50% 的上限说明即便前沿模型也有可观的提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要之外的细节有待全文校验。论文 arXiv 页面上无法核实任何代码或项目发布。

## Related Works

- [MolPuzzle](./molpuzzle.md) — 静态、分阶段的对应物：同一个谱图推结构问题，但没有交互。
- [SMDD-Bench](./smdd-bench.md) — 同样是信息受限下的多轮分子问题求解。
- [Gravity-Bench-v1](./gravity-bench.md) — 同样把「选择观测/实验」纳入科学推断的被测范围。
