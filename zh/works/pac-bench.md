# PAC Bench (2025)

> [English](../../works/pac-bench.md) | **简体中文**

> **首次公开：** 2025-06-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2506.23725)

## Overview

PAC Bench 追问基础模型是否理解执行操作策略的前提——物体的属性（Properties）、affordance 与约束（Constraints）：30,000+ 条标注，覆盖 673 张真实图像（115 个物体类别）、100 个真实人形机器人第一视角场景与四类任务下的 120 个模拟约束场景。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Activities

N/A — 能力探针，agent 本身并不执行科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2506.23725>
- **Project:** <https://pacbench.github.io/>
- **Dataset:** <https://huggingface.co/datasets/Pacbench/pacbench>
- **Venue:** arXiv preprint (cs.RO), 2025

## Summary

机器人规划一次操作之前，总得有东西知道玻璃杯易碎、把手可拉、悬垂物挡住抓取。PAC Bench 从「任务可执行性」角度评估的正是这个前提层：VLM 在真实图像（含 Unitree G1 人形机器人视角拍摄）与模拟约束场景上回答属性、affordance 与约束问题。评估暴露出当前 VLM 对基本物理概念理解的显著缺口——在「识别全部正确 affordance」上，多数模型的表现掉到接近零（项目页）。

## Tasks

对 30,000+ 条标注的静态选择题/理解式评估：673 张真实图像（115 个物体类别、15 种属性、每类 1–3 个 affordance）、100 个真实人形机器人第一视角场景、四类任务下的 120 个模拟约束场景。无机器人执行。

## Domains

机器人学——在真实机器人视角（Unitree G1）与桌面图像上评估的操作前提理解，以「服务于操作策略的可执行性」为框架。

## Evaluation

- 约 8–10 个前沿与开源 VLM 上按类别（属性/affordance/约束）的准确率（项目页）。
- **报告。** 基本物理概念存在显著缺口；「识别全部 affordance」在各模型上接近零（例外为 11–20%，项目页）。

## Typical Duration

按题的静态查询；无回合式交互。

## Main Contribution

评测操作策略底下的前提层——表明被当作机器人大脑的模型，尚不能可靠地列举物体是什么、允许什么、禁止什么。

## Key Design Ideas

- P/A/C 分解对应规划器行动前隐式跑的那份清单。
- 人形机器人视角拍摄从部署视角而非精选网络角度考察感知。
- 「全部 affordance」判据惩罚了单答案准确率掩盖的片面知识。

## Strengths

- 干净地剥离出端到端操作分数无法归因的一个失败层。
- 混合的真实/模拟构造，以真实一侧为主。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目页编写（2026 年 8 月）；这些来源无法核实任何发表信息（项目页表明工作在审）。

## Related Works

- [RoboSpatial](./robospatial.md) — 同样是面向机器人的 VLM 评估，考空间理解并有真实机器人验证。
- [ManipBench](./manipbench.md) — 同样探测 VLM 的操作推理，处于动作决策层面。
- [PhysBench](./physbench.md) — 同样是 VLM 的物理理解评估，世界范围更广。
