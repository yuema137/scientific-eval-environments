# Robotouille (2025)

> [English](../../works/robotouille.md) | **简体中文**

## Overview

Robotouille 是面向 LLM agent 的异步规划 benchmark：长程烹饪任务要求同时照管相互重叠的动作并应对打断——ReAct（GPT-4o）在同步任务上做到 47%，在异步任务上只剩 11%。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2502.05227>
- **Code:** <https://github.com/portal-cornell/robotouille>
- **Project:** <https://portal-cornell.github.io/robotouille/>
- **Venue:** ICLR 2025（据官方仓库与 OpenReview；arXiv 元数据未载明发表信息）

## Summary

多数规划 benchmark 允许 agent 一次只做一件事，Robotouille 的烹饪环境不允许：做菜要求启动耗时的动作（煎、煮），趁其进行去干别的活，还要应对打断。Benchmark 提供 30 个长程场景，覆盖同步、异步与多 agent 三种设定，每个场景配 10 个任务、各 10 个程序化生成的实例（官方仓库）。从同步到异步的成绩骤降——ReAct（GPT-4o）从 47% 跌到 11%——把「处理时间重叠」剥离成一项独立且未解决的能力；论文将失败归因于长程反馈利用不足与缺少对自身推理的自查。

## Tasks

30 个长程规划场景（同步、异步、多 agent），每个场景为 10 任务 × 10 程序化实例的数据集；LLM agent 在烹饪模拟器中规划并行动。仅模拟。

## Domains

模拟烹饪环境——不在本仓库的科学/工程领域轴之内；因其评估方法学而收录。

## Evaluation

- 按设定（同步/异步/多 agent）计任务成功率，附失败模式分析。
- **报告。** ReAct（GPT-4o）：同步 47% vs 异步 11%；较小的模型在异步任务上接近零。

## Typical Duration

含并发、时间上重叠动作的长程回合。

## Main Contribution

把异步性剥离为被测变量：同一套规划机制，动作一旦在时间上重叠，成功率便折损四分之三。

## Key Design Ideas

- 带完成延迟的长时动作让「时间管理」而不只是「排序」成为难点。
- 程序化实例生成给每个场景以统计深度。
- 同步/异步任务集相互匹配，把比较变成受控实验。

## Strengths

- 迄今对 LLM agent 异步规划短板最干净的公开剥离。
- 材料全公开，程序化生成天然抗污染。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；ICLR 2025 由仓库与 OpenReview 声明，arXiv 元数据未载明；场景数量出自仓库。
- 仅模拟；「机器人」是抽象的——无物理平台。

## Related Works

- [Gaia2](./gaia2.md) — 同样向 agent 评估注入时间事件与异步性，在移动环境设定中。
- [LoTa-Bench](./lota-bench.md) — 同样是执行判分的 LLM 规划评估，处于同步一侧。
- [PARTNR](./partnr.md) — 同样考并发下的协调，对象是人类搭档而非并行动作。
