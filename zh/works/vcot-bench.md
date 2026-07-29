# VCoT-Bench (2026)

> [English](../../works/vcot-bench.md) | **简体中文**

## Overview

VCoT-Bench 是一个 benchmark，用于评估 LLM 是否理解 Rust 程序验证背后的验证思维链（Verification Chain-of-Thought，VCoT），而不只是其通过或失败的结果。它包含 1,988 个 VCoT 补全任务，源自 150 个已验证的 Verus 程序，并沿三个正交维度分层：移除比例、证明类型与证明位置。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.18334>
- **Venue:** ICML 2026

## Summary

VCoT-Bench 针对的局限是：现有评估把 Rust 验证当作黑箱，仅以证明提示通过或失败的二元结果来衡量模型，从而掩盖了模型是否真正理解证明所需的逻辑推导。作者提出 VCoT-Lift 框架，将底层 Z3 求解器推理提升为高层、人类可读的 Verus 证明步骤，并据此构建 VCoT-Bench-Org 这一 ground truth 语料，其证明行数相较 Verus-Bench 平均增加 6.5×。对十个前沿模型的评估揭示出严重的脆弱性：最强的模型 Claude Sonnet 4.5 的准确率从 10% 块移除时的 71.58% 降至全部移除时的 17.22%。

## Tasks

1,988 个 VCoT 补全任务，通过在 VCoT-Bench-Org 中以语义块为粒度挖出结构化的证明洞而构造——lemma 块（每个独立的 lemma function）、invariant 块（同一循环的全部 loop invariant）、assertion 块（两行可执行代码之间的全部 assertion）。三个子 benchmark 对整个套件进行分层：VCoT-Bench-Ratio，1,159 个任务，从程序的 N 个块中随机移除 1 到 N 个；VCoT-Bench-Type，439 个任务，移除某一类型的全部块；VCoT-Bench-Loc，390 个任务，从链条的 Front（前 33%）、Middle（33%–66%）或 End（后 33%）移除块。源程序为 Verus-Bench 的 150 个已验证 Verus 程序，取自 MBPP-DFY-153、CloverBench、Diffy 以及 Verus 库。

## Domains

Rust 程序在 Verus 中的形式化验证，证明由 Z3 SMT 求解器完成。

## Evaluation

- **Syntactic Accuracy (SynAcc).** 补全后的程序能否通过解析，以仅语法模式（`--no-verify`）调用 Verus 来检查。
- **Semantic Accuracy (SemAcc).** 补全的步骤是否与作为 ground truth 的 VCoT 语义等价，由一个专门的 LLM judge 依据带有精选示例的协议判定；在 100 个分层抽样任务上的元评估显示，该 judge 与作者共识的一致率为 94%。
- **Overall Accuracy (Acc).** 一个强调语义甚于语法的加权分数：每个预测被归入语法语义均正确、仅语义正确、仅语法正确或均不正确四档，分别加权 1、0.5、0.25 与 0，再在全部样例上取平均并以百分比报告。
- **Reported.** 在 10% 块移除下，准确率从 71.58%（Claude Sonnet 4.5）跨至 32.89%（gpt-oss）；在 100% 移除下，Claude Sonnet 4.5 降至 17.22%，Qwen 3 think 降至 0.66%。Claude Sonnet 4.5 在 loop invariant 上为 68.71%，在 assertion 上为 39.55%，并从 Front 块的 69.04% 降至 Middle 块的 46.35%。未给出人类 baseline。

## Typical Duration

零样本补全，所有模型均以默认设置运行。未说明：没有给出任何单任务的 wall-clock、步数或 token 预算——论文只说明输出长度上限对所有程序都设置得足够高。

## Main Contribution

一个包含 1,988 个 Verification Chain-of-Thought 补全任务的 benchmark，连同将底层 Z3 求解器推理提升为人类可读 Verus 证明步骤以提供其 ground truth 的 VCoT-Lift 框架，把 Rust 验证的评估从通过或失败的二元结果推进到对验证推理的细粒度分析。

## Key Design Ideas

- 求解器导出的参考链：Z3 证明被提升为 Verus 层面的验证步骤，因而 ground truth 遵循的是 prover 自身的推理，而非人类选择的表述方式。
- 一套 Z3 规则层级，将全部 36 条证明规则划分为 8 条高层、12 条中层与 16 条低层，引导 transformer 关注语义上更有信息量的步骤。
- 一个 perform-all-check-partial 循环：transformer 面向整个 Z3 证明，而五个专门的 checker agent 只校验高层规则类别，并返回粗粒度的完整或不完整二元信号。
- 一个剪枝与修复的收尾阶段，剔除平凡与冗余步骤，再由 Verus 验证器编译并检查程序，将错误信息回馈直至验证通过。

## Strengths

- 从求解器自身的证明导出参考链，使 ground truth 锚定于验证真正需要的内容，而非标注者对哪些步骤重要的判断。
- 将语法准确率与语义准确率分开，暴露出单一通过或失败分数会掩盖的模型间失衡。
- 沿移除比例、证明类型与证明位置对同一语料分层，从而定位推理在何处退化，而不只是退化了多少。

## Limitations

- Repository note: 作为 ground truth 的链条并非直接从求解器读出——由 LLM 提升 Z3 证明、由 LLM checker agent 判定其完整性、由 LLM pruner 进行剪裁，而 Verus 验证器只把关最终程序能否编译并通过验证；因此参考链的完整性依赖于 LLM 判断，而非机器可校验的判据。
- Repository note: Semantic Accuracy 由 LLM judge 给出，其 94% 的一致率是在 100 个分层抽样任务上相对作者共识测得的，因此语义分数继承了该 judge 的残余误差，且其验证并不独立于作者。

## Related Works

- [TRACE](./trace.md) — 同样评估中间推理链而不只看最终结果，但其对象是 deep research trajectory，按认知质量维度评判，而非从求解器提升而来的证明步骤。
- [T-Eval](./t-eval.md) — 同样把评估分解到 end-task 成功之下，但沿 tool-use 能力子过程展开，而非单条证明链内缺失步骤的类型与位置。
- [AgentBoard](./agentboard.md) — 同样以中间步骤给出部分得分而非二元成功，但其依据是人工标注的任务 subgoal，而非从求解器自身证明导出的步骤。
