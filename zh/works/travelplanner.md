# TravelPlanner (2024)

> [English](../../works/travelplanner.md) | **简体中文**

## Overview

TravelPlanner 是现实旅行规划 benchmark，包含 1,225 条精心设计的旅行意图、近四百万条记录组成的封闭 sandbox，以及用于在环境、常识和用户约束下制定多日行程的工具。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — 通用旅行规划，未直接评估科学或研究活动。

## Links

- **Paper:** <https://proceedings.mlr.press/v235/xie24j.html>
- **Code:** <https://github.com/OSU-NLP-Group/TravelPlanner>
- **Venue:** ICML 2024

## Summary

TravelPlanner 要求语言 agent 在静态 sandbox 中检索航班、驾车路线、餐厅、景点和住宿信息，保留有用结果，并交付可行的三日、五日或七日行程。它同时检查交通不可用等环境约束、八类常识要求，以及预算、房间、菜系和交通偏好等明确用户约束。论文测试中，采用 ReAct 的 GPT-4 最终完全通过率仅为 0.6%，远低于其交付出答案的比例。

## Tasks

1,225 条意图按行程天数和约束数量分成九组：45 条带人工标注计划的训练题、180 条验证题和 1,000 条测试题。三日题覆盖一座城市，五日题覆盖两座，七日题覆盖三座。工具数据库含 3,827,361 条航班记录，以及城市、距离、餐厅、景点和住宿数据。

## Domains

封闭消费服务环境中的旅行规划。它是现实应用环境，但不属于规范化科学或工程 domain。

## Evaluation

确定性脚本分别计算 Delivery Rate、八项 Commonsense Constraint Pass Rate、Hard Constraint Pass Rate，以及要求所有适用检查同时通过的 Final Pass Rate。搜索失败时环境会返回反馈，因此成功既依赖信息收集，也依赖对不可用选项的调整。实验最多允许 30 步。

## Typical Duration

最多 30 步的交互式 trajectory，最终产出三日、五日或七日行程。

## Main Contribution

一套工具化、以执行环境为依据的 benchmark，用于检验语言 agent 能否在可复现的封闭 sandbox 中满足多类约束并拼出完整的现实计划。

## Key Design Ideas

- 冻结大型多源数据库，使所有 agent 面对相同信息。
- 区分环境约束、常识约束和明确的用户约束。
- 通过天数、城市数、同行人数和硬约束数量改变 horizon 与难度。
- 用程序检查约束满足情况，不依赖表面相似度或 LLM judge。

## Strengths

- 工具检索和环境反馈能暴露静态 prompt 规划测试看不到的失败。
- Final Pass 要求多类约束同时成立。
- 封闭 sandbox 在保留现实记录和接口的同时提高了可复现性。

## Limitations

- 环境静态且仅限旅行，无法覆盖开放世界变化和其他规划领域。
- Final Pass 严格而稀疏，需要结合分项指标才能区分检索、完整性与约束失败。
- 计划只在编码规则下检查可行性，没有通过真实预订或旅客结果验证。

## Related Works

- [NATURAL PLAN](./natural-plan.md) — 把旅行和日程信息直接放进上下文，不执行工具。
- [PlanBench](./planbench.md) — 用 solver 支撑的形式化规划领域与有效性检查。
- [Agent Planning Benchmark](./agent-planning-benchmark.md) — 在更广泛的工具与多模态设置中把规划诊断和执行分开。
