# Enconda-bench (2025)

## Overview

Enconda-bench（Environment Configuration Diagnosis Benchmark）在环境配置这一软件工程 agent 常见瓶颈上做过程级评估——避免端到端 build/test benchmark 只报最终结果，隐藏 agent 在哪里、为何失败。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.25694>

## Summary

Enconda-bench 在环境配置过程中对软件工程 agent 做 trajectory 过程级评估。不再仅给出端到端 build/test 是否成功，而是评估配置过程中细粒度的能力——planning、error diagnosis、repair、execution。任务实例通过向真实 README 注入实际错误自动构造，并在 Docker 中验证。

## Tasks

跨 323 个源仓库（各固定到特定 commit）的 4,201 个错误 README 任务（共 9,471 个注入错误）。构造漏斗：1,772 个双错误 README → 1,230 个经 Docker 验证（LLM–人工一致性 98.5%）→ 拆分与合并为含 1–10+ 个错误的 4,201 个 README，按难度分为 1–10 级。

## Domains

软件工程 agent 的环境配置。

## Evaluation

围绕四项能力（论文的 Planning、Perception、Feedback、Action）做过程级评分，各指标组分开报告，而非合成单一分数：

- **Perception（错误诊断）** — 将预测的错误类型（六类之一）与 gold 集匹配；因一个 README 可能含多个错误，以 **Precision / Recall / F1** 报告。
- **Feedback（修复）** — 将预测的**错误描述**与**修复建议**分别与 gold 匹配，并用 GPT-4.1-mini 作为 judge 判定一致性，得到两个**准确率**分数。
- **Planning + Action（执行）** — 抽取的 shell 脚本在固定 commit 的 Docker 容器中运行，以 **Pass@1** 打分：需环境构建成功、测试文件正确执行、进程正常退出方算通过。

**错误注入的有效性验证。** 一个注入错误只有在「带它时 setup 失败、修复后可继续」时才算有效；刻意用较弱的模型（GPT-4.1-mini）生成并运行 setup 脚本，以免更强的模型隐式自动修复错误而破坏有效性；此后再经 LLM 过滤与人工验证（一致性 98.5%）。

报告（最佳配置，Repo2Run + Claude-4）：错误类型 F1 = 60.6、描述准确率 = 52.2、修复准确率 = 47.3、Pass@1 = 22.9。修复准确率（47.3）与 Pass@1（22.9）之间的差距，正是论文关于「agent 能定位错误、却难以把反馈转化为可用修复」的证据。

## Typical Duration

多步配置工作流；摘要未给出具体时长。

## Main Contribution

软件工程 agent 在环境配置上的过程级 trajectory 评估；任务通过真实错误注入自动构造。

## Key Design Ideas

- 面向四个能力子过程（planning / diagnosis / repair / execution）的过程级评估。
- 通过向真实 README 注入错误自动构造任务。
- Docker 中的确定性验证。

## Strengths

- 自动构造无需大量人工标注即可扩展。
- Docker 执行提供确定性验证。
- 过程分解揭示 agent 在何处失败（诊断 vs. 修复 vs. 执行）。

## Limitations

- Repository note: 限定在环境配置——不评估代码编写、架构设计等其他软件工程活动。

## Related Works

- [T-Eval](./t-eval.md) — 同样把评估分解为能力子过程，但面向 tool use 而非环境配置。
- [AgentBoard](./agentboard.md) — 同样是过程级 trajectory 评估，但通过标注子目标，而非通过错误注入构造任务。
