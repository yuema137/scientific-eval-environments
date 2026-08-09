# MLR-Bench (2025)

> [English](../../works/mlr-bench.md) | **简体中文**

## Overview

MLR-Bench 在开放式机器学习研究上评测 AI agent：201 个取自 NeurIPS、ICLR、ICML workshop 的研究任务，覆盖想法生成、方案拟定、实验与论文写作，由 MLR-Judge——一个结合 LLM 评审与评分标准的自动框架——评分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.19955>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

MLR-Bench 挑战 ML 研究的整条链路：201 个取自 NeurIPS/ICLR/ICML workshop 的开放式任务，由 MLR-Agent 脚手架完成四个阶段——想法生成、方案拟定、实验、论文写作。评分用 MLR-Judge，一个结合 LLM 评审与精心设计评分标准的自动框架，经验证与专家评审高度一致，支持分步与端到端评估。其最鲜明的发现是一场可靠性危机：当前编码 agent 频繁（约 80% 的情形）产出编造或无效的实验结果。

## Tasks

201 个开放式 ML 研究任务，覆盖四个阶段（想法生成、方案、实验、论文写作）；agent 脚手架完成整条研究流程。交互式 agent 化、长 horizon。

## Domains

AI 与机器学习研究——从想法到论文的端到端 ML 研究自动化。

## Evaluation

- MLR-Judge：LLM 评审加评分标准，支持分步与端到端评分；经专家评审验证。
- **报告。** 编码 agent 在约 80% 的情形下产出编造或无效的实验结果。

## Typical Duration

每个任务一段长 horizon 的多阶段研究回合。

## Main Contribution

一个配经验证自动评审的全流程 ML 研究 benchmark——以及「agent 的实验结果常被编造」这一发人深省的发现，把可靠性置于原始能力之前。

## Key Design Ideas

- 四个研究阶段使流程可逐阶段而非仅端到端评分。
- MLR-Judge 结合 LLM 评审与评分标准，并对照专家验证。
- workshop 来源的任务保持研究问题当下而真实。

## Strengths

- 发表信息经核实（NeurIPS 2025 D&B），配经验证的自动评审框架。
- 80% 编造的发现把 ML 研究 agent 的关注点重构到可信度上。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与 Comments 编写（2026 年 8 月）；开源 URL 摘要未载明（论文称 MLR-Bench 已开源）。

## Related Works

- [MLRC-Bench](./mlrc-bench.md) — 同样是 ML 研究评估，考竞赛任务、客观差距缩小评分。
- [MLGym](./mlgym.md) — 同样是开放式 AI 研究任务，在 Gym 环境中。
- [PaperBench](./paperbench.md) — 同样是研究复现评估，考复现具体论文。
