# Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities (2025)

> [English](../../works/enhancing-agentic-autonomous-scientific-discovery.md) | **简体中文**

> **首次公开：** 2025-11-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2511.14631)

## Overview

一个面向数据驱动科学发现的 10 任务 benchmark——题目以宇宙学功率谱和分子谱线问题为主——外加一个视觉语言「plot judge」：它按动态生成的领域专属评分细则给 agent 画出的图打分，再把判定结果作为自我纠正信号回灌给 agent。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2511.14631>
- **Code:** <https://github.com/CMBAgents/cmbagent>
- **Venue:** arXiv preprint (cs.CL, cs.AI, cs.CV, cs.MA), 2025

## Summary

这项工作针对 agentic 科学发现中的一个特定盲区：只看得到文本和堆栈回溯的编码 agent，无从察觉拟合曲线漏掉了某条谱特征，也看不出功率谱的峰结构不对——这类失败只在图上才显形。作者在 cmbagent 多智能体系统中加入一个视觉语言模型作为验证检查点：先由一个 GPT-4o 模型把自然语言任务提示拆解成一份可逐条核查的视觉判据清单，再由具备视觉能力的 judge 仅对照该清单检查产出的图、全程看不到代码，最后给出「continue」或「retry」判定，驱动 agent 修改。为衡量这样做是否有帮助，作者构建了一个含 10 个数据驱动发现问题的 benchmark，数据集由他们自行生成，并在三个编码 agent 上报告纯代码基线、文本反馈变体与 VLM 反馈变体的 pass@1。

## Tasks

10 个任务，数据集均由作者生成，分为四组：谐振子动力学（2 个任务——区分阻尼振子与啁啾振子）；分子谱线建模（3 个任务——双高斯轮廓、自吸收、超精细结构）；SEIR 传染病模型（2 个任务——免疫衰减与行为反馈）；宇宙学功率谱（3 个任务——错误的谱指数、EE 谱、错误的哈勃常数）。每个任务给出一份数据集和一段自然语言提示；成功的定义是 agent 发现了数据中的目标特征，也就是识别出正确的底层模型。任务的具体设定见论文附录 A。作者表示，跨领域的分布是刻意安排的，为的是不让评测偏向某一个领域。

## Domains

天文学是主领域：十个任务中有六个属于天文——三个宇宙学功率谱问题（CMB 谱指数、EE 偏振谱、哈勃常数），以及三个来自天体化学的分子谱线建模问题，其建模对象是带自吸收和超精细结构的天文谱。物理学通过两个谐振子动力学任务成为共同领域。两个 SEIR 传染病任务不属于这两个领域中的任何一个，它们是刻意设置的领域外对照，而非作者主张的领域贡献。

## Evaluation

报告指标是 pass@1，定义为系统单次运行即正确走完整个工作流的概率，成败取决于系统是否识别出数据中正确的底层模型。报告结果：纯代码基线的 pass@1 为 0.2–0.3；只带文本反馈的 cmbagent 为 0.4–0.5；带 VLM 反馈的 cmbagent 为 0.7–0.8。最佳配置是 cmbagent 搭配 GPT-4.1 编码 agent 与 Gemini 2.5 Pro 视觉 judge，pass@1 为 0.8。参与比较的编码 agent 有 Gemini 2.5 Pro、GPT-4.1 与 Claude Opus 4.1；judge 与 critic 模型为 GPT-4o 与 Gemini 2.5 Pro，各有纯文本与带视觉两种变体。循环内的 plot judge 本身不做数值打分——它对照评分细则返回「continue」或「retry」/「explore」的二值判定。论文未说明这些 pass@1 数字背后跑了多少次试验；完整结果表的逐格数值记为 `TODO(reference)`。

## Typical Duration

N/A — 任何实验都没有报告运行时长、wall-clock、token 或成本统计。作者只提到每次试验的计算开销都很大，这也是他们只报告单次运行 pass@1、而不做重复试验的理由。

## Main Contribution

