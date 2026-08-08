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
- **能力分解（capability-decomposed）。** 将某种复杂能力拆解为若干子过程，并在孤立任务上分别打分。[T-Eval](../works/t-eval.md) 将 tool use 拆为 6 个子过程；[Enconda-bench](../works/enconda-bench.md) 将环境配置拆为 planning / diagnosis / repair / execution 四个子过程。
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

## Open Questions

- **子目标指标对标注者的依赖。** 进展率依赖标注者对任务的分解方式。若 agent 通过另一种可行的分解完成任务，可能被"扣分"却并非表现更差。子目标类指标在不同标注方案下是否稳定？
- **自动化 trajectory 判分的可靠性。** 效用函数类指标依赖评审者（模型或人类）为 reasoning quality 与 evidence grounding 打分。LLM-judge 对 trajectory 的评审在可靠性上是否能对齐人类评审者？扩展到大规模又如何？
- **分解结果的合成方式。** 无论是基于子目标还是能力分解都会产出 per-piece 分数。如何在保留分解本身希望提供的诊断信号的前提下，将 per-piece 分数合成为一个 trajectory 总分？
- **不同设计线之间的一致性。** 基于子目标、分级子任务、能力分解、效用函数、诊断覆盖层都产出非 Pass@1 的 trajectory 信号。它们在共享任务上对模型的排名是否一致？
- **覆盖框架 vs. 任务套件。** AgentAtlas 与 Insights Generator 不新增任务，而是解读既有 benchmark。领域是否应标准化此类覆盖，使 trajectory 级信号能在原本不可比的 benchmark 之间可比？
- **确定性 vs. LLM 生成的 ground truth。** Traxgen 证明从结构化 workflow 规范出发的确定性 ground-truth 生成比基于 LLM 的生成快数万倍且与人工验证参考 100% 对齐。这是否会把未来 trajectory-evaluation 工作的合理 baseline 从"LLM 生成的 gold"移开？

## Related Works

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

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
