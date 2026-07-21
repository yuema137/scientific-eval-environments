# Aviary (2024)

## Overview

Aviary 是一个面向 language agent 的可扩展 gymnasium，将 agent 形式化为在 language-grounded 部分可观测马尔可夫决策过程（POMDP）中求解的策略。它实现五个环境，其中三个为科学环境——DNA 构建操作（分子克隆）、科学文献研究与蛋白质工程——提供可复用的多步科学任务环境。本仓库为这些科学评估环境而收录它；论文的训练框架贡献是与本仓库范围相邻的 agent 构建工作（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.21154>
- **Code:** <https://github.com/Future-House/aviary>

## Summary

Aviary 将 language agent 形式化为在 language-grounded 部分可观测马尔可夫决策过程中行动的策略，并提供一个可扩展的环境 gymnasium 供其运行。它实现五个环境，其中三个为具挑战性的科学环境，聚焦 DNA 构建操作（分子克隆）、通过科学文献访问回答研究问题，以及蛋白质（稳定性）工程，均强调与当代生物学研究相关的多步推理。论文报告，由开源、非前沿 LLM 支撑的 language agent 能在多个任务上以至多 100× 更低的推理成本匹敌并超越前沿 LLM agent 与人类专家。

## Tasks

五个环境，其中三个为科学环境：DNA 构建操作 / 分子克隆、科学文献研究问答，以及蛋白质（稳定性）工程。确切的环境名称、任务计数以及两个非科学环境：TODO(reference)——摘要未说明。

## Domains

分子生物学（分子克隆、蛋白质工程）与科学文献研究的科学任务环境，另有两个非科学环境（摘要未说明）。

## Evaluation

- agent 作为 language-grounded POMDP 环境中的策略行动；性能按各环境的任务成功率衡量。
- 确切指标与各环境任务计数：TODO(reference)——摘要未说明。
- 报告：开源、非前沿 LLM 的 agent 在多个任务上以至多 100× 更低的推理成本匹敌或超越前沿 LLM agent 与人类专家。

## Typical Duration

每个环境的多步推理回合。单任务步数 / 时间预算：TODO(reference)——摘要未说明。

## Main Contribution

论文陈述的贡献是作为 language agent gymnasium 的 Aviary，以及使小模型 agent 能匹敌前沿 agent 与人类专家的训练 / 推理时计算方法。在本仓库中，其在范围内的贡献是 Aviary 的科学环境作为可复用的评估环境。

## Key Design Ideas

- 将 agent 形式化为 language-grounded 部分可观测 MDP 上的策略。
- 在一个抽象下承载多个环境的可扩展 gymnasium。
- 三个科学环境（分子克隆、文献研究、蛋白质工程），强调多步推理。
- 通过在线训练与推理时计算扩展展示了强的成本–性能权衡（至多 100× 更低推理成本）。

## Strengths

- 在统一 agent 抽象下提供可复用、可扩展的科学任务环境。
- 科学环境根植于当代生物学研究问题。
- 报告了一个引人注目的成本–性能结果，重构了前沿对开源的比较。

## Limitations

- Repository note: 论文的主要框架是*训练* language agent（在线训练、推理时计算扩展）——属于本仓库以评估为核心的范围之外的 agent 构建工作。此处为 Aviary 的科学环境作为评估环境而收录，而非为训练方法。
- Repository note: 确切的环境名称、任务计数与各环境评估指标在摘要中未说明，标注为 `TODO(reference)`，待从论文或代码核实。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样评估 agent 在科学任务上的能力，但作为专家验证任务的固定 benchmark，而非可扩展的训练兼评估 gymnasium。
- [SciAgentArena](./sciagentarena.md) — 同为面向 agent 的交互式科学研究环境，跨尺度进行逐步验证。
