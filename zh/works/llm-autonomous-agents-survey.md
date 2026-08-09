# A Survey on Large Language Model based Autonomous Agents (2023)

> [English](../../works/llm-autonomous-agents-survey.md) | **简体中文**

## Overview

*A Survey on Large Language Model based Autonomous Agents* 是一篇关于 LLM-based 自主 agent 的综述：提出统一的 agent 构建框架，编目其在社会科学、自然科学与工程领域的应用，并综述这类 agent 常用的评估策略。此处以**参考论文**（非 benchmark 贡献）纳入；其主题是 agent 构建而非评估（见 Limitations 中的 repository note）。

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — 综述或立场论文，无受评任务。

## Links

- **Paper:** <https://arxiv.org/abs/2308.11432>

## Summary

综述从整体视角沿三大支柱——构建、应用、评估——回顾 LLM-based 自主 agent 领域。在构建方面，它提出一个由 profiling module、memory module、planning module 与 action module 构成的统一框架；随后概述其在社会科学、自然科学与工程领域的应用；并综述常用的评估策略，区分 subjective evaluation（基于人类判断）与 objective evaluation（可量化的性能指标）。最后给出挑战与未来方向。

## Tasks

N/A——综述论文。

## Domains

跨领域覆盖：LLM-based 自主 agent，应用于社会科学、自然科学与工程。

## Evaluation

N/A——综述论文。综述本身回顾了 LLM-based 自主 agent 的评估策略，将其分为 subjective evaluation（基于人类判断）与 objective evaluation（可量化的性能指标）。

## Typical Duration

N/A。

## Main Contribution

一篇整体性的 LLM-based 自主 agent 综述，围绕统一构建框架、跨三个领域族的应用分类，以及 subjective 与 objective 评估策略的回顾组织。

## Key Design Ideas

- 统一的 agent 构建框架，含四个模块：profiling、memory、planning、action。
- 应用分类跨越社会科学、自然科学与工程。
- 评估被回顾为 subjective（基于人类判断）与 objective（基于指标）两类策略。

## Strengths

- 对 LLM-based 自主 agent 文献的早期、整体性覆盖广泛。
- 四模块构建框架提供了比较各类 agent 设计的通用词汇。
- 将构建、应用与评估合并讨论，而非彼此孤立。

## Limitations

- Repository note: 该综述的主要贡献是 agent *构建*（架构、应用），评估只是三大支柱之一，而非论文重心。此处为完整性纳入 Survey；寻求以评估为核心的综述的读者应从 [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) 入手。
- Repository note: 综述在发布时刻冻结了领域状态；作为一篇 2023 年 8 月的综述，它早于本仓库记录的大多数工作。

## Related Works

- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — 同为综述参考论文，但专注于 LLM-agent *评估*，而非 agent 构建与应用。
- [From Chatbot to Digital Colleague](./from-chatbot-to-digital-colleague.md) — 同为元层次参考论文；一篇主张方向的立场论文，而非编目领域的综述。
