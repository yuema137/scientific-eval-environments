# NATURAL PLAN (2024)

> [English](../../works/natural-plan.md) | **简体中文**

> **首次公开：** 2024-06-06 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2406.04520)

## Overview

NATURAL PLAN 是一套包含 3,600 个实例的自然语言规划 benchmark，覆盖旅行安排、会面规划与日程协调；评估时，模型所需的工具信息会全部随 prompt 提供。

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — 通用旅行、会面和日程规划，未直接评估科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2406.04520>
- **Code:** <https://github.com/google-deepmind/natural-plan>
- **Venue:** arXiv preprint (2024)

## Summary

NATURAL PLAN 将 Google Flights、Google Maps 和 Google Calendar 的输出直接放入上下文，从而把规划能力与工具操作能力分开。三类任务通过城市数量、参与者、已有日程和约束数量控制难度，并用真实工具数据支撑合成实例。在 five-shot 评估中，GPT-4 的 Trip Planning exact match 为 31.1%，Gemini 1.5 Pro 为 34.8%；城市数达到十个时，所有参评模型都低于 5%。

## Tasks

共 3,600 个测试实例：Trip Planning 1,600 个、Meeting Planning 1,000 个、Calendar Scheduling 1,000 个。旅行题抽取 3–10 个欧洲城市，并加入停留天数、指定日期和直飞连通性约束；会面题要求在参与者空闲时段和驾车时间限制下尽量见到更多人；日程题要求在多人已有安排中找出唯一的 30 或 60 分钟会议时段。

## Domains

面向消费者的旅行、会面和日程规划。数据具有现实地理与日程基础，但不对应规范化科学或工程 domain。

## Evaluation

模型输出会被解析为 benchmark 的结构化格式，再与标准计划做 exact match。实验还改变约束复杂度，并测试从简单示例泛化到困难题、反向泛化、提示式自我纠错，以及最多使用 800 个示例的长上下文规划。

## Typical Duration

主实验中，每题在五个上下文示例后生成一次回答，不执行工具调用。难度依任务类型随 3–10 个城市、2–7 位参与者或 1–5 个工作日上升。

## Main Contribution

在固定信息获取条件下评估现实自然语言规划，使结果不再混入工具选择和执行能力。

## Key Design Ideas

- 直接提供工具产出的事实，不要求实时调用工具。
- 用城市、人员和天数等承载约束的实体数量控制难度。
- 以航班连通性、路程时间和日历安排支撑合成问题。
- 通过消融实验检验自我纠错、示例难度和更多上下文是否改善规划。

## Strengths

- 去掉工具执行后，规划失败的解释更清晰。
- 三类任务在同一协议下覆盖路径、排程与约束满足。
- exact match 是确定性评分，生成器也便于系统扫描复杂度。

## Limitations

- exact match 可能拒绝与唯一标准表示不同、但同样有效的计划。
- 全量提供信息，移除了部署环境中关键的检索与适应过程。
- benchmark 测量一次性生成计划，而非根据反馈在线重规划。

## Related Works

- [PlanBench](./planbench.md) — 同样隔离规划，但使用形式化动作模型和 plan validator。
- [TravelPlanner](./travelplanner.md) — 要求 agent 在封闭旅行环境中通过工具检索信息并制定计划。
- [Agent Planning Benchmark](./agent-planning-benchmark.md) — 分开测量完整计划生成与基于反馈的下一步规划。
