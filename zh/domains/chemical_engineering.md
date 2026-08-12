# Chemical Engineering

> [English](../../domains/chemical_engineering.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

化学过程工程——化工过程与装置的设计、仿真、优化、运行与安全——与作为科学的 Chemistry 区分。本页收录的工作，评测的内容包括工艺流程搭建与依托仿真器的设计（Aspen Plus、IDAES/Pyomo）、操作参数优化、过程控制与监控层故障恢复、HAZOP 与 P&ID 校核一类的过程安全分析，以及贯穿物料与能量衡算、热力学、传递现象、反应动力学与分离过程的化工知识与计算。分子、反应与材料层面的问题归 Chemistry；一项工作所评测的目标只有落在过程或装置层面的决策上才归入本页，而评测确实横跨两者的工作会在两页同时列出。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Engineering Sciences 分组下的化学工程任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| CeProBench | 2026 | 围绕三大支柱评测化工过程开发：知识（工艺路线、催化剂、分离技术）、概念（工艺流程图的解析、补全与设计）与参数（操作参数优化）。 | 六类任务，含 243 道问题与 235 项具体任务；素材来自 70 份技术文档（4,406 个实体 / 4,967 条关系）、113 张竞赛来源的 PFD（986 个设备单元、1,172 条连接）与 20 个 Aspen Plus 参数文件（91 个可调参数、65 个目标）。 | 参数类任务把候选设定放进 Aspen Plus 实际运行来评分，借此校验化学与热力学可行性；知识与概念类任务则对照专家标注的图谱，用实体 F1、MEC/MED 及设备与连接准确率评分。 | [→](../works/ceprobench.md) |
| Simona | 2026 | 把文字描述的化工过程转成能收敛运行的仿真流程图——既要给出单元操作拓扑，也要给出操作配置。 | 由化学工程专家撰写的 1,000 份过程描述，在单元操作难度与描述详略两个维度上有梯度变化。 | 以 Simulation Convergence Rate（收敛设计数占需求总数之比）为准，由作者的过程仿真器经 HTTP API 实际运行判定；结果连同设计耗时一并报告，并与 LLM、多 agent 及人类专家基线比较。 | [→](../works/simona.md) |
| CRAFTS | 2026 | 自动搭建可执行的 IDAES/Pyomo 过程仿真模型：选取单元操作、构建拓扑、指定物性包、补齐规格、初始化、处理循环物流与诊断求解器。 | OpenIDAES-450：450 条面向用户的请求，各自配有可执行的 IDAES 模型与运行记录，其中 82 条冻结为留出测试集。 | 以 Staged Workflow Success 契约为准，由确定性的 IDAES/Pyomo 晋级门把关（接口兼容、自由度闭合、初始化通过、求解器终止状态可接受）；另在单元记录、物流记录与有向连接上计 macro-F1。 | [→](../works/crafts.md) |
| A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents | 2026 | 化工装置中的监控层故障恢复：在泵故障与性能退化、主管路堵塞、泄漏、换热器结垢与冷却阀饱和之后，把模块化间歇混合单元和连续搅拌釜反应器拉回安全运行状态。 | 两个开放发布的可执行 Python 环境，支持带类型、可配置的故障注入与可插拔的恢复/验证接口；提供参数化的场景生成器，而非固定的任务清单或数据划分。 | 不给任务总分，而是逐个动作验证：符号验证器对照装置结构检查状态可达性与执行机构是否存在，仿真验证器则在数字孪生中把动作向前推演，只有不安全暴露被限制在界限以内时才予放行。 | [→](../works/ctrl-alt-recover.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | 让 LLM 推理安全地进入工业过程控制，在化工装置场景上评测——三个源自 Tennessee Eastman Process，另有一个聚合反应器与一台干燥器。 | 五个兼有连续与间歇运行的装置场景、一组 43 条人工构造的错误注入提案、N = 50 的重复运行鲁棒性研究，以及 B0–B3 的上下文消融阶梯。 | 在装置 P&ID 上做确定性图遍历，逐条检查所提控制动作的位号是否存在、是否可执行、失效状态是否一致以及下游影响；验证器的召回率对照注入的错误集测量。 | [→](../works/aae-framework.md) |
| Can Large Language Models Automate the HAZOP Process Without Human Intervention? | 2026 | 流程工业中的危险与可操作性分析：由一张管道及仪表流程图产出完整的 HAZOP 工作表——偏差、原因、后果与安全措施。 | 每个模型拿到同一张 P&ID 与同一条标准化提示，四个多模态 LLM 各自在无人干预下生成一份完整工作表。 | 对照专家编制的参考工作表，分两组彼此独立的指标比较：一是相似度（F1，四个模型均高于 86%）与单份工作表成本，二是场景的语义有效性（0.19–0.37）与安全措施的多样性。 | [→](../works/can-large-language-models-automate-the-hazop-proce.md) |
| PSE-Bench | 2026 | 四个方向上的过程系统工程咨询：过程建模与仿真、过程优化、面向化工过程的机器学习，以及过程设计与系统工程（HAZOP、LOPA、全厂控制、FEED）。 | 200 道开放式问题，每个方向 50 道，采用单轮零样本作答；随题公开参考答案与逐题 rubric。 | 五个独立的 LLM judge 依七要素 rubric 为每份回答打分，再与 ROUGE-1、ROUGE-L、余弦相似度和 rubric 要素覆盖率合成综合分，并与三位领域专家的评分对照校验（rs = 0.416，ICC = 0.793，宽松度偏移 +0.85）。 | [→](../works/pse-bench.md) |
| ChemEBench | 2025 | 从基础知识一路到应用型专业技能的化工能力——反应与分离设备、精馏与萃取、换热器、过程与工厂安全、过程经济性，以及工厂工程建设。 | 三个递进层级，覆盖 15 个维度、101 个不同任务；题型分客观（选择、填空、判断）与主观（简答、计算）两类；比较 14 个模型。 | 客观题计准确率；主观题按完整性与清晰度打 0–5 分，并逐步核查推理链中的事实、逻辑、计算与知识错误。 | [→](../works/chemebench.md) |
| PEOA | 2024 | 化工与过程工程的问题求解：物料与能量衡算、热力学、传热、反应动力学、流体力学、分离过程与过程控制。 | 从学术文献整编的两个数据集，按 70/15/15 划分——ChemProc（7,000+ 化工问答对）与作为支撑的 MathComp（8,500+ 建模与数值方法问答对）；每道题都以多步、工具集成的轨迹求解。 | 按阶段拆解的工具学习评分：任务规划对照金标准方案，工具选择用 Recall@K / NDCG@K / COMP@K 对照真值工具集，工具调用看参数抽取正确性与错误处理，回答生成用 BLEU、ROUGE-L 与精确匹配。 | [→](../works/peoa.md) |
| Using Large Language Models for Solving Thermodynamic Problems | 2025 | 化工热力学：闭系与开系、单步与多步状态变化、循环过程，以及不止涉及气体、也涉及液体的过程。 | 22 道专门编写的题目（13 道简单、9 道进阶），每道题都在文字中完整给定条件且数值解唯一，对五个模型各出题三次。 | 由受过训练的人类专家按高校考试阅卷的方式评分，每做对一个解题步骤给 0.5 分（声明的不确定度通常为 ±0.5）；简单与进阶两个子集分别报告均分，并跨重复次数考察一致性。 | [→](../works/llm-thermodynamics.md) |
| ERI Benchmark | 2026 | 化学工程是其覆盖的九个领域之一，下设六个子领域：物料与能量衡算、化工热力学、反应工程、分离过程、过程控制与传递现象。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对）；其中化学工程一片占 126 种组合、约 6,300 条记录，单独计分。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商组成的评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值，各领域的均分单独报告。 | [→](../works/eri-benchmark.md) |

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [CeProBench](../works/ceprobench.md)
- [Simona](../works/simona.md)
- [CRAFTS](../works/crafts.md)
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](../works/ctrl-alt-recover.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [Can Large Language Models Automate the HAZOP Process Without Human Intervention?](../works/can-large-language-models-automate-the-hazop-proce.md)
- [PSE-Bench](../works/pse-bench.md)
- [ChemEBench](../works/chemebench.md)
- [PEOA](../works/peoa.md)
- [Using Large Language Models for Solving Thermodynamic Problems](../works/llm-thermodynamics.md)
- [ERI Benchmark](../works/eri-benchmark.md)