把视觉语言验证引入自主发现循环，作为其中的一个检查点——图被当作可验证的工件，对照自动生成的任务专属评分细则打分；配套给出一个 10 任务的数据驱动发现 benchmark，在其上 VLM 反馈把 pass@1 从纯代码的 0.2–0.3 提升到 0.7–0.8；judge 还留下可审计的推理轨迹，使 agent 的自我纠正决策变得可查。

## Key Design Ideas

- 评分细则按任务现场生成，而非固定不变：一个 GPT-4o 模型把自然语言提示中的科学要求拆解成一组可核查的条目。
- 细则用 Pydantic schema 表达，把静态字段（视觉清晰度、完整性、呈现质量）与动态生成的科学准确性判据结合起来。
- plot judge 只对照细则评判图，不参考底层代码，因此一张「碰巧看着对」的图不会因为源码读起来合理而被放过。
- judge 输出的是二值控制判定（「continue」对「retry」/「explore」）而非分数，可以直接用作循环控制信号。
- 同一个 VLM 信号既用于纠错，也用于把探索性分析引向信息量更大的方向，不只是把关准入。
- 消融按三档展开：纯代码、文本反馈、视觉反馈；隔离出的是视觉通道相对文本自我批评的增益，而不是相对完全没有反馈的增益。
- 任务领域刻意越出宇宙学，延伸到谱线建模、振子动力学与流行病学，使增益不能被归因于底层系统在宇宙学上的专门调优。

## Strengths

- 消融的对照是文本反馈而非无反馈，因此报告的增益可以专门归因于视觉通道（纯文本 0.4–0.5，VLM 反馈 0.7–0.8）。
- 评分细则由每个任务自己的提示派生，而不是套用固定清单，判据因此贴合具体科学问题的要求。
- 对 plot judge 隐藏代码堵住了一处明显的泄漏：否则一段看似合理的脚本会替一张错图开脱。
- 任务横跨四个问题族，其中两个刻意落在作者自己的宇宙学专长之外，降低了结果只是对单一领域调优的风险。
- judge 会产出可审计的推理轨迹，循环内部的接受 / 重试决策因此可查而非不透明。
- 比较覆盖三个编码 agent 与两个 judge 模型，而不是单一的系统组合。

## Limitations

- 作者把 pass@1 结果称为初步的概念验证，并表示统计上严格的评估要等更大的 benchmark 和更多算力。
- 只报告了单次运行的评估，作者将此归因于模型组合的组合空间以及每次试验的开销。
- Repository note: 10 个任务是一个非常小的套件，且 pass@1 的区间报告时既无逐任务拆分也无置信区间，一个任务的差别就会让报告分数移动 0.1。
- Repository note: 论文没有提及是否公开 benchmark 任务或数据集；只有 cmbagent 框架被说明为开源，因此该 benchmark 作为独立工件的可复用性尚未确立。
- Repository note: 通过与否似乎由作者根据是否复原出正确的底层模型来判定，文中没有描述独立的人工评审组或自动检查器，因此打分流程比它所衡量的循环内细则机制更不形式化。
- Repository note: VLM judge 既是受评系统的一部分，又是被研究的机制本身，因此这项比较衡量的是新增一个组件带来的价值，而不是提供了一个第三方可以拿去评测其他 agent 的 judge。

## Related Works

- [CosmoPaperQA](./cosmopaperqa.md) — 出自同一研究组、同一 cmbagent 谱系，评测的是文献检索准确率而非数据驱动的模型发现。
- [SciVisAgentBench](./scivisagentbench.md) — 同样为 agent 产出的科学可视化打分，但把它当作最终交付物，而非循环内的验证检查点。
- [BLADE](./blade.md) — 开放式数据驱动分析上最接近的对应物，评判 agent 在科学数据集上做出的分析决策。
- [Stargazer](./stargazer.md) — 天文模型拟合评测，每次提交都给出逐判据反馈，是径向速度数据上一种可比的「反馈进循环」设计。
