# AI & Machine Learning Research

> [English](../../domains/ai_ml_research.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为被研究科学的 AI 与机器学习：复现、重发现与扩展已发表的 AI 研究。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
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

## Related Works

- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
- [PaperBench](../works/paperbench.md)
- [MLE-bench](../works/mle-bench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLAgentBench](../works/mlagentbench.md)
- [ML-Bench](../works/ml-bench.md)
- [DSBench](../works/dsbench.md)
- [DA-Code](../works/da-code.md)
- [BLADE](../works/blade.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [SUPER](../works/super.md)
- [MLR-Bench](../works/mlr-bench.md)
- [RE-Bench](../works/re-bench.md)
- [MLGym](../works/mlgym.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [IdeaBench](../works/ideabench.md)
- [LiveIdeaBench](../works/liveideabench.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)
- [Replica](../works/replica.md)
- [Beyond Final Scores](../works/beyond-final-scores.md)
- [AutoWorldModel-Bench](../works/autoworldmodel-bench.md)
