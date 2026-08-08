# CodePDE (2025)

> [English](../../works/codepde.md) | **简体中文**

## Overview

CodePDE 是 LLM 驱动的 PDE 求解器生成推理框架：把 PDE 求解构造成代码生成问题，其内置的评估研究——在代表性 PDE 问题上考察推理、调试、自我改进与测试时扩展——事实上成为 LLM 生成数值求解器的参照评估。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.08783>
- **Code:** <https://github.com/LithiumDA/CodePDE>
- **Venue:** TMLR

## Summary

CodePDE 不训练代理模型，而是让 LLM 直接写出数值求解器，再测量所生成求解器在代表性 PDE 问题上的精度。框架系统评估求解器生成的关键能力——对离散化的推理、修复出错代码的调试、跨迭代的自我改进与测试时扩展——并报告 LLM 能在一系列代表性 PDE 问题上取得强表现，分析则指出求解器生成仍在何处失败。

## Tasks

在代表性 PDE 问题上的求解器代码生成，含迭代改进；任务与模型数为 TODO(reference)。

## Domains

面向物理系统建模的偏微分方程数值求解。

## Evaluation

- 生成求解器在代表性 PDE 问题上的精度，评估轴覆盖推理、调试、自我改进与测试时扩展；具体指标定义为 TODO(reference)。
- **报告。** LLM 在一系列代表性 PDE 问题上取得强表现。

## Typical Duration

每个问题为「生成-改进」求解器回合；非交互式环境。

## Main Contribution

把 PDE 求解重新定位为 LLM 代码生成问题——生成的是求解器而非解场——并确立了后续求解器生成 benchmark 沿用的评估轴（推理、调试、改进、扩展）。

## Key Design Ideas

- 生成求解器保留了端到端代理模型所放弃的可解释性与数值保证。
- 改进与测试时扩展被当作受测能力，而非实现细节。
- 解对照参考解检验，而非交给 judge 评判。

## Strengths

- 「LLM 写求解器」范式的奠基性评估。
- TMLR 发表并开源代码。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- Repository note: CodePDE 是推理框架，其内置评估研究充当其 benchmark；已验证来源中没有固定的任务套件。

## Related Works

- [PDEAgent-Bench](./pdeagent-bench.md) — 固定套件的后继者：645 个求解器生成实例，带分级的可执行/精度/效率检查。
- [CFDLLMBench](./cfdllmbench.md) — 同样以物理为根基验证求解器编码，专精于 CFD。
- [PDEBench](./pdebench.md) — 代理模型一侧的对应物：CodePDE 的问题所依托的经典 SciML PDE 套件。
