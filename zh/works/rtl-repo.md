# RTL-Repo (2024)

> [English](../../works/rtl-repo.md) | **简体中文**

## Overview

RTL-Repo 在大规模 RTL 设计项目上评测 LLM：4,000 多个从公开 GitHub 仓库抽取的 Verilog 样本，每个都提供其所在仓库的完整上下文，考察多文件、仓库级的 Verilog 代码补全。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.17378>
- **Code:** <https://github.com/AUCOHL/RTL-Repo>
- **Venue:** LAD 2024（IEEE International Workshop on LLM-Aided Design）

## Summary

多数 RTL benchmark 给模型一个自包含的问题，而真实硬件存在于多文件仓库里。RTL-Repo 测的正是这一场景：4,000 多个来自公开 GitHub 项目的 Verilog 样本，每个都附带完整仓库上下文，要求模型补全与周边跨文件设计相契合的 Verilog 代码。它评测 GPT-4、GPT-3.5、Starcoder2 以及 Verilog 专用模型（VeriGen、RTLCoder），以编辑相似度与精确匹配判分，而非仿真 pass@k。

## Tasks

仓库级 Verilog 代码补全，覆盖 4,000+ 样本，每个附完整仓库上下文；静态补全，按字符串级相似度判分。

## Domains

电气工程——数字设计：真实项目中的仓库级 RTL 代码补全。

## Evaluation

- 相对参考补全的编辑相似度与精确匹配（仓库排行榜指标）。
- **报告。** 比较了 GPT-4、GPT-3.5、Starcoder2、VeriGen、RTLCoder；摘要未给出单一头条数值。

## Typical Duration

每个样本单次补全，以完整仓库上下文为条件。

## Main Contribution

把仓库级、跨文件上下文引入 RTL 评估——测量模型能否写出契合既有项目的硬件，而不只是孤立模块。

## Key Design Ideas

- 完整仓库上下文考察 RTL 特有的长上下文跨文件推理。
- 取材公开 GitHub，规模化地提供真实项目结构（4,000+ 样本）。
- 编辑相似度/精确匹配的判分适配仿真不便的补全场景。

## Strengths

- 自包含 RTL benchmark 缺失的仓库级视角。
- 样本量大，比较中纳入了 Verilog 专用模型。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；据官方仓库发表于 LAD'24（「MLCAD 2024」的说法有误）。字符串相似度指标不验证功能正确性。

## Related Works

- [VerilogEval](./verilogeval.md) — 同样是 LLM Verilog 生成，规模为自包含单题、带仿真。
- [RTLLM](./rtllm.md) — 同样是 RTL 生成，规模为完整设计而非仓库级。
- [CVDP](./cvdp.md) — 同样是大范围 RTL 评估，兼含设计与验证。
