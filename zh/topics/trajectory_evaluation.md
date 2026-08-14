# Trajectory Evaluation

> [English](../../topics/trajectory_evaluation.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

Trajectory evaluation 指的是一类评估方法：根据 agent 产生的动作序列与中间状态来打分，而不仅是最终答案。指标可以包括分步正确性、子目标完成度、按能力子过程打分、推理质量、evidence grounding 或过程效率。

## Motivation

端到端 success 是一种粗信号。两个都失败——或都成功——的 agent，在**如何**达成结果上可能有重要差异。Trajectory 级指标能揭示这些差异，使我们诊断 agent 的能力在**哪一步**开始崩坏。

Trajectory evaluation 对长 horizon 场景同样至关重要——单一的最终奖励难以定位到底哪一步出了问题。

## Existing Approaches

Trajectory-evaluation 贡献大致可归为六条设计线。前四条是任务套件；第五条是覆盖在既有 benchmark 之上的诊断框架；第六条直接针对"参考 trajectory 从何而来"这一问题。

- **基于子目标（subgoal-based）。** 将 trajectory 用一条子目标链标注，以完成比例作为主指标。[AgentBoard](../works/agentboard.md) 是这一路线的代表，将子目标级的进展率与分析面板结合。
- **分级子任务 / 密集奖励（graded-subtask）。** 任务被分解为可打分（非二值）的子任务，在可配置的奖励阈值下聚合。[Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) 在长 horizon terminal 任务上沿这一路线。
- **能力分解（capability-decomposed）。** 将某种复杂能力拆解为若干子过程，并在孤立任务上分别打分。[T-Eval](../works/t-eval.md) 将 tool use 拆为 6 个子过程；[Enconda-bench](../works/enconda-bench.md) 将环境配置拆为 planning / diagnosis / repair / execution 四个子过程；[PEOA](../works/peoa.md) 把这一思路用于化工与过程工程，对工具学习的四个阶段分别打分——任务规划对照金标准方案，工具选择以 Recall@K / NDCG@K / COMP@K 对照真值工具集，工具调用看约定一致性、参数抽取正确性与错误处理，回答生成则用 BLEU / ROUGE-L / 精确匹配。
- **效用函数（utility-function based）。** 在整条 trajectory 上定义关于多个质量维度的联合指标。[TRACE](../works/trace.md) 面向 deep-research agent，联合 accuracy、efficiency、evidence grounding、reasoning quality；[FinTrace](../works/fintrace.md) 在金融 tool use 上采用 4 维度 9 指标。
- **诊断覆盖层（diagnostic overlay）。** 本身不是任务套件，而是把诊断词汇与审计协议覆盖到既有 benchmark 之上。[AgentAtlas](../works/agentatlas.md) 在 15 个 agent benchmark 上应用一个六路控制决策分类与失败分类；[Insights Generator](../works/insights-generator.md) 是面向 trace 语料级诊断的多 agent 系统。
- **确定性 ground-truth 生成。** Trajectory 评估依赖高质量的参考 trajectory。[Traxgen](../works/traxgen.md) 直接针对参考生成这一问题：把结构化的 workflow 规范与用户数据编译为 DAG 上的确定性 gold trajectory，取代基于 LLM 的 ground-truth 生成，得到可复现且数量级更快的替代方案。
- **人工标注的 step-level 有效性。** [AgentProcessBench](../works/agentprocessbench.md) 以三元 +1 / 0 / −1 方案为 1,000 条多轮 tool-use trajectory 中的 8,509 个 assistant step 打标，标注者间一致性达 89.1%。
- **与验证配对的 trajectory 评审。** [AgentLens](../works/agentlens.md) 将五个 LLM-judge 维度与形式化验证平均为一个质量指数，并为每个分数附上一份有据可查、链接到证据的书面评审，从而把靠脆弱捷径通过客观检查的运行与真正干净的运行区分开。
- **Span 级错误定位。** [TELBench](../works/telbench.md) 把 1,000 条经验证的 deep-research trajectory（平均 11.95 个 span）切分为错误 / 非错误 span，要求模型找出最早的有害决策；其 DRIFT 审计框架把整体 macro-F1 最高提升至 54.91。
- **形式逻辑裁决每一步。** [MATP](../works/matp.md) 把自然语言推理的每一步自动形式化为一阶逻辑并交由自动定理证明器裁决，在 PrOntoQA-OOD 上步骤正确性的 macro F1 达到 94.26%，而 GPT-4o prompting baseline 为 47.79%。
- **由求解器导出的参考推理链。** [VCoT-Bench](../works/vcot-bench.md) 把 Z3 证明提升为人可读的 Verus 步骤，并让模型补全被刻意移除的块，因此轨迹 credit 是对照证明器实际所需的推理来衡量，而非一个二元的验证结果。
- **逐级设卡的工件正确性。** [SysMoBench](../works/sysmobench.md) 为 11 个真实系统工件的 AI 生成 TLA+ 模型评分，四项自动检查的指标——语法、运行时、trace 一致性、不变式正确性——逐级设卡，并明确拒绝 LLM-as-a-judge 评分。
- **模块级证明检查。** [Pseudo-Formalization](../works/pseudo-formalization.md) 把证明改写为自包含模块并独立核验每一个前提–结论模块，在 35 篇 arXiv 论文、共 40 处已披露错误上考察错误定位。
- **成对轨迹偏好。** [Plan-RewardBench](../works/plan-rewardbench.md) 让一条选中轨迹与一条易混淆的 hard negative 在 1,171 对样本上对抗，考察的是评判者而非 agent。
- **评判者与专家标签的一致性。** [AgentRewardBench](../works/agentrewardbench.md) 用 1,302 条 web agent 轨迹上的专家标签考察 12 个 LLM judge 与各 benchmark 自带的规则式评分器，发现没有任何 judge 的 precision 超过 70%。
- **Harness 效应诊断。** [Harness-Bench](../works/harness-bench.md) 固定任务、沙箱、预算与评估器，只变换模型外围的 harness，用安全门控的 completion × 过程分（从轨迹评出的 robustness、tool use、consistency）为 5,194 条轨迹打分；在完全相同的任务与模型上，最好与最差的可配置 harness 相差 23.8 分，支持按模型–harness 配置报告能力。
- **以 commit 为结果锚点的真实环境轨迹。** [SWE-chat](../works/swe-chat.md) 用来自 opt-in 开源开发者的约 6,000 个真实 coding-agent 会话取代人工编写的任务，把每一行提交代码归属到人类或 agent。其轨迹指标植根于用户真正保留的内容——agent 产出代码中仅 44.3% 最终进入用户 commit——并辅以经人类 gold 标签验证的 LLM 标注会话成功度（0–100）与逐轮 pushback 标签。
- **Skill 感知的轨迹验证。** [SkillTV-Bench](../works/skilltv-bench.md) 在 681 条来自 skill 增强执行的真实轨迹上评测 LLM-as-a-Judge 与 Agent-as-a-Judge——在这一设定下，评判者必须掌握任务相关的 skill 知识才能判对。其 SkillTV-Evolve 循环把误判样例蒸馏为可复用的 JudgeSkill，使同一评判者的准确率提高 14.8 个百分点，并把从 rollout 池中挑出轨迹的成功率从单条时的 22.9% 提升到十条时的 45.5%。
- **对失败搜索运行的定位-归因-修复审计。** [SearchAuditor](../works/searchauditor.md) 把失败分析变成一个有 benchmark 支撑的任务：在 SearchAuditBench 的 1,243 条专家标注失败 deep-search 轨迹（平均 65.1K token）上，端到端考察关键步骤定位、搜索特有的根因归因，以及对照带评分 rubric 的参考修复打分。
- **错误生命周期追踪。** [TRAJDEBUG](../works/trajdebug.md) 通过多粒度历史压缩、基于证据的错误识别与解决状态追踪，把 agent 事后已恢复的错误与真正决定失败的错误区分开，以 TrajErrBench 的 486 条人工标注失败轨迹（取自 Tau2Bench 与 SWE-Bench Pro）为锚点。
- **执行轨迹的语义评估。** [EnvTrace](../works/envtrace.md) 让 LLM 生成的仪器控制代码在同步辐射光束线的数字孪生上执行，通过对齐执行轨迹得到覆盖多个行为维度的功能正确性分——在「正确性即随时间的物理行为」的场景里，轨迹比较替代了单元测试；30 余个 LLM 受评。
- **模块化的具身错误分析。** [Embodied Agent Interface](../works/embodied-agent-interface.md) 把具身 LLM 的失败按决策模块拆成幻觉、affordance 与规划错误，对照模拟器状态检查。
- **机器人失败解释。** [REFLECT / RoboFail](../works/robofail.md) 让 LLM 在层级化的多传感器经验摘要上推理，解释操作失败并引导纠正规划。
- **规模化的失败检测。** [AHA](../works/aha.md) 在程序化生成的失败轨迹（FailGen）上微调 VLM 来检测并解释操作失败，超过 GPT-4o 上下文学习 10.3%。
- **分类化的失败问答。** [RoboFAC](../works/robofac.md) 在 9,440 条错误轨迹上提供 78,623 个 QA 对，覆盖八个失败理解维度，并把专用模型用作真实管线的监督者。
- **实验室机器人失败分析。** [LabRobFail](../works/labrobfail.md) 向模拟化学自主实验室执行注入控制级、物理级与语义级失败，评估六项诊断能力。
- **反事实的路由评估。** [The Replay Gap](../works/the-replay-gap.md) 指出：通过重放已记录轨迹来给逐步模型切换打分，度量的是一个从未真正运行过的世界，并以分叉的反事实 rollout 与匹配的同模型对照分叉取而代之。
- **面向故障定位的遥测充分性。** [TelemetrySuffBench](../works/telemetrysuffbench.md) 在带延迟绑定故障的合成多组件轨迹上，把失败检测与故障源定位分开，揭示遥测被削减时的检测–定位落差。
- **组件级轨迹归因。** [Long-Horizon Agent Trajectory Attribution](../works/long-horizon-agent-trajectory-attribution.md) 在统一组件 schema 下，于 1,351 条标注 agent 轨迹上引入主责组件归因与归因链恢复。
- **计划遵从度。** [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md) 在 16,991 次运行上衡量 SWE-agent 轨迹对既定计划的忠实程度，把遵从度拆解为阶段覆盖、顺序与逐阶段保真度。
- **轨迹上的反事实因果归因。** [TempoBench](../works/tempobench.md) 在可形式验证的 Mealy 机执行轨迹上，把前向模拟与最小必要成因识别分开，量化 SIM/MIN 落差。
- **推理对齐的代码评估。** [RACE-Bench](../works/race-bench.md) 把可执行的补丁验证与结构化的参考推理配对，评估仓库级 code agent 的中间推理与开发者认可轨迹的对齐程度。
- **阶段对齐的问题解决诊断。** [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) 在可执行补丁评估之外，补充需求澄清与实现规划的已验证真值，实现对完整编码轨迹的 GT 对齐诊断。
- **推理轨迹可靠性。** [MiraMind](../works/miramind.md) 沿可用性、逻辑结构与信息贡献为心理健康推理轨迹打分，把正确的最终答案与不可靠的"证据到判断"路径区分开。
- **以对抗方式检验的逐动作准入判定。** [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md) 把判定单位从最终任务下移到单个被提出的动作：LLM 每提出一个控制动作，都要经由对装置 P&ID 的图遍历，核查位号是否存在、是否可执行、失效状态是否一致以及下游影响如何。验证器自身的覆盖面也一并纳入度量——针对其各类失效模式构造了 43 个无效方案，在所覆盖的类别上报告 100% 召回率；此外还有一项 N = 50 的鲁棒性研究，覆盖不安全方案占比从 10% 到 70% 的各种运行，以及一条 B0–B3 阶梯，为每一级上下文增强单独计分。
- **从轨迹里读出 skill 起了什么作用。** 当 agent 配上一个可复用的 skill，轨迹就成了这个 skill 的作用唯一显形的地方，一批工作也就相应地在轨迹上下探针。[SkillJuror](../works/skilljuror.md) 统计每条轨迹触及的不同 skill 资源数与有效采纳次数，发现组织方式先动的是这两个量，之后才轮到结果。[Skill Coverage](../works/skill-coverage.md) 把测试充分性的思路移植过来：把 skill 指令编译成带条件作用域的行为约束，再逐条轨迹考察它覆盖了哪些约束、以及观察到的行为是否通过。[SkillCoach](../works/skillcoach.md) 的 rubric 是在一道校验闸门下从真实 rollout 中提炼出来的，对选取、遵循、组合与反思分别评分，并有意把外部验证器排除在 rubric 之外，好让过程与结果可以彼此不一致。[SkillLearnBench](../works/skilllearnbench.md) 在两者之下又加了第三层：生成出来的 skill 产物，与产出它的那条轨迹一并评分。
- **用生命周期上的多道闸门取代唯一的终态裁决。** [SkillMisevo-Bench](../works/skillmisevo-bench.md) 把轨迹到 skill 这条流水线上的编写、检索与执行分成三道独立的闸门来测量——因为一个终态的攻击成功率数字无法区分「库本身是安全的」与「不安全的产物只是碰巧没被检索到」；在它的全网格中，21 种演化条件全都写出了不安全产物，其中 19 种会把它们检索回来，而只有 15 种会让危害留存到全新的会话里。
- **把过程纪律本身作为工程工作的一个计分维度。** [RigorBench](../works/rigorbench.md) 从经插桩的执行轨迹中算出七根加权支柱——计划忠实度、验证覆盖率、恢复效率、弃权质量、原子转换完整性、测试断言密度、探索效率——并在同一批运行上单独给结果打分，使过程与结果的关系本身成为研究对象；它固定基础模型，只变 harness。
- **每个实例都标注了金标准计划。** [AISE-Bench](../works/aise-bench.md) 把全部 1,133 个实例端到端地标注了一遍——查询、计划、实际执行的 API 调用及其经校验的参数、参考答案——于是过程指标有了金标准可依，而不必靠启发式：计划按与标注计划之间的图编辑距离评分，参数准确率则作为一等指标报告；多数被评方法虽然部分完成度很高，恰恰是在这里失分。
- **当产物本身难以检查时，改用参考操作链。** [DrafterBench](../works/drafterbench.md) 为土木工程图纸修改评分的办法，是计算 agent 记录下来的操作链与参考操作链之间的交并比；配套的 dual function 只记录操作路径而不改动文件，因此修改后的 PDF 根本无需人眼查看。在它的 1,920 个任务里，指令质量是一个受控变量：措辞无结构、取值含糊、信息不全这三种情况可以各自独立开关，结果也按控制变量分别报告，于是轨迹得分的下滑能被归因到某一种具体的指令缺陷上。

## Comparison

| Work | Year | Trajectory 指标 | Domain | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | 基于标注子目标的进展率 | Embodied / game / web / tool | [→](../works/agentboard.md) |
| T-Eval | 2023 | 6 个 tool-use 能力子过程分别打分 | Tool use | [→](../works/t-eval.md) |
| Long-Horizon-Terminal-Bench | 2026 | 分级子任务 + 阈值聚合的部分奖励 | Terminal 长 horizon | [→](../works/long-horizon-terminal-bench.md) |
| Enconda-bench | 2025 | 4 个环境配置子过程的过程级打分 | 软件环境配置 | [→](../works/enconda-bench.md) |
| TRACE | 2026 | Hierarchical trajectory utility + scaffolded-capability assessment | Deep research | [→](../works/trace.md) |
| FinTrace | 2026 | 4 维度共 9 指标（action / efficiency / process / output） | 金融 | [→](../works/fintrace.md) |
| AgentAtlas | 2026 | 6 路控制决策分类 + 失败分类（覆盖 15 个 benchmark 的审计） | 跨 benchmark 覆盖 | [→](../works/agentatlas.md) |
| Insights Generator | 2026 | 自动化的语料级 trace 诊断（多 agent 假设检验） | Trace 语料分析 | [→](../works/insights-generator.md) |
| Traxgen | 2025 | 基于 DAG 的确定性 ground-truth 生成（与 gold 100% 对齐；相较 LLM 生成中位数 > 17,000× 加速） | 客户服务 tool use（配套 benchmark） | [→](../works/traxgen.md) |
| AgentProcessBench | 2026 | 步骤有效性（StepAcc / FirstErrAcc） | Tool use（web / CLI / API） | [→](../works/agentprocessbench.md) |
| AgentLens | 2026 | 覆盖 5 个 LLM-judge 维度的质量指数 + 形式化验证；成对并排评审 | 交互式编码（Java） | [→](../works/agentlens.md) |
| TELBench | 2026 | Span 级 F1 + 首错准确率 | Deep-research agent trajectory（GAIA、XBench、BrowseComp） | [→](../works/telbench.md) |
| MATP | 2025 | 每一步的 provable / refutable / indeterminate 判定，外加六类推理链分类 | 演绎逻辑推理 | [→](../works/matp.md) |
| VCoT-Bench | 2026 | 加权的语法 + 语义块补全准确率 | Verus 中的 Rust 验证 | [→](../works/vcot-bench.md) |
| SysMoBench | 2025 | 四项逐级设卡的部分得分指标（语法 → 运行时 → trace 一致性 → 不变式），不用 LLM judge | 并发 / 分布式系统的形式化建模 | [→](../works/sysmobench.md) |
| Pseudo-Formalization | 2026 | 错误定位 precision + recall；每份证明的覆盖率与误报错误 | 数学证明验证 | [→](../works/pseudo-formalization.md) |
| Plan-RewardBench | 2026 | chosen / rejected 轨迹对上的成对判定准确率 | 工具集成的 agent 规划 | [→](../works/plan-rewardbench.md) |
| AgentRewardBench | 2025 | 评判者相对专家成功标签的 precision | Web agent | [→](../works/agentrewardbench.md) |
| Harness-Bench | 2026 | 安全门控的 Completion × Process（从轨迹评出的 robustness / tool use / consistency） | 跨 harness 的可执行 agent 工作流（8 类） | [→](../works/harness-bench.md) |
| SWE-chat | 2026 | 每行提交代码的代码存活 / 效率 / 成本 + LLM 标注的会话成功度与逐轮 pushback，基于真实用户轨迹 | 真实环境的 coding-agent 会话（开源仓库） | [→](../works/swe-chat.md) |
| SkillTV-Bench | 2026 | Skill 增强执行上的评判准确率 + rollout 池挑选成功率 | Skill 增强的 agent 执行（11 个领域） | [→](../works/skilltv-bench.md) |
| SearchAuditor | 2026 | 关键步骤定位、根因归因与按 rubric 修复的端到端通过率 | 长 horizon deep-search 轨迹 | [→](../works/searchauditor.md) |
| TRAJDEBUG | 2026 | 错误识别 + 经解决状态与最终影响的关键归因 | Tool-use 与编码的失败轨迹 | [→](../works/trajdebug.md) |
| EnvTrace | 2025 | 对照数字孪生的执行轨迹对齐；多维度功能正确性分 | 仪器控制代码（同步辐射光束线） | [→](../works/envtrace.md) |
| Embodied Agent Interface | 2024 | 按决策模块的类型化错误分类（幻觉/affordance/规划） | 具身任务规划（VirtualHome、BEHAVIOR） | [→](../works/embodied-agent-interface.md) |
| REFLECT / RoboFail | 2023 | 从多传感器摘要出发的 LLM 失败解释；纠正规划成功率 | 机器人操作失败分析 | [→](../works/robofail.md) |
| AHA | 2024 | 自由形式的失败检测/推理；模糊匹配、ROUGE-L、二元成功 | 机器人操作失败（模拟生成 + 真实） | [→](../works/aha.md) |
| RoboFAC | 2025 | 八维度失败问答；失败分析准确率 | 机器人操作失败分析与纠正 | [→](../works/robofac.md) |
| LabRobFail | 2026 | 六项能力，含时间定位与严重度评估 | 化学自主实验室机器人失败（模拟） | [→](../works/labrobfail.md) |
| The Replay Gap | 2026 | 分叉 rollout 的偏离（归一化编辑距离、动作改写比例）对照匹配的同模型对照分叉；重放评估器审计 | agent 式模型路由（SWE-bench 底座） | [→](../works/the-replay-gap.md) |
| TelemetrySuffBench | 2026 | 遥测掩蔽下的起源步骤 Top-1 定位对照检测 F1；弃权（FAR / UAR） | agent 遥测 / trace 诊断（合成） | [→](../works/telemetrysuffbench.md) |
| Long-Horizon Agent Trajectory Attribution | 2026 | 主责组件定位（Hit@1、MRR）+ 归因链恢复（Recall@K、MAP） | LLM-agent 工具使用 / 安全轨迹 | [→](../works/long-horizon-agent-trajectory-attribution.md) |
| Evaluating Plan Compliance (From Plan to Action) | 2026 | 计划阶段遵从 / 顺序遵从 / 阶段保真度（几何平均），覆盖 16,991 条轨迹 | 编程 agent（SWE-bench） | [→](../works/from-plan-to-action.md) |
| TempoBench | 2025 | SIM/MIN 分离：前向模拟步骤准确率对照最小必要成因识别 | 执行轨迹的因果推理（Mealy 机） | [→](../works/tempobench.md) |
| RACE-Bench | 2026 | 双轨：补丁解决率 + 相对开发者参考轨迹的推理对齐召回 / 过预测 | 仓库级 code agent（功能新增） | [→](../works/race-bench.md) |
| SWE-RPG | 2026 | 解决率 + GT 对齐的阶段失败归因与逐阶段澄清 / 规划覆盖 | 仓库级问题解决（Python / Java） | [→](../works/a-unified-issue-resolution-benchmark-for-requireme.md) |
| MiraMind | 2025 | 在可用性、逻辑结构、信息贡献上给推理轨迹打分（与结果指标并列） | 心理健康推理 | [→](../works/miramind.md) |
| PEOA | 2024 | 工具学习的分阶段打分：规划（工具使用意识、通过率、相对金标准方案的计划准确率）、工具选择（Recall@K、NDCG@K、COMP@K）、工具调用（约定一致性、参数抽取、错误处理）、回答生成（BLEU、ROUGE-L、EM） | 化工与过程工程问题求解（MathComp、ChemProc） | [→](../works/peoa.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | 通过 P&ID 图遍历逐动作验证（位号存在性、可执行性、失效状态、下游影响）；在 43 个注入的无效方案上的验证器召回率、N = 50 次鲁棒性运行、B0–B3 上下文阶梯 | 工业过程控制（Tennessee Eastman 以及另外两个装置场景） | [→](../works/aae-framework.md) |
| DrafterBench | 2025 | 记录下来的操作链与参考操作链之间的交并比，叠加在两级评分（代码可执行性，再到六个子任务上的目标完成度）之上，并对弱子任务扣分；按各指令控制变量分别报告 | 覆盖 46 个自定义工具的土木工程技术图纸修改 | [→](../works/drafterbench.md) |
| AstroVisBench | 2025 | 把同一条工作流分阶段评分：处理阶段用 Variable Inspection Score 衡量它产出的标准答案内存变量，随后由一个依据与五位职业天文学家的相关性（ρ = 0.822）选出的 judge，对最终的图给出 No / Minor / Major 错误判定；崩溃率与 VisFail 率则与这两者分开报告 | 源自教程 notebook 的天文科学计算与可视化 | [→](../works/astrovisbench.md) |
| Spec-o3 / SpecVI-Bench | 2026 | 六位天文学家在标签准确率之外，依公开的 0–5 分 rubric 就连贯性与物理自洽性为 100 条推理轨迹打分；另在每个巡天的 50 个案例上与 o3 做两两偏好对比；每条轨迹的工具调用上限为 8 次 | 稀有天体的天文光谱甄别（LAMOST、SDSS/DESI） | [→](../works/spec-o3.md) |
| Plausible but Wrong | 2026 | 由 Execution Success、Parameter Accuracy 与 Numerical Accuracy 上的阈值界定四种互斥的失败模式——代码失败、参数错误、计算错误、正确——从而把静默的数值错误与崩溃分开归类，而不是压成一个通过/不通过 | 天体物理计算工作流（CAMB 求解器调用与档案数据分析） | [→](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
| First head-to-head comparison of agentic AI on Einstein Telescope data | 2026 | 从 agent 自己的日志中数出的过程行为——重启、对规格说明的静默偏离与显式自我纠正之别、未经要求的优化、token 预算变动、指令理解上的分歧——与相同的科学输出、运行时间和峰值内存并列报告 | 在模拟 Einstein Telescope 数据上执行引力波流程 | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| SkillJuror | 2026 | 每条轨迹触及的不同 skill 资源数与有效采纳次数（Progressive Disclosure 下分别由 1.18 → 3.85、1.33 → 3.92），通过验证器的试验数作为滞后的次级信号 | Agent skill 的组织方式；基于 82 个任务的 SkillsBench 研究，共 410 组配对试验 | [→](../works/skilljuror.md) |
| Skill Coverage | 2026 | 每条轨迹对抽取出的 skill 行为约束的覆盖率，以及已覆盖约束上的 Pass / Fail 判定 | 可复用的 agent skill，作用于 SkillsBench 排行榜轨迹 | [→](../works/skill-coverage.md) |
| SkillCoach | 2026 | 自演化的、以 skill 为依据的 rubric，覆盖四个维度——skill 选取（对照金标准 skill 集的 F1）、skill 遵循、按先后依赖判定的组合、以及以 skill 为依据的反思——评分与外部验证器分开 | Agent 的 skill 使用；28 个任务族，由 SkillsBench 与 SkillLearnBench 筛得 | [→](../works/skillcoach.md) |
| SkillLearnBench | 2026 | 三个层次：任务通过率、生成 skill 的质量（功能覆盖、可执行性、安全性）、轨迹质量（要点召回、执行顺序、完整性） | 持续的 skill 学习；15 个子领域中的 20 个依赖 skill 的任务（100 个经校验实例） | [→](../works/skilllearnbench.md) |
| SkillMisevo-Bench | 2026 | 九项沿生命周期设闸的指标，把在线行为、演化产物的不安全性（内容不安全、不安全泛化、隐蔽性）与重置后的不安全检索及危害延续区分开 | 沙箱 agentic 操作下的持久 skill 库；四种 agent 框架 × 六种演化方法 | [→](../works/skillmisevo-bench.md) |
| RigorBench | 2026 | 从经插桩的轨迹算出的七根过程纪律支柱，合成加权 RigorScore；结果在同一批运行上单独评分 | AI 编码 agent；五个类别共 100 个任务，各 harness 之间基础模型固定不变 | [→](../works/rigorbench.md) |
| AISE-Bench | 2026 | 计划与标注计划之间的图编辑距离、参数准确率与执行成功率，与答案的正确性 / 完整性 / 忠实度 / F1-LM 分开报告 | 面向学术知识图谱 API（AMiner、Google Scholar）的学术信息检索 | [→](../works/aise-bench.md) |

## Open Questions

- **子目标指标对标注者的依赖。** 进展率依赖标注者对任务的分解方式。若 agent 通过另一种可行的分解完成任务，可能被"扣分"却并非表现更差。子目标类指标在不同标注方案下是否稳定？
- **自动化 trajectory 判分的可靠性。** 效用函数类指标依赖评审者（模型或人类）为 reasoning quality 与 evidence grounding 打分。LLM-judge 对 trajectory 的评审在可靠性上是否能对齐人类评审者？扩展到大规模又如何？
- **分解结果的合成方式。** 无论是基于子目标还是能力分解都会产出 per-piece 分数。如何在保留分解本身希望提供的诊断信号的前提下，将 per-piece 分数合成为一个 trajectory 总分？
- **不同设计线之间的一致性。** 基于子目标、分级子任务、能力分解、效用函数、诊断覆盖层都产出非 Pass@1 的 trajectory 信号。它们在共享任务上对模型的排名是否一致？
- **覆盖框架 vs. 任务套件。** AgentAtlas 与 Insights Generator 不新增任务，而是解读既有 benchmark。领域是否应标准化此类覆盖，使 trajectory 级信号能在原本不可比的 benchmark 之间可比？
- **确定性 vs. LLM 生成的 ground truth。** Traxgen 证明从结构化 workflow 规范出发的确定性 ground-truth 生成比基于 LLM 的生成快数万倍且与人工验证参考 100% 对齐。这是否会把未来 trajectory-evaluation 工作的合理 baseline 从"LLM 生成的 gold"移开？

## Related Works

- [SkillJuror](../works/skilljuror.md)
- [Skill Coverage](../works/skill-coverage.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [RigorBench](../works/rigorbench.md)
- [AISE-Bench](../works/aise-bench.md)
- [AstroVisBench](../works/astrovisbench.md)
- [Spec-o3](../works/spec-o3.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [DrafterBench](../works/drafterbench.md)
- [PEOA](../works/peoa.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [TempoBench](../works/tempobench.md)
- [TelemetrySuffBench](../works/telemetrysuffbench.md)
- [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md)
- [Long-Horizon Agent Trajectory Attribution](../works/long-horizon-agent-trajectory-attribution.md)
- [MiraMind](../works/miramind.md)
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md)
- [RACE-Bench](../works/race-bench.md)
- [The Replay Gap](../works/the-replay-gap.md)
- [AgentBoard](../works/agentboard.md)
- [T-Eval](../works/t-eval.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [Enconda-bench](../works/enconda-bench.md)
- [TRACE](../works/trace.md)
- [FinTrace](../works/fintrace.md)
- [AgentAtlas](../works/agentatlas.md)
- [Insights Generator](../works/insights-generator.md)
- [Traxgen](../works/traxgen.md)
- [AgentProcessBench](../works/agentprocessbench.md)
- [AgentLens](../works/agentlens.md)
- [TELBench](../works/telbench.md)
- [MATP](../works/matp.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [SysMoBench](../works/sysmobench.md)
- [Pseudo-Formalization](../works/pseudo-formalization.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [AgentRewardBench](../works/agentrewardbench.md)
- [Harness-Bench](../works/harness-bench.md)
- [SWE-chat](../works/swe-chat.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [SearchAuditor](../works/searchauditor.md)
- [TRAJDEBUG](../works/trajdebug.md)
- [EnvTrace](../works/envtrace.md)
- [Embodied Agent Interface](../works/embodied-agent-interface.md)
- [REFLECT / RoboFail](../works/robofail.md)
- [AHA](../works/aha.md)
- [RoboFAC](../works/robofac.md)
- [LabRobFail](../works/labrobfail.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
