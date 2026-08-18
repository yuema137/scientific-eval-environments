# General Long-Horizon Agent Benchmarks

> [English](../../topics/long_horizon_evaluation.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

长 horizon agent 评估覆盖这样一类 benchmark：其任务需要多次顺序决策、多轮工具调用或多轮交互才能判定完成。"长"并非固定的步数——它指失败可能沿步骤累积、中间状态起作用、单一的最终奖励难以给出足够的诊断信号。

## Motivation

短 horizon benchmark 会奖励擅长一步推理的模型。真实部署——专业工作流、科学计算 pipeline、多轮 tool use——远长于一次 prompt-response。长 horizon benchmark 是规划、错误恢复、状态维护与 cost-awareness 变得可测量的场景，通常也是 trajectory 级评估的开销真正值得的场景。

## Existing Approaches

长 horizon benchmark 沿几个维度分化：环境介质、horizon 长度、是否存在密集中间奖励、任务的生态 grounding。

- **职业工作流 grounding。** [Agents' Last Exam](../works/agents-last-exam.md) 把长 horizon 任务锚定在美国职业分类的 13 个行业大类，由 250+ 行业专家共同设计。
- **Terminal 场景的长 horizon 扩展。** [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) 用密集奖励式评分把 Terminal-Bench 推向更长的 horizon。
- **科学长 horizon 工作流。** [Terminal-Bench Science](../works/terminal-bench-science.md) 面向自然科学的容器化计算工作流。
- **能力驱动的 proactive-agent 任务。** [UniClawBench](../works/uniclawbench.md) 在 Docker 闭环模拟下沿五个能力轴评估 proactive agent。
- **Deep research trajectory。** [TRACE](../works/trace.md) 面向长 horizon 的 deep-research 工作流，配 hierarchical trajectory utility function。
- **长 horizon 金融 tool use。** [FinTrace](../works/fintrace.md) 在长 horizon 金融决策上做 4 维度共 9 指标的评估。
- **真实软件工程任务。** [SWE-bench](../works/swe-bench.md) 要求 agent 通过编辑代码库解决 2,294 个真实 GitHub issue，以各仓库自身的测试套件执行打分；其人工验证的 500 实例 SWE-bench Verified 子集是以可靠性为重点的变体。
- **多环境 agent 能力。** [AgentBench](../works/agentbench.md) 在一个框架下汇集 8 个不同的交互环境，考察 LLM-as-agent 在多轮交互中的推理与决策。
- **通用助手问题。** [GAIA](../works/gaia.md) 提出 466 个需要推理、多模态、web 浏览与工具使用的真实世界问题，答案单一无歧义——人类达 92%，配插件的 GPT-4 为 15%。
- **真实 web 环境。** [WebArena](../works/webarena.md) 托管跨四个领域的完全功能网站，以功能正确性对长 horizon web 任务打分（最佳 GPT-4 agent 14.41%，人类 78.24%）。
- **整机计算机任务。** [OSWorld](../works/osworld.md) 在真实操作系统（Ubuntu / Windows / macOS）中提供 369 个开放式任务，配以逐任务的基于执行的评估脚本（最佳模型 12.24%，人类 72.36%）。
- **真实感多应用工具编排。** [Toolathlon](../works/toolathlon.md) 通过 MCP server 暴露 32 个真实软件应用与 604 个工具，用来自真实软件的状态初始化环境，并以确定性的、基于状态的评估脚本为 108 个跨应用任务（平均约 20 轮）打分；最佳模型 pass@1 仅 38.6%，pass@3 / pass^3 的差距把可靠性暴露为独立短板。
- **文档密集型数据分析。** [LongDA](../works/longda.md) 把导航长文档变成瓶颈本身：505 条分析查询覆盖 17 个美国全国性调查，配套文档平均 263k token，agent 在 100 步预算内以多轮块状交互完成文档检索、信息整合与 Python 执行；最强受评模型的 match rate 仅 68.91%，且论文把成功归因于检索与工具使用策略而非推理。
- **开放式文献搜索。** [AutoResearchBench](../works/autoresearchbench.md) 在构造上就让 horizon 开放：其 1,000 条文献发现查询中符合条件的论文数量未知，agent 必须持续进行渐进式多步探查并自行决定何时停止；最强模型在其两类任务上均低于 10%。
- **异步环境。** [Gaia2](../works/gaia2.md) 在事件驱动的环境中运行 1,120 个场景，这些环境按自己的时钟推进而非仅在 agent 行动时才变化，从而使时间意识成为一项被打分的能力：GPT-5（high）以 42.1% 的 pass@1 总分领先，但在 Time 划分上得分为 0.0，且每个受评模型在该划分上都低于 9 分。
- **研究型 horizon 上的终端报告质量。** [DeepResearch Bench](../works/deepresearch-bench.md) 覆盖与 TRACE 相同的 deep research horizon，却有意只评价最终产物——理由是商业 agent 的内部检索与推理不可观测：100 个由专家撰写的任务，其主题配比压缩自 44,019 条经过筛选的真实用户 query，由 reference-based 自适应准则框架（RACE）与实时引用核验（FACT）共同评判。Gemini-2.5-Pro Deep Research 以 48.88 的 RACE 总分领先，而引用 grounding 的排序与报告质量的排序并不一致。
- **迭代式工程优化。** [Frontier-Eng](../works/frontier-eng.md) 把 horizon 变成一条优化轨迹：在 47 个真实工程任务上，agent 反复提出候选设计、从工业级仿真器获得硬性可行性约束下的连续奖励，并在固定交互预算内修订——改进的频率与幅度都沿轨迹按 power law 衰减。
- **以可合并性为目标。** [FrontierCode](../works/frontiercode.md)（Cognition；业界 benchmark，无论文）在真实开源仓库中按「维护者会不会真的合并」为 PR 量级任务打分——正确性、测试质量、范围克制、风格——采用测试、评分标准与验证器的组合，查阅含解来源的运行记零分。
- **开放式的生存 horizon。** [KellyBench](../works/kellybench.md) 把 agent 投入一整个赛季的非平稳体育博彩市场模拟，目标是长期资金增长；受评前沿模型平均全部亏损（最佳 −8%），人类专家评分标准给其策略的精细程度打出低分。
- **交互迁移落差。** [SWE-Interact](../works/swe-interact.md) 把软件工程任务改成需求逐步披露的多轮用户驱动会话；单轮能解约 50% 的模型，交互式下跌到约 25%。
- **回放真实会话。** [SWE-Together](../works/swe-together.md) 从 11,260 条真实用户-agent 会话中整理出 109 个可验证的仓库级任务，经保持原意的用户模拟器回放，在最终正确性之外同时统计 agent 消耗的纠正反馈轮数。
- **长 horizon 的生物学发现。** [scBench-Long](../works/scbench-long.md) 给 agent 原始或近原始的单细胞数据、不预设方法，要求走完整条分析链路，直到该研究已发表的结论；受控答案词表让开放式 horizon 仍可确定性判分，最强模型-harness 组合也只通过 25.4% 的运行。
- **执行判分的具身规划。** [LoTa-Bench](../works/lota-bench.md) 把 LLM 任务规划器的比较自动化：在 ALFRED/AI2-THOR 与 VirtualHome 中执行计划、按目标达成度判分，取代人工审读。
- **按能力分解的具身决策。** [Embodied Agent Interface](../works/embodied-agent-interface.md) 沿四个模块——目标解释、子目标分解、动作排序、状态转移建模——对照模拟器状态评估 LLM，并在 VirtualHome 与 BEHAVIOR 上配类型化错误分类。
- **高低能力的分裂。** [EmbodiedBench](../works/embodiedbench.md) 让 24 个 MLLM 作为视觉驱动 agent 跑四个环境里的 1,128 个任务；模型能应付高层语义、却在底层操作上失手，GPT-4o 平均止于 28.9%。
- **类别宽广的交互式评估。** [EmbodiedEval](../works/embodiedeval.md) 让 MLLM 在 125 个 3D 场景中完成 328 个任务，横跨导航、物体与社交互动及具身问答，与人类水平差距很大。
- **量化的协作开销。** [PARTNR](../works/partnr.md) 在 100,000 个人机协作任务上评测 LLM 规划器，发现 LLM 搭档反而让人比单干更慢（步数为 1.1 倍）。
- **异步性作为变量。** [Robotouille](../works/robotouille.md) 剥离异步规划：同一套 ReAct 机制从同步烹饪任务的 47% 跌到动作时间重叠时的 11%。
- **对话即协调。** [RoCo / RoCoBench](../works/rocobench.md) 评估多机器人协作，每条臂的 LLM 用自然语言协商计划与路径点，并有真实 UR5 演示。
- **安全意识的具身规划。** [SafeAgentBench](../works/safeagentbench.md) 成对给出危险与安全任务（共 750 个、10 类危险）；最谨慎的基线也只拒绝 10% 的详细危险任务，换 LLM 也无济于事。
- **用编码 agent 做机器人控制时的脚手架依赖。** [CaP-X](../works/cap-x.md) 评测 12 个前沿模型跨抽象层级编写机器人控制程序，表明人工设计的原语被移除后成功率随之下降。
- **Kaggle 上的 ML 工程。** [MLE-bench](../works/mle-bench.md) 让 agent 端到端跑完整 Kaggle 竞赛——数据准备、训练、迭代——在 75 个竞赛上对照奖牌门槛评分。
- **可训练的 ML 工程竞技场。** [MLE-Dojo](../works/mle-dojo.md) 把 ML 工程做成 200+ Kaggle 挑战上、带迭代反馈循环的可 RL 训练交互环境。
- **提升指标的实验。** [MLAgentBench](../works/mlagentbench.md) 在 13 个 ML 任务上跑「读取-执行-检查-迭代」循环，按相对起始代码的实测提升评分。
- **新颖方法研究竞赛。** [MLRC-Bench](../works/mlrc-bench.md) 让 agent 在 7 个竞赛任务上提出并实现研究方法，按缩小的人类差距评分。
- **仓库搭建与执行。** [SUPER](../works/super.md) 要求多步配置并执行真实研究仓库以复现结果。
- **完整研究流程。** [MLR-Bench](../works/mlr-bench.md) 在 201 个任务上覆盖想法、方案、实验、论文四阶段，凸显结果编造的可靠性问题。
- **带时间预算的 AI R&D。** [RE-Bench](../works/re-bench.md) 在 2/8/32 小时预算下就开放式研究工程对照人类专家评估 agent。
- **AI 研究竞技场。** [MLGym](../works/mlgym.md) 在支持 RL 训练的 Gym 环境中，于 13 个任务上跑从想法到分析的完整研究循环。
- **AI 开发 agent。** [DevAI / Agent-as-a-Judge](../works/devai.md) 让 agent 对照 365 个层级化需求构建 AI/ML 项目，逐步评估。
- **难度可分解的机器人操作。** [VLA-Arena](../works/vla-arena.md) 在 170 个操作任务上评估视觉-语言-动作策略，配以正交的难度轴与 L0–L2 分级，含一个专门的 Long Horizon 套件与累积成本指标。
- **任务状态 horizon。** [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md) 提出「任务状态 horizon」——agent 必须跟踪、维护、探索与更新的任务相关状态的跨度——并编制 588 个具身规划回合，配干预诱发的状态更新与恢复指标。
- **端到端数据科学工作流。** [DSAgentBench](../works/dsagentbench.md) 把数据科学刻画为在真实计算机环境中执行的长 horizon、多阶段、多工具工作，为 275 个任务各配一个确定性评估器。
- **浏览与计算交织。** [DrBencher](../works/drbencher.md) 合成需要多跳浏览与多步计算交织的 deep-research 问题，其金标准答案由知识图谱链条提供、可经执行验证。
- **harness 自我改进。** [Evo-Bench](../works/evo-bench.md) 按模型在有界演化循环中能把自身 agent harness 改进多少来评分，报告下游表现与一条随时验证的轨迹。
- **多语言大规模重构。** [SWE-Bench ProMax](../works/swe-bench-promax.md) 检验横跨七种编程语言、平均每个实例改动 11.4 个文件与 261.6 行的协调式、保行为变更。
- **loop engineering。** [LoopsBench](../works/loopsbench.md) 把持续软件开发建模为可分别测试单元上的依赖 DAG，配一个流感知运行时：沿就绪前沿释放测试，并把已完成节点保留为回归义务。
- **Horizon 是积累下来的状态，而不是走过的步数。** 有一类工作把 horizon 一直拉到 episode 之外，于是跨过边界传下去的是一件外部产物，而不是一段上下文窗口。[SkillEvolBench](../works/skillevolbench.md) 把获取阶段与部署阶段分开，部署阶段的 skill 库冻结为只读，再沿上下文漂移、对抗性捷径、组合三条轴给留出任务打分，并同时设「无 skill」与「原始轨迹」两组对照；结果是未经蒸馏的原始轨迹常常胜过由它蒸馏出的 skill。[PATH-Bench](../works/path-bench.md) 动的则是这种积累的*先后顺序*：依照估计出的任务关系矩阵采样出 100 个中间任务组成的序列，其间只反复执行同一个探针任务，于是前向迁移、后向迁移与遗忘都能从一条纵向轨迹上读出——同一批任务、换一条路径走，就足以让 agent 的排名重新洗牌。
- **除了能力，horizon 还会一并带上什么。** [SkillMisevo-Bench](../works/skillmisevo-bench.md) 把同一套持久状态的设计搬到安全上：恶意暴露按固定日程在一个 episode 内分次投放，最后一个区块则在彻底重置后只重新载入 agent 自己写下的 `SKILL.md`，从而把当场造成的危害与熬过整场会话留存下来的危害分开。
- **只有长度，没有环境。** [Skill²-Bench](../works/skill2-bench.md) 单独抽出长 horizon 难度中的一个成分——在前后依赖的相邻步骤之间切换推理 skill 所付出的代价——放进 2 到 10 步的链条里考察：没有工具、没有外部状态，失败一步也无从补救；难度由一个有向的成对 skill 熵测度校准，该测度以单一参考模型为准固定下来。

## Comparison

| Benchmark | Year | Horizon 信号 | 环境 | Card |
|---|---|---|---|---|
| Agents' Last Exam | 2026 | ~1,000+ 真实职业任务 | 职业分类任务 | [→](../works/agents-last-exam.md) |
| Long-Horizon-Terminal-Bench | 2026 | 46 任务；数百步；密集分级奖励 | Terminal (Docker) | [→](../works/long-horizon-terminal-bench.md) |
| Terminal-Bench Science | 2026 | 数分钟至数小时的科学工作流 | Container（pytest 验证） | [→](../works/terminal-bench-science.md) |
| UniClawBench | 2026 | 400 多轮 checkpointed 任务 | 实时 Docker + 闭环模拟 | [→](../works/uniclawbench.md) |
| TRACE | 2026 | Deep-research 多步 trajectory | Deep research | [→](../works/trace.md) |
| FinTrace | 2026 | 800 条长 horizon 金融 trajectory | 金融 tool use | [→](../works/fintrace.md) |
| SWE-bench | 2023 | 2,294 个 issue；跨多文件多函数编辑 | 软件工程（Python 仓库）；执行打分 | [→](../works/swe-bench.md) |
| AgentBench | 2023 | 8 个交互环境；多轮 | 跨环境 agent 能力 | [→](../works/agentbench.md) |
| GAIA | 2023 | 466 个多工具助手问题 | 通用助手（推理 / 浏览 / 工具） | [→](../works/gaia.md) |
| WebArena | 2023 | 长 horizon web 任务；功能正确性 | 实时自托管网站（4 领域） | [→](../works/webarena.md) |
| OSWorld | 2024 | 369 个开放式计算机任务 | 真实 OS（Ubuntu / Windows / macOS）；执行打分 | [→](../works/osworld.md) |
| Gaia2 | 2026 | 1,120 个场景，横跨七个能力划分；环境独立于 agent 推进 | 模拟智能手机世界，含 12 个有状态 app；面向 write 动作的验证器 | [→](../works/gaia2.md) |
| AutoResearchBench | 2026 | 1,000 条开放式文献发现查询；答案集大小未知的渐进式多轮探查 | 学术检索与通用 web 检索上的 agentic 搜索 | [→](../works/autoresearchbench.md) |
| LongDA | 2026 | 505 条查询按出版物分块多轮交互；平均 263k token 文档下的 100 步预算 | 美国联邦调查数据上的文档导航 + 沙箱化 Python | [→](../works/longda.md) |
| Toolathlon | 2025 | 108 个跨应用任务；平均约 20 轮（上限 100 轮）；每任务平均暴露 69.9 个工具 | 经 MCP 的 32 个真实应用 / 604 个工具；容器化 + 远程；基于状态的脚本 | [→](../works/toolathlon.md) |
| Frontier-Eng | 2026 | 47 个任务；固定交互预算下的迭代 propose-execute-evaluate 循环 | 工业级工程仿真器（连续奖励、硬性可行性约束） | [→](../works/frontier-eng.md) |
| DeepResearch Bench | 2025 | 100 个博士级研究报告任务；horizon 不设预算，只在终端产物上打分 | 商业 deep research agent 与带搜索的 LLM；reference-based LLM judge 报告评分 + 实时引用核验 | [→](../works/deepresearch-bench.md) |
| FrontierCode | 2026 | 每个任务投入 40+ 小时的 PR 量级端到端任务；按可合并性判分 | 真实开源仓库（业界 benchmark；测试、评分标准与验证器组合） | [→](../works/frontiercode.md) |
| KellyBench | 2026 | 一整个模拟赛季的序贯决策；破产为吸收态 | 非平稳体育博彩市场（2023–24 英超模拟） | [→](../works/kellybench.md) |
| SWE-Interact | 2026 | 多轮用户驱动会话；单轮约 50% vs. 交互约 25% | 需求由模拟用户逐步披露的软件工程 | [→](../works/swe-interact.md) |
| SWE-Together | 2026 | 109 个回放的仓库级会话；正确性之外统计纠正轮数 | 源自真实会话、经保持原意的用户模拟器回放的交互式编码 | [→](../works/swe-together.md) |
| scBench-Long | 2026 | 从近原始数据到已发表结论的 21 项评估；1,068 条轨迹 | 单细胞生物学分析；确定性判分 + 轨迹评分标准 | [→](../works/scbench-long.md) |
| LoTa-Bench | 2024 | 多步技能序列计划执行至目标达成 | ALFRED/AI2-THOR 与 Watch-And-Help/VirtualHome（模拟） | [→](../works/lota-bench.md) |
| Embodied Agent Interface | 2024 | 四个决策模块对照模拟器状态评分；类型化错误分类 | VirtualHome 与 BEHAVIOR（模拟） | [→](../works/embodied-agent-interface.md) |
| EmbodiedBench | 2025 | 1,128 个任务，从高层到原子动作；六个能力子集 | 四个具身环境（模拟） | [→](../works/embodiedbench.md) |
| EmbodiedEval | 2025 | 五类共 328 个交互式任务 | 125 个 3D 场景（模拟） | [→](../works/embodiedeval.md) |
| PARTNR | 2024 | 100,000 个协作任务；相对人类基线的步数开销 | 60 栋 Habitat 房屋，人类在环（模拟） | [→](../works/partnr.md) |
| Robotouille | 2025 | 同步 vs 异步的成功率落差（47% → 11%） | 长程烹饪模拟 | [→](../works/robotouille.md) |
| RoCo / RoCoBench | 2023 | 6 个协作任务；环境反馈下的对话 + 重规划 | MuJoCo 多机器人 + 真实 UR5 演示 | [→](../works/rocobench.md) |
| SafeAgentBench | 2024 | 750 个危险/安全任务；拒绝率与成功率 | SafeAgentEnv 具身模拟 | [→](../works/safeagentbench.md) |
| CaP-X | 2026 | 跨抽象层级的代码合成成功率；脚手架依赖 | Robosuite/LIBERO-PRO/BEHAVIOR 模拟 + 真实机器人 | [→](../works/cap-x.md) |
| MLE-bench | 2024 | 端到端 Kaggle 竞赛；按奖牌门槛评分 | 75 个精选 Kaggle ML 工程竞赛 | [→](../works/mle-bench.md) |
| MLE-Dojo | 2025 | 迭代实验/调试循环；长 horizon 解质量 | 200+ Kaggle 挑战的 Gym 环境 | [→](../works/mle-dojo.md) |
| MLAgentBench | 2023 | 读取-执行-检查-迭代；相对起始代码的提升 | 13 个 ML 实验任务 | [→](../works/mlagentbench.md) |
| MLRC-Bench | 2025 | 提出+实现新颖方法；相对顶尖人类的差距缩小 | 7 个 ML 研究竞赛任务 | [→](../works/mlrc-bench.md) |
| SUPER | 2024 | 多步仓库搭建与执行；端到端 vs 场景成功率 | 真实 ML/NLP 研究仓库 | [→](../works/super.md) |
| MLR-Bench | 2025 | 四个研究阶段；约 80% 编造结果率 | 201 个开放式 ML 研究任务 | [→](../works/mlr-bench.md) |
| RE-Bench | 2024 | 2/8/32 小时预算下对照人类专家的 best-of-k | 7 个研究工程环境（METR） | [→](../works/re-bench.md) |
| MLGym | 2025 | 完整研究循环；可 RL 训练的 Gym | 13 个开放式 AI 研究任务（Meta） | [→](../works/mlgym.md) |
| DevAI / Agent-as-a-Judge | 2024 | 构建 AI/ML 项目；逐步的需求判分 | 55 个 AI 开发任务、365 个需求 | [→](../works/devai.md) |
| VLA-Arena | 2025 | 11 个套件共 170 个任务；L0–L2 分级含一个 Long Horizon 套件；SR + 累积成本 | 模拟机器人操作（RoboSuite / LIBERO / VLABench） | [→](../works/vla-arena.md) |
| RoboGraphBench | 2026 | 588 个回合；任务状态 horizon（维护 / 探索 / 更新）；100 步闭环；状态管理 + 恢复指标 | 具身高层规划（RoboTwin 2.0 / RoboCasa 模拟器） | [→](../works/compiling-and-benchmarking-task-state-horizons-for.md) |
| DSAgentBench | 2026 | 275 个多阶段、多工具数据科学工作流 | 真实计算机环境（notebook / IDE / 终端 / 浏览器 / 数据库） | [→](../works/dsagentbench.md) |
| DrBencher | 2026 | 多跳浏览 + 多步计算交织；答案优先的 KG 链合成 | 五个领域上的 deep research（web + 领域 API） | [→](../works/drbencher.md) |
| Evo-Bench | 2026 | 608 个任务；有界 harness 演化循环（20 轮 / 1,000 步 / 48h）；Overall + Anytime Validation Score | Search / Office / General agent harness 自我改进 | [→](../works/evo-bench.md) |
| SWE-Bench ProMax | 2026 | 170 个重构实例；每任务平均改动 11.4 个文件 / 261.6 行 | 多语言软件仓库（7 种语言）；执行打分 | [→](../works/swe-bench-promax.md) |
| LoopsBench | 2026 | 112 个任务；对 5,300+ 开发单元的依赖 DAG「loop engineering」；流感知的回归义务 | 软件开发（8 种语言、9 个领域）；Docker 支撑 | [→](../works/loopsbench.md) |
| SkillEvolBench | 2026 | 180 个任务，按角色分族、族内共享同一条隐含流程；先获取，再在冻结库上部署，按上下文漂移 / 对抗性捷径 / 组合三项评分 | 六类通用 agent 环境（代码、工具、数据、文档、信息综合、沟通），跨三种 agent harness | [→](../works/skillevolbench.md) |
| PATH-Bench | 2026 | 每条序列 5 个热身任务加 100 个中间任务，每隔 6–12 个任务重复一次探针；每个数据集与条件各 50 条序列；测前向迁移、后向迁移与遗忘 | BigCodeBench 程序合成与 WildToolBench 多轮工具使用；主干冻结，配八种终身 agent 的记忆 / skill 实现 | [→](../works/path-bench.md) |
| Skill²-Bench | 2026 | 300 个留出任务，每个 2–10 步且步步依赖，相邻步骤取自不同领域并按三档 skill 熵采样；单 skill 与跨 skill 查询成对比较 | 覆盖九个领域的跨 skill 推理链；无工具、无外部状态、失败步骤不可补救 | [→](../works/skill2-bench.md) |
| SkillMisevo-Bench | 2026 | 每种条件 25 个 episode、每个 21 个任务，恶意/良性按固定日程排布，每三个任务为一块、每块之后演化一次，最后在彻底重置后加一个持久性区块 | 沙箱内的 agentic 操作（AgentHazard 基座）；四种 agent 框架、六种演化方法，共用一个主干模型 | [→](../works/skillmisevo-bench.md) |
| AutoResearchEval | 2026 | 每个任务走完六个研究生命周期阶段，全部 800 条轨迹从头到尾标注，而不是只在终点打分 | agent harness（Claude Code、Codex、Gemini CLI）与其研究工具链 | [→](../works/autoresearcheval.md) |
| PACE-Bench | 2026 | 每对 20 次迭代修复，反馈只作诊断不给修改建议 | Box2D 刚体仿真器，60 FPS | [→](../works/pace-bench.md) |
| Beyond Final Scores | 2026 | 每个任务 2–12 小时墙钟预算，全程有验证器检查点；avg@3 对照 best@3 把跨轮次可靠性与天花板分开 | AutoLab 任务，共用 Claude Code harness | [→](../works/beyond-final-scores.md) |
| AutoWorldModel-Bench | 2026 | 单张 H100 上 6 小时一个会话，每次单独训练限时 10 分钟，把预算折算成迭代次数 | 八个暴露结构化实体状态的游戏环境 | [→](../works/autoworldmodel-bench.md) |
| R³-Bench | 2026 | 一份预算由六道题共用，因此必须分配算力，还得舍掉一部分题 | 无工具作答与 Terminus-2 shell | [→](../works/r3-bench.md) |

## Open Questions

- **"长 horizon" 到底指什么？** 步数？wall-clock？独立 tool call？独立子决策？不同 benchmark 采用不同定义，跨 benchmark 比较受限。
- **最终奖励 vs. trajectory 指标。** 带密集子任务奖励的 benchmark 产出非 Pass@1 信号；仅有终态结果的 benchmark 则不产出。长 horizon 排行榜应如何权衡两者？
- **生态效度 vs. 可复现性。** 生态 grounding 的任务（Agents' Last Exam、Terminal-Bench Science）源于真实工作流，需付出评审成本；合成任务更易扩展。哪一种更适合作为主要评估面？
- **难度上限。** Frontier 模型在短 horizon 上迅速饱和。当前长 horizon benchmark 是否在下一代模型面前仍保留难度上限？

## Related Works

- [SkillEvolBench](../works/skillevolbench.md)
- [PATH-Bench](../works/path-bench.md)
- [Skill²-Bench](../works/skill2-bench.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [VLA-Arena](../works/vla-arena.md)
- [DrBencher](../works/drbencher.md)
- [LoopsBench](../works/loopsbench.md)
- [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md)
- [SWE-Bench ProMax](../works/swe-bench-promax.md)
- [DSAgentBench](../works/dsagentbench.md)
- [Evo-Bench](../works/evo-bench.md)
- [Agents' Last Exam](../works/agents-last-exam.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [UniClawBench](../works/uniclawbench.md)
- [TRACE](../works/trace.md)
- [FinTrace](../works/fintrace.md)
- [SWE-bench](../works/swe-bench.md)
- [AgentBench](../works/agentbench.md)
- [GAIA](../works/gaia.md)
- [WebArena](../works/webarena.md)
- [OSWorld](../works/osworld.md)
- [Gaia2](../works/gaia2.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [LongDA](../works/longda.md)
- [Toolathlon](../works/toolathlon.md)
- [Frontier-Eng](../works/frontier-eng.md)
- [DeepResearch Bench](../works/deepresearch-bench.md)
- [FrontierCode](../works/frontiercode.md)
- [KellyBench](../works/kellybench.md)
- [SWE-Interact](../works/swe-interact.md)
- [SWE-Together](../works/swe-together.md)
- [scBench-Long](../works/scbench-long.md)
- [LoTa-Bench](../works/lota-bench.md)
- [Embodied Agent Interface](../works/embodied-agent-interface.md)
- [EmbodiedBench](../works/embodiedbench.md)
- [EmbodiedEval](../works/embodiedeval.md)
- [PARTNR](../works/partnr.md)
- [Robotouille](../works/robotouille.md)
- [RoCo / RoCoBench](../works/rocobench.md)
- [SafeAgentBench](../works/safeagentbench.md)
- [CaP-X](../works/cap-x.md)
- [MLE-bench](../works/mle-bench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLAgentBench](../works/mlagentbench.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [SUPER](../works/super.md)
- [MLR-Bench](../works/mlr-bench.md)
- [RE-Bench](../works/re-bench.md)
- [MLGym](../works/mlgym.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)
- [AutoResearchEval](../works/autoresearcheval.md)
- [PACE-Bench](../works/pace-bench.md)
- [Beyond Final Scores](../works/beyond-final-scores.md)
- [AutoWorldModel-Bench](../works/autoworldmodel-bench.md)
- [R³-Bench](../works/r3-bench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
