# SlowLab (2026)

> [English](../../works/slowlab.md) | **简体中文**

> **首次公开：** 2026-10-26 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.34644)

## Overview

SlowLab 检查 AI agent 在实验又慢、又少、又无法撤回时，能不能当好实验者。agent 要在四个模拟温室隔间里完成为期一年的一轮实验：每种下一茬作物，就要占用一个隔间 180 天，中途只能继续种或直接毁掉。年底，agent 推荐一套气候控制策略，由一个不公开的评估器放到它从没见过的天气年份里打分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** [SlowLab: Benchmarking Autonomous AI Agents on a Year of Experiments They Cannot Undo](https://arxiv.org/abs/2610.34644)
- **Full text:** <https://arxiv.org/html/2610.34644v1>
- **Code:** <https://github.com/dingningpei/slowlab-benchmark>（MIT 许可证）
- **Venue:** arXiv 预印本（2026）

## Summary

每个站点都隐藏了品种和设施参数，agent 只能从自己种的作物里摸清这些情况。分支设计把生长期内的测量与作物收尾时的汇总数据分开；Reader swap 则把收集证据和解读证据分开。在 48 个未见站点上的预注册研究中，三个低成本语言模型 agent 的成绩与固定的种植者设定相近，低于一个带先验信息的贝叶斯优化基线。在 94–100% 的 Full 分支里，agent 都等第一批作物收尾后才种第二批，所以生长期内的读数从来没有改变过它们种什么。

## Tasks

- 一次实验就是一次开始操作：选一个隔间、一个开始日（不晚于第 183 天）和一套气候策略。作物随后生长 180 天，再清理 2 天；中途停止就直接毁掉，没有任何回收。
- 一套策略设定六个值：白天温度（18–26 °C）、夜间温度（15–22 °C，且不高于白天）、CO₂（400–1200 ppm）、补光时长（0–16 h）、通风温度偏移（2–6 °C）和通风湿度上限（70–90%）。
- 系统每 300 s 记录八个通道：气温、相对湿度、CO₂、冠层 LAI 代理量，以及累计收获量、供热、补光和 CO₂ 施用量。
- Full 反馈下，agent 可以读取到目前为止测得的任何记录；Endpoint 反馈下，只能看到隔间状态和每茬作物收尾时的汇总数据。
- 研究使用 48 个测试站点和 8 个试点站点。每个站点从十一个经过审核的 KNMI Cabauw 天气年份（2002–2011 年和 2015 年）中抽取一个实验年份和三个评估年份。

## Domains

设施环境作物生产：对一种模拟的结果实作物做温室气候管理，基于 GreenLight 温室模型（Katzin et al., 2020），使用 Cabauw 天气数据。论文没有写明作物品种。分数是经济利润，所以任务同时涉及作物生长与供热、补光和 CO₂ 成本。

## Evaluation

- 评估器把推荐策略放到三个留出天气年份和两个种植日期（1 月 1 日和 7 月 2 日）下运行。站点得分是这六次运行的边际贡献平均值，单位为 EUR/m²，即收获收入减去按公开价格计算的电、热、CO₂、种植、清理和每日固定开支。
- agent 知道评分规则，但始终看不到自己的分数。
- 被测 agent 为 DeepSeek V4.1 Flash、MiMo V2.6 Flash 和 GLM-5.3 Flash，每个站点重复两次。参照对象有两个：一是在开发站点上选定、不做任何实验的固定种植者设定；二是带先验信息的局部贝叶斯优化基线，采用 TuRBO 式信赖域，从种植者设定出发。
- Full 反馈下的平均分：基线 33.62，GLM 29.62，MiMo 28.90，DeepSeek 28.02，固定设定 29.34 EUR/m²。模型比基线低 3.99 到 5.60（Holm 校正后 p 均小于 0.001）。
- 对任何方法，Full 与 Endpoint 之差都不显著。Reader swap 也没有显著改善模型的推荐结果。
- 统计方法：双侧符号翻转置换检验和 BCa bootstrap 区间；七项主要检验采用 Holm 校正。最小关注效应 2 EUR/m² 事先固定；在 80% 统计功效下，可检出的最小差异为 1.30–3.03 EUR/m²。
- 在 8 个测试站点上，数值搜索找到的已知最优策略平均比固定设定高 7.56 EUR/m²。这些值只是下界；两次重复搜索之间分别相差 1.63 和 2.05 EUR/m²。

## Typical Duration

每轮实验覆盖 365 个模拟日。预算为 16 次实验、32 次决策调用（开始、停止、推荐）、128 次接口调用和 5×10⁶ 个提示词字符；模型 agent 另有最多 200 次模型调用的限制。一轮分支实验的 API 成本约为 0.079 美元（DeepSeek）、0.048 美元（GLM）或 0.052 美元（MiMo）。正式运行共 480 轮实验、2,880 次评估，API 总花费 18.70 美元。论文没有报告每轮实验的实际运行时长。

## Main Contribution

一个考察缓慢、不可撤回、有预算限制的实验过程的基准，带隐藏站点参数和不公开的样本外评分，并用分支设计和 Reader swap 诊断 agent 的不足出在哪一步。

## Key Design Ideas

- 作物周期长且不可撤回，每次种植都要消耗稀缺的隔间时间。
- 在未见天气年份中评分，可以区分学到的策略和只适配实验年份的策略。
- Full 与 Endpoint 两个分支从同一个第 0 天设计出发，单独检验生长期内数据的价值。
- 正式运行前，预注册用哈希锁定了样本量、检验方法、模型、提示词、代码和配置。

## Strengths

- 报告了功效分析、多重比较校正、置信区间，以及偏离预注册之处。
- 把收集证据和解读证据分开检查，而不只报告最终利润。
- 报告了每轮实验的 API 成本和调用次数。

## Limitations

- 模拟器没有通过论文对照温室实测数据做的外部检验：气温 RMSE 为 2.579 °C（阈值 2.04），湿度 RMSE 为 9.983 个百分点（阈值 8.50）；CO₂ 通过。结论针对的是模拟环境，不是真实设施。
- 只测试了三个低成本模型，GLM 的推理长度还受限。
- 基线拥有模型所没有的领域先验，并且是在试点后重新设计的。
- Reader swap 研究中不同方法使用的站点不同，因此不能比较各方法收集的证据质量。

## Related Works

- [Model Discovery Agent](./model-discovery-agent.md) — 在预算内，agent 每做完一次实验，就对它学到的内容打分一次。
- [Gravity-Bench-v1](./gravity-bench.md) — 限制对模拟物理系统的观测次数。
- [Frontier-Eng](./frontier-eng.md) — 在固定的模拟器交互预算内优化工程设计。
