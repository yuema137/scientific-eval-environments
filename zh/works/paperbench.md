# PaperBench (2025)

> [English](../../works/paperbench.md) | **简体中文**

> **首次公开：** 2025-04-02 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2504.01848)

## Overview

PaperBench 评估 AI agent 能否复现最前沿的 AI 研究：agent 需从零复现 20 篇 ICML 2024 Spotlight 与 Oral 论文——理解贡献、搭建代码库、执行实验——并对照与论文作者共同开发的层级式评分标准判分，可判分节点共 8,316 个。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.01848>
- **Code:** <https://github.com/openai/preparedness>
- **Venue:** arXiv preprint (cs.AI, cs.CL), 2025

## Summary

PaperBench 通过把每篇论文分解为带明确判分标准的层级式子任务，使「复现」可以客观打分——评分标准与论文作者共同开发。LLM judge 按标准大规模评判复现尝试，而 judge 本身也在一个单独的 judge benchmark 上被评估。受评中最好的 agent——配开源脚手架的 Claude 3.5 Sonnet (New)——平均复现分仅 21.0%；受邀的顶尖 ML 博士在所试子集上仍然胜过模型。

## Tasks

从零复现 20 篇 ICML 2024 Spotlight 与 Oral 论文，分解为 8,316 个可单独判分的评分节点，覆盖理解、代码库开发与实验执行。

## Domains

AI 研究（机器学习）：ICML 2024 论文的复现。

## Evaluation

- **先复跑，再判分。** 每篇论文都配一份与作者共同开发的层级式评分标准。agent 的运行结束后，提交物会被复制到一台全新的 Ubuntu 24.04 虚拟机（配一块 A10 GPU），从干净状态执行其中的 `reproduce.sh`，这样运行期间硬写进去的结果就能和代码真正跑出来的结果区分开。随后 SimpleJudge 逐个判定评分标准的叶节点，输入包括论文、完整的评分标准 JSON、该节点的具体要求，以及它自己排序后认为最相关的十个提交文件。
- **judge 自己也有一套 benchmark。** JudgeEval 取 PaperBench 中四篇论文加开发集中一篇论文的部分复现结果，这些复现或从零写成、或改自原作者的代码库，再由研究者逐个叶节点人工判分，把这些人工标签当作 judge 二分判断的 ground truth。按论文做宏平均后，SimpleJudge 换用不同后端模型的 F1 依次为：GPT-4o-mini 0.59（每篇 $8）、GPT-4o 0.73（$120）、o1-mini 0.78（$72）、o1 0.84（$830）、o3-mini 0.83（$66），随机打标签为 0.49。主结果采用 o3-mini，取的是性价比而不是最高 F1。
- **报告。** 最好的受评 agent（配开源脚手架的 Claude 3.5 Sonnet (New)）平均 21.0%。在一个三篇论文的子集上，ML 博士基线在 48 小时的有效工时后达到 41.4%，同一子集上 o1 为 26.6%；在一次 36 小时的加长运行里，o1 前期领先于人类，24 小时后被人类反超。

## Typical Duration

agent 的单次运行上限为 12 小时，环境是配单块 NVIDIA A10 GPU 的 Ubuntu 24.04 Docker 容器；另有一次 o1 搭配 IterativeAgent 的加长运行跑到 36 小时，每小时存一次快照，并在第 1、3、6、12、36 小时的快照上判分。独立的复跑环节把 `reproduce.sh` 的运行时间上限设为 12 小时，实测足够所有脚本跑完，agent 产出的脚本平均只跑 5.5 分钟。8 位人类基线参与者以兼职方式投入，有效工时由工时表记录，其分数取自相同工时刻度上的快照。

## Main Contribution

与作者共同开发的层级式评分标准，把「agent 是否复现了论文」变成数千个可客观判分的子判断——连判分用的 judge 也被单独评测。

## Key Design Ideas

- 与原作者共同制定评分标准，确定「什么才算复现」。
- 层级分解在细粒度上给出部分得分，而非单一的复现与否。
- 单独的 judge benchmark 使自动评分器的可靠性成为一个被实际测量的量。

## Strengths

- 8,316 个判分节点为「复现败在哪里」提供了少见的分辨率。
- 同期的专家人类基线为模型分数提供锚点。

## Limitations

- Repository note: 所有分数都由 judge 给出。o3-mini 版 SimpleJudge 在 JudgeEval 上的 F1 是 0.83，并非与人工完全一致，而 JudgeEval 本身只由五篇论文的部分复现构成，因此判分误差是在一个很小的标注样本上被测出来的，而不是被消除了。
- Repository note: 题集是机器学习方向的 20 篇 ICML 2024 论文；人类基线只在其中 4 篇上采集、每篇 3 次尝试，而对外报告的专家对比又落在一个三篇论文的子集上，所以这个人类锚点覆盖的只是 benchmark 的一小块。

## Related Works

- [ReplicationBench](./replicationbench.md) — 同样是与作者共同开发的论文复现，面向天体物理而非 AI 研究。
- [PRBench](./prbench.md) — 同样按评分标准打分的论文复现，在物理领域。
- [CORE-Bench](./core-bench.md) — 同样面向可复现性，但基于论文提供的代码与数据而非从零开始。
