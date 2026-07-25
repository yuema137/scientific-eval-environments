# Gaia2 (2026)

## Overview

Gaia2 是一个面向异步环境中 LLM agent 的 benchmark——在这类环境里，世界按自己的时钟推进，而非仅在 agent 行动时才变化。它的 1,120 个场景运行在一个模拟的智能手机世界中，由一个验证器对照 oracle 标注检查每一个改变状态的动作来打分，使该 benchmark 可直接用于基于可验证奖励的强化学习（RLVR）。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.11964>
- **Venue:** ICLR 2026

## Summary

作者指出，多数 agent benchmark 是静态或同步的——环境只在 agent 行动时改变，且评估忽略中间动作——因此真实部署中占主导的挑战，例如异步事件与在时间约束下工作，都未被考察。Gaia2 的应对方式是：把场景放进独立于 agent 推进的事件驱动环境中，并对照一条由改变状态的动作构成的最小 oracle 序列而非最终答案来给 trajectory 打分。在七个能力划分上，GPT-5（high）以 42.1% 的 pass@1 总分领先，但在 Time 划分上得分为 0.0，且没有任何受评系统能在所有能力上全面领先。

## Tasks

1,120 个场景，横跨七个能力划分。其中五个为核心划分——Execution、Search、Ambiguity、Adaptability、Time——由 800 个不重复的、人工编写的场景构成，每个场景都配有自己的事件 DAG 与初始环境状态。余下两个 Noise 与 Agent2Agent 是施加在基础场景上的环境级增强：Noise 注入工具异常与无关的环境事件，Agent2Agent 则把 app 替换为 app-agent，主 agent 必须通过消息与之协作。标注者通过 ARE 标注界面在一个生成的移动世界中构建场景，把 write 动作与环境事件的 DAG 编写为 ground truth，随后经过多轮独立验证、自动化的结构性护栏，以及以基线 agent 做的事后难度校准。

## Domains

一个模拟的消费级智能手机环境，含十二个有状态的 app——消息、邮件、日历、联系人、文件、聊天、打车、购物、城市信息、租房以及一个系统 app——而非某个科学领域。

## Evaluation

- **面向 write 动作的 ARE Verifier。** Trajectory 被对照一条最小 oracle 序列检查，判定为目标导向而非路径最优：read 动作不限次数且不受惩罚，只有改变状态的 write 动作计入目标，且相互独立的目标不计次序。
- **四个验证维度。** Consistency（工具名称与调用次数必须匹配；对 ID 这类刚性字段用精确匹配，对自由文本字段用 LLM 评分标准，并带反作弊检查）、Causality（动作必须遵守依赖 DAG）、Timing（通过容差窗口强制）与 Completeness（成功要求匹配每一个 oracle write 动作）。
- **验证器的验证。** 在 450 条人工标注的验证 trajectory 上，ARE Verifier 达到 0.98 一致性、0.99 precision 与 0.95 recall，而仅用 in-context LLM judge 的基线为 0.72、0.53 与 0.83。验证器自身运行 Llama-3.3-70B-Instruct，温度为 0。
- **以成本为条件的打分。** 结果还以预算伸缩曲线的形式报告——只有在低于某个单场景美元预算上限时解出的场景才计入 pass@1，该上限从约 0.01 扫到 10 USD，定价取自第三方模型价格数据。
- **报告结果。** GPT-5（high）以 42.1% 的 pass@1 总分领先，其中 Execution 为 69.2、Search 为 79.6，但 Time 为 0.0；Claude-4-Sonnet Thinking 总分 37.8，Kimi-K2 以 20.1 领先开放权重模型。所有模型在 Time 上都低于 9 分，作者报告指令遵循与搜索已大体被解决，而鲁棒性、歧义消解与协作仍未解决。

## Typical Duration

场景在以下四者中最先发生者处终止：200 步、上下文溢出、验证完成、超时。模型在完整上下文长度下运行，每轮生成上限为 16,000 个 token，温度为 0.5，且每个场景运行三次以计入方差。由于环境按自己的时钟推进，评测框架会模拟生成耗时——在模型响应期间暂停，并以匹配的时间偏移恢复——从而使 wall-clock 延迟影响任务结果本身，而不只是影响成本。

## Main Contribution

一个把环境异步性变为 agent 评估中可打分维度的 benchmark，并配以一个针对 write 动作的验证器——作者将其呈现为一个独立、可复用的细粒度 credit assignment 与可验证奖励训练机制，其用途超出 Gaia2 本身。

## Key Design Ideas

- 事件驱动的环境按自身时钟推进，使时间意识与延迟成为被测量的失败模式，而非附带的成本项。
- 区分 read 与 write 动作：通过 read 动作的探索不限次数且不受惩罚，只有改变状态的 write 动作被计入，从而把信息收集与实际承诺区分开。
- 能力划分被设计为主导性的"风味"而非彼此正交的维度，并刻意决定不增设组合式划分——因为早期尝试人为组合三个及以上能力会产出不自然的任务，且缺乏清晰的评估信号。
- 面向 Noise 与 Agent2Agent 的环境级增强复用基础场景的标注，因为验证器检查的是状态变化而非特定的工具轨迹。

## Strengths

- 验证器是经过验证而非仅作宣称的：450 条人工标注 trajectory 上其一致性为 0.98，而仅用 LLM judge 的基线为 0.72，因此该 credit 信号带有一个可测的可靠性数字。
- 对照依赖 DAG 为 write 动作计功、而非匹配一条参考路径，既容许多种有效次序，又仍能捕捉缺失或因果错位的步骤。
- Time 划分在每个受评模型上都造成近乎全面的失败，尽管总分不低——从而单独暴露出一项被总体通过率完全掩盖的能力。

## Limitations

- Repository note: 该环境是一个模拟的消费级智能手机世界，因此这个 benchmark 衡量的是在毫无科学内容的领域中的异步协作能力；它的设计思路可迁移到科学场景，但它的任务不能。
- Repository note: 验证依赖人工编写的 oracle DAG，加上对自由文本字段使用的 LLM 评分标准，因此 ground truth 与部分打分都继承了标注者与 judge 的决策，且所报告的可靠性数字来自作者自建的验证集。

## Related Works

- [GAIA](./gaia.md) — 同样提出对人类简单而对模型困难的任务，但它在最终输出层面以精确匹配判定正确性——而这正是 Gaia2 作者所指出的、其动作级验证器要解决的局限。
- [TRACE](./trace.md) — 同样在最终结果之下为 trajectory 计功，但它聚合的是一个覆盖推理质量与效率的层级化效用函数，而非对照 oracle 依赖图检查改变状态的动作。
- [OSWorld](./osworld.md) — 同样对照真实环境状态为执行打分，但其操作系统是同步的，只在 agent 行动时才改变，而非按独立时钟推进。
