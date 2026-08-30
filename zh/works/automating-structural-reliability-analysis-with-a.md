# Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework (2026)

> [English](../../works/automating-structural-reliability-analysis-with-a.md) | **简体中文**

> **首次公开：** 2026-07-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.16580)

## Overview

一个由五个 agent 组成的 LLM 框架，把构件级结构可靠度分析从自然语言题面一路做到给出可靠指标与失效概率并加以解读；随论文发布的还有一套留出的 20 题可靠度 benchmark，其参考解由经过验证的求解器给出，方法类别标签则由一条公开的确定性判据生成。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.16580>

## Summary

结构可靠度分析量化的是建筑或土木基础设施超出规定极限状态的概率，但要真正做一次，需要同时具备概率论、结构力学与数值仿真三方面的专长。论文搭建了一条多 agent流水线：问题表述、方法规划、求解器代码生成与结果解读由专门的 LLM agent 负责，而可靠指标 β 与失效概率 P_f 只由一个确定性的非 LLM 运行器调用经过验证的求解器算出——任何数值结果都不出自语言模型。整条流程中最难的一步判断，是事先选定哪一族可靠度方法既够准又代价可接受；论文把这一步单独交给 Method Planner，也是唯一经过微调的 agent，用 QLoRA 在 150 个由确定性参考判据打标的合成样例上适配得到。评估在一套留出的、与训练数据不相交的 20 道手工编写可靠度题目上进行，既用于端到端执行与参考解的对照，也用于在方法类别选择这一环节上独立比较三种模型配置。

## Tasks

留出的 benchmark 由 20 道手工编写的构件级结构可靠度题目组成，与用于微调 Planner 的 150 个合成样例不相交，且刻意构造成没有任何单一可靠度方法能一体适用于全部题目。论文报告的覆盖面为：11 种概率分布类型（正态、对数正态、Gumbel、Weibull、Fréchet、Beta、卡方、指数、Rayleigh、Type-I 最小值与 Type-III 最小值），问题维度从 2 个到 30 个随机变量，极限状态函数从线性一直到强非线性，失效概率则从常见事件跨到罕见事件。按确定性打标规则，这 20 道题分为 8 道 FORM 类、6 道 MCS 类与 6 道 Advanced 类。题目在结果表中逐一列名，且明显属于土木与结构范畴：抗力–荷载（R–S）算例、梁屈服、混凝土受压、欧拉柱屈曲、指数比值算例、三角函数振子、Weibull 疲劳、罕见的安全壳事件、相关桩群、十变量的海洋导管架、有界（Beta）抗力、Mohr–Coulomb 边坡、卡方振动、Fréchet 风极值、Rayleigh 波浪越浪、相关荷载下的桥梁主梁、30 变量并联系统、Type-I 最小值屈服、平移后的 Type-III 最小值算例，以及指数退化。每道题以自然语言题面呈现，agent 须从中提取随机变量及其分布与参数、极限状态函数与相关结构，选定方法类别，生成求解器代码，执行代码，并解读结果。论文全篇使用的示例是一根受欧拉屈曲的细长钢柱（题号 p04）。

## Domains

土木与结构工程。受评目标是结构构件与土木基础设施基于可靠度的安全评定——梁屈服、混凝土受压、柱屈曲、相关荷载下的桥梁主梁、海洋导管架、桩群与 Mohr–Coulomb 边坡——结果还要对照规范的目标可靠度水平来解读，例如 Eurocode EN 1990 中 50 年基准期下承载能力极限状态的 β = 3.8。这覆盖了该领域内结构分析、岩土工程与设计规范的范围。作者分属 University of Toronto、Seoul National University 与 Yonsei University 的土木工程系。题集中确有岩土（边坡稳定、桩群）与海洋（导管架结构、波浪越浪）方面的算例，但它们只是结构可靠度题集里的个别题目，而非独立受评的领域，因此不指派地球科学或能源系统作为共同领域。

## Evaluation

