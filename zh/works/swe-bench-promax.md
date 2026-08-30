# SWE-Bench ProMax (2026)

> [English](../../works/swe-bench-promax.md) | **简体中文**

> **首次公开：** 2026-08-10 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.09802)

## Overview

SWE-Bench ProMax 是一个专家整理的多语言代码重构 benchmark，含 170 个来自真实提交的实例，横跨七种编程语言，用于考察 coding agent 在跨多文件、协同且保持行为不变的改动上的能力。

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — 通用软件工程（多语言代码重构）benchmark；作为一般应用软件工程而非科学/工程软件被排除。

## Links

- **Paper:** <https://arxiv.org/abs/2608.09802>
- **Venue:** COLM 2026（arXiv 备注：「Published as a conference paper at COLM 2026」）

## Summary

SWE-Bench ProMax 瞄准代码重构——跨多文件、协同且保持行为不变的改动——作者认为相较正在迅速饱和的既有 issue 解决 benchmark，它是对 agent 能力更难、更贴近现实的检验。它由取自真实提交、横跨七种编程语言（Python、Java、TypeScript、Go、C、C++、Rust）的 170 个实例构成。每个实例都经过多阶段整理流程，以解决先前 benchmark 中发现的质量问题：issue 描述从零重写，以提供精确无歧义的规格；测试套件经人工评审，剔除过窄测试（会否掉正确解）与过宽测试（会检查未言明的需求）。复杂度不足或跨文件范围有限的任务被过滤掉，从而得到大规模重构任务，平均每个实例改动 11.4 个文件、261.6 行代码。

## Tasks

170 个代码重构实例，取自真实提交，横跨七种编程语言：Python、Java、TypeScript、Go、C、C++、Rust。每个任务都要求跨多文件做协同且保持行为不变的改动。任务平均每个实例改动 11.4 个文件、261.6 行代码。实例由多阶段整理流水线产生：(a) issue 描述从零重写以获得精确无歧义的规格；(b) 测试套件经人工评审，剔除过窄与过宽测试；(c) 过滤掉复杂度不足或跨文件范围有限的任务。逐语言的确切实例分布与完整的整理流程为 TODO(reference)。

## Domains

软件工程——横跨七种编程语言（Python、Java、TypeScript、Go、C、C++、Rust）的真实世界多语言开源仓库。

## Evaluation

基于执行：agent 以解决率（被解决实例的比例）计分，对照实例经人工评审的测试套件——这些套件经整理，使正确的、保持行为不变的重构能通过，而过窄或过宽测试被剔除。前沿模型在两种 agent 脚手架下评估；最佳模型的解决率仅为 41.2%。所评估的具体模型、确切的通过/失败判据与两种 agent 脚手架为 TODO(reference)。

## Typical Duration

TODO(reference)。论文以编辑规模刻画任务量级——平均每个实例改动 11.4 个文件、261.6 行代码——但摘要未给出逐任务的步数、wall-clock 或 token 预算。

## Main Contribution

引入一个多语言、专家整理的大规模代码重构任务 benchmark，其整理直接针对先前软件工程 benchmark 中发现的质量问题（有缺陷的过窄/过宽测试、含糊的 issue 规格），以超出既有 benchmark 的规模，提供一个更难、更不饱和的 coding-agent 能力检验。

## Key Design Ideas

- 以重构——跨文件、协同且保持行为不变的改动——作为评估目标，而非单一 issue 的缺陷修复。
- 横跨七种编程语言（Python、Java、TypeScript、Go、C、C++、Rust）的多语言覆盖。
- 多阶段整理：issue 描述从零重写以获得精确规格，测试套件经人工评审剔除过窄与过宽测试，并过滤掉低复杂度或窄范围任务。
- 由构造决定的大规模任务（平均每个实例改动 11.4 个文件、261.6 行代码）。

## Strengths

- 整理明确针对测试质量缺陷（会否掉正确解的过窄测试；会检查未言明需求的过宽测试）——先前一项审计报告这类缺陷在 SWE-bench Verified 大量未解实例中存在。
- 由设计即多语言且大规模，超出先前 issue 解决 benchmark 的逐实例编辑量级。
- 报告的余量很低（最佳模型解决率 41.2%），表明该 benchmark 远未饱和。

## Limitations

- Repository note: 170 个实例的规模相对较小；逐语言覆盖及其平衡此处未经核验（TODO(reference)）。
- Repository note: 所评估的具体模型、agent 脚手架与确切的评分 harness 未在摘要中给出，仍未经核验（TODO(reference)）。

## Related Works

- [SWE-bench](./swe-bench.md) — 更早的真实 GitHub issue 解决 benchmark；ProMax 针对其饱和与所报告的测试质量问题定位，并把任务转向多语言重构。
- [SWE-Interact](./swe-interact.md) — 同为软件工程 agent benchmark，聚焦交互式、逐步细化的需求，而非大规模重构。
- [SWE-Together](./swe-together.md) — 同为仓库级软件工程 agent 评估，聚焦人–agent 协作。
- [FrontierCode](./frontiercode.md) — 同为强调整理质量的高难度真实仓库 coding-agent benchmark。
