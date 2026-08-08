# PDEAgent-Bench (2026)

> [English](../../works/pdeagent-bench.md) | **简体中文**

## Overview

PDEAgent-Bench 是多指标、多库的 PDE 求解器生成 benchmark：645 个实例横跨 6 个数学类别与 11 个 PDE 族，面向常用有限元库 DOLFINx、Firedrake 与 deal.II，采用分级评估——生成的求解器须依次通过可执行性、数值精度与计算效率检查。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.09636>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

每个实例提供一份面向 agent 的问题规格，模型须为三个 FEM 库之一产出求解器代码。分级评估把阶梯摆明：能跑的代码不等于准确的代码，准确的代码也未必高效——求解器要在规定的评估网格上对照参考解，满足按算例设定的精度与运行时目标。核心发现：模型往往能产出可运行的代码，但一旦强制执行精度与效率要求，通过率就大幅下滑。

## Tasks

645 个「PDE 到求解器代码」实例，横跨 6 个数学类别与 11 个 PDE 族，各面向 DOLFINx、Firedrake 或 deal.II。

## Domains

数值 PDE 与有限元方法，覆盖三个生产级 FEM 库。

## Evaluation

- 分级检查：可执行性 → 数值精度（在规定评估网格上对照参考解，按算例设定目标）→ 计算效率（运行时目标）。
- **报告。** 模型往往能产出可运行代码，但强制精度与效率要求后通过率大幅下滑。

## Typical Duration

每个实例为「规格到求解器」的生成，配自动分级检查。

## Main Contribution

为 LLM 生成的 PDE 求解器把「能跑」「算得对」「跑得快」分成三关，且横跨多个 FEM 库而非单一工具链。

## Key Design Ideas

- 分级门的结构把失败定位到执行、精度或效率。
- 三个 FEM 库让针对特定库的记忆现出原形。
- 按算例设定的精度与运行时目标取代一刀切的阈值。

## Strengths

- 本仓库记录的最大固定求解器生成套件（645 实例、11 个 PDE 族）。
- 「可运行但不准确」的落差恰好量化了从业者最担心的失败模式。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [CodePDE](./codepde.md) — 把 LLM 求解器生成确立为评估对象的框架。
- [MooseBench](./moosebench.md) — 同样验证生成的模拟代码是否求解了预期的物理，通过 PDE 重构。
- [FEM-Bench](./fem-bench.md) — 同样是 FEM 代码生成，在研究生课程粒度上做客观验证。
