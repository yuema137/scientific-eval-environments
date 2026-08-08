# Mechanical & Aerospace Engineering

> [English](../../domains/mechanical_aerospace_engineering.md) | **简体中文**

## Scope

机械与航空航天工程。计算流体力学与热输运折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| CFDLLMBench | 2025 | 三个深度上的计算流体力学：研究生水平知识（CFDQuery）、用 Python 数值求解给定 PDE（CFDCodeBench）、端到端 OpenFOAM 算例配置与执行（FoamBench）。 | 240 个任务：90 道专家整理的选择题、24 个 PDE 求解器编程题、126 个 OpenFOAM 算例（110 个由 tutorial 派生 + 16 个刻意不同于任何 tutorial 的专家手工算例）。 | 执行加对照参考解的分档归一化误差（NMSE），以及网格与时间步细化下的显式收敛检查；接受任何有效的数值方法。 | [→](../works/cfdllmbench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Engineering Sciences 分组下的机械工程任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |

## Related Works

- [CFDLLMBench](../works/cfdllmbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
