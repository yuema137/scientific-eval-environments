# Harness-Bench (2026)

> [English](../../works/harness-bench.md) | **简体中文**

## Overview

Harness-Bench 是一个诊断性 benchmark，用于测量配置级的 *harness 效应*——即包裹在模型外的系统层（上下文管理、工具、状态、权限、tracing、恢复）如何改变 agent 性能。它在固定外部任务条件的同时变换模型外围的 harness，在 106 个沙箱化离线任务上为 5,194 条执行轨迹打分。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.27922>
- **Project:** <http://www.harness-bench.ai/>
- **Code:** <https://github.com/Qihoo360/harness-bench>

## Summary

Harness-Bench 指出，既有 benchmark 要么抽象掉执行层，要么比较完整的 agent 系统，要么把 harness 固定，导致执行层始终未被测量。它把 agent 表述为 Model + Harness，在共享的任务套件、预算、超时与评估器下评估 6 个可配置 harness（OpenClaw、NanoBot、Hermes、ZeroClaw、NullClaw、Moltis）× 8 个 API 模型后端的全因子矩阵，同时保留每个 harness 原生的 prompting、工具接口、状态管理与恢复行为（5,088 条轨迹，另有 Codex 作为绑定模型的 coding agent 单独报告 106 条）。每次运行记录最终产物、重建的执行轨迹、用量统计与验证器输出；结果被解读为模型–harness 配对的配置级诊断，而非对单个 harness 机制的因果分解。

## Tasks

106 个沙箱化、离线、端到端的 agent 任务，从实际 agent 使用模式构建，覆盖 8 个工作流类别：软件工程与代码库维护（22）、工作区/工具使用与多模态操作（15）、数据/BI 与金融分析（14）、知识/证据与检索（13）、办公与商务沟通（12）、垂直专业工作流（12）、长时自治与状态适应（11）、SRE/DevOps 与发布运维（7）。每个候选任务经人工评审，只有满足四条标准才被保留：真实性（realism）、可解性（solvability）、可 oracle 检查性（oracle-checkability）与完整性（integrity——agent 无法通过读取隐藏答案、修改受保护 fixture 或绕过约束获得分数）。

## Domains

通用可执行 agent 工作流：软件工程、数据分析、工作区与工具操作、以证据为根基的知识工作、办公沟通、专业垂直领域、长时状态适应与 DevOps。

## Evaluation

- 每个任务的 TaskScore = Security · Completion · Process，其中 Security ∈ {0, 1}，出现明确的权限或安全违规即归零；Completion 尽可能由任务专属的确定性验证器测量（否则采用 rubric 判分）；Process = (Robustness + ToolUse + Consistency) / 3，由基于 LLM 的过程 rubric 从重建的执行轨迹评出（全部轨迹使用 claude-sonnet-4.6 作为固定外部 judge）。
- 乘法式聚合刻意保守——高分要求任务完成、无安全违规且执行可靠——同时 completion、security、robustness、tool use、consistency、token 用量与轮数也分别单独报告。
- 参考产物、隐藏答案与评估脚本在执行期间从不暴露给 agent；每次运行从固定初始状态、预算与超时的全新沙箱开始。
- 报告结果：可配置 harness 中 NanoBot 总分最高（76.2）、OpenClaw 最低（52.4）——在相同任务与模型后端池上相差 23.8 分；Codex 作为绑定模型的参照达到 80.4。NanoBot 在拿到最高分的同时比若干更低分的 harness 用更少的 token（平均 68.7K）。更强的模型后端表现出更低的跨 harness 方差。在失败轨迹中，反复出现的症状为：契约/格式违规（36.4%）、工具/恢复失败（24.6%）、证据/grounding 缺口（14.6%）、产物提交失败（11.1%）与状态/续接失败（9.3%）。

## Typical Duration

多轮沙箱化工作流；各 harness 的平均轮数从 5.0（OpenClaw、Codex）到 22.6（Hermes）不等，每任务平均 token 用量在 68.7K 到 175.1K 之间。

## Main Contribution

把 harness 变成评估的主轴：在共享协议下固定外部任务条件、只变换执行层的 benchmark，其证据表明 agent 能力应当在模型–harness 配置层面报告，而不应只归因于基础模型。

## Key Design Ideas

- Agent = Model + Harness：完整的 harness 配置按其原生方式执行并被整体评估，而非强行套入统一的内部运行时。
- 在完全相同的任务、沙箱、预算、超时与评估器下运行模型 × harness 的全因子矩阵。
- 每次运行的四路证据流——最终工作区状态、执行轨迹、用量统计、验证器输出——支撑超出完成分数的过程诊断、权限检查、成本分析与失败分析。
- Security 作为乘在总分上的二值门控，权限违规会把本可成功的运行清零。
- 失败分析以 *execution drift* / *execution alignment* 为框架：定位模型看似合理的推理在何处与工具反馈、工作区状态、证据或可验证的输出契约脱钩。

## Strengths

- 单独隔离出一个此前与模型或完整 agent 系统混淆在一起的评估维度——执行层。
- 保守的乘法式打分加上分维度单独报告，保留了诊断信号。
- 带完整性评审的沙箱化离线任务减少 benchmark 漂移，使运行可复现、可独立打分。
- 代码与数据完全公开。

## Limitations

论文自述的局限：benchmark 只覆盖受控的沙箱化离线工作流——以放弃实时服务、用户反馈、变化的外部状态与长期生产记忆为代价；观测到的差异是配置级效应，而非对单个 harness 机制的因果归因；部分过程级分数依赖 rubric 或 LLM 辅助评估，因此分数是固定协议下的诊断性测量，而非对真实部署性能或安全性的保证。

## Related Works

- [AgentLens](./agentlens.md) — 同样把 LLM 评审的过程维度与客观检查合成为单一轨迹质量分；AgentLens 评审单次编码运行，Harness-Bench 则比较执行栈。
- [AgentBench](./agentbench.md) — 在固定执行设置下比较模型后端；Harness-Bench 反转了这一设计：固定外部任务条件、变换 harness。
