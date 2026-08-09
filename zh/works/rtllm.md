# RTLLM (2023)

> [English](../../works/rtllm.md) | **简体中文**

## Overview

RTLLM 是从自然语言指令生成设计级 RTL 的开源 benchmark：29 个手工设计（v2.0 扩展到 50 个），按语法、功能、设计质量三个递进目标判分，并配套一个提升 GPT-3.5 的「self-planning」提示方法。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.05345>
- **Code:** <https://github.com/hkust-zhiyao/RTLLM>
- **Venue:** ASP-DAC 2024

## Summary

问题集 benchmark 测的是小片段，RTLLM 评估的是从自然语言描述生成完整设计级 RTL。它的 29 个手工设计（v2.0 版扩展到 50 个，分为算术、存储、控制、杂项四类）按三个递进目标判分——语法正确、功能正确、设计质量。论文还提出「self-planning」提示方法，显著提升 GPT-3.5 在该 benchmark 上的表现。

## Tasks

29 个手工 RTL 设计任务（v2.0：50 个），从自然语言指令生成；静态生成，按语法、功能、设计质量判分。

## Domains

电气工程——数字设计：从自然语言生成完整设计级 RTL。

## Evaluation

- 语法、功能、设计质量三个递进目标，在 GPT-3.5 上评估 self-planning 的有无。
- **报告。** self-planning 显著提升 GPT-3.5；摘要未给出单一数值通过率。

## Typical Duration

每个任务单次设计生成。

## Main Contribution

一个早期的设计级（而非片段级）RTL benchmark，配分级目标阶梯，以及成为广泛引用基线的 self-planning 提示方法。

## Key Design Ideas

- 完整设计而非 HDLBits 片段，把生成推向真实硬件。
- 语法 → 功能 → 质量的阶梯给出部分得分结构。
- self-planning 表明提示结构与选模型同等重要。

## Strengths

- 奠基性的开源 RTL 生成 benchmark，持续扩充（v1.1、v2.0）。
- 三目标判分把「能编译」「能工作」「设计良好」区分开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；ASP-DAC 2024 经 arXiv Journal-ref 确认。摘要的 29 个设计对应 v1.0；仓库 v2.0 扩展到 50 个。

## Related Works

- [VerilogEval](./verilogeval.md) — 同样是 LLM Verilog 生成，规模为 HDLBits 单题、带 pass@k。
- [RTL-Repo](./rtl-repo.md) — 同样是 RTL 生成，规模到仓库级、含跨文件上下文。
- [CVDP](./cvdp.md) — 同样是 RTL 设计评估，扩展到验证与 agent 化格式。
