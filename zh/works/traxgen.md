# Traxgen (2025)

> [English](../../works/traxgen.md) | **简体中文**

> **首次公开：** 2025-05-17 · **来源：** [PyPI 首次发布](https://pypi.org/project/traxgen/0.1.0/)

## Overview

Traxgen 是一个面向 AI-agent 评估的**确定性** ground-truth trajectory 生成工具包。它把结构化的 workflow 规范与用户数据编译成一份有向无环图（DAG），进而生成完整规定的参考 trajectory——把 LLM 从 ground-truth 生成流程中移除。论文同时发布一份含 675 个任务实例的配套 benchmark，用于以 Traxgen 生成的参考对比六个 LLM 的规划能力。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** *Traxgen: Ground-Truth Trajectory Generation for AI Agent Evaluation*（Mazzolenis & Zhang）
- **Venue:** NeurIPS 2025 Workshop on Scaling Environments for Agents (SEA)
- **License:** MIT
- **Distribution:** PyPI 包（`traxgen`）

## Summary

Traxgen 主张：trajectory 级 agent 评估依赖高质量的参考 trajectory，而基于 LLM 的参考生成慢、噪声大，也不适用于合规敏感领域。它提供一个完全确定性的替代方案：workflow 以 JSON 描述——包含 steps、soft-ordering blocks 与基于用户数据的 conditional 规则；工具包把每对 workflow–user 编译为 DAG，按条件裁剪，并枚举有效 trajectory。论文既贡献了工具包（MIT 许可），也贡献了一份配套 benchmark，用来在其确定性参考之上比较六个 LLM。

## Tasks

配套 benchmark：**675 个任务实例**，横跨 3 个领域（E-Commerce、HR、Travel）下的 9 个 workflow，涉及 71 个工具。10% 的任务实例是多意图。

复杂度分布：

- Simple：3 workflow × 50 实例（E-Commerce）
- Intermediate：3 workflow × 75 实例（HR）
- Complex：3 workflow × 100 实例（Travel）

## Domains

客户服务场景的 tool-use workflow（E-Commerce、HR、Travel）。Traxgen 工具包本身与领域无关；发布的 benchmark 为客户服务。

## Evaluation

- **Trajectory 质量指标**：Exact Match、Count Agreement、Tool 级与 Parameter 级的 Precision / Recall / F1、Contiguous Overlap Length（CMR）、Prefix Length。预测被通过 Hungarian 算法对齐到最匹配的 gold trajectory 后再打分。
- **在 LLM baseline 上的消融维度**：输入格式（自然语言 vs. JSON）、prompt 风格（Vanilla / ReAct / ReAct + few-shot）、推理策略（直接生成 vs. DFSDT 搜索引导）。
- **六个 LLM 参与基准**：DeepSeek-Chat-v3-0324、Mistral-7B-Instruct、Llama-4-Maverick、Gemini-2.0-Flash-001、Claude-3.7-Sonnet、GPT-4.1。
- **报告**：Traxgen 在所有指标上与 gold trajectory 100% 对齐；在 simple workflow 上相较 LLM 生成有 median 30,000× 加速，跨全部复杂度中位数 > 17,000× 加速。在 complex workflow 上 Sonnet 与 Gemini 显著优于其他被测 LLM；性能随复杂度上升而下降；在 intermediate 复杂度上 JSON 输入普遍优于自然语言；ReAct 风格 prompt 的收益只有边际、不一致的效果。

## Typical Duration

Traxgen 每条 trajectory 的执行近乎瞬时（毫秒的很小分数）。LLM baseline 每条 trajectory 约 1.5 s – 29 s，取决于模型与复杂度（见论文 Table 2）。

## Main Contribution

一个完全确定性、基于 DAG 的框架，可从结构化的 workflow 规范与用户数据出发生成 gold-standard 的 agent trajectory——把基于 LLM 的 ground-truth 生成替换为可复现、MIT 许可、加速数万倍的替代方案——并附带一份 benchmark，量化 LLM 生成与确定性参考之间的差距。

## Key Design Ideas

- Workflow 为 JSON：Steps + Soft Ordering blocks + 面向用户数据的 Conditional 规则。
- Trajectory 规划即 DAG 构造：node 插入、条件裁剪、edge 连线、cycle 检查、soft-order 排列。
- 多 agent 组合通过按顺序拼接各 agent 的 trajectory 完成。
- 四种输出格式以适配现有生态（Tool Only、Google Style、LangChain Tool Style、Traxgen Style）。
- 确定性且可复现——参考生成过程无推理时随机性。
- 配套 benchmark 使用 Traxgen 生成的初稿加两位盲评标注者的独立复审来产生 gold trajectory。

## Strengths

- 把 LLM 噪声从 ground-truth 生成中移除——报告了与人工验证参考的 100% 对齐。
- 相较 LLM 生成有数量级加速（中位数 > 17,000×）。
- MIT 许可与 PyPI 分发降低采用成本。
- 显式面向合规敏感场景（finance、healthcare）作为设计目标。
- 配套 LLM 基准隔离了输入格式、prompt 风格与推理策略的效应。

## Limitations

- 作者说明：尚未在真实世界工作流上验证——真实工作流常涉及复杂互依、多模态输入与非幂等行为。
- 作者说明：对 soft-order 块的全排列在块变大时会阶乘增长，限制可扩展性。
- 作者说明：框架不会在没有预先指定逻辑的情况下适配全新或有歧义的输入。
- 作者说明：LLM 基准受限于所选模型与 prompt 设计。
- Repository note: 尽管工具包与领域无关，配套 benchmark 仍局限在客户服务场景（E-Commerce、HR、Travel）。

## Related Works

- [FinTrace](./fintrace.md) — 同样做多维 trajectory 评估，但是 benchmark 而非 ground-truth 生成工具包。
- [AgentBoard](./agentboard.md) — 同样通过每个任务的标注 ground-truth 结构（subgoal）作为 trajectory 打分的参照。
- [TRACE](./trace.md) — 同样以 trajectory 为一等评估对象，但走的是 trajectory 上的 hierarchical utility function，而非确定性参考生成。
