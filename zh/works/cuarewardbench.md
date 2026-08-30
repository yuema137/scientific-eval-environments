# CUARewardBench (2025)

> [English](../../works/cuarewardbench.md) | **简体中文**

> **首次公开：** 2025-10-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2510.18596)

## Overview

CUARewardBench 是一个把 outcome reward model（ORM）与 process reward model（PRM）本身作为被评判对象的 benchmark，用于检验 vision-language model 能否复现专家对 computer-using agent trajectory 的判定。它在来自七个 policy model、成功率跨越 25.9–50.8% 的 OSWorld rollout 上，配套了 272 条 trajectory 成功标注与 346 条 step 正确性标注。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2510.18596>

## Summary

CUARewardBench 提出，面向 computer-using agent 的脚本式验证器扩展性差且无法评估单个 step，而被提议取而代之的 VLM 式 reward model 在很大程度上仍未经检验。它从 OSWorld-verified rollout 中筛选出经专家标注的 trajectory，并在三套已公开的 CUA reward prompt 模板下，把七个 vision-language model 同时作为 outcome 与 process reward model 进行评测。最佳单一配置在 trajectory 级判定上达到 82.9% precision 与 80.1% 总体准确率，作者提出的 Unanimous Prompt Ensemble 通过仅在全体成员一致时才给出判定，把 precision 提升到 89.8%、NPV 提升到 93.3%。

## Tasks

272 条标注 trajectory（139 条成功 / 133 条失败）与 346 个标注动作（182 个 good action / 164 个 bad action），取自预先收集的 OSWorld-verified rollout，覆盖全部十个 OSWorld 任务类别以及七个 policy model 的十种配置。筛选保持类别与成功–失败的平衡，剔除没有任何 agent 解出的任务以及八个及以上配置都能解出的任务，并只接受步数少于 25 步的 trajectory；标注随后由人工完成，而非取自 OSWorld 的验证脚本。论文称标注为专家工作并经过多阶段质量控制，但未给出标注者人数，也未给出标注者间一致性数值。

## Domains

Ubuntu 桌面计算机操作，覆盖十个 OSWorld 软件类别：Chrome、Thunderbird、LibreOffice Writer/Calc/Impress、VS Code、GIMP、VLC、OS 操作与多应用工作流。

## Evaluation

- **结果 reward model（ORM）。** reward model 读取指令与 trajectory 的截图序列，预测二值的 trajectory 成功与否，并与人工 trajectory 标注对照评分。
- **过程 reward model（PRM）。** 同一批模型对单个已标注动作预测二值正确性，并与人工 step 标注对照评分。
- **Precision 与 NPV 为主要指标。** Precision = TP/(TP+FP) 与 NPV = TN/(TN+FN) 被视为 reward 可靠性，recall = TP/(TP+FN) 与 specificity = TN/(TN+FP) 作为次要的采样效率指标报告。
- **Unanimous Prompt Ensemble (UPE)。** 多个 VLM 与 prompt 模板的组合进行投票，仅当全体成员一致时才对样本给出判定，否则弃权。
- **报告结果（表 4 与表 5）。** 使用 SE-WSM prompt 的 GLM-4.5V-106B 是论文中表现最佳的 ORM，达到 82.9% precision、77.6% NPV 与 80.1% 总体准确率，同一组合作为 PRM 时为 69.5% / 64.2% / 66.9%；UPE 在 ORM 上达到 89.8% precision 与 93.3% NPV，在 PRM 上为 81.7% 与 85.1%。论文未报告人类 baseline。

## Typical Duration

入选 trajectory 的步数少于 25 步，其来源 rollout 是在 OSWorld 上以 15 步与 50 步的 agent 上限生成的。未说明：论文没有给出 reward model 自身判定过程的 wall-clock 或 token 预算。

## Main Contribution

一个用于评测 computer-using agent trajectory 上 outcome 与 process reward model 的专家标注 benchmark——论文称其为首个同时覆盖 trajectory 级与 step 级 CUA reward 评测的工作——并配套了基于其发现提出的 Unanimous Prompt Ensemble 方法。

## Key Design Ideas

- 在同一 trajectory 池上设置两层标注：二值的 trajectory 成功，以及被单独挑选出的动作的二值正确性。
- 关键动作的挑选面向那些既能推进任务又不显而易见的 good action，以及那些看似合理却妨碍任务的 bad action；冗余动作为保证标注客观性而基本被排除。
- trajectory 筛选在一个难度区间内保持类别与成功–失败的平衡，剔除没有任何 agent 解出的任务以及八个及以上配置都能解出的任务。
- reward model 的实现被拆解为 VLM × prompt 模板两个维度，复用了来自 ZeroGUI、OpenCUA 与 SE-WSM 的三套已公开的开源 CUA reward prompt。

## Strengths

- trajectory 成功由人工标注而非直接取自 OSWorld 的验证脚本，使标签独立于这些 reward model 意在取代的脚本式验证器。
- trajectory 来自七个成功率跨越 25.9–50.8% 的 policy model，因此所呈现的失败模式并非单一 agent 设计所独有。
- bad action 在成功 trajectory 内被标注，good action 在失败 trajectory 内被标注，从而把 step 级判定与结果级判定分离开。

## Limitations

- Repository note: 只有挑选出的关键动作带有 step 正确性标签——272 条 trajectory 上共 346 个，且冗余动作基本被排除——因此 PRM 分数衡量的是对刻意设置的关键或迷惑性步骤的判定，而非对整条 trajectory 逐步的均匀准确率。
- Repository note: UPE 是以成员意见不一致即弃权换来 precision 与 NPV 的提升，覆盖率代价很大——ORM 的总体准确率为 59.9%，而论文按 precision 认定为最佳的那个配置为 80.1%，PRM 的 specificity 为 24.4%，而该配置为 67.7%；论文没有在真实的 RL 训练回路中验证该方法。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在最终任务成功之下分配 credit，但依靠环境内已标注的 subgoal 进展，而非检验 reward model 能否复现人工的 step 判定。
- [TRACE](./trace.md) — 同样评估 trajectory 而非最终答案，但对 agent trajectory 按多维评分标准打分，而非评估发出此类判定的 judge。
