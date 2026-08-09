# TRAJDEBUG (2026)

> [English](../../works/trajdebug.md) | **简体中文**

## Overview

TRAJDEBUG 是在长 horizon agent 轨迹中识别关键失败的错误生命周期追踪框架，随之发布 TrajErrBench——486 条人工标注的失败轨迹，取自 Tau2Bench 与 SWE-Bench Pro。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.06346>
- **Venue:** arXiv preprint, 2026

## Summary

TRAJDEBUG 通过多粒度历史压缩与基于证据的错误识别来解决长轨迹中的错误发现问题，并追踪每个错误的解决状态与最终影响以支持关键归因——把 agent 事后已恢复的错误与真正决定失败的错误区分开。TrajErrBench 提供 486 条人工标注的失败轨迹，覆盖 tool-use 与编码场景。

## Tasks

TrajErrBench：486 条人工标注的失败轨迹，取自 Tau2Bench 与 SWE-Bench Pro，覆盖 tool-use 与编码场景。

## Domains

Tool-use 与编码 agent 轨迹。

## Evaluation

- 在多粒度压缩历史上做基于证据的错误识别。
- 关键归因：追踪每个错误的解决状态与最终影响，把已恢复错误与决定失败的错误分开。
- 摘要之外的详细指标定义为 TODO(reference)。

## Typical Duration

对长 horizon 失败轨迹的事后分析。

## Main Contribution

把错误生命周期——发生、解决、最终影响——作为轨迹失败分析的单元，而非把每个检出的错误同等归责。

## Key Design Ideas

- 多粒度历史压缩使超长轨迹的错误发现变得可行。
- 解决状态追踪避免归罪于 agent 已经恢复的错误。
- 带标注的 benchmark 为每次失败配对其关键错误，使归因可度量。

## Strengths

- 瞄准实践中占多数的情形——失败的长 horizon 运行——并加以人工标注。
- 作者承诺发布代码与数据。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [TELBench](./telbench.md) — 同样在长轨迹中定位最早的有害决策，但面向 deep-research 而非 tool-use/编码运行。
- [Who&When Pro](./who-and-when-pro.md) — 同样把失败归因到决定性步骤，但通过受控错误注入而非对自然失败的标注。
- [SearchAuditor](./searchauditor.md) — 同样审计失败的长 horizon 轨迹并有专家标注的关键步骤，面向搜索 agent。
