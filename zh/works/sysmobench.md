# SysMoBench (2025)

> [English](../../works/sysmobench.md) | **简体中文**

## Overview

SysMoBench 是一个 benchmark，评估 AI 用 TLA+ 为大型复杂计算机系统编写形式化模型的能力。它覆盖 11 个并发与分布式系统构件，并用四个可自动检查的指标为生成的模型打分，而不依赖人工或 LLM 判断。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.23130>
- **Project:** <https://sysmobench.com>
- **Code:** <https://github.com/specula-org/SysMoBench>
- **Venue:** ICLR 2026

## Summary

SysMoBench 针对这样一个局限：已有的 AI 规约 benchmark 面向的是小规模代码片段——函数级前置与后置条件，或逻辑谜题——而非完整系统，而完整系统需要把复杂的行为性质抽象为形式化模型。作者在真实世界的并发与分布式系统构件上构建 benchmark，以 TLA+ 作为规约语言，并将质量指标自动化，使评分环路中不存在人工或 LLM judge。在 11 个系统构件上，报告结果显示 agent 能较好地建模最简单的构件，而 Etcd Raft 这类 Raft 实现已超出其能力。

## Tasks

11 个系统构件，每个构件对应一项任务：生成 TLA+ 系统模型及其 TLC 配置。其中 4 个是来自 Asterinas 操作系统的并发原语（Spinlock、Mutex、Rwmutex、Ringbuffer，均为 Rust），7 个是分布式系统（Go 实现的 Etcd Raft、C 实现的 Redis Raft、Rust 实现的 Xline CURP、Java 实现的 ZooKeeper 选主，以及 PGo 合成的 dqueue、locksvc 与 raftkvs，均为 Go），源码规模从 175 行到 5,360 行。每项任务都列出必须建模的核心 action 与应当排除的实现细节，因此粒度由任务固定，而非由 agent 自行选择。

## Domains

并发与分布式系统的形式化规约：操作系统同步原语、共识实现、复制、选主与分布式数据结构。

## Evaluation

四个指标，按固定顺序应用，每个阶段都是下一阶段的门槛：

- **Syntax correctness.** TLA+ SANY Syntactic Analyzer 检查整个模型，另有一轮按 action 的检查把每个 action 单独封装以给出部分得分；两者权重相等，因此整体检查未通过但每个 action 检查均通过的模型得 50%。只有得分为 100% 的模型才会进入后续指标的评估。
- **Runtime correctness.** TLC 在关闭不变式检查的情况下执行有界模型检查与模拟，得分为未报运行时错误的被覆盖 action 数除以模型中 action 的总数。只有不含运行时错误的模型才会被评估 conformance 与 invariant correctness。
- **Conformance to system implementation.** Trace validation 把从插桩系统代码中收集的执行 trace 在模型的状态空间上重放，得分为被覆盖且无 conformance 错误的插桩代码 action 比例。
- **Invariant correctness.** 每条系统特定的安全性与活性不变式都在独立的 TLC 运行中做模型检查，得分为在所探索状态空间上成立的不变式比例。
- **Reported (Table 3).** 在 Asterinas Spinlock 上，basic modeling agent 下所有 LLM 的 syntax 与 runtime 均达到 100.00%，其中 Claude-Sonnet-4 的 conformance 为 100.00%，GPT-5、Gemini-2.5-Pro 与 DeepSeek-R1 为 80.00%。在 Etcd Raft 上，该 agent 下只有 Claude-Sonnet-4 通过 syntax 门槛，随后达到 25.00% runtime、7.69% conformance 与 69.23% invariant correctness；code translation agent 配合 Claude-Sonnet-4 则达到 66.67%、15.38% 与 92.31%。在不变式中，8.3% 的安全性性质与 41.9% 的活性性质被违反。

## Typical Duration

每个 agent 在每个构件上运行五次，取最好的输出模型进行评估；当生成的模型无法编译或出现运行时错误时，最多允许三轮反馈循环迭代。未说明：论文没有给出每项任务的 wall-clock、步数或 token 预算。

## Main Contribution

一个用于评估 AI 以 TLA+ 对真实世界并发与分布式系统进行形式化建模的 benchmark，其四项质量指标——syntax、runtime、conformance 与 invariant correctness——均可自动检查，无需人工或 LLM 判断。

## Key Design Ideas

- 以真实系统构件作为任务来源——取自 Etcd、Redis、Xline、ZooKeeper 与 Asterinas OS 的生产代码，而非合成程序或逻辑谜题。
- 门控式指标链条：syntax 门控 runtime，runtime 同时门控 conformance 与 invariant correctness，因此无法执行的模型不会在行为层面被打分。
- 每个指标内部都设有部分得分并归一化为百分比，其中按 action 的语法分析可区分整体畸形的模型与只含单个错误 action 的模型。
- Conformance 通过对插桩系统代码日志的 trace validation 来度量，使得分锚定于实现本身，而非人工编写的参考规约。

## Strengths

- 机器检查的指标使评分可复现且不依赖任何 judge 模型，作者在发现 LLM-as-a-judge 不可靠且难以解释后做出这一选择。
- 门控顺序给出的是诊断性画像而非单一分数，将语法层面的能力与对系统行为进行推理的能力区分开。
- 将 conformance 锚定在真实实现的执行 trace 上，避免了与参考规约的比对，而真实世界系统很少有这类规约。

## Limitations

- Repository note: 11 个构件是相当小的任务池，其中 3 个是 PGo 合成而非人工编写的系统代码——论文报告 agent 在这些构件上同样表现不佳，因此部分测得的难度反映的是机器生成代码的风格，而非系统本身的复杂度。
- Repository note: 评分环节排除了 LLM-as-a-judge，但 LLM 仍存在于流水线内部——在 trace validation 中把模型元素映射到系统日志元素，以及将不变式模板具体化——因此这些指标并非完全不含 LLM；作者在 11 个系统中的 2 个上用 gold model 对此做了检验。

## Related Works

- [TRACE](./trace.md) — 同样给出多维质量画像而非单一通过/失败，但它在 deep research trajectory 上综合准确性、效率与推理质量，而非对生成的形式化模型给出检查器判定。
- [Traxgen](./traxgen.md) — 同样把 LLM 移出评估环路，但发生在 ground-truth 生成环节而非评分环节，而 SysMoBench 通过让每个指标都可机器检查来封住评分环节。
- [Enconda-bench](./enconda-bench.md) — 同样把一项任务分解为四个分级阶段，但沿的是 planning、diagnosis、repair 与 execution 这些 agent 子过程，而非所产出制品的门控式正确性性质。
