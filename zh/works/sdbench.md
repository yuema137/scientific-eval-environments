# SDBench (2025)

> [English](../../works/sdbench.md) | **简体中文**

## Overview

SDBench（Sequential Diagnosis Benchmark）把 304 个高难度 NEJM 临床病理讨论会（CPC）病例改造成交互式接诊：agent 从简短的病例摘要出发，须向一个「守门人」模型逐条索取检查发现——信息只有被明确问到才会给出——评分同时看诊断准确率与就诊和检查的花费。配套的 MAI-DxO 编排器属于 agent 构建工作（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.22405>
- **Project:** <https://microsoft.ai/new/the-path-to-medical-superintelligence/>
- **Venue:** arXiv preprint (cs.CL), 2025

## Summary

SDBench 把诊断变成预算化的信息获取问题：每项检查都有费用，守门人只应答被明确提出的询问，被评估的因此是「准确率-成本前沿」而非单独的准确率。OpenAI、Gemini、Claude、Grok、DeepSeek 与 Llama 系模型与 21 位美英执业医生（据官方页完成病例的平均准确率为 20%）同场受评。论文配套的 MAI-DxO 编排器搭配 o3 达到 80% 准确率——医生平均值的四倍——同时比医生降低 20% 诊断费用、比裸用 o3 降低 70%；最高准确率配置达 85.5%。

## Tasks

304 个 NEJM-CPC 病例的序贯诊断接诊：向守门人索取发现、开具带费用的检查、给出最终诊断。

## Domains

临床诊断（NEJM-CPC 病例的普通内科范畴）、诊断检验与医疗成本。

## Evaluation

- 诊断准确率与就诊、检查费用成对报告——显式的准确率-成本前沿；最终诊断的判分细节为 TODO(reference)。
- **报告。** MAI-DxO 配 o3：80% 准确率（医生平均 20%），费用比医生低 20%、比裸 o3 低 70%；最高准确率配置 85.5%。

## Typical Duration

每个病例为迭代的守门人问询回合，逐动作累计费用。

## Main Contribution

给每个诊断问题标上价格：成本与准确率联合评分，把「诊断得准」与「诊断得起」区分开来。

## Key Design Ideas

- 守门人把信息获取变成显式、可审计的动作。
- 成本核算使过度检查成为被测的失败模式，而非免费策略。
- 同病例的医生队列为前沿的两条轴同时提供锚点。

## Strengths

- 本仓库记录的最干净的成本感知临床评估。
- 前沿结果表明改变编排方式（而不只是换模型）就能移动准确率-成本前沿。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与微软官方页面编写（2026 年 8 月）；此外的细节有待全文校验。官方页面声明 SDBench 与 MAI-DxO 为研究演示、未公开发布；绝对金额为 TODO(reference)。
- Repository note: 论文的第二项贡献 MAI-DxO 属于 agent 实现，超出本仓库范围；本卡片记录其 benchmark。

## Related Works

- [AgentClinic](./agentclinic.md) — 同样是序贯临床评估，侧重对话、偏差与多模态而非成本。
- [CostBench](./costbench.md) — 同样把成本最优决策作为评估对象，在工具使用规划中。
- [MedHELM](./medhelm.md) — 这一序贯设计所补充的静态、医生验证的套件。
