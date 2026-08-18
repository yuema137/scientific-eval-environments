# 实验设计与科学发现

> [English](../../activities/experiment_design_discovery.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 决定如何获取科学信息或推断新的科学结构的能力——设计实验、规划观测、选择测量、生成并检验假设，以及发现规律。

## Scope

涵盖 agent 自主选择实验或观测的交互式与模拟实验、符号规律发现，以及假设或想法生成。与实验室与仪器控制相区分（决定测什么 vs. 物理执行装置）；仅仅环境是模拟的，并不使任务归入模拟与科学计算。

## Task Patterns

一大类工作把科学发现设定为**在物理规律隐藏的模拟世界中进行交互式实验**：agent 反复提出实验、观察输出，最终提交支配性的规律。[NewtonBench](../works/newtonbench.md) 通过 run_experiment 工具在经过反事实改动的物理定律上开展实验，[PhysGym](../works/physgym.md) 增加了可控的先验知识分级，[Gravity-Bench-v1](../works/gravity-bench.md) 探究模拟的二体系统，[DiscoverPhysics](../works/discoverphysics.md) 要求在 N-body 世界中既给出解释又给出 Python 形式的规律，[SciGym](../works/scigym.md) 则围绕隐藏的 SBML 系统运行一个 systems-biology 的干实验室。其中一些工作把发现过程明确地与**资源/测量预算**挂钩：[MaD Physics](../works/mad-physics.md) 在固定上限下按精度为每次观测定价，[Gravity-Bench-v1](../works/gravity-bench.md) 则对数据采集加以约束。

**符号方程 / 假设再发现**这一类工作在抑制记忆的前提下评估对规律或假设的复原能力。[LLM-SRBench](../works/llm-srbench.md) 把方程改写成陌生的形式并加入合成问题，[MOOSE-Chem](../works/moose-chem.md) 则再发现训练截止之后的化学假设。对已发表成果的全流程再发现见于 [EXP-Bench](../works/exp-bench.md) 和 [FIRE-Bench](../works/fire-bench.md)，其中 agent 需设计并执行实验以复现已记录的结果。

**想法与假设生成**由模拟专家或专家评审团式的指标来评分：[IdeaBench](../works/ideabench.md) 让构思立足于有影响力论文的背景，[LiveIdeaBench](../works/liveideabench.md) 从单个关键词考察发散性思维，[Materials Hypothesis Generation](../works/materials-hypothesis.md) 生成以目标和约束为导向的材料假设。与之相关的、偏规划的预测类工作有 [AlchemyBench](../works/alchemybench.md)（合成配方）和 [MLRC-Bench](../works/mlrc-bench.md)（提出新颖的 ML 方法）。两项天文工作把这条脉络朝相反的方向各推了一步。[CLASS 模型构建框架](../works/an-llm-driven-framework-for-cosmological-model-bui.md) 把自提假设的回路闭合了起来：agent 自己发明一个暗能量模型、把它实现出来，随后的评分不来自 judge，而来自对照真实 DESI、Planck、Pantheon+ 与 SH0ES 数据算出的似然、BIC 与 Hubble 张力奖励。[AI 辅助课题规划研究](../works/ai-assisting-research-ii-project-planning.md) 则把科学问题固定住，只评那份计划本身——方法、数据集与工具、可行性、时间安排与风险——在盲评中与专家撰写的计划书相比，从而把规划质量与选题质量剥离开来。

最后一类工作把发现刻画为**面向某一结论的序贯信息获取**，且往往伴随成本约束。临床诊断类基准 [AgentClinic](../works/agentclinic.md) 和 [SDBench](../works/sdbench.md) 要求逐步问诊获取发现、按成本安排检查，然后再给出诊断结论；[MolQuest](../works/molquest.md) 把化学结构解析变成一个不断选择采集哪些谱图的溯因循环；[SciAgentArena](../works/sciagentarena.md) 则涵盖真实的生物医学发现与优化任务，并带有逐步验证。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AgentClinic | 2024 | 不完全信息下的序贯临床诊断 | 模拟的医患问诊，9 个专科、7 种语言、多模态 | 通过采集病史/检查确定正确诊断 | [卡片](../works/agentclinic.md) |
| IdeaBench | 2024 | 立足论文背景的研究想法生成 | 基于有影响力论文标题/摘要及参考文献的静态单轮生成 | 由 GPT-4o 排名 + Insight Score 评分的新颖想法 | [卡片](../works/ideabench.md) |
| LiveIdeaBench | 2024 | 从极简背景出发的发散思维式科学构思 | 单关键词提示，1,180 个关键词、22 个领域、40+ 个模型 | 由 LLM 评审团在 5 个创造性维度上评分的想法 | [卡片](../works/liveideabench.md) |
| MOOSE-Chem | 2024 | 再发现未见过的化学假设 | 51 篇 2024 年之后的标注论文，3,000 篇论文的灵感语料库 | 复原论文隐藏的假设，与 ground truth 高度相似 | [卡片](../works/moose-chem.md) |
| AlchemyBench | 2025 | 端到端的材料合成规划 | 基于 17,000 份专家核验配方的静态预测 | 材料/流程/表征由 LLM-as-Judge 评分 | [卡片](../works/alchemybench.md) |
| Cosmological Model-Building with CLASS | 2025 | 提出新的暗能量模型并探索其参数 | 一次性的模型发明，外加在 CLASS 中手动探索参数 | 对照 DESI/Planck/SH0ES 数据的似然、BIC 与 Hubble 张力奖励 | [卡片](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| EXP-Bench | 2025 | 完成完整的 AI 研究实验 | 来自 51 篇 NeurIPS/ICLR 2024 论文的 461 项任务，起始代码不完整 | 设计、实现、执行、分析；12,737 个可评分子任务 | [卡片](../works/exp-bench.md) |
| Gravity-Bench-v1 | 2025 | 面向引力发现的有预算观测规划 | 交互式模拟二体系统，OOD 物理，约 100 点预算 | 从采集到的观测中刻画隐藏的物理规律 | [卡片](../works/gravity-bench.md) |
| LLM-SRBench | 2025 | 抗记忆的符号方程发现 | 239 个问题（LSR-Transform、LSR-Synth），四个领域 | 复原支配方程；最佳符号准确率 31.5% | [卡片](../works/llm-srbench.md) |
| Materials Hypothesis Generation | 2025 | 目标驱动、约束导向的假设生成 | 基于精选近期期刊论文数据集的静态生成 | 由可扩展的模拟专家指标评分的假设 | [卡片](../works/materials-hypothesis.md) |
| MLRC-Bench | 2025 | 提出并实现新颖的 ML 研究方法 | 脚手架下的 7 项竞赛任务 | 缩小 baseline 到人类的差距；最佳 agent 缩小 9.3% | [卡片](../works/mlrc-bench.md) |
| NewtonBench | 2025 | 交互式科学定律发现 | 324 项任务，改动过的定律，run_experiment 工具，难度分级 | 以符号表达式提交隐藏的目标定律 | [卡片](../works/newtonbench.md) |
| PhysGym | 2025 | 带可控先验的交互式物理发现 | 97 个精选问题，100 次实验预算，四种先验知识分级 | 提交关于支配物理定律的假设 | [卡片](../works/physgym.md) |
| SciGym | 2025 | systems-biology 干实验室中的迭代实验设计 | 隐藏的 SBML 系统；137 个小型系统参与评测，350 个已发布 | 提交假设的 SBML 机制并与 ground truth 比对 | [卡片](../works/scigym.md) |
| SDBench | 2025 | 有预算的序贯诊断 | 304 个 NEJM-CPC 病例，gatekeeper 按需揭示发现 | 在准确率-成本前沿上评分的诊断结论 | [卡片](../works/sdbench.md) |
| AI-Assisted Project Planning in Astrophysics | 2026 | 为一个研究课题规划方法、数据、工具与时间安排 | 覆盖 8 个专家设计课题的 32 份一页纸计划书；盲评 | 四位人类评审与两位 LLM 评审依四方面 1–5 分 rubric 打分 | [卡片](../works/ai-assisting-research-ii-project-planning.md) |
| DiscoverPhysics | 2026 | 发现反事实模拟世界的规律 | 22 个 N-body 世界，迭代实验，原始轨迹数据 | 提交解释加 Python 规律；轨迹 MSE + 评分量表 | [卡片](../works/discoverphysics.md) |
| FIRE-Bench | 2026 | 对已发表 ML 成果的全流程再发现 | 40 项已执行任务 + 60 篇论文池，仅给研究问题 | 设计/运行实验以再发现成果；最佳 F1 <50 | [卡片](../works/fire-bench.md) |
| MaD Physics | 2026 | 有预算的测量规划与定律推断 | 三个 JAX 模拟器（经典/流体/量子），改动物理的变体 | 在按精度定价的预算下推断定律以预测未来状态 | [卡片](../works/mad-physics.md) |
| MolQuest | 2026 | 智能体式化学结构解析 | 多轮谱图采集（NMR/MS），迭代精化 | 正确结构；SOTA 约 50% | [卡片](../works/molquest.md) |
| SciAgentArena | 2026 | 跨尺度的真实世界科学研究 | 约 200 项逐步验证的任务，五个生物医学领域，与 agent 无关 | 完成数据分析/优化/发现/有效性类任务 | [卡片](../works/sciagentarena.md) |
| Apodex Discovery | 2026 | 在带隐藏验证器的可执行环境中求解真实世界的发现问题 | 覆盖 561 个行业的调研从 423 个候选中选出 20 个问题；环境有状态，自带工具、数据与预算 | 隐藏验证器给出的结果，外加盲评的六维过程分；衣壳设计比已发表的最好水平高出 7% | [卡片](../works/apodex-discovery.md) |

## Related Works

- [AgentClinic](../works/agentclinic.md)
- [IdeaBench](../works/ideabench.md)
- [LiveIdeaBench](../works/liveideabench.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [AlchemyBench](../works/alchemybench.md)
- [EXP-Bench](../works/exp-bench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [LLM-SRBench](../works/llm-srbench.md)
- [Materials Hypothesis Generation](../works/materials-hypothesis.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [NewtonBench](../works/newtonbench.md)
- [PhysGym](../works/physgym.md)
- [SciGym](../works/scigym.md)
- [SDBench](../works/sdbench.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [FIRE-Bench](../works/fire-bench.md)
- [MaD Physics](../works/mad-physics.md)
- [MolQuest](../works/molquest.md)
- [SciAgentArena](../works/sciagentarena.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation](../works/ai-assisting-research-ii-project-planning.md)
- [Apodex Discovery](../works/apodex-discovery.md)
