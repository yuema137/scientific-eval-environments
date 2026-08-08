# Robo2VLM (2025)

> [English](../../works/robo2vlm.md) | **简体中文**

## Overview

Robo2VLM 从大规模真实场景机器人操作数据生成视觉问答：Robo2VLM-1 含 684,710 个选择题，覆盖 463 个场景、3,396 个操作任务，取自 176K 条真实遥操作机器人轨迹——其传感器流（末端执行器位姿、夹爪开合、力觉）提供真值。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Links

- **Paper:** <https://arxiv.org/abs/2505.15517>
- **Dataset:** <https://huggingface.co/datasets/keplerccc/Robo2VLM-1>
- **Venue:** arXiv preprint (cs.RO), 2025

## Summary

多数 VQA 的真值来自看着图片的人类标注者，Robo2VLM 的真值来自物理。该框架把真实遥操作轨迹切分为操作阶段，从本体感知与力觉中提取机器人、任务目标与目标物体的 3D 属性，并实例化空间、目标条件与交互推理三类问题模板，其答案由传感器记录而非主观意见认定。由此考察 VLM 能否从机器人图像中读出接触、意图与几何——并且既能评测也能微调。

## Tasks

静态选择题 VQA：取自 176K 条真实机器人轨迹的 684,710 个问题，覆盖 463 个场景、3,396 个操作任务；空间、目标条件与交互推理模板。评估中无机器人执行。

## Domains

机器人学——以真实遥操作机器人轨迹为依据的操作场景推理，真值由传感器（位姿、夹爪、力）导出。

## Evaluation

- 按模板族的选择题准确率；轨迹传感器导出的答案无需人工标注或 LLM judge。
- **报告。** Robo2VLM-1 可评测并改进 VLM 的空间与交互推理能力；各模型数字为 TODO(reference)——摘要未载明。

## Typical Duration

按题的静态查询；无回合式交互。

## Main Contribution

由传感器判定真值的 VQA 生成：把机器人自身的本体感知与力觉记录，变成可规模化、客观的操作场景理解真值。

## Key Design Ideas

- 来自传感的真值从源头消除标注者分歧。
- 阶段切分把问题定位在语义上有意义的轨迹时刻。
- 生成框架的规模随机器人车队数据增长——遥操作越多，benchmark 越大。

## Strengths

- 源自真正的真实场景数据，是最大的机器人依据 VQA 资源之一。
- 兼作评测与微调，数据集（107 GB）公开发布。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方数据集页编写（2026 年 8 月）；这些来源无法核实任何发表信息与代码仓库，各模型结果有待全文校验。

## Related Works

- [RoboSpatial](./robospatial.md) — 同样是真实数据的机器人空间理解，以 3D 扫描为依据。
- [ManipBench](./manipbench.md) — 同样是 VLM 的操作推理选择题，为人工策划而非传感器生成。
- [PhysBench](./physbench.md) — 同样是物理理解 VQA，范围超出操作，达世界尺度。