同一套留出的 20 题上跑了两项评估。**端到端执行**：当 Code Engineer 产出可执行代码、Runner 返回可解析的 β 与 P_f 估计值时，该次运行即记为成功；随后再把流水线给出的估计值与参考解对照。多数题目的参考解取自用经过验证的后端求解器逐题扫描得到的蒙特卡洛仿真结果；对于蒙特卡洛参考解达不到目标变异系数的罕见事件题，则改用子集模拟结果。框架跑完了全部 20 道题，每一题都生成了可执行代码并返回了有效的 β 与 P_f，可靠指标与参考解的偏差总体在 Δβ ≤ 0.1 以内。唯一一处实质性偏差是 p16（相关荷载下的桥梁主梁），流水线给出 β = 3.03，参考值为 β = 2.00——这是强非线性极限状态上的方法选择失误，而非代码执行失误；至于那些本可用更简单方法解决却选了高级方法的题目（p14、p18–p20），主要只是多花了算力，精度上并无实质损失。**方法选择准确率**：每道 benchmark 题目由确定性打标判据指定一个参考方法类别——β > 3.5 的罕见事件题一律归入 Advanced，不论非线性程度；其余情况下，若 FORM 估计与蒙特卡洛参考可靠指标的差距在 5% 以内则标为 FORM 类，否则标为 MCS。随后关闭流水线其余环节，只让 Planner 在每题的 ProblemSpec 上单独运行，把它预测的类别与参考标签对照；指标为类别准确率，按总体和分类别分别报告。三种开放权重配置收到完全相同的提示词：未微调的 Gemma 4 E4B（总体 45%）、未微调的 Gemma 4 26B-A4B（50%），以及仅对 Planner 做 QLoRA 微调的 Gemma 4 E4B（60%）。微调后的 Planner 把少数类别拉了回来——FORM 类 4/8、MCS 类 4/6、Advanced 类 4/6——而两个未微调模型在这些类别上都塌缩到 FORM 类一栏。

## Typical Duration

`N/A — the paper reports neither wall-clock time, token budget, nor trajectory length per problem.` 该工作流是一条固定的顺序流水线（Orchestrator → Problem Analyst → Method Planner → Code Engineer → Runner → Result Interpreter），而非开放式的 agent 循环；agent 不会自主回头修改或重跑前面的环节，且运行过程中会在四个 human-in-the-loop 关口暂停，因此耗时既取决于计算，也取决于用户何时响应。

## Main Contribution

按作者的表述，本文提出的是一个能端到端自动完成构件级结构可靠度分析、同时保持计算可信度的多 agent LLM 框架：把语言推理与数值计算分开，β 与 P_f 只由确定性地执行经验证求解器得出；结构化的数据契约让每一个中间产物都可追溯；此外，只对 Method Planner 做领域专用的 QLoRA 微调，在事先选择可靠度方法这件事上比单纯放大模型规模更有效。

## Key Design Ideas

- 五个 LLM agent 加一个确定性组件：Orchestrator（意图路由）、Problem Analyst（自然语言 → ProblemSpec）、Method Planner（方法类别选择，经 QLoRA 微调）、Code Engineer（spec + plan → 求解器代码）、Runner（非 LLM，在隔离子进程中执行代码并解析 β 与 P_f）与 Result Interpreter（数值 → 工程解读）。
- 五份带类型的数据契约固定了每一次交接——ProblemSpec、AnalysisPlan、GeneratedCode、ExecutionResult、EngineeringInterpretation——字段格式错误、随机变量缺失或极限状态函数写法不合规，都会在产生它的那一环被拦下；最终估计值也可以沿方法、代码、执行一路回溯。
- 数值结果绝不由 LLM 生成；Code Engineer 必须让代码在最后两行按固定格式打印 β 与 P_f，Runner 才能确定性地解析。
- 方法选择是一个只含三类的封闭集合——FORM 类（FORM、SORM、基于 FORM 的重要性抽样）、MCS，以及 Advanced（子集模拟、交叉熵重要性抽样、序贯重要性抽样、组合线抽样）——类别内具体用哪种方法，推迟到后面的关口再定。
- 只有 Planner 被微调：在 4 bit 量化并冻结的 Gemma 4 E4B 上做 QLoRA，适配器 rank 为 16、α = 16，训练 4 个 epoch，学习率 2 × 10⁻⁴，有效批大小 4，使用 8 bit AdamW 与线性调度，在单块 24 GB RTX A5000 上经 Unsloth 的 FastModel 加载器完成训练，视觉塔保持冻结。
- 论文明确把打标判据（β > 3.5 → Advanced；其余情况以 FORM 与 MCS 相差 5% 为界）当作一个可替换的设计选择：换掉它只需重新生成标签并重训 Planner，其他 agent 不受影响。
- Human-in-the-loop 确认关口在四个位置暂停工作流，其中包括类别确认，以及在 Advanced 类别下的具体方法选择；FORM 类的第一遍结果还可以用 SORM 或基于 FORM 的重要性抽样再细化一次。
- 全程使用开放权重模型，本地执行，不依赖任何闭源 API。

