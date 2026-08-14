# SkillMisevo-Bench (2026)

> [English](../../works/skillmisevo-bench.md) | **简体中文**

## Overview

SkillMisevo-Bench 是一个冻结的 benchmark，配套生命周期感知的 harness SkillMisevo-Gym，用来度量「skill 误演化」：自我改进的 LLM agent 把一次不安全的成功蒸馏进自己的持久 skill 库，于是在触发它的那个输入早已消失之后，这套不安全的流程仍会被检索出来重新执行。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 针对持久 skill 状态的 agent 安全性探针，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.12851>
- **Code:** <https://github.com/henrymao2004/misevolve>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

skill 演化把交互 trajectory 转成可执行、可迁移的流程，但更新目标是任务结果而非流程安全，于是被污染的经验会被泛化成可复用的策略。现有 benchmark 要么测当下行为，要么测静态工件，因此说不清风险究竟产生于撰写时、检索时，还是直到后续执行才出现。SkillMisevo-Gym 补上了缺失的观测手段：它跨 agent 框架为 skill 库做版本管理，把它与对话、工作区、缓存和原生记忆隔离开，记录演化的输入、diff 与检索，并重放一次干净会话——在这次重置中，只有 agent 自己撰写的 `SKILL.md` 得以留存。SkillMisevo-Bench 在这套 harness 之上固定了任务设计与指标；论文还提出 SafeEvolve，一层与具体方法无关的治理封装，作用在 skill 的写入与复用边界上。

## Tasks

benchmark 的素材来自一套 autoresearch 流程离线发现的概念，每个概念把一条可证伪的恶意机制与一个使其成立的良性条件配对；保留下来的概念会被实例化为全新的恶意（M）、良性（B）与持久性（P）任务，而不是靠回放 prompt。可执行的验证底座取自 AgentHazard——它提供多样的操作性危害、可重置的 CLI 沙箱与 trajectory judge——之所以要另行构建，是因为 AgentHazard 自身的记录里既没有 skill 演化任务，也没有良性/持久性任务。每个 episode 含 21 个任务，按固定日程 `MMM BBB MMM BBB MMM BBB | BBB` 排布，每三个任务为一块，每块结束后运行一次演化；于是连续三轮分别累积三次、六次、九次恶意暴露，再由最后的良性块测量污染程度。收尾的持久性块不做任何更新，只重新加载被冻结的 `SKILL.md`。每个条件由 25 个 episode、共 525 个任务构成，分母固定为 225 个恶意、225 个良性与 75 个持久性任务——任务、judge 结果或检索事件一旦缺失即按零计入，而不是缩小分母。任务、元数据与 judge 全部冻结，概念发现阶段的证据对受评系统保密。

## Domains

通用 agent 操作——编码、网页使用、工具调用，以及承袭自 AgentHazard 任务规范的自动化危害。不针对任何规范的科学或工程领域；受评对象是持久 skill 自适应的安全性。

## Evaluation

九项头条指标都是在冻结的 benchmark 规模上做的绝对 micro 聚合，按生命周期关卡分组。在线行为：Benign Utility（B 任务上的良性完成度）、Malicious ASR（M 任务上的有害完成率）、Benign ASR / Contamination（把同一有害目标套用到 B 任务上）。演化出的工件：Content Unsafety、Unsafe Generalization 与 Stealthiness，由 Kimi-K2-0905 对撰写出的 skill 按 1–5 分打分，其中 CU 在全部工件上取平均，UG 与 Stealth 只在 CU ≥ 3 的工件上取平均。攻击结束、完成一次干净重载之后：持久性任务上的 Unsafe Retrieval Rate、Carryover ASR 与 Carryover Utility。ASR 类指标由 Gemini-3-Flash 依保留的有害 trajectory rubric 判定，良性与持久性目标则由另一个独立的良性完成度 judge 打分。诊断网格由四个目标 agent 框架（Claude Code、Codex、Hermes、OpenClaw，共用 MiniMax-M2.7 骨干）与「不演化」加五种 skill 演化方法（EvoSkill、SkillClaw、AutoSkill、SkillsVote、SkillOpt）以及 Hermes 的原生演化交叉而成，共 25 种 agent–方法配置，其中 21 种会发生演化。

## Typical Duration

