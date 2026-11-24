# Autonomous Science Bench (2026)

> [English](../../works/autonomous-science-bench.md) | **简体中文**

> **首次公开：** 2026-10-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.18449)

## Overview

Autonomous Science Bench（ASB）把已发表的实验室实验改造成有预算限制的 design-build-test-learn campaign。Agent 从候选池里订购固定数量的实验批次，从一个 lab 服务拿回记录下来的测量值，最后提交一个预测模型。这个 benchmark 既不给书面报告打分，也不只看单个最好结果，而是要求两道独立的关卡都通过才算解决：已测批次里要有足够多有科学意义的 hit（discovery gate），提交的模型要能把留出的设计排好序（learning gate）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** [Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449)，Yibo Wen 与 Han Liu，2026 年预印本（v1 2026-10-13，v2 2026-11-16）。
- **Full text:** <https://arxiv.org/html/2610.18449v2>
- **Project:** <https://asb.open-ssi.org/>（版本 0.1，附 leaderboard）
- **Code:** <https://github.com/Open-SSI/autonomous-science-bench>（Apache-2.0；`github.com/Yibo-Wen/as-bench` 会重定向到这里）
- **Venue:** arXiv 预印本（cs.AI），2026 年

## Summary

每个 campaign 都以一项已发表的筛选实验为起点，整个设计池的测量值都是已知的。Agent 能看到 seed 数据和可订购的设计池，然后每轮通过 `asb` 命令行客户端提交一个批次。Lab 容器运行在内部网络上，负责检查请求（轮次顺序、批次大小、是否可订购、是否重复），只对接受的批次扣预算，把它们记进一个 agent 无法修改的账本，然后返回测量值：replay 后端返回原实验记录的值，digital-twin 后端返回来自原研究的隐藏代理模型给出的值。最后一轮结束后，agent 提交一个 JavaScript 的 `predict(design)` 函数，它在 sandbox 中运行，没有文件、网络、时钟、随机数，也拿不到标签。把分数拆成 discovery gate 和 learning gate，就能把「找到了好设计」和「学会了设计空间的模型」分开。在 180 次 trial 中，129 次未解决：29 次只差 discovery，34 次只差 learning，66 次两道都没过。

## Tasks

版本 0.1 有六个 campaign，生物、化学和材料科学各两个，每个都基于一项已发表的实验（论文 Table 2）：

| Campaign | Source | Backend | Rounds × batch | Pool | Budget / pool | Discovery gate | Learning gate |
|---|---|---|---|---|---|---|---|
| Nuclease | Thomas et al. 2025 | replay | 4 × 96 | 20,000 | 1.9% | ≥190 个 hit 且 ≥175 个 family | NDCG@100 ≥ 0.42 |
| Biosensor | Wang et al. 2025a | replay | 3 × 10 | 677 | 4.4% | ≥21 个选择性 hit | NDCG@20 ≥ 0.70 |
| Propylene | Kim et al. 2025 | twin | 3 × 20 | 736 | 8.2% | ≥7 个 hit | NDCG@20 ≥ 0.52 |
| Suzuki | Perera et al. 2018 | replay | 4 × 48 | 2,764 | 6.9% | ≥32 个 standout | NDCG@100 ≥ 0.37 |
| OER | Rohr et al. 2020 | replay | 4 × 48 | 3,419 | 5.6% | ≥55 个 standout，每个 library ≤28 个 | NDCG@100 ≥ 0.55 |
| Coercivity | Wang et al. 2022 | replay | 4 × 16 | 604 | 10.6% | peak score ≥ 0.60 | NDCG@20 ≥ 0.65 |

每个 campaign 的专家耗时估计为 8 到 12 小时。按表中顺序，留出评估集分别包含 5,000、332、244、1,844、5,039 和 307 个设计。

以 coercivity campaign 为例走一遍。底层数据是一组 Co–Fe–Ni 薄膜成分梯度样品，共 921 个成分，测了矫顽力和 Kerr 旋转。Agent 一开始拿到 10 个分布在成分三角形各处的 seed 成分，从 604 个候选中分四轮、每轮订 16 个，最后提交的预测器在 307 个留出成分上评分。矫顽力分布有两个峰（矫顽力 ≥ 8 mT 的连续区域，且最大值 ≥ 9.5 mT），但峰的个数不会告诉 agent。Discovery 分数的一半来自在覆盖较少的那个峰里找到的 standout 比例，所以如果只围着文献中已知的那个峰订购，最多只能拿 0.25，而门槛是 0.60。

## Domains

生物（nuclease 和 biosensor campaign）、化学（基于 digital twin 的 propylene campaign；Suzuki 偶联 campaign）以及材料科学（析氧反应 library；Co–Fe–Ni 薄膜矫顽力）。Coercivity 以外各 campaign 的科学细节为 TODO(reference)。

## Evaluation

