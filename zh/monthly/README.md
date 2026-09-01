# 月度报告

> [English](../../monthly/README.md) | **简体中文**

月报要讲清楚三件事：这个月知识库收了什么，几项工作放在一起以后说明了什么，以及这些变化为什么值得注意。它是带分析的仓库更新记录，不是简单按论文发布日期排出来的清单。

## 一项工作算在哪个月

一项工作在哪个月第一次进入 `main`，就归到哪个月。Card 上的 `首次公开` 仍单独记录这项工作最早在哪一天能被公众访问。

历史档案有一个一次性的例外：仓库已经收录的 cards 从 2024 年 1 月开始，按各自的 `首次公开` 月份回填；2023 年及更早的工作不做历史月报。以后每月新增的报告仍按进入 `main` 的月份归档。这样老工作晚发现时会在当月标成历史补录，不会悄没声地漏过去。

这俩日期不能混一块儿：

- 如果工作首次公开的月份正好就是报告月份，表里标成 **当月新发布**。
- 如果仓库这个月才补进来一项更早的工作，表里标成 **历史补录**。月报照样收它，但不能说它是这个月刚发表的。

## 月报怎么组织

每份月报包含五部分：

1. **本月概览**：给出数量，再挑三到五条真正值得记住的结论。
2. **这个月到底变了什么**：用三到六条研究故事线把相关工作串起来，不把 card 摘要一股脑贴上去。
3. **值得展开的 Topic**：只有本月形成了文献集群、边界变化或方法分歧的 Topic 才单独成节。
4. **值得展开的 Domain**：只有新增工作暴露了某个领域自己的约束或变化，才单独成节。
5. **本月完整索引**：这个月加入的 card 一张不少，每张只出现一次，同时列出首次公开时间、新发布或补录状态、Topics 和 Domains。

正文负责把重点讲明白，末尾索引负责保证不漏。同一项工作可以属于多个分类，但正文只选一个最合适的位置讲透，其他关系用链接带过去，别来回重复。

## 档案重点

<!-- MONTHLY_ARCHIVE_OVERVIEW_START -->
- 现在一共有 `32` 份月报，覆盖 `366` 项工作，时间从 `2024-01` 到 `2026-08`。
- 目前最密的一期是 [2026-08](./2026-08.md)，单月收了 `41` 项工作。
- 整个档案里最常反复出现的主线，主要还是 `Scientific Agent Benchmarks、Trajectory Evaluation`。
<!-- MONTHLY_ARCHIVE_OVERVIEW_END -->

## 月报列表

这里按月份从新到旧排列。每一行都直接给出这期规模、主要 Topic 聚集点，以及值不值得点进去看的那句重点。

