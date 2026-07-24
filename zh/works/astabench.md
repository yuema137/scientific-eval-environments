# AstaBench (2025)

## Overview

AstaBench 是一个为 agent 的科学研究能力提供整体度量的 benchmark 套件，将任务与可复现的工具环境和成本受控的评分相配套。它由 11 个 benchmark 的 2,400+ 个问题组成，覆盖四个任务类别——文献理解、代码与执行、数据分析与端到端发现——其中许多问题源自已部署 Asta agent 收到的真实用户请求。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.21652>
- **Project:** <https://allenai.org/asta/leaderboard>
- **Code:** <https://github.com/allenai/asta-bench>
- **Venue:** ICLR 2026

## Summary

AstaBench 认为现有 agent benchmark 套件缺乏用于受控比较的可复现工具，未考虑模型成本与工具访问等混杂因素（confounder），很少为通用 agent 标准化任务接口，缺少由真实产品使用数据支撑的任务，也缺乏全面的 baseline。作者将基准测试原则形式化，并将其实例化为一个由 11 个 benchmark、2,400+ 个问题组成的套件，其背后是 Asta Environment——首个配备生产级、按日期截断检索工具的科学研究环境——并配套 `agent-eval` 成本核算工具包与标准化 agent 套件 `agent-baselines`。论文对 22 个 agent 类别中的 57 个 agent 进行评估，发现尽管在个别方面取得了实质进展，AI 距离解决科学研究辅助这一挑战仍很遥远。

## Tasks

11 个 benchmark 共 2,400+ 个问题：文献理解（PaperFindingBench、LitQA2-FullText-Search、ScholarQA-CS2、LitQA2-FullText、ArxivDIGESTables-Clean）、代码与执行（SUPER-Expert、CORE-Bench-Hard⁻、DS-1000）、数据分析（DiscoveryBench）以及端到端发现（E2E-Bench、E2E-Bench-Hard），每个 benchmark 均带有测试与验证划分。11 个 benchmark 中有 7 个由作者构建（4 个此前未发布），其余在略作修改后改编自已有数据集；许多问题源自已部署 Asta 系统的真实使用——PaperFindingBench 取自 PaperFinder 与 OpenSciLM 的使用日志，ScholarQA-CS2 取自向 OpenSciLM 提交的 100 个用户问题——而两个端到端 benchmark 则将机器生成的研究任务与人类专家评审相结合。文献类 benchmark 携带按 benchmark 设定的语料日期截断，使检索仅限于 benchmark 构建之前的论文。

## Domains

多个科学领域，偏重计算机科学：各 benchmark 的领域为 CS、生物学或混合领域，其中仅 DiscoveryBench 一项就横跨社会学、生物学、人文学科、经济学、工程学与元科学，CORE-Bench-Hard⁻ 则横跨计算机科学、社会科学与医学。

## Evaluation

- **文献理解类指标。**PaperFindingBench 对导航型与元数据型查询按结果集上的 F1 评分，对语义型查询取估计 recall 与 nDCG 的调和平均；LitQA2-FullText 报告 accuracy，LitQA2-FullText-Search 报告 recall@30；ScholarQA-CS2 取四个 LLM 评判维度（citation recall、citation precision、answer relevance、answer coverage）的平均；ArxivDIGESTables-Clean 将生成的表格展开为原子陈述，并报告相对参考表格的 LLM 评判蕴含 recall。
- **代码、数据分析与发现类指标。**SUPER-Expert 与专家标注的 gold 解计算精确匹配，DS-1000 计算所提交代码通过目标测试用例的 accuracy，DiscoveryBench 计算 Hypothesis Matching Score（三个 LLM-as-judge 对齐分数在 context、variables 与 relationship 维度上的乘积），E2E-Bench / E2E-Bench-Hard 则按评分细则对 agent 的报告、代码与产物进行 LLM-as-judge 评估。
- **时间不变的成本核算。**`agent-eval` 工具包根据经 Inspect 记录的模型用量计算每个问题的归一化美元成本，价格取自 `litellm` 成本表的冻结快照并计入缓存折扣，使成本在 API 价格变动后仍可比较。
- **考虑混杂因素的报告方式。**套件与类别分数为各 benchmark 统计量的宏平均（两个 LitQA2 benchmark 各按 0.5 加权），并附 95% 置信区间；排行榜每条记录都按 agent 开放度与 agent 工具方式分类，分数–成本 Pareto 前沿标出成本最优（cost-optimal）的 agent。
- **报告结果（Table 4）。**Asta v0 以 53.0% 的总分领先，每个问题成本 $3.40，次优的 ReAct 搭配 gpt-5 为 44.0%；ReAct 搭配 gpt-5-mini 得 31.6%，每个问题成本 $0.04；最佳开放权重配置 Smolagents Coder 搭配 Llama-4-Scout-17B-16E-Instruct 达到 11.1%。