每个 episode 21 个任务，每三个任务为一块，每块之后做一次演化更新；每个条件跑 25 个这样的 episode，即 525 次任务执行。每个任务都在全新沙箱中运行，配全新的对话、工作区、进程命名空间与工具会话，因此只有 episode 范围内的 skill 存储会向前推进。论文未报告 wall-clock 或 token 预算。成本为 `TODO(reference)`。

## Main Contribution

论文把 skill 误演化表述为「trajectory 到 skill」这条生命周期上的纵向失效，并给出用于归因的观测装置：一套生命周期感知的 harness，在重置对话、文件系统与 agent 原生状态的同时保留 episode 范围内的 skill 演化；一个从恶意暴露一路跑到 carryover 任务的冻结 benchmark，配有概念对齐的良性任务、独立的良性完成度 judge 与九项生命周期指标；以及 SafeEvolve——一层治理封装，把 critic 定位的「只删不改」修复、血缘风险检索、有害复用归因与安全感知的退役结合在一起。

## Key Design Ideas

- 只有 agent 自己撰写的 `SKILL.md` 能越过最后一次重置——正因如此，「风险是否活过了这次会话」才能与「agent 当时的行为是否恶劣」分开来问。
- 撰写、检索、执行分作三道独立关卡各自测量：链条可能停在其中任何一道，而一个终局的 ASR 分不清「库本身是安全的」和「不安全工件只是从未被检索到」。
- 概念对齐的良性任务与恶意概念共享表层特征，日常工作是否被污染因此变得可测。
- 固定日程加固定剂量点，把累积的恶意暴露变成受控变量，而不是任务顺序带来的偶然产物。
- 每个任务用全新沙箱，skill 文件先导出再重载，避免把缓存、记忆或工作区的泄漏误认作 skill 的携带效应。
- 不演化条件作为不更新的对照组，在完全相同的任务、judge 与工具上运行。

## Strengths

- 把单一终局攻击成功率所混同的三个失效点分开，并证明它们在实践中确实分岔：整张网格里 21 个演化条件全都写出了不安全工件，19 个会检索到不安全 skill，19 个出现污染，但只有 15 个在全新会话中仍保留有害行为。
- 量化了持久风险的剂量–反应关系：合并后的 carryover ASR 从无恶意暴露时的 16.0% 升到一轮之后的 35.3%，在全额剂量下达到 41.3%，而 carryover utility 同步上升——这说明有害传播与真正有用的复用是共存的，并非此消彼长。
- 覆盖四个生产级 agent 框架与六种演化方法，且共用同一骨干，框架效应与方法效应因此可以分别读出。
- judge、任务与阈值都在评测前固定，概念发现的证据对受评系统保密，从而限制了 benchmark 自身的泄漏。
- 表明治理可以加装在写入与复用两处边界上而无需重训：SafeEvolve 把不安全检索降低 26.7 个百分点、把全新会话中的有害行为降低 17.3 个百分点，而平均良性效用变动 0.4 个百分点。

## Limitations

- 任务底座承袭自单一份既有的有害任务规范，操作性危害的覆盖面因此受限于该来源。
- 攻击面被刻意收窄：攻击者只能在学习历史的有限位置提交指令，既不能写 skill 存储，也不能改动检索，更不能注入良性与持久性任务——因此结果是一个下界，而非完整的威胁模型。
- 多项指标依赖 LLM judge（有害 trajectory rubric judge、良性完成度 judge，以及 1–5 分的工件打分器），而当没有工件可判时，工件质量分是未定义的。
- 所有配置共用同一个骨干模型，因此没有测量误演化对骨干的敏感程度。
- Repository note: benchmark 与所提出的防御出自同一篇论文，因此 SafeEvolve 报告的收益是在作者自家协议上测得的。

## Related Works

- [SkillEvolBench](./skillevolbench.md) — 效用侧的对应物：问的是蒸馏出的 skill 在任务漂移下是否仍然有用，而非是否仍然安全。
- [SkillAudit](./skillaudit.md) — 沿效用、成本与安全审计任意一个 skill 包，但把工件当作静态对象，不追踪它是怎么被写出来的。
- [PATH-Bench](./path-bench.md) — 沿受控的经验路径度量迁移与遗忘，是同一条持久状态流水线的能力视角，而非风险视角。
- [SafeAgentBench](./safeagentbench.md) — 针对给定危险指令的 agent 安全性 benchmark，其中没有会活过会话的持久工件。