<!-- MONTHLY_REPORTS_START -->
| 月份 | 工作数 | 主要 Topic | 这期值不值得回看 |
|---|---:|---|---|
| [2026-08](./2026-08.md) | 41 | Scientific Agent Benchmarks、Trajectory Evaluation | 2026 年 8 月是目前档案里最密的一个月，一共 41 项新工作。它看起来已经不像某一条单一趋势在变强，而更像整个领域开始拆成几块彼此区分很清楚的子问题。Scientific benchmarking 还是最大头，但真正值得注意的是另外四条线也同时站起来了：trajectory evaluation 开始像一门独立的诊断方法学；long-horizon benchmark 不再只看任务做没做完，而开始把 agent improvement loop 也纳进来；evaluator reliability 这件事本身，终于开始被系统性地测；evaluation-driven post-training 也从“调一个模型”往“重新设计 learning algorithm”推进了一层。 |
| [2026-07](./2026-07.md) | 23 | Scientific Agent Benchmarks、Skill Hierarchy | 2026 年 7 月从数量上看没 6 月那么猛，但结构更集中。这个月主要围着一个问题转：如果 agent 的输出最后要对外部机构、物理过程、或者专家 workflow 负责，而不是只对 benchmark 自己那套打分规矩负责，那 evaluation 该怎么做？最清楚的例子就是桥梁检测排序、物理/天体物理文献综述与项目计划书、结构可靠度分析，以及在固定算力预算下改世界模型。 |
| [2026-06](./2026-06.md) | 36 | Scientific Agent Benchmarks、Skill Hierarchy | 2026 年 6 月是一个很关键的月：这时候仓库前面刚扩出来的 scope，开始不像“先把 topic 开着，后面再慢慢填”，而是真有结构支撑了。表面上看是 36 项工作很多，但更重要的是，这批新文献已经不再像一排平铺的 benchmark 名单。你能同时看到三条主线长出来：scientific benchmark 更贴近真实 workflow 和可执行产物；skill 开始变成一层可以单独评、单独诊断的对象；process-level evaluation 也不再是泛泛而谈，而是开始落到 validator、rubric、planning step 这些真能卡住系统的控制点上。 |
| [2026-05](./2026-05.md) | 28 | Scientific Agent Benchmarks、Trajectory Evaluation | 2026 年 5 月是 6 月那次明显爆发前的一个 scale-up month。AgentAtlas、AutoMat、BioXArena、AstroAlertBench 以及这个月其他新增，把仓库往 arena、agent ecosystem 和更多 scientific subfield 上同时铺开，但焦点还是没变：要的是能支持反复诊断和比较的 evaluation setup，而不是一次性 demo。 |
| [2026-04](./2026-04.md) | 18 | Scientific Agent Benchmarks、Trajectory Evaluation | 2026 年 4 月可以直接叫 plan-and-failure month。AutoResearchBench、FinTrace、Plan-RewardBench、plan-compliance evaluation、Frontier-Eng，再加上那篇天体物理里的“plausible but wrong”研究，都在把过去糊在一起的几个问题拆开：计划本身好不好、trace 靠不靠谱、以及系统失败到底是 reasoning、execution 还是 evaluator 自己出了问题。 |
| [2026-03](./2026-03.md) | 15 | Scientific Agent Benchmarks、Trajectory Evaluation | 2026 年 3 月是一个很典型的 process-instrumentation month。AgentProcessBench、CaP-X、CeProBench、AEC-Bench 和那篇受控天体物理 workflow 研究，本质上都在做同一个动作：把中间过程质量露出来，这样 failure analysis 就不用再从一个孤零零的最终分数开始猜。 |
| [2026-02](./2026-02.md) | 13 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 2026 年 2 月把 evaluation 更深地推进到了 institutional、biomedical 和 safety-constrained settings 里。AIRS-Bench、AutoBM/BMEval、FIRE-Bench、ChemCensor/CREED 以及这个月其他工作，关心的都是同一个问题：当 agent 必须在更强的领域规则、policy boundary 或 reviewer control 之内工作时，系统会怎么变。 |
| [2026-01](./2026-01.md) | 11 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 2026 年 1 月是 exploratory science、long-document workflow 和 step-level judging 明显接到一起的月份。LongDA、Terminal-Bench Science、HeurekaBench、MolecularIQ、ToolPRMBench 和 MetaAct-RL 放一块看，很清楚地说明：这份档案已经开始把 open-ended discovery、long-horizon evidence gathering 和中间决策质量当成同一个连着的评测问题来处理。 |
| [2025-12](./2025-12.md) | 9 | Scientific Agent Benchmarks、Trajectory Evaluation | 2025 年 12 月很像 engineering-heavy scientific evaluation 的一个 maturity month。AInsteinBench、FEM-Bench、Hydro-SE Bench、HiSciBench、CASCADE 这些工作继续把焦点压在可执行 workflow、结构化物理推理和端到端系统上，这些东西都不是靠表面流畅度就能轻易糊过去的。 |
| [2025-11](./2025-11.md) | 6 | Scientific Agent Benchmarks、Resource-aware Evaluation | 2025 年 11 月开始，cost 和 operational risk 不再只是 side metrics，而是硬约束。BATS、CostBench、BridgeEQA、那篇 HAZOP evaluation 和 EnvTrace 都在问同一件事：当预算、安全流程、instrument trace 和真实检查证据都在限制什么动作才算好动作时，agent 还能不能保持有用。 |
| [2025-10](./2025-10.md) | 22 | Scientific Agent Benchmarks、Credit Assignment | 2025 年 10 月算是第二次 breakout month，但这次扩出来的 breadth 带着更明显的诊断压力。Scientific benchmark 还是主体，可 CUARewardBench、Hard2Verify、TempoBench、Enconda-bench 和 PTA-GRPO 已经把 step-level judgment、verifier quality 和 high-level planning 硬塞进 benchmark 主叙事里了，想分都分不开。 |
| [2025-09](./2025-09.md) | 10 | Scientific Agent Benchmarks、Skill Hierarchy | 2025 年 9 月很像一个 engineering-and-tooling month。AECBench、CFDLLMBench、AstroMMBench、gammapyGPT 和 CritPt 共同加压的，都是同一个问题：agent 到底能不能真正操作领域软件、科学 pipeline 或多步工程 workflow，而不是只会围着它们说。 |
| [2025-08](./2025-08.md) | 5 | Scientific Agent Benchmarks、Benchmark Design, Validity & Contamination | 2025 年 8 月虽然量小，但在 benchmark design 上特别锋利。CODE2BENCH、CEQuest、CMPhysBench、FGBench 和 QCBench 都在做同一件事：让分数更难被糊弄出来，要么靠动态构题，要么逼模型真的做领域里的 quantitative 和 structural reasoning。 |
| [2025-07](./2025-07.md) | 10 | Scientific Agent Benchmarks、Survey | 2025 年 7 月有个很明显的特点，就是它特别在意“到底谁来定义什么叫做好”。那篇 survey、CosmoPaperQA、EngDesign、DrafterBench 和那篇 astronomy criteria paper，都在把 evaluation 往 expert review criteria、proposal quality 和真实文献工作上拉，而不是继续跟着 benchmark 自己的捷径走。 |
| [2025-06](./2025-06.md) | 10 | Scientific Agent Benchmarks、Skill Hierarchy | 2025 年 6 月的中心，是在更强 execution 和 cost 约束下做 professional-discipline evaluation。MedAgentGym、CVDP、DeepResearch Bench、SDBench、ChemEBench，再加上那几篇结构分析和地基设计工作，都在追同一个问题：到了医疗、硬件、土木和研究这些场景里，如果真正重要的是 workflow 跑没跑通，而不是答案像不像，那 agent 到底该怎么打分。 |
| [2025-05](./2025-05.md) | 22 | Scientific Agent Benchmarks、Trajectory Evaluation | 2025 年 5 月是一次很明显的 breadth explosion，而且已经能提前看见仓库后面那条 development-loop 主线。AstroVisBench、BAISBench、MLE-Dojo、MLR-Bench、RoboFAC、Traxgen 和 Beyond 'Aha!' 横跨天文、生物医学、机器学习研究、failure analysis 和 post-training，但它们最后都在往同一句话收：evaluation 不该只负责排结果，还得负责指导怎么改。 |
| [2025-04](./2025-04.md) | 8 | Scientific Agent Benchmarks、Evaluator Reliability & Validation | 2025 年 4 月可以直接叫 verification-hardening month。FEABench、HLS-Eval、LLM-SRBench、PHYBench 和 AgentRewardBench 其实都在拆同一个问题：agent 会不会做、benchmark 能不能验、以及当验证不是确定性的时，evaluator 本身还能不能信。 |
| [2025-03](./2025-03.md) | 6 | Scientific Agent Benchmarks、Survey | 2025 年 3 月不是靠规模取胜的，而是一个 framing month。那篇 agent-evaluation survey、ASIMOV、CoLA、AstroChart 和 LLM-EPANET 都在把 scope、abstraction level 和 environment design 这些问题磨得更清楚，后面仓库加 topic，其实就靠这些问题先站稳了。 |
| [2025-02](./2025-02.md) | 9 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 2025 年 2 月是 scientific-agent environments 和 long-horizon evaluation 开始接头的月份。MLGym、BixBench、EmbodiedBench、Robotouille、PDE-Controller 和 TPBench 一起把仓库从静态题库往外推，推到 interactive research、具身 planning 和 tool-grounded scientific tasks 这些地方。 |
| [2025-01](./2025-01.md) | 8 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 2025 年 1 月是一个很典型的 breadth month，一头连着 frontier 级的 general exams，一头连着领域味很重的 scientific tasks。Humanity's Last Exam、Gravity-Bench、热力学问题求解和 materials hypothesis generation 放一块看，能看到这份档案开始同时往“能力上限”与“学科内推理”两个方向扩。 |
| [2024-12](./2024-12.md) | 6 | Scientific Agent Benchmarks、Credit Assignment | 2024 年 12 月看起来很像一次从静态 benchmark 往 live、往 process-aware evaluation 的过渡。ProcessBench、Aviary、LiveIdeaBench、SafeAgentBench 和 AnalogXpert 共同关心的，都是系统在时间里怎么运行，而不只是它能不能一次性吐出一个像样答案。 |
| [2024-11](./2024-11.md) | 5 | Scientific Agent Benchmarks、Resource-aware Evaluation | 2024 年 11 月量不大，但方法上混得很有用。RE-Bench、OpenCATP、RoboSpatial、MaCBench 和 EEE-Bench 把 evaluation 往预算、具身几何和协同操作这些地方都伸进去了，于是 resource limits 和 physical context 这两件事越来越没法再当成事后备注。 |
| [2024-10](./2024-10.md) | 15 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 2024 年 10 月是 agent evaluation 第一次真正大面积铺开的 breakout month，工程、科学和具身系统这几边同时扩开。MLE-bench、DevAI、ControlEval、FVEval、Embodied Agent Interface 和 PARTNR 放在一起看，很清楚地说明一件事：realistic evaluation 现在得把 workflow、simulator、judge 和 long-horizon state 一起算进去。 |
| [2024-09](./2024-09.md) | 4 | Scientific Agent Benchmarks、Skill Hierarchy | 2024 年 9 月是一个很典型的 decomposition 月。CORE-Bench、SUPER、DSBench 和 ChemEval 都在顶同一个方向：别再用一个总分把东西糊住，而是把 tool use、subskill 和领域推理层拆开来看，这些拆法后来也慢慢长成了仓库 taxonomy 的骨架。 |
| [2024-08](./2024-08.md) | 4 | Scientific Agent Benchmarks、Trajectory Evaluation | 2024 年 8 月把 planning 和 execution 又往真实操作场景里推近了一步。TransportBench、SimBench、BLADE 和 PEOA 共同关心的，都是 practical constraints 下的结构化行动，不管 agent 面对的是运输规划、仿真运行，还是具身任务里的推理。 |
| [2024-07](./2024-07.md) | 6 | Scientific Agent Benchmarks | 2024 年 7 月是第一次让 domain-authentic scientific benchmarking 明显占上风的月份。AstroMLab 1、LAB-Bench、ElecBench、MolPuzzle 和 SciCode 都是在让领域本身来定义任务表面，所以这个月看起来很像一次真正的转向：从“带科学术语皮的 QA”，转到“按科学工作本身来长出来的评测”。 |
| [2024-06](./2024-06.md) | 6 | Scientific Agent Benchmarks、Planning & Decision-Making Evaluation | 2024 年 6 月最明显的推进，是把 evaluation 往外部验证上推，而不是停在“答案听起来像对”。AssertionBench、GenoTEX、MatText、BioKGBench 和 NATURAL PLAN 都给系统加上了 oracle、simulator 或约束结构，于是模型想靠说得顺就拿高分，这条路越来越走不通。 |
| [2024-05](./2024-05.md) | 4 | Scientific Agent Benchmarks | 2024 年 5 月开始，真实专业 workflow 明显变重要了。AgentClinic、AnalogCoder、RTL-Repo 和 CPsyExam 共同暴露出一个很实在的断层：文本看着像对，不等于临床判断、电路设计或者硬件产物真能过检。 |
| [2024-04](./2024-04.md) | 2 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 2024 年 4 月只有两项工作，但对比特别有力，因为它把一件事讲透了：headline score 到底说明什么，很大程度上取决于交互表面。ChemBench 评的是静态 chemistry knowledge，OSWorld 评的是长动作链上的真实 computer use，所以“模型能力”和“agent 能力”从这个月开始就不该再混着说。 |
| [2024-03](./2024-03.md) | 1 | Scientific Agent Benchmarks | 2024 年 3 月规模不大，但很重要，因为 BrainBench 把一个完整学科拉进来了，而且没有假装通用 QA 就够用。它把神经科学评测扎在专家编写的问题上，覆盖分子、系统、认知和临床几个层次，于是“学科内部到底有多宽”本身也成了评测问题的一部分。 |
| [2024-02](./2024-02.md) | 2 | General Long-Horizon Agent Benchmarks、Planning & Decision-Making Evaluation | 2024 年 2 月是这份档案里第一次把 planning 单独拎清的月份。TravelPlanner 和 LoTa-Bench 一起把后来一直要分开的两件事摆出来了：agent 制定计划时能不能满足现实约束，以及这个计划放进长时程具身执行以后还能不能站得住。 |
| [2024-01](./2024-01.md) | 1 | Trajectory Evaluation、Skill Hierarchy | 2024 年 1 月虽然只有一项工作，但它一上来就把这份档案后来反复坚持的标准立住了。AgentBoard 不只看最后答没答对，还把部分进展、subgoal 完成度和错误传播都纳进评测，所以这个月一开头就在说：agent evaluation 不能只剩一个最终正确率，还得说清这趟 run 是在哪儿坏掉的。 |
<!-- MONTHLY_REPORTS_END -->
