# AI & Machine Learning Research

> [English](../../domains/ai_ml_research.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为被研究科学的 AI 与机器学习：复现、重发现与扩展已发表的 AI 研究。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Curation-Bench | 2026 | 自动开展 vision-language instruction-tuning 数据选择研究，反复设计和修改可执行 curation policy。 | 固定 base model、训练 recipe 与 evaluator 的开放式 agent 研究 loop；最多迭代 10 轮。 | 用每个数据子集训练模型，再做 downstream evaluation，并与已有 selection baseline 和数据预算比较。 | [→](../works/curation-bench.md) |
| PostTrainBench | 2026 | 围绕七类推理、工具、知识、医疗和代码目标，自主 post-train base LLM。 | 四种 base model × 七个 benchmark target；每任务单张 H100、10 小时，使用四种 CLI scaffold。 | Held-out target benchmark score，跨 base model 与目标聚合，并审计 trace、data 和 script contamination。 | [→](../works/posttrainbench.md) |
| EXP-Bench | 2025 | 完成来自有影响力 AI 论文的完整研究实验——提出假设、设计并实现流程、执行、得出结论——覆盖计算机视觉、NLP 与强化学习。 | 461 个任务，来自 51 篇 NeurIPS 2024 与 ICLR 2024 论文，分解为 12,737 个可单独评分的子任务，每个任务给定研究问题与不完整起始代码。 | 设计、实现（对照真值 git diff）与结论由 LLM judge 评分，另有容器化执行验证器；All·E✓ 要求四项全对（最佳报告值 0.5%）。 | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | 在只给高层研究问题的条件下，重新发现近期高影响力 ML 研究中已确立、可验证的发现——LLM 行为实证研究，外加 CV 与神经网络分析扩展。 | 40 个完整执行的任务，构建自逐论文的研究问题树（根问题 → 子问题 → 叶实验）；全部轻量计算（单块 80GB A100 上 ≤24 小时）。 | 把 agent 结论与真值发现各自拆为原子主张后做语义蕴含匹配，计主张级 precision/recall/F1；judge 与人类对照验证 F1 达 0.89。 | [→](../works/fire-bench.md) |
| AIRS-Bench | 2026 | 语言建模与时间序列预测（连同数学与生物信息学）中的前沿研究任务，覆盖完整研究生命周期，不提供基线代码。 | 20 个任务；agent 以 CSV 提交留出测试集上的预测。 | 基于执行、只看结果：任务专属评估脚本计分；SOTA 归一化分数，接近上限处用 'march of nines' 变换。 | [→](../works/airs-bench.md) |
| AstaBench | 2025 | 以计算机科学为主的整体科研能力：文献理解、代码与执行、数据分析、端到端发现；许多问题来自真实用户对已部署 Asta agent 的请求。 | 11 个 benchmark 共 2,400+ 个问题，配标准可复现工具环境与逐 benchmark 的语料日期截止；已为 57 个 agent 计分。 | 各 benchmark 自有指标（F1、recall@30、精确匹配、LLM 评判的 rubric 与假设匹配），随时间不变的美元成本核算与分数–成本 Pareto 前沿一并报告。 | [→](../works/astabench.md) |
| PaperBench | 2025 | 复现最前沿的 AI 研究——20 篇 ICML 2024 Spotlight 与 Oral 论文——从理解贡献到执行实验。 | 从零复现，分解为 8,316 个可判分的评分节点；另征集 ML 博士人类基线。 | LLM judge 对照与作者共同开发的层级式评分标准打分，judge 本身在单独的 benchmark 上评测。 | [→](../works/paperbench.md) |
| MLE-bench | 2024 | 在真实竞赛上做端到端机器学习工程。 | 75 个配真实数据集的精选 Kaggle 竞赛；agent 训练模型并提交方案（OpenAI）。 | Kaggle 奖牌门槛（铜/银/金）对照公开排行榜人类基线。 | [→](../works/mle-bench.md) |
| MLE-Dojo | 2025 | 在交互环境中迭代构建并改进 ML 方案。 | Gym 式环境中的 200+ Kaggle 挑战，支持 agent 的 SFT/RL。 | 八个 LLM 上的迭代改进、长 horizon 解质量与错误修复效率。 | [→](../works/mle-dojo.md) |
| MLAgentBench | 2023 | 通过迭代式 ML 实验提升模型性能。 | 13 个任务（CIFAR-10 到 BabyLM）；agent 读写文件、运行代码、检查输出、迭代。 | 成功率（相对起始代码基线提升 >10%）与平均提升。 | [→](../works/mlagentbench.md) |
| ML-Bench | 2023 | 使用真实仓库级代码完成 ML 任务。 | 18 个 GitHub 仓库上的 9,641 个样例；ML-LLM-Bench（文本到代码）+ ML-Agent-Bench（沙箱）。 | 代码生成用 Pass@5；自主执行用成功率。 | [→](../works/ml-bench.md) |
| DSBench | 2024 | 在真实感任务上做数据分析与预测建模。 | 540 个任务（466 分析 + 74 建模），带长上下文、多模态、多表数据。 | 分析用任务解出率；建模用相对性能差距。 | [→](../works/dsbench.md) |
| DA-Code | 2024 | 为数据整理与分析编写可执行的数据科学代码。 | 可控 Docker 沙箱中的 agent 式数据科学编码任务。 | 基于执行的准确率；最强 LLM 30.5%。 | [→](../works/da-code.md) |
| BLADE | 2024 | 在开放式数据驱动科学中做出站得住的分析决策。 | 12 个配研究问题与独立专家参考分析的数据集。 | 对照专家真值对分析决策做多方面自动评分。 | [→](../works/blade.md) |
| MLRC-Bench | 2025 | 提出并实现新颖方法以赢得 ML 研究竞赛。 | 7 个竞赛任务；agent 提交方案对照基线与顶尖人类评分。 | 客观的差距缩小指标；最佳 agent 缩小基线到人类差距的 9.3%。 | [→](../works/mlrc-bench.md) |
| SUPER | 2024 | 搭建并执行真实研究仓库中的任务以复现结果。 | 来自 ML/NLP GitHub 仓库的 45 端到端 + 152 子问题 + 602 自动生成任务。 | 端到端与场景（landmark）成功率；GPT-4o 端到端 16.3%。 | [→](../works/super.md) |
| MLR-Bench | 2025 | 从想法到论文开展开放式 ML 研究。 | 覆盖想法生成、方案、实验与论文写作的 201 个任务（workshop）。 | MLR-Judge（LLM 评审 + 评分标准），经专家验证；约 80% 编造结果。 | [→](../works/mlr-bench.md) |
| RE-Bench | 2024 | 在时间预算下做前沿 AI R&D / 研究工程。 | 7 个开放式研究工程环境；61 位人类专家的 71 次 8 小时尝试（METR）。 | 2/8/32 小时预算下对照参考解的 best-of-k；与人类直接对照。 | [→](../works/re-bench.md) |
| MLGym | 2025 | 横跨 CV、NLP、RL 与博弈论开展开放式 AI 研究。 | MLGym-Bench：Gym 环境中支持 agent RL 训练的 13 个任务（Meta）。 | 五个前沿模型在 13 个任务上的表现。 | [→](../works/mlgym.md) |
| ResearchCodeBench | 2025 | 把近期 ML 论文的新颖贡献实现为代码。 | 来自 2024–2025 顶尖论文的 212 个挑战；含 13 篇的抗污染子集。 | 带污染与错误模式分析的成功率；最佳 37.3%。 | [→](../works/researchcodebench.md) |
| IdeaBench | 2024 | 在科学上下文中生成新颖研究想法。 | 从有影响力论文标题/摘要及其参考文献生成想法。 | 两阶段 GPT-4o 按新颖性/可行性排序加相对 Insight Score。 | [→](../works/ideabench.md) |
| LiveIdeaBench | 2024 | 从极简（单关键词）上下文生成科学想法。 | 覆盖 22 领域的 1,180 个关键词；40+ 模型由 LLM 面板评分。 | 五个创造力维度（原创性、可行性、流畅性、灵活性、清晰性）。 | [→](../works/liveideabench.md) |
| DevAI / Agent-as-a-Judge | 2024 | 自主开发满足层级化需求的 AI/ML 项目。 | 55 个自动化 AI 开发任务，配 365 个层级化用户需求。 | 需求级、过程级的 Agent-as-a-Judge 评估，可靠性媲美人类。 | [→](../works/devai.md) |
| Replica | 2026 | 重跑实验，把一篇已发表 ML 或 AI for science 论文中被抹掉的结果图复现出来。 | 从 1990–2026 年的 100 篇论文自动生成 310 个任务（242 训练 / 68 测试）；每任务 60 分钟，算力为一张 H200 的七分之一 MIG 切片。 | 在看不到原图的条件下生成的五维 rubric 评判器；两次评判采样之间一致性 τ = 0.66，而两位人类评分者之间只有 τ = 0.30。 | [→](../works/replica.md) |
| Beyond Final Scores | 2026 | 在长时程运行中改进一份正确但刻意做得不够好的 ML 或系统工件。 | 四族共 36 个 AutoLab 任务（模型开发 7、系统优化 15、谜题与挑战 10、CUDA 4）；七个模型共 756 条 rollout。 | 逐任务自动验证器，分数归一化到 [0, 1]；人工审计发现只有 1.2% 的解真正新颖，6.3% 利用了评测特有的捷径。 | [→](../works/beyond-final-scores.md) |
| AutoWorldModel-Bench | 2026 | 在事先不指定改进方向的前提下，自主改进一个给定的世界模型。 | 64 个会话（2 个 agent × 8 个游戏 × 4 种基础架构），每会话单张 H100 上 6 小时，单次训练限时 10 分钟。 | 留出集上 Position L1 与 Alive F1 在 h ∈ {1, 10, 20} 上的组合；64 个会话中 33 个达到 Δ ≥ +0.10，91% 的胜出改动是实质性修改而非调参。 | [→](../works/autoworldmodel-bench.md) |
| AI Research Preference Models | 2026 | 判断 AI 研究 agent 提出的哪些候选 ML 方案值得花 GPU 时间真正跑一遍。 | 两个基于冻结预训练模型的偏好模型（一个只读方案与代码；一个先在 5 分钟上限内跑试点实验），接入 AIRA-dojo 的子节点生成环节，覆盖 20 个 AIRS-Bench 任务；每任务单张 H200 跑 24 小时、10 个随机种子，合计 200 GPU 小时。 | AIRS-Bench 归一化分数：未引导 0.684 → 只读式 0.711 → agentic 式 0.729，验证集 oracle 上界为 0.748；在 WinoGrande（94.1%）与 SVAMP（95.7%）上刷新最好水平。 | [→](../works/ai-research-preference-models.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的人工智能与机器学习研究子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`LM` 语言建模与自然语言处理 · `CV` 计算机视觉与视觉-语言建模 · `RL` 强化学习 · `GT` 博弈论与多智能体决策 · `TS` 时间序列预测 · `WM` 世界模型与动力学学习 · `INTERP` 神经网络分析与可解释性 · `MLE` 机器学习工程与模型开发 · `SYS` ML 系统、算子与性能工程 · `DS` 数据科学与统计数据分析 · `CODE` 科研代码实现、环境搭建与复现 · `IDEA` 研究选题与假设生成 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

**两个分，不是一个。** 各列分成**覆盖面**——评测设置把什么纳入了考察——与**严谨度**——它报出来的东西有多可信。两者分开求和，因为它们方向相反：一个 benchmark 可以什么都考一点却什么都没验扎实，而一个刻意收窄的 benchmark 反而可能是本页最可信的。各行按 `Cov` 从高到低排，`Cov` 相同时比 `Rig`，仍相同则保持 Comparison 表原序。以覆盖面领先排序，是因为读者扫表时先问的就是这件事——*这个 benchmark 到底有没有把我关心的问题纳入考察*——`Rig` 随后回答它报出的东西能信到什么程度。

### 覆盖面（`Cov`，满分 7）

是非列，按稀缺程度排序——做到的工作越少排得越靠前，因此这一组的左侧就是该领域的薄弱处。几乎人人都满足的性质不设列：*是否编写并运行代码* 就是因此删去的。

- **Net** — 允许联网或实时外部检索；给定的固定语料库不算。
- **E2E** — 端到端研究：只给问题或目标，不提供源论文、参考实现或分步规范，整个研究过程由 agent 自己推进。
- **Cost** — 预算或资源成本被计入评分或明确定价，仅有步数上限不算。
- **MM** — 多模态内容是承重的，要么必须作为输入，要么作为产出物被打分。
- **Repro** — 以某项已发表结果为准，agent 需要复现或还原它。
- **Real** — 使用真实实验或观测数据，而非合成或仿真数据（数字孪生算仿真）。
- **Inter** — 交互式：agent 对环境、工具或仿真器多次动作，并根据反馈决定下一步。

### 严谨度（`Rig`，满分 13）

- **Human** — 有实测的人类专家基线或人类参考表现为整个量表定锚。若锚点只是一篇已发表结果或专家参考实现，而非实际跑出来的人类成绩，记 `◐`。
- **Rubric** — 专家撰写的 rubric 或官方评分标准，带具名维度或权重；连续型自动指标不算 rubric。
- **Contam** — 有刻意设计的机制让答案无法靠记忆得到：取材于训练截止之后、未发表或新撰写的题目、反事实改写、按需生成，或做过泄漏筛查。评测时把一篇已发表论文藏起来记 `◐`——藏起来并不能把它从预训练语料里去掉。
- **Verif** `0`–`3` — 这个分数要在多大程度上依赖对某个模型的信任。`0` 仅由 LLM judge 或 rubric 打分，且该判分器未经验证 · `1` judge/rubric 打分，且报告了与人类专家的一致性 · `2` 确定性校验与 judge/rubric 并用 · `3` 完全确定性——执行、测试、与参考解做数值比对、符号检查或证明内核，全程无 judge 介入。它取代了原先"有无确定性验证"的是非列：那一列 85% 的工作都满足，因而区分不出任何东西；做成阶梯后区分度很高。另有一个 `Judge` 列因与 `Verif` < 2 几乎等价而删去。
- **Scale** `0`–`3` — **本领域内**受评的条目数：`0` 少于 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 及以上 · `?` 原文未给出逐领域计数。它数的是条目而非工作量：30 个论文复现任务远比 3,000 道考试题费力，这一列看不见这一点。
- **Fail** `0`–`4` — 失败分析做到多深，因为"论文有失败分析"这句话的跨度太大——从一句话带过到专门设计的对照实验都算。`0` 除成绩外没有任何失败分析 · `1` 只有关于模型薄弱环节的叙述性评论，未给出类别 · `2` 有具名的错误类别或示例性案例分析，但没有计数或占比 · `3` 定量的失败刻画：带逐类计数或占比的分类体系，或能分离出特定失败条件的实测拆分 · `4` 在第 3 级之上，另有专门设计的对照实验或消融，用来检验失败*为何*发生。

### 怎么读这两个分

是非列按 `✔` 1 分、`◐` 0.5 分、`✘` 0 分、`?` 0 分计；分级列直接计其数值，`?` 计 0 分。`Domain` 不计分。

三点要留意。`?` 与 `✘` 的代价完全相同，所以两个分都是"该工作*可查证地*做到了多少"的下界，而不是对它的判决。两个分也都不是质量排名：`Cov` 高而 `Rig` 低，说的是这个 benchmark 什么都想够到却什么都没钉死；`Cov` 低而 `Rig` 高，说的是它把一件窄事量得很仔细——哪一种才是对的设计，完全取决于要回答什么问题。还有，`Cov` 描述的是*评测设置*而非科学本身：一份工作可以排在本表末尾，同时是它那个子领域最重要的论文。

跨领域套件的行按本领域的切片来写，与上面的 Comparison 表一致。
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MLR-Bench | GEN | ✔ | ✔ | ◐ | ✔ | ✘ | ✔ | ✔ | **5.5** | ✘ | ✔ | ✘ | 1 | 2 | 3 | **7** |
| PostTrainBench | MLE | ✔ | ✔ | ✔ | ✘ | ✘ | ✔ | ✔ | **5** | ✘ | ◐ | ✘ | 2 | 1 | 4 | **7.5** |
| AIRS-Bench | LM, TS | ✔ | ✔ | ✘ | ✘ | ✔ | ✔ | ✔ | **5** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| Curation-Bench | CV, MLE | ? | ✔ | ✔ | ✔ | ✘ | ✔ | ✔ | **5** | ✘ | ✘ | ✘ | 3 | 0 | 4 | **7** |
| PaperBench | GEN | ✔ | ✘ | ◐ | ◐ | ✔ | ✔ | ✔ | **5** | ✔ | ✔ | ◐ | 1 | 1 | 3 | **7.5** |
| AI Research Preference Models | GEN | ? | ✔ | ✔ | ✘ | ✔ | ✔ | ✔ | **5** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| Replica | GEN | ? | ✘ | ✔ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ◐ | 1 | 2 | 2 | **7** |
| DevAI / Agent-as-a-Judge | MLE | ✔ | ◐ | ◐ | ✔ | ✘ | ✔ | ✔ | **5** | ✘ | ✔ | ◐ | 1 | 1 | 3 | **6.5** |
| FIRE-Bench | LM, CV, INTERP | ? | ✔ | ◐ | ? | ✔ | ✔ | ✔ | **4.5** | ◐ | ✘ | ◐ | 1 | 1 | 3 | **6** |
| AstaBench | GEN | ◐ | ◐ | ✔ | ? | ◐ | ✔ | ✔ | **4.5** | ◐ | ✔ | ◐ | 2 | ? | 1 | **5** |
| MLE-bench | MLE | ◐ | ◐ | ◐ | ? | ✘ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 3 | 1 | 3 | **9** |
| EXP-Bench | CV, LM, RL | ? | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **3.5** | ◐ | ◐ | ◐ | 2 | 2 | 3 | **8.5** |
| MLRC-Bench | GEN | ? | ◐ | ◐ | ◐ | ✘ | ✔ | ✔ | **3.5** | ✔ | ◐ | ✔ | 3 | 0 | 3 | **8.5** |
| Beyond Final Scores | MLE, SYS | ? | ◐ | ✔ | ✘ | ✘ | ✔ | ✔ | **3.5** | ◐ | ✘ | ✘ | 3 | 1 | 4 | **8.5** |
| DSBench | DS | ? | ◐ | ◐ | ◐ | ✘ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 2 | 2 | 2 | **7** |
| MLGym | CV, LM, RL, GT | ✔ | ◐ | ◐ | ✘ | ✘ | ◐ | ✔ | **3.5** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| SUPER | CODE | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | ✔ | **3** | ◐ | ✘ | ✘ | 3 | 3 | 3 | **9.5** |
| MLE-Dojo | MLE | ✘ | ◐ | ◐ | ✘ | ✘ | ✔ | ✔ | **3** | ✔ | ✘ | ✘ | 3 | 1 | 3 | **8** |
| DA-Code | DS | ? | ◐ | ✘ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| MLAgentBench | MLE | ✘ | ◐ | ◐ | ? | ✘ | ✔ | ✔ | **3** | ✘ | ◐ | ✔ | 2 | 1 | 3 | **7.5** |
| RE-Bench | SYS, MLE | ? | ◐ | ✔ | ? | ✘ | ◐ | ✔ | **3** | ✔ | ✘ | ✔ | 2 | 0 | 2 | **6** |
| ResearchCodeBench | CODE | ? | ✘ | ✘ | ? | ✔ | ✔ | ✘ | **2** | ◐ | ✘ | ✔ | 3 | 2 | 3 | **9.5** |
| BLADE | DS | ? | ◐ | ✘ | ✘ | ✘ | ✔ | ◐ | **2** | ◐ | ◐ | ✘ | 2 | 1 | 3 | **7** |
| IdeaBench | IDEA | ✘ | ✘ | ✘ | ? | ✔ | ✔ | ✘ | **2** | ◐ | ◐ | ✔ | 0 | 3 | 2 | **7** |
| ML-Bench | CODE | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✔ | ✘ | ✔ | 3 | 3 | 3 | **11** |
| AutoWorldModel-Bench | WM | ? | ◐ | ✘ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| LiveIdeaBench | IDEA | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ◐ | 1 | 3 | 2 | **7.5** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note: 几乎所有未知都集中在两列。`Net` 在 47 行中有 35 行为 `?`，这也正是它排在覆盖面一组最前的原因——本领域几乎没有工作被明确记载允许实时检索，而大多数干脆不提；为核这一列，其中十一篇的全文都读过，没有一篇给出说法。`Scale` 有 12 行为 `?`，无一例外都是跨领域套件：给了任务总数，却不给逐领域拆分。两列都如实记录这种沉默，而不靠推断把它填掉；而在两列上，沉默都实实在在地扣掉了这些工作的分数。另有两格仍为 `?`：SciCode 与 Terminal-Bench Science 的 `Real`。

## Related Works

- [AI Research Preference Models](../works/ai-research-preference-models.md)
- [Beyond Final Scores](../works/beyond-final-scores.md)
- [Replica](../works/replica.md)
- [AutoWorldModel-Bench](../works/autoworldmodel-bench.md)
- [Curation-Bench](../works/curation-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [AstaBench](../works/astabench.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [EXP-Bench](../works/exp-bench.md)
- [MLR-Bench](../works/mlr-bench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [PaperBench](../works/paperbench.md)
- [MLGym](../works/mlgym.md)
- [LiveIdeaBench](../works/liveideabench.md)
- [RE-Bench](../works/re-bench.md)
- [IdeaBench](../works/ideabench.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)
- [DA-Code](../works/da-code.md)
- [MLE-bench](../works/mle-bench.md)
- [DSBench](../works/dsbench.md)
- [SUPER](../works/super.md)
- [BLADE](../works/blade.md)
- [ML-Bench](../works/ml-bench.md)
- [MLAgentBench](../works/mlagentbench.md)
