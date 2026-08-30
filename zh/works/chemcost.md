# ChemCost (2026)

> [English](../../works/chemcost.md) | **简体中文**

> **首次公开：** 2026-05-08 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.07251)

## Overview

ChemCost 问的是 agent 能否给一个反应定价：1,427 个可评估反应锚定在一份冻结的价格快照上（2,261 种化学品、230,775 条供应商报价），agent 必须确定化学品身份、检索报价、选出可购买的有效包装、归一化数量并计算成本——最强的 agent 在干净输入下也只有 50.6% 的答案落在 25% 相对误差内。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.07251>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

给一条合成路线算成本，是化学里再平常不过、却容不得半点差错的活儿：身份确定、报价检索、包装选择、数量归一化、算术——每一步都必须做对。ChemCost 冻结一份价格快照，使真值精确且无需 judge；评测覆盖前沿、开源权重与化学专用的 LLM agent，并逐阶段诊断失败。最好的 agent 在干净输入下 50.6% 的答案落在 25% 相对误差内，而在受控噪声注入——扰动化学品别名、数量表达、缺失字段与输入格式——之后显著退化。

## Tasks

1,427 个反应定价任务，基于冻结快照（2,261 种化学品、230,775 条供应商报价）；工具调用式的交互回合，覆盖身份确定、检索、采购选择与成本计算，另有一组噪声注入下的鲁棒性评测。

## Domains

化学——作为实际合成规划一环的化学品采购与成本估算。

## Evaluation

- 冻结快照给出的精确、无 judge 真值；标量成本评分，配有对身份确定、检索、采购与算术四个阶段的失败诊断。
- **报告。** 最强 agent：干净输入下 50.6% 落在 25% 相对误差内；真实感噪声下显著退化。

## Typical Duration

每个反应一段多步工具调用回合（确定身份 → 检索 → 选择 → 归一化 → 计算）。

## Main Contribution

把「对化学本身的经济推理」变成被测任务——冻结的市场快照让成本问题第一次有了现实世界里从不存在的精确真值。

## Key Design Ideas

- 冻结价格快照把一个移动靶任务变成可复现的 benchmark。
- 阶段级诊断把失败归因到管线环节，而不只看最终数字。
- 噪声注入这一组设定所测的鲁棒性，正对应真实采购数据固有的那种脏数据问题。

## Strengths

- 在定价这个通常无法验证的领域给出了无 judge 的标量真值。
- 干净与含噪的差距量化了干净 benchmark 分数掩盖的脆弱性。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要之外的细节有待全文校验。论文 arXiv 页面上无法核实任何代码或数据集发布。

## Related Works

- [EcoAgent-Bench](./ecoagent-bench.md) — 同样考 agent 的经济决策，基于有价动作与预算。
- [SDBench](./sdbench.md) — 同样在成本维度上为 agent 计分，沿准确率-成本前沿。
- [SMDD-Bench](./smdd-bench.md) — 同样是资源受限的多步分子任务，通过 oracle 调用预算实现。
