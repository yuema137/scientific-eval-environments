# MetaSyn (2026)

> [English](../../works/metasyn.md) | **简体中文**

## Overview

MetaSyn 是面向系统综述与 meta 分析的 LLM agent benchmark，基于从 34,000 余篇 Nature Portfolio 文章中整理出的 422 项专家 meta 分析构建，提供研究问题、结构化的入选标准、原综述作者纳入的研究，以及锚定 PubMed 的共享语料。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.17041>
- **Venue:** arXiv preprint, 2026

## Summary

MetaSyn 追问 LLM agent 能否按标准化协议（PI/ECO 框架）开展可靠的系统综述与证据综合。每个任务给定带结构化入选标准的研究问题，语料中混有原综述作者纳入的研究与不合格干扰项；agent 须识别出合格集合并做综合。论文随数据集一并发布了 MA-Retriever 模型。

## Tasks

422 项专家整理的 meta 分析，取自 34,000 余篇已发表的 Nature Portfolio 文章；每项打包研究问题、结构化入选标准、原综述作者纳入的研究，以及含不合格干扰项、锚定 PubMed 的共享语料。

## Domains

Meta 分析主题横跨物理、化学、心理学与医学。

## Evaluation

- 以原综述作者的纳入集合为对照做文献识别，语料含不合格干扰项。
- 分阶段评估与分析，定位系统在 meta 分析流程中的薄弱环节。
- **报告。** 作者结论：现有 AI 系统在协议忠实的 meta 分析上仍远非完善。

## Typical Duration

在文献语料上的多阶段系统综述工作流；单任务预算为 TODO(reference)。

## Main Contribution

首个将 agent 评估锚定于专家完成的 meta 分析的大规模 benchmark，使忠实于协议的系统综述成为可度量的 agent 能力。

## Key Design Ideas

- 真值是原综述作者实际纳入的研究，而非合成标签。
- 带干扰项、锚定 PubMed 的共享语料把入选筛查变成受控的检索问题。
- 分阶段评估沿综述流程定位失败，而非只报一个总分。

## Strengths

- 从 34,000+ 篇文章蒸馏出 422 个任务，专家锚定的评估达到少见的规模。
- 评估的是 PI/ECO 协议忠实度，而不只是答案重合。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [DeepResearch Bench](./deepresearch-bench.md) — 同样评估以文献为根基的综合，但打分对象是开放域研究报告而非受协议约束的 meta 分析。
- [AutoResearchBench](./autoresearchbench.md) — 同样对照已验证答案集为文献识别打分，但面向论文发现而非入选筛查。
- [NatureBench](./naturebench.md) — 同样从 Nature 系列论文派生评估目标，但用于方法复现而非证据综合。
