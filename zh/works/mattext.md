# MatText (2024)

> [English](../../works/mattext.md) | **简体中文**

## Overview

MatText 是用大语言模型从晶体文本表示预测材料性质的 benchmark 框架：横跨九种表示、参数规模至 70B、数据规模至 200 万结构，记录了一种持续的「几何盲区」——LLM 能抓住类别模式却漏掉坐标信息，而专门的几何架构以显著优势胜过它们。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.17295>
- **Code:** <https://github.com/lamalab-org/MatText>
- **Project:** <https://lamalab-org.github.io/MatText/>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2024

## Summary

当前版本题为「Less can be more for predicting properties with large language models」，本工作引入 MatText benchmark 框架，检验 LLM 能否从文本编码预测晶体性质。它横跨九种文本表示（composition/Hill、SLICES、CIF P1、crystal-text-llm、原子序列、Z 矩阵、局部环境等）、参数规模至 70B、数据规模至 200 万结构，评测 Llama-3-8B（LoRA 微调）与自建 BERT 类模型，并对照几何 GNN 基线。结论是一堵「GNN-LM 墙」：LLM 一贯无法捕捉坐标信息，却擅长类别模式，几何架构以显著优势胜过它们。

## Tasks

跨九种表示从文本编码的晶体做性质回归（MatBench 任务——剪切/体积模量、钙钛矿形成能——加合成可调数据集）；静态预测，非交互。

## Domains

材料科学——从文本表示做晶体性质预测，并对照几何图神经网络。

## Evaluation

- 跨表示与规模的性质预测误差（回归），对照 GNN 基线。
- **报告。** LLM 抓住类别模式却漏掉坐标信息；几何架构以显著优势胜过 LLM（「GNN-LM 墙」）。

## Typical Duration

单次预测查询；无交互式设定。

## Main Contribution

把「几何盲区」单独界定为文本式 LLM 材料建模的结构性局限——一个「框架加发现」的工作，指出文本编码路线会在何处撞上几何感知模型这堵墙。

## Key Design Ideas

- 九种表示把「如何把结构编码为文本」变成被测变量。
- 扫过规模（至 70B、至 200 万结构）检验这一局限是否只是容量问题。
- 合成可调数据集直接分离坐标信息与类别信息。

## Strengths

- 表示扫描比任何单一编码研究都广。
- 几何盲区的诊断是具体、可落地的局限，而非一张排行榜。

## Limitations

- Repository note: 该论文的贡献是 MatText 框架加一项分析/立场发现；本卡片以 benchmark 框架为中心。论文已改题为「Less can be more for predicting properties with large language models」；arXiv 元数据无发表信息。

## Related Works

- [LLM4Mat-Bench](./llm4mat-bench.md) — 同样是从文本做 LLM 材料性质预测，性质与来源广度更大。
- [AtomWorld](./atomworld.md) — 同样探测 LLM 的晶体几何理解，走结构操作路线。
- [MatTools](./mattools.md) — 同样是 LLM 面向材料计算，走工具使用。
