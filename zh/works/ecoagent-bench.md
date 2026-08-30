# EcoAgent-Bench (2026)

> [English](../../works/ecoagent-bench.md) | **简体中文**

> **首次公开：** 2026-08-06 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.05519)

## Overview

EcoAgent-Bench 是面向预算受限 LLM agent 经济决策的 benchmark：每个任务都指定带定价的动作与显式预算，评分对象是决策是否经济合理，而不仅是任务是否完成。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — 评估的是 agent 的元属性（成本、安全性或鲁棒性），而非科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.05519>
- **Venue:** arXiv preprint, 2026

## Summary

EcoAgent-Bench 包含 304 个源自真实数据的任务，分五个族，改编自 GAIA、HotpotQA 与 MuSiQue，考察四类决策：避免不必要的升级、需要时升级、选择模型档位、在前提不成立时停止。经济一致性分数比较升级导向与节省导向两组任务上的表现，从而暴露一味花钱或一味省钱的单边策略。

## Tasks

304 个源自真实数据的任务，分五个族，改编自 GAIA、HotpotQA 与 MuSiQue；每个任务指定带定价的动作与显式预算，并对应四类决策之一（避免不必要升级、需要时升级、选择模型档位、前提不成立时停止）。

## Domains

跨多个知识领域的问答（改编自既有 QA benchmark）；无单一科学领域。

## Evaluation

- 微平均准确率与严格成功率。
- **经济一致性分数**对比升级导向与节省导向任务组，使一味升级（或从不升级）的策略无法得高分。
- 在 tool-API 与 workspace-CLI 两种设定下评估七个 LLM agent，外加四个脚本化 oracle 对照。
- **报告。** Tool-API agent 的微平均严格成功率仅 3.9–24.0%，经济一致性至多 7.3%；预算扫描中 GPT-5.4 的升级率仅从 0% 变到 3%。

## Typical Duration

带定价动作的预算化 QA 回合；单任务预算由任务指定。

## Main Contribution

把 agent 决策的经济合理性——而不仅是预算上限下的任务成功——作为度量对象，用成对任务组暴露单边花钱策略。

## Key Design Ideas

- 带定价的动作加显式预算，使每一步都成为经济决策。
- 升级/节省成对分组使经济一致性可度量，且无法被恒定策略钻空子。
- 脚本化 oracle 对照给出理性策略的可达上界。

## Strengths

- 表明 agent 对预算变化几乎无感（扫描中升级率仅 0% → 3%）。
- 严格成功与经济一致性共同揭示当前 agent 两头都不及格。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [CostBench](./costbench.md) — 同样评估成本最优的 agent 决策，但面向动态定价的旅行规划。
- [BAGEN](./bagen.md) — 同样把预算作为在线决策信号，通过逐轮预算区间预测。
- [CATP-LLM](./catp-llm.md) — 同样为动作定价以做成本感知规划，面向工具执行计划。
