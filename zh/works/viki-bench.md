# VIKI-Bench (2025)

> [English](../../works/viki-bench.md) | **简体中文**

## Overview

VIKI-Bench 是首个面向具身多 agent 协作的层级化 benchmark，设三个结构化层级——agent 激活、任务规划、轨迹感知——覆盖多样的机器人形态与多视角视觉观测；配套方法 VIKI-R 用链式思维示范微调 VLM，再以多层级奖励做强化学习。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Links

- **Paper:** <https://arxiv.org/abs/2506.09049>
- **Code:** <https://github.com/MARS-EAI/VIKI-R>
- **Project:** <https://faceong.github.io/VIKI-R/>
- **Dataset:** <https://huggingface.co/datasets/henggg/VIKI-R>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

VIKI-Bench 把视觉多机器人协作拆成层级：第一层依据场景图像与任务上下文选择激活哪些机器人，第二层生成多 agent 行动计划，第三层从第一视角视图感知细粒度运动轨迹。据官方项目页，套件在 RoboCasa 与 ManiSkill3 之上构建，含 20,000+ 任务样本、100 个场景、6 种异质机器人（人形、四足、轮式机械臂）。配套的 VIKI-R——链式思维微调加多层级奖励的强化学习——在全部层级上显著超过基线。

## Tasks

三个层级（激活、规划、轨迹感知）上的层级化视觉推理任务，20,000+ 样本、100 个场景、6 种机器人形态（项目页）；按样本做视觉推理查询，而非闭环控制。仅模拟。

## Domains

机器人学——异质多机器人协调：在人形、四足与轮式机械臂平台上（模拟中）做机器人形态选择、多 agent 行动规划与机器人运动感知。

## Evaluation

- 分层指标：规划的分布内/分布外准确率；轨迹感知的 RMSE、Hausdorff 距离与方向性 Fourier 距离（项目页）。
- **报告。** VIKI-R 在所有任务层级上显著超过基线方法（摘要）；具体层级分数见项目页。

## Typical Duration

三个层级上按样本的单次视觉推理查询。

## Main Contribution

把多机器人协作结构化为可测量的层级，让「模型会不会协调机器人」分解为「派谁、什么计划、什么运动」——各自单独计分。

## Key Design Ideas

- 异质形态使「agent 激活」成为真实的能力问题，而非走过场。
- 多视角与第一视角观测把规划绑在感知上，而非抽象状态上。
- 分布外的规划测试集测量的是泛化，而非背下来的场景-任务对。

## Strengths

- 发表信息经核实，benchmark、方法、数据集全公开。
- 层级结构给出端到端协作分数所缺乏的部分得分结构。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；规模数字出自项目页而非摘要。论文标题的贡献是 VIKI-R 方法；本卡片覆盖的是 VIKI-Bench。
- 仅模拟；无物理机器人评估。

## Related Works

- [RoCo / RoCoBench](./rocobench.md) — 同样评估多机器人协作，经机器人间对话并有真实机械臂演示。
- [PARTNR](./partnr.md) — 同样是大规模具身多 agent 评测，带人类协作者。
- [EmbodiedBench](./embodiedbench.md) — 同样是视觉驱动的具身 MLLM 评估，单 agent 设定。
