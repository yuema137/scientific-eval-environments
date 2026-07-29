# QVal (2026)

> [English](../../works/qval.md) | **简体中文**

## Overview

QVal 是一个 training-free 的评估方法学与 testbed，通过稠密监督（dense supervision）信号在多大程度上能按强 reference policy 的 Q 值排序 agent 的候选 action，来为这些信号打分。它被实例化为 QVal-v1.0，在四个环境与六个开放权重模型 backbone 上，对来自七个方法学家族的 21 个稠密监督方法做 benchmark。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.32034>
- **Project:** <https://q-val.com>
- **Code:** <https://github.com/bethgelab/qval>

## Summary

QVal 针对的是这样一种常见做法：通过集成了稠密监督方法的训练流水线的下游表现来评估这些方法；作者认为它代价高昂，把监督质量与训练工程上的混杂因素纠缠在一起，并使需要不同训练设置的方法学家族之间无法比较。给定一个 state-action 对，QVal 度量某方法的分数是否 Q 对齐——即它是否像强 reference policy 的 Q 值那样排序 action——从而使信号可以在任何训练运行之前就被比较。QVal-v1.0 覆盖 21 个稠密监督方法、七个方法学家族、四个环境与六个开放权重模型 backbone，共超过 1.2K 次评估实验，并发现简单的 prompting baseline 一致优于文献中较新的稠密监督方法。

## Tasks

受测单元是七个方法学家族——ranking、direct、intrinsic scoring、self-distillation、pre-trained、embedding 与 code——中的 21 个稠密监督方法，它们在取自四个环境的带标注 state-action 对上被打分。状态取自每条已收集 trajectory 的中段区间，排除过早与过晚的状态；每个状态配有四个候选 action：trajectory 自身的 action 加上三个采样得到的替代 action。逐环境的样本量列在附录表中，而非正文。

## Domains

目标导向导航、具身推理、基于浏览器的计算机操作与终端问题求解——FrozenLake、ALFWorld、OpenApps 与 TerminalBench，其中 TerminalBench 仅有文本，其余同时提供文本与视觉观测。

## Evaluation

- **Q-alignment。** 当一个方法的分数是参考 Q 值的严格单调递增变换时，该分数即为 Q 对齐的，因而它在某个状态上对候选 action 的排序与参考值完全一致。
- **Spearman's ρ。** 主指标，既在全局报告，也逐状态计算后在各状态上取平均；Kendall's τ 在附录中报告。
- **参考值。** reference policy 因环境而异：FrozenLake 与 OpenApps 用脚本化的最优策略，ALFWorld 用专家 planner，而 TerminalBench 因最优策略难以求得，改用以 GPT-5.5 为 backbone、k = 16 的 Max-Value Monte-Carlo rollout 来估计。为给一个点打标签，需把环境恢复到记录下的状态，强制第一步续接为数据集中的 action，再按 reference policy 继续并记录折扣回报。
- **鲁棒性检查。** 文本–图像观测对比、Q 值与状态值目标对比，以及在 TerminalBench 标签上以 GPT-5.5 与 Claude Opus 4.7 作为 Monte-Carlo backbone 的对比，后者给出的方法相关性高度接近。
- **报告。** ranking 与 direct prompting 在各环境与各 backbone 上都取得最高的 Q 对齐程度；在同一家族内部，更复杂的变体并不能可靠地提升 Q 对齐；direct prompting 类方法在所有环境上都保持为正，TerminalBench 亦然。数值化的相关系数由图给出，正文并未列出。

## Typical Duration

在一组固定的带标注 state-action 对上做离线打分，无需任何训练运行。未说明：论文未给出运行一次 QVal 的 wall-clock、步数或 token 预算，也未报告成本数字。

## Main Contribution

一种 training-free 的方法学，通过 Q 对齐——即方法的分数在多大程度上能按参考值排序中间 action——来评估稠密监督方法，从而把一个此前需要一次训练运行才能回答的问题变成廉价的离线评估。

## Key Design Ideas

- 以 Q 对齐为评估目标：一个信号由它是否像参考 Q 值那样排序候选 action 来判定，而不是由训练流水线的下游表现来判定。
- 因环境而异的 reference policy：FrozenLake 与 OpenApps 用脚本化的最优策略，ALFWorld 用专家 planner，TerminalBench 用以 GPT-5.5 驱动的 Max-Value Monte-Carlo rollout。
- 通过环境恢复来打标签——回放到记录下的状态，强制执行数据集中的 action，再按 reference policy 继续并记录折扣回报。
- 各方法共用固定的 backbone 与完全相同的上下文——任务描述、环境动态、奖励说明，以及状态空间与动作空间的描述——使 Q 对齐上的差异反映打分方法本身而非模型。

## Strengths

- 把信号质量与训练流水线工程分离开来，使需要不同训练设置的方法学家族能在同一基准上比较。
- 每个 state-action 对输出单一分数就是新方法需要满足的全部接口，这让该 testbed 能廉价地扩展到更多方法与环境。
- 在各方法之间固定 backbone 与所提供的上下文，把打分信号与底层模型自身的能力隔离开来。

## Limitations

- Repository note: 论文自身的讨论指出，信号质量并非影响 RL 后训练效果的唯一因素，也不与流水线的其余部分相互隔离，因此高 Q 对齐分数本身并不能确立某个信号一定会改善训练运行。
- Repository note: 数值化的 Spearman 与 Kendall 数值由图与附录给出而非正文，逐环境的样本量也列在附录表中——因此本卡片以定性方式而非数字记录其主要结论。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在最终任务成败之下分配 credit，但依据的是 agent benchmark 内人工标注的子目标进展，而非用来给外部打分方法排序的参考 Q 值。
- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — 同样在长 horizon 任务上产生稠密的中间奖励，但方式是给 benchmark 自身定义的子任务分级评分，而非评判第三方的监督方法。
- [TRACE](./trace.md) — 同样把中间 trajectory 内容当作一等的评估对象，但用 hierarchical utility 函数为整条 deep research trajectory 打分，而非在单个状态上给候选 action 排序。
