# LabRobFail (2026)

> [English](../../works/labrobfail.md) | **简体中文**

## Overview

LabRobFail 评测化学自主实验室中的机器人失败分析：20,000+ 条轨迹、70+ 个任务场景，失败在控制、物理、语义三个层级被注入（五个类别、11 种细粒度类型），评估从失败检测到可执行纠正的六项能力——配套的领域专用 VLM 达到 90.83% 检测准确率，作为实时监督者把下游任务成功率抬高 4–16 个百分点。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 能力探针，agent 本身并不执行科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.23704>
- **Code:** <https://github.com/Su-ISE-2001/SciRobo>
- **Venue:** arXiv preprint (cs.RO), 2026（Comments 载明在审）

## Summary

自主实验室的失败方式与家用机器人不同——一次夹错的样品瓶或一次错时的转移会悄无声息地毁掉一次实验。LabRobFail 为这一场景搭起失败中心的评估栈：LabRobFail-Sim 在 Isaac Sim 的实验室机器人执行中于三个层级注入异常，LabRobFail-Data 汇聚 20,000+ 条覆盖 70+ 场景的轨迹，LabRobFail-Bench 评估六项能力——任务理解、失败检测、时间定位、严重度评估、失败分类与可执行纠正。领域专用模型 LabRobFail-VLM 达到 90.83% 的失败检测与 77.21% 的时间定位准确率，明显优于通用 VLM，作为实时监督者接入后把下游任务成功率提高 4–16 个百分点。

## Tasks

对 20,000+ 条模拟实验室机器人轨迹（70+ 场景；5 个失败类别、11 种类型，在控制/物理/语义层级注入）的失败分析；benchmark 侧为静态诊断，另有下游实时监督。仅模拟（Isaac Sim）。

## Domains

机器人学——实验室机器人操作的失败分析：在模拟化学自主实验室执行中注入控制级、物理级与语义级异常，并把 VLM 部署为闭环监督者。

## Evaluation

- 六项能力分数：任务理解、失败检测、时间定位、严重度评估、失败分类、可执行纠正。
- **报告。** LabRobFail-VLM：失败检测准确率 90.83%、时间定位准确率 77.21%；作为监督者使下游任务成功率提升 4–16 个百分点。

## Typical Duration

按轨迹的诊断；监督模式则在实验室任务执行期间持续运行。

## Main Contribution

把失败中心的评估带进实验室机器人学——在这里未检出的失败毁掉的是科学而不只是任务——并用一套三层注入分类法，把控制故障、物理事故与语义错误分开。

## Key Design Ideas

- 在控制、物理、语义三层注入，使失败来源成为真值的一部分。
- 时间定位与严重度评估越过「检测」走向「分诊」。
- 监督者集成把 benchmark 分数转化为被挽回的实验。

## Strengths

- 本处所录工作中首个专攻自主实验室的失败分析 benchmark。
- 能力分解给出六项可分别落地的分数，而非单一检测率。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；据 arXiv Comments 论文在审，且 benchmark 仅模拟——这些来源无法核实任何物理实验室部署。

## Related Works

- [RoboFAC](./robofac.md) — 同样用专用模型做失败分析与纠正，面向通用操作。
- [AHA](./aha.md) — 同样以程序化失败注入来制造训练与评估数据。
- [EnvTrace](./envtrace.md) — 同样以执行行为评估实验室仪器控制，在数字孪生上做轨迹对齐。