- **Discovery gate：** 对 agent 已测集合计算一个统计量，与校准过的门槛比较，通常是超过某个有科学意义标准的 hit 数。"Standout" 指在组内按排名定义的 hit。Nuclease 取 hit 比例和 family 比例中较小的那个；coercivity 用上面说的双峰分数。
- **Learning gate：** 在留出集上计算提交的 `predict` 函数的 NDCG@k，相关度为 max(真实分数 − τ, 0)；NDCG@k 达到这个 campaign 的门槛即通过。
- **判定规则：** 两道关卡都通过才给 reward 1。
- **校准检查：** 什么都不做的 agent 必须得 0 分，参考解法必须能解决所有 campaign，不做任何测量的预测器必须过不了 learning gate。一个按 biosensor 目录直接计数的做法在 30 个划分中有 2 个两道关卡都通过了。
- **Pilot（v2）：** 10 个 agent-模型配置，每个 campaign 跑 3 次 trial，共 180 次，解决 51 次。GPT-6 Astra（Codex）解决 13/18（72%），Opus 5.5（Claude Code）12/18（67%），GPT-5.6 Terra 8/18（44%），Muse Wonder（Muse Code）7/18（39%），GPT-5.6 Luna 5/18（28%），Sonnet 5.5 和 GLM-5.3 Flash 各 2/18，Qwen3.8 27B 和 MiniMax M3 各 1/18，Haiku 4.5 为 0/18。最难的是 coercivity（30 次中解决 5 次），解决最多的是 OER（13/30）。
- **成本：** 18 次 trial 的总成本从 $6.91（GPT-5.6 Luna）到 $190.22（GPT-6 Astra）不等；每次成功解决的成本为 $1.38（Luna）、$6.45（Terra）、$14.41（Opus 5.5）和 $14.63（GPT-6 Astra）。
- **两道关卡的相关性：** 归一化后的 discovery 分数与 learning 分数之间的 Spearman 相关系数，在全部 180 次 trial 上为 0.47，在单个 campaign 内为 0.42 到 0.75。

## Typical Duration

每次 trial 上限 8 小时，以 Harbor task 形式在本地 Docker 上运行（Harbor 0.21.0；Muse Code 的 trial 用 0.25.0）。报告的 18 次 trial 总 agent 时间从 1.5 小时（Haiku 4.5）到 28.4 小时（GLM-5.3 Flash）不等。没有报告 token 数。

## Main Contribution

一个闭环发现 benchmark：agent 在一个 lab 接口上花掉固定的实验预算，按 discovery 和学到的预测能力两项独立结果打分；lab API 的设计让同一个 campaign 以后可以换成 digital twin 或真实实验室来运行。

## Key Design Ideas

- 实验账本和预算归 lab 管，不归 agent 管；被拒绝的请求不扣预算，已接受的任务不能修改。
- 每个 campaign 两道关卡：已测批次中的 hit，以及 sandbox 中预测器在留出设计上的 NDCG@k。
- 设计关卡时就堵住捷径。例如 nuclease 数据里有两列已发表数据和答案很接近，benchmark 不把它们给 agent；coercivity 则用双峰评分。
- 同一个 Lab API 后面有三档后端：replay（五个 campaign）、digital twin（一个 campaign），以及只定义了接口的真实实验室后端。
- 为真实实验室后端提出了一个自适应预算调度器（v0.1 中未评估）。

## Strengths

- 关卡拆分本身就有诊断作用。各 campaign 的失败计数显示，例如 propylene（v1）的 19 次未解决 trial 中有 16 次只差 learning，而 coercivity 的失败大多两道关卡都没过。
- 空操作、参考解法和零测量三组对照检查了每道关卡都能按预期被通过和被卡住。
- 每个配置都在解决率旁边报告了成本和 agent 时间。

## Limitations

- 作者把规模（三个领域共六个 campaign）列为局限，并指出 replay 和 twin 后端把设计空间限制在已记录或已模拟的设计之内。
- 已发表数据可能被模型记住，或者在出网控制失效时，在 trial 过程中被检索到；作者表示出网控制会屏蔽已知的答案来源。
- v0.1 中真实实验室后端只有接口，没有评估任何真实实验室 trial。
- Muse Wonder 的成本是按 token 数和标价估算的，Muse Code 也无法固定版本。
- 项目 leaderboard 注明，每个任务只跑三次 trial，配置之间的小差距目前还说明不了问题。
- Repository note: 论文 v1 报告的是 8 个配置共 144 次 trial（最好 67%，最难的 campaign 为 3/24）；v2 加入了 GPT-6 Astra 和 Muse Wonder。官方仓库 README 仍显示 v1 的统计（144 次中解决 31 次），其 campaign 表列出了七个 campaign，而结果描述的是六个。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — 同样把科学 agent 任务打包成容器化的 Harbor 风格任务，但用的是单次会话的程序化验证，而不是多轮实验预算。
- [DiscoveryBench](./discoverybench.md) — 同样面向数据驱动的发现，但基于固定数据集，而不是由 agent 自己选择实验批次。
- [RE-Bench](./re-bench.md) — 同样在明确的预算下比较 agent，但场景是 ML research engineering，而不是从湿实验数据改造来的 campaign。
