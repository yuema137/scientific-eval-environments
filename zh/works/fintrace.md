# FinTrace (2026)

> [English](../../works/fintrace.md) | **简体中文**

## Overview

FinTrace 是面向 LLM 工具调用在长 horizon 金融决策任务上的 holistic trajectory-level 评估 benchmark。它在 4 个维度下给出 9 个指标，而不仅仅打分最终答案。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.10015>

## Summary

FinTrace 评估 LLM 在金融决策中使用外部工具的能力。它不仅评分最终答案，而是把整条 trajectory 放在 4 个维度下的 9 个指标上评估：action correctness、execution efficiency、process quality、output quality。该 benchmark 同时发布了一个带标注的 trajectory 训练语料库。

## Tasks

800 条 trajectory，覆盖 34 个任务类别。

## Domains

金融决策 + 外部工具调用。

## Evaluation

4 个维度下的 9 个指标：

- Action correctness
- Execution efficiency
- Process quality
- Output quality

报告：在测试的 13 个模型中，所有模型都在信息利用与最终答案质量上表现不佳，暴露出"调用正确工具"与"对工具输出有效推理"之间的差距。作者同时发布了 8,196 条标注 trajectory 的训练数据集；微调带来了可测量的提升，但端到端的答案质量仍有挑战。

## Typical Duration

长 horizon 的金融工作流。摘要未给出具体单任务时长。

## Main Contribution

面向金融工具调用 agent 的 trajectory 级、四维评估框架，并配套一个大规模标注训练语料。

## Key Design Ideas

- Trajectory 级评估——4 个维度共 9 个指标。
- 领域绑定在金融决策。
- 配套的标注 trajectory 训练语料。

## Strengths

- 多维 trajectory 打分揭示了驱动失败的能力维度。
- 配套训练集使评估与改进工作可在同一框架下进行。
- 覆盖金融领域内的 34 个任务类别。

## Limitations

- Repository note: 领域限定在金融——多维指标框架对其他领域的迁移未被评估。

## Related Works

- [TRACE](./trace.md) — 也做多维 trajectory 评估，但面向 deep-research agent 而非金融。
- [AgentBoard](./agentboard.md) — Trajectory 评估通过子目标进展率，而不是多维指标。
