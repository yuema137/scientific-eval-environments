# AssertionBench (2024)

> [English](../../works/assertionbench.md) | **简体中文**

## Overview

AssertionBench 评测大语言模型的硬件断言生成：100 个从 OpenCores 精选的 Verilog 设计，配以经形式验证的断言（来自 GoldMine 与 HARM 工具），考察 LLM 能否为数字硬件推断出功能正确的断言。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.18627>
- **Venue:** NAACL 2025

## Summary

断言是硬件设计「绝不能违反」的可执行规格，撰写它既专业又繁琐。AssertionBench 把断言生成变成可测量的 LLM 任务：100 个来自 OpenCores 的 Verilog 设计，每个都以 GoldMine 与 HARM 工具产生的、经形式验证的断言为真值。最先进的 LLM 按其产出的功能正确断言比例评分，论文还研究了上下文示例数量对质量的影响——结论是基于 LLM 的断言生成器仍有很大改进空间。

## Tasks

为 100 个 OpenCores Verilog 设计生成功能正确的 SystemVerilog 断言；静态生成，对照经形式验证的参考断言判分。

## Domains

电气工程——数字硬件验证：Verilog 设计的断言生成。

## Evaluation

- 所生成断言中功能正确的比例，并分析上下文示例数量的影响。
- **报告。** 各 SOTA LLM 均有很大改进空间；摘要未给出单一头条数值。

## Typical Duration

每个设计单次断言生成；无交互式设定。

## Main Contribution

一个以形式验证为根基的硬件断言生成 benchmark——用机器验证的真值而非表面合理性来衡量 LLM 对设计意图的把握。

## Key Design Ideas

- 经形式验证的参考断言（GoldMine、HARM）给出客观正确性。
- 真实 OpenCores 设计把难度锚定在实用硬件上。
- 变动上下文示例数量，把提示效应与模型能力分开。

## Strengths

- 发表信息经核实（NAACL 2025），正确性有形式化根基。
- 瞄准验证——硬件设计的瓶颈——而不仅是代码生成。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；arXiv 页面无法确认代码 URL，摘要未给出单一头条准确率。

## Related Works

- [FVEval](./fveval.md) — 同样是 LLM 硬件验证，横跨断言生成与形式验证推理。
- [VerilogEval](./verilogeval.md) — 同样是 LLM Verilog 评估，考功能代码生成而非断言。
- [CVDP](./cvdp.md) — 同样兼含 RTL 设计与验证，在综合的 agent 化 benchmark 中。
