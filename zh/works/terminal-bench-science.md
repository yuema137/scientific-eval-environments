# Terminal-Bench Science (2026)

> [English](../../works/terminal-bench-science.md) | **简体中文**

> **首次公开：** 2026-01-25 · **来源：** [官方代码库创建](https://github.com/harbor-framework/terminal-bench-science)

## Overview

Terminal-Bench Science 将 Terminal-Bench 框架扩展到自然科学领域，通过确定性的编程化验证在容器化环境中评估 AI agent 在真实科学计算工作流上的表现。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Release 0.1:** <https://www.tbench.ai/news/terminal-bench-science-0-1>
- **Leaderboard:** <https://www.terminal-bench-science.ai/>
- **Code:** <https://github.com/harbor-framework/terminal-bench-science>
- **Initial call:** <https://www.tbench.ai/news/tb-science-announcement>
- **Opus 5.5 evaluation:** <https://www.anthropic.com/claude-opus-5-5>
- **License:** Apache 2.0

## Summary

研究者通过提案、实现和审阅流程贡献可执行的科学工作流。Agent 在容器中提交分析、模拟、证明、代码或数据产物，由各任务的测试检查。0.1 版已从早期征集阶段进入正式发布，并在解出率之外报告美元与 token 成本。

## Tasks

0.1 版共有 70 个任务，覆盖五大科学分组，包括数据分析、统计推断、模拟、优化、定理证明、图像重建、信号处理、逆问题、传感器校准、模型拟合、分类和科学机器学习。团队从 386 个实现 PR 中选出了这 70 题。

## Domains

五个科学领域：

- **Life Sciences** — Biology、Ecology、Medicine、Neuroscience。
- **Physical Sciences** — Astronomy、Chemistry、Materials Science、Physics。
- **Earth Sciences** — Atmospheric、Environmental、Geosciences、Ocean Sciences。
- **Mathematical Sciences** — Applied Mathematics、Formal Mathematics、Operations Research、Statistics。
- **Engineering Sciences** — Chemical、Civil、Electrical、Mechanical Engineering。

## Evaluation

- 在容器内执行，以各任务的程序化验证检查产物，包括 pytest 测试。
- 领域审阅检查科学有效性，技术审阅检查任务构建与验证方式，最后由 bar raiser 把关。
- 0.1 首发评测对全部 70 题各运行三次。Opus 5 搭配 Claude Code 的解出率为 30.0%，GPT-5.6 Sol 搭配 Codex 为 22.4%；同时报告成本及 token 与解出率的 Pareto 比较。
- Anthropic 9 月 22 日发布的 Opus 5.5 结果为 max effort 下 58.7%，其重跑的 Opus 5 基线为 29.0%。同表引用 OpenAI 报告的 GPT-6 Astra 64.6%，因此 Opus 5.5 并非该比较中最高。各模型标准误为 3.5–5 个百分点。
- 厂商设置允许在生物学或前沿模型开发任务触发生产防护时由旧模型接替。需与首发榜单的 30.0% 基线及三次试验协议分别记录。

## Typical Duration

按公告，每任务从数分钟到数小时不等，取决于工作流复杂度。

## Main Contribution

一个由科学家驱动、把 Terminal-Bench 扩展到自然科学计算工作流的 benchmark；配套容器化确定性验证和明确的贡献 / 评审协议。

## Key Design Ideas

- 研究者提供实际工作流和可检查的产物。
- 收录前经过科学、技术和最终质量审阅。
- 任务版本化，便于复用、重新判分或重跑试验。
- 后续版本可增加工作流，也可移除已饱和或定义不足的任务。

## Strengths

- 科学家直接参与，生态效度强。
- 基于 pytest 的确定性评分避免了 LLM-judge 波动。
- 跨领域科学覆盖在同一执行框架内。

## Limitations

- Repository note: 70 题是五大分组的总数，不能用作本仓库每个细分领域的任务数。
- Repository note: 首发成绩和后续厂商评测的设置不同，必须保留来源与版本标签。
- 项目将 0.1 定位为持续更新评测的首个版本，任务分布并非永久固定。

## Related Works

- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Terminal-Bench 的姊妹扩展，聚焦长 horizon 而非科学工作流。
- [NatureBench](./naturebench.md) — 同样面向科学任务，但以 Nature-family 论文的 SOTA 为锚点，而非可执行工作流。
