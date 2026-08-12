# MASSE (2025)

> [English](../../works/masse.md) | **简体中文**

## Overview

MASSE 是一套面向结构工程、无需训练的多 agent LLM 系统，随之发布的还有一个含 100 道结构工程题的数据集，题目均配专家核验的 ground truth，另有四项按评分细则打分的 benchmark（SAAB、SDAB、LAB、MASEB），分别覆盖结构分析、结构设计、荷载转换与端到端工作流执行。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** https://arxiv.org/abs/2510.11004
- **Code:** https://github.com/DelosLiang/masse

## Summary

MASSE 把一家咨询公司真实的结构工程工作流拆成三个 LLM agent 团队——分析团队、工程师团队与管理团队，角色之间以结构化 JSON 传递信息，通过 RAG 从建筑规范文档中检索抗震参数，构建并求解 OpenSeesPy 有限元模型，最后给出承载力校核结论。为衡量该系统，作者构建了一个含一百道结构工程题、难度不一的数据集，每题都配一份经专家验证的 ground-truth 解，并定义四项 benchmark，各自带有明确的分项评分细则，由一个 LLM judge 对照完整的分析日志逐项打分。论文报告了四种 LLM 后端的模型对比、一项成本与运行时长的权衡分析、一项关于 agent 记忆与结构化 I/O 的消融，以及一项与执业工程师的人类对照研究。

## Tasks

一百个各不相同的题目实例，围绕一个货架系统设计场景构建，每个实例包含自然语言题目描述、中间推理步骤，以及用作评测判据的最终结果。数据由加拿大不列颠哥伦比亚省真实货架系统项目的生产记录重新整理而来，发布前作了匿名化；ground-truth 解由专家给出。分项任务涵盖参数检索、抗震荷载转换、结构建模、结构分析、截面特性确定、截面承载力计算与结构适用性校核。每道题运行十次独立试验，系统整体评估共采集一百条轨迹。

## Domains

土木与结构工程。全程受评的目标都是一项结构工程判断：从建筑规范文档中检索场地相关的抗震参数（Sa(0.2)、Sa(0.5)、Sa(1.0)、Sa(2.0)、PGA、PGV），把它们换算为楼层地震荷载，为货架结构装配一个由梁柱与支撑构成的 OpenSeesPy 模型，运行有限元分析，计算构件承载力，最后返回结构适用性的通过/不通过结论。这属于地震*工程*——承重结构的设计与校核——而不是地震危险性科学。未指派共同领域：有限元与 RAG 工具只是通向结构结论的手段，本身并非独立的受评目标。

## Evaluation

GPT-5 充当 LLM judge，读入一份完整的 MASSE 分析日志，对照专家核验的 ground-truth 解，输出一个 JSON 对象，内含四项 0–100 分的得分外加总 token 用量与总耗时。每项 benchmark 都有明确的分项细则：SAAB = 模型几何准确性（30 分）+ 截面与荷载数据的整合（20）+ OpenSees 分析执行（30）+ 结果提取准确性（20）；SDAB = 提取准确性（30）+ 承载力计算（30）+ 数据存储与记忆更新（20）+ 传递与可得性（20）；LAB = 荷载提取（25）+ 调整与归一化（25）+ RAG 抗震检索（25）+ 荷载计算（25）；MASEB = 流程完成度（30）+ agent 之间的一致性（30）+ 最终结果准确性（20）+ 效率与鲁棒性（20）。报告结果：o4-mini 在 SAAB（96.6）、SDAB（91.4）与 MASEB（94.7）上领先；GPT-4o 在 LAB 上领先（98.1）；Claude 3.5 Sonnet 平均 89.2，GPT-3.5-turbo 为 73.6。一项消融显示，agent 记忆加上 JSON 结构化 I/O 把平均分从 61.8 抬到 88.5。

## Typical Duration

