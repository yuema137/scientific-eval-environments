# 月度报告

> [English](../../monthly/README.md) | **简体中文**

月报要讲清楚三件事：这个月知识库收了什么，几项工作放在一起以后说明了什么，以及这些变化为什么值得注意。它是带分析的仓库更新记录，不是简单按论文发布日期排出来的清单。

## 一项工作算在哪个月

一项工作在哪个月第一次进入 `main`，就归到哪个月。Card 上的 `首次公开` 仍单独记录这项工作最早在哪一天能被公众访问。

历史档案有一个一次性的例外：仓库已经收录的 cards 从 2024 年 1 月开始，按各自的 `首次公开` 月份回填；2023 年及更早的工作不做历史月报。以后每月新增的报告仍按进入 `main` 的月份归档。这样老工作晚发现时会在当月标成历史补录，不会悄没声地漏过去。

这俩日期不能混一块儿：

- 如果工作首次公开的月份正好就是报告月份，表里标成 **当月新发布**。
- 如果仓库这个月才补进来一项更早的工作，表里标成 **历史补录**。月报照样收它，但不能说它是这个月刚发表的。

## 月报怎么组织

每份月报包含五部分：

1. **本月概览**：给出数量，再挑三到五条真正值得记住的结论。
2. **这个月到底变了什么**：用三到六条研究故事线把相关工作串起来，不把 card 摘要一股脑贴上去。
3. **值得展开的 Topic**：只有本月形成了文献集群、边界变化或方法分歧的 Topic 才单独成节。
4. **值得展开的 Domain**：只有新增工作暴露了某个领域自己的约束或变化，才单独成节。
5. **本月完整索引**：这个月加入的 card 一张不少，每张只出现一次，同时列出首次公开时间、新发布或补录状态、Topics 和 Domains。

正文负责把重点讲明白，末尾索引负责保证不漏。同一项工作可以属于多个分类，但正文只选一个最合适的位置讲透，其他关系用链接带过去，别来回重复。

## 档案重点

<!-- MONTHLY_ARCHIVE_OVERVIEW_START -->
- 现在一共有 `32` 份月报，覆盖 `364` 项工作，时间从 `2024-01` 到 `2026-08`。
- 目前最密的一期是 [2026-08](./2026-08.md)，单月收了 `39` 项工作。
- 整个档案里最常反复出现的主线，主要还是 `Scientific Agent Benchmarks、Trajectory Evaluation`。
<!-- MONTHLY_ARCHIVE_OVERVIEW_END -->

## 月报列表

这里按月份从新到旧排列。每一行都直接给出这期规模、主要 Topic 聚集点，以及值不值得点进去看的那句重点。

