# The Well (2024)

> [English](../../works/the-well.md) | **简体中文**

## Overview

The Well 是面向机器学习的大规模多样物理模拟集合：16 个数据集共 15 TB，横跨生物系统、流体力学、声散射，以及河外星系流体与超新星爆发的磁流体动力学模拟，配统一的 PyTorch 训练评估接口。它服务的是科学 ML 代理模型而非 LLM agent（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.00568>
- **Code:** <https://github.com/PolymathicAI/the_well>
- **Project:** <https://polymathic-ai.org/the_well/>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks

## Summary

代理模型的进展卡在数据广度上：在一种物理工况上调好的模型换一种工况就常常失灵。The Well 用体量与多样性作答——与领域专家共同整理的 16 个模拟数据集共 15 TB，从活性物质、粘弹性失稳到天体物理磁流体——统一在一个 PyTorch 接口与示例基线之后，让单一训练评估循环就能横扫过去需要逐一搭管线的各种物理工况。

## Tasks

通过统一接口对 16 个时空物理模拟数据集（15 TB）做代理模型训练与评估；非 LLM 设定。

## Domains

多样的模拟物理：流体力学、声散射、河外星系流体与超新星的磁流体动力学、生物系统。

## Evaluation

- 通过统一 PyTorch 库做基线训练与评估；指标定义为 TODO(reference)。
- **报告。** 摘要的主张即资源本身：16 个专家整理数据集共 15 TB。

## Typical Duration

N/A——离线代理模型训练与评估；非 agent 设定。

## Main Contribution

达到基础模型规模与多样性的物理模拟数据，使代理模型的跨工况泛化从愿景变成可检验的命题。

## Key Design Ideas

- 一个接口下的十六种异质物理工况让跨工况迁移失败无处遁形。
- 领域专家的整理保证每个数据集物理上有意义，而不只是量大。
- 统一的访问方式消除了狭窄评估的工程借口。

## Strengths

- 本仓库记录的最大、最多样的开放物理模拟集合。
- NeurIPS D&B 出身，Polymathic AI 持续维护。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。16 个数据集的完整清单见项目文档站。
- Repository note: The Well 服务的是科学 ML 代理模型而非 LLM agent；收录为 agent 相关 PDE benchmark 与本仓库代理模型注意事项类卡片所引用的经典数据基座。

## Related Works

- [PDEBench](./pdebench.md) — 结构化 PDE 的经典前代套件。
- [RealPDEBench](./realpdebench.md) — 以配对的真实世界测量补足模拟多样性。
- [gwBenchmarks](./gwbenchmarks.md) — 用同一类昂贵模拟数据（数值相对论）做 agent 压力测试。