运行时长随 agent 之间通信轮数的上限而变：一轮时约 20 秒，升到四轮时接近 70 秒——该数据在十道有代表性的 MASEB 题目上各重复十次测得，同一区间内系统得分从不足 40 升至接近 90。在人类对照研究中，以 GPT-4o 为后端的 MASSE 完成那道标准化的货架系统设计任务约需两分钟。此外，MASEB 还把 token 成本与 wall-clock 运行时长折进它的「效率与鲁棒性」分项。

## Main Contribution

作者把 MASSE 定位为首个面向结构工程的多 agent 系统，也是一次概念验证：现实中大多数结构工程工作流，都可以由一套无需训练的 LLM 多 agent 系统完全自动化；支撑这一主张的是一个新数据集、若干扎根于真实问题的案例研究，以及与各核心 agent 角色对齐的评测指标。

## Key Design Ideas

- agent 角色照搬咨询公司的层级——分析团队（荷载、抗震、动力、结构分析师）、工程师团队（设计工程师、校核工程师）、管理团队——从而把长周期工作流切成若干单个 agent 应付得来的子任务。
- benchmark 按 agent 角色分别定义（SAAB、SDAB、LAB），再加一项整体性的系统 benchmark（MASEB），于是失败可以定位到分析、设计还是荷载环节。
- MASEB 有意把技术准确性与系统成本、运行时长混在一起打分，让效率成为分数的一部分，而不是另开一份报告。
- 抗震参数经由建筑规范文档上的检索增强生成获得，而非取自模型记忆，检索到的数值本身也作为 LAB 的一部分接受核查。
- agent 之间的通信全部受 JSON 约束，agent 记忆则是共享的；消融认定这两项组件贡献了绝大部分性能。
- 一项针对 OpenSeesPy 代码生成的单 agent 对双 agent 受控实验显示，单 agent 系统十次试验全部失败，而分解后的双 agent 系统在所有算例上都稳定执行。

## Strengths

- 这份 100 题数据集来自经过认证的生产记录，而不是合成构造；在文中提及的司法辖区内，此类荷载报告依法必须由结构工程师签字。
- 评分细则逐项公布并附分值权重，judge 的判定面因此可供检视，而不是一个笼统不透明的整体分。
- 成本、token 用量与运行时长与准确率一并报告，各后端之间的准确率—成本权衡也作了明确分析。
- 人类基线是直接测出来的：11 位经验丰富的结构工程师完成同一道标准化任务平均耗时 132 分钟。
- 代码与数据集已公开发布。

## Limitations

- 一百道题全部出自同一个场景族——货架系统设计——因此这些 benchmark 测的是单一结构类型内部的难度跨度，而不是结构工程的广度。
- 判分依赖单个 LLM judge（GPT-5）阅读分析日志；论文未报告 judge 之间的一致性，也未做人类与 judge 的标定。
- 这些 benchmark 是围绕 MASSE 自身的 agent 角色与日志格式定义的，因此要用到外部构建的 agent 上，得先把它映射到同一套角色分解上。
- Repository note: 模型对比覆盖 2025 年可用的四种后端，且只在 MASSE 内部作为后端评测，因此分数衡量的是「系统 + 模型」这对组合，而非模型本身。
- Repository note: 人类对照研究拿一条全自动流水线与无辅助的人工作业相比，衡量的是自动化带来的提速，而不是两者之间正确性的差距。

## Related Works

- [StructureClaw](./structureclaw.md) — 另一个带可执行求解器验证的结构工程 agent benchmark，判分依据是冻结的参考求解器响应，而非 LLM judge。
- [AutoBM / BMEval](./autobm.md) — 同样评测由自然语言生成 OpenSeesPy 结构模型，但判的是可执行性与自振周期一致性，而非按细则打分的工作流日志。
- [FEABench](./feabench.md) — 通过 API 驱动 COMSOL 的有限元 agent 评测，同一套「以仿真为中介」的模式，只是场景不在土木。
- [ERI Benchmark](./eri-benchmark.md) — 多领域工程指令 benchmark，其分类体系中含土木工程一门。
