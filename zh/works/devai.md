# DevAI / Agent-as-a-Judge (2024)

> [English](../../works/devai.md) | **简体中文**

> **首次公开：** 2024-10-14 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2410.10934)

## Overview

DevAI 是含 55 个真实感自动化 AI 开发任务、365 个层级化用户需求的 benchmark，随 Agent-as-a-Judge 一同发布——一种「用 agent 评估 agent」的评估方法，提供逐步反馈，在可靠性上媲美人类评估、并远胜 LLM-as-a-Judge。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.10934>
- **Code:** <https://github.com/metauto-ai/agent-as-a-judge>
- **Dataset:** <https://huggingface.co/DEVAI-benchmark>
- **Venue:** arXiv preprint (cs.AI), 2024

## Summary

论文「Agent-as-a-Judge: Evaluate Agents with Agents」贡献了一种评估方法——用 agent 系统评判 agent 系统，是 LLM-as-a-Judge 的有机延伸，检视整个任务求解过程并给出中间反馈——并以其作为概念验证测试台推出 DevAI：一个含 55 个真实感自动化 AI 开发任务、365 个层级化用户需求与丰富人工标注的可复用 benchmark。在 DevAI 上，Agent-as-a-Judge 显著胜过 LLM-as-a-Judge，且可靠性与人类评估基线相当，把 agent 化评估定位为专家评审 AI 开发 agent 的可扩展替代。

## Tasks

55 个自动化 AI 开发任务（构建 AI/ML 项目），配 365 个层级化需求；agent 系统求解并被逐步评估。交互式 agent 化、长 horizon。

## Domains

AI 与机器学习研究——自动化 AI 开发：agent 对照层级化需求构建 AI/ML 项目。

## Evaluation

- 需求级评估，由 Agent-as-a-Judge 方法提供中间的、过程级反馈；对照 LLM-as-a-Judge 与人类评估基线。
- **报告。** Agent-as-a-Judge 显著胜过 LLM-as-a-Judge，可靠性媲美人类评估基线。

## Typical Duration

每个任务一段长 horizon 的 AI 开发回合，逐步评估。

## Main Contribution

DevAI 提供一个以需求结构化的 AI 开发 agent benchmark，而 Agent-as-a-Judge 表明 agent 化、过程级评估能以远低于 LLM-as-a-Judge 的成本媲美人类可靠性。

## Key Design Ideas

- 365 个层级化需求使判分细粒度化，而非每任务一个通过/失败。
- 过程级（而非仅结果）评估为中间进展计分。
- 单独发布 DevAI，使该 benchmark 可独立于评判方法复用。

## Strengths

- 一个可复用、标注丰富的 AI 开发 benchmark，加一个经验证的 agent 化评判器。
- 代码与 HuggingFace 数据集公开；评判器被证明可靠性媲美人类评估。

## Limitations

- Repository note: 该论文的头号贡献是 Agent-as-a-Judge 方法；DevAI 是其配对、单独发布的 benchmark，本卡片以 benchmark 为中心。arXiv 元数据无发表信息；效率数字（时间/成本节省）为仓库声明。

## Related Works

- [MLE-bench](./mle-bench.md) — 同样是对「构建 ML 系统」的 agent 评估，考 Kaggle 竞赛。
- [MLR-Bench](./mlr-bench.md) — 同样为研究 agent 使用自动（LLM 评审）评估框架。
- [AstaBench](./astabench.md) — 同样是整体式 agent 评估，配评分标准与 judge 打分。
