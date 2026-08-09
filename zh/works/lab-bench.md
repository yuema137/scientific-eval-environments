# LAB-Bench (2024)

> [English](../../works/lab-bench.md) | **简体中文**

## Overview

LAB-Bench（Language Agent Biology Benchmark）测量语言模型面向生物学研究的能力：2,400 余道选择题，横跨八个类别——文献回忆与推理（LitQA2）、图表解读（FigQA、TableQA）、数据库访问（DbQA、SuppQA）、协议规划（ProtocolQA）与 DNA/蛋白质序列操作（SeqQA、CloningScenarios）——配人类专家生物学研究者基线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)
- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.10362>
- **Dataset:** <https://huggingface.co/datasets/futurehouse/lab-bench>
- **Venue:** arXiv preprint (cs.AI), 2024

## Summary

LAB-Bench 瞄准的是生物学研究实际需要的实用能力而非教科书知识：对文献的回忆与推理、图表解读、数据库的访问与导航、以及 DNA 与蛋白质序列的理解与操作。八个子任务中包括被广泛引用的 CloningScenarios（多步分子克隆工作流），评分对照人类专家生物学研究者；约 80% 的题目（1,967 道）公开发布。

## Tasks

2,400 余道选择题，八个类别 / 30 个子任务：LitQA2、DbQA、SuppQA、FigQA、TableQA、ProtocolQA、SeqQA 与 CloningScenarios；静态，可选配工具。

## Domains

广义的生物学研究实践：分子生物学与克隆、DNA 与蛋白质序列、协议、文献与数据库。

## Evaluation

- 对照答案的选择题评分，以人类专家生物学研究者为参照基线。
- **报告。** 模型与专家的对比数字为 TODO(reference)；摘要未给出数值结果。

## Typical Duration

单题作答，可选配工具；非交互式环境。

## Main Contribution

把生物学评估从考试知识转向研究实践——图表、数据库、序列、协议、克隆——并成为具备生物学能力的语言系统事实上的参考套件。

## Key Design Ideas

- 类别对应科研的日常动作（读、查、解读、规划、操作序列），而非课程主题。
- CloningScenarios 把序列级步骤串联起来，以选择题形式探查多步湿实验推理。
- 保留的私有题目集用于防污染。

## Strengths

- 全类别配备人类专家基线。
- 广泛采用使其分数成为整个领域的公共参照点。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方数据集材料编写（2026 年 8 月）；此外的细节有待全文校验。arXiv Comments 记录其向 NeurIPS 2024 Datasets and Benchmarks「投稿在审」；从这些来源无法证实录用。

## Related Works

- [LABBench2](./labbench2.md) — 后继套件：情境更真实、难度显著跃升。
- [BioProBench](./bioprobench.md) — 同样以协议为中心的评估，规模到语料级并含生成与修复任务。
- [Aviary](./aviary.md) — 同样出自 FutureHouse 的生物学评估，以交互环境呈现（SeqQA 与克隆在两条谱系中都出现）。
