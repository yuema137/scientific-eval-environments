# ManipBench (2025)

> [English](../../works/manipbench.md) | **简体中文**

> **首次公开：** 2025-05-14 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.09698)

## Overview

ManipBench 评测视觉-语言模型的底层机器人操作推理——决定精确的机器人动作，含物体间交互与可变形物体操作——覆盖 10 个模型族的 33 个代表性 VLM，其表现与真实世界操作结果强相关。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Activities

N/A — 能力探针，agent 本身并不执行科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2505.09698>
- **Code:** <https://github.com/slurm-lab-usc/ManipBench-Real-Robot-question>
- **Project:** <https://manipbench.github.io>
- **Venue:** CoRL 2025

## Summary

高层规划 benchmark 问「做什么」，ManipBench 问的是「究竟怎么做」——哪个抓取点、哪个方向、怎么叠布。其 12,617 道选择题（项目页）取自真实机器人轨迹（DROID、Bridge）、人工策划的织物操作场景，以及覆盖抓放、关抽屉、绳索操作、清扫与投球的模拟环境。对 10 个族 33 个 VLM 的评测显示：表现随任务显著变化，与真实世界操作趋势强相关，且离人类水平理解仍有明显差距。

## Tasks

探测底层动作决策的静态选择题（项目页 12,617 道），取自真实机器人数据、织物场景与模拟环境；配对的真实世界操作任务建立相关性。

## Domains

机器人学——由真实机器人轨迹构建的底层操作推理，并以与物理操作表现的强相关性加以验证。

## Evaluation

- 按任务族的选择题准确率；与真实世界操作任务表现的相关性分析。
- **报告。** 表现随任务显著变化；与真实世界操作趋势强相关；离人类水平理解仍有明显差距。

## Typical Duration

按题的静态查询；相关联的真实机器人任务是物理回合。

## Main Contribution

经过验证的代理测量：表明一个选择题 benchmark 能与 VLM 的物理操作效用一致地排序模型，从而无需每个实验室都摆一台机器人也能测底层能力。

## Key Design Ideas

- 动作级问题直指 VLA 策略委托给 VLM 先验的那一层。
- 可变形物体与物体间交互覆盖刚体套件跳过的富接触情形。
- 真实世界相关性研究是 benchmark 主张的一部分，而非事后补充。

## Strengths

- 发表信息经核实，是本处所录机器人推理 benchmark 中 VLM 覆盖最广的（33 个模型）。
- 代理有效性的证据抬高了「机器人相关 VQA 应当证明什么」的门槛。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；题量出自项目页而非摘要。

## Related Works

- [PAC Bench](./pac-bench.md) — 同样是与底层操作相关的 VLM 评估，处于前提层面。
- [Robo2VLM](./robo2vlm.md) — 同样是操作场景选择题，由真实轨迹传感生成。
- [RoboSpatial](./robospatial.md) — 同样是机器人视角的 VLM 评估，考空间理解。
