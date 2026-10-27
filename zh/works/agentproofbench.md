# AgentProofBench (2026)

> [English](../../works/agentproofbench.md) | **简体中文**

> **首次公开：** 2026-10-25 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.34634)

## Overview

AgentProofBench 评测 Web agent 的可复用 verifier。模型先写出一个验收程序，之后程序被冻结，根据任务前后的状态判断任务是否完成。基准回答两个问题：同一条指令在不同初始状态下的要求会变，这个程序还能不能判对？让 agent 依据程序的判定决定是否交付，最终交付结果会不会更好？

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — 评测对象是通用 Web 服务 agent 的 verifier，不涉及科学研究活动。

## Links

- **Paper:** [AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634)
- **Full text:** <https://arxiv.org/html/2610.34634v1>
- **Venue:** arXiv 预印本（2026）

## Summary

公开指令保持不变，但它具体要求哪些实体、数值或集合，可能取决于初始状态。只看指令写出来的检查程序，可能会把错误结果判为通过。在需求层面，每个冻结程序都要在三种初始条件产生的终止状态上运行。Source 是原始状态；Background 改动与任务无关的数据；Related 改动任务所需的实体绑定、初始值、集合或保留条件。论文把复用原程序和针对新状态重建程序的结果相比较。在策略层面，四种交付策略都从同一个保存的起点分出来，看依据 verifier 把关后，正确交付是否发生变化。

## Tasks

97 个任务，分属 79 个任务族，覆盖 Linear、Slack、Box 和 Calendar 四个 Web 服务，运行环境是 Agent-Diff 的企业服务复制环境。配对复用实验从 48 个任务族各取一个任务（Linear 18 个、Slack 10 个、Box 19 个、Calendar 1 个），共 576 个冻结程序和 558 个终止状态（有效 270 个，失败 288 个）。自然验收面板有 556 个状态（成功 452 个，失败 104 个）。执行实验有来自 22 个任务族的 44 条轨迹、88 个保存起点和 352 个策略结果。经检查后，有三个任务不计入显式验收视图。

## Domains

N/A — 任务运行在通用 Web 服务上，不属于科学或工程领域。

## Evaluation

- 程序实现 `verify(task, before, after)`，返回 Pass、Fail 或 Unknown。每次都在新的只读沙箱里运行，限制为一个 CPU、1 GB 内存、60 秒、80 次业务操作，并且不能调用模型。Unknown 和 Error 不得分。
- 指标包括有效状态与失败状态上的 balanced accuracy（BA），以及完整面板正确率。decision-replay witness 会在条件改变后重放一个先前有效的决策；面板和 witness 都判对才算 joint pass。
- 复用：原程序在 Related 状态上的 BA 为 93.23%（Flash）和 90.36%（Pro）。用 10,000 次按任务族的 bootstrap 重采样估计，复用减重建的 BA 区间为 [−5.47, 1.57] 和 [−10.16, 0.00] 个百分点。joint pass 数量：Flash 复用 82/96、重建 82/96；Pro 复用 79/96、重建 86/96。
- 程序与在线判定对比：在自然面板上，十二次调用构建的程序 BA 为 92.1%，十二次调用的新鲜在线判定为 99.0%。在 135 个状态的集合对比中，按其中 99 个失败状态计算，误接受率分别为 3.5% 和 31.7%。
- 执行：Related 面板全部判对的 33 个分配中，有 32 个在两个起点上都正确交付；面板有错误的 11 个分配中，只有 1 个做到。在检查点上，正确交付数分别是：中性继续 20/22 和 22/22，程序把关 17/22 和 16/22，在线把关 20/22 和 21/22。
- GPT-6 Astra 审核了参考标签，在 192 个有定论的标签中与 191 个一致（κ = 0.989）。

## Typical Duration

每次 verifier 判定最多 60 秒。程序构建成本中位数为 0.0173 美元（Flash）和 0.0765 美元（Pro）。与每次重新在线判定相比，中位回本次数分别为 12 次和 10 次。agent 完成任务的实际耗时未报告。

## Main Contribution

一个基准：在初始状态改变任务要求时检验冻结的 Web agent verifier，并从相同的保存起点出发，把 verifier 是否判对和最终交付结果联系起来。

## Key Design Ideas

- 程序只生成一次就冻结，再在同样的变化状态上比较复用与重建。
- 把任务所需绑定的变化和无关背景数据的变化分开。
- 所有策略都从同一个保存起点分支，起点包含原始状态、当前状态和交互历史。
- 以中性继续作为基线，衡量验证把关额外带来了什么。

## Strengths

- 复用与重建做配对比较，并给出按任务族的 bootstrap 区间。
- verifier 的判定与下游交付结果挂钩，不只看面板准确率。
- 报告了程序构建成本和在线判定成本。

## Limitations

- 生成、判定和执行结果只用了 DeepSeek Flash 和 Pro 两个模型，并关闭了 thinking。
- 面板正确率与交付结果之间的关联属于探索性结论，只基于 22 个任务族的 44 个分配。
- 把关结果只适用于论文测试的那条通用反馈消息。
- 参考规则的开发用到了 LLM，标签审核也由 LLM 完成；论文没有报告人工标注。
- Repository note: 论文说明其原创代码和标注采用 MIT 许可，但 arXiv 页面和 v1 全文都没有给出代码或数据的发布链接，2026-10-27 的网络搜索也没有找到。

## Related Works

- [AgentRewardBench](./agentrewardbench.md) — 将 Web agent 的自动 evaluator 与专家标签进行比较。