## Strengths

- 留出的 benchmark 刻意构造成没有哪一种方法能一体适用——11 个分布族、2 到 30 个随机变量、从线性到强非线性的极限状态、从常见到罕见的失效概率——而不是挑容易的算例。
- 参考解出自经过验证的求解器，并为蒙特卡洛参考解达不到目标变异系数的罕见事件题设了明确的兜底方案（子集模拟），因此真值本身站得住脚。
- 方法类别的打标规则以明确的确定性判据连同阈值一并公布，评分因此可复现，标签也可审计。
- Planner 评估把这一个决策从流水线其余部分中隔离出来，并让三种配置用完全相同的提示词，从而把微调的效果与模型规模的效果分开。
- 报告的是混淆矩阵而不只是总体准确率，因而暴露出真正要紧的失败模式——未微调模型一律退回 FORM 类，而这恰恰是非线性与罕见事件题上偏不安全的一侧。
- 端到端结果表把全部 20 道题的流水线 β、P_f 与参考值一并列出，论文还专门分析了自己最差的那一例（p16），而不是只报一个汇总结果。

## Limitations

- 只处理单一极限状态函数的构件级可靠度；含多个极限状态的体系可靠度留待后续，也没有纳入任何专门的体系可靠度算法。
- 极限状态函数必须能在生成的代码内直接求值——需要有限元分析这类外部数值模型的问题不在当前实现范围内，作者也把这一点认定为通向真实工程算例的主要障碍。
- 规范信息不是从权威文档检索得来的：概率模型由用户提供，目标可靠度水平则在解读环节用预设参考值加模型判断来处理。
- 即便是最好的配置，方法类别准确率也只有 60%；而 p16 说明类别选错可能一路传导成实质错误的可靠指标（β = 3.03，参考值为 2.00）。
- Repository note: 该 benchmark 规模很小（n = 20）且没有名字，参与比较的三种配置是同一个开放权重模型族的两种规模加上其中较小者的微调版，因此这场比较更接近作者对自家设计的消融，而不是跨系统的排行榜；分类别结果各自只建立在 6 到 8 道题上。
- Repository note: 源码、微调权重与 benchmark 题目均标注为「论文录用后在 GitHub 公开」，因此建卡时无法核实任何制品 URL。
- Repository note: 论文未报告任何成本、延迟或 token 统计，因此支撑方法选择这一动机的计算效率论证，并没有在 agent 侧得到实测。

## Related Works

- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — 设计上最接近的邻居：同样用一个专门构建的小型结构 benchmark，比较纯 LLM 与背靠经验证求解器的代码生成 agent。
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — 规模相当的手工整理结构分析题集，执行后端为 OpenSeesPy。
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — 同样是「自然语言 → 可执行求解器脚本」的模式，对照人工搭建的参考模型评分。
- [StructureClaw](./structureclaw.md) — 规模更大的可执行结构工程 agent benchmark，以与冻结参考求解器响应的数值一致性来验证。
