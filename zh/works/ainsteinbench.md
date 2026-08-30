# AInsteinBench (2025)

> [English](../../works/ainsteinbench.md) | **简体中文**

> **首次公开：** 2025-12-24 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2512.21373)

## Overview

AInsteinBench 在科学代码仓库上评测 coding agent：任务派生自六个广泛使用的生产级科学代码库的维护者 pull request——覆盖量子化学、量子计算、分子动力学、数值相对论、流体力学与化学信息学——在可执行环境中以测试驱动的方式验证。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.21373>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.PL), 2025

## Summary

SWE-bench 式评估遇上科学软件：AInsteinBench 从真实科学代码库维护者实际合并的改动出发，经多阶段筛选与专家评审整理任务，在可执行环境中做测试驱动验证，并关注有科学意义的失败模式。通用编码 benchmark 测的是 Web 应用里的胶水代码和杂活，这里的任务则要求遵守科学计算的数值约定、物理单位与算法契约。

## Tasks

派生自六个生产级科学仓库（量子化学、量子计算、分子动力学、数值相对论、流体力学、化学信息学）维护者 PR 的任务；任务数为 TODO(reference)。

## Domains

跨量子化学、量子计算、分子动力学、数值相对论、流体力学与化学信息学代码库的科学软件工程。

## Evaluation

- 可执行环境中的测试驱动验证；经多阶段筛选与专家评审整理；按科学意义归类失败模式。
- **报告。** 数值结果为 TODO(reference)；摘要未给出数字。

## Typical Duration

每个任务为仓库级 agent 编码会话。

## Main Contribution

把维护者 PR 的评估范式从通用软件移植到科学计算——在这里，正确性意味着数值与物理上的有效，而不只是通过普通测试。

## Key Design Ideas

- 维护者撰写的 PR 把任务锚定在科学真正需要的改动上。
- 可执行环境加测试驱动验证保持判分机械化。
- 失败模式按科学意义分类，而不只是当作测试失败。

## Strengths

- 覆盖六个科学领域的生产级代码库。
- 专家评审的整理守住任务效度。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布或任务数。

## Related Works

- [SWE-bench](./swe-bench.md) — AInsteinBench 移植到科学代码库的那个通用软件范式。
- [SciCode](./scicode.md) — 同样是科学家整理的科研编码，以独立问题而非仓库 PR 呈现。
- [MDArena](./mdarena.md) — 同样是源自科研的科学计算任务，在单一模拟模态。
