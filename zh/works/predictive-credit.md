# Predictive Credit (2026)

> [English](../../works/predictive-credit.md) | **简体中文**

> **首次公开：** 2026-09-29 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.00314)

## Overview

很多研究型 agent 的 benchmark 会给 agent 写出的解释打分，可 judge 光读解释，分不清它是真带来了信息，还是只是听上去有道理。Predictive Credit 不靠阅读，改用预测来检验。一个固定的 LLM 预测器要预测某项计划干预的实测效果，并且分三种条件各预测一次：只给普通描述；附上该状态自己的解释；附上另一个状态的解释（称为 donor）。只有当解释让预测损失同时低于“只给描述”和“给 donor 解释”两种条件时，解释才算有贡献。判定规则在看到结果之前就已冻结，另外用一条研究者手写的机制说明作为阳性对照。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — 这是一种给解释打分的评测方法，不评测 agent 完成科学任务的能力。

## Links

- **Paper:** [Predictive Credit: Measuring What Scientific Explanations Add to Experimental Forecasts](https://arxiv.org/abs/2610.00314)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.00314v1>
- **Venue:** arXiv 预印本（cs.AI，2026）
- **Code:** 论文提到一份匿名补充材料和代码仓库，但没有给出链接。TODO(reference)

## Summary

每个状态由一个公开的实验设置和一项计划中的干预组成；要预测的是留出的子实验相对父实验在某个结果指标上的变化，预测器始终看不到这个结果。对每种条件 c，协议计算风险 R_c = E[ℓ(f(c_i), y_i)]，并报告 G_description = R_D − R_M（描述对比匹配解释）和 G_alignment = R_S − R_M（donor 对比匹配解释），数值为正说明匹配解释更好。比如一个 Tox21 状态，在每种条件下都会得到两次独立的 ROC AUC 变化预测，再拿区间得分和事先冻结的伤害阈值比较。三个设置下，冻结规则给出的结论不是“不确定”就是“不成立”。作者的结论是：在测试过的 donor 分辨率下，自然语言解释的预测贡献没有得到证实；不过研究者手写的机制说明确实降低了点预测误差。

## Tasks

N/A — 方法论文。协议应用于 336 个前瞻性状态（3,708 个前瞻性预测位置），分布在三个设置和一个阳性对照中：

- **Controlled v5：** 来自一个合成学习环境的 120 个状态，包含六种 ML 设定，预测目标是准确率和 log-loss。
- **Tox21 锚点：** 72 个状态（12 个终点 × 3 种标注预算 × 2 个种子），数据来自 MoleculeNet 的分子测定，模型为 logistic 回归。
- **OpenML v2.1：** 来自 24 个任务（12 个 CC18 分类任务、12 个 CTR23 回归任务）的 144 个状态，使用 LightGBM 流水线和六种干预。
- **机制阳性对照：** 40 个配对任务，真实说明会透露一个隐藏的二次函数形式。

## Domains

这些设置都是机器学习实验：一个合成学习环境、Tox21 分子毒性测定和 OpenML 表格任务。协议针对的是一般意义上的实验结果预测，不局限于某个科学领域。

## Evaluation

- **指标：** 点预测 MAE、方向准确率、80% 区间的覆盖率和宽度、区间得分 IS80，以及两次独立预测之间的重复漂移 |ŷ₁ − ŷ₂|。
- **冻结判定：** v5 为 “inconclusive”；Tox21 和 OpenML 为 “confirmation_no_go”。Tox21 的规则要求：匹配减对照的估计值 ≥ .005 且单侧下界为正，至少 8 个终点和 4 种干预同时为正，并且每一层的提取完整度 ≥ .95。bootstrap 是分层做的；部分对比属于探索性分析，没有做多重比较校正。
- **Controlled v5：** 准确率 MAE（描述减匹配）为 +.071 pp [−.102, +.252]；log-loss MAE 为 +.0363 [−.0061, +.0807]。
- **Tox21（DeepSeek V4 Pro）：** ROC AUC 区间得分（描述减匹配）为 −.002628 [−.017392, +.010375]，阈值是 .005。重复漂移在只给描述时是 .01004，给匹配解释时降到 .00357，给 donor 解释时为 .00411；点预测 MAE 分别是 .02056、.02041 和 .02023。
- **Tox21 Flash 重跑：** 漂移从 .00704 降到 .00278（匹配）和 .00288（donor），但匹配条件下的点预测 MAE 从 .01823 升到 .02020；匹配减 donor 的区间得分为 .003268 [−.008096, .014485]，结论是 “replication_not_supported”。
- **OpenML：** 给完整解释卡片后，平均区间宽度从 .06179 增加到 .07474，覆盖率却是 49.3%，只给描述时为 51.4%；144 个状态中只有 66 个的卡片不为空。点预测 MAE（描述减匹配）为 −.00741 [−.02804, +.00251]。
- **阳性对照（240 次 Flash 预测）：** 点预测 MAE 在真实说明下为 3.795，只给描述为 6.391，给错误说明为 8.151；真实说明比只给描述好 2.596 [2.314, 2.880]。
- Repository note：在 Tox21 上，匹配解释和 donor 解释带来的漂移下降幅度差不多，所以漂移下降本身并不能说明预测器用上了解释的内容。

## Typical Duration

调用通过 Claude CLI 会话发往 DeepSeek 兼容 Anthropic 接口的端点。按记录还原的 API 花费：v5 为 6.01 美元，Tox21 Pro 为 2.87 美元，Tox21 Flash 重跑为 0.50 美元，OpenML 为 9.59 美元。

## Main Contribution

提出一种配对预测协议：把解释的价值定义为它帮预测减少了多少损失，同时与普通描述和 donor 解释两种条件对比，并在结果揭晓前冻结判定规则。

## Key Design Ideas

- donor 条件把内容和形式分开：donor 解释来自另一个状态，形式相同，所以匹配解释如果胜过它，功劳可以归到解释的内容上。
- donor 的分辨率是受控的：Tox21 和 OpenML 在同一任务、同一预算、同一干预的单元里互换种子，v5 则用不同的干预。
- 按 intention-to-treat 原则分析；调用次数用尽时给出确定性的兜底预测，而不是直接剔除。
- 用研究者手写的机制说明检查：当解释真的带有信息时，协议能不能识别出来。

## Strengths

- 阴性和不确定的结果都按事先定好的规则报告，没有事后改口。
- 阳性对照表明预测器确实会对解释内容做出反应：真实说明降低误差，错误说明提高误差。
- 区间宽度、覆盖率和漂移分开报告，能看出漂移下降和点预测准确率没有提升可以同时出现。

## Limitations

- 作者说明，在测试过的 donor 分辨率下，自然语言解释的预测贡献没有得到证实。
- OpenML 上引导提取的完整度为 60.42%，低于 .95 的门槛。
- 完整卡片带来的漂移变化幅度在几次 Flash 运行之间不一致；区间变宽的同时覆盖率仍然不足。
- 作者指出，OpenML 的误差很大一部分来自一个任务（brazilian_houses）。
- 阳性对照由研究者自己编写。
- 返回的 API 包装结果没有记录实际调用的模型 ID。

## Related Works

- [AutoResearchEval](./autoresearcheval.md) — 同样关心评测者对研究型 agent 产出的判断能否信任，但用的是人工标注而不是预测。
- [EurekaBench](./eurekabench.md) — 对提交的机制打分时，部分依据是它对留出数据的预测效果。
