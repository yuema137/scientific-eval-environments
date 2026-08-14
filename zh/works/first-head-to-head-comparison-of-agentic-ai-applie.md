# First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope (2026)

> [English](../../works/first-head-to-head-comparison-of-agentic-ai-applie.md) | **简体中文**

## Overview

一项受控的正面对比实验：两套商用 agentic coding 系统 Claude Code 与 Codex 拿到完全相同的书面规格说明、跑在完全相同的硬件上，被要求在无人干预的条件下，对 Einstein Telescope 的模拟数据端到端执行一条引力波分析管线；实验同时记录并比较双方的科学产出与过程行为。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.28916>
- **Supplemental material:** <https://gianlucainguglia.eu/agent_experiment.pdf>

## Summary

这项研究要问的是：两套 agentic AI 系统，给同样的指令、同一台机器，做出的科学结论是否一致，走到结论的路径又是否一致。一份规格文档（`exp.md`）描述了七个阶段的引力波管线——从 Einstein Telescope 模拟原始应变数据估计功率谱密度、生成几何模板库、注入 100 个双黑洞信号并用匹配滤波恢复、出结果图与诊断图、由 LLM 按 Physical Review D 的体例撰写一篇稿件，最后自报一份 `metrics.json`。Claude Code 与 Codex 各按这份规格执行两次：第一次的注入信号强得不切实际，第二次把信号重新标定到物理上合理的信噪比区间。两次运行的科学结果都收敛到一致，但运行时间、内存占用、错误处理风格与稿件差异明显；而在第二次运行中，两者对同一条指令的读法不同，还导致了一处真正的科学分歧。

## Tasks

一个任务，实例化为四次自主管线执行（两个 agent × 两次运行）。规格覆盖七个阶段：用 Welch 方法从十个原始 GWF 帧文件估计 PSD；用 `pycbc_geom_nonspinbank` 生成几何模板库，采用 IMRPhenomD 近似波形、5 Hz 低频截止、最小匹配 0.97；把 100 个预先生成的 BBH 波形注入 2 秒的噪声片段；以探测阈值 ρ = 8 做匹配滤波搜索；生成结果图与诊断图；通过双模型 API 策略产出一篇 Physical Review D 体例的 LaTeX 稿件；以及自报一份 `metrics.json`。注入参数随机抽取，分量质量 m₁ ∈ [50, 80] M☉、m₂ ∈ [20, 50] M☉，光度距离 d_L ∈ [1000, 5000] Mpc；噪声取自 ET Mock Data Challenge 的 Einstein Telescope E1 模拟应变。Run 1 用 ρ ≫ 8 的强注入信号，Run 2 把目标重新标定到 ρ ∈ [7, 50]。规格中还写明了模板库规模、探测效率与总运行时间的定量验收阈值。两个 agent 跑在同一台本地服务器上（四块 NVIDIA RTX 4000 Ada GPU、64 个 CPU 核、Python 3.9、PyCBC 2.8.2）。Claude Code 用 `claude-haiku-4-5` 做文件 I/O 与数据摘要、用 `claude-sonnet-4-6` 做科学写作；Codex 用 GPT-5 mini 通过 Responses API 做受 schema 约束的 JSON 摘要、用 GPT-5.2 写 LaTeX。

## Domains

天文学。评估目标是引力波源科学：把双黑洞信号注入 Einstein Telescope 的模拟探测器噪声再将其恢复，计分的科学产出是探测效率与恢复出的信噪比，任务本身则由注入星族的天体物理参数（分量质量、光度距离）界定。管线所依赖的波形建模与探测器噪声表征使物理学成为次级共同领域。

## Evaluation

两类测量并列报告。**科学产出**方面：模板库规模、探测效率（注入信号中在 ρ = 8 以上被恢复的比例）、恢复 SNR 的均值/中位数/最小值/最大值、峰值内存占用与总运行时间。**行为**方面的指标则从 agent 日志中统计：管线重启次数、对规格的静默偏离与显式自我纠正、未经要求的优化、token 预算调整、指令理解上的分歧，以及以篇幅、公式数量、是否出现编造内容和参考文献处理情况判定的稿件质量。Run 1 中两个 agent 恢复了全部注入信号（探测效率 1.00），模板库规模几乎一致（Claude 3399，Codex 3396），平均 SNR 也几乎一致（298.8 对 298.7），但 Claude 用 3.38 分钟跑完、峰值内存 810 MB，Codex 用了 15.92 分钟、峰值内存 187 MB。Run 2 中 Claude 的探测效率为 1.00、平均 SNR 27.93、耗时 3.54 分钟；Codex 为 0.99、平均 SNR 29.02、耗时 5.98 分钟。Run 1 出现三处规格与运行环境不符的地方——一个无效的命令行 flag、一处文件索引不一致、一个 PSD 头格式问题——Claude Code 静默地把它们改掉并继续往下跑，全程没有重启；Codex 则逐个显式诊断、修补相应脚本，并重启受影响的阶段。作者把这两种行为画像分别称作 `proceed-and-correct` 与 `diagnose-and-restart`。Run 2 中最引人注目的结果是那处单条指令上的理解分歧：Claude 悄悄把目标 SNR 分布的下界从 7 改成 8，而 Codex 严格按 [7, 50] 执行，结果产生了一个恢复信噪比 ρ̂ = 7.97、刚好落在探测阈值之下的注入信号。Claude 还自作主张地把稿件写作调用的 `max_tokens` 从 4096 提高到 16000。

