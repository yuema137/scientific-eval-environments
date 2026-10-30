# SAEScientist-Bench (2026)

> [English](../../works/saescientist-bench.md) | **简体中文**

> **首次公开：** 2026-09-08 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.09113)

## Overview

稀疏自编码器（SAE）可解释性研究通常由人来做：写探针文本，看字典里哪些特征被激活，再用 steering 检验候选特征。SAEScientist-Bench 把这个流程交给 agent。给定一个目标概念，比如“报税用语”，agent 设计对比文本，在 Gemma-2-9B-IT 的 Gemma Scope 字典（131,072 个特征）里查询，最后提交一个特征 ID。提交的特征会与 Neuronpedia 上的专家参考特征做对比，看三件事：它对这个概念激活得有多强，能不能把概念和对照文本区分开，以及用它做 steering 能不能把模型输出往这个概念上带。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?](https://arxiv.org/abs/2609.09113)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2609.09113v1>
- **Code:** <https://github.com/Trae1ounG/SAEScientist>
- **Venue:** arXiv 预印本（cs.AI、cs.CL、cs.LG，2026）；标注为 “Preprint. Work in Progress.”

## Summary

agent 在一个可写的工作区里工作，网络关闭，只有一个工具 `probe_sae`。每次请求最多传 64 段文本，工具返回激活最强的特征，或者对给定候选特征报告激活值和在整个字典中的排名。查多少次、什么时候停，由 agent 自己决定，限时 60 分钟。提交的特征会在固定的文本集上运行。Activation Rank 比较它与专家特征在正例文本上的平均字典排名；Activation Selectivity 为 100 × max(0, 2·AUROC − 1)，比较正例与困难负例和中性对照；Causal Steering 由 GPT-4o judge 分两轮、打乱顺序，给未干预输出、steering 后的输出和随机特征输出打分，只有 steering 后输出的目标相关性超过两个对照中较好的那个，才计分。总分是三项的简单平均。论文发现，agent 设计的对比文本还不错，但常常读错自己的测量结果。

## Tasks

在 Gemma Scope 残差流第 9 层和第 20 层上，共 17 个概念、20 个“概念 × 层”任务，涵盖语言（法语、德语、拉丁语、葡萄牙语、西班牙语、土耳其语）、文档格式（招聘启事、房产信息、天气预报）和领域概念（临床症状报告、药物剂量、考古发掘）；财报、投资组合配置和报税用语在两层都有。每个任务固定一个专家特征，能用公开 steering 预设的就直接采用，否则由专家用正例、困难负例和中性文本整理验证。

## Domains

语言模型的机制可解释性：在 Gemma-2-9B-IT 的 SAE 字典里找出单个特征。

## Evaluation

- **运行：** 10 种 agent 配置，每个任务跑三次，共 600 个计分轮次；多数模型用 Cursor，GPT-5.6 Sol 和 Luna 用 Codex，推理强度都设为 high。
- **专家参考：** 总分 85.56（Rank 100.00、Activation 98.92、Steering 57.75）。
- **各 agent 总分（Rank / Activation / Steering），三次平均：** Kimi K3 65.82（74.30 / 92.91 / 30.26）、Claude Opus 5 65.41（75.35 / 91.89 / 28.99）、Claude Sonnet 5 65.04（73.45 / 92.01 / 29.66）、Grok 4.6 62.93（67.21 / 90.11 / 31.47）、Claude Opus 4.8 62.57、Gemini 3.8 Flash 59.57、GPT-5.6 Sol 57.28、GPT-5.5 54.34、GLM-5.2 52.27、GPT-5.6 Luna 50.27。
- **规律：** 在选择性上 agent 已接近专家（最高 92.91，专家 98.92），差距最大的是 steering（最高 31.47，专家 57.75）。
- **失败分析：** 只有案例分析。例如在葡萄牙语任务里，agent 选中的特征在英语对照上的激活（4.50）比在葡萄牙语目标上（3.81）还高，总分只有 13.91。论文没有统计读错测量结果的次数。

## Typical Duration

每个任务限时 60 分钟，没有步数或 token 预算。所有运行加起来共调用探针 4,873 次。

## Main Contribution

一个 benchmark：拿 agent 找到的可解释性结果，与专家参考在相关性和因果两类标准上比较打分，而不是去评它写出来的解释。

## Key Design Ideas

- 交付物只是一个特征 ID，所以得分取决于对这个特征的测量，而不取决于 agent 的报告写得如何。
- 选择性用到困难负例和中性文本，对什么都激活的特征拿不到高分。
- steering 只有超过未干预基线和随机特征对照中较好的那个，才计分。

## Strengths

- 三项指标中有两项直接由激活值确定性地算出，每种配置跑三次，并报告标准差。
- 专家参考这一行让 agent 的分数有了同一把尺子。
- 探针接口固定且共用，不同配置之间唯一的差别就是 agent。

## Limitations

- 作者承认只覆盖一个模型、两层和一个固定的探针接口。
- 任务是针对给定概念找单个特征，不涉及多特征电路，也不涉及开放式的假设生成。
- steering 分数来自 LLM judge，没有经过人工验证；文本集和专家特征都是固定的。
- 没有下游的编辑或遗忘测试。
- Repository note：论文说不同运行之间的波动通常在 1–3 分以内，但表中总分的标准差有 5.42（Opus 4.8）和 7.40（Luna）。

## Related Works

- [EurekaBench](./eurekabench.md) — 同样对 agent 通过自己设计并运行的实验得出的结论打分。
- [FIRE-Bench](./fire-bench.md) — 同样评测 agent 在机器学习研究中的发现，并以已有结论为参照。
