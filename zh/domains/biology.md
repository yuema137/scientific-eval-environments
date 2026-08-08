# Biology

> [English](../../domains/biology.md) | **简体中文**

## Scope

从分子到群体尺度的生命科学评估。生物信息学、基因组学与单细胞生物学折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Aviary | 2024 | 分子克隆（DNA 构建体操作）与蛋白质工程：为真实蛋白提出稳定化突变；另含科学文献研究（LitQA2）。 | 带终末奖励的 POMDP 环境：SeqQA（500 训练 / 约 140 测试克隆问题）、Protein Stability（在 megascale 稳定性数据集的 40 个蛋白上提出突变）、LitQA2（248 题）。 | SeqQA / LitQA2 按选择题准确率计分；蛋白任务当且仅当所提突变的 Rosetta ΔΔG < 0（稳定化）记为通过。 | [→](../works/aviary.md) |
| HeurekaBench | 2026 | 回答开放式单细胞生物学研究问题——派生自 13 篇 Nature 与 Cell 论文中的 41 条已验证洞见——agent 需在原研究数据集上自主设计并执行多步分析。 | 50 道开放题 + 50 道选择题（Lite 子集：22 + 18，限 750 MB 以下数据集），由半自动的洞见到问题流水线产出。 | 真值是已发表的研究发现；开放题由 G-Eval GPT-4o judge 按原子事实重合度打 1–5 分，选择题按准确率。 | [→](../works/heurekabench.md) |
| GeneBench-Pro | 2026 | 基因组学、数量生物学与转化生物医学中的多阶段统计分析，每题含 3–13 个推断岔路，貌似合理的错误选择会改变下游答案。 | 129 个问题，构建于因果结构完全已知的构造性模拟数据生成过程之上，刻意避开教科书案例。 | 对照可恢复目标的二元评分，含精确匹配规则与数值容差；无部分得分；每个模型–问题对独立尝试 10 次。 | [→](../works/genebench-pro.md) |
| SciAgentArena | 2026 | 覆盖单细胞组学、空间组学、计算药物发现、EHR 建模与遗传学的真实生物医学研究场景。 | 约 200 个任务，分四类（Data Analysis、Optimization、Discovery、Validity），在交互式、agent 无关的环境中运行；Validity 类含刻意不可行的请求。 | 按领域的逐步验证——专家设计的二元标准、动作级 F1 与任务原生指标（AUROC、Jaccard、相关系数）——基于执行与专家标准，不用 LLM judge。 | [→](../works/sciagentarena.md) |
| ScienceAgentBench | 2024 | 生物信息学任务——其 102 个任务中的 27 个——提取自经同行评审的数据驱动发现工作流。 | 每个任务要求生成一个自包含的 Python 程序，复现真实论文中的分析。 | 有效执行加逐任务手写的成功检查器，对照专家标注参考；图形输出由 GPT-4o 评判。 | [→](../works/scienceagentbench.md) |
| NatureBench | 2026 | 达到 Nature 系列 Cellular Omics（31）与 Protein Biology（16）研究的已发表 SOTA——其 90 个任务中的 47 个——只给目标算法的输入，不给其操作或输出。 | 经评审门控流水线与信息防火墙构建的 code-agent 任务；每任务平均约 3.7 个主指标。 | 在论文自身主指标上的 SOTA 归一化相对差距 g；报告 Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）比率，另有 judge 标记捷径运行。 | [→](../works/naturebench.md) |
| AIRS-Bench | 2026 | 其四个领域之一的生物信息学中的前沿研究任务，覆盖完整研究生命周期，不提供基线代码。 | 套件共 20 个任务；agent 以 CSV 提交留出测试集上的预测。 | 基于执行、只看结果：任务专属评估脚本计分；SOTA 归一化分数，接近上限处用 'march of nines' 变换。 | [→](../works/airs-bench.md) |
| AstaBench | 2025 | 其 11 个 benchmark 的科研套件中的生物学领域 benchmark——如 DiscoveryBench 的数据驱动发现——与以 CS 为主的文献、代码与发现任务并列。 | 11 个 benchmark 共 2,400+ 个问题，配标准、可复现的工具环境；已为 57 个 agent 计分。 | 各 benchmark 自有指标，从精确匹配到 LLM 评判的假设匹配，随时间不变的美元成本核算与分数–成本 Pareto 前沿一并报告。 | [→](../works/astabench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Life Sciences 分组下的生物学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Life 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |

## Related Works

- [Aviary](../works/aviary.md)
- [HeurekaBench](../works/heurekabench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [SciAgentArena](../works/sciagentarena.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [NatureBench](../works/naturebench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
