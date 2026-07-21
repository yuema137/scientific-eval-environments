# AgentBench (2023)

## Overview

AgentBench 是一个多维 benchmark，跨 8 个不同的交互环境将 LLM 作为 agent 评估，考察其在多轮交互中的推理与决策能力。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.03688>
- **Code:** <https://github.com/THUDM/AgentBench>
- **Venue:** ICLR 2024

## Summary

AgentBench 回应了在交互环境中对 LLM 作为 agent 进行定量评估的迫切需求。它汇集 8 个不同环境，考察 LLM-as-agent 在多轮交互中的推理与决策，并同时评估基于 API 的商用模型与开源模型。研究报告了顶尖商用 LLM 与开源模型之间的显著能力差距，并指出长期推理、决策与指令遵循是主要瓶颈。

## Tasks

8 个不同的交互环境，覆盖推理与决策任务。8 个环境的确切清单：TODO(reference)——摘要未逐一列出。

## Domains

跨多种任务类型的交互式 agent 环境（编码 / 操作系统式、知识 / 数据库、游戏、web、家务式环境）。精确的环境清单：TODO(reference)。

## Evaluation

- 每个环境内的多轮交互，按各环境的任务特定成功率打分。
- 在同一协议下评估商用（基于 API）与开源 LLM。

## Typical Duration

每个环境的多轮交互回合。单任务的步数 / 时间预算：TODO(reference)——摘要未说明。

## Main Contribution

一个系统性的多环境 benchmark，定量评估 LLM-as-agent 的推理与决策，浮现出显著的商用–开源差距与具体能力瓶颈。

## Key Design Ideas

- 在一个评估框架下的 8 个异构环境，覆盖 agentic 能力的广度。
- 多轮交互而非单次响应。
- 对商用与开源模型的统一评估。
- 诊断瓶颈：长期推理、决策、指令遵循。

## Strengths

- 单一 benchmark 覆盖 8 个不同环境的广度。
- 在同一协议下直接比较商用与开源模型。
- 指出可操作的能力瓶颈，而非单一排行榜数字。

## Limitations

- Repository note: 8 个环境的确切集合在摘要中未逐一列出，标注为 `TODO(reference)`，待从论文核实。

## Related Works

- [SWE-bench](./swe-bench.md) — 同为通用 agent benchmark，但专注于软件工程 issue 解决，而非横跨 8 个环境。
- [GAIA](./gaia.md) — 同样评估通用助手能力，但通过统一的问答界面而非多个环境。
