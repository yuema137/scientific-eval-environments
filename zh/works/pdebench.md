# PDEBench (2022)

> [English](../../works/pdebench.md) | **简体中文**

## Overview

PDEBench 是科学机器学习在时变 PDE 上的经典 benchmark 套件：覆盖对流、Burgers、反应扩散、扩散吸附、Darcy 流、浅水方程与可压缩/不可压缩 Navier–Stokes 的即用数据集，含正问题与反问题任务，基线包括 FNO、U-Net 与 PINN。它评估的是科学 ML 代理模型而非 LLM agent（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2210.07182>
- **Code:** <https://github.com/pdebench/PDEBench>
- **Dataset:** <https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/darus-2986>
- **Venue:** NeurIPS 2022 Datasets and Benchmarks

## Summary

PDEBench 把 SciML 评估从寥寥几个玩具方程拓宽开来：更广的 PDE 范围、更大的即用数据集，且在多种初始条件、边界条件与 PDE 参数下含多次模拟（据官方仓库：1D 对流、Burgers、反应扩散、扩散吸附；2D 扩散反应、Darcy 流、浅水、不可压缩 Navier–Stokes；可压缩 Navier–Stokes）。模型在该套件提出的新评估指标下，同时对照经典数值模拟与 ML 基线比较，并有可扩展 API 供新增任务。

## Tasks

上述九个方程族的时变 PDE 模拟数据集上的正问题与反问题学习任务；非 LLM 的代理模型训练与评估。

## Domains

计算物理：从对流、Burgers 到浅水与 Navier–Stokes 流动的经典 PDE 族。

## Evaluation

- 在套件提出的指标下对照经典数值模拟与 ML 基线（FNO、U-Net、PINN、梯度式反演方法）比较；指标定义为 TODO(reference)。
- **报告。** 摘要未给出标志性数字；该套件的角色是标准化比较。

## Typical Duration

N/A——固定数据集上的离线代理模型训练与评估；非 agent 设定。

## Main Contribution

PDE 代理模型学习的参照评估基座——后来 LLM 求解器 benchmark（以及本仓库 RealPDEBench 一类的卡片）都以它为坐标系。

## Key Design Ideas

- 参数、初始条件与边界条件的变化内建于数据集，而非留给用户。
- 正问题与反问题共存于同一套件、同一 API。
- 基线加预训练模型让比较开箱即可复现。

## Strengths

- 经典地位：PDE 代理模型评估的共同语言。
- 数据与代码可扩展、许可宽松。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: PDEBench 评估的是科学 ML 代理模型而非 LLM agent；收录为 agentic 求解器生成 benchmark 所依托的经典 PDE 套件参照点。

## Related Works

- [RealPDEBench](./realpdebench.md) — 真实数据的后继者：把测量与模拟配对，适用同一类注意事项。
- [CodePDE](./codepde.md) — 在 LLM 求解器生成评估中取用 PDEBench 的问题族。
- [The Well](./the-well.md) — 大规模、多领域的物理模拟数据姊妹集合。
