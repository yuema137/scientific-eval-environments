# RoboSpatial (2024)

> [English](../../works/robospatial.md) | **简体中文**

## Overview

RoboSpatial 为面向机器人的视觉-语言模型教授并测试空间理解：真实室内与桌面场景上的 1M 图像、5K 3D 扫描、3M 标注空间关系，兼备 2D 与 3D 就绪形式——在其上训练的模型在空间 affordance 预测、空间关系预测与机器人操作上胜过基线。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Links

- **Paper:** <https://arxiv.org/abs/2411.16537>
- **Code:** <https://github.com/NVlabs/RoboSpatial>
- **Project:** <https://chanh.ee/RoboSpatial>
- **Dataset:** <https://huggingface.co/datasets/chanhee-luke/RoboSpatial-Home>
- **Venue:** CVPR 2025 (Oral)

## Summary

通用 VQA 数据教模型描述场景，机器人却需要从自身视角回答「东西能放哪、什么装得下」。RoboSpatial 用真实 3D 扫描的室内与桌面场景搭起这套训练与评估底座——1M 图像、5K 扫描上的 3M 空间关系——涵盖多参考系下的空间配置、语境与兼容性。微调后的模型在下游空间任务上胜过基线；据官方项目页，一项真实机器人实验显示，RoboSpatial 训练出的指向（pointing）预测把机械臂的抓取成功率提升到 52.6%，而基线为 23.7%。

## Tasks

真实场景上的空间问答（配置、语境、兼容性；2D 与 3D），既作微调数据也作评估集（RoboSpatial-Val、RoboSpatial-Home）；静态 VQA，另有真实机器人操作评估环节（项目页）。

## Domains

机器人学——真实扫描场景上的机器人视角空间理解，通过物理机械臂抓取评估加以验证。

## Evaluation

- 在空间 affordance 预测、空间关系预测与机器人操作上，对照基线 VLM 的下游任务表现。
- **报告。** 训练后的模型在各下游任务上胜过基线；项目页：真实机器人抓取成功率 52.6% vs 23.7%（LLaVA-NeXT + RoboSpatial 对基线）。

## Typical Duration

按查询的空间问题；机器人评估跑「以指向预测为条件」的抓取回合。

## Main Contribution

把机器人视角的空间理解做成可训练、可测量的能力——以真实扫描为依据，并用物理抓取验证把 VQA 分数连到执行结果。

## Key Design Ideas

- 真实 3D 扫描提供渲染场景与网络图像所缺的几何真值。
- 配置/语境/兼容性的类型划分覆盖操作真正会提的空间问题。
- 2D 与 3D 就绪两种格式无需重新标注即可服务两类 VLM。

## Strengths

- 发表信息经核实（CVPR 2025 oral），规模（3M 关系）足以支撑训练而非仅测试。
- 抓取成功率的迁移结果把 benchmark 表现连到物理结果。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；机器人实验数字出自项目页而非摘要。本质上是「训练 + 评估」数据集，而非纯 benchmark。

## Related Works

- [PAC Bench](./pac-bench.md) — 同样是机器人前提的 VLM 评估，考属性、affordance 与约束。
- [ManipBench](./manipbench.md) — 同样是与真实机器人操作结果相关联的 VLM 评估。
- [Robo2VLM](./robo2vlm.md) — 同样以真实机器人为依据的 VQA，由遥操作轨迹生成。
