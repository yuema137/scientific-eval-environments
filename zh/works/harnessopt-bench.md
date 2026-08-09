# HarnessOpt-Bench (2026)

> [English](../../works/harnessopt-bench.md) | **简体中文**

## Overview

HarnessOpt-Bench 是度量前沿 LLM 自动化 harness 优化能力的 benchmark——在可信执行环境内、固定的目标评估预算下，迭代改进围绕 LLM 的提示词、工具、控制流与编排代码。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.06301>
- **Venue:** arXiv preprint, 2026

## Summary

每个优化器模型获得种子 harness、评估反馈与固定的目标评估预算，按其在留出测试划分上相对种子的归一化增益计分。可信执行环境强制评估边界、计量资源使用，并保存候选版本以供审计。在 4 个下游任务、5 个前沿优化器模型、共 111 次计分运行中，论文报告：优化器模型之间的差异大于它们所借助的编码 harness 之间的差异，且增益随任务与种子设定的不同而差异显著。

## Tasks

4 个下游任务；5 个前沿 LLM 作为优化器受评；共 111 次计分运行。每次运行从种子 harness 出发，在固定目标评估预算下获得评估反馈。

## Domains

Agent 系统的 harness 优化；无单一科学领域。

## Evaluation

- 在留出测试划分上**相对种子 harness 的归一化增益**。
- 可信执行环境强制评估边界、计量资源使用，并保存候选版本以供审计。
- **报告。** 优化器模型之间的差异大于其所借助的编码 harness 之间的差异；增益随任务与种子设定的不同而差异显著。

## Typical Duration

以固定目标评估预算为界的迭代优化–评估循环。

## Main Contribution

在受审计、预算受限的评估下把 LLM 作为 harness 优化器进行考核，表明优化器模型比其操作的 harness 更能拉开差距。

## Key Design Ideas

- 评估预算是稀缺资源；优化能力按每次评估的产出来衡量。
- 留出测试划分把真实的 harness 改进与对反馈信号的过拟合分开。
- TEE 强制计量使资源使用与候选历史可审计。

## Strengths

- 直接度量其他 benchmark 只能间接暗示的能力（自我改进的脚手架）。
- 可审计留痕的基础设施，防止靠信息泄漏取得优化增益。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- 摘要未报告绝对性能数字；逐任务数字为 TODO(reference)。

## Related Works

- [VeRO / VeRO-Bench](./vero.md) — 同样在硬性评估调用预算下考核优化其他 agent 的 agent；HarnessOpt-Bench 增加了 TEE 审计执行与留出增益计分。
- [Harness-Bench](./harness-bench.md) — 同样把 harness 作为研究变量，但采取固定任务、变换 harness 而非优化 harness。
- [GATE](./gate.md) — 同样研究 agent 脚手架组件的演化，面向工具图而非整个 harness。
