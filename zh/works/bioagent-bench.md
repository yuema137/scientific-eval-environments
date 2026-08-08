# BioAgent Bench (2026)

> [English](../../works/bioagent-bench.md) | **简体中文**

## Overview

BioAgent Bench 是生物信息学的 AI agent 评估套件：人工整理的端到端任务——RNA-seq、变异检测、宏基因组——agent 须以多步流水线完成并产出具体的输出产物，鲁棒性用受控扰动检验。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.21800>
- **Venue:** ICML 2026

## Summary

每个任务给 agent 一段任务提示，期待其交付完整的生物信息学流水线，输出产物由 LLM 判分器按流水线进度与结果有效性打分。前沿闭源与开放权重模型在多个 agent harness 下受评，鲁棒性用受控扰动检验——损坏的输入、诱饵文件与提示膨胀。核心发现：前沿 agent 无需精心定制的脚手架也能完成多步生物信息学流水线，但流水线整体搭对并不保证步骤级推理可靠。

## Tasks

人工整理的端到端生物信息学流水线（如 RNA-seq、变异检测、宏基因组），从任务提示做到具体输出产物；具体任务数为 TODO(reference)。

## Domains

生物信息学工作流：RNA 测序、变异检测与宏基因组学。

## Evaluation

- LLM 判分器基于输出产物为流水线进度与结果有效性打分。
- 鲁棒性套件含受控扰动：损坏输入、诱饵文件、提示膨胀。
- **报告。** 前沿 agent 无需复杂脚手架即可完成多步流水线，但高层流水线正确不保证步骤级推理可靠。

## Typical Duration

每个任务为多步流水线的构建与执行；预算为 TODO(reference)。

## Main Contribution

在生物信息学中把「能搭对流水线」与「每一步推理都对」分开，并表明抗扰动能力是独立于干净输入成功率的另一条轴。

## Key Design Ideas

- 基于输出产物判分，评估与 harness 无关。
- 受控扰动（诱饵、损坏、膨胀）实测鲁棒性而非默认它成立。
- 多 harness 评估暴露表现有多少依赖于脚手架。

## Strengths

- 覆盖基因组学实验室通用的标准流水线族，端到端真实。
- 「流水线对但步骤推理错」的缺口是其他套件没有单独隔离的诊断。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [BixBench](./bixbench.md) — 同样是探索式生物信息学 agent 评估，取自已发表的 notebook 分析。
- [GenoTEX](./genotex.md) — 同样是流水线级基因组学评估，对照专家整理的参考分析。
- [MDArena](./mdarena.md) — 同样是容器化、源自科研的科学工作流，在分子动力学领域。
