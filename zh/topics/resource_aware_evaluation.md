# Resource-aware Evaluation

> [English](../../topics/resource_aware_evaluation.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

一个 agent 花 1 美元做对 60%，另一个花 100 美元做对 62%。只看 accuracy，真正的 deployment decision 就被藏起来了。Token、wall-clock time、GPU hour、simulator call 和实验材料都有同样的问题。

Resource-aware evaluation 会记录或限制这些成本。比如总 budget 是 10 美元，agent 用 2 美元 retrieval、5 美元 simulation，再留 3 美元 verification；score 要同时展示 task quality 和 spending。便宜的失败不自动比昂贵的成功好，所以 benchmark 应该把 trade-off 摊开，别悄悄压成一个解释不清的 total。

## 定义

Resource-aware evaluation 不只看 agent 做成了什么，还记录它为此花了什么。成本可以是 token、tool fee、wall-clock time、compute、simulator time 或实验材料。有些 benchmark 只报告消耗；更强的设计会直接给 agent 一个预算，测它能不能在资源约束下权衡任务质量。

## 为什么重要

更多资源通常能换来更好结果：更强的 model 更贵，多调几次 tool 能找到更多 evidence，搜得更久也可能找到更好的 solution。如果 score 完全忽略消耗，就是在奖励「不惜代价解题」。科学和生产环境很少允许这么做，所以 evaluation 必须把 trade-off 摊开。

有两个划分维度：

- **资源作为额外报告的指标** vs. **资源作为显式目标**：前者在分析阶段浮现 trade-off；后者考察 agent 是否能在预算下**规划**。
- **仅 token 成本** vs. **tool-use 成本（仿真时间、实验资源）**：只看 token 成本会遗漏许多科学工作流的主要成本。

## 现有方法

- **在 tool use 中把成本作为一等目标。** [CostBench](../works/costbench.md) 把成本最小化本身设为任务，在 travel-planning 场景下具有可配置的原子/组合工具成本，并通过阻断事件迫使重规划。
- **Token 之外的 tool-use 成本，聚焦科学仿真。** [SimulCost](../works/simulcost.md) 把 cost-aware 评估扩展到物理仿真参数调优，显式建模仿真时间与实验资源成本，覆盖 13 个仿真器，并直接与传统方法对比。
- **面向 cost-aware planning 的专用数据集。** [CATP-LLM / OpenCATP](../works/catp-llm.md) 贡献了 OpenCATP——被称为首个面向 cost-aware planning 的数据集（11,100 样本），其中工具执行成本（如执行时间）与任务性能联合打分。其配对的规划方法属于本仓库范围之外的 agent 构建工作；数据集才是此处记录的 resource-aware 评估贡献。
- **按保真度定价的测量预算。** [MaD Physics](../works/mad-physics.md) 对每次观测收取随其精度上升的成本，并对每个 trial 的总花费设上限，使 agent 必须在固定预算下分配测量，以推断一条未知的——有时被改动的——物理定律。
- **给物理发现设观测预算。** [Gravity-Bench-v1](../works/gravity-bench.md) 限定 agent 对模拟二体引力系统可观测的次数，让实验设计本身进入评分范围；据官方项目页，最佳模型从全量数据下的 74% 跌到预算下的 49%。
- **把 oracle 调用作为分子设计中的定价资源。** [SMDD-Bench](../works/smdd-bench.md) 为 502 个保证有解的药物设计任务设定有限的 oracle 调用预算，探索必须规划而非穷举；最佳前沿模型仅解出 40.2%。
- **把诊断成本写上记分表。** [SDBench](../works/sdbench.md) 对 agent（与 21 位医生）的每次就诊与检查计费，守门人只应答被明确提出的询问，按准确率-成本前沿评分；改变编排方式比换模型更能移动这条前沿。
- **成本本身即任务。** [ChemCost](../works/chemcost.md) 不是给 agent 的开销设预算，而是让 agent 计算一个反应的成本——对照冻结价格快照，配无 judge 的精确真值与阶段级失败诊断。
- **作为在线控制信号的预算。** [BAGEN](../works/bagen.md) 让 agent 在每一轮预测剩余预算的上界与下界并标记不可行，把资源使用作为逐步的估计目标而非执行后的统计来评分。
- **把评估调用作为预算化的资源。** [VeRO / VeRO-Bench](../works/vero.md) 在硬性评估调用预算下 benchmark 优化其他 agent 的 coding agent：对目标 agent 的每次打分都经过门控评估器，扣减 n_E ≤ B 并阻断超额请求，对应昂贵查询下的黑盒优化设定；B ∈ {2, 4, 8, 16, 32} 的预算消融把预算效应与能力效应区分开。
- **迭代式设计优化上的交互预算。** [Frontier-Eng](../works/frontier-eng.md) 为每个真实工程任务的 propose-execute-evaluate 循环设置固定交互预算：agent 必须分配有限次数的仿真器交互，在连续奖励与硬性可行性约束下细化候选设计，使 benchmark 内在具备 resource-aware 属性。
- **把经济一致性作为测量对象。** [EcoAgent-Bench](../works/ecoagent-bench.md) 在 304 个任务上为每个动作定价并设定显式的单任务预算，同时把「该升级」与「该省钱」的任务成对分组，使一味花钱或一味省钱的单边策略无法得高分。Tool-API agent 的经济一致性至多 7.3%；预算从低到高扫过一遍，GPT-5.4 的升级率也只从 0% 升到 3%。
- **给 harness 优化设评估预算。** [HarnessOpt-Bench](../works/harnessopt-bench.md) 给优化器 LLM 一个种子 harness、评估反馈与固定的目标评估预算，在 TEE 审计的循环内运行，以留出测试集上相对种子的归一化增益评分；在 4 个任务、5 个优化器模型、111 次计分运行中，优化器模型之间拉开的差距大于它们借以行动的编码 harness 之间的差距。
- **把效率写进评分 rubric。** [MASSE](../works/masse.md) 既不给 agent 设预算，也不把成本单列出来报告：它的整体系统 benchmark MASEB 在 100 分里划出 20 分给「效率与鲁棒性」，而负责评阅一整份结构工程分析日志的 GPT-5 评审，会把总 token 用量与总运行时间与四项分数一并写进同一个 JSON 对象——于是一条又准又贵的流水线拿不到满分。论文随附的四个后端之间的成本/运行时权衡分析，读的也正是这同一批测量值。
- **省下的资源，而非花掉的资源。** [SkillAudit](../works/skillaudit.md) 测的是装上一件产物之后资源的**变化量**：在相同指令与相同输入下配对跑「用 skill」与「不用 skill」两组，得到 Efficiency Gain（执行时间的相对节省）与 Cost Gain（有效输入 token 的相对节省），两者各自截断到 [-1, 1] 后合成 Efficiency-Cost Gain，与效用、安全性一起写进同一份 per-skill 报告。这里不设任何预算，要测的是：采纳这个 skill，是否值回它所占的上下文。
- **把 token 与工具调用折算到同一种计价。** [BATS / Budget Tracker](../works/bats-budget-aware.md) 给出 `C_unified = c_token + Σ cᵢ·Pᵢ`，把工具调用按每次 0.001 美元与 token 成本并列计价——正是有了单一货币，成本—性能的 **scaling 曲线**才画得出来，而不必在名义上相等的工具预算下比准确率。它的发现是：只把预算调高、却不告诉 agent 还剩多少，并没有用；仅仅注入已用/剩余的计数，就能以十分之一的预算追平 ReAct 基线的准确率，总成本还低 31.3%。
- **成本–性能前沿式报告。** 另一些工作在 accuracy 之外同时报告 token 或 dollar 成本，用于在 Pareto 前沿上而非单一 accuracy 数字上做比较。这是分析时的资源意识，而非 benchmark 内部的资源意识。

### 一处缺口：预算是给定的，不是预测出来的

上面每一种做法，都是把预算作为**agent 必须遵守的约束**交下去，事后再看它花了多少。几乎没有谁要求 agent 或 harness 在动作执行**之前**估计它会花多少。库内有两项工作最接近，但值得区分开：

- [BAGEN](../works/bagen.md) 要求 agent 每一轮预测**剩余**预算的上下界并标记不可行——预测的是总量，且按步计分。
- [AI Research Preference Models](../works/ai-research-preference-models.md) 在付出代价之前预测哪些**候选方案**值得执行，但它预测的是相对优劣而非资源数量，而且只作用在一个搜索脚手架内部，并非可复用的接口。

两者都没有给出规划器在方案之间做取舍时真正需要的东西：一个以动作为单位、以任务特征为条件的分布，覆盖 token、墙钟、GPU 时间、内存与费用，并带有校准过的不确定性。参见下方的 Open Questions。

## 方法对比

| Benchmark | Year | 资源单位 | 资源角色 | 场景 | Card |
|---|---|---|---|---|---|
| CostBench | 2025 | 可配置的原子/组合工具成本 | 一等目标——为成本最优做规划 | 动态（阻断事件）；报告约 40% 静态→动态下降 | [→](../works/costbench.md) |
| SimulCost | 2026 | 仿真时间 + 实验资源 | 一等目标——预算下的参数调优 | 单轮与多轮；13 个仿真器 | [→](../works/simulcost.md) |
| CATP-LLM / OpenCATP | 2024 | 归一化工具价格（USD；执行时间 + 内存） | 通过 Quality of Plan 与性能联合报告（QoP = α·perf − (1−α)·cost） | 111 个工具规划任务 / 11,100 样本 | [→](../works/catp-llm.md) |
| MaD Physics | 2026 | 测量成本（按保真度定价的观测） | agent 分配的每个 trial 固定预算 | 模拟经典 / 流体 / 量子物理 | [→](../works/mad-physics.md) |
| BAGEN | 2026 | Token；时间 / 占用 / 成本 | 预测目标 + 提前停止目标 | 谜题 / 检索 / 编码 / 供应链 | [→](../works/bagen.md) |
| VeRO / VeRO-Bench | 2026 | 对目标 agent 的评估调用（门控预算 n_E ≤ B） | 强制硬约束——优化器须分配昂贵的评估 | 覆盖 5 个目标 agent 任务套件的 agent-harness 优化 | [→](../works/vero.md) |
| Frontier-Eng | 2026 | 仿真器交互（每任务固定预算） | 对 propose-execute-evaluate 循环的硬性上限 | 真实工程优化；47 个任务、5 个类别 | [→](../works/frontier-eng.md) |
| EcoAgent-Bench | 2026 | 显式单任务预算下的定价动作 | 一等目标——升级/省钱成对分组上的经济一致性 | 304 个源自 QA 的任务、5 个族；tool-API 与 workspace-CLI 两种设定 | [→](../works/ecoagent-bench.md) |
| HarnessOpt-Bench | 2026 | 目标评估调用（固定预算，TEE 计量） | 对优化-评估循环的强制硬约束 | Harness 优化；4 任务 × 5 个优化器 LLM，111 次计分运行 | [→](../works/harnessopt-bench.md) |
| Gravity-Bench-v1 | 2025 | 对模拟系统的观测（据官方项目页每次运行至多 100 次） | 对实验设计的强制预算；报告全量与预算下的差距 | 模拟双星上的引力物理发现 | [→](../works/gravity-bench.md) |
| SMDD-Bench | 2026 | oracle 调用（有限的单任务预算） | 对设计空间探索的强制硬约束 | 小分子药物设计；502 个有解任务、102 个靶点 | [→](../works/smdd-bench.md) |
| SDBench | 2025 | 就诊与诊断检查的费用 | 与准确率联合评分，构成准确率-成本前沿 | 带信息守门人的 304 个 NEJM-CPC 病例序贯诊断 | [→](../works/sdbench.md) |
| ChemCost | 2026 | 冻结价格快照中的供应商报价与可购包装 | 成本即任务本身——agent 对照精确真值计算反应成本 | 反应定价；1,427 个反应、230,775 条报价；含噪声注入下的鲁棒性评测 | [→](../works/chemcost.md) |
| MASSE | 2025 | 总 token 用量与总运行时间，由评审与质量分一并给出 | 计分项——「效率与鲁棒性」在 MASEB 的 100 分中占 20 分；同一批数字还支撑了四个后端之间的成本/运行时权衡分析 | 多智能体结构工程工作流；100 道经专家校验的题目，每道跑十次 | [→](../works/masse.md) |
| First head-to-head comparison of agentic AI on Einstein Telescope data | 2026 | 每次流程执行的墙钟运行时间与峰值内存；token 成本刻意未测，并被列为一项局限 | 只是报告出来的测度，而非预算——运行时间与内存与科学输出并列，两个 agent 之间「快」与「可审计」的取舍就从这里读出来 | 两个 agentic coding 系统在同一硬件上执行同一份引力波流程规格说明；共四次自主运行 | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| SkillAudit | 2026 | agent 执行时间与有效输入 token，以相对配对的「不用 skill」运行的节省量计（Efficiency Gain、Cost Gain，合成为取值于 [-1, 1] 的 ECG） | 只是报告出来的测度，而非预算——效率-成本增益是 per-skill 报告三个维度之一，另两个是效用（pass-rate 增益）与安全性评分 | 对 226 个真实 skill 包自动生成的逐一审计，覆盖 23 个职业门类；Codex / GPT-5.4 配置下有 643 个有效场景 | [→](../works/skillaudit.md) |
| Beyond Final Scores | 2026 | 每任务的墙钟小时数与逐模型的美元推理开销 | 预算限定运行时长；成本与分数并列报告，而非折算进分数 | 36 个 AutoLab 任务上的长时程 AI 研发 | [→](../works/beyond-final-scores.md) |
| R³-Bench | 2026 | 输出 token（无工具）或计数的工具动作（agentic），按各模型自身无预算基线校准为 ρ ∈ {0.2, 0.8} | 由六道题共用，分配本身成为被评估的能力 | 数学、竞赛编程与抽象推理 | [→](../works/r3-bench.md) |
| AI Research Preference Models | 2026 | 候选方案执行所耗的 H200 GPU 小时 | 预算固定，贡献在于如何**分配**——用一个冻结的预训练模型预测哪些候选值得真正跑一遍 | AI 研究 agent 在 ML 解空间上的搜索（AIRA-dojo 跑 AIRS-Bench） | [→](../works/ai-research-preference-models.md) |
| BATS / Budget Tracker | 2025 | 统一计价：token 开销加上按每次 0.001 美元固定计价的工具调用 | 预算是硬约束，但每一轮都让 agent **看得见**；scaling 曲线在统一计价下绘制 | 网页搜索 agent（BrowseComp、BrowseComp-ZH、HLE-Search），另有 τ²-bench 与 SWE-bench Verified | [→](../works/bats-budget-aware.md) |

## 还没解决的问题

- **不同场景下的资源规范化。** 一美元的 API 支出、一美元的 tool-call 费用、一秒的 wall-clock 或仿真时间并不直接可比。哪一种"资源货币"应作为跨 benchmark 比较的标准？或者它们本就无法完全统一？
- **静态 vs. 动态的鲁棒性。** CostBench 报告了显著的静态–动态下降。这一差距是当前模型的属性，还是仅是特定扰动分布的属性？领域是否应就一套标准扰动分布达成共识？
- **报告 vs. 优化。** 将资源作为一等目标的 benchmark 强制 agent 在预算下规划；仅报告资源使用的 benchmark 则没有。是否应显式区分这两类，以避免它们的数字被无声地拿去横向比较？
- **Token 成本 vs. tool-use 成本。** 聚合排行榜是否应仅报告 token（可移植、模型可比）还是也报告 tool-use 资源（在科学上有意义但依赖领域）？
- **预测出来的成本 vs. 花掉的成本。** 本页所有工作都是在动作**选定之后**再去限制或测量资源消耗。没有谁暴露出一个以动作为单位、以任务特征为条件的事前成本预测——即 `C(动作, 任务特征) → 分布`，覆盖 token、墙钟、GPU 时间、显存峰值与费用，并附带不确定性估计。这一点之所以要紧，是因为 agent 工作流方差大且带条件结构：一次失败会牵出「诊断—重试」链，因此实际期望成本是 `C₀ + P(失败)·C_重试 + …`，而不是把计划中的各步简单相加；而在预算下做取舍的规划器需要的是尾部分位数（p90），不是均值。由此引出三个问题。成本预测器究竟是一件**评估**工具，还是 agent 的一个组件——它到底该不该进入这条轴？这样的预测器是否应当按自身的校准度（分动作类别的预测值对实际值）单独计分，而不只看它带来的下游任务分数？以及，benchmark 是否应当在消耗量之外一并报告**预测误差**，好把「碰巧没超预算」的 agent 与「知道每件事要花多少因而没超」的 agent 区分开？
- **谁的估计算数。** 如果资源估计出自规划器自己的自然语言（「这大概要二十分钟」），它既没有依据也无从计分。把提出动作的执行者、为动作定价的估计器、以及在预算下放行或驳回的策略三者分开，就能各自独立地衡量——但本页目前没有任何 benchmark 把这三种角色分开评估。

## 相关工作

- [PostTrainBench](../works/posttrainbench.md)
- [CostBench](../works/costbench.md) — 动态 tool-use 条件下的成本最优规划。
- [SimulCost](../works/simulcost.md) — 覆盖 13 个仿真器的 cost-aware 物理仿真参数调优。
- [CATP-LLM / OpenCATP](../works/catp-llm.md) — OpenCATP，面向 cost-aware 工具规划的数据集（11,100 样本）。
- [MaD Physics](../works/mad-physics.md) — 模拟物理中按保真度定价的测量预算；agent 在测量的质与量之间权衡以推断被改动的物理定律。
- [BAGEN](../works/bagen.md) — 跨 token 与多资源 agent 的渐进式预算区间预测与可训练的提前停止。
- [VeRO / VeRO-Bench](../works/vero.md) — 在门控评估调用预算下把 coding agent 作为 agent 优化器来 benchmark。
- [Frontier-Eng](../works/frontier-eng.md) — 固定仿真器交互预算下的迭代式工程优化。
- [EcoAgent-Bench](../works/ecoagent-bench.md) — 定价动作与显式预算下的经济决策，以经济一致性评分。
- [HarnessOpt-Bench](../works/harnessopt-bench.md) — LLM 在固定且经 TEE 审计的评估预算下优化 agent harness。
- [Gravity-Bench-v1](../works/gravity-bench.md) — 引力物理发现中预算受限的观测规划。
- [SMDD-Bench](../works/smdd-bench.md) — 有限 oracle 调用预算下、保证有解的药物设计。
- [SDBench](../works/sdbench.md) — 按准确率-成本前沿评分的序贯诊断。
- [ChemCost](../works/chemcost.md) — 把反应成本计算本身作为被测任务，配无 judge 的精确定价真值。
- [MASSE](../works/masse.md) — 在端到端结构工程工作流 benchmark 中，把 token 用量与运行时间作为 rubric 的一个计分项。
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) — 每一次自主流程运行都测量运行时间与峰值内存；两个 agent 产出的科学结果相同，速度与资源占用便成了它们之间的一条比较轴。
- [SkillAudit](../works/skillaudit.md) — 对照配对的「不用 skill」运行测量时间与 token 的节省，逐个 skill 包与效用、安全性一并报告。
- [Beyond Final Scores](../works/beyond-final-scores.md) — 每任务墙钟预算与逐模型推理开销与性能并列报告，七个模型之间成本相差约 20 倍。
- [R³-Bench](../works/r3-bench.md) — 一份预算由六道题共用，并校准到各模型自己已展示出的单题水平。
- [AI Research Preference Models](../works/ai-research-preference-models.md) — 用不到三分之二的执行预算、约 15 小时就达到未引导 agent 24 小时的分数，并同时给出验证集与测试集的 oracle 上界。
- [BATS / Budget Tracker](../works/bats-budget-aware.md) — 把 token 与工具调用折算进同一种计价；仅仅把剩余预算告诉 agent，就能用十分之一的预算追平 ReAct 基线的准确率。

