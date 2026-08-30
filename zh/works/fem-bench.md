# FEM-Bench (2025)

> [English](../../works/fem-bench.md) | **简体中文**

> **首次公开：** 2025-12-23 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2512.20732)

## Overview

FEM-Bench 是面向代码生成 LLM 的计算力学结构化科学推理 benchmark：FEM-Bench 2025 收录与研究生第一门计算力学课程对齐、入门但不平凡的任务——函数编写赛道 33 个任务——配客观验证与成对的单元测试编写评估。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.20732>
- **Venue:** arXiv preprint (cs.LG, cs.AI, cs.SE), 2025

## Summary

FEM-Bench 把有限元方法当作探针，考察模型能否把物理推理——力、变形、约束——落成正确的数值代码。模型在两条赛道上各尝试五次：编写 FEM 及相关函数，以及编写单元测试，两者都客观验证。函数编写最强的 Gemini 3 Pro 有 30/33 个任务至少成功一次、26/33 个任务五次全部成功；测试编写最强的 GPT-5 的 Average Joint Success Rate 为 73.8%——有能力，但离工程实践要求的可靠性还有距离。

## Tasks

与研究生课程对齐的计算力学编码任务（函数编写赛道 33 个），外加单元测试编写赛道；每个模型-任务对尝试五次。

## Domains

计算力学与有限元方法：把力、变形与约束落成代码。

## Evaluation

- 对生成函数与单元测试的客观验证；每任务五次尝试的成功统计；测试编写用 **Average Joint Success Rate**。
- **报告。** Gemini 3 Pro 有 30/33 个函数任务至少成功一次、26/33 个五次全成；GPT-5 在测试编写上达 73.8% Average Joint Success Rate。

## Typical Duration

单函数与单测试的生成；非交互式设定。

## Main Contribution

把 FEM 代码生成锚定在人类工程师受训的粒度上——并把测试编写列为受评能力，因为验证代码与求解代码同样重要。

## Key Design Ideas

- 与课程对齐使难度尺度对力学界一目了然。
- 五次尝试的评估把偶然成功与可靠成功分开。
- 单元测试赛道测的是模型能否验证（而不只是产出）数值代码。

## Strengths

- 难度校准得当、客观验证干净。
- 一次成功与五次全成之间的落差（30/33 vs 26/33）量化了不稳定性。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [PDEAgent-Bench](./pdeagent-bench.md) — 同样是 FEM 库代码生成，规模到研究级并带分级的精度/效率关卡。
- [FEABench](./feabench.md) — 同样是有限元评估，通过操作专业软件而非编写函数。
- [SciCode](./scicode.md) — 同样是带金标准测试、面向科学家的科研代码生成，横跨 16 个子领域。
