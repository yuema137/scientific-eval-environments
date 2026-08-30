# Curation-Bench (2026)

> [English](../../works/curation-bench.md) | **简体中文**

> **首次公开：** 2026-06-02 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.04261)

## Overview

Curation-Bench 测试 generalist coding agent 能否在模型、训练 recipe 和 eval suite 固定时，通过反复 train、evaluate、revise 改进训练数据策略。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Data Curation](../topics/evaluation_driven_data_curation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.04261>
- **Venue:** arXiv preprint (2026)

## Summary

Agent 检查候选 dataset，通过 CLI 实现 selection policy，把策略交给固定的 vision-language instruction-tuning pipeline，再根据 evaluation result 修改，最多进行十轮。普通 agent 能追上已有的强 baseline，但大多只在局部调参；要求每轮引用并改造既有方法的 scaffold 能扩大探索范围，最终得到一套只用十分之一数据预算、但超过强 baseline 的策略。

## Tasks

面向 vision-language instruction tuning 的开放式数据策略研究。每次运行都修改可执行的 curation code，并反复调用同一训练和下游评估 pipeline；被测 artifact 是选出的数据子集及其生成策略。

## Domains

AI 与 ML 研究，具体是多模态 instruction-tuning 数据选择。

## Evaluation

固定 base model、recipe 和 suite，比较每个数据子集训练出的模型在 downstream benchmark 上的表现。系统跟踪最多十轮的变化，并与已有 selection baseline、数据预算和不同 scaffold 条件比较；trajectory 分析还区分局部调优和新方法族探索。

## Typical Duration

每次运行最多十轮 train–evaluate–revise；论文比较数据预算，没有给出统一墙钟上限。

## Main Contribution

将 downstream evaluation feedback 直接作为自动数据研究的控制信号。

## Key Design Ideas

- 固定模型、recipe 和 evaluator，只让 curation policy 改变。
- 用通用 coding agent 可操作的 CLI 暴露完整 loop。
- 比较开放 prompt 与要求引用、改造方法的 scaffold。
- 同时评价最终下游质量和 trajectory 中体现的研究行为。

## Strengths

- 受控 pipeline 能把提升归因到数据策略。
- 多轮迭代使 evaluation 成为 active feedback，而非终局报告。
- 数据预算比较同时反映效率与质量。

## Limitations

- 当前只覆盖一种 VLM instruction-tuning 设置。
- 训练成本限制了重复次数和策略探索规模。
- Scaffold 条件下的成功不能证明 agent 已具备开放式自动研究能力。

## Related Works

- [PostTrainBench](./posttrainbench.md)
- [SkillCoach](./skillcoach.md)
- [MLE-bench](./mle-bench.md)