## 延伸阅读

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. 指出 cost-efficiency 是当前 agent 评估中覆盖不足的维度。<https://arxiv.org/abs/2503.16416>

**「预测成本」这一问题的既有谱系。** 上面的 Open Questions，实际上是把一个在 AI 中源流很长的问题，重新放到使用工具的 LLM agent 上重述了一遍。以下文献仅供定位，均非 LLM-agent 评估工作，也都不做成卡片。

- Russell, Wefald. *Principles of Metareasoning*. Artificial Intelligence 49(1–3):361–395, 1991（更早见于 KR 1989, 400–411）。把「思考」本身当作一个有成本的动作，并把计算的价值定义为它带来的期望改进减去其成本——这正是「一次工具调用或一次实验值不值得做」这一问法的形式化祖先。DOI 10.1016/0004-3702(91)90015-C
- Zilberstein. *Operational Rationality through Compilation of Anytime Algorithms*. AI Magazine 16(2):79–80, 1995。概述了 resource-bounded reasoning 这条线：每个组件携带一份**conditional performance profile**——它的输出质量随输入条件与所分配时间而变——再由运行时监控器据此在组合系统各部分之间分配资源。这是「以动作为单位、随条件变化的成本/质量 profile」在经典文献中最接近的术语。DOI 10.1609/aimag.v16i2.1136
- Klein, Falkner, Bartels, Hennig, Hutter. *Fast Bayesian Optimization of Machine Learning Hyperparameters on Large Datasets*（FABOLAS）。arXiv 1605.07079, 2016；AISTATS 2017。在目标函数之外另学一个显式的成本模型，并按「单位预测成本所换来的信息增益」挑下一次评估——同样是「先预测、再取舍」的结构，只不过发生在超参优化里。<https://arxiv.org/abs/1605.07079>
- Lee, Perrone, Archambeau, Seeger. *Cost-aware Bayesian Optimization*. arXiv 2003.10870, 2020。在评估代价各不相同且本身被建模的前提下，于固定预算内做成本感知的采集。<https://arxiv.org/abs/2003.10870>

「在期望 GPU 小时 ≤ B₁、费用 ≤ B₂ 的约束下最大化任务质量」这一提法，标准名称是 **constrained Markov decision process**；若把剩余预算显式放进状态，也常被称作 budgeted MDP。

**预算感知的 agent 方法（不做卡片——它们是方法，不是评估）。** 与本轴相邻、让 agent 行为随预算变化但未贡献评估工具的近期工作：

- Li, Deng, Li, Li. *Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents*（BAVT）。arXiv 2603.12634, 2026。以预算为条件的节点选择，随资源耗尽从探索式转为贪心式，并用一个残差价值预测器刻画步级进展。<https://arxiv.org/abs/2603.12634>
- Yang, Luo, Liu, Lou, Chen. *BAMAS: Structuring Budget-Aware Multi-Agent Systems*. arXiv 2511.21572, 2025。先用整数线性规划在成本各异的 LLM 之间做选择，再学习协作拓扑；报告在性能相当的前提下最多降低 86% 成本。<https://arxiv.org/abs/2511.21572>
