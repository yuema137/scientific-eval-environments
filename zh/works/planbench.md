# PlanBench (2023)

> [English](../../works/planbench.md) | **简体中文**

## Overview

PlanBench 是一套可扩展的规划 benchmark，用于检验大语言模型能否在形式化规划领域中生成并验证计划、推断状态变化、应对突发事件重新规划，以及分辨有效与无效的动作序列。

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — 通用规划与推理 benchmark，未直接评估科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2206.10498>
- **Code:** <https://github.com/karthikv792/LLMs-Planning>
- **Venue:** NeurIPS 2023 Datasets and Benchmarks Track

## Summary

PlanBench 把经典规划问题转成自然语言，同时保留明确的动作模型、初始状态、目标与可机器验证的语义。它旨在区分真正的规划与对熟悉常识模式的检索：首版包含 Blocksworld 和 Logistics，也提供用误导词或随机字符串替换名称的混淆版本，并借助 planner 和 plan validator 生成参考信息、核验模型输出。论文报告 GPT-4 在 600 道 Blocksworld 计划生成题上通过 34.3%，在对应的成本最优规划题上通过 33.0%。

## Tasks

约 26,250 条 prompt，覆盖八类测试以及原始或混淆后的规划领域：计划生成、成本最优规划、计划验证、动作序列后的状态推断、状态突变后的重新规划、计划泛化、计划复用和部分目标条件下的推理。首版源问题包括 600 个主要 Blocksworld 实例、另设的 500 个 Blocksworld 泛化实例，以及 285 个 Logistics 实例。

## Domains

Blocksworld 与 Logistics 中的形式化经典规划。这些是受控的 AI 规划环境，不是科学或工程应用领域，因此不映射到规范化 domain 页。

## Evaluation

系统把模型生成的动作序列解析回形式化计划，再交给领域无关的 plan validator 检查可执行性和目标是否达成。成本最优规划还会将生成计划的成本与最优成本对比；其他辅助任务则根据形式化状态转移或有效性进行判定。

## Typical Duration

每题是带 few-shot 示例的单次规划回答。难度随对象数量和最优计划长度变化；论文未规定墙钟时间或 token 预算。

## Main Contribution

一套可扩展、可自动验证的评估框架，把形式化规划领域引入自然语言 LLM 评估，并通过名称混淆检验表面上的规划能力是否依赖熟悉词汇与世界知识。

## Key Design Ideas

- 将领域无关的生成、验证机制与领域特有的模型、问题生成器和自然语言转换器分开。
- 明确给出动作的前置条件与效果，使答案可按形式化转移语义验证。
- 分别评估规划及相关推理能力，不压成一个总成功率。
- 在底层问题不变的前提下，用误导词或随机字符串替换谓词和动作名。

## Strengths

- 确定性的计划验证不依赖 LLM judge。
- 形式化领域便于控制问题规模、计划长度、动作成本和突发事件。
- 混淆版本直接测量模型对词汇熟悉度的敏感性。

## Limitations

- 首版集中在两个经典规划领域，不含感知、实时工具或不确定的环境动态。
- 形式化环境中的有效性和最优性定义清晰，但不足以覆盖现实规划中的歧义与多目标权衡。
- 论文实验主要围绕 Blocksworld，并未同等完整地覆盖每种领域与测试组合。

## Related Works

- [NATURAL PLAN](./natural-plan.md) — 同样隔离规划，但以现实自然语言约束替代形式化动作语言。
- [TravelPlanner](./travelplanner.md) — 在工具检索和多类现实约束下评估可执行的旅行计划。
- [Agent Planning Benchmark](./agent-planning-benchmark.md) — 将诊断扩展到多模态 agent、基于反馈的下一步、坏工具、干扰工具和不可解任务。
