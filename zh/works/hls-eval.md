# HLS-Eval (2025)

> [English](../../works/hls-eval.md) | **简体中文**

> **首次公开：** 2025-04-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2504.12268)

## Overview

HLS-Eval 是评测 LLM 高层综合（HLS）设计任务的 benchmark 与框架：94 个配自然语言描述与测试台的独特设计，覆盖两类任务——从自然语言生成 HLS 代码，以及做 HLS 专有的编辑以优化性能与硬件效率——在 Vitis HLS 上按可解析性、可编译性、可运行性、可综合性判分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.12268>
- **Code:** <https://github.com/stefanpie/hls-eval>
- **Venue:** ICLAD 2025（据官方仓库；arXiv 元数据无发表信息）

## Summary

高层综合把 C/C++ 编译成硬件，其质量取决于代码是否写得「面向硬件」。HLS-Eval 检验 LLM 能否做到这点：94 个设计（取自标准 HLS benchmark 与新来源），每个配自然语言描述与测试台，覆盖两类任务——据描述生成 HLS 代码，以及做 HLS 专有编辑以优化性能与硬件效率，呼应迭代式 HLS 设计循环。输出在 Vitis HLS 上按四个面向硬件的指标判分：可解析性、可编译性、可运行性、可综合性，并报告 pass@k。

## Tasks

覆盖 94 个 HLS 设计的两类任务：自然语言到 HLS 代码生成，以及 HLS 专有的优化编辑；框架承载的生成，在 Vitis HLS 上评估。

## Domains

电气工程——高层综合：LLM 对可综合硬件代码的生成与优化。

## Evaluation

- 四个指标——可解析性、可编译性、可运行性、可综合性——加 pass@k，在 Vitis HLS 上评估。
- **报告。** 评测了开源 LLM；具体分数在正文中（TODO(reference)）。

## Typical Duration

每个设计单次生成或编辑；由工具评估。

## Main Contribution

把 HLS——一门独立的硬件代码学问——纳入 LLM 评估，配以超越「能否编译」、直抵「能否综合」的面向硬件指标。

## Key Design Ideas

- 四指标阶梯（解析 → 编译 → 运行 → 综合）评判硬件就绪度，而非只看文本。
- 优化编辑任务捕捉迭代式 HLS 精修循环，而非只看初稿生成。
- 真实的 Vitis HLS 评估使结果绑定在工业工具链上。

## Strengths

- 覆盖纯 Verilog/RTL benchmark 忽略的 HLS，且框架开放。
- 可综合性判分瞄准硬件真正在意的属性。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；ICLAD 2025 是仓库声明，arXiv 元数据未载明。各模型分数在正文中。

## Related Works

- [VerilogEval](./verilogeval.md) — 同样是 LLM 硬件代码生成，在 RTL/Verilog 层而非 HLS。
- [CVDP](./cvdp.md) — 同样是多任务硬件设计评估，兼含生成与验证。
- [RTLLM](./rtllm.md) — 同样是从自然语言做设计级硬件生成。