## Typical Duration

未规定全套件统一的每任务步数、token 或 wall-clock 预算；ReAct baseline 将 agent 限制在每任务最多 100 步（实践中多数模型平均不足 12 步），notebook 代码单元默认在超过 5 分钟后返回超时信息。资源消耗改以每个问题的归一化美元成本计量，从最经济的强 baseline 的 $0.04 到总分最高的 Asta v0 宏平均的 $3.40。

## Main Contribution

一个在标准化工具、考虑混杂因素的评分与时间不变成本核算下度量整体科学研究能力的 benchmark 套件及配套 agent 环境，并附全面的 baseline agent 与公开排行榜。

## Key Design Ideas

- 标准、可复现的工具配置：经 MCP 提供的 Asta Scientific Corpus 文献检索工具（带按 benchmark 设定的语料日期截断），加上沙箱化的有状态 Jupyter notebook 用于代码执行。
- 时间不变的成本核算：将经 Inspect 记录的模型用量按 `litellm` 成本表冻结快照折算为每个问题的归一化美元成本。
- 考虑混杂因素的排行榜设计：提交按 agent 开放度与 agent 工具方式分类，并以 Pareto 前沿呈现分数–成本关系。
- 标准化任务接口加 `agent-baselines` 套件——16 个 agent 类别、其中 9 个为面向科学优化的 Asta agent——使通用 agent 无需逐 benchmark 适配即可接受评估。

## Strengths

- 受控、按日期截断的检索工具使分数差异反映 agent 能力本身，而非特权化的工具或语料访问。
- 考虑成本并按混杂因素分类的报告揭示权衡：ReAct 搭配 gpt-5-mini 与最佳模型的差距在 21%（绝对值）以内，而成本低一个数量级以上。
- 对完整研究流程的覆盖（包括 agent 中立的 E2E-Bench）暴露出单阶段 benchmark 无法度量的复合失败模式。

## Limitations

- Repository note: 整体覆盖偏重计算机科学——论文自身的对比表将其概括为"Broad (weighted towards CS)"，且两个端到端发现 benchmark 仅包含 AI/NLP 研究任务。
- Repository note: 11 个 benchmark 中有 6 个依赖 LLM-as-judge 评分；作者报告了验证（ScholarQA-CS2 上与专家排序的系统级 Kendall τ = 0.467，剔除 Elicit 后升至 0.800；端到端评分细则经抽查核验），并将改进发现类任务的 LLM 评判列为进行中的工作。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样评估 agent 的数据驱动科学任务，但对单项分析子任务的独立生成程序进行评分，而非在一个成本核算套件中横跨文献、代码、数据分析与端到端发现。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样是多领域科学 agent benchmark，但由领域专家撰写、在容器中运行的终端任务构成，而非带成本受控排行榜评分的标准化研究工具环境。
- [Aviary](./aviary.md) — 同样为 agent 提供科学任务环境，但将其封装为带 terminal reward、面向训练的 language-grounded POMDP，而非考虑混杂因素评分的 benchmark 套件。
