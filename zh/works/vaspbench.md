# AutoDFT / VASPBench (2026)

> [English](../../works/vaspbench.md) | **简体中文**

> **首次公开：** 2026-05-25 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.26179)

## Overview

VASPBench 是面向自主密度泛函理论计算的专建 benchmark，横跨 34 个任务、9 种 DFT 计算类型；它随 AutoDFT 一同发布——一个闭环多 agent 框架，负责规划、运行并修复 VASP 计算，用 GPT-5.2 达到 94.1% 的任务级成功率。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.26179>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2026

## Summary

搭建 DFT 既专业又琐碎、还容易出错，AutoDFT 把这一循环自动化：战略规划器列出骨架式的步骤目标，步骤规划器即时填入数值参数，「监控-恢复-反思」循环诊断并修复失败、同时修订计划。VASPBench 在 34 个任务、9 种 DFT 计算类型上测量这套系统，AutoDFT 用 GPT-5.2 达到 94.1% 的任务级成功率，并在既有材料数据库上对电子、磁性与能量性质给出定量可靠的预测。

## Tasks

横跨 9 种计算类型的 34 个 DFT 计算任务；agent 以闭环方式规划、执行并修复 VASP 运行。交互式/agent 化；运行真实 DFT 计算。

## Domains

材料科学——自主密度泛函理论工作流执行（VASP），产出电子、磁性与能量性质预测。

## Evaluation

- VASPBench 上的任务级成功率，加对照既有材料数据库的定量性质预测准确率。
- **报告。** AutoDFT 用 GPT-5.2 达到 94.1% 的任务级成功率。

## Typical Duration

每个 DFT 任务一段闭环、多步回合，含失败诊断与重规划。

## Main Contribution

把自主、能自我修复的 agent 带入 DFT 计算搭建——并提供一个 benchmark（VASPBench），评判 agent 能否把真实的电子结构工作流驱动到正确结果。

## Key Design Ideas

- 把战略规划器与即时步骤规划器分开，对应专家分阶段推进 DFT 的方式。
- 「监控-恢复-反思」循环把失败修复纳入被测行为。
- 对照既有数据库检验性质正确性，而不只是作业完成度。

## Strengths

- 材料领域最早的 DFT 工作流编排 agent benchmark 之一。
- 评估的是闭环失败修复，而非一次性搭建。

## Limitations

- Repository note: 该论文的头号贡献是 AutoDFT 框架；VASPBench 是其配对 benchmark，本卡片以 benchmark 为中心。arXiv 页面无法核实 VASPBench 的公开发布，arXiv 元数据无发表信息。

## Related Works

- [MatTools](./mattools.md) — 同样是 LLM 驱动材料计算，走 pymatgen 工具使用而非 DFT 编排。
- [MDArena](./mdarena.md) — 同样是 agent 式计算工作流，对象是分子动力学而非 DFT。
- [EnvTrace](./envtrace.md) — 同样以执行行为评估科学仪器/计算的控制。
