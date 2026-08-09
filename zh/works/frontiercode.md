# FrontierCode (2026)

> [English](../../works/frontiercode.md) | **简体中文**

## Overview

FrontierCode 是 Cognition 推出的业界 benchmark，自称首个测量「可合并性」（mergeability）的评测——维护者真的会合并这个 PR 吗？——任务由 20 余位资深开发者构建，每个任务投入超过 40 小时。目前没有配套论文（见 Limitations 中的 repository note）。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Project:** <https://cognition.com/frontiercode>
- **Venue:** 业界 benchmark（Cognition）；无论文；当前版本 FrontierCode 1.1（2026-07-07）

## Summary

FrontierCode 在真实开源仓库中由维护者撰写任务，对端到端代码质量打分——正确性、测试质量、范围克制、代码风格与对代码库规范的遵循——评分采用单元测试、评分标准与新型验证器的组合。联网访问仅限文档：凡查阅原始 pull request 等含解的来源的运行，都会被检测并记零分。

## Tasks

跨多个真实开源仓库、由维护者撰写的任务，由 20 余位资深开发者以每任务 40 小时以上的投入构建；具体任务数为 TODO(reference)。

## Domains

开源软件工程；无科学领域。

## Evaluation

- 以可合并性作为待测目标；用单元测试、评分标准与新型验证器的组合，对正确性、测试质量、范围克制、风格与代码库规范遵循打分。
- 泄漏检测：查阅原始 pull request 等含解来源的运行记零分。
- 具体分数只发布在交互式排行榜上；TODO(reference)。

## Typical Duration

Pull request 量级的端到端编码任务；预算为 TODO(reference)。

## Main Contribution

把 coding agent 的目标从「测试通过」改为「维护者愿意合并」，直接对人类审阅者真正把关的那些品质打分。

## Key Design Ideas

- 可合并性把正确性与审阅时真正看重的那些品质（改动范围克制、代码风格、测试质量）捆绑在一起，这些是通过/不通过指标看不见的。
- 每任务 40 小时以上的资深开发者投入换来任务的真实性。
- 内建的防泄漏检测对触碰含解来源的运行直接记零。

## Strengths

- 评估的是与部署直接相关的目标本身——维护者是否接受——而非代理指标。
- 评估阶段有显式的防泄漏强制机制。

## Limitations

- Repository note: 卡片仅依据官方网站编写（2026 年 8 月）；FrontierCode 无配套论文，任务数、分数与方法学细节均为 TODO(reference)，本仓库对论文实施的两级内容校验在此无法完整执行。

## Related Works

- [SWE-bench](./swe-bench.md) — 同样是真实仓库的编码任务，但以测试套件而非可合并性判分。
- [SWE-chat](./swe-chat.md) — 同样把评估植根于人类真正接受的东西，用真实会话中被提交的代码行。
- [Agents' Last Exam](./agents-last-exam.md) — 同样是高投入、专家构建的真实职业任务。
