# T-Eval (2023)

## Overview

T-Eval 是一个细粒度的 tool-use benchmark，把 tool-use 评估拆解为 6 个能力子过程分别打分，而不是简化为一个端到端的成功率。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- Skill Hierarchy *(topic page pending)*

## Links

- **Paper:** <https://arxiv.org/abs/2312.14033>
- **Code:** <https://github.com/open-compass/T-Eval>

## Summary

T-Eval 论文指出，整体化的 tool-use 打分会把多种不同能力混在一起——一个 agent 可以看起来 "会用工具"，却在其中某个环节（例如 planning）上很弱。该 benchmark 将 tool-use 拆为 6 个子过程，并在孤立任务上分别评估，得到每个能力维度上的画像，同时保留与传统结果指标的可比性作为一致性检验。

## Tasks

TODO(reference)：论文摘要未给出精确任务数，需比对论文正文再补上。

## Domains

Tool-use 类任务。

## Evaluation

按 6 个能力维度进行分步打分：

1. Instruction following（指令遵循）
2. Planning（规划）
3. Reasoning（推理）
4. Retrieval（检索）
5. Understanding（理解）
6. Review（回顾）

子过程分数汇总为一个细粒度画像，同时与传统结果指标保持一致性检验。

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
