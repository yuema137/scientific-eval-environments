# Scientific Agent Benchmarks

## Definition

Scientific agent benchmark 是在真实科学研究或实践中提取任务的 AI agent 评估——计算工作流、参数调优、文献 grounding 的问题，或对已发表结果的复现。它们与通用 agent benchmark 的区别在于任务来源（真实科学工作）和正确性标准（对已发表或专家定义结果的匹配）。

## Motivation

科学工作具有通用 agent benchmark 建模不足的若干特征：中间评估可能开销昂贵（仿真、实验）、任务通常长 horizon、正确性有时需要参照已发表或专家标准而非合成 ground truth、工作流涉及需要领域知识才能正确串联的异构工具。给科学 agent 打分需要在评估中显式关注这些特征——因此值得作为独立 topic。

## Existing Approaches

- **可执行的科学工作流。** [Terminal-Bench Science](../works/terminal-bench-science.md) 在容器中用 pytest 确定性验证 AI agent 在自然科学计算工作流上的表现，覆盖五个科学领域。
- **以出版物 SOTA 锚定难度。** [NatureBench](../works/naturebench.md) 从 Nature-family 论文蒸馏 90 个任务，追问 coding agent 是否能达到已发表 SOTA——揭示了显著缺口：最强 agent 仅在 17.8% 的任务上超越已发表 SOTA（匹敌 47.8%）。
- **专家验证、基于执行的任务。** [ScienceAgentBench](../works/scienceagentbench.md) 从四个学科的 44 篇同行评审论文中提取 102 个任务，邀请九位领域专家验证，并将每个任务的输出统一为自包含的 Python 程序，按程序、执行结果与成本打分。它坚持在宣称端到端自动化之前先评估单个工作流任务，并报告了偏低的最佳 agent 求解率（独立 32.4%，含专家知识 34.3%）。
- **端到端研究生命周期。** [AIRS-Bench](../works/airs-bench.md) 提供 20 个 frontier 研究科学任务，不提供 baseline 代码，要求 agent 在语言建模、数学、生物信息学、时间序列预测中从零构造工作流。
- **跨尺度的真实研究场景。** [SciAgentArena](../works/sciagentarena.md) 在 agent-agnostic 环境中提供约 200 个来自真实世界科学研究场景、带逐步验证的任务，报告 agent 能处理结构化数据分析工作流，但在新颖洞见、自主探索与开放式问题上表现挣扎。
- **科学环境的 gymnasium。** [Aviary](../works/aviary.md) 提供一个可扩展的 language-agent 环境 gymnasium，其中三个为科学环境（分子克隆、科学文献研究、蛋白质工程）；其环境是可复用的评估面，尽管论文的头号贡献是训练框架而非评估贡献。
- **Cost-aware 科学仿真。** [SimulCost](../works/simulcost.md) 把 cost-aware 评估扩展到覆盖 13 个仿真器的物理仿真参数调优，显式建模仿真时间与实验资源成本。
- **医生共同验证的医疗评估。** [MedHELM](../works/medhelm.md) 把 Stanford CRFM 的 HELM 扩展到医疗任务：121 任务、由医生共同验证的分类体系；跨 35 benchmark 聚合；LLM-jury 方法与医生一致性（ICC = 0.47）被显式测量。

## Comparison

| Benchmark | Year | 任务来源 | 科学范围 | 验证方式 | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | 领域专家编写 | Life / Physical / Earth / Math / Engineering Sciences | 容器内 pytest 确定性验证 | [→](../works/terminal-bench-science.md) |
| NatureBench | 2026 | 从 Nature-family 论文蒸馏 | 跨学科（Nature 编辑范围） | 与已发表 SOTA 比较 | [→](../works/naturebench.md) |
| ScienceAgentBench | 2024 | 从 44 篇同行评审论文提取（专家验证） | 数据驱动发现（四个学科） | 执行统一的 Python 程序；程序 / 结果 / 成本指标 | [→](../works/scienceagentbench.md) |
| AIRS-Bench | 2026 | Frontier 研究科学任务 | LM / 数学 / 生物信息学 / 时间序列 | 端到端研究生命周期评分 | [→](../works/airs-bench.md) |
| SciAgentArena | 2026 | 约 200 个真实研究场景任务 | 生物医学：5 个领域（分子 → 群体） | 按领域的逐步验证（执行 + 专家标准） | [→](../works/sciagentarena.md) |
| Aviary | 2024 | 五环境 gymnasium（3 个科学） | 分子生物学（克隆 / 蛋白质）+ 文献 | POMDP 环境中的各环境任务成功率 | [→](../works/aviary.md) |
| SimulCost | 2026 | 覆盖 13 个仿真器的参数调优 | 物理仿真 | 预算下成功率；与传统方法对比 | [→](../works/simulcost.md) |
| MedHELM | 2025 | 医生共同设计的分类（29 位医生） | 医疗 / 临床 | LLM-jury（与医生 ICC = 0.47）；跨 35 benchmark 聚合 | [→](../works/medhelm.md) |

## Open Questions

- **正确性的参照标准。** 科学任务允许多种合理的参照标准——已发表 SOTA（NatureBench）、专家分类（MedHELM）、可执行验证（Terminal-Bench Science）、与传统方法对比（SimulCost）。跨 benchmark 比较时，哪一种应成为标准？
- **发现 vs. 复现。** NatureBench 明确区分"匹敌 SOTA"与"真正的方法论创新"。评分指标该如何操作化"发现"？
- **成本作为评估维度。** 科学工作流有真实 tool-use 成本（仿真时间、实验资源）。scientific-agent topic 是否应像 SimulCost 那样把成本作为强制维度？
- **广度 vs. 深度。** 跨学科 benchmark（NatureBench、AIRS-Bench、MedHELM）给出广度；单仿真器 / 单领域 benchmark 给出深度。哪一种更适合作为主要评估面？
- **Judge 可靠性。** MedHELM 报告的 LLM-jury 与医生一致性为 ICC = 0.47。这是否是其他使用 LLM-judge 评分的科学领域 benchmark 应报告的下限？多少才算充分？

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [NatureBench](../works/naturebench.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [SciAgentArena](../works/sciagentarena.md)
- [Aviary](../works/aviary.md)
- [AIRS-Bench](../works/airs-bench.md)
- [SimulCost](../works/simulcost.md)
- [MedHELM](../works/medhelm.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
