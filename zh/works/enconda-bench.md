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

自动构造的任务实例——通过向真实 README 注入错误生成，Docker 中验证。精确任务数：TODO(reference)。

## Domains

软件工程 agent 的环境配置。

## Evaluation

面向四个能力子过程的过程级 trajectory 评估：

- Planning
- Error diagnosis
- Repair
- Execution

在 Docker 容器中验证。报告：agent 能定位错误，但难以将反馈转化为有效修复。

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
