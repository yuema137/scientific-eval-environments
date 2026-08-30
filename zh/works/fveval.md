# FVEval (2024)

> [English](../../works/fveval.md) | **简体中文**

> **首次公开：** 2024-10-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2410.23299)

## Overview

FVEval 是 NVIDIA 面向数字硬件形式验证、理解语言模型能力的 benchmark，含三个子任务——从自然语言生成 SystemVerilog 断言、从测试台/设计生成断言、以及设计级验证推理——用 Cadence Jasper 形式工具校验。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.23299>
- **Code:** <https://github.com/NVlabs/FVEval>
- **Venue:** arXiv preprint (cs.AR), 2024

## Summary

形式验证是硬件正确性真正被证明的地方，FVEval 衡量 LLM 能否参与其中。它定义三个不同层次的子任务：NL2SVA-Machine 与 NL2SVA-Human 从自然语言生成 SystemVerilog 断言，Design2SVA 从设计生成断言/测试台。生成的产物用 Cadence Jasper 形式工具校验，而非启发式；benchmark 以开放许可发布预生成数据集与评估代码。

## Tasks

三个形式验证子任务：NL2SVA-Machine、NL2SVA-Human（自然语言到 SVA）与 Design2SVA（设计到断言/测试台）；静态生成，经形式工具校验。

## Domains

电气工程——数字硬件的形式验证：SystemVerilog 断言与测试台生成。

## Evaluation

- 用 Cadence Jasper 形式工具校验所生成断言/测试台的正确性。
- **报告。** LLM 能力在三个子任务间各异；总题数与头条数字为 TODO(reference)——摘要未载明。

## Typical Duration

每个任务单次生成；验证由工具完成。

## Main Contribution

一个以形式工具为根基的 benchmark，把硬件验证分解为不同的 LLM 能力——面向机器与面向人工的断言生成、以及设计级推理。

## Key Design Ideas

- 形式工具校验（Jasper）使正确性是证明而非启发式。
- 三个子任务把翻译难度与设计理解分开。
- 开放数据集加评估代码使 benchmark 可复现。

## Strengths

- 以工业形式验证而非仿真启发式为根基。
- NVlabs 公开发布，含预生成数据集与 harness。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv 元数据无发表信息，各子任务题数与分数在正文中。

## Related Works

- [AssertionBench](./assertionbench.md) — 同样是 LLM 断言生成，对照经形式验证的参考判分。
- [CVDP](./cvdp.md) — 同样在设计之外兼含 RTL 验证，在更广的 agent 化 benchmark 中。
- [VerilogEval](./verilogeval.md) — 同样是 LLM Verilog 评估，考功能代码生成。
