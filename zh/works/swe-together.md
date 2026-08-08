# SWE-Together (2026)

> [English](../../works/swe-together.md) | **简体中文**

## Overview

SWE-Together 是从真实用户-agent 会话重建的多轮编码 benchmark：从 11,260 条录制会话中整理出 109 个仓库级任务，通过一个保持原始用户意图的反应式 LLM 用户模拟器，在不同 agent 之间回放。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.29957>
- **Venue:** arXiv preprint (cs.SE, cs.AI), 2026

## Summary

多数 coding-agent benchmark 是静态的——任务一次给全、只看最终代码——而真实的编码辅助是交互式的。SWE-Together 通过筛选仓库状态可恢复、用户目标清晰、结果可观察的会话，让真实交互变得可验证，再用保持原意的用户模拟器回放，在 agent 进展需要时给予反馈。agent 被当作协作者来评分：最终仓库正确性，加上交互中所需的纠正反馈轮数。更强的 agent 总体上成功率更高、所需干预更少。

## Tasks

109 个仓库级多轮任务，整理自 11,260 条真实用户-agent 录制会话，每个任务具备可恢复的仓库状态、清晰的用户目标与可观察的结果。

## Domains

植根于真实用户会话的交互式软件工程。

## Evaluation

- **最终仓库正确性**，加上交互期间所需的**纠正反馈轮数**。
- **报告。** 更强的 agent 总体上最终成功率更高，同时需要的干预更少。

## Typical Duration

每个任务为多轮回放会话。

## Main Contribution

把真实而杂乱的用户-agent 协作变成可验证的 benchmark，并在「代码最终对不对」之外，度量协作让用户付出的纠正成本。

## Key Design Ideas

- 从真实会话筛选（状态可恢复、目标清晰、结果可观察），让真实性与可验证性兼容。
- 保持原意的用户模拟器使同一段真实交互能公平地在不同 agent 上回放。
- 统计纠正轮数，为协作消耗的人力标价。

## Strengths

- 任务分布继承自 11,260 条真实会话，而非 benchmark 作者的想象。
- 双指标捕捉的不只是终局正确性，还有用户体验。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [SWE-chat](./swe-chat.md) — 观察性的对应物：在真实会话之上做指标，而非回放交互。
- [SWE-Interact](./swe-interact.md) — 同样是多轮用户驱动编码，但需求全程由模拟生成。
- [SWE-bench](./swe-bench.md) — 两个交互式 benchmark 共同背离的那个静态范式。
