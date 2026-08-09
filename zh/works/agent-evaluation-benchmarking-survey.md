# Evaluation and Benchmarking of LLM Agents: A Survey (2025)

> [English](../../works/agent-evaluation-benchmarking-survey.md) | **简体中文**

## Overview

*Evaluation and Benchmarking of LLM Agents: A Survey* 是一篇关于 LLM-agent 评估领域的综述：提出一个二维分类法，沿 evaluation objectives（评估什么）与 evaluation process（如何评估）组织现有工作，并强调面向企业部署的评估挑战。此处以**参考论文**（非 benchmark 贡献）纳入。

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — 综述或立场论文，无受评任务。

## Links

- **Paper:** <https://arxiv.org/abs/2507.21504>

## Summary

综述对 LLM-agent 评估——它称之为一个复杂且尚不成熟的领域——作了深入综述。它沿二维分类法组织领域：(1) evaluation objectives——评估什么，如 agent behavior、capabilities、reliability 与 safety；(2) evaluation process——如何评估，包括 interaction modes、datasets and benchmarks、metric computation methods 与 tooling。除分类法外，它还强调了当前研究常忽视的面向企业的挑战——role-based data access、reliability guarantees、dynamic and long-horizon interactions 与 compliance——并指出面向 holistic、更现实、可扩展评估的未来方向。

## Tasks

N/A——综述论文。

## Domains

跨领域覆盖：LLM-agent 评估与 benchmarking，并显式关注企业部署场景。

## Evaluation

N/A——综述论文。综述本身将 evaluation-process 方法（interaction modes、datasets and benchmarks、metric computation methods、tooling）作为其分类法的一个维度加以组织。

## Typical Duration

N/A。

## Main Contribution

一个二维的 LLM-agent 评估分类法——沿 evaluation objectives（评估什么）与 evaluation process（如何评估）组织工作——并阐明面向企业的评估挑战。

## Key Design Ideas

- 二维分类法，区分*评估什么*（objectives）与*如何评估*（process）。
- Evaluation objectives：agent behavior、capabilities、reliability 与 safety。
- Evaluation process：interaction modes、datasets and benchmarks、metric computation methods 与 tooling。
- 显式处理企业挑战：role-based data access、reliability guarantees、dynamic and long-horizon interactions 与 compliance。

## Strengths

- 将评估目标与评估过程分离，厘清原本碎片化的图景。
- 突出以 benchmark 为中心的综述常忽略的企业部署关切（访问控制、可靠性、合规）。
- 给出具体的未来方向：holistic、现实、可扩展的评估。

## Limitations

- Repository note: 综述在发布时刻冻结了领域状态；作为一篇 2025 年 7 月的综述，它未覆盖本仓库中记录的更晚工作。

## Related Works

- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — 同为专注 LLM-agent 评估的综述；沿五视角分类组织领域，而非本文的 objectives/process 二维划分。
- [A Survey on Large Language Model based Autonomous Agents](./llm-autonomous-agents-survey.md) — 更宽泛的 agent 综述，除评估外还覆盖构建与应用，而非只谈评估。
- [From Chatbot to Digital Colleague](./from-chatbot-to-digital-colleague.md) — 同为元层次参考论文；一篇主张方向的立场论文，而非编目领域的综述。
