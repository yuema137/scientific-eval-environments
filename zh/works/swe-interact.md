# SWE-Interact (2026)

> [English](../../works/swe-interact.md) | **简体中文**

## Overview

SWE-Interact 是评估 coding agent 在多轮、交互式、用户驱动的软件工程任务上的测试平台：用户模拟器逐步披露需求并给出反馈，考察 agent 能否发现意图、适应变化并在已有工作上继续推进。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.30573>
- **Venue:** arXiv preprint (cs.LG), 2026

## Summary

SWE-Interact 把 SWE benchmark 重新构想成用户驱动的长 horizon 编码会话：任务描述不再一次性给全，需求通过一个会对 agent 工作做出反应的模拟用户逐步到来。最突出的发现是迁移落差——前沿模型（Opus 4.8、GPT-5.5 及开放权重变体）在单轮形式下能解约 50% 的任务，在多轮用户驱动设定下跌到约 25%：单轮 SWE 上的强表现并不能可靠迁移到交互式工作流。

## Tasks

多轮、用户驱动的软件工程会话，用户模拟器逐步披露需求并提供反馈；任务数为 TODO(reference)。

## Domains

带模拟用户的交互式软件工程。

## Evaluation

- 多轮用户驱动协议下的任务成功率，与相同底层任务的单轮基线直接对比。
- **报告。** 顶级模型单轮约解 50%，多轮仅约 25%——交互使表现近乎减半。

## Typical Duration

需求逐步披露的多轮会话。

## Main Contribution

量化了软件工程中「单轮 → 交互」的迁移落差：成对设计表明一次性作答的能力把协作能力高估了约一倍。

## Key Design Ideas

- 需求逐步披露使意图发现成为受评技能，而非默认前提。
- 同一批任务分别以单轮与多轮运行，交互带来的代价被单独隔离。
- 反应式用户模拟器把协作中的人类一侧标准化。

## Strengths

- 约 50%→约 25% 的成对比较是对交互成本的一次干净、受控的测量。
- 瞄准编码辅助的部署现实，而非批量解 issue。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [SWE-Together](./swe-together.md) — 同样是多轮交互式编码评估，但从真实会话重建而非全程模拟。
- [SWE-bench](./swe-bench.md) — 单轮范式本身——SWE-Interact 测量的正是它的迁移极限。
- [SWE-chat](./swe-chat.md) — 同样研究用户与 agent 的编码交互，以真实会话做观察性研究。
