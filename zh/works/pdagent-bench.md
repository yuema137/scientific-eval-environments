# PDAgent-Bench (2026)

> [English](../../works/pdagent-bench.md) | **简体中文**

> **首次公开：** 2026-06-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.17253)

## Overview

PDAgent-Bench 是一个 benchmark，用于在整个 VLSI 物理设计流程上评估基于 LLM/VLM 的 agent，它把任务级评估（概念题与工具中心题）与在真实电子设计自动化（EDA）环境中的工作流级闭环执行结合起来。

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities


- [优化与工程设计](../activities/optimization_engineering_design.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.17253
- **Venue:** arXiv 预印本（cs.AR），2026 年 6 月 15 日提交

## Summary

PDAgent-Bench 瞄准语言与视觉语言模型在 VLSI 物理设计上尚未被充分探索的能力——该任务要求在严格设计约束下做高维、多阶段优化，与 EDA 工具协同交互，并做迭代式精化。该 benchmark 把一套任务级套件（353 道精选题目——涵盖概念性问题与带专家验证参考及可执行解的真实工业产物）与一套工作流级 agentic 框架（支持对完整物理设计流程做闭环评估）整合在一起。作者评估了 11 个最新模型，发现现代 LLM/VLM 虽在概念题上有竞争力，但在工具中心的执行以及长时程、多阶段推理上仍存在实质性不足。

## Tasks

353 道精选任务，跨五个能力维度（据论文报告）：

- **基础知识：** 90 题
- **报告理解：** 11 题
- **根因分析：** 21 题
- **静态时序分析：** 11 题
- **脚本生成：** 210 题（Innovus：90，ICC2：88，ECO：10，FM：22）
- **全流程实现：** 10 个设计项目

任务把概念性问题与真实工业产物结合起来。所有题目与参考答案均由三位领域专家独立评审，所有基于脚本的解答均通过执行验证。所报告的工艺与工具：TSMC 28nm 为主工艺节点，Nangate 45nm 用于开源流程；商用 EDA 工具包括 Cadence Innovus 22、Synopsys IC Compiler II 2022、PrimeTime 2022 与 Formal 2022，另有开源 OpenROAD 流程。

## Domains

VLSI 物理设计 / 电子设计自动化——芯片后端实现，包括布图规划、供电规划、布局、时钟树综合、布线、静态时序分析与工程变更单（ECO）工作。

## Evaluation

两部分评估。**任务级：** 在精选题目上的 pass@1 / pass@5 准确率，基于脚本的解答由执行检查，概念/分析类答案对照专家验证参考评分。所报告的头条数字（针对 GPT-5.5）包括：基础知识 80.4%、报告理解 74.6%、根因分析 73.3%、ICC2 脚本生成 45.5%、Innovus 脚本生成 42.2%。**工作流级：** PDAgent 框架通过规划、实现、调试与优化的闭环编排各专业 agent；全流程执行以代表性设计（如 TinyRISCV、AES-256、Ethernet MAC）上的时序收敛与 DRC（设计规则）违例结果来评估，论文报告可实现时序收敛且 DRC 违例为零或极少。

## Typical Duration

TODO(reference) — 论文未给出逐任务的 wall-clock 或 token 预算。全流程实现任务贯穿多阶段的物理设计流程（初始化、布图规划、供电规划、布局、时钟树综合、CTS 优化、布线、布线优化），相对单题概念任务而言属长时程。

## Main Contribution

一个面向 VLSI 物理设计中 LLM/VLM agent 的综合、多维 benchmark，把任务级评估与工作流级闭环执行统一起来，并配一套与人类对齐的 agentic 物理设计工作流框架（PDAgent）。作者报告，融入人类技能的 agentic 工作流能显著提升端到端物理设计表现。

## Key Design Ideas

- 把评估拆成任务级评估（概念 + 工具中心题）与在真实 EDA 环境中的工作流级闭环执行。
- 把任务扎根于真实工业产物，配专家验证参考与可执行的参考解。
- 通过对多种 EDA 工具（Innovus、ICC2）、ECO 与形式验证（FM）的脚本生成，直接覆盖工具中心的能力面。
- 提供一个多 agent 的 PDAgent 框架，在物理设计各阶段上闭合规划、实现、调试与优化的循环。
- 同时纳入商用（TSMC 28nm；Innovus、ICC2、PrimeTime、Formal）与开源（Nangate 45nm；OpenROAD）的工具/工艺设定。

## Strengths

- 瞄准一个论文指出对 LLM/VLM agent 而言明显未被充分探索的领域（VLSI 物理设计后端），与前端设计形成对比。
- 对基于脚本的解答做可执行验证、对参考做三专家评审，支撑答案质量（论文）。
- 评估了横跨专有与开源家族的 11 个模型，便于跨模型比较。

## Limitations

- 工具中心执行的脚本生成准确率仍偏低（例如最强模型在 Innovus 上为 42.2%），作者将其归结为当前模型而非 benchmark 的实质性局限。
- Repository note: 撰写时论文称 benchmark 与框架将「很快」开源，但未提供公开仓库 URL，故代码/数据可得性未经核验。
- Repository note: 论文未报告逐任务时长或 token/算力预算，限制了资源感知的比较。

## Related Works

- TODO(reference) — 待建立索引后可链接相关的 EDA/硬件 agent 评估（如 AMS 电路与 ASIC 设计 agent benchmark）。
