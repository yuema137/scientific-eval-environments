# REFLECT / RoboFail (2023)

> [English](../../works/robofail.md) | **简体中文**

## Overview

REFLECT 在机器人多传感器经验的层级摘要之上让 LLM 解释失败，其解释进一步引导基于语言的规划器纠正失败；配对的 RoboFail 数据集提供多种任务与失败场景，在模拟与真实世界中评估这套「失败推理」闭环。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 能力探针，agent 本身并不执行科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2306.15724>
- **Code:** <https://github.com/columbia-ai-robotics/reflect>
- **Project:** <https://robot-reflect.github.io/>
- **Venue:** CoRL 2023

## Summary

REFLECT 把机器人的原始多传感器记录——视觉、听觉、本体感知——转换成 LLM 可推理的层级化经验摘要，再运行渐进式失败解释算法，定位并解释哪里出了错。解释不是终点：它作为条件输入纠正规划器，产出可执行的恢复计划。RoboFail 提供评估底座——注入了失败场景的一系列任务，在模拟与真实世界中评估。

## Tasks

对机器人任务执行的失败解释与纠正回合，覆盖多种任务与失败场景（RoboFail）；事后解释加交互式纠正重规划。数据集规模为 TODO(reference)——摘要与项目页均未载明。

## Domains

机器人学——基于多传感器执行记录的机器人操作失败分析，在模拟与真实世界的机器人任务上评估。

## Evaluation

- 失败解释的质量与由其引导的纠正规划的成功率；具体指标名称摘要与项目页未载明。
- **报告。** REFLECT 生成的失败解释信息量足以辅助成功的纠正规划。

## Typical Duration

对一次（失败的）已完成执行做事后分析，随后进入纠正回合。

## Main Contribution

把机器人失败解释确立为一项 LLM 推理任务，并闭环到恢复——后来的失败分析 benchmark 都建立在这一奠基性表述之上。

## Key Design Ideas

- 层级化经验摘要把多传感器流压缩成 LLM 能消化的结构。
- 渐进式解释从摘要层层收窄到失败步骤。
- 解释按其下游效用打分：纠正计划到底管不管用？

## Strengths

- 发表信息经核实的早期表述；RoboFail 成为后继系统的参考评估集。
- 同时覆盖模拟与真实世界的执行。

## Limitations

- Repository note: 该论文的头号贡献是 REFLECT 框架；RoboFail 是其配对数据集，本卡片覆盖数据集/benchmark 一侧。RoboFail 的规模数字无法从允许的来源核实——计数为 TODO(reference)。
- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）。

## Related Works

- [AHA](./aha.md) — 同样是机器人操作失败推理，借程序化失败生成实现规模化。
- [RoboFAC](./robofac.md) — 同样是失败分析与纠正，规模达 7.8 万 QA 并配专用模型。
- [TRAJDEBUG](./trajdebug.md) — 同样在 agent 轨迹中定位错误，面向软件 agent。
