# HARDMath (2024)

> [English](../../works/hardmath.md) | **简体中文**

> **首次公开：** 2024-10-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2410.09988)

## Overview

HARDMath 是应用数学难题的 benchmark 数据集——研究生渐近分析课程中的解析近似技术——问题自动生成、解对照数值真值验证，另有 40 道应用科学情境的应用题；其 HARDMath-mini 测试集含 366 题。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.09988>
- **Code:** <https://github.com/sarahmart/HARDMath>
- **Venue:** arXiv preprint (cs.LG, cs.AI), 2024

## Summary

应用数学的日常是近似：知道哪种渐近技术适用，并把它算到底。HARDMath 规模化地自动生成这类问题，并把每个解对照数值真值验证——既绕开专家出题的标注瓶颈，又保持答案可检验。在少样本思维链提示下，即便 GPT-4 这样的领先闭源模型在 HARDMath-mini 上也只有 43.8% 的总体准确率，论文的错误分析进一步描绘了近似推理在何处断裂。

## Tasks

需要解析近似技术的自动生成应用数学问题，解对照数值真值验证；HARDMath-mini 测试集 366 题，另有 40 道应用科学应用题；静态解题。

## Domains

应用数学：研究生课程水平的渐近方法与解析近似技术。

## Evaluation

- 对照经数值验证的真值解计算准确率，采用少样本思维链提示，并附详细错误分析。
- **报告。** GPT-4 在少样本思维链下总体准确率仅 43.8%。

## Typical Duration

单题推导；非交互式设定。

## Main Contribution

把「近似」而非「精确求解」立为受测的数学技能，其自动生成管线靠数值验证保证生成问题可信。

## Key Design Ideas

- 自动生成加数值验证在不牺牲可检验性的前提下扩大题目供给。
- 渐近分析瞄准精确答案 benchmark 从不触及的应用数学推理。
- 应用题把技术连接到应用科学情境。

## Strengths

- 少见的近似推理 benchmark——这是 PDE 与物理建模实践的基本功。
- 发布时 GPT-4 43.8% 的上限留有明确空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。完整（非 mini）数据集规模在已验证来源中未说明。

## Related Works

- [TPBench](./tpbench.md) — 同样是可自动验证、从研究生到研究级的评估，在理论物理。
- [CMPhysBench](./cmphysbench.md) — 同样以推导为中心并配定制判分，在凝聚态物理。
- [PDE-Controller](./pde-controller.md) — 同样是面向 PDE 系统的应用数学推理，取向为控制。
