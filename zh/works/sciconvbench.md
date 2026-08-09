# SciConvBench (2026)

> [English](../../works/sciconvbench.md) | **简体中文**

## Overview

SciConvBench 评测 LLM 在计算科学任务表述上的多轮澄清能力：面对流体力学、固体力学、材料科学或 PDE 领域一个不适定的仿真请求，模型须在任何计算发生之前，通过对话问出缺失的信息（消歧）并发现内部自相矛盾的要求（矛盾消解）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.18630>
- **Code:** <https://github.com/csml-rpi/SciConvBench>
- **Venue:** arXiv preprint (cs.AI, physics.comp-ph), 2026

## Summary

多数仿真失败发生在第一次求解之前：请求本身就欠规范或自相矛盾。SciConvBench 评估先于计算的对话能力，采用结构化任务本体与基于评分标准的框架，从三个维度打分——澄清行为、对话中的共识建立与最终规格保真度——指标含 grounded conversation rate 与澄清召回/精确率（据官方仓库）。即便最好的模型，在流体力学的消歧算例上也只解决 52.7%。

## Tasks

跨四个领域（流体力学、固体力学、材料科学、PDE）的不适定计算科学请求上的多轮澄清对话，分消歧与矛盾消解两类变体；任务数为 TODO(reference)。

## Domains

跨流体力学、固体力学、材料科学与 PDE 的计算科学任务表述。

## Evaluation

- 基于结构化任务本体的评分标准框架：澄清行为、对话共识建立、最终规格保真度；据官方仓库另有 grounded conversation rate 与澄清召回/精确率。
- **报告。** 最好的模型在流体力学消歧算例上仅解决 52.7%。

## Typical Duration

每个任务为多轮澄清对话。

## Main Contribution

把评估边界前移到求解器之前：模型能否把一个不适定的科学请求变成适定的规格，被作为一项独立能力来测量。

## Key Design Ideas

- 不适定性是刻意构造的（信息缺失对信息矛盾），因此所需的对话行为是已知的。
- 最终以规格保真度收口，把对话质量绑定到一个可检验的产物上。
- 非科学的对照集把领域能力与通用对话技巧分开（据官方仓库）。

## Strengths

- 瞄准了多数仿真 benchmark 直接跳过的失败阶段。
- 流体力学 52.7% 的上限表明澄清远未被解决。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [SWE-Interact](./swe-interact.md) — 同样测量需求逐步披露的对话，在软件工程中。
- [SimBench](./simbench.md) — 同样是多轮的仿真设定，但在生成工件层面评估。
- [CFDLLMBench](./cfdllmbench.md) — 下游对应物：评估适定 CFD 规格之后的求解。
