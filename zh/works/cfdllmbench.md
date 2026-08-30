# CFDLLMBench (2025)

> [English](../../works/cfdllmbench.md) | **简体中文**

> **首次公开：** 2025-09-19 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2509.20374)

## Overview

CFDLLMBench 是评估大语言模型计算流体力学（CFD）能力的三层 benchmark 套件，难度逐级递进：从研究生水平的 CFD 知识（CFDQuery），到生成 Python 求解器所需的数值与物理推理（CFDCodeBench），再到端到端的 OpenFOAM 算例配置与执行（FoamBench）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.20374>
- **Project:** <https://openreview.net/forum?id=kTcH1MnkjY>
- **Code:** <https://github.com/NREL-Theseus/cfdllmbench>
- **Venue:** Journal of Data-centric Machine Learning Research (JDMLR), 2026

## Summary

论文认为 CFD 是检验 LLM 科学能力的一块格外苛刻的试金石：它同时要求领域知识、数值方法选择以及长上下文下的软件操作；而此前的 CFD-LLM 评估往往止步于"生成的 OpenFOAM 算例能否跑起来"，并不追问由此得到的仿真在物理上是否正确。该套件被组织成三个难度递进、考察不同能力的层级，因此最终报告的是模型在各层上的能力剖面，而非单一聚合分数。其评估框架看结果而非实现方式：解答按可执行性、相对参考解的数值误差、以及在网格与时间步细化下的数值收敛性打分。论文在最难的一层上同时评估零样本 LLM 与 agentic 框架（MetaOpenFOAM、Foam-Agent）。

## Tasks

三个组成部分，共 240 个任务：

- **CFDQuery** — 90 道由三位领域专家整理的多项选择题，考察流体力学、线性代数与数值方法；素材改编自网络抓取内容与 CFD 讲义，且为本 benchmark 专门创建。
- **CFDCodeBench** — 24 个要求模型生成 Python 代码来数值求解给定 PDE 的问题。每题给出控制方程、边界与初始条件、空间与时间域以及需要计算并保存的目标变量。覆盖 1D 与 2D、线性与非线性 PDE，横跨流体力学、热输运与湍流；参考解或为闭式解析表达式，或为专家撰写的 Python 实现，平均每题 70 行代码。题目整理自公开 GitHub 仓库与既有资料，其中进阶题的描述由专家撰写。
- **FoamBench** — 126 个 OpenFOAM 算例，覆盖 15 种以上不同的几何与物理场景，分为 **Basic**（110 个算例，由 11 个 OpenFOAM tutorial 按算例逐一改变边界条件与参数派生而来）与 **Advanced**（16 个由 CFD 专家手工设计、刻意不同于 tutorial 的算例，要求模型根据自然语言 prompt 自行选择湍流模型、创建新几何并生成合适的网格）。Prompt 会说明物理场景、几何、边界条件、参数、湍流模型、时间步、求解器与保存间隔。

## Domains

计算流体力学及相邻的科学计算领域：流体力学、热输运、湍流建模、数值方法与离散格式、网格生成，以及 OpenFOAM 工作流操作。

## Evaluation

- **CFDQuery。** 多项选择准确率，以 Success Rate 报告。
- **CFDCodeBench。** 四个指标：**可执行性** `M_exec`（二值，类似 pass@1）；**相对误差** `M_NMSE`，在仿真终止时刻对照参考解计算归一化均方误差百分比，并按 NMSE ≤10%、10–30%、>30% 三档分别记 1 / 0.5 / 0——论文说明这两个阈值取自工程实践，并有实证敏感性分析支撑；**数值收敛性** `M_conv`（同时细化空间与时间离散，若误差下降则记 1）；以及一个严苛的 **Success Rate**，只统计三项全部为 1 的题目。
- **FoamBench。** **可执行性** `M_exec`；**目录与文件结构** `M_struct`（用 ROUGE 相似度比较生成的工程结构与参考算例）；**文件相似度** `M_file`（对文件内容做 ROUGE）；**相对误差** `M_NMSE`，方式同上。此处的 Success Rate 要求 `M_exec` 与 `M_NMSE` 同时为 1——结构与文件相似度仍会报告，但不作为成功与否的门槛。
- **看结果而非方法。** 只要误差在容差内且解收敛，采用不同但有效的数值算法（有限差分对有限体积）同样判为正确；论文明确表示该 benchmark 不惩罚算法多样性。论文还指出代码相似度指标并不适用，因为仿真代码写法差异极大却可能给出等价的解。
- **实验设置。** 全程使用 OpenFOAM v10。CFDQuery 与 CFDCodeBench 采用零样本 prompt。FoamBench 既做零样本评估，也在两个 agentic 框架（MetaOpenFOAM 与 Foam-Agent）下、以三种配置（RAG + Reviewer、有 RAG 无 Reviewer、有 Reviewer 无 RAG）评估，以便分离各组件的贡献。
- **报告结果。** 性能沿层级急剧下滑。CFDQuery 上所有闭源模型表现良好，o3-mini 以 92% 领先，开源模型为 60%。CFDCodeBench 的最佳 Success Rate 约为 14%。FoamBench 上最佳配置——Foam-Agent 搭配 RAG 与 Reviewer、基于 Claude Sonnet 3.5——在 Basic 上为 34%、Advanced 上为 25%。同一层级下零样本 prompt 则彻底崩溃：Sonnet 3.5 在 Basic 上 Success Rate 仅 0.045、Advanced 上仅 0.007。在 Basic 上以 Sonnet 3.5 + RAG + Reviewer 对比两个框架，Foam-Agent 达到 0.336（`M_exec` 0.836、`M_NMSE` 0.427），而 MetaOpenFOAM 为 0.136（`M_exec` 0.555、`M_NMSE` 0.173）；去掉 Reviewer 后 Foam-Agent 降至 0.200。Sonnet 3.5 的优势伴随成本溢价——平均每次运行 $6.56，而 GPT-4o 为 $0.42（API 价格以 2025 年 5 月为准）。

