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
| SysMoBench | 2025 | 为真实的并发与分布式系统——操作系统同步原语、Raft 实现、ZooKeeper 领导者选举——编写 TLA+ 形式化模型，粒度由任务固定。 | 11 个系统工件，源代码 175–5,360 行，覆盖 Rust、Go、C 与 Java；每个任务要求 TLA+ 模型及其 TLC 配置。 | 四项机器检查、逐级设卡的指标：SANY 语法、TLC 运行时、对照插桩执行轨迹的一致性、不变式模型检查；明确不用 LLM judge。 | [→](../works/sysmobench.md) |
| VCoT-Bench | 2026 | 补全经过验证的 Verus Rust 程序背后验证思维链中被刻意移除的块——引理、循环不变式、断言。 | 1,988 个补全任务，派生自 150 个已验证 Verus 程序，按移除比例、证明类型与位置分层。 | Verus 语法检查，加由协议引导的 LLM 判定与真值链的语义等价（与作者共识一致率 94%），合并为加权准确率。 | [→](../works/vcot-bench.md) |
| Long-Horizon-Terminal-Bench | 2026 | 长 horizon 终端工作流，包括软件工程与科学计算，另有实验复现、多模态分析与交互游戏。 | 46 个任务、九个类别，每个任务分解为细粒度的分级子任务。 | 稠密的分级子任务奖励，配可调通过阈值（最佳模型：阈值 0.95 下 pass@1 为 15.2%，阈值 1.0 下为 10.9%）。 | [→](../works/long-horizon-terminal-bench.md) |
| FrontierCode | 2026 | 在真实开源仓库中产出维护者愿意合并的 pull request——无配套论文的业界 benchmark。 | 由 20 余位资深开发者以每任务 40+ 小时撰写的维护者任务；任务数未公布。 | 以单元测试、评分标准与验证器的组合评判可合并性，覆盖正确性、测试质量、范围克制与风格；查阅含解来源的运行记零分。 | [→](../works/frontiercode.md) |
| SWE-Interact | 2026 | 完成需求由模拟用户逐步披露的软件工程任务。 | 多轮用户驱动会话，与同批任务的单轮基线成对比较。 | 交互协议下的任务成功率对比单轮（顶级模型约 50% vs. 约 25%）。 | [→](../works/swe-interact.md) |
| SWE-Together | 2026 | 在从真实会话重建的仓库级编码任务上与用户协作。 | 从 11,260 条录制会话整理出的 109 个任务，经保持原意的用户模拟器回放。 | 最终仓库正确性，加上所需的纠正反馈轮数。 | [→](../works/swe-together.md) |

## Related Works

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
