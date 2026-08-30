# AgentBench (2023)

> [English](../../works/agentbench.md) | **简体中文**

> **首次公开：** 2023-08-07 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2308.03688)

## Overview

AgentBench 是一个多维 benchmark，跨 8 个不同的交互环境将 LLM 作为 agent 评估，考察其在多轮交互中的推理与决策能力。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2308.03688>
- **Code:** <https://github.com/THUDM/AgentBench>
- **Venue:** ICLR 2024

## Summary

AgentBench 回应了在交互环境中对 LLM 作为 agent 进行定量评估的迫切需求。它汇集 8 个不同环境，考察 LLM-as-agent 在多轮交互中的推理与决策，并同时评估基于 API 的商用模型与开源模型。研究报告了顶尖商用 LLM 与开源模型之间的显著能力差距，并指出长期推理、决策与指令遵循是主要瓶颈。

## Tasks

八个交互环境，按 grounding 分组：**代码类**——Operating System（Linux bash）、Database（MySQL 上的 SQL）、Knowledge Graph；**游戏类**——Digital Card Game、Lateral Thinking Puzzles、House-Holding（基于 ALFWorld）；**web 类**——Web Shopping（基于 WebShop）、Web Browsing（基于 Mind2Web）。

## Domains

跨操作系统、数据库、知识图谱、游戏、具身家务模拟与 web 的交互式 agent 任务。

## Evaluation

- **各环境指标。** 每个环境采用与之匹配的指标：Success Rate（Operating System、Database、House-Holding）、Answer F1（Knowledge Graph）、reward / 胜率（Digital Card Game、Web Shopping）、Game Progress——达成情节点的比例（Lateral Thinking Puzzles），以及 Step Success Rate（Web Browsing）。
- **通过逐任务归一化得到 Overall Score。** 八个指标量纲不同，因此先归一化再平均：以固定的逐任务权重（该任务上所有被测模型平均分的倒数）把每个任务的跨模型平均值缩放到 1.0，将每个模型的逐任务得分乘以该权重，再对八个任务取平均。权重被冻结，以便对未来模型可复现地打分。
- **报告。** GPT-4 以 4.01 的 overall score 大幅领先；最强开源模型（CodeLlama-34b）为 0.96。按模型平均，基于 API 的商用 LLM 为 2.15，开源为 0.51——约 4 倍差距。主要失败模式：长期推理、决策与指令遵循偏弱。

## Typical Duration

多轮交互，长度随环境而异——交互最密集的（House-Holding、Digital Card Game、Lateral Thinking Puzzles）可达数十回合，而 Operating System、Database、Web Shopping 较短。论文未单独列出逐任务的硬性回合上限。

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

- Repository note: 八个环境中有六个基于或改编自既有数据集（ALFWorld、WebShop、Mind2Web）；AgentBench 自身的贡献是统一的评测框架、三个代码类环境与跨环境的归一化打分，而非全部任务内容。

## Related Works

- [SWE-bench](./swe-bench.md) — 同为通用 agent benchmark，但专注于软件工程 issue 解决，而非横跨 8 个环境。
- [GAIA](./gaia.md) — 同样评估通用助手能力，但通过统一的问答界面而非多个环境。
