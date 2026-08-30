# LoopsBench (2026)

> [English](../../works/loopsbench.md) | **简体中文**

> **首次公开：** 2026-07-31 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.00267)

## Overview

LoopsBench 是一个长 horizon benchmark，用于评估 coding agent 的「循环工程（loop engineering）」——即持续、多步的软件开发；其中每个任务都是一张由可分别测试的开发单元构成的依赖 DAG，先决关系的边有源码证据支撑。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A —— 面向通用仓库的通用软件工程（长 horizon「循环工程」）benchmark；作为通用应用软件工程而排除在外。

## Links

- **Paper:** <https://arxiv.org/abs/2608.00267>
- **Project:** <https://loopsbench.ai>
- **Code:** <https://github.com/microsoft/Loopsbench>
- **Venue:** arXiv preprint (2026)

## Summary

LoopsBench 关注 coding-agent 基础设施从 harness 工程向循环工程的转变，认为既有 benchmark 多聚焦于局部任务或终态结果，对持续执行的洞察有限。每个任务被建模为一张依赖 DAG，其节点是可分别测试的开发单元，由有源码证据的先决边相连。一个「流感知」（flow-aware）运行时会随着先决条件被满足，沿「就绪前沿」逐步释放测试，并把已完成的节点保留为回归义务，因此 agent 既要向前推进，又要避免破坏此前的成果。作者评估了与广泛使用的循环实现配对的前沿 coding agent。

## Tasks

112 个取自真实来源的任务，覆盖 8 种编程语言与 9 个领域，包含超过 5,300 个带可执行测试的开发单元。每个任务都是一张由可分别测试的开发单元构成的依赖 DAG，其先决边从源码证据中还原。

## Domains

跨 8 种编程语言与 9 个领域的软件开发（具体领域名称：`TODO(reference)`）。该 benchmark 评估 coding agent 在持续软件工程工作上的能力。

## Evaluation

经「流感知」运行时的基于执行评分：随着先决条件完成，测试沿就绪前沿释放，已完成节点被保留为回归义务，从而能检测回归。据官方仓库，验证由 Docker 支撑，验证器可区分未完成、部分完成与完全完成的解，且每个任务在发布前都带有一次由维护者用于核验的 oracle 运行。分析另会把记录到的 agent 计划与源码还原的先决 DAG 作比较。

## Typical Duration

`TODO(reference)` —— 论文把任务定位为长 horizon/持续执行，但此处未抽取到具体的单任务轨迹长度、墙钟时间或 token 预算。

## Main Contribution

一个面向 coding-agent 评估中循环工程的长 horizon benchmark，结构为由可分别测试之开发单元构成、有源码证据的依赖 DAG，配一个「流感知」运行时——它沿就绪前沿释放测试，并把已完成节点视作回归义务。

## Key Design Ideas

- 任务 = 由可分别测试之开发单元构成的依赖 DAG，先决边有源码证据支撑。
- 「流感知」运行时随先决条件满足沿「就绪前沿」释放测试。
- 已完成节点被保留为回归义务，从而在持续执行中暴露回归。
- 评估与广泛使用的循环实现（如 outer-continuation 循环）配对的前沿 coding agent。
- 把记录到的 agent 计划与源码还原的先决 DAG 作比较。

## Strengths

- 大规模的可执行底座：112 个任务、超过 5,300 个带可执行测试的开发单元（论文）。
- 覆盖 8 种编程语言与 9 个领域的广度（论文）。
- 明确衡量长 horizon 执行中的回归，而不仅是终态结果（论文）。
- 在 MIT 许可下开源 benchmark 数据与代码，配 Docker 支撑的验证以及面向多种 agent/循环的适配器（官方仓库）。

## Limitations

- 最强的评估配置（Opus-4.7 配 Claude Code 与 outer continuation）仅解决 25.00% 的任务，表明尚有大量提升空间（论文）。
- 记录到的计划只能还原源码还原之先决 DAG 的一部分，且在所评估的各循环配置中回归事件仍然可见（论文）。
- Repository note: 9 个领域的具体名称与单任务的时长/预算此处未抽取，标记为 `TODO(reference)`。

## Related Works

- [SWE-bench Pro-Max](./swe-bench-promax.md) —— 另一个长 horizon coding-agent benchmark，同样强调对软件任务的基于执行评估。
