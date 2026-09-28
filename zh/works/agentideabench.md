# AgentIdeaBench (2026)

> [English](../../works/agentideabench.md) | **简体中文**

> **首次公开：** 2026-09-07 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.07611)

## Overview

AgentIdeaBench 检查 agent 自己搜集文献后能否提出科学假设。它将这个过程与直接提供整理好的参考文献作比较，两种设置使用相同的输出格式和结合文献的评审模型。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **论文：** [AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era](https://arxiv.org/abs/2609.07611)，2026 年预印本。
- **全文：** <https://arxiv.org/html/2609.07611v1>
- **代码与数据：** <https://github.com/HKUST-KnowComp/AgentIdeaBench>（9 月 11 日宣布发布）。

## Summary

评审流程先检索已有研究，再判断原创性，不只依赖评审模型的记忆。论文报告主动探索提高了可行性、清晰度和具体程度，但没有显著提高测得的原创性。实验一共涉及 35 个模型，其中 33 个具有配对的 Static–Active 输出；主要结果使用主实验组中 28 个具有配对输出的模型。

## Tasks

基准包含 100 个研究子领域，其中 40 个接受密集评分，每个学科八个。每个模型在每个子领域、每种设置下生成三个假设。Static 直接提供论文标题和摘要；Active 提供子领域名称及 Semantic Scholar search/fetch 工具。两种设置都要求输出一个 80–150 词的假设。因此，一次任务从研究方向出发，经过证据收集，形成提案，最后获得各项评审分数。

## Domains

计算机科学、物理、生物、化学和医学。每个学科有八个密集评分子领域。任务要求依据文献提出假设，不要求执行实验。原文没有为每个学科的整组任务指定一个统一的子领域标签。

## Evaluation

三个评审模型分别判断原创性、可行性、清晰度、影响和具体程度。每个维度去掉最高分，再平均其余两分，最后按权重汇总，原创性的权重最高。人类代表性论文提供评分参照，并非人类与 agent 在同一时限下比赛。一项初步人工研究检查了 100 对计算机科学假设，评审模型与人工多数意见的一致率为 77%（Cohen kappa 0.55）；这不能验证其他学科的评分。论文还检查 rubric 校准、重放对照，以及工具协议错误的数量。目标文献晚于几乎所有被测模型的知识截止日期，但并不保证每个模型都满足这一条件。

## Typical Duration

Active 最多进行十次 search/fetch 调用，生成上限为 6,000 token。未报告统一的实际运行时长。调用上限不等于按价格计分的成本指标。

## Main Contribution

在输出和评分保持一致的条件下，比较由评测者提供文献与由 agent 自行收集文献，并要求原创性判断有检索证据。

## Key Design Ideas

- 两种文献获取设置使用相同的提案格式和评审方法。
- 将 agent 检索到的文献按 Static 格式重新提供，区分文献内容与检索过程的影响。
- 用代表性论文校准评审，并检查不连贯或套模板的提案。

## Strengths

- 区分基准覆盖的全部任务与实际密集评分的子集。
- 在模型差异之外，同时报告对照实验和评分边界。

## Limitations

- 分数仍由模型判断，假设没有经过实验验证。
- Active 同时改变了检索控制、多轮交互和工具使用。
- 探索性的 Scientific World Modeling 收益未能同时通过多重比较校正和算力匹配对照。

## Related Works

- [IdeaBench](./ideabench.md)
- [LiveIdeaBench](./liveideabench.md)
