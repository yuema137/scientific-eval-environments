# AgentRewardBench (2025)

## Overview

AgentRewardBench 是一个 benchmark，用于衡量自动评估器——LLM judge 以及 web agent benchmark 自带的规则式评分器——在多大程度上复现专家对 agent trajectory 的判断。它包含 1,302 条 trajectory，取自 5 个 web benchmark 和 4 个 agent LLM，每条都由专家标注者就成功、副作用和重复行为进行审阅。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.08942>
- **Project:** <https://agent-reward-bench.github.io/>
- **Code:** <https://github.com/McGill-NLP/agent-reward-bench>
- **Venue:** COLM 2025

## Summary

AgentRewardBench 指出，规则式评估难以扩展到新任务，且可能无法识别成功的 trajectory，而人工审阅更慢、成本更高，因此 LLM judge 能否作为替代方案尚不清楚。作者收集了 1,302 条 web agent trajectory，由专家标注者对每一条标注任务成功、非预期副作用和重复循环，再用这些标签为 LLM judge 和环境自带的评分器打分。在 12 个 LLM judge 中没有任何一个模型能在所有 benchmark 上都表现出色，而来源 benchmark 所使用的规则式评估相对于专家标注低报了 web agent 的成功率。

## Tasks

351 个独立任务，覆盖 8 个环境和 66 个网站，划分为 51 个开发任务和 300 个测试任务：WebArena、VisualWebArena 和 WorkArena++ 各 100 个，AssistantBench 33 个，WorkArena 18 个。任务并非新编写，而是从 5 个已有的 web agent benchmark 中采样：WebArena 每个 domain-evaluation 组最多取 8 个任务，VisualWebArena 最多取 9 个，WorkArena++ 限定为 Level 2。用 4 个 agent LLM 在这些任务上运行，产生 1,302 条 trajectory，其中 196 条在开发划分、1,106 条在测试划分。

## Domains

自建站点与真实网站上的 web agent trajectory：通用浏览、需要视觉定位的任务、开放网络信息检索，以及 ServiceNow 上的企业 IT、HR 与客户管理工作流。

## Evaluation

- **专家标注作为 ground truth。** 一组 6 名专家标注者对每条 trajectory 回答三个二元问题——动作序列是否达成目标、是否执行了可能导致非预期副作用的多余动作、agent 是否陷入没有进展的循环——共产生 3,906 条二元标注；在来自 WebArena 的 GPT-4o trajectory 上，标注者间在成功维度上的一致性为 89.3%。
- **以专家成功标签为准的 precision。** 各 judge 按 precision 排名，理由是 false positive 会污染 rejection finetuning 与 reward modeling；recall 和 F1 作为辅助指标报告。
- **成功率重建。** 由专家标注、读取 accessibility tree 的 GPT-4o judge、以及 benchmark 自带规则式评分器分别算出的 agent 成功率被并列摆放，以暴露三者在何处产生分歧。
- **报告结果（表 1）。** 规则式评估达到 83.8% 的 precision 和 55.9% 的 recall，而 precision 最高的 LLM judge——作者提出的读取 accessibility tree 的简化 GPT-4o judge——达到 69.8% 的 precision 和 83.1% 的 recall，且没有任何 judge 超过 70% 的 precision。相对于专家标注，规则式评分把 GPT-4o 在 WebArena 上压低 16.7%，在 VisualWebArena 上压低 18.5%。

## Typical Duration

各 agent 的配置上限为 40K input token 和 8,192 output token。未说明：没有给出每个任务的步数上限、wall-clock 限制或 trajectory 长度分布。

## Main Contribution

一个包含 1,302 条专家标注 web agent trajectory 的 benchmark，用于衡量 LLM judge 和规则式评分器在多大程度上复现专家对任务成功、副作用和重复行为的判断。

## Key Design Ideas

- 汇集自 5 个已有 web benchmark 和 4 个 agent LLM 而非单一环境的 trajectory，使 judge 质量可以跨任务类型比较。
- 三部分二元标注体系：任务成功、非预期副作用、重复循环。
- 以成功标签上的 precision 作为主指标，其选择依据是下游的 rejection finetuning 与 reward modeling，而非平衡准确率。
- 一个简化 judge，直接依据最终的 accessibility tree 或最终截图回答三个标注问题，去掉了此前 judge 所需的图像描述与变化摘要环节。

## Strengths

- 每条 trajectory 都有专家标签，给出独立于环境自身评分规则的 ground truth，这正是规则式评分器本身得以被测量的前提。
- 汇集 5 个 benchmark 和 4 个 agent 骨干模型，把 judge 质量与任何单一环境的特异性分离开。
- 在成功之外同时标注副作用和重复行为，捕捉到单一成功比特无法表达的失败模式。

## Limitations

- Repository note: 主榜单只对成功标签打分；副作用和重复行为的预测在附录表中单独报告，因此主对比并未反映标注者所标注的三个维度中的两个——而且这两者表现不同：重复行为的 precision 高于成功标签，副作用的 precision 则远低于它。
- Repository note: 覆盖范围自始至终都是 web 浏览——5 个 web benchmark 背后的 8 个环境——因此这些 judge 排名无法迁移到其他载体上的 agent trajectory。

## Related Works

- [AgentAtlas](./agentatlas.md) — 同样是对已有 benchmark 的审计而非新的任务集，但它对 trajectory 内部的控制决策做分类，而非衡量自动评分器复现专家成功标签的忠实程度。
- [AgentBoard](./agentboard.md) — 同样在最终任务成功之下对 trajectory 打分，但走的是人工编写子目标的进度路线，而非为发出成功标签的评估器本身做 benchmark。
- [FinTrace](./fintrace.md) — 同样是多维度 trajectory 评估，但评的是金融工作流中的 agent，而非评判 web agent 的 judge。