## Typical Duration

论文未以 wall-clock 报告。规模改由成本与循环次数体现：agentic 的 FoamBench 配置每次运行平均消耗约 63k–379k token（随模型与框架而异），其中 Foam-Agent 在 Sonnet 3.5 上平均 2 次 reviewer 循环，而对比配置为 7 次。CFDCodeBench 的解答平均 70 行代码；FoamBench 则需要生成完整的 OpenFOAM 算例目录并把求解器跑到结束。

## Main Contribution

第一个在三个层级上整体评估 LLM 之 CFD 能力的 benchmark——研究生水平知识、数值与物理推理、以及实际仿真工作流自动化——并配以基于执行的评估框架，考察物理准确性与数值收敛性，而不只看可执行性或文本相似度。

## Key Design Ideas

- 三个难度递进的层级分离出不同能力，使得知识分数再高也无法掩盖"跑不出仿真"这一事实。
- 物理准确性通过与参考解的数值比对来评分，且 NMSE 分档对齐工程实践，而非随意选定。
- 数值收敛性是一个显式指标：在网格与时间步细化下重新运行，检查误差是否真的下降——这是任何代码相似度指标都无法察觉的性质。
- Success Rate 被有意设计得严苛（各分项指标的合取），从而把"部分能力"与"真正可用的仿真"区分开。
- Advanced split 的构造刻意让检索失效：算例与 tutorial 不同，迫使模型真正构建几何与网格，而不是改写某个相近范例。
- Agentic 框架以可消融的配置（RAG、Reviewer）而非整体黑箱来评估，因而每个组件的贡献都可被测量。

## Strengths

- 评价的正是 CFD 从业者真正在意的东西——仿真能否运行、结果在物理上是否正确、是否收敛——而不是有没有生成文件。
- Basic / Advanced 的划分干净地区分了"贴近 tutorial 的能力"与"开放式工程能力"，且实测二者差距很大。
- 接受任何有效的数值方法，避免惩罚合理的实现多样性。
- 在报告能力的同时报告成本，揭示出 FoamBench 上最强的模型每次运行贵出一个数量级以上。
- 除 CFDQuery 外各层级均留有充足提升空间；套件以 BSD 3-Clause 许可证发布并公开代码。

## Limitations

- 作者把空间推理点名为一处主要短板而非已解决的变量：在 Advanced 的 `doubleSquare` 算例中，prompt 已精确给出障碍物位置，生成的几何与网格却仍然错误，论文称 LLM 的几何理解是亟需改进的主要方向。
- 作者指出部分被测模型存在约 8,000 token 的内部上下文窗口限制（涵盖 prompt 与输出），且 o3-mini 不允许设置 temperature（其默认值未公开），因此各模型的配置并非完全一致。
- Repository note: FoamBench Basic 的 110 个算例由 11 个 tutorial 算例通过改变边界条件与参数派生而来，因此同一族内的算例并不相互独立；而刻意区别于 tutorial 的 Advanced split 只有 16 个算例。
- Repository note: `M_struct` 与 `M_file` 是相对某个特定参考算例目录的 ROUGE 相似度，因而会奖励"与参考布局相像"；但按设计它们并不作为 Success Rate 的门槛，后者只取决于执行与数值误差。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — 同样在受控环境中评估科学计算工作流，但采用确定性 pytest 验证，而非数值误差与收敛性评分。
- [ScienceAgentBench](./scienceagentbench.md) — 同样对照专家验证的参考实现来评判科学代码的执行结果，但覆盖数据驱动的发现类任务，而非单一仿真领域。
- [Stargazer](./stargazer.md) — 同样以物理一致性反馈评分迭代式科学模型拟合，领域为天文学而非流体力学。
- [T-Eval](./t-eval.md) — 同样把一项能力拆成分别打分的层级，但依据的是 tool-use 子过程，而非知识 / 推理 / 实现的深度递进。
