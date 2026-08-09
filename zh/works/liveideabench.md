# LiveIdeaBench (2024)

> [English](../../works/liveideabench.md) | **简体中文**

## Overview

LiveIdeaBench 在极简上下文下评测 LLM 的发散思维——科学想法生成能力：40 多个领先模型从单关键词提示生成想法，覆盖 22 个科学领域的 1,180 个关键词，由 LLM 面板按五个维度评分——原创性、可行性、流畅性、灵活性、清晰性。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.17596>
- **Code:** <https://github.com/x66ccff/LiveIdeaBench>
- **Dataset:** <https://huggingface.co/datasets/6cf/liveideabench>
- **Venue:** Nature Communications（据官方仓库；arXiv 元数据无发表信息）

## Summary

当前版本题为「Evaluating LLMs' Divergent Thinking Capabilities for Scientific Idea Generation with Minimal Context」。LiveIdeaBench 把创造力与上下文分开：模型从单关键词提示生成科学想法，考的是发散思维而非上下文丰富的展开。40 多个领先模型在覆盖 22 个科学领域的 1,180 个关键词上受评，由一个动态的先进 LLM 面板按五个基于 Guilford 创造力理论的维度评分——原创性、可行性、流畅性、灵活性、清晰性。一个关键发现：创造力难以由通用智力指标预测——QwQ-32B-preview 尽管通用智力分较低，却可与 claude-3.7-sonnet:thinking 等顶尖模型比肩。

## Tasks

覆盖 1,180 个关键词、22 个领域、40 多个模型的单关键词科学想法生成；静态生成，由 LLM 面板按五个创造力维度评分。

## Domains

AI 与机器学习研究——科学研究构思与发散思维（经关键词提示覆盖诸多科学领域）。

## Evaluation

- LLM 面板按五个维度（原创性、可行性、流畅性、灵活性、清晰性）评分，基于 Guilford 创造力理论。
- **报告。** 创造力难以由通用智力指标预测；QwQ-32B-preview 尽管通用智力分较低仍与 claude-3.7-sonnet:thinking 比肩。

## Typical Duration

单轮「关键词到想法」生成；无交互式设定。

## Main Contribution

一个极简上下文的发散思维 benchmark，把科学创造力与通用能力分开——表明想法生成质量不为标准智力指标所捕捉。

## Key Design Ideas

- 单关键词提示剥去上下文，隔离发散思维。
- 五个基于 Guilford 的维度给创造力一个结构化、有理论依据的评分标准。
- 动态 LLM 面板在广度上评分（40+ 模型、1,180 关键词、22 领域）。

## Strengths

- 大规模、跨领域的创造力评估，配有理论根基的评分标准，公开发布。
- 「创造力 vs 通用智力」的解耦是新颖、可引用的发现。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；论文已改题，Nature Communications 是仓库声明、arXiv 元数据未载明。仓库列出 41 个模型，摘要为「40 多个」。

## Related Works

- [IdeaBench](./ideabench.md) — 同样是研究想法生成，以更丰富的论文上下文而非单关键词为依据。
- [MLR-Bench](./mlr-bench.md) — 同样评估想法生成，在完整研究流程内。
- [MLGym](./mlgym.md) — 同样涉及假设/想法生成，在 AI 研究循环中。
