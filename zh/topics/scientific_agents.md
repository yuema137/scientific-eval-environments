# Scientific Agent Benchmarks

> [English](../../topics/scientific_agents.md) | **简体中文**

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
- **生成而非编写的 benchmark。** [HeurekaBench](../works/heurekabench.md) 贡献了一条半自动流水线，从已发表研究及其代码仓库中派生开放式研究问题，并将候选答案与这些研究已报告的发现比对验证。其单细胞实例含 50 道开放题与 50 道选择题，构建自 13 篇论文中的 41 条洞见；最强的现有 agent 在开放题正确性上为 5 分制的 2.34 分。
- **以模拟为根基的判分有效性。** [GeneBench-Pro](../works/genebench-pro.md) 把 129 个多阶段基因组学与定量生物学问题构建在人工模拟的数据生成过程而非真实数据集之上，从而使失败可归因于科学判断失误，而非归因于若干同样站得住脚的分析选择之一。每个问题内含 3 至 13 个相互依赖的决策点，仅以对决策相关数值的二元通过与否判分；所测得的最佳配置为 28.7%。
- **溯源审计下的已发表分析复现。** [Collider-Bench](../works/collider-bench.md) 要求 agent 仅凭公开论文与开源仿真软件复现 LHC 分析，用连续的直方图保真度对照隐藏参考产额为 10 个 CMS 搜索任务打分，并由 LLM judge 审计执行轨迹；在 364 次受评运行中 6% 的提交被标记为伪造，且平均而言没有 agent 能可靠胜过物理学家在环的解法。
- **反事实定律发现。** [NewtonBench](../works/newtonbench.md) 让 agent 对模拟物理系统运行实验，以复原 12 条经典物理定律的反事实偏移版本，用 LLM 判定的符号等价性为其 324 个任务打分。
- **计算材料科学中的主张级复现。** [AutoMat](../works/automat.md) 将 85 条由专家整理的计算材料科学论文主张打包为可运行的 HPC 任务，报告最佳 coding-agent 设定达到 54.1% 成功率，而当工作流必须仅凭论文正文复原时成功率接近零。
- **对接实时地理空间 API 的结构化工具调用。** [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) 针对一个开放、可自托管、服务于西班牙与葡萄牙三项指标的 API 运行 93 个环境分析任务，以机制性检查（不用 LLM judge）为每个案例打分，并把能力与单案例成本作为正交维度报告；最佳模型达到 60.8% ± 0.8%，而近似值比较类任务对每个模型都是 0%。
- **已发表 AI 实验的端到端复现。** [EXP-Bench](../works/exp-bench.md) 从 51 篇 NeurIPS 2024 与 ICLR 2024 论文中整理出 461 个任务，要求 agent 设计、实现、执行并得出完整实验结论；最佳 agent 配置仅能以可执行形式完成 0.5% 的实验。
- **全流程洞见再发现。** [FIRE-Bench](../works/fire-bench.md) 只给 agent 一个来自已发表机器学习研究的高层研究问题，并以对照该研究记录发现的主张级 F1 为其结论打分；最强的受评 agent Claude Code（Sonnet-4）在 30 任务核心集上达到 46.7。
- **隐藏论文再发现。** [ResearchClawBench](../works/researchclawbench.md) 将 40 个任务各自 grounding 在一篇真实已发表论文上，而该论文在评测期间保持隐藏，由 GPT-5.1 按 0–100 的 RADS 刻度、对照专家整理的加权评分标准为 agent 研究报告打分。
- **仿真驱动的模型拟合。** [Stargazer](../works/stargazer.md) 在带有逐准则物理一致性反馈的迭代式径向速度模型拟合上评估 agent；跨三个难度层级与 20 个真实档案系统，没有一个受评前沿 agent 能通过任何一个真实任务。
- **以论文复现为评估单元。** [PRBench](../works/prbench.md) 要求 agent 端到端复现已发表物理论文——30 个跨 11 个子领域的专家整理任务，其上最佳 agent OpenAI Codex（GPT-5.3-Codex）得分 34%，端到端回调成功率为零。
- **整体、成本受控的研究套件。** [AstaBench](../works/astabench.md) 聚合 11 个 benchmark、2,400+ 个问题，覆盖文献理解、代码与执行、数据分析、端到端发现，在标准工具下以时间不变的美元成本核算为 57 个 agent 打分。
- **以文献发现为评估目标。** [AutoResearchBench](../works/autoresearchbench.md) 用 1,000 条查询把自主研究中的文献查找环节单独拿出来评估，分两类任务——Deep Research（通过渐进式多步探查追踪一篇目标论文）与 Wide Research（全面收集满足给定条件的所有论文）——并报告最强模型分别仅达到 9.39% accuracy 与 9.31% IoU，尽管它们已基本攻克 BrowseComp 等通用 agentic browsing benchmark。
- **在真实仪器上物理执行。** [AFMBench](../works/afmbench.md) 要求 agent 在一台真正的原子力显微镜而非仿真器上完成 100 个经整理的任务，并报告材料科学问答能力并不迁移：Claude-3.5-Sonnet 的错误率达 51.6%，而最佳模型的总体任务完成率为 65%，在文档记录与分析合并时则跌至 23.3%。

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
| HeurekaBench | 2026 | 基于已发表研究及其代码仓库的半自动流水线 | 单细胞生物学（流水线被主张为领域无关） | G-Eval LLM judge（GPT-4o，1–5 分）对照已发表发现 | [→](../works/heurekabench.md) |
| GeneBench-Pro | 2026 | 人工模拟的数据生成过程 | 基因组学 / 定量生物学 / 转化医学 | 在校准容差下与可复原目标作二元匹配 | [→](../works/genebench-pro.md) |
| Collider-Bench | 2026 | 源自四项已发表 CMS 超对称搜索（先由专家解出） | 实验粒子物理（LHC recasting） | 对照隐藏参考产额的相对 L²（τ = 0.33 通过阈值）；LLM 溯源 judge | [→](../works/collider-bench.md) |
| NewtonBench | 2025 | 12 条经典物理定律的 108 个反事实偏移，各置于 3 种模拟系统 | 物理中的交互式科学定律发现 | LLM 判定的符号等价加 RMSLE 数据保真度 | [→](../works/newtonbench.md) |
| AutoMat | 2026 | 由材料科学专家从近期论文整理的 85 条主张 | 计算材料科学（统计/ML、DFT、MD、DDD） | artifact-grounded LLM 评估 agent 对照隐藏专家复现步骤打 1–5 分；成功为至少 4 分 | [→](../works/automat.md) |
| GeoNatureAgent Benchmark | 2026 | 针对可自托管地理空间 API、以领域专家 ground truth 指定的任务 | 环境地理空间分析（西班牙 / 葡萄牙） | 自动化工具调用 / 关键词 / 数值容差检查；无 LLM-as-judge | [→](../works/geonatureagent-benchmark.md) |
| EXP-Bench | 2025 | 从 51 篇 NeurIPS 2024 / ICLR 2024 论文及其代码提取的 461 个任务 | 端到端 AI 研究实验：设计、实现、执行、结论 | 对设计 / 实现 / 结论的 LLM-judge 评分加容器化执行验证 | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | 30 篇 ICLR、ICML、NeurIPS 2024–2025 实证 LLM 分析论文各一任务，加 10 任务跨域扩展 | 全流程：从高层研究问题到规划 → 编码 → 执行 → 结论 | 固定 gpt-5.2 蕴含 judge 对照真值发现的主张级 precision、recall、F1 | [→](../works/fire-bench.md) |
| ResearchClawBench | 2026 | 从真实已发表论文专家整理的 40 个任务，目标论文隐藏 | 10 个领域：天文、化学、地球、能源、信息、生命、材料、数学、神经科学、物理 | GPT-5.1 对照加权多模态评分标准为报告打分（RADS，0–100） | [→](../works/researchclawbench.md) |
| Stargazer | 2026 | 100 个种子模拟器任务 + 20 个匿名化档案系统（NASA 系外行星档案、VizieR） | 天体物理：径向速度时间序列上的系外行星模型拟合 | 四项联合通过/失败准则（残差 RMS、ΔBIC、参数匹配、行星数） | [→](../works/stargazer.md) |
| PRBench | 2026 | 由北京大学 20 多个课题组整理并复现的已发表物理论文 | 30 个任务，跨 11 个物理子领域 | 加权四维评分标准，由 green agent 对照专家 ground truth 打分；端到端回调率 | [→](../works/prbench.md) |
| AstaBench | 2025 | 作者自建 + 改编数据集，多来自 Asta 用户请求 | 全流程：文献、代码、数据分析、端到端发现（CS 加权） | LLM-judge 评分标准 + 程序化打分，带成本核算 | [→](../works/astabench.md) |
| AFMBench | 2025 | 100 个专家整理的任务，沿工具数、agent 数、复杂度与功能领域分层 | 材料的扫描探针显微术 | 在 Nanosurf DriveAFM 上物理执行；按领域的完成率加一套命名的错误分类 | [→](../works/afmbench.md) |
| AutoResearchBench | 2026 | 1,000 条查询，由基于论文全文与引用图的 full-text-first 人机协同流水线构建 | 科学文献发现（八个核心 CS 领域） | 对照已验证答案集的精确匹配 accuracy（Deep Research）与集合级 IoU（Wide Research） | [→](../works/autoresearchbench.md) |

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
- [HeurekaBench](../works/heurekabench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [Collider-Bench](../works/collider-bench.md)
- [NewtonBench](../works/newtonbench.md)
- [AutoMat](../works/automat.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Stargazer](../works/stargazer.md)
- [PRBench](../works/prbench.md)
- [AstaBench](../works/astabench.md)
- [AFMBench](../works/afmbench.md)
- [AutoResearchBench](../works/autoresearchbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
