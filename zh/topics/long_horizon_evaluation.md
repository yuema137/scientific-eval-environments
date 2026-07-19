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
- **有界预算下的迭代优化。** [Frontier-Eng](../works/frontier-eng.md) 把真实工程任务处理为面向工业级仿真器的 propose-execute-evaluate 循环——horizon 由固定的交互预算界定，而不是固定步数。

## Comparison

| Benchmark | Year | Horizon 信号 | 环境 | Card |
|---|---|---|---|---|
| Agents' Last Exam | 2026 | ~1,000+ 真实职业任务 | 职业分类任务 | [→](../works/agents-last-exam.md) |
| Long-Horizon-Terminal-Bench | 2026 | 46 任务；数百步；密集分级奖励 | Terminal (Docker) | [→](../works/long-horizon-terminal-bench.md) |
| Terminal-Bench Science | 2026 | 数分钟至数小时的科学工作流 | Container（pytest 验证） | [→](../works/terminal-bench-science.md) |
| UniClawBench | 2026 | 400 多轮 checkpointed 任务 | 实时 Docker + 闭环模拟 | [→](../works/uniclawbench.md) |
| TRACE | 2026 | Deep-research 多步 trajectory | Deep research | [→](../works/trace.md) |
| FinTrace | 2026 | 800 条长 horizon 金融 trajectory | 金融 tool use | [→](../works/fintrace.md) |
| Frontier-Eng | 2026 | 47 任务；迭代式 propose-execute-evaluate；horizon = 固定交互预算 | 工程（工业级仿真器） | [→](../works/frontier-eng.md) |

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
- [Frontier-Eng](../works/frontier-eng.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
