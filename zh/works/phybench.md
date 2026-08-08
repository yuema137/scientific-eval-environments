# PHYBench (2025)

> [English](../../works/phybench.md) | **简体中文**

## Overview

PHYBench 是含 500 道原创物理问题的 benchmark，难度从高中到物理奥赛，用 Expression Edit Distance（EED）分数——一种作用于数学表达式的连续指标——评分；论文报告该指标比二元计分把样本效率提升 204%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.16074>
- **Project:** <https://www.phybench.cn/>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks

## Summary

PHYBench 评估物理感知与多步骤、多条件的推理，题目全部为 benchmark 原创——从构造上杜绝污染。EED 分数衡量错误符号答案「差多远」，而不是把所有错误一视同仁；论文报告在 AIME 2024、OlympiadBench 与 GPQA 已趋饱和的地方，该 benchmark 仍能区分模型。人类专家基线为分数提供外部锚点：最佳模型 Gemini 2.5 Pro 准确率 36.9%，人类专家为 61.9%。

## Tasks

500 道原创物理问题，难度从高中到物理奥赛；静态文本解题，答案为符号表达式。

## Domains

高中到奥赛难度区间的物理解题；子领域构成摘要未说明。

## Evaluation

- 作用于数学表达式的 **Expression Edit Distance（EED）分数**，报告比二元计分提升 204% 样本效率；同时报告准确率。
- **报告。** 最佳模型 Gemini 2.5 Pro 准确率 36.9%，人类专家 61.9%。

## Typical Duration

单题解题；非交互式 agent 设定。

## Main Contribution

以原创性做防污染、以连续表达式指标做评分，得到一个在标准套件饱和处仍能区分前沿模型的物理 benchmark。

## Key Design Ideas

- 所有题目为 benchmark 而写，预训练暴露从构造上被排除。
- EED 让符号答案的部分正确变得可测量。
- 实测的人类专家基线为分数提供外部锚点。

## Strengths

- 仅 500 题即取得很强的模型区分度，归功于连续指标。
- 25 个百分点的人机差距量化了剩余提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [CMPhysBench](./cmphysbench.md) — 同样以表达式编辑距离（SEED）为物理答案评分，在凝聚态研究生水平。
- [PhysGym](./physgym.md) — 以 PHYBench 的问题为素材构建其交互式发现环境。
- [HiPhO](./hipho.md) — 同样是奥赛难度物理，用官方人工评分方案判分。
