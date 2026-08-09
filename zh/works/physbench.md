# PhysBench (2025)

> [English](../../works/physbench.md) | **简体中文**

## Overview

PhysBench 评测视觉-语言模型的物理世界理解：10,002 条视频-图像-文本交错数据，覆盖四个领域——物体物理属性、物体关系、场景理解与基于物理的动力学——分 19 个子类、8 个能力维度，在 75 个 VLM 上评估，并配套 PhysAgent 增强框架。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Activities

N/A — 能力探针，agent 本身并不执行科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2501.16411>
- **Code:** <https://github.com/USC-GVL/PhysBench>
- **Project:** <https://physbench.github.io/>
- **Dataset:** <https://huggingface.co/datasets/USC-GVL/PhysBench>
- **Venue:** ICLR 2025

## Summary

出于具身 AI 对物理常识的依赖，PhysBench 衡量 VLM 是否理解它将要在其中行动的物理世界。在 75 个代表性 VLM 上，结论一致：模型长于常识推理，却在物理理解上举步维艰——论文认为这多半源于训练数据缺乏物理知识、以及没有内嵌的物理先验。配套的 PhysAgent 框架把 VLM 的通用性与视觉专用模型的专长结合，将 GPT-4o 的物理理解提升 18.4%，论文并演示了更好的物理理解有助于 MOKA 等具身 agent。

## Tasks

对 10,002 条交错视频-图像-文本数据（四个物理领域，19 个子类、8 个能力维度）的静态选择题 QA；公开排行榜与 EvalAI 挑战承接提交。

## Domains

机器人学——作为具身与机器人 agent 感知底座的物理世界理解，并演示了向 MOKA 具身 agent 的迁移；benchmark 本身是静态 VQA，而非机器人控制。

## Evaluation

- 跨领域与能力维度的选择题准确率；基于排行榜的比较。
- **报告。** 75 个 VLM 尽管常识推理强，物理理解却薄弱；PhysAgent 把 GPT-4o 提升 18.4%；增强的物理理解有助于 MOKA 具身 agent。

## Typical Duration

按题的静态查询；benchmark 本身无回合式交互。

## Main Contribution

在大规模上把物理理解与一般常识分开——并把前者（而非后者）定位为具身部署底下的薄弱层。

## Key Design Ideas

- 四领域分类法从属性贯通到动力学，而非只看静态属性。
- 交错的视频-图像-文本条目让动力学问题真的能展示运动。
- PhysAgent 的配对表明这一缺口可用专用视觉专长来弥补。

## Strengths

- 发表信息经核实，模型覆盖异常广（75 个 VLM），并有持续维护的排行榜。
- 具身迁移演示把这个静态 benchmark 连到 agent 结果。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；流传有「oral」之说，但 arXiv Comments 仅可核实「ICLR 2025」。条目中真实与模拟的构成在已核实来源中未载明。

## Related Works

- [PAC Bench](./pac-bench.md) — 同样是 VLM 的物理概念评估，专于操作前提。
- [EmbodiedEval](./embodiedeval.md) — 同样考 MLLM 的具身能力，以交互而非「理解」来测量。
- [RoboSpatial](./robospatial.md) — 同样是感知层 benchmark，且有已演示的下游机器人效应。
