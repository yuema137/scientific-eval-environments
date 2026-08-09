# VerilogEval (2023)

> [English](../../works/verilogeval.md) | **简体中文**

## Overview

VerilogEval 是评测 LLM 生成 Verilog 代码的标杆 benchmark：取自 HDLBits 教学网站的 156 个问题，通过将生成的 RTL 与参考解仿真对比来自动检验功能正确性。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2309.07544>
- **Code:** <https://github.com/NVlabs/verilog-eval>
- **Venue:** ICCAD 2023（特邀）

## Summary

VerilogEval 为 LLM 硬件代码生成确立了功能正确性评估：156 个 HDLBits 问题，模型据题生成 Verilog RTL，通过将输出与金标准仿真对比来判分，并报告 pass@k。后续「Revisiting VerilogEval」（arXiv 2408.11053）扩展了基础设施，加入规格到 RTL 任务、上下文学习与自动失败分类，报告 GPT-4o 在规格到 RTL 上达 63% 的通过率。VerilogEval 至今仍是 RTL 代码生成 benchmark 的参照点。

## Tasks

156 个源自 HDLBits 的 Verilog 问题；LLM 据问题描述生成 RTL（v1 为代码补全，v2 增加规格到 RTL）。静态生成，经仿真判分。

## Domains

电气工程——数字设计：Verilog RTL 代码生成。

## Evaluation

- 将生成的 RTL 与参考解仿真对比得功能正确性；pass@k。
- **报告。** 监督微调自举可提升通过率；v2 论文报告 GPT-4o 在规格到 RTL 上 63%。

## Typical Duration

每题单次 RTL 生成；经仿真验证。

## Main Contribution

LLM Verilog 生成的奠基性功能正确性 benchmark，其 HDLBits 设计与 pass@k 协议成为 RTL 代码生成领域的模板。

## Key Design Ideas

- 与参考解仿真对比，使正确性是功能性的而非文本性的。
- 取材 HDLBits，给出分级、经教学验证的问题。
- v2 的规格到 RTL 任务从代码补全走向规格遵循。

## Strengths

- RTL 代码生成评估的事实标准，NVlabs 持续维护。
- 基于仿真的 pass@k 客观且广泛可比。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、Comments 与官方仓库编写（2026 年 8 月）；ICCAD 2023 经 Comments 与仓库确认。此处引用的头条数字来自 v2 论文（2408.11053）。

## Related Works

- [RTLLM](./rtllm.md) — 同样是从自然语言生成 Verilog，规模为完整设计而非 HDLBits 单题。
- [RTL-Repo](./rtl-repo.md) — 同样是 RTL 生成，规模到仓库级、含跨文件上下文。
- [CVDP](./cvdp.md) — 同样是 RTL 评估，扩展到验证与 agent 化格式。
