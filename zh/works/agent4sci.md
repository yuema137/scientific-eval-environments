# Agent4Sci (2026)

> [English](../../works/agent4sci.md) | **简体中文**

> **首次公开：** 2026-10-20 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.28763)

## Overview

ML 工程类 benchmark 通常让 agent 在竞赛任务上拿一个好分数，参照物是排行榜，而不是某个科学领域已发表的最好水平。Agent4Sci 让每次运行都从一个经过核验的复现出发，复现的是某个科学 ML benchmark 上已发表的最佳模型，然后要求 agent 在 8 块 H200、12 小时内把它改得更好。提交的模型由另一个评测 agent 在封存的测试集上打分，还有一个审查 agent 检查轨迹里有没有钻空子。最终分数是相对已发表最佳结果的提升幅度。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)

## Activities

- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** [Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](https://arxiv.org/abs/2610.28763)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.28763v1>
- **Code:** <https://github.com/maszhongming/agent4sci>
- **Data:** <https://huggingface.co/datasets/MingZhong/agent4sci>
- **Venue:** NeurIPS 2026 Evaluations & Datasets Track（据 arXiv 备注）

## Summary

一个 benchmark 只有在标准化复现与原论文的主结果相差不超过核验过的容差时，才会被收录。agent 拿到这份复现以及训练数据（有验证集的也一并给出），但不能读取测试集，也不能在测试集上评估；hill-climbing 和评测分别在不同的容器里运行，数据划分是固定的。12 小时后，评测 agent 在封存测试集上运行 agent 提交的产物。对于越高越好的指标，分数为 Δ% = (s − b)/|b| × 100（越低越好的指标符号相反），其中 b 是复现出来的基线。审查 agent（默认是 Claude Opus 4.6）逐条检查轨迹里有没有选择性报告、测试集污染、操纵指标和硬编码；每个 agent 的运行有一半还会由另外三个模型家族重新审查，并辅以人工抽查。论文指出，大部分提升来自工程技巧，而不是研究层面的洞见；另外没有人类研究者的基线。

## Tasks

20 个 benchmark、25 个任务，覆盖 11 个领域，例如暂现源分类（ATAT）、σ8 回归（CosmoBench）、根据质谱检索分子（MassSpecGym）、DMS 突变效应预测（ProteinGym）、全拓扑潮流计算（PFDelta）和枯死树分割（TreeFinder）。benchmark 要过四道筛选：目标必须是科学领域；按数据、训练、基线、评测、许可等七项标准自动筛查；人工复核；再审查可复现性、任务针对性、代码库是否好用以及领域覆盖。在 NeurIPS 2025 Datasets & Benchmarks track 的 497 个候选里，这套流程只收录了 10 个；其余来自其他 ML 会议和领域期刊。

## Domains

天文（ATAT、Mars-Bench）、宇宙学（CosmoBench）、生物（SR-CACO-2 共聚焦超分辨）、基因组学（DART-Eval）、生物工程（ESCAPE、gRNAde、MOTIVE、ProteinGym、UniSite）、化学（CheMixHub、MassSpecGym）、生态（CarbonGlobe、TreeFinder）、地理（GEO-Bench-2、GTPBD）、地质（LITHOS）、神经科学（NeuroGraph）和物理（PFDelta，以及 TIDMAD 暗物质信号去噪），领域名称沿用论文的标注。

## Evaluation

- **指标：** 相对复现出的已发表最佳结果的带符号提升，由独立的评测 agent 在封存测试集上计算。
- **默认 agent（平均 Δ%）：** Claude Opus 4.6 10.4%、Claude Sonnet 4.6 9.6%、Gemini 3.1 Pro 6.8%、Codex（GPT-5.4）4.4%。每个 benchmark 上默认 agent 的最好结果都是正的，从 1.1%（ProteinGym）到 64.4%（PFDelta）；论文报告没有一次运行被判定为作弊。
- **轨迹分析：** 反复出现三类问题。一是对新颖性判断失准，把早已成熟的技术当成新想法；二是资源用不满，GPU 闲置、本可并行的实验被串行跑；三是早期有了一点进展后，就收缩到调超参和做集成上。超参调优在 Opus 的改动中占 56%，在 Codex 中占 44%，在 Gemini 中占 48%。
- **插入式 skill：** 三个 markdown skill，分别负责研究构思、实验管理和每小时一次的自查清单。加上之后，Opus 从 10.4% 提高到 20.1%（20 个 benchmark 中 18 个变好），Codex 从 4.4% 提高到 8.1%（20 个中 12 个变好）。正文没有对单个 skill 做消融。
- 论文把这些平均值当作逐个 benchmark 的探针，而不是排行榜，并指出不同运行之间有波动。TODO(reference)：每个 agent 的运行次数。

## Typical Duration

每次运行 12 小时、8 块 H200；Opus 平均每次 490 轮、338 次工具调用。附录在两个 benchmark 上报告了 3 天的运行。TODO(reference)：每次运行的 token 数和 API 成本。

## Main Contribution

一个长时程测试平台，衡量 agent 在固定算力下能把已发表的科学 ML 最佳模型改进多少；评测由另一个 agent 在留出数据上完成，作弊检查经过交叉审查。论文还做了轨迹分析，并针对发现的失败模式设计了插入式 skill。

## Key Design Ideas

- 基线是复现出来的已发表最佳结果，所以只要分数为正，就超过了该领域在这个 benchmark 上报告过的结果。
- hill-climbing 和测试评估在不同容器里进行，只有另一个 agent 能接触测试集。
- 作弊审查会跨模型家族交叉核对，并有人工抽查。
- skill 干预是针对轨迹中发现的三类失败模式设计的。

## Strengths

- 每个任务的起点都是一份与原论文数字核对过的复现。
- 除了分数，论文还量化了 agent 的行为：轮数、工具调用次数、各类改动的占比。
- skill 实验在相同的 benchmark 和预算下，对比了加与不加干预的结果。

## Limitations

- 作者列出的局限包括：没有人类研究者基线，只覆盖单 agent harness，留出验证不完美，hill-climbing 的范围有限，以及插入式 skill 可能过拟合（这些 skill 是针对 Claude Code 优化的）。
- 每个领域只有一到五个 benchmark，按领域得出的结论依据的任务很少。
- 作弊检测依靠 LLM 审查，只做了人工抽查，没有全面人工复核。
- Repository note：基线量级不同的指标之间，相对提升不能直接比较；论文是逐个 benchmark 报告，同时给出平均值。

## Related Works

- [MLE-bench](./mle-bench.md) — 同样在 ML 工程任务上给 agent 打分，但参照的是 Kaggle 排行榜，而不是已发表的科学基线。
- [AIRS-Bench](./airs-bench.md) — 同样是 20 个研究型 ML 任务组成的套件，但不提供基线代码。
- [Harness-Bench](./harness-bench.md) — 同样比较不同 harness 配置下的 agent 表现。