<!-- MONTHLY_REPORTS_START -->
| 月份 | 工作数 | 主要 Topic | 这期值不值得回看 |
|---|---:|---|---|
| [2026-08](./2026-08.md) | 39 | Scientific Agent Benchmarks、Trajectory Evaluation | 2026 年 8 月是目前档案里最密的一个月，一共 39 项新工作。它看起来已经不像某一条单一趋势在变强，而更像整个领域开始拆成几块彼此区分很清楚的子问题。Scientific benchmarking 还是最大头，但真正值得注意的是另外三条线也同时站起来了：trajectory evaluation 开始像一门独立的诊断方法学；long-horizon benchmark 不再只看任务做没做完，而开始把 agent improvement loop 也纳进来；evaluator reliability 这件事本身，也终于开始被系统性地测。 |
| [2026-07](./2026-07.md) | 23 | Scientific Agent Benchmarks、Skill Hierarchy | 2026 年 7 月从数量上看没 6 月那么猛，但结构更集中。这个月主要围着一个问题转：如果 agent 的输出最后要对外部机构、物理过程、或者专家 workflow 负责，而不是只对 benchmark 自己那套打分规矩负责，那 evaluation 该怎么做？最清楚的例子就是桥梁检测排序、物理/天体物理文献综述与项目计划书、结构可靠度分析，以及在固定算力预算下改世界模型。 |
| [2026-06](./2026-06.md) | 36 | Scientific Agent Benchmarks、Skill Hierarchy | 2026 年 6 月是一个很关键的月：这时候仓库前面刚扩出来的 scope，开始不像“先把 topic 开着，后面再慢慢填”，而是真有结构支撑了。表面上看是 36 项工作很多，但更重要的是，这批新文献已经不再像一排平铺的 benchmark 名单。你能同时看到三条主线长出来：scientific benchmark 更贴近真实 workflow 和可执行产物；skill 开始变成一层可以单独评、单独诊断的对象；process-level evaluation 也不再是泛泛而谈，而是开始落到 validator、rubric、planning step 这些真能卡住系统的控制点上。 |
| [2026-05](./2026-05.md) | 28 | Scientific Agent Benchmarks、Trajectory Evaluation | 本月共有 28 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Trajectory Evaluation、Resource-aware Evaluation。 |
| [2026-04](./2026-04.md) | 18 | Scientific Agent Benchmarks、Trajectory Evaluation | 本月共有 18 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Trajectory Evaluation、General Long-Horizon Agent Benchmarks。 |
| [2026-03](./2026-03.md) | 15 | Scientific Agent Benchmarks、Trajectory Evaluation | 本月共有 15 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Trajectory Evaluation、Resource-aware Evaluation。 |
| [2026-02](./2026-02.md) | 13 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 本月共有 13 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks、Credit Assignment。 |
| [2026-01](./2026-01.md) | 11 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 本月共有 11 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks、Credit Assignment。 |
| [2025-12](./2025-12.md) | 9 | Scientific Agent Benchmarks、Trajectory Evaluation | 本月共有 9 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Trajectory Evaluation、Skill Hierarchy。 |
| [2025-11](./2025-11.md) | 6 | Scientific Agent Benchmarks、Resource-aware Evaluation | 本月共有 6 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Resource-aware Evaluation、General Long-Horizon Agent Benchmarks。 |
| [2025-10](./2025-10.md) | 22 | Scientific Agent Benchmarks、Credit Assignment | 本月共有 22 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Credit Assignment、Trajectory Evaluation。 |
| [2025-09](./2025-09.md) | 10 | Scientific Agent Benchmarks、Skill Hierarchy | 本月共有 10 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Skill Hierarchy、Benchmark Design, Validity & Contamination。 |
| [2025-08](./2025-08.md) | 5 | Scientific Agent Benchmarks、Benchmark Design, Validity & Contamination | 本月共有 5 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Benchmark Design, Validity & Contamination。 |
| [2025-07](./2025-07.md) | 10 | Scientific Agent Benchmarks、Survey | 本月共有 10 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Survey、Trajectory Evaluation。 |
| [2025-06](./2025-06.md) | 10 | Scientific Agent Benchmarks、Skill Hierarchy | 本月共有 10 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Skill Hierarchy、General Long-Horizon Agent Benchmarks。 |
| [2025-05](./2025-05.md) | 22 | Scientific Agent Benchmarks、Trajectory Evaluation | 本月共有 22 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Trajectory Evaluation、General Long-Horizon Agent Benchmarks。 |
| [2025-04](./2025-04.md) | 8 | Scientific Agent Benchmarks、Evaluator Reliability & Validation | 本月共有 8 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Evaluator Reliability & Validation、Trajectory Evaluation。 |
| [2025-03](./2025-03.md) | 6 | Scientific Agent Benchmarks、Survey | 本月共有 6 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Survey、Hierarchical Decision Abstraction。 |
| [2025-02](./2025-02.md) | 9 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 本月共有 9 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks、Skill Hierarchy。 |
| [2025-01](./2025-01.md) | 8 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 本月共有 8 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks、Resource-aware Evaluation。 |
| [2024-12](./2024-12.md) | 6 | Scientific Agent Benchmarks、Credit Assignment | 本月共有 6 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Credit Assignment、General Long-Horizon Agent Benchmarks。 |
| [2024-11](./2024-11.md) | 5 | Scientific Agent Benchmarks、Resource-aware Evaluation | 本月共有 5 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Resource-aware Evaluation、Skill Hierarchy。 |
| [2024-10](./2024-10.md) | 15 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 本月共有 15 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks、Trajectory Evaluation。 |
| [2024-09](./2024-09.md) | 4 | Scientific Agent Benchmarks、Skill Hierarchy | 本月共有 4 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Skill Hierarchy、General Long-Horizon Agent Benchmarks。 |
| [2024-08](./2024-08.md) | 4 | Scientific Agent Benchmarks、Trajectory Evaluation | 本月共有 4 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Trajectory Evaluation、Skill Hierarchy。 |
| [2024-07](./2024-07.md) | 6 | Scientific Agent Benchmarks | 本月共有 6 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks。 |
| [2024-06](./2024-06.md) | 6 | Scientific Agent Benchmarks、Planning & Decision-Making Evaluation | 本月共有 6 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、Planning & Decision-Making Evaluation。 |
| [2024-05](./2024-05.md) | 4 | Scientific Agent Benchmarks | 本月共有 4 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks。 |
| [2024-04](./2024-04.md) | 2 | Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks | 本月共有 2 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks、General Long-Horizon Agent Benchmarks。 |
| [2024-03](./2024-03.md) | 1 | Scientific Agent Benchmarks | 本月共有 1 项工作首次公开。先看文献最集中的方向：Scientific Agent Benchmarks。 |
| [2024-02](./2024-02.md) | 2 | General Long-Horizon Agent Benchmarks、Planning & Decision-Making Evaluation | 本月共有 2 项工作首次公开。先看文献最集中的方向：General Long-Horizon Agent Benchmarks、Planning & Decision-Making Evaluation。 |
| [2024-01](./2024-01.md) | 1 | Trajectory Evaluation、Skill Hierarchy | 本月共有 1 项工作首次公开。先看文献最集中的方向：Trajectory Evaluation、Skill Hierarchy、Credit Assignment。 |
<!-- MONTHLY_REPORTS_END -->
