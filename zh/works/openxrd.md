# OpenXRD (2025)

> [English](../../works/openxrd.md) | **简体中文**

> **首次公开：** 2025-07-12 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2507.09155)

## Overview

OpenXRD 是面向 LLM 与多模态 LLM 的 X 射线衍射问答 benchmark 框架：217 个专家策划的晶体学问题，在 74 个最先进模型上以闭卷与开卷两种条件评测，发现专家审校的上下文对中等规模模型帮助最大。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.09155>
- **Venue:** Digital Discovery (Royal Society of Chemistry), 2025

## Summary

XRD 是晶体学的主力工具，OpenXRD 检验基础模型是否懂它：217 个专家策划的 XRD 问题，由 74 个 LLM 与 MLLM（7B–70B 乃至更大）作答，分闭卷与带辅助段落的开卷两种形式。段落由 GPT-4.5 生成、经晶体学专家审校，由此引出头条发现——即使 token 数相同，专家审校的材料带来的提升也显著大于 AI 生成的材料，且中等规模模型受益最多，而超大模型则出现饱和，甚至反而受到干扰。

## Tasks

217 个专家策划的 XRD/晶体学问题，分闭卷与开卷两种条件；74 个模型上的静态问答。输入是否含真实 XRD 图样图像，摘要未确认。

## Domains

材料科学——晶体学：X 射线衍射的知识与推理。

## Evaluation

- 闭卷与开卷条件下的准确率，在 token 数相同时比较专家审校与 AI 生成的上下文。
- **报告。** 中等规模模型（7B–70B）受上下文帮助最大；超大模型则出现饱和，甚至反而受到干扰；专家审校的上下文胜过 AI 生成的上下文。

## Typical Duration

单轮问答；无交互式设定。

## Main Contribution

一个以罕见模型广度（74 个）进行的晶体学专项评估，并用受控对比分离出「专家策划上下文」相对「AI 生成上下文」的价值。

## Key Design Ideas

- token 数相同下的「专家 vs AI」上下文对比，把提升干净地归因于上下文质量。
- 闭卷与开卷条件把参数化知识与检索利用分开。
- 74 个模型的覆盖让「中等规模受益最多」的结论稳健。

## Strengths

- 发表信息经核实（Digital Discovery, RSC），是本处所录材料 benchmark 中模型扫描最广的。
- 上下文质量结论对检索增强的材料助手有直接指导意义。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与 Comments 编写（2026 年 8 月）；官方代码仓库无法核实，且是否使用真实衍射图像摘要未载明。

## Related Works

- [AtomWorld](./atomworld.md) — 同样以晶体学为中心的 LLM 评估，考结构操作而非 XRD 问答。
- [MatQnA](./matqna.md) — 同样是含 XRD 的表征问答，在覆盖十种方法的多模态设定中。
- [MaScQA](./mascqa.md) — 同样是专家策划的材料科学问答，覆盖更广。
