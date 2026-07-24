# Trajectory Evaluation

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

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
