# VeRO / VeRO-Bench (2026)

> [English](../../works/vero.md) | **简体中文**

> **首次公开：** 2026-02-25 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.22480)

## Overview

VeRO（Versioning, Rewards, and Observations）是一个外层 harness，用于 benchmark coding agent 在 *agent harness optimization* 任务上的表现——即通过编辑并评估目标 agent 的代码来迭代改进它——提供版本化快照、预算受控的评估与结构化执行轨迹。VeRO-Bench 是配套的 benchmark 套件，包含目标 agent、任务与参考评估流程。

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2602.22480>
- **Code:** <https://github.com/scaleapi/vero>
- **Venue:** ICML 2026

## Summary

VeRO 把 agent 优化表述为一个开放式编程任务，考察作为*优化器*的 coding agent 能在多大程度上把*目标 agent harness* 当作任意程序来改进——论文将这一设定与把底层工作流视为固定的 prompt 优化框架区分开。由于 harness 交织着确定性代码与随机的 LLM 补全，且不受控的优化会带来评估污染与预算滥用的风险，VeRO 强制执行六项要求：版本化（每次修改都是自动提交的 Git 快照）、预算强制、权限控制（无法访问 held-out 测试数据与评估基础设施）、可复现执行（uv 锁定依赖、隔离环境）、结构化 tracing、以及标准化的观察接口。优化目标是 *lift*——在 held-out 数据上相对 baseline agent 的期望改进——并受硬性评估调用预算 n_E ≤ B 约束。

## Tasks

Benchmark 研究在五个目标 agent 任务上评估优化器，覆盖数学推理（MATH）、tool use（TAU-Bench Retail）、多步推理（GAIA）、事实性 QA（SimpleQA）与科学 QA（GPQA），各任务带 train/validation/test 划分与手工编写的任务专属目标 agent（目标模型固定为 GPT-4.1 mini）。主协议比较 8 个优化器配置 × 5 个任务 × N = 3 次迭代（120 组实验，预算 B = 8）：Claude Code 变体（Pure、VeRO Tools）、VeRO-Agent 变体（Default、三种优化器模型下的 Orchestrator、Resources-Only），以及作为外部 baseline 的 GEPA。案例研究另含一对极简 vs. 复杂 agent（Pawn / Knight）在 GAIA 上的对照实验，以及在 TerminalBench-2（89 个终端任务）上优化 Terminus-KIRA harness 的长 horizon 编码研究。

## Domains

在通用 agentic 任务套件上的 agent harness 优化：数学、tool use、多步 QA、事实性与科学 QA、终端编码。

## Evaluation

- **相对 baseline 的 lift**——跨迭代相对初始 agent 的最大准确率增益，在 held-out 数据上评估——另报告跨迭代方差（优化稳定性）与每样本平均推理时间。
- **预算受控的评估：** 每次评估请求检出指定 commit、运行门控的 Evaluator、存储结果并扣减预算；超出 n_E ≤ B 的请求被阻断，因此没有优化器能靠额外算力获利。TerminalBench-2 的预算按样本数而非完整轮次定义，因为用 Claude Haiku 4.5 完整评估一次 89 任务套件约需 180 美元。
- 报告结果：固定目标模型下，完整 VeRO harness 的平均最佳分数为 0.61（baseline 0.50）；不带 VeRO 工具的 Claude Code 为 0.53，仅添加 VeRO 工具为 0.55。外部 baseline GEPA（0.54）与 VeRO 的 Resources-Only 变体（0.54）持平，均低于 VeRO-Agent Default。增益高度依赖任务——tool-use 类任务（GAIA、Retail、SimpleQA）持续改进，而推理密集型任务（GPQA、MATH）几乎不动；B ∈ {2, 4, 8, 16, 32} 的预算消融表明推理任务的平台期并非预算不足所致。在 TerminalBench-2 上，最佳优化运行把通过率从 30.3%（27/89）提升到 37.1%（33/89），另有一次运行在不改变通过率的情况下把崩溃率从 46.1% 降到 30.3%。

## Typical Duration

最多 B 次评估调用的迭代优化循环（主研究 B = 8），每次包含代码审读、修改与一次经预算门控的目标 agent 训练样本评估。

## Main Contribution

把 agent 优化变成 coding agent 的一项可 benchmark 的能力：一套受控协议（版本化、预算强制、权限控制、可复现执行、结构化 tracing、标准化观察）加上标准化套件，使优化器能在完全相同的资源与信息条件下被比较。

## Key Design Ideas

- 把评估调用作为稀缺资源：对目标 agent 的每次打分都被视为昂贵的黑盒查询，从硬预算中扣减。
- Git worktree 版本化加自动提交 hook，使每次修改都成为不可变、可 diff 的轨迹步骤，支持回滚与事后分析。
- 权限控制以程序化方式隔离 held-out 测试数据、评估基础设施与模型 checkpoint 更换，杜绝平凡解或污染取胜。
- 标准化观察接口固定每个优化器可见的轨迹、历史与统计信息，使比较隔离的是优化器本身而非其信息获取。
- 优化轨迹的可解释性：按变更类型为 commit 历史打标，显示优化器默认倾向 prompt 修改（首阶段之后超过 50% 的阶段），且变更多样性在早期阶段后迅速收缩。

## Strengths

- 把评估成本预算变成强制执行的门控协议要素，而非君子协定。
- 与 coding agent 无关：任何消费其暴露接口并保持 commit 级可追溯性的优化器都可被 benchmark。
- 排行榜之外的实证发现：优化空间与目标 agent 的复杂度成反比；指令模板在方差与峰值性能之间存在权衡；单任务增益并不可靠泛化（一次 commit 在 GAIA 上 +5.75 分的同时在 SimpleQA 上倒退 −17.8）。
- 鲁棒性研究检验更换目标模型后优化过的 harness 是否仍有效，发现增益在同模型家族内保持、跨家族可能倒退。

## Limitations

论文自述的局限：预算只按评估调用而非 token 或 API 成本定义，引入方差；未比较跨独立会话的预算分配策略；缺少目标 agent 的人类 baseline；公共 API 的不稳定性与经泄露 ground truth 的 reward hacking 未受控制。

## Related Works

- [Harness-Bench](./harness-bench.md) — 同样把 agent harness 作为一等评估对象，但测量的是固定 harness 配置跨模型对性能的影响，而 VeRO 评估的是*编辑* harness 的 agent。
- [SWE-bench](./swe-bench.md) — 基于执行打分的 coding-agent benchmark，其 Docker 式可复现性被 VeRO 用 uv 锁定、Git 版本化的目标包显式效仿；SWE-bench 测量任务完成，VeRO 测量改进其他 agent 的能力。
