# UGPhysics (2025)

> [English](../../works/ugphysics.md) | **简体中文**

## Overview

UGPhysics 是本科物理推理的综合 benchmark：5,520 道中英双语问题，覆盖 13 个科目、七种答案类型与四种物理推理技能，全部经过严格的数据泄漏筛查，并由 MARJ（Model-Assistant Rule-based Judgment）流水线判分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.00334>
- **Code:** <https://github.com/YangLabHKUST/UGPhysics>
- **Venue:** ICML 2025

## Summary

UGPhysics 把系统化的物理评估扩展到本科广度：5,520 道双语问题覆盖 13 个科目，七种答案类型堵住答案格式上的捷径，泄漏筛查守住效度。其 MARJ 流水线把规则检查与模型辅助结合起来，专为物理答案的正确性判定而设。在 31 个领先 LLM 上，最高总体准确率为 49.8%（OpenAI o1-mini）——作者以此论证物理推理需要的不止是数学能力。

## Tasks

5,520 道本科水平物理问题，中英双语，横跨 13 个科目、七种答案类型与四种物理推理技能；静态解题。

## Domains

覆盖 13 个科目的本科物理；摘要未逐一列出。

## Evaluation

- **MARJ（Model-Assistant Rule-based Judgment）**流水线，专为物理答案正确性定制。
- **报告。** 31 个领先 LLM 受评；最高总体准确率 49.8%（OpenAI o1-mini）。

## Typical Duration

单题解题；非交互式 agent 设定。

## Main Contribution

带泄漏筛查与物理专用判分流水线的本科广度双语物理评估，把物理推理从数学能力中剥离出来测量。

## Key Design Ideas

- 七种答案类型防止评分塌缩到单一可判格式。
- 双语构建兼作跨语言鲁棒性探针。
- MARJ 在纯规则解析不了物理答案的地方引入模型辅助。

## Strengths

- 规模与广度（5,520 题、13 科目）配上显式的泄漏筛查。
- 31 个模型全部不到 50% 的上限量化了「物理超出数学」的差距。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [CMPhysBench](./cmphysbench.md) — 同样是大规模物理解题评估并配定制判分方案，但为单一子领域的研究生水平。
- [PHYBench](./phybench.md) — 同样是原创物理问题加定制表达式指标，难度到奥赛级。
- [SeePhys](./seephys.md) — 同样是大范围物理评估，配视觉不可或缺的多模态问题。
