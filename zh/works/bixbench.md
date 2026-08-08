# BixBench (2025)

> [English](../../works/bixbench.md) | **简体中文**

## Overview

BixBench 是面向计算生物学 LLM agent 的 benchmark：50 余个来自真实世界的生物数据分析场景、近 300 个开放式问题，agent 在容器化 Jupyter 环境中探索数据集并完成长的多步分析轨迹。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.00096>
- **Code:** <https://github.com/Future-House/BixBench>
- **Dataset:** <https://huggingface.co/datasets/futurehouse/BixBench>
- **Venue:** arXiv preprint (q-bio.QM, cs.AI), 2025

## Summary

BixBench 的场景来自真实发表的分析，要求 agent 探索底层数据集、执行多步分析并解读微妙的结果。评估分两种设定：开放式作答（LLM 判分）与选择题（精确匹配），通过开源 agent harness 做 Docker 容器化的代码执行。前沿模型表现很差：最新模型在开放式设定下也只有 17% 准确率，选择题不比随机好。

## Tasks

50 余个真实生物数据分析场景、近 300 个开放式问题（摘要口径；当前仓库版本为来自 60 个已发表 Jupyter notebook 的 205 个问题），以带容器化代码执行的探索式多步 agent 轨迹运行。

## Domains

源自真实已发表 notebook 分析的计算生物学与生物信息学数据分析。

## Evaluation

- 开放式设定用 LLM 判分，选择题用精确匹配；据官方仓库对多副本做多数投票。
- **报告。** 前沿模型（GPT-4o、Claude 3.5 Sonnet）开放式设定下仅 17% 准确率，选择题不比随机好。

## Typical Duration

每个场景为长的多步分析轨迹；预算为 TODO(reference)。

## Main Contribution

把真实发表的分析改写成开放式 agent 任务，表明前沿 agent 做不好计算生物学家日常在做的探索式数据分析。

## Key Design Ideas

- 场景取自真实 notebook，难度反映真实的分析实践。
- 开放式与选择题成对设置，把生成能力与识别能力分开。
- 容器化执行让多步轨迹在不同 agent 间可复现。

## Strengths

- 任务来源生态真实，出自已发表的分析。
- 「开放式仅 17%、选择题不优于随机」这一结果，为生物信息学 agent 立起了严峻的早期基线。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。摘要与当前仓库的问题数不一致（约 296 vs. 205），应为数据集修订所致。

## Related Works

- [GenoTEX](./genotex.md) — 同样源自真实分析的生物信息学 agent 评估，配专家整理的参考流水线。
- [BioAgent Bench](./bioagent-bench.md) — 同样是端到端生物信息学流水线，按产物判分并带鲁棒性扰动。
- [HeurekaBench](./heurekabench.md) — 同样从已发表研究及其代码派生开放式问题，在单细胞生物学。
