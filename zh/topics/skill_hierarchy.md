# Skill Hierarchy

> [English](../../topics/skill_hierarchy.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

两个 agent 总分一样，原因可能完全相反。一个 planning 很强，却不会正确用 tool；另一个能 retrieve 到信息，却从不 verify。单一 leaderboard score 看不出哪个更适合具体工作。

Skill hierarchy 会把 capability profile 拆开。比如 tool-use task 分别测 instruction following、planning、retrieval、execution 和 review，最后得到 `planning 90% / retrieval 40% / execution 85%`，retrieval bottleneck 就露出来了。这张图说明 agent 有哪些能力，不说明某一条 trajectory 为什么失败；后一个问题属于 credit assignment。

## Definition

Skill hierarchy 指把复杂的 agent 能力分解为一组更窄的能力或 subskill 的结构化集合，并配以对每个 subskill 分别打分的评估协议。这类 benchmark 共享一个设计承诺：单一聚合分数把太多东西混在一起——要理解 agent 能做什么、不能做什么，评估必须探查能力树的多个层次。

## Motivation

聚合排行榜掩盖了 agent 能力的形状。两个总分相同的 agent 可能在完全不同的 subskill 上失败，单指标排名无法告诉下游用户"哪一个 agent 更适合哪一类子任务"。Skill-hierarchy benchmark 通过产出**per-capability 画像**来解决这一问题。

Skill hierarchy 与 [Credit Assignment](./credit_assignment.md) 相关但不同。Skill hierarchy 问**agent 拥有哪些 subskill**；credit assignment 问**trajectory 的哪一步驱动了成功或失败**。两者可以合起来做——沿 trajectory 对每个 subskill 分别打分——但它们回答的是不同的问题。

## Existing Approaches

- **任务子目标分解。** [AgentBoard](../works/agentboard.md) 为每个任务标注一条子目标链，并报告进展率——实际上是 per-subgoal 的能力信号。
- **能力子过程分解（tool use）。** [T-Eval](../works/t-eval.md) 把 tool use 拆为 6 个子过程（instruction following / planning / reasoning / retrieval / understanding / review），在孤立任务上分别评估。
- **能力子过程分解（环境配置）。** [Enconda-bench](../works/enconda-bench.md) 把软件环境配置拆为 planning / error diagnosis / repair / execution。
- **以能力轴作为组织原则。** [UniClawBench](../works/uniclawbench.md) 围绕五个能力轴（Skill Usage、Exploration、Long-Context Reasoning、Multimodal Understanding、Cross-Platform Coordination）组织其 400 任务的 benchmark，并把这些轴作为主要报告维度。
- **跨 benchmark 的控制决策分类。** [AgentAtlas](../works/agentatlas.md) 不按任务或能力做分解，而是把 agent 的**控制决策**分成六类，覆盖 15 个 benchmark——提供的是跨任务可迁移的 skill-hierarchy 信号。
- **单一领域内的能力深度分层。** [CFDLLMBench](../works/cfdllmbench.md) 按*深度*而非按子过程来分解 CFD 能力：知识（CFDQuery）、数值与物理推理（CFDCodeBench）、实际工作流实现（FoamBench），各自是独立的任务集。由于这些层级在难度上是嵌套而非并列的，它给出的能力剖面更像一条天花板——很高的知识分数与近乎为零的端到端仿真成功率同时存在。
- **Tool-evolution 框架（越界归属）。** [GATE](../works/gate.md) 为覆盖完整性而纳入，但论文实际主题是面向 LLM 的图式 tool making，而非 skill 分解。详见卡片。
- **按侧面分解的 skill 使用。** [Skill-Use](../works/skill-use.md) 把「使用一个 skill」拆成三个可分离的侧面——触发相关 skill、遵从其规定流程、守住其边界——在 79 个真实 skill 与 177 个沙箱可执行任务上评估。触发与流程遵从表现为相互独立的瓶颈，最强配置的 SU 分数也只有 0.613。
- **为 skill 的内部结构估值。** [SkillSV](../works/skillsv.md) 把 skill 编译为单元、依赖与层级，并为每个单元赋予结构感知的 Shapley 价值，使 skill 库变得可审计——哪些单元配得上自己占用的上下文成本——并在不损失整体 skill 增益的前提下指导剪枝与压缩。
- **把评判者的 skill 知识作为测量对象。** [SkillTV-Bench](../works/skilltv-bench.md) 在 skill 增强执行上评估轨迹评判者——在该设定下，评判者必须掌握相应的 skill 知识才能判对——并证明缺失的验证知识本身可以外化为可复用的 JudgeSkill，为同一评判者带来 14.8 个百分点的准确率提升。
- **把组织方式当作独立于内容的一个变量。** [SkillJuror](../works/skilljuror.md) 固定一个 skill 的任务知识，只改它的排布——用一份精简的根文件按需指向支撑资源，对照一条做过归一化的扁平基线——在 410 组配对试验上比较。效果先出现在轨迹上，之后才出现在分数上：触及的不同资源数从 1.18 升到 3.85，采纳事件从 1.33 升到 3.92，多换来 17 次通过验证器的试验。这里被分解的是*产物*，不是能力，而它恰恰证明了两者可以分开。
- **从 skill 文本内部取出充分性与依赖关系。** 有两项工作不采用设计者的分类法，而是从 skill 自己的指令里取分解单位。[Skill Coverage](../works/skill-coverage.md) 把指令编译成带条件作用域的行为约束，再逐条约束地问：这条轨迹覆盖到它了吗？覆盖到之后行为通过了吗？——相当于把软件测试中的测试充分性搬了过来；结果是排行榜上的轨迹只覆盖了一个 skill 全部约束中的 38.66% 到 45.51%。[SLBench](../works/slbench.md) 抽取的则是指令*之间*的关系——前置条件、约束、回退方案，外加另外五种类型，在 5,000 多个公开 skill 中有 70% 含有这类关系——并把其中可局部测试的那些编译成 86 个可执行用例，不安全率高达 70%。
- **把原子与它们的组合分开来量。** [ATOM-Bench](../works/atom-bench.md) 把真机操作分解为动作原子与指令原子，只在原子上微调，把组合任务全部留出——再扣掉弱原子本身已能预测的那部分失败，于是它的 Compositional Failure Share 把「组合」孤立成一个独立的失败来源。[TS-Skill](../works/ts-skill.md) 得到同样的分离靠的不是归因而是构造：三项信号级 skill 在出题时就已指定，七种非空组合全部覆盖，因此单 skill 需求与组合需求在画像里本就可以分辨。
- **切换的代价，而非是否拥有某项 skill。** [Skill²-Bench](../works/skill2-bench.md) 测的是 per-subskill 画像里没有的一个量：skill 熵——一个有向的成对测度，刻画从一项推理 skill 转到另一项有多难；它只对照一个固定的参考模型推导一次，因此难度标尺不会随着新模型被纳入评测而漂移。对每个模型都查询两次——先让每一步孤立作答，再走完整条链——切换代价由此与单项 skill 的水平分离开来。
- **把 skill 层当作攻击面来分解。** 上面几项工作分解的是能力，另有一条安全线分解的是暴露面。[SkillSec-Eval](../works/skillsec-eval.md) 把 skill 生命周期切成五个各有独立信任边界的阶段——仓库准入、语义检索、规划器选取、运行时执行、演化——并在每一阶段分别报告攻击与防御，由此说明失效远在执行之前就已开始。[SCR-Bench](../works/scr-bench.md) 改按组合机制分解，给能力流动、信任传递与授权混淆各配一个子 benchmark 及配套的孤立对照，于是报告出的风险能归到组合本身，而不是归到那些 skill 上。[HarmfulSkillBench](../works/harmfulskillbench.md) 把危害定位在 skill 预期的功能之中，并用四种条件把「装上」的效应与「声明意图」的效应分开。
- **被评的对象是产物，而不是能力。** 有一簇工作评的是 skill 本身，而不去分解 agent 能做什么。在构建一侧，[SkillLearnBench](../works/skilllearnbench.md) 对自动生成的 skill 按功能覆盖、可执行性与安全性打分，与轨迹和结果并列；[SkillEvolBench](../works/skillevolbench.md) 在部署时把归纳出的 skill 库冻结，发现原始轨迹常常胜过由它蒸馏出的 skill。在采纳一侧，[SkillAudit](../works/skillaudit.md) 与 [A Framework for Evaluating Agentic Skills at Scale](../works/a-framework-for-evaluating-agentic-skills-at-scale.md) 干脆不要固定题库，直接从写好的 skill 包生成任务与 rubric，让覆盖面跟着该 skill 声明的范围走；两者都在配对运行上测量「用 skill」与「不用 skill」的差值。其中几张卡片在自己的 repository note 中就写明，这并不是本 topic 当初据以定义的那种分解模式；把它们收在这里，只因这是现有最接近的落脚点——与 [GATE](../works/gate.md) 的情形相同，那张卡片的归属说明也记下了同样的错位。

## Comparison

| Benchmark | Year | 分解粒度 | 轴 | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | 每任务的子目标链 | 任务特定（人工标注） | [→](../works/agentboard.md) |
| T-Eval | 2023 | 跨任务的能力子过程 | 6 个 tool-use 子过程 | [→](../works/t-eval.md) |
| Enconda-bench | 2025 | 跨任务的能力子过程 | 4 个环境配置子过程 | [→](../works/enconda-bench.md) |
| UniClawBench | 2026 | Benchmark 级组织轴 | 5 个 proactive-agent 能力 | [→](../works/uniclawbench.md) |
| AgentAtlas | 2026 | 每次控制决策（跨 benchmark 覆盖） | 6 类控制决策 | [→](../works/agentatlas.md) |
| GATE | 2026 | *Tool-evolution 框架，非 skill 分解——见卡片* | 层级化工具图 | [→](../works/gate.md) |
| CFDLLMBench | 2025 | 单一领域内的嵌套能力层级 | 3 个深度层级（知识 / 数值推理 / 工作流实现） | [→](../works/cfdllmbench.md) |
| Skill-Use | 2026 | 每个 skill 的侧面分解 | 3 个侧面：触发 / 流程遵从 / 边界遵守 | [→](../works/skill-use.md) |
| SkillSV | 2026 | Skill 内部的单元分解（单元 / 依赖 / 层级） | 每单元的结构感知 Shapley 价值 | [→](../works/skillsv.md) |
| SkillTV-Bench | 2026 | 评判者侧的 skill 知识，外化为可复用的 JudgeSkill | 评判准确率 + rollout 挑选提升 | [→](../works/skilltv-bench.md) |
| PEOA | 2024 | 工具学习的跨任务阶段分解 | 4 个阶段：任务规划 / 工具选取 / 工具调用 / 应答生成，各配一族自己的指标 | [→](../works/peoa.md) |
| ChemEval | 2024 | 单一领域内依职业需求划出的能力分类 | 42 个任务上的 4 个递进层级 × 12 个维度 | [→](../works/chemeval.md) |
| MaCBench | 2024 | 实验与表征工作的三个核心方面 | 数据抽取 / 实验理解 / 结果解读，按方面分项报告 | [→](../works/macbench.md) |
| ChemEBench | 2025 | 单一领域内递进的能力层级 | 3 个层级（基础知识 / 进阶知识 / 专业技能），覆盖 15 个维度、101 个任务 | [→](../works/chemebench.md) |
| HiSciBench | 2025 | 横跨六个学科的嵌套能力层级 | 5 个递升层级：事实素养 → 文献解析 → 文献问答 → 综述撰写 → 数据驱动发现，各配自己的评分协议 | [→](../works/hiscibench.md) |
| EmbodiedBench | 2025 | Benchmark 级精选的能力子集 | 6 个子集，涵盖常识推理、复杂指令理解、空间意识、视觉感知与长期规划 | [→](../works/embodiedbench.md) |
| RoboFAC | 2025 | 把失败理解分解为若干问答维度 | 8 个问答维度，逐维打分，以失败分析准确率为主指标 | [→](../works/robofac.md) |
| VIKI-Bench | 2025 | 具身多智能体协作的三级层次 | 智能体激活 / 任务规划 / 轨迹感知，各配自己的指标 | [→](../works/viki-bench.md) |
| AECBench | 2026 | 单一领域内嵌套的认知层级 | 23 个任务上的 5 个层级（记忆 / 理解 / 推理 / 计算 / 应用） | [→](../works/aecbench.md) |
| Gaia2 | 2026 | Benchmark 级的能力切分 | 7 个切分：Execution、Search、Ambiguity、Adaptability、Time，另加 Noise 与 Agent2Agent 两种增强 | [→](../works/gaia2.md) |
| LabRobFail | 2026 | 把失败分析拆成分别打分的能力 | 6 项：任务理解、失败检测、时间定位、严重度评估、失败分类、可执行的纠正 | [→](../works/labrobfail.md) |
| SciExplore | 2026 | 科学信息检索内部递进的任务类型 | 4 类：数据库导航、模糊文献检索、缺失引用补全、跨源结构化综合 | [→](../works/sciexplore.md) |
| PDAgent-Bench | 2026 | 任务级能力维度，另加一个工作流级层次 | 5 个维度（基础知识、报告理解、根因分析、静态时序分析、脚本生成），逐维报告 pass@1，另有全流程执行 | [→](../works/pdagent-bench.md) |
| DefectBench | 2026 | 在同一份统一语料上层层递进的三个认知层级 | 语义感知 / 空间定位 / 生成式几何分割，各配一族自己的指标 | [→](../works/defectbench.md) |
| SkillJuror | 2026 | Skill 产物的组织方式，与 skill 内容分开处理 | Progressive Disclosure 对照归一化的扁平排布；每条轨迹触及的资源数与采纳事件数 | [→](../works/skilljuror.md) |
| Skill Coverage | 2026 | 对 skill 自身指令按约束逐条分解 | 抽取出的行为约束的覆盖率 × 已覆盖约束上的 Pass/Fail | [→](../works/skill-coverage.md) |
| SLBench | 2026 | 对 skill 指令之间的依赖按关系逐类分解 | 8 种关系类型（前置条件、约束、回退方案……）；按 harness 与主干模型分别报告不安全率 | [→](../works/slbench.md) |
| SkillLearnBench | 2026 | 对 skill 学习方法产出物的三层分解 | Skill 质量（功能覆盖 / 可执行性 / 安全性）、轨迹质量、任务结果 | [→](../works/skilllearnbench.md) |
| SkillEvolBench | 2026 | 按阶段分解：获取阶段 vs. 冻结后的部署阶段 | LSR / RSR / ESR，其中 ESR 再分为上下文漂移、对抗性捷径与组合 | [→](../works/skillevolbench.md) |
| SkillAudit | 2026 | 直接由 skill 产物本身生成的逐包审计 | 效用（pass-rate 增益）/ 效率-成本增益 / 安全性评分 | [→](../works/skillaudit.md) |
| A Framework for Evaluating Agentic Skills at Scale | 2026 | 每个生成任务配两族 rubric，按「用 skill」与「不用 skill」的差值计分 | 指令遵循 vs. 目标达成 | [→](../works/a-framework-for-evaluating-agentic-skills-at-scale.md) |
| Agent Skill Evaluation and Evolution | 2026 | *综述——给出的是该领域的分类法，而非可打分的分解* | 4 类演化范式 × 6 类以 skill 为中心的 benchmark | [→](../works/agent-skill-evaluation-survey.md) |
| SkillCoach | 2026 | 对 skill 使用过程的四维分解，rubric 由 rollout 归纳而来 | Skill 选取 / skill 遵循 / skill 组合 / 以 skill 为依据的反思 | [→](../works/skillcoach.md) |
| BACKROOMBench | 2026 | 对 skill 做五条轴的干预，把「自称用了」与「实测有影响」分开 | 语义 / 措辞 / 身份 / 内容 / 指派；依赖度、带符号效用、Attribution Fidelity Score、Backroom Gap | [→](../works/backroombench.md) |
| SkillShapley | 2026 | 单个 skill 内部的逐步分解 | 在分界自适应采样预算下为每个 skill 步骤计 Shapley 值 | [→](../works/skillshapley.md) |
| Skill²-Bench | 2026 | 在一个 558 项 skill 的库上按成对切换做分解 | 每个有序 skill 对的有向 skill 熵；单 skill 与跨 skill 之间的分差 | [→](../works/skill2-bench.md) |
| RigorBench | 2026 | 对工程过程纪律的七支柱分解 | 计划忠实度 / 验证覆盖率 / 恢复效率 / 弃权质量 / 原子转换完整性 / 测试断言密度 / 探索效率，加权合成 RigorScore | [→](../works/rigorbench.md) |
| ATOM-Bench | 2026 | 把操作分解为原子，组合任务全部留出 | 6 个动作原子 × 7 个指令原子；Atomic Score vs. Compositional Failure Share | [→](../works/atom-bench.md) |
| TS-Skill | 2026 | 信号级 skill 在构建时即已标注，且组合全覆盖 | 3 项 skill：时间尺度选择 / 时间定位 / 跨区间整合，覆盖全部 7 种非空组合 | [→](../works/ts-skill.md) |
| RubricsTree | 2026 | 自顶向下的 rubric DAG，从宏观能力一路拆到原子布尔叶节点 | 100 多条临床可核验的叶节点 rubric，按查询路由并自动配权 | [→](../works/rubricstree.md) |
| HarmfulSkillBench | 2026 | 覆盖 skill 层的危害分类，与安装条件的分解相交叉 | 分两级的 20 个策略类别；被动暴露 / 主动调用 / 去除防护 / 无 skill 基线 | [→](../works/harmfulskillbench.md) |
| SCR-Bench | 2026 | 各组合机制各配一个子 benchmark，并各带一个配套的孤立对照 | 能力流动 / 信任传递 / 授权混淆 | [→](../works/scr-bench.md) |
| SkillSec-Eval | 2026 | 把 skill 生命周期切成各有独立信任边界的若干阶段 | 5 个阶段：仓库准入 / 语义检索 / 规划器选取 / 运行时执行 / skill 演化，每阶段分报攻击与防御 | [→](../works/skillsec-eval.md) |

## Open Questions

- **任务特定 vs. 跨任务分解。** AgentBoard 对每个任务单独分解成子目标；T-Eval / Enconda-bench 则把能力本身分解成跨任务共享的子过程；AgentAtlas 跨 benchmark 按控制决策类型做分解。哪一种能给出更可迁移的能力画像？
- **轴的选择。** T-Eval 的 6 个、Enconda-bench 的 4 个、UniClawBench 的 5 个、AgentAtlas 的 6 个都是合理分解。是否存在一个规范化的最小集合，还是轴的选择必然依赖领域？
- **合成。** 这个问题最初问的是：per-subskill 分数该如何合成为一个总体能力估计。如今有两项结果与之相关，而且都指向同一个答案——合不出来。ATOM-Bench 在同一批策略上分别测量原子能力与组合能力，报告 Pi0.5 在任务所需原子上的 Atomic Score 达到 83.3%，而留出的组合任务只成功了 15.8%；它设立 Compositional Failure Share，正是为了量化弱原子*解释不了*的那部分失败。Skill²-Bench 则发现，同一项 skill 放进跨 skill 链条里考察，比作为孤立问题考察时准确率低大约 4 到 13 个百分点，而且各领域的切换难度与各领域自身的难度基本脱钩——科学本是个容易的领域，切换熵却最高。可见组合表现得更像一项独立的能力，而不是能力画像的某个函数；这个开放问题也随之变成：如何直接测量它。
- **分解 vs. 归纳。** 本页如今装着两类结构上不同的东西：一类 benchmark 分解一项能力并给各部分打分，另一类给 agent *产出*的 skill 打分（SkillLearnBench、SkillEvolBench、SkillAudit、A Framework for Evaluating Agentic Skills at Scale，以及 GATE——其卡片已记下这种错位）。后一类中有几张卡片在 repository note 里就是这么说的。这两类该不该放在同一个标题之下？第二类本身是否自成一条脉络？
- **嵌入式 vs. 覆盖式分解。** Skill-hierarchy 信号应由底层 benchmark 内嵌产出（AgentBoard、T-Eval、Enconda-bench、UniClawBench 的方式），还是作为跨 benchmark 的覆盖层（AgentAtlas 的方式）？

## Related Works

- [AgentBoard](../works/agentboard.md)
- [T-Eval](../works/t-eval.md)
- [Enconda-bench](../works/enconda-bench.md)
- [UniClawBench](../works/uniclawbench.md)
- [AgentAtlas](../works/agentatlas.md)
- [GATE](../works/gate.md) — 为覆盖完整性而纳入；实际主题是面向 LLM 的 tool making，而非 skill-hierarchy 评估。
- [CFDLLMBench](../works/cfdllmbench.md)
- [Skill-Use](../works/skill-use.md)
- [SkillSV](../works/skillsv.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [PEOA](../works/peoa.md)
- [ChemEval](../works/chemeval.md)
- [MaCBench](../works/macbench.md)
- [ChemEBench](../works/chemebench.md)
- [HiSciBench](../works/hiscibench.md)
- [EmbodiedBench](../works/embodiedbench.md)
- [RoboFAC](../works/robofac.md)
- [VIKI-Bench](../works/viki-bench.md)
- [AECBench](../works/aecbench.md)
- [Gaia2](../works/gaia2.md)
- [LabRobFail](../works/labrobfail.md)
- [SciExplore](../works/sciexplore.md)
- [PDAgent-Bench](../works/pdagent-bench.md)
- [DefectBench](../works/defectbench.md)
- [SkillJuror](../works/skilljuror.md)
- [Skill Coverage](../works/skill-coverage.md)
- [SLBench](../works/slbench.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [SkillAudit](../works/skillaudit.md)
- [A Framework for Evaluating Agentic Skills at Scale](../works/a-framework-for-evaluating-agentic-skills-at-scale.md)
- [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](../works/agent-skill-evaluation-survey.md)
- [SkillCoach](../works/skillcoach.md)
- [BACKROOMBench](../works/backroombench.md)
- [SkillShapley](../works/skillshapley.md)
- [Skill²-Bench](../works/skill2-bench.md)
- [RigorBench](../works/rigorbench.md)
- [ATOM-Bench](../works/atom-bench.md)
- [TS-Skill](../works/ts-skill.md)
- [RubricsTree](../works/rubricstree.md)
- [HarmfulSkillBench](../works/harmfulskillbench.md)
- [SCR-Bench](../works/scr-bench.md)
- [SkillSec-Eval](../works/skillsec-eval.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
