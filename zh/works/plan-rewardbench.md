# Plan-RewardBench (2026)

## Overview

Plan-RewardBench 是一个 benchmark，衡量 reward model 与 LLM judge 在工具集成场景中识别更优 agent trajectory 的能力。它包含 1,171 个成对 trajectory 偏好实例，覆盖七个评测 split 和四个场景族。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.08178>
- **Code:** <https://github.com/wyy-1112/Plan-RewardBench>
- **Venue:** ACL 2026

## Summary

Plan-RewardBench 认为，现有 reward model benchmark 只在短上下文中给单条回复或孤立的工具调用打分，无法评估 reward model 在 agent 系统实际产生的多轮、带工具执行的 trajectory 上的表现。作者构造偏好对：对内固定工具环境与用户意图，只让 agent 的 trajectory 变化，用一条经过验证的 chosen trajectory 对上一条易混淆的 hard negative。在 21 个被评测系统上，最高宏平均为 69.96%（Qwen-Plus），且准确率在超过 32k token 的长 horizon 区间下降，其中成对 LLM judge 下降最陡，逐点 reward model 则更为平缓。

## Tasks

1,171 个偏好对，分布在七个评测 split 上：Tool-Irrelevance / Unavailable 275、Robust Recovery 361、Planning-Single (Easy) 144、Planning-Single (Hard) 158、Planning-Multi (Easy) 109、Planning-Multi (Hard) 73、Safety Refusal 51。这些 split 归并为四个场景族——Safety Refusal、Tool-Irrelevance / Unavailability、Complex Planning、Robust Error Recovery——其中 Complex Planning 按 horizon（单轮 vs. 多轮）与难度分层。种子任务与 MCP 工具注册表来自 Toucan，候选则通过在 Qwen-Agent 与 OpenAI-Agent 两种 runtime 下重跑 rollout、并变化基础模型、system prompt、温度与随机种子来扩展，最终 trajectory 池中 70% 为自然 rollout、22% 为扰动、8% 为规则注入。

## Domains

基于 MCP 风格工具注册表的纯文本、带工具增强的 agent trajectory，覆盖安全拒答、工具无关与工具不可用、多步规划以及错误恢复。

## Evaluation

- **成对准确率。** 主指标是 evaluator 选中 gold 偏好 trajectory 的样本对占比，总分为七个评测 split 上的宏平均。
- **顺序交换协议。** 每个样本对以颠倒的候选顺序评测两次并报告平均正确率，从而控制成对 evaluator 的位置偏置；pointwise 的判别式 reward model 独立给每条 trajectory 打分，不受影响。
- **统一输入。** 每个 evaluator 收到相同的上下文——工具注册表 schema、多轮对话，以及由推理、工具调用与执行输出交错构成的完整 trajectory——因此样本对内部只有 trajectory 不同。
- **人工审核。** 两名标注者在每族 51–80 个样本对的分层子集上独立选出更优 trajectory，分歧由第三名资深标注者裁决；裁决前四个场景族的 Cohen's κ 为 0.71–0.86。
- **报告结果。** 21 个 evaluator 的宏平均准确率从 50.67%（Llama-3.2-8B-Instruct）到 69.96%（Qwen-Plus），其中判别式 reward model 最强者为 Inf-ORM-Llama3.1-70B，达 69.21%。各族最高分归属不同系统——Safety Refusal 上 GPT-5 为 84.80%，Tool-Irrelevance 上 Gemini-3-Flash (preview) 为 75.55%——且没有 evaluator 在 Multi-turn Hard 规划上超过 70%。未报告人类准确率 baseline。

## Typical Duration

对预先录制的 trajectory 对做离线判定——发布版本无需重新执行工具或访问外部服务——因此未定义每任务的步数或 wall-clock 预算。取而代之的是 trajectory 规模：2–64 轮（均值 10.6，中位数 9.0），各 split 的平均输入从 Planning-Single (Easy) 的 1,186 个 token 到 Planning-Multi (Hard) 的 6,554 个，最长单实例为 29,622 个 token。

## Main Contribution

面向复杂工具集成场景的 trajectory 级偏好 benchmark，把经过验证的正例 trajectory 与易混淆的 hard negative 配对，使判别式 reward model、生成式 reward model 与 LLM judge 能在同一套成对协议下比较。

## Key Design Ideas

- 每个样本对内部固定工具环境与用户意图，使 agent 的 trajectory 成为 evaluator 看到的唯一变量。
- 三类 hard negative 来源：多模型自然 rollout、基于规则的扰动，以及只改动 assistant 可见文本、保留已记录工具调用与输出的最小编辑改写。
- 在难度与偏置控制下组装样本对：近似失误与可区分两档分数差、按长度与工具 token 占比分层，以及风格受控的负例。
- 两阶段标注：三判官 panel 按各族专属 rubric 以 1–5 分给每个候选打分并取中位数聚合，meta-review 处理分差过大或标签冲突的情形，再由独立的成对 post-check 确认偏好方向；生成模型集合与判官集合互不相交。

## Strengths

- 在样本对内部固定工具环境与用户意图，把 trajectory 质量与 evaluator 处理不同 prompt 的能力隔离开。
- 最小编辑的 hard negative 保留了已记录的工具调用与源 trajectory 的表层风格，使样本对无法仅凭冗长程度或格式被区分。
- 报告七个 split 而非单一汇总分，显示总体最强的 evaluator 并不是安全拒答或工具无关场景上的最强者。

## Limitations

- Repository note: 作为 gold 的偏好标签由 LLM judge panel 产生并经自动化的成对 post-check 确认；直接的人工验证只覆盖每族 51–80 个样本对的分层子集，因此 1,171 条标签中的绝大多数依赖模型判断。
- Repository note: 各 split 的规模刻意不均衡——Safety Refusal 只有 51 个样本对，而 Robust Recovery 有 361 个——且总分是七个 split 上的宏平均，因此最小的 split 与最大的 split 权重相同。

## Related Works

- [TRACE](./trace.md) — 同样评估完整的 agent trajectory 而非最终答案，但用多维 rubric 给单条 trajectory 打分，而不是让 evaluator 在 chosen 与 rejected 两条 trajectory 之间做选择。
- [FinTrace](./fintrace.md) — 同样是多维 trajectory 评估，但在金融领域给 agent 自身的 trajectory 评分，而不是衡量 reward model 与 judge 对工具使用 trajectory 排序的准确程度。
- [AgentAtlas](./agentatlas.md) — 同样关注 trajectory 内部被评估遗漏的部分，但在已有 benchmark 上套用控制决策分类体系，而不是用 trajectory 偏好对给 judge 打分。
