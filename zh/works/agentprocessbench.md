# AgentProcessBench (2026)

> [English](../../works/agentprocessbench.md) | **简体中文**

## Overview

AgentProcessBench 是一个用于评估 tool-using agent 中间步骤 step-level 有效性的 benchmark，面向真实的多轮 trajectory。它包含采样自 5 个 policy model、覆盖 4 个 tool-use benchmark 的 1,000 条 trajectory，以及 8,509 条人工标注的 step 标签，采用三元 +1 / 0 / −1 方案，标注者间一致性（inter-annotator agreement）达 89.1%。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2603.14465>
- **Project:** <https://huggingface.co/datasets/LulaCola/AgentProcessBench>
- **Code:** <https://github.com/RUCBM/AgentProcessBench>

## Summary

AgentProcessBench 指出，现有的 process-level benchmark 大多局限于闭世界的数学推理，无法刻画 tool 执行动态、开放的特性，而这类场景中的失败往往带来不可逆的副作用。为弥补这一空白，作者构建了他们所称的首个专门用于 tool-augmented trajectory 中 step-level 有效性评估的 benchmark，将一个能够体现探索的三元标注方案与一条用于降低标注歧义的错误传播规则相结合。最终的 benchmark 包含 1,000 条 trajectory 和 8,509 条人工标注 step，标注者间一致性为 89.1%（Cohen's κ 为 0.767），并用于将 20 个 LLM 作为 step-level verifier 进行评估。

## Tasks

1,000 条 tool-use agent trajectory，覆盖 200 个不重复任务，均匀取自四个成熟 benchmark——HotpotQA（多跳推理）、GAIA（deep research）、BFCL（多轮 function calling）与 τ²-Bench（dual-control 对话式 tool use）。每个任务由 5 个 policy model（Qwen3-4B-Instruct-2507、Qwen3-30B-A3B-Instruct-2507、DeepSeek-V3.2、GPT-5-mini、GPT-5）分别 rollout，并保留全部五条以支持跨模型比较；任务通过最大化 E5 embedding 的成对距离来挑选，以保证多样性。

## Domains

开放世界的 tool use，跨越 web（搜索 / 浏览）、命令行文件访问与 function-calling API，涵盖多跳 QA、deep research 信息检索与对话式客服任务。

## Evaluation

- **Ternary step labels.** 每个 assistant step 相对整体任务进展被标注为 +1（正确且有效）、0（中性或探索性）或 −1（错误或有害）。
- **Error-propagation rule.** 一旦某个 step 出错，所有在因果上依赖它的后续 step 都被标注为 −1，直到 agent 明确纠正该错误或转入一个独立的子任务。
- **Step Accuracy (StepAcc).** 模型预测的 step 标签与人工 step 标签之间的 micro-averaged 一致率，在所有 assistant step 上汇总，因而更长的 trajectory 贡献成比例更大。
- **First-Error Accuracy (FirstErrAcc).** 首个 −1 step 与人工标注首个错误相匹配的 trajectory 占比；若双方都未标出错误，则该 trajectory 记为正确。
- **Reported.** 在 20 个受评 LLM 中，平均 StepAcc 从 35.3%（LLaMA-3.2-3B-Instruct）到 81.6%（Gemini-3-Flash-Preview-Thinking）不等，最强的开源模型（Qwen3-30B-A3B-Thinking-2507）达到 68.5%，且 StepAcc 与 FirstErrAcc 高度相关，Pearson r = 0.90。

## Typical Duration

该 benchmark 对预先收集的 trajectory 进行评分，因此自身不设定每任务的 step、wall-clock 或 token 预算。trajectory 长度随子集而变：每条 trajectory 的平均 assistant step 数从 2.7（成功的 HotpotQA）到 15.8（失败的 τ²-Bench）不等，且失败的 τ²-Bench trajectory 中有 28.2% 超过 16 个 step。

## Main Contribution

首个面向 tool-using agent trajectory 的 step-level 有效性评估的人工标注 benchmark，将三元 +1 / 0 / −1 标注协议与一条错误传播规则相结合，覆盖 1,000 条 trajectory 和 8,509 条标注 step。

## Key Design Ideas

- 三元 step 标注：+1 正确且有效、0 中性或探索性、−1 错误或有害，从而奖励必要的探索而非加以惩罚。
- 一条错误传播规则，将一处错误在因果上的所有下游 step 标注为 −1，直到 agent 明确纠正它或转入一个独立的子任务。
- 跨模型 trajectory 采样：在每个任务上 rollout 规模与家族各异的 5 个 policy model，从而暴露与 policy 相关的失败与提前终止行为。
- 两个互补的 verifier 指标：StepAcc 衡量全局 step 标注可靠性，FirstErrAcc 衡量最早错误的定位。

## Strengths

- 高可靠的 ground truth：每条 trajectory 均由受训专家独立进行双重标注，标注者间一致性为 89.1%（Cohen's κ 为 0.767），且已表明发布的标签基本不受向标注者展示的 LLM 参考的影响。
- 首个将 step 验证从闭世界数学推理带入开放世界、跨 web、CLI 与 API 环境的多轮 tool use 的 process-level benchmark。
- 中性标签与显式的错误传播规则相配合，在降低标注歧义的同时区分良性探索与真正有害的动作。

## Limitations

- Repository note: 该 benchmark 对静态、预先收集的 trajectory 进行评分，因此衡量的是模型作为 verifier 判断 step 的能力，而非生成更优 trajectory 的能力，也不会在真实环境中实际驱动 agent。
- Repository note: 标注者在标注时可见来自三个参考 LLM 的预测，作者将其标记为可能的锚定偏差；一次无参考的对照重标注与发布标签的一致率为 84.06%，但以参考为条件的标签仍作为 ground truth。

## Related Works

- [AgentBoard](./agentboard.md) — 同样将 agent 评估分解到 end-task success 之下，但追踪自动的 subgoal 进展，而非人工标注的 step 有效性信号。
- [T-Eval](./t-eval.md) — 同样在最终答案之下对 tool use 进行评分，但沿固定的能力子过程、在短实例上进行，而非在完整 trajectory 上评估自由形式的 step 有效性。
- [TRACE](./trace.md) — 同样在结果之下评估 trajectory，但在 deep research 运行上聚合一个多维认知质量 rubric，而非为单个 tool-use step 赋予三元有效性标签。