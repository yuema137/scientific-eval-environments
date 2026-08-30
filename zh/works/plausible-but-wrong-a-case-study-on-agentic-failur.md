# Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows (2026)

> [English](../../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) | **简体中文**

> **首次公开：** 2026-04-28 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2604.25345)

## Overview

一项针对 CMBAgent 多 agent 系统的评估研究，横跨两种工作流范式与十八项天体物理任务，贡献了一套自动化评分协议（执行、参数准确性、数值准确性）和一个四模式失败分类法；其核心发现是「静默的错误计算」——代码语法合法，却在没有任何错误信号的情况下返回看似合理实则错误的物理结果。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.25345>
- **Venue:** arXiv preprint (cs.AI, astro-ph.IM), 2026

## Summary

论文问的不是天体物理 agent 能否成功，而是它失败时是怎么失败的、失败是否看得见。CMBAgent 以两种配置运行——One-Shot 单次通过，以及完整的 Deep Research 规划与控制循环——覆盖十四项以工具为依托的 CAMB 计算任务和四项基于公开天文数据集的研究型分析任务。评分被拆开，使崩溃、求解器参数配置错误、以及参数看似正确但算出错误数字这三件事彼此区分，而不是一并压缩成单一的通过 / 不通过。提供领域专属文档上下文后，One-Shot 综合分从接近零升到 0.85，约六倍的提升；但剩下的主要失败模式是 Mode C：执行成功、参数看上去合理，数值结果却是错的。作者把这项工作定位为案例研究与可靠性分析，而不是新的模型或框架。

## Tasks

十八项天体物理任务，分两组。十四项结构化的 CAMB 计算任务考察参数配置的稳健性、求解器可靠性与数值准确性，改编自 CMBAgent 的 benchmark 仓库并按复杂度分层（任务 1–6 为单次 API 调用，任务 7 起复杂度递增）。四项研究型任务（T1–T4）使用公开档案数据：基于 Union2.1 的 Ia 型超新星拟合、基于 SPARC 星系数据的 NGC 3198 转动曲线建模、取自 NASA Exoplanet Archive 的系外行星质量–半径分析，以及 SLACS 强引力透镜分析。

## Domains

通篇属于天文学与天体物理：用 CAMB 做宇宙学 Boltzmann 求解器计算、超新星宇宙学拟合、星系转动曲线建模、系外行星族群分析与强引力透镜。宇宙学占最大比重；把它同时读作物理学也说得通，但受评目标是基于观测星表的天文推断和天文专用求解器。

## Evaluation

- **执行成功率（ESR）。** 二值；输出必须至少含两列数值，并覆盖参考 x 范围的 95% 以上。
- **参数准确性分（PAS）。** CAMB 求解器各参数相对误差的加权均值，权重按物理重要性取 2.0、1.5 与 1.0。
- **数值准确性分（NAS）。** NRMSE（0.2）、SMAPE（0.3）与 Lin 一致性相关系数（0.5）的加权平均。
- **综合分。** 执行成功时 `Score = PAS × NAS`。头条的 One-Shot 得分 0.85 即 PAS = 0.95 与 NAS = 0.86 之积；不给领域上下文时该分约为 0，差距约六倍。
- **Deep Research 评分**为人工进行，采用参数恢复分 `PRS = max(0, 1 − |θ̂_p − θ*_p| / (3σ*_p))`，再加上对物理合理性与失败可见性的定性评级（✓ / ∼ / ×）。
- **失败分类法**，四种互斥模式：Mode A 代码失败（ESR = 0）；Mode B 参数错误（ESR = 1，PAS < 0.5）；Mode C 计算错误（ESR = 1，PAS ≥ 0.5，NAS < 0.5）；Mode D 正确（ESR = 1，PAS ≥ 0.5，NAS ≥ 0.5）。
- **报告。** 基础 LLM 约有 91% 的运行以 Mode A 失败。不给文档上下文的 CMBAgent 约有 47% 的运行落入 Mode C——计算错误却没有任何错误信号。四项 Deep Research 任务全部出现静默失败；在 T2（NGC 3198）上，5 次试验全部返回 PRS = 0.05，并给出非物理的聚集度参数。

## Typical Duration

未以 token、成本或实测 wall-clock 形式报告。论文给出了 Deep Research 运行的硬件（Dell Precision 5480、32 GB 内存、20 个 CPU 线程），以及 MCMC 步骤「几分钟内完成」的目标运行时间。

## Main Contribution

一项以可靠性为焦点的天体物理 agent 系统评估：把崩溃与静默数值错误区分开，量化其表面能力中有多少来自上下文里的领域文档，并表明剩下的主要失败模式会产出自信、物理上不自洽、却没有任何可见错误提示的结果。

## Key Design Ideas

- 乘法式综合评分（`PAS × NAS`），使一次运行不能靠「配置正确、物理算错」而显得成功。
- 按物理重要性加权的参数误差，而不是把所有字段一视同仁。
- 数值准确性由三个互补的一致性度量（NRMSE、SMAPE、Lin CCC）组合而成，而非单一距离。
- 四模式分类法以同一批分数上的阈值来定义，使失败归类可复现，而不是靠叙述判定。
- 成对的工作流范式——One-Shot 对比带批评与重试的完整 Planning & Control 循环——作为受控变量，检验编排能否消除静默失败。
- 一项关于领域专属上下文的消融（有无 CAMB 文档），把 API 知识的检索与科学能力本身分离开。

## Strengths

- 直指科学部署中最关键的那类失败：结果是错的，却不带任何错误信号。
- 评分是拆解式且由阈值定义的，失败类别从指标推导而来，而非人工指派。
- 任务既覆盖以工具为依托的求解器调用，也覆盖真实档案数据上的开放式分析，因此结论不局限于单一 API 接口。
- 上下文消融给出了一个具体量度：系统表现有多少取决于文档是否出现在 prompt 里。

## Limitations

- 研究只评估了单一 agent 系统（CMBAgent）配单一 LLM 后端（GPT-4o-mini）的若干配置，因此这些失败率不能当作天体物理 agent 的普遍属性来读。
- Deep Research 的评分为人工进行，只覆盖四项任务，且每项任务的试验次数很少。
- 十四项 CAMB 任务改编自 CMBAgent 的 benchmark 仓库，论文未说明有独立发布的任务集与永久 URL，复用因此受限。
- Repository note: 作者明确把这项工作定位为案例研究而非 benchmark；它在此处的持久贡献是评分协议与失败分类法，而不是一套可复用的任务套件。
- Repository note: 综合分是同一次运行上两个子分数的乘积，因此一处参考范围设定失误就可能同时压低两个分项。

## Related Works

- [ReplicationBench](./replicationbench.md) — 同样以作者定义的 ground truth 评估 agent 的天体物理研究工作流，但那是分级的复现 benchmark，而非针对单一系统的失败模式研究。
- [Stargazer](./stargazer.md) — 同样在天文场景中把统计拟合质量与物理参数恢复分开，也报告了拟合好看但物理错误的同一模式。
- [AstroVisBench](./astrovisbench.md) — 同样通过检查数据产物而非代码文本来给天文科学计算的输出打分。
- [EnvTrace](./envtrace.md) — 同样是基于执行的评估，把表面合法的 agent 输出与实质正确的行为区分开。
