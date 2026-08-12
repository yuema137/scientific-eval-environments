# Mechanical & Aerospace Engineering

> [English](../../domains/mechanical_aerospace_engineering.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

机械与航空航天工程。计算流体力学与热输运折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| CFDLLMBench | 2025 | 三个深度上的计算流体力学：研究生水平知识（CFDQuery）、用 Python 数值求解给定 PDE（CFDCodeBench）、端到端 OpenFOAM 算例配置与执行（FoamBench）。 | 240 个任务：90 道专家整理的选择题、24 个 PDE 求解器编程题、126 个 OpenFOAM 算例（110 个由 tutorial 派生 + 16 个刻意不同于任何 tutorial 的专家手工算例）。 | 执行加对照参考解的分档归一化误差（NMSE），以及网格与时间步细化下的显式收敛检查；接受任何有效的数值方法。 | [→](../works/cfdllmbench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Engineering Sciences 分组下的机械工程任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| SimBench | 2024 | 在 Chrono 仿真器中为多体动力学、FEA、车辆动力学、机器人动力学与传感器仿真生成数字孪生。 | 34 个物理系统上 102 个演示任务（官方仓库），经多轮对话构建；比较 33+ 个 LLM。 | 带预定义规则与人在环指导的 LLM judge 评分。 | [→](../works/simbench.md) |
| FEM-Bench | 2025 | 为计算力学问题——力、变形、约束——编写有限元函数与单元测试。 | 与研究生课程对齐的 33 个任务、两条赛道，每个模型-任务对五次尝试。 | 客观验证；测试编写用 Average Joint Success Rate。 | [→](../works/fem-bench.md) |
| RealPDEBench | 2026 | 基于与数值模拟配对的真实测量数据，预测流体与热工程系统——流固耦合、圆柱与翼型绕流、燃烧。 | 五个真实测量数据集配成对模拟与三类真实-模拟对比任务；评估科学 ML 代理模型而非 LLM agent。 | 十个基线上的八项数据导向与物理导向指标。 | [→](../works/realpdebench.md) |
| FEABench | 2025 | 通过 API 操作 COMSOL Multiphysics，用有限元分析端到端求解多物理场工程问题。 | 以自然语言给出问题描述；agentic 设定下对照软件反馈迭代 API 调用。 | 对生成 API 调用与计算答案的评估，API 调用可执行率为主要指标。 | [→](../works/feabench.md) |
| MooseBench | 2026 | 生成求解预期物理的多物理场有限元模拟代码（MOOSE），而不只是能跑的代码。 | 220 个带 PDE 级数学真值的算例。 | 经确定性 PDE 重构的 Intent Fidelity Score；只修执行错误时 39–40% 的算例保持「能跑但物理错误」。 | [→](../works/moosebench.md) |
| SciConvBench | 2026 | 澄清不适定的仿真请求；流体力学与固体力学是其四个计算科学领域中的两个。 | 基于结构化任务本体的多轮消歧与矛盾消解对话。 | 按评分标准为澄清行为、对话共识建立与最终规格保真度打分。 | [→](../works/sciconvbench.md) |
| AInsteinBench | 2025 | 解决生产级科学仓库中的维护者 PR 任务；流体力学在其六个代码库之列。 | 可执行环境中的仓库级 coding agent 任务。 | 经专家评审整理的测试驱动验证。 | [→](../works/ainsteinbench.md) |
| ERI Benchmark | 2026 | 机械工程与航空航天工程是该 benchmark 覆盖的九个领域中的两个：前者涵盖热力学、流体力学、传热、机械设计、动力学与振动、制造与暖通空调，后者涵盖空气动力学、飞行力学、推进、航空航天结构与轨道力学。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对），各领域的均分单独报告。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商的模型组成评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值；在所有受评模型上，航空航天工程都属最难的领域之列。 | [→](../works/eri-benchmark.md) |

## Related Works

- [CFDLLMBench](../works/cfdllmbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [SimBench](../works/simbench.md)
- [FEM-Bench](../works/fem-bench.md)
- [RealPDEBench](../works/realpdebench.md)
- [FEABench](../works/feabench.md)
- [MooseBench](../works/moosebench.md)
- [SciConvBench](../works/sciconvbench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
