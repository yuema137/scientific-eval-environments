# AgentLens (2026)

## Overview

AgentLens 是一个面向 interactive code agent 的 production-assessed benchmark，它评估整条交互 trajectory 而非最终的 pass/fail 结果，将形式化验证（formal verification）与 LLM 撰写的 trajectory review 以及 side-by-side 对比相结合。它发布了一个包含 16 个 Java 编码场景的初始 fold，每个场景在一个宽松的 default 用户与一个略带对抗性的 toxic 用户下各运行一次，为每个受评 agent 产生 32 条 trajectory。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.06624>
- **Code:** <https://github.com/agent-lens/agent-lens-bench>

## Summary

AgentLens 认为，大多数 code-agent benchmark 把一次运行压缩为单个 pass/fail 比特，而真正使用这些 agent 的人体验到的是整条 trajectory——agent 如何遵循指令、使用工具、验证自己的工作、从错误中恢复以及与用户沟通。它评估整条 trajectory，在存在客观检查之处将形式化验证与 LLM 撰写的 trajectory review 以及 side-by-side 对比相结合，使每次运行都给出一段关于得分缘由的可读解释。作者不仅用它对模型排名，还用它诊断模型行为、对比自家 agent 的历次版本，并在每晚运行的评估 pipeline 中捕捉产品回归。

## Tasks

一个包含 16 个 coding-agent 场景的初始 fold，每个场景在一个宽松的 default persona 与一个略带对抗性的 toxic persona 下各运行一次，为每个受评 agent 产生 32 条 trajectory。场景有两个来源：在开发者访谈中就其近期实际工作梳理出的工作流，以及由匿名使用摘要构造的、源自生产环境的场景，这些摘要以类似 Clio 的方式聚类并匹配到开源项目。代表性的任务族包括单元测试与测试重构、遗留数据库逻辑迁移，以及 API 文档与 DTO 清理。

## Domains

面向真实开源仓库的 Java 编码助手工作：Spring Boot 项目中的单元测试、数据库逻辑迁移与 API 文档。

## Evaluation

- **形式化验证。** 客观检查——测试、正则表达式匹配、仓库状态断言、构建任务执行以及静态分析校验器（表 1）——在其存在之处施加；只有当某场景的每一个校验器都通过时，该场景才通过形式化验证，运行报告还会记录单个校验器通过的比例。
- **沿五个维度的 trajectory 评审。** LLM judge 沿 EndResult、InstructionCompliance、Pitfalls、Pleasantness 与 ToolCalls 为每条 trajectory 打分，每个维度采用一个小的有序标度，并撰写一段简短评审，引用回指 trajectory 内部的带编号证据指针。
- **Quality Index (QI)。** 单一聚合指数是五个 judge 指标连同形式化验证的非加权均值，各自映射到 [0, 100]。
- **Side-by-side 评审。** 一个成对 judge 就同一场景沿单一维度对比两条 trajectory，给出胜者（A1 / A2 / Tie）、一个相对严重度以及简短证据。
- **确定性 telemetry。** 硬性的按运行统计量——交互成本、cache 命中率、延迟、终止原因、生成 token 吞吐率以及各工具的成功率——独立于任何评判而收集。
- **报告（表 6）。** 在横跨两个 harness（Explyt AI Agent 与 Claude Code）的 17 个 agent 配置中，搭载 Opus 4.7 的 Explyt AI Agent 以 QI 81.5 领先，其后是搭载 Opus 4.7 的 Claude Code（76.2）、GPT-5.5（73.0）与 Sonnet 4.6（70.2），直至 Kimi K2.6 的 28.1（因供应商侧 tool-parser 不稳定而被标注）；单次运行的评审以 GPT-5.4 作为 judge，且未报告任何人类表现 baseline。

## Typical Duration

论文未给出任何按任务的步数或 token 上限。示例运行报告中的终止 telemetry 显示，agent 的单次回复在 900 秒后超时、整个场景在 1,200 秒后超时；论文并指出，搭载 Opus 4.7 的一次完整运行成本可超过 100 美元。

## Main Contribution

一个面向 interactive code agent 的 production-assessed benchmark，它通过将形式化验证与 LLM judge 评审相结合的协议来评估完整的交互 trajectory，并为已部署的编码助手支持 side-by-side 模型对比、特性评估与每晚的回归检测。

## Key Design Ideas

- 以整条交互 trajectory 作为评估单元——用户消息、agent 回复、tool call、文件编辑、命令执行、验证尝试以及最终的仓库状态。
- 将形式化验证与 LLM 撰写的 trajectory review 相配对，使客观检查（在其存在之处）附带一段可读、带证据链接的得分解释。
- 将 LLM 模拟的用户实例化为不同的 persona——一个宽松的 default 用户与一个略带对抗性的 toxic 用户——以在合作式反馈与稀疏、对抗式反馈下考察鲁棒性。
- 一条生产 CI pipeline，按计划运行该 fold，将每个候选版本与一个 anchor 运行对比，并将统计上显著的变化标记为潜在回归。

## Strengths

- Trajectory 级打分暴露出单个 pass/fail 比特所掩盖的失败模式——误导性验证、不安全的工具使用、令人不快的交互——并为每一项附上证据指针。
- 将形式化验证与 LLM 评审相配对削弱了 reward hacking，因为 agent 可以满足一个绿色检查，而评审仍会记录下脆弱的走捷径或被跳过的验证。
- 书面评审与 side-by-side 对比使该 benchmark 在排名之外亦有用武之地，可用于对已部署 agent 的诊断、特性对比与回归检测。

## Limitations

- Repository note: 所发布的 fold 仅限 Java，且覆盖的是某一特定类别的编码助手任务——16 个场景与 32 条 persona 配对的 trajectory——因此得分刻画的是交互式编码行为，而非通用的模型能力。
- Repository note: 该 benchmark 最初是围绕作者自家的编码助手（Explyt AI Agent）构建的，而后者在排行榜上居首；其 LLM-judge 协议的有效性依赖于内部的成对标注经验，而非一项公开发表的人类一致性研究。

## Related Works

- [TRACE](./trace.md) — 同样以多维 utility 为整条 trajectory 打分，但面向 deep-research agent、采用以正确性为硬门控的 hierarchical 函数，而非面向交互式编码助手、采用在 LLM-judge 维度与形式化验证之上的非加权 quality index。
- [FinTrace](./fintrace.md) — 同样是聚合多个质量维度的整体式 trajectory 级评估，但作用于长程金融 tool use、以四个维度上的九个指标计分，而非作用于交互式编码、以五个 LLM-judge 维度并配合形式化验证计分。