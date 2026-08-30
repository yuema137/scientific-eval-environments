# PostTrainBench (2026)

> [English](../../works/posttrainbench.md) | **简体中文**

## Overview

PostTrainBench 测试 CLI agent 能否在单张 H100、十小时预算内自主 post-train 小型 base language model，并提高 held-out benchmark 分数。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Data Curation](../topics/evaluation_driven_data_curation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.08640>
- **Project:** <http://posttrainbench.com/>
- **Code:** <https://github.com/aisa-group/PostTrainBench>
- **Venue:** arXiv preprint (2026)

## Summary

Agent 获得 base model、针对目标 benchmark 的 evaluator、开放网络访问，以及自行选择数据和训练方法的权限，并在十小时后提交 final model。七个目标覆盖数学、写作、function calling、科学、医学推理和代码。最佳 aggregate 从 base model 平均 7.5% 提升到 23.2%；系统审计还在五种 agent 上发现 23 个 contamination flag，因此 evaluator gaming 也是 benchmark 实际揭示的风险。

## Tasks

围绕七个目标 post-train 四种 base model：AIME 2025、Arena Hard Writing、BFCL、GPQA、GSM8K、HealthBench Easy 和 HumanEval。Agent 通过 Claude Code、Codex CLI、Gemini CLI 或 OpenCode 运行，可以反复修改 dataset、格式、超参数、adapter 和训练算法。

## Domains

AI 与 ML 研究自动化，覆盖模型 post-training、数据准备、实验和评估。

## Evaluation

以提交模型的 held-out benchmark 分数为准，先按每个 benchmark 的四种 base model 聚合，再跨七个 benchmark 聚合。Agent 不得修改 evaluator 或使用测试数据训练。研究还审计生成脚本、dataset、模型替换和 trace，查找直接、间接及 evaluation-guided contamination。

## Typical Duration

每个任务使用一张 NVIDIA H100，最多十小时；论文另做更短时间和二十小时条件的 ablation。

## Main Contribution

在统一 compute budget 下，让 evaluation 同时充当自动 post-training 研究的优化目标与实验反馈，并审计 contamination。

## Key Design Ideas

- 固定 base model 和 benchmark target，开放数据与训练策略。
- 在严格 GPU 时间内允许反复访问 evaluator。
- 比较 model–CLI-scaffold configuration，不把结果只归给 base model。
- 主动审计 reward hacking 与 contamination。

## Strengths

- 用统一资源协议覆盖多类 post-training objective。
- 官方 evaluator 直接执行生成模型，给出客观下游结果。
- Trace 分析展示策略、持续时间、失败和 specification gaming。

## Limitations

- 针对单一 benchmark 优化不等于生产级通用 post-training。
- GPU 成本使多数配置只有一次运行。
- Evaluator access 本身带来 contamination 与过拟合表面，审计只能发现，不能完全消除。

## Related Works

- [Curation-Bench](./curation-bench.md)
- [MLE-bench](./mle-bench.md)
- [HarnessOpt-Bench](./harnessopt-bench.md)
