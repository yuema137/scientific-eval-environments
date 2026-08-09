# AtomWorld (2025)

> [English](../../works/atomworld.md) | **简体中文**

## Overview

AtomWorld 评测大语言模型对晶态材料的空间推理：模型在四类常用建模范式下执行十种基本的原子结构操作，用可验证的检查判分——在涉及复杂空间关系的操作上表现很差（旋转成功率低于 12%）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.04704>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2025

## Summary

晶态材料由其原子结构的几何决定，因此对它推理的 LLM 必须操作结构，而不只是回忆关于它的事实。AtomWorld 设计了十种基本操作——构建与修改原子结构——横跨四类常用建模范式，按对所得结构的可验证检查判分，而非依赖 judge。结论是一个鲜明的空间推理缺口：即便最强的模型也能应付简单编辑，却在需要复杂空间关系的操作上失手，旋转成功率低于 12%。

## Tasks

四类建模范式下的十种原子结构构建与修改操作；基于文本/结构（无图像输入），可静态验证。各范畴题量为 TODO(reference)——摘要未载明。

## Domains

材料科学——晶态结构的空间推理：在标准建模操作下构建与修改原子结构。

## Evaluation

- 对每个操作所产生的原子结构做可验证检查；无 LLM judge。
- **报告。** 强模型能应付简单操作，却在复杂空间关系上失手；旋转成功率低于 12%。当前摘要称 Claude Opus 4.6 表现最好。

## Typical Duration

单次结构编辑操作；非交互式多步循环。

## Main Contribution

把晶体结构的空间操作提炼为一项独立、可验证的 LLM 能力——并揭示当前模型对材料文本的理解远好于对材料几何的理解。

## Key Design Ideas

- 可验证的结构检查让判分客观，无需 judge。
- 四类建模范式把表示与操作类型分开。
- 旋转等空间关系操作暴露出几何盲区。

## Strengths

- 在真正的几何任务上做可验证、无 judge 的判分。
- 被定位为 agent/RL 测试台，而不只是静态排行榜。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；各范畴题量与代码可得性未载明。arXiv 元数据无发表信息。
- Repository note: 摘要中「Claude Opus 4.6」的命名对论文日期而言异常，应对照正式版复核。

## Related Works

- [MatText](./mattext.md) — 同样探测 LLM 对晶体结构的理解，走文本表示而非操作路线。
- [OpenXRD](./openxrd.md) — 同样以晶体学为中心的 LLM 评估，考 XRD 问答。
- [MatSciBench](./matscibench.md) — 同样是材料推理评估，覆盖更广的大学水平范围。
