# General Long-Horizon Agent Benchmarks

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
- **异步环境。** [Gaia2](../works/gaia2.md) 在事件驱动的环境中运行 1,120 个场景，这些环境按自己的时钟推进而非仅在 agent 行动时才变化，从而使时间意识成为一项被打分的能力：GPT-5（high）以 42.1% 的 pass@1 总分领先，但在 Time 划分上得分为 0.0，且每个受评模型在该划分上都低于 9 分。

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

## Open Questions

- **"长 horizon" 到底指什么？** 步数？wall-clock？独立 tool call？独立子决策？不同 benchmark 采用不同定义，跨 benchmark 比较受限。
- **最终奖励 vs. trajectory 指标。** 带密集子任务奖励的 benchmark 产出非 Pass@1 信号；仅有终态结果的 benchmark 则不产出。长 horizon 排行榜应如何权衡两者？
- **生态效度 vs. 可复现性。** 生态 grounding 的任务（Agents' Last Exam、Terminal-Bench Science）源于真实工作流，需付出评审成本；合成任务更易扩展。哪一种更适合作为主要评估面？
- **难度上限。** Frontier 模型在短 horizon 上迅速饱和。当前长 horizon benchmark 是否在下一代模型面前仍保留难度上限？

## Related Works

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

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
