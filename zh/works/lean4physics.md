# Lean4Physics / LeanPhysBench (2025)

> [English](../../works/lean4physics.md) | **简体中文**

## Overview

Lean4Physics（Lean4PHYS）是大学物理在 Lean4 中的推理框架，贡献了 LeanPhysBench——200 条手工编写、经同行评审的形式化物理命题，取材于大学教材与物理竞赛题——以及 PhysLib，一个社区驱动的、收录形式化物理推理所需单位制与定理的基础仓库。论文称这是首个 Lean4 物理 benchmark。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.26094>
- **Venue:** ICLR 2026

## Summary

LeanPhysBench 把物理评估搬进形式化证明助手：解题意味着给出被 Lean4 内核接受的证明，正确性由机器检查而非评判。由于形式化物理需要数学库所缺少的基础设施——单位制、物理定理——论文同时构建了 PhysLib 作为地基。在专业数学 Lean4 证明器与最先进闭源模型上，最佳成绩分别为 16%（DeepSeek-Prover-V2-7B）与 35%（Claude-Sonnet-4）；PhysLib 平均带来 11.75% 的提升。

## Tasks

200 条手工编写、经同行评审的 Lean4 物理命题，取材于大学教材与物理竞赛题；静态定理证明评估。

## Domains

以 Lean4 形式化命题呈现的大学物理；子领域构成摘要未说明。

## Evaluation

- Lean4 证明成功与否——正确性由证明助手确立，全程无 judge 介入。
- **报告。** 最佳成绩：DeepSeek-Prover-V2-7B 为 16%，Claude-Sonnet-4 为 35%；PhysLib 平均提升 11.75%。

## Typical Duration

单命题形式化证明；非交互式 agent 设定。

## Main Contribution

把内核校验的形式化验证引入物理评估，并补齐了让形式化物理「可证」的基础库（单位制与基础定理）。

## Key Design Ideas

- 以证明助手为判分者，把 judge 带来的误差从物理评估中彻底移除。
- PhysLib 把物理基础设施（单位、基础定理）当作可复用的一等公民。
- 命题经同行评审，形式化本身的忠实性也被检查。

## Strengths

- 最严格的验证标准：证明要么通过内核，要么不通过。
- 实测的基础库效应（+11.75%）表明形式化物理的难度有多少来自基础设施缺失。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [FormalRewardBench](./formalrewardbench.md) — 同样以 Lean 4 验证为真值，用于测试奖励模型的证明偏好。
- [Hard2Verify](./hard2verify.md) — 同样以验证为中心的前沿难度评估，通过专家为非形式化证明逐步打标。
- [MATP](./matp.md) — 同样把步骤裁决交给形式化机制，通过自动形式化到一阶逻辑。
