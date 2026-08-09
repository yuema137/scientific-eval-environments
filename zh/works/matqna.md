# MatQnA (2025)

> [English](../../works/matqna.md) | **简体中文**

## Overview

MatQnA 是面向多模态 LLM 的材料表征与分析 benchmark 数据集，覆盖十种主流表征方法——XPS、XRD、SEM、TEM 等——最先进的模型（GPT-4.1、Claude 4、Gemini 2.5、Doubao Vision Pro）在客观题上已接近 90%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.11335>
- **Dataset:** <https://huggingface.co/datasets/richardhzgg/matQnA>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

MatQnA 按方法组织材料表征评估：十种主流技术，含 X 射线光电子能谱、X 射线衍射、扫描电镜与透射电镜。其问答对——含选择题与主观题——由「LLM 加人类在环校验」的混合方式构建。初步结果显示，前沿多模态模型（GPT-4.1、Claude 4、Gemini 2.5、Doubao Vision Pro 32K）在客观的数据解读题上已达接近 90% 的准确率，这表明，相比更难的推理类 benchmark，表征问答已更接近被攻克。

## Tasks

覆盖十种表征方法（XPS、XRD、SEM、TEM 等）的选择题与主观题；静态多模态问答。题目总数为 TODO(reference)——摘要未载明。

## Domains

材料科学——横跨十种技术的仪器级材料表征与分析。

## Evaluation

- 客观题（选择题）准确率与主观评估；问答由「LLM 加人类在环校验」构建。
- **报告。** 前沿模型在客观题上达接近 90% 的准确率（作者称为初步结果）。

## Typical Duration

单轮多模态问题；无交互式设定。

## Main Contribution

一个按表征方法组织的 benchmark，其接近 90% 的前沿分数把「客观数据解读」定位为当前 MLLM 已然较强的领域——与它们失手的重推理材料 benchmark 形成有用对照。

## Key Design Ideas

- 按表征方法组织，使各技术上的能力可见。
- 混合客观与主观题，把回忆与开放式解读分开。
- 人类在环校验保障问答质量。

## Strengths

- 单一数据集覆盖广泛仪器，且在 HuggingFace 公开发布。
- 接近 90% 的客观题结果是清晰、可引用的能力标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与数据集页编写（2026 年 8 月）；题目总数未载明，且作者称结果为初步。arXiv 元数据无发表信息。

## Related Works

- [MatCha](./matcha.md) — 同样是多模态表征评估，按研究阶段而非方法组织。
- [MatVQA](./matvqa.md) — 同样是表征问答，带抗捷径的视觉推理任务。
- [OpenXRD](./openxrd.md) — 同样是表征问答，专于 X 射线衍射。
