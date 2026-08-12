# AutoBM / BMEval (2026)

> [English](../../works/autobm.md) | **简体中文**

## Overview

AutoBM 定义了这样一项任务：依据自然语言的结构描述，生成可执行且物理自洽的 OpenSeesPy 建筑模型代码。配套的 BMEval 则是一个以验证为驱动的 benchmark，含 128 个经专家验证的建模任务，按沙箱执行、自振周期吻合度与设计规范符合性三方面判分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2602.07083
- **Code:** https://github.com/Jovanqing/AutoBM
- **Venue:** KDD 2026 (32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining), DOI
  10.1145/3770855.3818987

## Summary

论文把自动建筑建模（Automatic Building Modeling, AutoBM）形式化为条件式程序合成：给定结构描述（建筑功能、平面尺寸、层高、抗震设防烈度）、一组物理与工程约束，以及目标建模 API，模型须产出 OpenSeesPy 代码，且该代码执行后能给出物理上有效的结构响应。围绕这项任务，论文发布了三样成果——CivilInstruct 指令语料、BMEval 评测 benchmark，以及 RLA-SPC：一套「两阶段监督微调 + 物理约束 GRPO 对齐」的流程。十六个开源与商业 LLM 在统一协议下于 BMEval 上评分，微调结果则以同一 benchmark 上的前后对比形式报告。

## Tasks

BMEval 含 128 个带标注的评测样本，构建分三步：先在合理的结构参数范围内，于多样的属性空间（建筑功能、层高、平面尺寸）中随机生成建筑样本；再由一套专家驱动的机制严格依照抗震设计规范对每个设计方案作优化与验证，以保证结构可行性；最后由经验公式给出每个结构的自振周期，作为 ground-truth 参考值。每个样本都带有完整的建筑信息及其对应的结构周期。另一份独立的 CivilInstruct 训练语料由四部分构成——约 3,800 条由 OpenSeesPy 文档合成的 API 学习样本、3,100 条专家级的「指令—代码」实例、3,500 条执行报错的调试思维链样本，以及 512 条得分高于 90/100、并标注了有限元结构周期的物理感知专家样本。生成的程序一般在 600 行左右，涵盖建模、分析与校验。

## Domains

土木与结构工程。每个受评实例都是一栋建筑：模型须为钢筋混凝土框架布置节点与单元，指派截面与材料，施加与所述抗震设防烈度相符的荷载，运行模态分析求出一阶自振周期，并输出对照设计规范的校核结论。中国抗震与混凝土设计规范中的领域知识——GB 50011-2010、GB 50010-2010 与 JGJ 3-2010——被嵌入提示模板，JGJ/T 415-2017 则用于指导数据构建实践。这是应用于结构的地震工程，而非地震危险性科学；未指派共同领域，因为代码生成这层外衣服务的是结构目标，而不是一项通用的软件工程任务。

## Evaluation

每个测试样本都独立生成 n 份候选程序，在受限沙箱中依次执行；程序若在规定时限内正常终止，即计为成功。评测采用 HumanEval/MBPP 的无偏 pass@k 估计量，并在其上叠加三种任务专属的变体。Pass@k_period 要求由确定性规则匹配从程序输出中提取的一阶自振周期，与 ground-truth 值的相对误差落在 0.30 的阈值以内。Pass@k_compliance 要求输出给出满足设计校核判据的明确结论，检测方式是带否定处理的保守关键词匹配。Pass@k_strict 要求三者同时成立：干净执行、周期在容差内，以及明确的符合性结论。结果取 BMEval 五次扰动评测的平均值，并报告标准差。最好的成绩是 Claude-Sonnet-4.5 的 52.34 Pass@1、80.16 Pass@5 与 17.97 Pass@5_strict，以及 Gemini-3-pro-Preview 的 32.03 Pass@5_period；所有 7B–8B 的代码专用模型在工程级平均分上都低于 3.0，GLM-4.6 的 Pass@5_strict 为 0.00。

