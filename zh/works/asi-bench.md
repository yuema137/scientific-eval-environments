# ASI-Bench (2026)

> [English](../../works/asi-bench.md) | **简体中文**

> **首次公开：** 2026-08-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.17271)

## Overview

ASI-Bench 包含 11 个领域的 60 个项目级科研任务，衡量在逐步撤去人类方法指导的过程中，agent 能把一个研究项目推进到多远。每个任务用四个层级的提示（B1–B4）表述：研究目标、数据和所需产出保持不变，依次去掉方法、去掉流程，最后再加入真实但无关的信息。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.17271>
- **Code:** <https://github.com/apexin-ai/ASI-Bench>
- **Project:** <https://asibench.apexin.ai/>
- **Submission portal:** <https://asibench.apexin.ai/submit>
- **Package:** `pip install asibench`

## Summary

ASI-Bench 认为现有 benchmark 大多考察 AI 能否基于已学知识给出正确答案，或在大量人类指导下完成任务，因此测不到自主的科研执行能力。它给出 11 个科学领域的 60 个项目级科研任务，每个任务在同一研究项目内用四个指导层级重写，从而把方法选择、工作流搭建和抗干扰能力分开测量。benchmark 由 40 多位专家构建，声称投入 31,000+ 人时，来源于 1,300+ 条候选研究想法和 1,100+ 次评审分配。在 18 个 agent–模型组合上，平均分从 B1（完整方法指导）的 50.91 降到 B2（只给方法）的 29.10，再到 B3（agent 自己确定方法）的 26.62；作者据此认为当前系统仍高度依赖人类指导。

## Tasks

60 个项目级科研任务。每个任务在四个层级发布，研究目标、给定数据和所需产出保持不变：

- **B1** — 科学背景、方法、方程和完整流程。
- **B2** — 预期方法和相关约束，不给完整流程；agent 需自行搭建可执行工作流。
- **B3** — 只给目标、数据、约束和所需产出；方法由 agent 决定。
- **B4** — 在 B3 基础上加入真实但非必要的信息，考察抗干扰能力。

整个 benchmark 的完整研究轨迹涉及 2,600+ 次交互轮、2,400+ 个执行步，累计超过 35 小时的 agent 执行。任务取自科学文献（1,300+ 条候选想法），经过多轮专家评审筛选到最终 60 个。

## Domains

论文列出的 11 个科学领域：mathematics、physics、chemistry、biology、astronomy、materials science、earth science、medicine and biostatistics、computer science、robotics、electrical engineering。

## Evaluation

- **指导梯度打分。** 每个任务在 B1–B4 各层级都用同一个 0–100 分制打分；主结果是对 60 个任务和 18 个 agent–模型组合的宏平均：B1 = 50.91，B2 = 29.10，B3 = 26.62。
- **逐任务打分器。** 任务由各自的评估门（gate）和加权打分器判分，对照可复现的逐任务参考产出（每个任务都带一个 ground-truth 生成脚本和一个可选的自定义打分器）。Repository note：论文没有用一句话说明确定性检查与任何模型判分成分之间的划分。
- **参考集与随机种子。** 公开的 `seed31415` 集发布参考产出（在 Hugging Face 上），支持本地打分；官方 `seed42` 集参考不公开，通过提交 Portal 打分。
- **沙箱执行。** 运行在隔离沙箱中；本地运行可用 `none` 或 `linux_ns` 沙箱，官方 `seed42` 提交要求基于 Docker 的 `os` 沙箱。每个任务都经过专家评审、AI 辅助审计、沙箱执行和打分器验证。
- **难度护栏。** 任务被接收的条件是其 B3 和 B4 的平均分都严格低于 40；B1 和 B2 没有上限。这让自主层级保持未饱和。
- **成本只报告，不计分。** token 用量和 wall-clock 时间按指导层级测量并报告，论文指出更高成本不保证更高分数，但计算成本不进入任务指标。

## Typical Duration

整个 benchmark 累计超过 35 小时 agent 执行，完整轨迹有 2,600+ 次交互轮和 2,400+ 个执行步。逐任务的 wall-clock 和 token 数据按指导层级报告，而非单一预算；提交不设固定的逐任务步数或 token 上限。

## Main Contribution

第一个在同一研究项目内逐步撤去人类方法指导（B1–B4）的 benchmark，把"agent 能否自己选方法并仍然完成项目"变成一个可测量的量，覆盖 60 个项目级任务和 11 个领域，配有公开的任务贡献 portal 和针对自主层级的难度护栏。

## Key Design Ideas

- 每个任务四个层级只改变方法指导的多少，因此 B1→B3 的落差把方法选择和工作流搭建从任务本身难度中分离出来。
- 一个干扰层级（B4）在 B3 上加入真实但无关的信息，把"抗干扰"和"方法选择"分开。
- 接收规则强制每个任务的 B3 和 B4 平均分低于 40，防止自主区间饱和。
- 公开 / 私有参考集划分（`seed31415` / `seed42`），官方集用 Portal 打分。
- agent 中立的 harness 适配器（Codex CLI、Claude Code、Kimi Code、CodeWhale、AntiGravity）以及一个通用命令接口。

## Strengths

- 项目内的指导梯度是一个受控操纵：同一任务的 B1 和 B3 只差在是否给出方法，因此分数差可解释。
- 大量的构建和验证投入（40+ 专家、31,000+ 人时、多轮评审、AI 辅助审计、沙箱执行、打分器验证）。
- B3/B4 难度护栏在任务接收时检查，不是事后声称。
- 开放的任务贡献，有成文的提交和验证流程，逐任务 ground-truth 生成可复现。

## Limitations

- Repository note：公开材料没有完整说明每个任务的打分器设计（权重，以及是否有模型判分成分），因此 0–100 分制的跨任务可比性依赖非公开的打分器代码。
- Repository note：主结果是 18 个 agent–模型组合的宏平均；本处查阅的摘要级材料没有汇总逐领域和逐任务的难度分布。
- Repository note：`medicine and biostatistics` 在论文的列表里是一个合并领域，因此 11 个领域的计数不是对本仓库标准领域的干净划分。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样从文献中提取经专家验证、以执行判分的科学任务，但把单个分析子任务作为独立程序评分，而非在不同指导层级下提出完整研究项目。
- [AstaBench](./astabench.md) — 同样是带公开榜单的多领域科研任务套件，但围绕跨文献、代码、数据分析和端到端发现的成本受控打分组织，而非项目内的指导梯度。
- [AIRS-Bench](./airs-bench.md) — 同样通过不给基线代码迫使 agent 从零搭建工作流，但只在一个指导层级、20 个任务上，而非四个层级、60 个任务。
- [PaperBench](./paperbench.md) — 同样衡量自主的端到端研究，但作为对某一目标论文的复现来打分，而非开放方法地完成一个研究目标。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样是 agent 中立、容器内执行的多领域科学 benchmark，但由领域专家编写的终端任务加确定性 pytest 检查构成，没有指导层级操纵。
