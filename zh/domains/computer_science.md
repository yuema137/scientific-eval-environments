# Computer Science

> [English](../../domains/computer_science.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为被研究领域的计算机科学，不含 AI/ML 研究本身——AI 论文复现见 AI & Machine Learning Research，软件构建与验证见 Software & Systems Engineering。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| AutoResearchBench | 2026 | 覆盖八个核心 CS 领域的科学文献发现：通过渐进多步探查追踪一篇特定目标论文（Deep Research），或全面收集满足给定条件的所有论文（Wide Research）。 | 1,000 条查询——600 条 Deep Research + 400 条 Wide Research（平均每条 9.23 个有效答案）——由全文优先的人机流水线与基于引用的多跳扩展构建。 | 对照已验证目标论文的精确匹配准确率（Deep）；对照经严格审计、须 LLM 一致同意方可收录的答案集的集合级 IoU（Wide）。 | [→](../works/autoresearchbench.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Information 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| ScholarQuest | 2026 | 以研究者的真实检索方式搜索计算机科学文献（侧重信息检索与 AI）：方法导向、设定锚定、比较导向、范围受控四类查询。 | 在开放文献环境中的迭代式文献探索；查询由 1,000 余个计算机科学主题按四种研究意图构造。 | 对照真值论文集的 Recall@100 与 Recall@All，并分析搜索效率、意图级鲁棒性与失败案例。 | [→](../works/scholarquest.md) |
| CORE-Bench | 2024 | 用论文自带的代码与数据重现已发表的计算结果；计算机科学是其三个学科之一。 | 90 篇论文的 270 个任务，分三档难度，含纯语言与视觉-语言两种形式。 | 重现结果的准确率，由快速、可并行的评估系统校验。 | [→](../works/core-bench.md) |
| TCS-Bench | 2026 | 研究级理论计算机科学的证明生成——证明取自顶级 TCS 会议（FOCS、STOC、SODA）的结论。 | 300 个定理证明任务，每个由目标命题加上从 FOCS/STOC/SODA 论文（2020–2026）中提取并组织的上下文构成；模型产出一份自包含的证明。 | 证明由自动化验证 agent 检查（四次 Gemini 3.1 Flash 调用，四选三多数表决），并对照一个 100 项人类专家标注集校准，一致率超过 90%。 | [→](../works/tcs-bench.md) |
| EngDesign | 2025 | 把操作系统设计与计算机体系结构设计写成工程设计规格：给定目标、约束与性能要求。 | 九个工程方向共 101 项设计任务、473 个可评分条目，其中操作系统设计 8 项、计算机体系结构设计 5 项；评测 12 个对话模型与推理模型。 | 模型输出结构化结果，交由逐任务的评估脚本执行，返回二元通过/不通过、0–100 的部分给分与详细日志；101 项任务中有 53 项不涉及授权限制，单独以 EngDesign-Open 发布。 | [→](../works/engdesign.md) |

## Related Works

- [TCS-Bench](../works/tcs-bench.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [ScholarQuest](../works/scholarquest.md)
- [CORE-Bench](../works/core-bench.md)
- [EngDesign](../works/engdesign.md)
