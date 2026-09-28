# FrontierCode (2026)

> [English](../../works/frontiercode.md) | **简体中文**

> **首次公开：** 2026-06-08 · **来源：** [官方公告](https://cognition.com/blog/frontier-code)

## Overview

FrontierCode 是 Cognition 的代码评测，检查 agent 提交的 pull request 是否达到维护者愿意合并的标准。来自 36 个开源仓库的维护者参与制定要求，评判范围超出测试是否通过。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Project and leaderboard:** <https://cognition.com/frontiercode>
- **Initial methodology:** <https://cognition.com/blog/frontier-code>
- **Revision 1.1 (2026-07-07):** <https://cognition.com/blog/frontier-code-1.1>
- **Opus 5.5 evaluation settings:** <https://www.anthropic.com/claude-opus-5-5>
- **Venue:** 业界 benchmark；有官方方法说明，未找到配套论文。

## Summary

Agent 收到代码仓库、简洁的任务描述和代码库规范，提交补丁后，由测试和审阅标准检查正确性、测试质量、改动范围及代码风格。1.1 版允许正常联网查资料，同时检测对含解上游材料的访问；团队还审计了超过 1,000 条 blocker 标准，放宽其中过严的 75 条。

## Tasks

Extended 共 150 题，Main 取其中最难的 100 题。原来的 Diamond 含 50 题，1.1 版已将其停用：修订后它不再对应最难的任务，且过低的解出率使结果噪声较大。20 余位资深开发者参与任务编写和审阅，每题投入超过 40 小时。

## Domains

开源软件工程；无科学领域。

## Evaluation

- 同时报告 blocker 通过率和加权 rubric 分数；初始协议规定未满足 blocker 要求的解得零分。单元测试及其他验证器与 rubric 结合，并经过对抗检查、校准和人工质量审阅。
- 允许查询文档、API 和背景知识。公平联网提示与程序化扫描器检查含解的 PR、补丁、镜像及上游文件，违规运行记零分。
- 初始协议在每个可用 reasoning effort 下运行五次，报告成绩最好的 effort 的均值；排行榜同时比较成本与速度。
- 2026-09-27 核查：官方 Main 榜发布的数据中，Opus 5.5 以 54.6% 排第一，Opus 5 为 53.4%，GPT-6 Astra 为 53.3%。Changelog 于 9 月 22 日加入 Opus 5.5，方法版本仍为 1.1。
- Anthropic 另行报告 Opus 5.5 在 max effort 下为 54.4%、medium 下为 54.6%；其 max-effort 表中 Opus 5 为 48.0%。不能把这个基线替换进取最佳 effort 的官方榜单比较。

## Typical Duration

任务规模相当于一个 pull request。上述 40+ 小时是任务编写投入，不是 agent 运行时间；统一的单次运行时间预算为 TODO(reference)。

## Main Contribution

把 coding agent 的目标从「测试通过」改为「维护者愿意合并」，直接对人类审阅者真正把关的那些品质打分。

## Key Design Ideas

- 可合并性把正确性与审阅时真正看重的那些品质（改动范围克制、代码风格、测试质量）捆绑在一起，这些是通过/不通过指标看不见的。
- 每任务 40 小时以上的资深开发者投入换来任务的真实性。
- 内建的防泄漏检测对触碰含解来源的运行直接记零。

## Strengths

维护者制定的接受标准能检查功能正确性之外的代码质量。明确的联网规则保留正常资料查询，同时检查解答泄漏。

## Limitations

- Repository note: 分数受方法版本、reasoning effort 和执行设置影响；官方排行榜与模型厂商的结果表是不同快照。
- Anthropic 的发布评测启用生产环境防护；相关任务触发防护时会使用旧模型接替。因此，不能把它理解为每一题都完全由 Opus 5.5 独立完成。
- Repository note: 虽未找到常规论文，官方方法文章已提供任务规模与判分细节，不能据此把这些信息标成未知。

## Related Works

- [SWE-bench](./swe-bench.md) — 同样是真实仓库的编码任务，但以测试套件而非可合并性判分。
- [SWE-chat](./swe-chat.md) — 同样把评估植根于人类真正接受的东西，用真实会话中被提交的代码行。
- [Agents' Last Exam](./agents-last-exam.md) — 同样是高投入、专家构建的真实职业任务。
