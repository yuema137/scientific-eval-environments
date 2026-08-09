# MooseBench (2026)

> [English](../../works/moosebench.md) | **简体中文**

## Overview

MooseBench 是带 PDE 级真值的 220 例多物理场 benchmark，随一篇标题即结论的论文发布：「你的模拟能跑，但解的是错的物理」。配套的 Intent Fidelity Score（IFS）从 LLM 生成的 MOOSE 输入文件中确定性地重构其编码的 PDE，与预期契约比对。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.09360>
- **Venue:** arXiv preprint (cs.LG, cs.AI, cs.CL, cs.SE), 2026

## Summary

对模拟代码而言，执行成功是个危险的信号：一份 MOOSE 输入文件可以顺利跑完，却编码了错误的控制项、边界条件或系数。论文的 IFS 是覆盖控制项、边界条件、初始条件、系数与时间格式的结构化指标，通过从 MOOSE 的 Kernel/BC 对象确定性重构所编码的 PDE 来计算。在 220 个 MooseBench 算例上，只修执行错误能提高执行成功率，却让全部算例中的 39–40% 处于「能跑但物理错误」的状态；由确定性违规报告驱动、以 PDE 为依据的改进循环，在直接生成 IFS 低于 0.7 的算例上带来 +0.22 至 +0.41 的绝对提升。概念验证还把该方法扩展到 UFL/FEniCS、FreeFEM、FiPy 与 Devito。

## Tasks

220 个面向 MOOSE 框架的多物理场模拟代码生成算例，每例配有 PDE 级数学真值（预期契约）。

## Domains

多物理场有限元模拟（MOOSE），PDE 弱形式重构可扩展到 UFL/FEniCS、FreeFEM、FiPy 与 Devito。

## Evaluation

- **Intent Fidelity Score（IFS）：** 将确定性重构出的 PDE（控制项、边界条件、初始条件、系数、时间格式）与预期契约做结构化比对。
- **报告。** 只修执行错误使 220 例中 39–40% 保持「能跑但物理错误」；以 PDE 为依据的改进在起始 IFS 低于 0.7 的算例上带来 +0.22 至 +0.41 绝对提升。

## Typical Duration

每个算例为生成加自动改进循环；非交互式环境。

## Main Contribution

点名并测量了模拟代码的「理解-生成落差」：能跑不等于对，而分辨两者只能靠 PDE 级重构，不能靠执行。

## Key Design Ideas

- 真值是 PDE 而不是程序：重构使物理保真度可被确定性地检验。
- 确定性违规报告为改进循环提供不依赖 judge 的可操作反馈。
- 跨 DSL 的概念验证表明重构思路可泛化到 MOOSE 之外。

## Strengths

- 39–40% 的「能跑但物理错误」是迄今对无声物理错误最锋利的量化。
- IFS 把保真度分解为可审计的分量，而非单一分数。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。
- Repository note: 论文的头号贡献是 IFS 指标与改进方法；MooseBench 随之发布，本卡片记录其 benchmark。

## Related Works

- [PDEAgent-Bench](./pdeagent-bench.md) — 同样在可执行性之外为 LLM 生成的求解器设关卡，分级检查精度与效率。
- [CFDLLMBench](./cfdllmbench.md) — 同样以物理为根基验证模拟工作流，通过细化下的收敛性。
- [gwBenchmarks](./gwbenchmarks.md) — 同样记录了 agent 在缺乏外部验证时「假性完成」科学任务的现象。
