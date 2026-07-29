# T-Eval (2023)

> [English](../../works/t-eval.md) | **简体中文**

## Overview

T-Eval 是一个细粒度的 tool-use benchmark，把 tool-use 评估拆解为 6 个能力子过程分别打分，而不是简化为一个端到端的成功率。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2312.14033>
- **Code:** <https://github.com/open-compass/T-Eval>

## Summary

T-Eval 论文指出，整体化的 tool-use 打分会把多种不同能力混在一起——一个 agent 可以看起来 "会用工具"，却在其中某个环节（例如 planning）上很弱。该 benchmark 将 tool-use 拆为 6 个子过程，并在孤立任务上分别评估，得到每个能力维度上的画像，同时保留与传统结果指标的可比性作为一致性检验。

## Tasks

23,305 个测试用例，源自 553 个 query–solution 标注对（平均每个 query 5.8 个工具调用步），覆盖 6 个领域（Research、Travel、Entertainment、Web、Life、Financials）的 15 个工具。各维度测试用例数：Instruct 2,660、Plan 553、Reason 6,426、Retrieve 6,426、Understand 6,753、Review 487。

## Domains

Tool-use 类任务。

## Evaluation

六个子过程各自在孤立任务上打分，并在两套并行协议——宽松的 “string” 格式与严格的 “JSON” 格式——下评估；最终 T-Eval 分数是六个维度的等权算术平均：

- **Instruct**（格式遵循）— 生成格式合法的工具调用得 0.5，加上 0.5 × 参数正确匹配的比例（上限 1.0）。
- **Plan**（动作序列生成）— 预测序列与 golden 序列用 Sentence-BERT 余弦相似度比较，经 Hopcroft–Karp 二分最大匹配（相似度阈值 ≈ 0.7）与最长递增子序列（保证顺序）后，以 F1 = 2pr/(p+r) 打分。
- **Reason**（下一步 thought 生成）— 预测 thought 与 golden thought 的 Sentence-BERT 余弦相似度。
- **Retrieve**（工具选择）— 对所选工具名做精确匹配（1/0）。
- **Understand**（参数生成）— 预测与 golden API 参数的 Sentence-BERT 相似度。
- **Review**（响应判定）— 将工具响应归入五类之一（Success、Internal Error、Input Error、Irrelevant Response、Unable to Accomplish），以精确匹配打分。

报告的 overall：GPT-4 ≈ 86.4、GPT-3.5 ≈ 84.0、最强开源模型 Qwen-72B ≈ 71.4，其中开源与 GPT-4 差距最大处在 Retrieve 与 Review。

## Typical Duration

按能力维度分别测试的短时交互。

## Main Contribution

将 tool-use 评估从单一端到端指标，重塑为按子过程的细粒度诊断评估，以支持对 agent 失败点的可解释定位。

## Key Design Ideas

- 将 tool-use 拆解为 6 个能力子过程。
- 在针对每个子过程的孤立任务上分别评估。
- 保留与整体结果指标的可比性。

## Strengths

- 诊断粒度高：能定位 tool-use 管线中哪个子过程导致失败。
- 与端到端评估互补，而非替代。
- 提供公开代码库。

## Limitations

- 范围限定于 tool-use，不评估多轮状态维护、长 horizon 规划或 embodied 交互。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在最终任务结果之下做了拆分，但沿的是任务子目标，而非 tool-use 子过程。
