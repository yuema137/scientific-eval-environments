# Simona (2026)

> [English](../../works/simona.md) | **简体中文**

## Overview

Simona 是一份由专家撰写的 1,000 条化工过程描述数据集，作为一套多智能体 LLM 工作流的评测集提出——该工作流把自然语言的过程描述转换为可执行、可收敛的过程仿真流程图。系统以仿真收敛率（Simulation Convergence Rate）与设计耗时为指标，与 LLM、多智能体及人类专家基线对比。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.06776>

## Summary

论文针对的是工艺流程图与可用仿真之间的那一步：把描述出来的过程配置成在仿真器中真正能收敛的流程图。作者把这一步刻画为耗时费力、参数繁多的手工工作。所提系统由四个专职 agent 构成——语义解读、拓扑构建、配置整定与结果评估——并引入增强蒙特卡洛树搜索来稳定语义解析与配置生成，通过 HTTP API 与过程仿真器反复交互。评测在自建的过程描述语料 Simona 上进行，以收敛率与设计耗时为核心指标。

## Tasks

每个任务给出一段书面的化工过程描述，系统须产出一份仿真流程图——包含拓扑与单元操作配置——并能在过程仿真器中运行至收敛。论文写道：「Our experiments are conducted on a self-constructed dataset called Simona, consisting of 1000 process descriptions carefully designed by chemical engineering experts.」描述在两个维度上有差异：所涉单元操作的难度（混合器、精馏塔等，即流程图的节点），以及描述本身给出的细节程度。

## Domains

化学工程。受评目标是过程仿真与流程图设计——选取并连接混合器、精馏塔一类单元操作，整定其操作配置直至流程图收敛——这属于过程系统工程，而非化学。未指派共同领域：任务关心的是过程拓扑与仿真器配置，不涉及分子或反应层面的化学。

## Evaluation

主指标是仿真收敛率（SCR），「defined as the ratio of successfully converged process designs to total requirements」，并与以秒计的设计耗时一同报告。设计另按五个维度评分：经济可行性、环境可持续性、过程安全、技术可行性与拓扑合理性。仿真由自研工具完成——「For chemical process simulation, we integrate with our self-developed chemical process simulation software through HTTP APIs」——而非商业软件包。

报告结果：所提方法 SCR 达 80.3%；GPT-4o 为 23.4% SCR / 86.13 s，MetaGPT 为 49.2% SCR / 612.33 s，专家手工设计为 100% SCR / 8,301.91 s。摘要将其概括为：仿真成功率较基线提升 31.1%，设计耗时较人工专家减少 89.0%。主要评测骨干模型是 GPT-4o，另与 Claude Sonnet 4 做了对比。

## Typical Duration

每条过程描述的设计耗时被直接作为效率指标报告：GPT-4o 基线 86.13 s，MetaGPT 612.33 s，专家手工设计 8,301.91 s；所提方法据报告比人工基线快 89.0%。token 预算与 agent 步数未报告。

## Main Contribution

按作者的表述，贡献是一套端到端多智能体系统，把书面的过程描述一直推进到经计算确认的仿真配置，将四个角色专职的 agent 与增强蒙特卡洛树搜索结合起来，以获得可靠的语义解析与配置生成；随之提出的还有 Simona 描述语料，以及用于论证该系统的、以收敛性为核心的评估方式。

## Key Design Ideas

- 以收敛与否判分：只有生成的流程图在仿真器中真正收敛，该设计才算数，指标因此是执行验证的，而非基于相似度。
- 角色拆分为四个 agent——语义解读、拓扑构建、配置整定与结果评估——对应人工做流程图时的工作流。
- 在配置空间上做增强蒙特卡洛树搜索，并就每次扩展的子节点数（2、3、4、5）做了消融。
- 通过 HTTP API 访问仿真器，使 agent 与仿真器之间可以反复交互，而不是一次性生成。
- 对比表中纳入人类专家基线，为质量与耗时都提供了上界参照（100% SCR）。
- 任务差异刻意同时覆盖单元操作难度与描述细节程度，把解析难度与工程难度分开。

## Strengths

- 成功与否由执行验证：流程图在仿真器中收敛才算数，仅仅「看起来像一份合理流程图」的输出无法蒙混过关。
- 1,000 条专家撰写的过程描述，规模远大于流程图生成类论文常见的寥寥数个案例研究。
- 任务难度沿两条可分离的轴变化——单元操作复杂度与描述细节程度——因而解析难度可与工程难度区分开。
- 对比中含人类专家基线（100% SCR，8,301.91 s），使质量与耗时都有可解释的上界参照，而不只是模型之间互比。
- 设计耗时与收敛率并列报告，把效率变成显式的第二条评价轴，而非无人度量的副产物。

## Limitations

- 论文未说明 Simona 已公开发布，也未给出数据集网址或许可证；语料仅被描述为自建。
- 仿真依赖作者自研、经 HTTP 访问的仿真软件，因此结果无法在 Aspen Plus、HYSYS 或 DWSIM 这类通用工具上复现。
- 模型覆盖面窄：以 GPT-4o 为主要骨干，外加一次 Claude Sonnet 4 对比。
- 五个设计质量维度（经济可行性、环境可持续性、过程安全、技术可行性、拓扑合理性）只报告了分数，论文未给出评分细则或评分者一致性分析。
- Repository note: 该数据集是作为作者自家系统的评测载体提出的，因此所有报告的基线都由提出方自行运行，而非独立提交的结果。

## Related Works

- [CeProBench](./ceprobench.md) — 化工过程开发 benchmark，其概念与参数维度覆盖同样的「描述到流程图」和参数配置环节，并通过 Aspen Plus 判分。
- [FEABench](./feabench.md) — 工程 benchmark，成功的定义是通过 API 驱动商业仿真软件得到有效结果。
- [CFDLLMBench](./cfdllmbench.md) — 仿真配置 benchmark，以在 OpenFOAM 中的执行结果作为成功判据。
