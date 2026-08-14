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

## Related Works

- [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md)
- [LoopsBench](../works/loopsbench.md)
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md)
- [SWE-Bench ProMax](../works/swe-bench-promax.md)
- [RACE-Bench](../works/race-bench.md)
- [SWE-bench](../works/swe-bench.md)
- [SWE-chat](../works/swe-chat.md)
- [Enconda-bench](../works/enconda-bench.md)
- [AgentLens](../works/agentlens.md)
- [SysMoBench](../works/sysmobench.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [FrontierCode](../works/frontiercode.md)
- [SWE-Interact](../works/swe-interact.md)
- [SWE-Together](../works/swe-together.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [EngDesign](../works/engdesign.md)
- [RigorBench](../works/rigorbench.md)
