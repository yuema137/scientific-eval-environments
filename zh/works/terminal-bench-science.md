# Terminal-Bench Science (2026)

> [English](../../works/terminal-bench-science.md) | **简体中文**

## Overview

Terminal-Bench Science 将 Terminal-Bench 框架扩展到自然科学领域，通过确定性的编程化验证在容器化环境中评估 AI agent 在真实科学计算工作流上的表现。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Project:** <https://www.tbench.ai/news/tb-science-announcement>
- **Code:** <https://github.com/harbor-framework/terminal-bench-science>
- **Task Dashboard:** <https://stevendillmann.github.io/tb-science-task-dashboard/>
- **License:** Apache 2.0

## Summary

Terminal-Bench Science 是一个由科学家驱动的 benchmark，用来评估 AI agent 在自然科学研究中真实计算工作流上的表现。任务在容器化环境中执行，通过 pytest 进行确定性验证。项目由 Stanford University 与 Laude Institute 共同维护，采用结构化的 Propose → Build → Review 贡献模型。

## Tasks

当前 5 个科学领域下共 8 个任务，目标为 100+ 任务。首轮任务贡献的 PR 截止日期为 2026-08-17。

## Domains

五个科学领域：

- **Life Sciences** — Biology、Ecology、Medicine、Neuroscience。
- **Physical Sciences** — Astronomy、Chemistry、Materials Science、Physics。
- **Earth Sciences** — Atmospheric、Environmental、Geosciences、Ocean Sciences。
- **Mathematical Sciences** — Applied Mathematics、Formal Mathematics、Operations Research、Statistics。
- **Engineering Sciences** — Chemical、Civil、Electrical、Mechanical Engineering。

## Evaluation

- 容器化执行环境。
- 基于 pytest 的确定性验证。
- 官方目标：发布时 10–20% 的 solve rate（有意设计为困难）。
- 任务验证需三方批准（领域评审、通用评审、bar-raiser）+ CI 检查。

## Typical Duration

按公告，每任务从数分钟到数小时不等，取决于工作流复杂度。

## Main Contribution

一个由科学家驱动、把 Terminal-Bench 扩展到自然科学计算工作流的 benchmark；配套容器化确定性验证和明确的贡献 / 评审协议。

## Key Design Ideas

- 领域专家编写的任务，配以结构化的 Propose → Build → Review 协议。
- 容器内基于 pytest 的编程化验证。
- 显式的难度目标（10–20% solve rate）作为发布门槛。
- 在共享执行框架下的跨学科广度。

## Strengths

- 科学家直接参与，生态效度强。
- 基于 pytest 的确定性评分避免了 LLM-judge 波动。
- 跨领域科学覆盖在同一执行框架内。

## Limitations

- Repository note: 当前发布仅 8 个任务——100+ 是目标而非现状；当前结果建立在小任务集上。
- Repository note: 引用来源是项目公告与 GitHub 仓库——尚无同行评审论文与此发布相配套。

## Related Works

- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Terminal-Bench 的姊妹扩展，聚焦长 horizon 而非科学工作流。
- [NatureBench](./naturebench.md) — 同样面向科学任务，但以 Nature-family 论文的 SOTA 为锚点，而非可执行工作流。
