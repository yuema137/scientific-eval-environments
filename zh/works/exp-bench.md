# EXP-Bench (2025)

> [English](../../works/exp-bench.md) | **简体中文**

> **首次公开：** 2025-05-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.24785)

## Overview

EXP-Bench 是一个 benchmark，评估 AI agent 能否完成源自有影响力 AI 论文的完整研究实验：提出假设、设计并实现实验流程、执行实验并分析结果。它通过一条半自主（semi-autonomous）抽取流水线，从 51 篇 NeurIPS 2024 与 ICLR 2024 论文中整理出 461 个任务。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.24785>
- **Code:** <https://github.com/Just-Curieous/Curie/tree/main/benchmark/exp_bench>

## Summary

EXP-Bench 针对的局限是：尽管自动化 AI 研究前景可观，当前 AI agent 仍难以应对严谨的端到端实验的复杂性。给定研究问题与不完整的起始代码，agent 需要提出假设、设计并实现实验流程、执行实验并分析结果；半自主流水线从研究论文及其配套开源代码中抽取并结构化这些任务。OpenHands、IterativeAgent 等领先 agent 在实验设计或实现正确性等单项维度上得分为 20–35%，但在完整且可执行的实验上仅有 0.5%。

## Tasks

461 个任务来自 51 篇顶级 AI 研究论文——NeurIPS 2024（53%）与 ICLR 2024（47%）——每个任务向 agent 提供研究问题、高层方法描述以及来自论文仓库的不完整起始代码。任务由三阶段流水线整理（基于影响力的筛选、对论文与代码库的多轮抽取、带轻量人工复核的验证），并分解为 12,737 个可独立评分的子任务，覆盖设计、实现与结论。

## Domains

多样的 AI 研究子领域，包括计算机视觉、NLP 与强化学习。

## Evaluation

- **设计正确性（D）。** 由基于 LLM 的 judge 评分，衡量 agent 的实验设计满足 ground-truth 设计标准的比例。
- **实现正确性（I）与执行（E）。** 基于 LLM 的 judge 将 agent 的代码修改与 ground-truth git diff 对比；代码执行验证器在干净的容器化环境中重新运行这些修改，合取指标 I·E 要求两者同时满足。
- **结论正确性（C）。** 基于 LLM 的 judge 检查 agent 的最终结论在概念上是否可靠、完整，并与研究问题的 ground-truth 答案一致。
- **All✓ 与 All·E✓。** All✓ 统计在 D、I、C 上全部正确的任务；All·E✓ 额外要求可执行性；评分前由 monitor 先筛查 agent 日志中的违规行为，如访问原论文、Git 操作或伪造数据。
- **报告结果（Table 1）。** 最高的完整且可执行成功率 All·E✓ 为 0.5%，由 OpenHands 搭配 o3-mini 取得（All✓ 为 1.4%）；OpenHands 搭配 Claude-3.7 Sonnet 在实现正确性上达 35.0%、执行上达 33.2%，但 All·E✓ 仅为 0.4%。

## Typical Duration

每个 agent 每个任务的 wall-clock 时间上限为 40 分钟（作者说明该上限可调整），运行在配有 4 块 Nvidia A40 GPU 的 Ubuntu 24.04 Docker 容器中。未说明每任务的步数或 token 预算。

## Main Contribution

一个包含 461 个真实端到端 AI 研究实验任务的 benchmark，由半自主流水线从有影响力的论文及其开源代码中抽取，用于定位阻碍 AI agent 完成完整研究实验的瓶颈。

## Key Design Ideas

- 半自主整理流水线，从论文及其配套开源代码中抽取并结构化实验细节，含基于影响力的筛选与轻量人工验证。
- 每个任务将研究问题、高层方法描述与不完整起始代码配对；ground-truth 的设计、代码 diff 与结论均源自原论文自身的脚本。
- 将每个任务细粒度分解为可独立评分的子任务（共 12,737 个），覆盖设计、实现与结论，使单项得分与端到端成功相互分离。
- 容器化执行，并由 monitor 完整性检查在评分前筛查 agent 日志中的违规行为。

## Strengths

- 任务植根于真实发表的实验，可执行的 ground truth 源自论文自身代码。
- 按单项维度评分，将设计、实现、执行与结论的失败区分开来，揭示 agent 在何处失效。
- 单项得分（20–35%）与完整可执行成功率（0.5%）之间的巨大差距给出强 headroom 信号。

## Limitations

- Repository note: 设计、实现与结论的评分均依赖基于 LLM 的 judge 对照抽取的 ground truth；只有执行检查是程序化的，因此汇总得分继承了 judge 的可靠性。
- Repository note: 每个任务都是对两个 2024 年会议已发表 AI 实验的复现——开放式实验与非 AI 科学领域不在所评估的范围内。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样从同行评审论文中抽取任务并采用基于执行的评分，但其每个任务面向单个独立的数据分析程序，而非完整的设计 → 实现 → 执行 → 结论实验。
- [AIRS-Bench](./airs-bench.md) — 同样从机器学习论文中取材构建端到端 AI 研究任务，但其不提供 baseline 代码，并按 agent 所构建模型的实测性能评分，而非按对原实验设计与结论的还原度评分。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样是运行在容器化环境中的科学 agent benchmark，但其任务由领域专家按 Propose → Build → Review 流程编写，而非从已发表论文中抽取。