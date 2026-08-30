# EnvTrace (2025)

> [English](../../works/envtrace.md) | **简体中文**

> **首次公开：** 2025-11-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2511.09964)

## Overview

EnvTrace 提出一套基于模拟来评估 LLM 生成的仪器控制代码的方法学：不用静态单元测试，而是让候选代码在同步辐射光束线的数字孪生上执行，通过对齐执行轨迹来评判语义等价性。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [实验室与仪器控制](../activities/laboratory_instrument_control.md)

## Links

- **Paper:** <https://arxiv.org/abs/2511.09964>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.PL), 2025

## Summary

EnvTrace 的出发点是：物理系统的行为无法只靠单元测试刻画——控制代码的正确性在于它随时间对仪器做了什么。候选代码在光束线控制逻辑的数字孪生上运行，轨迹对齐产出一个覆盖关键行为维度的多维度功能正确性分数。30 余个 LLM 以这种方式受评，许多顶级模型在快速控制代码生成上接近人类水平；数字孪生还能在真实实验执行前做预先验证。

## Tasks

N/A——评估方法学，在同步辐射光束线控制代码生成上演示；30 余个 LLM 通过对照控制逻辑数字孪生的轨迹对齐受评。

## Domains

同步辐射光束线仪器——实验物理基础设施的控制。

## Evaluation

- 对照数字孪生的**执行轨迹对齐**，产出覆盖关键行为维度的多维度功能正确性分数。
- **报告。** 许多顶级模型在快速控制代码生成上接近人类水平。

## Typical Duration

N/A——对生成的控制代码做模拟执行评估。

## Main Contribution

对于「意义即物理行为」的代码，用轨迹级语义比较取代无状态的单元测试，并表明数字孪生可以兼作真实实验的执行前安全闸。

## Key Design Ideas

- 代码的语义等价性由它在模拟中的行为判定，而非其文本或静态测试。
- 多维度分数把正确性分解到各行为维度，而非单一的通过/不通过标记。
- 同一个数字孪生既能离线评估，也能在指令触及真实仪器前做验证。

## Strengths

- 评估对象与仪器控制的部署现实一致。
- 在一个高度专门化的科学场景下覆盖了 30 余个模型。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [SysMoBench](./sysmobench.md) — 同样以执行为根基的一致性评分（trace 一致性在其门控指标之列），并拒绝 LLM-judge 评分。
- [AFMBench](./afmbench.md) — 同样对照真实物理仪器评估 agent，在原子力显微镜上。
- [Traxgen](./traxgen.md) — 同样确定性地构建轨迹级参考，但用于真值生成而非执行对齐。
