# MOOSE-Chem (2024)

> [English](../../works/moose-chem.md) | **简体中文**

## Overview

MOOSE-Chem 评估 LLM 能否重新发现未见过的化学假说：benchmark 由 51 篇 2024 年 1 月之后发表的高影响力化学论文组成，每篇均由化学博士标注出背景、灵感来源与假说；配套一个 agent 式框架，依次完成灵感检索、假说组合与假说排序。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.07076>
- **Code:** <https://github.com/ZonglinY/MOOSE-Chem>
- **Venue:** ICLR 2025

## Summary

MOOSE-Chem 从数学上把假说发现分解为三个子任务——检索灵感、用灵感组合假说、为假说排序——并将这一分解直接实现为 agent 式 LLM 框架。为了排除污染，benchmark 选用 51 篇 2024 年 1 月之后的高影响力化学论文（专家标注为背景、灵感、假说三部分），并使用知识截止早于 2024 年的 LLM。该框架重新发现了许多与真值高度相似的假说，在灵感检索上的准确率高得出人意料。

## Tasks

基于 51 篇专家标注化学论文的重发现任务：从论文背景与灵感语料库（官方发布含 3,000 篇论文）出发，重新生成该论文的假说。多阶段 agent 管线，非环境交互式。

## Domains

化学——不限子领域的化学假说发现，以近期高影响力文献为基准。

## Evaluation

- 重发现假说与标注真值假说的相似度，并按子任务（检索、组合、排序）分别考核；通过 2024 年前的知识截止控制污染。
- **报告。** 许多假说以高相似度被重新发现；灵感检索准确率出人意料地高。定量数字为 TODO(reference)——摘要未载明。

## Typical Duration

每篇论文一个多阶段管线回合（检索 → 组合 → 排序）。

## Main Contribution

一套控制污染的科学假说重发现协议：近期专家标注论文加知识截止模型，让「机器能不能发现这个」成为可测量的问题。

## Key Design Ideas

- 背景/灵感/假说的标注方案把「发现」变成可分解、可分级评判的管线。
- 截止后论文配截止前模型，给出干净的「不可能是背下来的」保证。
- 把排序设为显式子任务，测系统能否认出自己最好的假说。

## Strengths

- 51 篇论文全部由化学博士标注，真值扎根于专家判断。
- 分解使部分得分有意义——检索、组合、排序各自独立地失败。

## Limitations

- Repository note: 该论文的头号贡献是 MOOSE-Chem agent 框架；51 篇论文的 benchmark 是为评估它而构建的。本卡片覆盖 benchmark，框架作为配对方法记录。
- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [ResearchClawBench](./researchclawbench.md) — 同样是对隐藏已发表结论的重发现，端到端覆盖十个领域。
- [HeurekaBench](./heurekabench.md) — 同样评估复现已发表的科学发现，以论文为评判依据。
- [MolQuest](./molquest.md) — 同样是溯因式化学推理，尺度在结构解析层面。