## Typical Duration

N/A — 论文未报告单任务的 wall-clock 时间或 token 预算。唯一给出的执行约束是一个规定的沙箱时限，超时即判为超时失败；生成的程序则被描述为每份约 600 行。

## Main Contribution

作者提出一套物理感知的 LLM 自动建筑建模框架，由三部分组成：CivilInstruct 领域数据集、以结构与物理约束为导向的两阶段微调策略，以及作为验证驱动型 benchmark 的 BMEval——后者通过闭环验证，对可执行性与结构动力一致性给出具工程意义的评估。

## Key Design Ideas

- 正确性由闭环仿真而非文本相似度定义：生成的程序真的在 OpenSees 沙箱中执行，其模态输出再与参考周期比对。
- 指标阶梯把三类不同的失效面分开——能不能跑起来、数值对不对、有没有给出符合性结论——Pass@k_strict 则把三者合取。
- ground-truth 周期来自经专家验证的设计方案、由经验公式算出，给出的是一个定量的物理目标，而不是一份评分细则的判断。
- 基于容差的周期奖励沿用工程实践的做法，在 10%、20% 与 40% 的相对误差带上分级给分，而不是一刀切的通过/不通过。
- 训练奖励分解为格式符合性（权重 0.05）、跨 OpenSeesPy 三层 API（拓扑、边界/荷载、分析/求解器）的层级 AST 逻辑完备性项（0.25），以及沙箱执行（0.70）。
- 调试数据以真实 bug 为源：3,500 条思维链样本取自 OpenSeesPy API、求解器与建模逻辑相互耦合而引发的真实执行失败，而非人为构造的缺陷。

## Strengths

- 判分落在一个实际算出来的物理量上——自振周期——而不是用文本相似度或 LLM judge 这类代理指标去评判生成的代码。
- 模型覆盖面广：十六个系统横跨代码专用模型、开放权重通用模型与前沿推理模型，每个都给出五次扰动评测的标准差。
- benchmark 能把模型能力与框架能力清楚分开，因为它以完全相同的方式施加于未调基线与微调后的 checkpoint。
- 失败模式按类别报告，指出未闭合的字符串字面量占可执行性失败的 95.7%，位移角限值超标则是符合性失败的主因。
- 设计规范的来源写得明确，点名了任务中嵌入的具体中国标准。

## Limitations

- 框架局限于弹性结构分析与简化的二维钢筋混凝土框架；非线性分析与三维相互作用未纳入。
- 研发以中国抗震设计规范为基准，对其他国家设计规范的泛化能力未作系统验证。
- 符合性检测依靠对程序打印结论作保守的关键词匹配，因此它判的是「有没有用可识别的措辞给出结论」，而不是独立重算这项校核。
- 作者指出，复杂工况下仍可能出现隐蔽的工程缺陷，并把 AutoBM 定位为辅助而非取代专业设计、专家审查或法定审查。
- Repository note: 论文自身的命名并不统一，摘要、章节标题与正文分别用 BMEval、MBEval 与 BMBench 指代同一个 benchmark；结果表中用的是 BMEval。
- Repository note: 绝对分数普遍偏低——最强模型在严格联合指标上也只到 17.97——因此该 benchmark 目前主要在难度区间的低端起区分作用。

## Related Works

- [MASSE](./masse.md) — 同样评测 LLM 驱动的 OpenSeesPy 结构建模，但判的是由 LLM judge 按细则打分的工作流日志，而非执行得到的模态输出。
- [StructureClaw](./structureclaw.md) — 结构工程 agent benchmark，校验结构模型匹配以及与冻结参考求解器响应的数值一致性。
- [FEM-Bench](./fem-bench.md) — 计算力学领域的代码生成 LLM benchmark，采用客观的单元测试验证。
- [FEABench](./feabench.md) — 通过 API 操作 COMSOL 的有限元 agent benchmark。
- [CodePDE](./codepde.md) — 可执行科学代码生成，判分方式是运行产出的求解器。
