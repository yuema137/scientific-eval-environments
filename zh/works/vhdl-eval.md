# VHDL-Eval (2024)

> [English](../../works/vhdl-eval.md) | **简体中文**

## Overview

VHDL-Eval 是评测 LLM 生成 VHDL 代码的框架：202 个问题，由 Verilog 评测问题翻译为 VHDL 并汇总公开 VHDL 问题而成，在零样本、上下文学习与参数高效微调三种设定下评估。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.04379>
- **Venue:** LAD 2024（IEEE International Workshop on LLM-Aided Design）

## Summary

Verilog 在 LLM 硬件 benchmark 中占主导，但 VHDL 是另一大 HDL，VHDL-Eval 填补了这一空缺：202 个问题，由一批 Verilog 评测问题翻译为 VHDL 并汇总公开的 VHDL 挑战而成，每题配自验证测试台。LLM 在零样本生成、上下文学习与参数高效微调下评估；论文的关键发现是——专门针对 VHDL 的监督微调是必要的，通用模型迁移得很差。

## Tasks

202 个 VHDL 代码生成问题（Verilog 翻译 + 汇总公开 VHDL），每题配自验证测试台；零样本、ICL、PEFT 设定下的静态生成。

## Domains

电气工程——数字设计：VHDL 代码生成。

## Evaluation

- 经自验证测试台得功能正确性，覆盖零样本、上下文学习与 PEFT 设定。
- **报告。** 结果论证了针对 VHDL 专门监督微调的必要性；摘要未给出单一数值通过率。

## Typical Duration

每题单次 VHDL 生成；经测试台验证。

## Main Contribution

把 LLM 硬件代码评估扩展到 VHDL——并记录了 Verilog 中心的模型迁移不佳、VHDL 需要专门微调。

## Key Design Ideas

- 把 Verilog 问题翻译为 VHDL，在几无先例处自举出一个 benchmark。
- 自验证测试台使正确性可检验、无需人工判分。
- 对比零样本/ICL/PEFT，定位 VHDL 能力必须从何而来。

## Strengths

- VHDL 代码生成的参照 benchmark，补上一个未被充分服务的 HDL。
- 「需要微调」的发现对 VHDL 工具直接有用。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与 Comments 编写（2026 年 8 月）；LAD'24 经 Comments 确认。arXiv 页面无法核实官方代码 URL。

## Related Works

- [VerilogEval](./verilogeval.md) — Verilog 对应物，VHDL-Eval 翻译了它的问题。
- [RTLLM](./rtllm.md) — 同样是从规格生成 HDL 设计，语言为 Verilog。
- [HLS-Eval](./hls-eval.md) — 同样是硬件代码生成评估，处于高层综合层。
