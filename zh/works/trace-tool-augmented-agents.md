# TRACE for Tool-Augmented Agents (2025)

> [English](../../works/trace-tool-augmented-agents.md) | **简体中文**

> **首次公开：** 2025-10-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2510.02837)

## Overview

GTA 这类 tool-use benchmark 通常只比对最终答案来给 agent 打分。于是两个答案相同的 agent 会拿到同样的分数，哪怕其中一个多调了不必要的工具，或者凭着从没检索到的事实在推理。拿每条 trajectory 去和参考 trajectory 比对可以发现这些问题，但合法的工具调用顺序往往有很多种，把它们全部标注出来代价很高。TRACE（Trajectory-based Reasoning Assessment and Comprehensive Evaluation）干脆不用参考 trajectory：LLM judge 依据由 agent 自己的工具调用构成的 *evidence bank*，给效率、幻觉和适应性打分。作者还构造了一套故意带缺陷的 trajectory 作为 meta-evaluation 集，检验 judge 能否发现这些人为插入的缺陷。这项工作与 deep research 方向的 [TRACE](./trace.md) 卡片不是同一个工作。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — 这是面向通用工具增强问答（GTA、m&m's、GAIA）的 trajectory meta-evaluation 框架，不评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2510.02837>
- **Code:** <https://github.com/wonjoong-kim/TRACE>
- **Venue:** ICML 2026

## Summary

对一条 ReAct 风格的 trajectory，TRACE 把每一步记成一条证据 e<sub>t</sub> = (action, input, observation)，并累积成证据库 E<sub>t</sub>。随后 judge 做三件事：拿每个 thought 去和它之前已有的证据对照，判断有没有幻觉；在每次工具调用失败之后，检查下一步是否选了合理的替代方案，以此衡量适应性；在答案正确时，找出足以支撑这个答案的最小证据子集，以此衡量效率。在基于 GTA 和 m&m's 构造的合成 meta-evaluation 集上，对大多数 judge 而言，TRACE 的判断准确率都高于普通的 LLM-as-a-judge baseline，提升最大的是最小的那个 judge。Meta-evaluation 集里的缺陷是人工合成插入的，所以 judge 在自然出现的错误上表现如何，并没有直接测量。

## Tasks

Meta-evaluation 数据集：

- **Meta-GTA：** 761 条 trajectory（168 条正确、171 条低效、251 条含幻觉、171 条涉及适应性），基于 GTA 构造。
- **Meta-m&m's：** 735 条 trajectory（374 条正确、361 条低效），基于 m&m's 经人工核验过滤后的测试集构造。由于 m&m's 的 trajectory 里没有 thought，这一集合不标注幻觉和适应性。

构造方式：GPT-4o 把每条 ground-truth trajectory 扩展成多种合法的工具调用顺序；再插入低效步骤和含幻觉的 thought；适应性案例的做法是让某个工具不可用，同时加入名字相近的工具（FastCalculator、FastOCR、ImageDescriptor、WebSearch）。生成结果由 Claude Sonnet 4、GPT-4o 和 Gemini Pro 分别检查，只保留三者都判为有效的样本；每个模型抽 100 个样本做人工检查，一致率为 98.79%。

应用研究：在 GTA 上评估 9 个 agent backbone，附录中另有一次在 GAIA 上运行 Magentic-One 多 agent 系统的实验。

## Domains

使用多模态工具和网络工具的通用工具增强问答（GTA、m&m's、GAIA）。

## Evaluation

