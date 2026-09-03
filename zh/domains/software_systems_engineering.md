# Software & Systems Engineering

> [English](../../domains/software_systems_engineering.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为工程的软件构建与验证：真实仓库上的代码生成、环境配置、形式化规约与验证。Web/UI agent 与 computer use 不属于软件工程。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| SWE-bench | 2023 | 通过编辑 12 个流行开源 Python 仓库之一的代码库来解决真实的 GitHub issue。 | 2,294 个 issue–pull-request 实例；模型对每个实例生成一个补丁。 | 由仓库自身测试套件裁定：应用补丁后所有 FAIL_TO_PASS 与所有 PASS_TO_PASS 测试都必须通过；无部分得分。 | [→](../works/swe-bench.md) |
| SWE-chat | 2026 | 真实实践中的软件工程：开源仓库上真实环境的人–agent 编码会话，覆盖代码理解、新建、git 操作与调试。 | 来自 200+ 个公开仓库的约 6,000 个记录会话，含 13,000+ 个 checkpoint 与行级的人类–agent 作者归属；观察性数据，无人工编写任务。 | 以 commit 为锚点的结果（agent 代码在用户 commit 中的存活）、对提交前后快照的 Semgrep 安全扫描、以及经人类 gold 标签验证的 LLM 标注。 | [→](../works/swe-chat.md) |
| Enconda-bench | 2025 | 诊断并修复注入到仓库安装文档中的错误，然后构建软件环境并运行其测试。 | 4,201 个含错 README 任务、共 9,471 个注入错误，覆盖 323 个固定 commit 的仓库，按难度 1–10 分层。 | Docker 执行的 Pass@1（环境可构建、测试可执行、正常退出），加诊断与修复的按能力 precision/recall；每个注入错误都经验证确实破坏安装。 | [→](../works/enconda-bench.md) |
| AgentLens | 2026 | 在真实开源 Spring Boot 项目上的交互式 Java 编码助手任务：单元测试与测试重构、遗留数据库逻辑迁移、API 文档与 DTO 清理。 | 16 个源自开发者访谈与生产使用的场景，各在宽松与轻度对抗两种用户 persona 下运行（每 agent 32 条轨迹）。 | 形式化验证——测试、仓库状态断言、构建执行、静态分析须全部通过——与五个 LLM-judge 维度合并为 Quality Index。 | [→](../works/agentlens.md) |
| SysMoBench | 2025 | 为真实的并发与分布式系统——操作系统同步原语、Raft 实现、ZooKeeper 领导者选举——编写 TLA+ 形式化模型，粒度由任务固定。 | 11 个系统产物，源代码 175–5,360 行，覆盖 Rust、Go、C 与 Java；每个任务要求 TLA+ 模型及其 TLC 配置。 | 四项机器检查、逐级设卡的指标：SANY 语法、TLC 运行时、对照插桩执行轨迹的一致性、不变式模型检查；明确不用 LLM judge。 | [→](../works/sysmobench.md) |
| VCoT-Bench | 2026 | 补全经过验证的 Verus Rust 程序背后验证思维链中被刻意移除的块——引理、循环不变式、断言。 | 1,988 个补全任务，派生自 150 个已验证 Verus 程序，按移除比例、证明类型与位置分层。 | Verus 语法检查，加由协议引导的 LLM 判定与真值链的语义等价（与作者共识一致率 94%），合并为加权准确率。 | [→](../works/vcot-bench.md) |
| Long-Horizon-Terminal-Bench | 2026 | 长 horizon 终端工作流，包括软件工程与科学计算，另有实验复现、多模态分析与交互游戏。 | 46 个任务、九个类别，每个任务分解为细粒度的分级子任务。 | 稠密的分级子任务奖励，配可调通过阈值（最佳模型：阈值 0.95 下 pass@1 为 15.2%，阈值 1.0 下为 10.9%）。 | [→](../works/long-horizon-terminal-bench.md) |
| FrontierCode | 2026 | 在真实开源仓库中产出维护者愿意合并的 pull request——无配套论文的业界 benchmark。 | 由 20 余位资深开发者以每任务 40+ 小时撰写的维护者任务；任务数未公布。 | 以单元测试、评分标准与验证器的组合评判可合并性，覆盖正确性、测试质量、范围克制与风格；查阅含解来源的运行记零分。 | [→](../works/frontiercode.md) |
| SWE-Interact | 2026 | 完成需求由模拟用户逐步披露的软件工程任务。 | 多轮用户驱动会话，与同批任务的单轮基线成对比较。 | 交互协议下的任务成功率对比单轮（顶级模型约 50% vs. 约 25%）。 | [→](../works/swe-interact.md) |
| SWE-Together | 2026 | 在从真实会话重建的仓库级编码任务上与用户协作。 | 从 11,260 条录制会话整理出的 109 个任务，经保持原意的用户模拟器回放。 | 最终仓库正确性，加上所需的纠正反馈轮数。 | [→](../works/swe-together.md) |
| AInsteinBench | 2025 | 维护生产级科学软件：解决六个广泛使用代码库中派生自维护者 PR 的任务。 | 经多阶段筛选与专家评审整理的仓库级 coding agent 任务。 | 可执行环境中的测试驱动验证，失败模式按科学意义归类。 | [→](../works/ainsteinbench.md) |
| SWE-Bench ProMax | 2026 | 在真实的多语言开源仓库（Python、Java、TypeScript、Go、C、C++、Rust）中进行大规模代码重构——跨多文件、协调一致、保持行为的改动。 | 170 个专家整理的真实 commit 重构实例，平均每个实例改动 11.4 个文件、261.6 行；issue 描述从零重写，测试套件经人工剔除过窄/过宽的测试。 | 基于执行的求解率，对照人工审阅的按实例测试套件；最佳受评模型达到 41.2%。 | [→](../works/swe-bench-promax.md) |
| Plan Compliance in Programming Agents | 2026 | 度量给定任务特定计划的 coding agent 在解决真实 GitHub issue 时是否真的遵循该计划，以及计划偏离与 issue 求解成功之间的关系。 | 四个 LLM 在 SWE-bench Verified（500 个实例）与 SWE-bench Pro（266 个 Python 实例）上、八种计划设定（移除、扩充、重排、提醒、无计划）下的 16,991 条 SWE-agent 轨迹。 | SWE-bench 式补丁验证（对照仓库测试套件的 issue 求解成功）在各计划设定间比较，并配计划遵循指标（Plan Phase Compliance、Plan Order Compliance、Plan Phase Fidelity）。 | [→](../works/from-plan-to-action.md) |
| RACE-Bench | 2026 | 仓库级特性新增——在真实开源代码库中实现一项新特性使相关测试通过——联合按补丁正确性与 agent 中间推理同开发者认可轨迹的契合度评估。 | 来自 12 个开源仓库的 528 个真实特性新增实例，每个配一套可执行的补丁验证 harness 与结构化参考推理（issue 理解、文件定位、实现任务、步骤分解）。 | 双轨：基于可执行测试的 Resolved Rate（三个 agent 从 29% 到 70%），加对照开发者认可参考轨迹的推理契合覆盖度。 | [→](../works/race-bench.md) |
| LoopsBench | 2026 | 持续的多步软件开发（"loop engineering"）——在长 horizon 编码工作上向前推进，同时避免对先前已完成单元的回归。 | 来自真实来源的 112 个任务，横跨 8 种编程语言与 9 个领域，每个是覆盖 5,300+ 个可单独测试开发单元的依赖 DAG，其前置边有源码证据支撑。 | 基于执行的评分，经一个 Docker 支撑、感知流程的运行时：沿就绪前沿释放测试，并将已完成节点保留为回归义务；验证器区分未完成/部分/完整解。最佳配置解出 25.0% 的任务。 | [→](../works/loopsbench.md) |
| SWE-RPG | 2026 | 仓库级 issue 解决——真实 Python 与 Java 项目中的缺陷修复与特性新增——沿完整轨迹（需求澄清 → 实现规划 → 代码生成 → 提交）诊断，而非仅按通过/失败评判。 | 来自 31 个 Python 与 Java 仓库的 163 个任务（113 个缺陷修复、50 个特性新增），每个配一套可执行的 fail-to-pass/pass-to-pass harness，加针对需求澄清与实现规划的、经验证的中间真值；三个 agent 跨六种 LLM 后端。 | 基于执行的求解率（补丁可应用、全部 fail-to-pass 通过、无 pass-to-pass 回归；平均 31.5%，最佳 49.7%），加 LLM-judge 的阶段归因与按阶段覆盖度，对照人类共识校准（92%/96%）。 | [→](../works/a-unified-issue-resolution-benchmark-for-requireme.md) |
| EngDesign | 2025 | 操作系统与计算机体系结构设计，交付物是一件真正能用的产物——设计须在给定约束下跑得通，而不是去对上某个参考答案。 | 九个工程方向共 101 项设计任务 / 473 个可评分条目，其中操作系统设计 8 项、计算机体系结构设计 5 项；默认单轮，另有一套依据仿真器反馈最多修改 10 轮的迭代协议。 | 逐任务的评估脚本执行所生成的设计，返回二元通过、0–100 的部分给分与日志；就整个基准而言，最佳模型首次尝试的通过率为 34.38%，十轮迭代后升至接近 60%。 | [→](../works/engdesign.md) |
| RigorBench | 2026 | 软件工作中的工程过程纪律——跨多文件实现功能、诊断并修复隐蔽缺陷、首次尝试失败后的恢复、面对不可能或含糊的规格时的弃权，以及带检查点的多步重构——衡量的是解法是怎么得到的，而不只是结果本身。 | 100 个任务，五个类别各 20 个，每个都附带一个 Node.js/Express、Python、Rust 或 Django 的起始仓库；四种 agentic harness 在同一个基础模型上共执行约 410 次任务。 | 基于轨迹为七根支柱——计划忠实度、验证覆盖率、恢复效率、弃权质量、原子转换完整性、测试断言密度、探索效率——打分，各子指标公式均已公开，再合成为综合的 RigorScore；构建与测试健康度在隔离的 Docker 环境中以程序方式检查，只有定性子指标交给 LLM 评审；结果分数在同一批运行上单独衡量。 | [→](../works/rigorbench.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的软件与系统工程子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`MAINT` 软件维护与演进（缺陷修复、issue 解决、重构） · `FEAT` 特性开发与仓库级实现 · `TEST` 软件测试与质量保证 · `FV` 形式化规约与程序验证 · `DIST` 分布式与并发系统 · `OS` 操作系统与系统编程 · `ARCH` 计算机体系结构与硬件设计 · `CFG` 构建、依赖与环境配置 · `REQ` 需求工程与意图澄清 · `PROC` 软件过程、规划与工程规范 · `HAI` 人机协作与开发者交互 · `SCISW` 科研软件工程 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

**两个分，不是一个。** 各列分成**覆盖面**——评测设置把什么纳入了考察——与**严谨度**——它报出来的东西有多可信。两者分开求和，因为它们方向相反：一个 benchmark 可以什么都考一点却什么都没验扎实，而一个刻意收窄的 benchmark 反而可能是本页最可信的。各行按 `Cov` 从高到低排，`Cov` 相同时比 `Rig`，仍相同则保持 Comparison 表原序。以覆盖面领先排序，是因为读者扫表时先问的就是这件事——*这个 benchmark 到底有没有把我关心的问题纳入考察*——`Rig` 随后回答它报出的东西能信到什么程度。

### 覆盖面（`Cov`，满分 7）

是非列，按稀缺程度排序——做到的工作越少排得越靠前，因此这一组的左侧就是该领域的薄弱处。几乎人人都满足的性质不设列：*是否编写并运行代码* 就是因此删去的。

- **Net** — 允许联网或实时外部检索；给定的固定语料库不算。
- **E2E** — 端到端研究：只给问题或目标，不提供源论文、参考实现或分步规范，整个研究过程由 agent 自己推进。
- **Cost** — 预算或资源成本被计入评分或明确定价，仅有步数上限不算。
- **MM** — 多模态内容是承重的，要么必须作为输入，要么作为产出物被打分。
- **Repro** — 以某项已发表结果为准，agent 需要复现或还原它。
- **Real** — 使用真实实验或观测数据，而非合成或仿真数据（数字孪生算仿真）。
- **Inter** — 交互式：agent 对环境、工具或仿真器多次动作，并根据反馈决定下一步。

### 严谨度（`Rig`，满分 13）

- **Human** — 有实测的人类专家基线或人类参考表现为整个量表定锚。若锚点只是一篇已发表结果或专家参考实现，而非实际跑出来的人类成绩，记 `◐`。
- **Rubric** — 专家撰写的 rubric 或官方评分标准，带具名维度或权重；连续型自动指标不算 rubric。
- **Contam** — 有刻意设计的机制让答案无法靠记忆得到：取材于训练截止之后、未发表或新撰写的题目、反事实改写、按需生成，或做过泄漏筛查。评测时把一篇已发表论文藏起来记 `◐`——藏起来并不能把它从预训练语料里去掉。
- **Verif** `0`–`3` — 这个分数要在多大程度上依赖对某个模型的信任。`0` 仅由 LLM judge 或 rubric 打分，且该判分器未经验证 · `1` judge/rubric 打分，且报告了与人类专家的一致性 · `2` 确定性校验与 judge/rubric 并用 · `3` 完全确定性——执行、测试、与参考解做数值比对、符号检查或证明内核，全程无 judge 介入。它取代了原先"有无确定性验证"的是非列：那一列 85% 的工作都满足，因而区分不出任何东西；做成阶梯后区分度很高。另有一个 `Judge` 列因与 `Verif` < 2 几乎等价而删去。
- **Scale** `0`–`3` — **本领域内**受评的条目数：`0` 少于 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 及以上 · `?` 原文未给出逐领域计数。它数的是条目而非工作量：30 个论文复现任务远比 3,000 道考试题费力，这一列看不见这一点。
- **Fail** `0`–`4` — 失败分析做到多深，因为"论文有失败分析"这句话的跨度太大——从一句话带过到专门设计的对照实验都算。`0` 除成绩外没有任何失败分析 · `1` 只有关于模型薄弱环节的叙述性评论，未给出类别 · `2` 有具名的错误类别或示例性案例分析，但没有计数或占比 · `3` 定量的失败刻画：带逐类计数或占比的分类体系，或能分离出特定失败条件的实测拆分 · `4` 在第 3 级之上，另有专门设计的对照实验或消融，用来检验失败*为何*发生。

### 怎么读这两个分

是非列按 `✔` 1 分、`◐` 0.5 分、`✘` 0 分、`?` 0 分计；分级列直接计其数值，`?` 计 0 分。`Domain` 不计分。

三点要留意。`?` 与 `✘` 的代价完全相同，所以两个分都是"该工作*可查证地*做到了多少"的下界，而不是对它的判决。两个分也都不是质量排名：`Cov` 高而 `Rig` 低，说的是这个 benchmark 什么都想够到却什么都没钉死；`Cov` 低而 `Rig` 高，说的是它把一件窄事量得很仔细——哪一种才是对的设计，完全取决于要回答什么问题。还有，`Cov` 描述的是*评测设置*而非科学本身：一份工作可以排在本表末尾，同时是它那个子领域最重要的论文。

跨领域套件的行按本领域的切片来写，与上面的 Comparison 表一致。
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SWE-chat | HAI, MAINT | ✔ | ◐ | ✔ | ✘ | ✘ | ✔ | ✔ | **4.5** | ✔ | ◐ | ◐ | 2 | 3 | 3 | **10** |
| Long-Horizon-Terminal-Bench | GEN | ? | ✘ | ◐ | ◐ | ◐ | ◐ | ✔ | **3** | ✘ | ✔ | ◐ | 3 | 1 | 3 | **8.5** |
| AgentLens | TEST, MAINT, HAI | ✔ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **2.5** | ✘ | ✔ | ◐ | 2 | 1 | 3 | **7.5** |
| Enconda-bench | CFG | ✔ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ◐ | ✘ | ✔ | 2 | 3 | 3 | **9.5** |
| LoopsBench | FEAT, PROC | ✘ | ✘ | ◐ | ✘ | ◐ | ✘ | ✔ | **2** | ◐ | ✘ | ✔ | 3 | 2 | 3 | **9.5** |
| SWE-Together | HAI | ✘ | ◐ | ◐ | ✘ | ✘ | ✘ | ✔ | **2** | ◐ | ✔ | ✘ | 2 | 2 | 2 | **7.5** |
| RigorBench | PROC, MAINT, TEST | ? | ✘ | ✔ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✔ | ◐ | 2 | 2 | 2 | **7.5** |
| SWE-Interact | HAI, REQ | ? | ◐ | ◐ | ✘ | ✘ | ✘ | ✔ | **2** | ◐ | ◐ | ✘ | 2 | 1 | 3 | **7** |
| FrontierCode | MAINT, TEST | ✔ | ✘ | ? | ? | ✘ | ✘ | ✔ | **2** | ◐ | ✔ | ✔ | 2 | ? | 0 | **4.5** |
| SWE-Bench ProMax | MAINT | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✔ | 3 | 2 | 3 | **9.5** |
| SWE-RPG | MAINT, FEAT, REQ | ? | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✔ | ◐ | 2 | 2 | 3 | **9** |
| EngDesign | OS, ARCH | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✔ | ◐ | 3 | 1 | 3 | **8.5** |
| RACE-Bench | FEAT | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ◐ | ✘ | 2 | 2 | 3 | **8** |
| Plan Compliance in Programming Agents | MAINT, PROC | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ◐ | 3 | 2 | 4 | **10** |
| SysMoBench | FV, DIST, OS | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| AInsteinBench | SCISW, MAINT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | 2 | 2 | **7.5** |
| SWE-bench | MAINT | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ◐ | ✘ | ◐ | 3 | 3 | 3 | **10** |
| VCoT-Bench | FV | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 2 | 3 | 3 | **8.5** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note: 几乎所有未知都集中在两列。`Net` 在 47 行中有 35 行为 `?`，这也正是它排在覆盖面一组最前的原因——本领域几乎没有工作被明确记载允许实时检索，而大多数干脆不提；为核这一列，其中十一篇的全文都读过，没有一篇给出说法。`Scale` 有 12 行为 `?`，无一例外都是跨领域套件：给了任务总数，却不给逐领域拆分。两列都如实记录这种沉默，而不靠推断把它填掉；而在两列上，沉默都实实在在地扣掉了这些工作的分数。另有两格仍为 `?`：SciCode 与 Terminal-Bench Science 的 `Real`。

## Related Works

- [SWE-Bench ProMax](../works/swe-bench-promax.md)
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md)
- [LoopsBench](../works/loopsbench.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [AgentLens](../works/agentlens.md)
- [SWE-Interact](../works/swe-interact.md)
- [SWE-Together](../works/swe-together.md)
- [RigorBench](../works/rigorbench.md)
- [FrontierCode](../works/frontiercode.md)
- [SWE-chat](../works/swe-chat.md)
- [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md)
- [RACE-Bench](../works/race-bench.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [Enconda-bench](../works/enconda-bench.md)
- [SysMoBench](../works/sysmobench.md)
- [EngDesign](../works/engdesign.md)
- [SWE-bench](../works/swe-bench.md)
