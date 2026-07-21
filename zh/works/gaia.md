# GAIA (2023)

## Overview

GAIA 是一个面向通用 AI 助手的 benchmark，提出需要推理、多模态处理、web 浏览与通用工具使用能力的真实世界问题。这些问题对人类而言概念简单且无歧义，对前沿模型却很困难。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2311.12983>
- **Project:** <https://huggingface.co/gaia-benchmark>

## Summary

GAIA 提出若被解决则代表通用 AI 助手里程碑的真实世界问题。每个问题都需要一组基础能力——推理、多模态处理、web 浏览与工具使用——但被设计为具有人类可可靠给出的单一无歧义答案。该 benchmark 揭示了巨大的人–模型差距：人类回答者达到 92%，而配备插件的 GPT-4 为 15%。

## Tasks

466 个带答案的真实世界问题，其中 300 个答案保留用于排行榜。每个问题都需组合基础助手能力（推理、多模态、web 浏览、工具使用）。

## Domains

跨日常与知识密集型任务的通用助手问题，需要 web 与工具访问；包含多模态输入。

## Evaluation

- 每个问题被设计为具有单一正确、无歧义的答案，便于自动打分。
- 精确打分协议细节：TODO(reference)——摘要未详述。
- 报告：人类得到 92%，配备插件的 GPT-4 为 15%。

## Typical Duration

多步：问题通常需要若干浏览 / 工具使用步骤。单任务预算：TODO(reference)——摘要未说明。

## Main Contribution

一个其问题对人类概念简单且无歧义、却需要真实助手能力（工具使用、浏览、多模态）的 benchmark，暴露出巨大且具诊断性的人–模型差距。

## Key Design Ideas

- 对人类简单无歧义、对模型困难的问题——一种抵抗投机取巧的不对称性。
- 需要在一个问题中组合多种基础能力。
- 单一答案设计使评分客观、低歧义。
- 保留答案的划分支持排行榜。

## Strengths

- 清晰无歧义的答案使评分客观。
- 考察真实助手能力（浏览、工具、多模态）而非闭卷知识。
- 巨大的人–模型差距给出强 headroom 信号。

## Limitations

- Repository note: 精确的自动打分协议在摘要中未详述，标注为 `TODO(reference)`。

## Related Works

- [AgentBench](./agentbench.md) — 同样面向通用 agent 能力，但横跨多个交互环境而非统一问答界面。
- [WebArena](./webarena.md) — 同样需要真实 web 交互，但在实时网站内以功能正确性打分，而非答案匹配。