- **效率。** Eff(T) = |E<sub>min</sub>| / |E<sub>n</sub>|，其中 E<sub>n</sub> 是完整证据库，E<sub>min</sub> 是足以支撑最终答案的最小子集；只对答对的情况计算。
- **幻觉。** 如果第 t 步的 thought 在 E<sub>t−1</sub> 中找不到依据，则 H(s<sub>t</sub>) = 1；第一步对照的是空证据库，使用证据库里没有的模型内部知识也算幻觉。H(T) = Σ H(s<sub>t</sub>) / n。
- **适应性。** 每次工具调用失败后，如果下一个 thought 承认了失败、下一个动作是合理的替代方案，记 1 分，否则记 0。
- **Trace。** 在一个 GTA 案例中，GPT-4.1 和 Qwen-72B 都答对了，但 GPT-4.1 手里已经有关键事实（"Regency Cafe"），还是多调了一次工具；这次调用不在 E<sub>min</sub> 里，所以 GPT-4.1 的效率分更低。
- **Meta-evaluation（准确率，LLM-as-a-judge baseline → TRACE，Meta-GTA）。** 效率：Claude-Sonnet-4 从 86.08 到 94.64，GPT-4.1 从 81.45 到 94.24，Llama-3.1-8B 从 55.67 到 70.46。幻觉：Llama-3.3-70B 从 88.95 到 95.97。在存在多条合法 trajectory 的情况下，TRACE 配 Claude 达到 98.68 ± 1.26，PIPA baseline 为 77.31 ± 9.96。
- **应用结果。** GTA 上的总体准确率从 0.5767（Claude-Sonnet-4）到 0.0154（Mistral-7B）不等；Qwen-7B（0.3904）高于 Llama-3.3-70B（0.3738）。适应性能把准确率相近的 agent 区分开：GPT-4.1 为 0.8056，o3-mini 为 0.6250，Claude-Sonnet-4 为 0.8750。

## Typical Duration

论文报告，用 Llama-3.3-70B 做 judge 时，准确率与更大的闭源 judge 相当，速度最多快约 3 倍；没有报告绝对耗时和成本。TODO(reference)

## Main Contribution

一个不依赖参考 trajectory 的框架，借助 evidence bank 从效率、幻觉和适应性三方面给工具增强 agent 的 trajectory 打分；同时提供由带缺陷 trajectory 组成的 meta-evaluation 数据集，并用它说明：即便换成较小的开源 judge，这个框架也能准确评估 trajectory。

## Key Design Ideas

- 用 agent 自己累积的证据替代参考 trajectory，这样任何合法的工具调用顺序都能评判，无需事先穷举。
- 把证据存成结构化的 (action, input, observation) 记录，而不是把原始对话直接交给 judge。
- 只在工具调用失败时给适应性打分，这样它衡量的是出错后的恢复能力，而不是一般行为。
- 先在已知插入了缺陷的 trajectory 上验证 judge，再拿它去评估 agent。

## Strengths

- 在 Meta-GTA 的效率评估上，TRACE 让每一个 judge 的准确率都超过了普通 baseline，提升最大的是最小的 judge（Llama-3.1-8B）。
- Meta-evaluation 包含同一解法的多种合法顺序，用来检验正确但与参考不同的 trajectory 不会被扣分。
- 代码已公开。

## Limitations

- 效率指标只能在已用到的工具里标出多余的那些，找不出最优的工具路径；作者指出，没有 ground truth 时这个问题无法求解。
- Repository note: Meta-evaluation 中的缺陷是合成插入的，适应性也是用人为制造的工具不可用来测试；在自然出现的错误上的准确率没有单独测量。
- Repository note: 在应用研究中，Claude-Sonnet-4 和 GPT-4.1 既是被评估的 agent，又充当 judge。
- Repository note: 只要用了内部知识就算幻觉，所以即使某一步依靠的背景知识是正确的，也会被严格地判为幻觉。

## Related Works

- [TRACE](./trace.md) — 缩写相同但是另一项工作；它用层级化的 utility function 给 deep research trajectory 打分。
- [AgentProcessBench](./agentprocessbench.md) — 同样在最终答案之下评估 tool-use trajectory，但用的是人工 step 标签，而不是基于 evidence bank 的 judge 评判。
- [T-Eval](./t-eval.md) — 同样在最终答案之下给 tool use 打分，但沿着固定的能力子过程进行。
- [ToolPRMBench](./toolprmbench.md) — 同样评估面向工具使用 agent 的 step 层面 judge，形式是让 process reward model 在正确与错误动作之间做选择。