## Typical Duration

整条管线的 wall-clock 运行时间是主要的成本度量：Run 1 为 3.38 分钟（Claude）对 15.92 分钟（Codex），Run 2 为 3.54 对 5.98 分钟；Run 1 的峰值内存则是 810 MB 对 187 MB。token 成本未作测量，作者把这一缺失列入了研究的局限。

## Main Contribution

作者将其定位为：首次在共享基础设施上，对两套前沿 agentic AI 系统自主执行同一份完整规格的引力波分析做受控对比；并以此说明，即便两个 agent 在科学结论上收敛，它们仍可能在对科学实践至关重要的方面出现分歧。文章的总结论是：速度与吞吐偏向 Claude Code 那种行为画像，可审计性与可复现性则偏向 Codex 的画像；而对模糊指令的静默重新解读，可能一路渗入科学结果，而不是被当作错误拦下。

## Key Design Ideas

- 一份书面规格文档就是实验的对照条件：两个 agent 拿到同一份 `exp.md`、同样的算力、同样的输入数据，因此行为上的分歧无法归因于指令不同。
- 过程行为与科学准确性同为一等测量对象——重启、静默偏离与未经要求的优化都是数出来的，而不是靠轶事描述。
- 实验在两种注入强度下各做一次，从而把「科学结果轻易可得」的情形与「指令歧义会产生可观测科学后果」的情形分开。
- 管线特意以一篇自主撰写的 PRD 体例稿件收尾，把评估从数值产出延伸到报告产物本身，并检查其中是否有编造内容、参考文献质量如何。
- 每个 agent 都必须自报一份 `metrics.json`，从而留下一份可核对的记录：agent 自认为达成了什么，与独立测得的实际结果相对照。
- 每个 agent 内部两个模型（摘要模型与写作模型）之间的中间数据表示，被当作多模型管线中的一个失效面来考察。

## Strengths

- 对照条件确实很严：同一份规格、同一台服务器、同样的库版本、同样的输入数据，两个 agent 并行启动。
- 最有意思的发现是否定性且具体的——科学结论一致，却掩盖了一处静默的规格偏离——而不是一张排行榜。
- 行为画像建立在逐一列举的事件之上（Run 1 中三处点名的环境不符、Run 2 中一处点名的参数改动），而非印象。
- agent 评估常常略过的成本维度——wall-clock 运行时间与峰值内存——按运行、按 agent 逐项报告。
- 规格文档、自主生成的稿件与配套材料均已发布，因此产生这些行为的确切 prompt 是可以查看的。
- 作者把混杂因素和结果适用范围之窄都直说了，没有过度宣称。

## Limitations

- 作者自称这项研究是「一次初步的粗略测试」：一条管线、每个 agent 两次运行、总共四次执行，因此观察到的行为画像未必能推广。
- token 成本未作测量，速度与可审计性之间那个权衡的经济面因此没有量化。
- 两个 agent 撰写稿件所用的底层 LLM 不同，这让 agent 框架的影响与模型本身的影响混杂在了一起。
- 行为观察是事后从日志重建的；作者也指出，严谨的研究应当直接对 agent 做插桩。
- Run 2 的 SNR 区间并未充分探到阈下区域，因此指令理解上的分歧只在单个临界注入信号上被观察到。
- Repository note: 没有可复用的任务套件、留出划分或公开评分工具——这项贡献是围绕一份规格做的对比研究，因此不重跑作者的整套设置，结果就无法扩展到新的 agent。
- Repository note: 论文是单作者预印本，没有记录任何同行评审 venue；科学产出也是对照规格自身设定的阈值打分，而非对照一条独立的真值管线。

## Related Works

- [gwBenchmarks](./gwbenchmarks.md) — 同一引力波场景下可复用任务套件的那一面，而本工作是在一条管线上做的双 agent 对比。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样评估 coding agent 在终端环境中端到端执行科学管线。
- [Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory](./quantifying-the-reproducibility-of-astrophysical-m.md) — 另一项单案例的天体物理评估，同样考察 agent 从书面规格中重建出了什么。
- [ReplicationBench](./replicationbench.md) — 天体物理复现任务，同样关心 agent 的结果是否忠实于原始描述。
- [Stargazer](./stargazer.md) — 天文学 agent 在定量模型拟合上的评估，与本工作侧重过程行为形成互补。
