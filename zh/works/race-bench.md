# RACE-Bench (2026)

> [English](../../works/race-bench.md) | **简体中文**

> **首次公开：** 2026-03-27 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2603.26337)

## Overview

RACE-Bench 是一个推理增强的 benchmark，用于评估仓库级代码 agent 在真实特性新增任务上的表现；它将可执行的补丁验证与结构化的中间参考推理配对，从而不仅按最终测试正确性考察 agent，还考察其推理与开发者认可轨迹的契合程度。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 通用型仓库级软件工程（特性新增）benchmark；作为一般应用软件工程排除在外。

## Links

- **Paper:** <https://arxiv.org/abs/2603.26337>
- **Venue:** arXiv preprint (cs.SE), submitted March 2026

## Summary

RACE-Bench 针对仓库级代码 agent 评估中的一处空缺：现有 benchmark 只按最终测试正确性把 agent 当作黑盒评判，对其如何推理、失败出在何处几乎没有洞察。该 benchmark 含 528 个真实特性新增实例，取自 12 个开源仓库。每个实例配一套可执行的补丁验证与结构化的中间参考推理，涵盖 issue 理解、文件定位、实现任务与步骤分解。在此之上，RACE-Bench 定义了一套双轨评估框架，联合度量补丁正确性与 agent 中间推理同开发者认可参考轨迹的契合度。作者评估三个有代表性的仓库级代码 agent，报告各 agent 的 Resolved Rate 从 29% 到 70% 不等，并发现当 agent 把高层意图转化为具体实现步骤时，推理质量下降得最厉害。

## Tasks

来自 12 个开源仓库的 528 个真实特性新增实例。每个实例携带 (a) 一套可执行的补丁验证 harness，以及 (b) 分解为 issue 理解、文件定位、实现任务与步骤分解的结构化中间参考推理。任务为仓库级特性新增——实现一项新特性使相关测试通过。具体的 12 个仓库、按仓库的实例分布，以及参考推理的构建/整理流水线为 TODO(reference)。

## Domains

Software & Systems — 横跨 12 个真实开源软件仓库的仓库级特性新增。

## Evaluation

双轨评估。(1) **补丁正确性**：用可执行验证（基于测试的求解）检查 agent 产出的补丁，汇总为 Resolved Rate；三个受评 agent 的报告值从 29% 到 70% 不等。(2) **推理契合度**：将 agent 的中间推理与开发者认可的参考轨迹（issue 理解、文件定位、实现任务、步骤分解）比对，采用召回式与过预测式的覆盖度量，相对参考推理衡量。作者报告，能应用但仍未通过测试的补丁覆盖的参考推理要素更少（较成功补丁召回低 35.7%、过预测高 94.1%）。确切的评分定义、推理契合是否使用 LLM judge，以及三个受评 agent 的身份为 TODO(reference)。

## Typical Duration

TODO(reference)。在此处核验的来源中，论文未给出每任务的步数、wall-clock 或 token 预算。

## Main Contribution

一个推理增强的仓库级特性新增 benchmark：它超越"只看最终测试正确性"的评估，为每个实例配上结构化的中间参考推理，并以双轨框架联合评分补丁正确性与推理契合度，从而揭示 agent 在推理过程的哪一环失败，而不只是是否失败。

## Key Design Ideas

- 以仓库级特性新增（而非缺陷修复）作为评估目标。
- 每个实例配结构化的中间参考推理，分解为 issue 理解、文件定位、实现任务与步骤分解。
- 双轨评估，联合度量最终补丁正确性与中间推理同开发者认可参考轨迹的契合度。
- 诊断性的推理级分析，将"能应用但失败"的补丁与参考推理要素覆盖度下降联系起来。

## Strengths

- 在结果级信号（补丁正确性）之外提供中间的过程级信号（推理契合度），弥补纯测试 benchmark 的黑盒局限。
- 由 12 个开源仓库的真实特性新增实例构建，配可执行验证。
- 推理级分析给出具体的诊断发现——例如 agent 能很好理解高层意图，但在将其转化为具体实现步骤时表现下滑。

## Limitations

- Repository note: 三个受评 agent、12 个仓库以及确切的推理契合评分流程此处未从一手来源确认，仍为 TODO(reference)。
- Repository note: 由开发者认可轨迹派生的参考推理可能偏向某一条被采纳的实现路径；是否对其他有效轨迹给予认可此处未经核实。

## Related Works

- [SWE-bench ProMax](./swe-bench-promax.md) — 同为由真实 commit 构建的仓库级 coding-agent benchmark，但聚焦多语言大规模重构，而非带推理契合评分的特性新增。
