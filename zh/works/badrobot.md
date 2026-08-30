# BadRobot (2024)

> [English](../../works/badrobot.md) | **简体中文**

> **首次公开：** 2024-07-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2407.20242)

## Overview

BadRobot 在物理世界越狱具身 LLM agent：一套利用 LLM-机器人栈三类弱点的攻击范式，配 277 条恶意物理动作查询（六个危害类别）的 benchmark，针对 Code as Policies、ProgPrompt、VoxPoser 等框架——平均操纵成功率 68.57%，并在真实 UR3e 与 myCobot 机器人上演示。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Activities

N/A — 评估的是 agent 的元属性（成本、安全性或鲁棒性），而非科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2407.20242>
- **Code:** <https://github.com/Rookie143/BadRobot>
- **Project:** <https://Embodied-LLMs-Safety.github.io>
- **Venue:** ICLR 2025

## Summary

对话侧的越狱研究问的是模型会不会说出有害内容，BadRobot 问的是它会不会做出有害动作。该攻击范式针对接收语音或文本查询、产出可执行动作计划或代码的具身 LLM/VLM 框架，使用一套 277 条恶意查询的 benchmark，覆盖物理伤害、隐私侵犯、色情、欺诈、非法活动与仇恨言论（正文）。在包括 GPT-4 级与开源 VLM 在内的目标上，该方法平均操纵成功率达 68.57%，并在物理 UR3e 与 myCobot 280-Pi 平台上闭环——由此确立：语言层面的安全训练无法可靠地存续到动作层面。

## Tasks

对抗回合：向具身 LLM 框架发出恶意查询（277 条、六类），其生成的动作在数字环境、模拟器与真实机械臂上执行。

## Domains

机器人学——针对 LLM 驱动机器人控制的攻击，在真实 UR3e 与 myCobot 平台上执行物理动作。

## Evaluation

- 在查询 benchmark 上的操纵成功率（MSR）与危害性评分。
- **报告。** 平均 MSR 68.57%（正文）；摘要无数值。

## Typical Duration

每次攻击尝试一段「查询到动作」回合。

## Main Contribution

把越狱评估跨过「说/做」的边界：用被执行的机器人动作证明，具身部署制造了语言层对齐覆盖不到的攻击面。

## Key Design Ideas

- 三类弱点把攻击空间结构化，而非临时拼凑提示。
- 277 条查询覆盖各危害类别，使各框架的拒绝行为可比。
- 真实机器人演示堵住了「它其实永远不会执行」的反驳。

## Strengths

- 发表信息经核实（arXiv 上含 ICLR 2025 与 Journal-ref），并有物理验证。
- 框架级的攻击范围覆盖从业者真正部署的具身栈。

## Limitations

- Repository note: 该论文的头号贡献是攻击范式；277 条查询 benchmark 是其配对评估集，本卡片覆盖 benchmark 一侧。查询数与 MSR 出自正文而非摘要。
- Repository note: 卡片依据 arXiv 摘要、正文与官方页面编写（2026 年 8 月）。

## Related Works

- [SafeAgentBench](./safeagentbench.md) — 同样是具身 LLM 安全，从防御方一侧考危险任务的拒绝。
- [ASIMOV](./asimov.md) — 同样是机器人安全评估，处于宪法式判断而非攻击层面。
- [EmbodiedBench](./embodiedbench.md) — 同样评估被 BadRobot 攻击的那些具身 LLM 栈。
