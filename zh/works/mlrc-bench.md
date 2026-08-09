# MLRC-Bench (2025)

> [English](../../works/mlrc-bench.md) | **简体中文**

## Overview

MLRC-Bench 追问语言 agent 能否解决机器学习研究挑战：一套 7 个竞赛任务，agent 须提出并实现新颖的研究方法，用客观指标评分——即它把「所提供基线到顶尖人类参与者」之间的差距缩小了多少——最佳 agent 只缩小了 9.3%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.09702>
- **Code:** <https://huggingface.co/spaces/launch/MLRC_Bench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

MLRC-Bench 测量 ML 研究里最难的部分——提出并实现真正新颖的方法，而不只是跑已知管线。其 7 个竞赛任务用客观指标（而非 LLM judge）评分：agent 方案把「所提供基线到顶尖人类参与者分数」之间的差距缩小的比例。即便最佳 agent（MLAB 脚手架下的 gemini-exp-1206）也只缩小了这一差距的 9.3%，暴露出 agent 离有竞争力的 ML 研究还很远。

## Tasks

7 个 ML 研究竞赛任务；agent 在脚手架下提出并实现新颖研究方法，提交方案对照基线与顶尖人类参照评分。

## Domains

AI 与机器学习研究——ML 研究竞赛：提出并实现新颖方法以超越基线、逼近人类竞争水平。

## Evaluation

- 客观的「差距缩小」指标：agent 方案缩小「基线到顶尖人类」差距的比例（无 LLM judge）。
- **报告。** 最佳 agent（MLAB 下的 gemini-exp-1206）只缩小该差距的 9.3%。

## Typical Duration

长 horizon 回合：每个任务提出、实现并迭代一种研究方法。

## Main Contribution

一个客观评分、以人类为锚的新颖方法 ML 研究 benchmark——对照有竞争力的人类基线测量方法创新，而非任务完成。

## Key Design Ideas

- 「差距缩小」评分把难度锚定在顶尖人类参与者，而非任意门槛。
- 客观指标避开了 LLM-as-judge 对研究质量评判的不可靠。
- 要求新颖方法（而非仅实现）瞄准研究而非工程。

## Strengths

- 发表信息经核实（NeurIPS 2025 D&B），公开排行榜。
- 9.3% 的差距结果是研究能力前沿的鲜明、可引用度量。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与 Comments 编写（2026 年 8 月）；套件较小（7 个任务），结果依赖 agent 脚手架（如 MLAB）。

## Related Works

- [MLR-Bench](./mlr-bench.md) — 同样是开放式 ML 研究评估，覆盖从想法到论文的全流程、用 LLM judge。
- [RE-Bench](./re-bench.md) — 同样是以人类为锚的 ML R&D 评估，对照专家时间预算。
- [MLGym](./mlgym.md) — 同样是开放式 AI 研究任务，在 Gym 环境中。
