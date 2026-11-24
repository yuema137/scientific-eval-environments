# ORBIT-Q (2026)

> [English](../../works/orbit-q.md) | **简体中文**

> **首次公开：** 2026-07-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.03105)

## Overview

ORBIT-Q 在研究级的量子编程任务上评估 coding agent。在这里，脚本能跑起来还不够：结果必须在物理上正确，必须用上指定框架原生的、可微分的功能，运行速度也要够快。它沿两条轴分别控制变量：一条轴固定框架（TensorCircuit-NG），更换 agent-模型组合；另一条轴固定 agent（Codex 配 GPT-5.5），更换量子计算框架。一个解只有同时通过功能测试、静态 policy 检查、LLM 源码审计和专家审查，才算数。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** [ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming](https://arxiv.org/abs/2607.03105)，Shi-Xin Zhang 与 Yu-Qin Chen，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2607.03105v1>
- **Code:** <https://github.com/sxzgroup/ORBIT-Q>（Apache-2.0，基于 Harbor）
- **Venue:** arXiv 预印本（quant-ph），2026 年

## Summary

12 个任务本身与框架无关，运行时通过追加框架 prompt、选择执行镜像和套用 verifier policy，变成针对某个框架的具体任务。Agent 有 30 分钟来写出 `run_solution(config)` 的实现。之后 verifier 先跑数值测试；如果解超过 200 行非空、非注释的 Python 代码，导入了禁用的库，或者篡改了测试，就直接拒绝；接着让 GPT-5.5 审计源码，看有没有绕开框架的做法（例如手写一个 NumPy/JAX 模拟器）；拿不准的情况交给专家判断。通过的解再与专家写的 TensorCircuit-NG 参考实现比较运行时间。在 TensorCircuit-NG 上，Codex 配 GPT-5.5 通过了 12 个任务中的 10 个，几何平均运行时间约为专家参考的 2.2 倍；没有任何配置能在通过率和运行时间上同时达到参考水平。

## Tasks

12 个任务提炼自变分和可微分量子工作流中的研究场景。论文点名的例子有：MPS 输入加变分优化（Task 1）、带成功率跟踪的后选择冷却（Task 3）、可训练的 Kraus 信道校准（Task 4）、非幺正的虚时演化（Task 5）、基于测量反馈的基态优化（Task 7）、从 7 × 7 二维电路中采样（Task 8）、512 量子比特浅层电路中的局域可观测量优化（Task 9），以及带弦序验证的 spin-1 Haldane 链态制备（Task 11）。任务打包成容器化的 Harbor task。

比较的框架有 TensorCircuit-NG（TC）、PennyLane、TorchQuantum 和 MindQuantum。Qiskit、Cirq 和 TensorFlow Quantum 被排除在外，因为它们的标准工作流缺少这些任务所需的端到端自动微分。

## Domains

量子物理与量子计算：量子电路模拟、变分算法、开放系统（Kraus 信道）建模、张量网络态输入，以及多体基态和态制备问题。

## Evaluation

- **第一层，功能验证：** 对照任务 evaluator 检查数值正确性，同时做静态 policy 检查（行数上限、必须导入和禁止导入的框架、是否操纵测试或 reward）。各任务的数值容差为 TODO(reference)。
- **第二层，LLM 语义审计：** GPT-5.5 阅读源码，返回 `uses_required_framework`、`raw_numpy_jax_quantum_simulator_bypass` 等结构化字段，检查框架是否真正被使用，以及解是否忠实于题目要求。
- **第三层，专家审查：** 处理框架使用是否合规还拿不准的情况。
- **产物运行时间：** 提交解的运行时间除以同一任务上专家 TC 参考的运行时间；几何平均只在通过且计了时的任务上计算。`run_solution(config)` 必须在 300 s 内完成；超过 180 s 开始扣运行时间分，到 300 s 时为零。
- **框架轴（Codex，GPT-5.5）：** TC 10/12，PennyLane 8/12，TorchQuantum 4/12，MindQuantum 4/12。几何平均慢速倍数从约 2.2 倍（TC）到约 10.1 倍（MindQuantum）；个别任务超过 40 倍。
- **Agent 轴（TC）：** Codex GPT-5.5 10/12，Claude Code 配 Opus-4.8 9/12，Sonnet-4.6 7/12，GLM-5.2 6/12。
- **失败归因（TC 上的 agent 轴）：** GPT-5.5 的失败是 1 次缺少产物、1 次绕开框架；Opus-4.8 是 1 次超时/内存溢出和 2 次安全拒答；GLM-5.2 是 3 次缺少产物、1 次运行时/API 异常和 2 次与题目不符；Sonnet-4.6 是 2 次缺少产物、1 次运行时/API 异常、1 次绕开框架和 1 次与题目不符。
- **Agent 侧资源（Table S2）：** 在 TC 上，12 个任务的总 token 数从 12,203,758（Opus-4.8）到 21,268,795（Sonnet-4.6），每次通过的成本从 $1.80（GPT-5.5）到 $2.16（GLM-5.2）。在 Codex GPT-5.5 下跨框架比较，每次通过的成本从 $1.80（TC）升到 $7.26（MindQuantum）。加入一份 TC 专用的性能检查清单 prompt 后，仍是 10/12 通过、约 2.2 倍慢速，但 token 从 14,241,691 降到 8,205,577，成本从 $17.99 降到 $13.29。Agent 侧成本不含 verifier 审计的开销。

## Typical Duration

每个任务给 agent 30 分钟求解（1800 s），verifier 时间 1200 s，提交的解最多运行 300 s。12 个任务的 agent 总墙钟时间从约 1.5 小时（GPT-5.5 加检查清单）到约 3.8 小时（GLM-5.2、Sonnet-4.6）不等。论文没有说明每个配置跑了几次。

## Main Contribution

一个双轴设计，在科学量子编程中把 agent 能力和框架易用性分开衡量；评分用多层 verifier，会拒绝数值正确但绕开了指定框架的代码，并以专家参考实现为基准测量运行时间。

## Key Design Ideas

- 任务描述本身与框架无关，到运行时才通过 prompt、镜像和 verifier policy 绑定到具体框架，所以同一任务可以跨框架比较。
- 一个解要被认定有效，必须同时通过功能验证、静态 policy、语义审计和人工审查。
- 效率以专家 TC 参考为基准报告，而不只是通过/不通过。
- 每个配置都同时报告 agent 侧的 token、墙钟时间、成本以及产物运行时间。

## Strengths

- 失败归因区分了缺少产物、绕开框架、与题目不符、超时和安全拒答，而不是只给一个失败总数。
- 框架轴固定了 agent，所以框架之间的差异反映的是同一个 agent 使用时各框架的易用性。
- 代码和任务已公开。

## Limitations

- 作者指出，语义审计依赖 GPT-5.5，拿不准的情况还要靠人工裁定。
- 框架比较衡量的是经由 agent 使用时的易用性和性能，而不是各框架下专家能写出的最佳实现；专家参考只有 TC 一个。
- 12 个任务是有限的样本。
- 作者是被评估框架之一 TensorCircuit-NG 的开发者，并已将此声明为利益冲突。
- 有些失败反映的是部署中 agent 的安全分类器，而不是模型能力。
- Repository note: 每个配置只报告了一组 12 个任务的结果；论文没有说明是否重复运行，因此没有报告运行间方差。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — 同样在容器化的科学计算任务上用程序化验证评估 agent，但覆盖多个自然科学领域，而不是单一的编程方向。
- [ScienceAgentBench](./scienceagentbench.md) — 同样通过执行来评判 agent 写的科学代码，但没有框架合规审计，也没有框架轴。
