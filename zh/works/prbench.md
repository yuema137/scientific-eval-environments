# PRBench (2026)

> [English](../../works/prbench.md) | **简体中文**

> **首次公开：** 2026-03-29 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2603.27646)

## Overview

PRBench 是一个 benchmark，检验 AI agent 能否端到端地复现已发表的物理研究——理解论文方法、从零实现相应算法，并产出与原始出版物相符的定量结果。它包含 30 个专家策划的任务，覆盖 11 个物理子领域，每个任务都在沙箱执行环境中运行。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.27646>
- **Project:** <https://prbench.phybench.cn/>

## Summary

PRBench 针对一个开放问题：由大语言模型驱动的 AI agent 能否可靠地对真实科学论文进行端到端复现。作者构建了 30 个专家策划的物理任务，由北京大学物理学院 20 多个研究组的领域专家贡献，每个任务都基于一篇真实发表的论文，并通过端到端复现加以验证，附带经过核验的 ground-truth 结果与详细的评分 rubric。表现最好的 agent——由 GPT-5.3-Codex 驱动的 OpenAI Codex——取得 34% 的平均总分，且所有被评估的 agent 的 end-to-end callback success rate 均为零。

## Tasks

30 个任务。每个任务只向 agent 提供任务说明与完整论文内容，要求其理解一篇已发表物理论文的方法、从零实现相应算法，并产出与原始出版物相符的定量结果，预期输出采用标准化的 CSV 格式。任务由北京大学物理学院 20 多个研究组的领域专家贡献，并经过四阶段流程：论文遴选、专家参考实现、结构化任务规格说明，以及对照原始出版物的独立核验。

## Domains

物理学：11 个子领域，包括量子色动力学（QCD）、量子光学、核物理、等离子体物理与凝聚态物理。

## Evaluation

- **加权 rubric 评分：**每个任务按四个维度评分——Methodology Understanding（权重 0.05）、Code Implementation Correctness（0.30）、Data Reproduction Accuracy（0.60）、Task Completeness（0.05）——加权求和为总分，并对照该任务由专家撰写的 rubric 评定。
- **End-to-end callback rate：**一次运行只有在所有维度得分均高于 0.9 时才算成功；callback rate 定义为 agent 取得此类端到端成功的任务占比。
- **Agent 化评估流水线：**white agent 负责解题与执行，green agent 负责编排与评分，在同一沙箱环境中将生成的输出与领域专家提供的 ground-truth 元数据进行比对。
- **报告结果：**表现最好的 agent——OpenAI Codex (GPT-5.3-Codex)——取得 34% 的平均总分，其中 Code Implementation Correctness 为 43%、Data Reproduction Accuracy 为 21%；基于 OpenCode 的 agent 依次为 GPT-5.3-Codex 28.5%、Kimi K2.5 (1T) 20.57%、DeepSeek V3.2 (671B) 18.5%、Minimax 2.7 (230B) 17.97%、GLM-5 (744B) 17.87%；所有 agent 的 end-to-end callback rate 均为零。

## Typical Duration

每个任务的沙箱限制为 800–21,600 秒的执行超时与 2–8 GB 的内存上限（依任务而定），且任务在遴选时即要求可在数小时内执行完毕。未说明步数、token 或金额预算。

## Main Contribution

一个由 30 个专家策划的论文复现任务构成的严格 benchmark，用于评估迈向自主科学研究的进展，任务植根于真实发表的物理论文，附带经过核验的 ground-truth 结果与详细的评分 rubric。

## Key Design Ideas

- 每个任务都植根于一篇真实发表的物理论文，随任务说明一同提供经过核验的 ground-truth 结果与细粒度评分 rubric。
- 封闭设定：agent 只获得任务说明与论文内容，必须在沙箱执行环境中从零实现全部算法。
- 以结果为重的加权评分：Data Reproduction Accuracy 权重为 0.60，Code Implementation Correctness 为 0.30，Methodology Understanding 与 Task Completeness 各为 0.05。
- 双 agent 评估设计：负责解题的 white agent 与负责编排执行、并对照专家提供的 ground truth 评分的 green agent 配对。

## Strengths

- 通过端到端复现进行的专家验证，使每个任务都拥有经过核验的 ground-truth 结果，而非从源论文推断出的答案。
- Callback 判据——所有维度均高于 0.9——将完整复现与部分得分分开度量，其当前为零的取值给出强 headroom 信号。
- 失败模式分析在总分之外识别出系统性的错误类别，包括公式实现错误、无法调试数值模拟，以及伪造输出数据。

## Limitations

- Repository note: 所有任务均由单一机构——北京大学物理学院——的研究组贡献，子领域覆盖因此反映单一学术社区的研究布局。
- Repository note: 评分由 agent 化评估流水线中的 green agent 发起，各维度得分因此依赖对照专家提供的 ground-truth 元数据所做的自动化 rubric 评判。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样从同行评审出版物中提取任务，但评估的是独立的数据分析程序，而非对论文定量结果的端到端复现。
- [Aviary](./aviary.md) — 同样让 language agent 在执行环境中完成科学任务，但构建的是各环境提供终止奖励、供训练用的 gymnasium，而非由专家验证的复现任务组成的固定 benchmark。
