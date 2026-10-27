# Evaluator Reliability & Validation

> [English](../../topics/evaluator_reliability_validation.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Evaluator 也是一套 measurement system，不是 oracle。LLM judge 给一条 trajectory 打了 8/10，下一步真正该问的是：它和 expert 是否一致？能不能把更好的 run 排在前面？换个 wording 或 candidate order，结果会不会变？

可以拿 100 条 expert-labeled trajectory，让 judge 全部打一次分，再分别看 false pass、false failure，并交换展示顺序重测。这是在用 judge 排 agent 或提供 reward 之前，先评价 judge 自己。即便这批数据上一致性很高，也不能保证 agent 改变行为、开始钻 judge 空子以后仍然可靠。

## 定义

Evaluator 把一次 agent run 变成分数、排名或 reward。它可以是确定性 verifier、专家 rubric、reward model、LLM judge，也可以把几种方法组合起来。这个 topic 检查它能不能给出正确 verdict，能不能如实表达不确定性，换个无关的展示方式会不会变分，以及这个分数到了下游是不是真能用。

## 为什么重要

分数会把 evaluator 的错误一起带到下游。Judge 可能在简单样例上和专家一致，但一换 candidate order 就颠倒排名，或者偏爱长答案，遇到和 validation set 不同的 trajectory 就失灵。在用它排 leaderboard 或提供 training reward 之前，先得用专家 ground truth、calibration check 和压力测试来评价 evaluator 自己。

## 现有方法

- **专家标注的 trajectory。** [AgentRewardBench](../works/agentrewardbench.md) 与 [MobileJudgeBench](../works/mobilejudgebench.md) 分别用 web 和 mobile agent 的专家结果检验自动 judge。
- **成对偏好。** [Plan-RewardBench](../works/plan-rewardbench.md) 交换候选顺序，测试 evaluator 能否从易混淆的工具 trajectory 中选出较优者。
- **需要 skill 知识的判断。** [SkillTV-Bench](../works/skilltv-bench.md) 检查 judge 能否验证依赖特定 skill 的执行过程。
- **混合验证。** [AgentLens](../works/agentlens.md) 把形式化检查、多个 judge 维度和带证据的文字审查结合起来。
- **领域校准。** [AstroVisBench](../works/astrovisbench.md)、[PSE-Bench](../works/pse-bench.md) 和 [FIRE-Bench](../works/fire-bench.md) 都报告科学输出 judge 与人类专家的一致程度。[DiscoveryBench](../works/discoverybench.md) 把自己的假设匹配 evaluator 验了两轮：先在 200 个抽取与匹配决策上逐步核对，再拿三位标注者对预测假设的排序做整体比对。[QFT-Bench](../works/qft-bench.md) 请同样三位 QFT 专家检查两类 judge 任务：Opus-5 判断答案正确性时与专家的一致率为 98%，判断推导忠实度时只有 73%，所以忠实度统计的可靠程度不如准确率。
- **拿会议的录用结论当锚点。** [AI-Researcher](../works/ai-researcher.md) 用内容相近的 ICLR 录用与拒稿配对检验自己的审稿 agent，并在给任何生成论文打分之前，先把最分不清这两类稿件的 evaluator 剔除。
- **领域校准。** [AstroVisBench](../works/astrovisbench.md)、[PSE-Bench](../works/pse-bench.md) 和 [FIRE-Bench](../works/fire-bench.md) 都报告科学输出 judge 与人类专家的一致程度。
- **给 judge 单独做一套 benchmark。** [PaperBench](../works/paperbench.md) 先人工判定论文部分复现结果的每一个评分叶节点，再把候选 judge 后端当作二分类器对照这些标签打分，最后按每美元换来的 F1 而不是最高 F1 来选型。
- **同一批答案，既换人也换 judge。** [HeurekaBench](../works/heurekabench.md) 在正式使用 judge 之前验两轮：11 位领域专家对同样的 25 条开放题答案打分，另有两个前沿模型对同一批 agent 结果重新评分，于是评分者之间的分歧和 judge 模型之间的分歧被分开报告。
- **要求变了，verifier 还能不能复用。** [AgentProofBench](../works/agentproofbench.md) 把 Web agent 的验收程序冻结，放到会改变同一条指令实际要求的初始状态上重新运行，并与重建的程序比较。随后它从相同的保存起点分出不同的交付策略，把 verifier 在面板上的错误与 agent 最终交付的结果对应起来。

这些新增工作验证的对象不同：[AgentIdeaBench](../works/agentideabench.md)校准评审模型，[AgentActionBench](../works/agentactionbench.md)比较自动与人工 rubric 得到的分数，[PTA-IRT](../works/pta-irt.md)检查子集能否预测全套成绩。某一层的一致性不能替另外两层提供保证。

[AlphaIdeaBench](../works/alphaideabench.md)只校验 judge 的新颖性评分，而且评审意见是由担任 judge 的同一个模型转换成分数的；在场景新颖性上，一致率明显下降。它的有效性和可行性分数没有人工参照。

[Into the Unknown](../works/into-the-unknown.md) 用写细则的科学家本人来检验开放研究的细则评分。每位原作者盲审三篇后续论文，他们的批评被拆成单条。关于是否达成研究方向的 41 条判断，细则全部覆盖，judge 也全部判对。到了审稿式的缺陷，一致率降到 80.34%；到了科学质量和影响，降到 68.68%。所以细则可以用来检查必要条件，却不能用来评判科学价值。另一项四次重复评判的实验按稳定性选定了 GPT-6-Astra judge（总评相同的比例为 86.5%，对比 57.7%），而 GPT-6-Astra 本身也是被评测的 agent 之一。

## 方法对比

| Work | 被检验的 evaluator | Ground truth | 可靠性信号 | 下游验证 |
|---|---|---|---|---|
| [AutoResearchEval](../works/autoresearcheval.md) | 能检查产物的 agent 评判器，对比只读对话记录的单次调用评判器 | 50 条人工标注研究轨迹 | 模式 κ 0.75 对 0.53；根因类别 κ 0.83 对 0.62；召回率 80.7% 对 63.5% | 标注 800 条轨迹的失败；没有分模式一致性或单独隔离产物访问的消融实验 |
| AgentRewardBench | web-agent 的 LLM 与规则 evaluator | 专家 trajectory 标签 | 多 benchmark 上的 precision、recall 与一致性 | Agent 评估 |
| MobileJudgeBench | 六种 mobile judge 方法 × 五个 backbone | 931 条人工标注 trajectory | 分类指标、排名相关、成功率误差 | Agent 排名与 on-policy reward |
| Plan-RewardBench | Reward model 与 LLM judge | 经验证的成对偏好 | 交换顺序后的 pairwise accuracy | 无 |
| SkillTV-Bench | LLM-as-a-Judge 与 Agent-as-a-Judge | 需要 skill 知识的 trajectory 标签 | Judge accuracy 与 best-of-N 选择 | Trajectory 选择 |
| AgentLens | 混合 judge 与形式化 verifier | 可执行检查和审查证据 | 多维质量指数 | Coding agent 诊断 |
| AstroVisBench | 多模态可视化 judge | 专业天文学家标注 | 排名相关与标注者一致性 | Judge 选择 |
| DiscoveryBench | GPT-4 假设匹配 evaluator（HMS） | 从已发表论文复现的标准假设；三位标注者在 100 组上的偏好排序 | 与人类排序一致率 95%，Fleiss κ = 0.91；200 个样例上抽取与匹配步骤正确率 94-99% | Benchmark 评分 |
| AI-Researcher | 五个 LLM 审稿 agent，换序两两比较 | 32 组内容相近的 ICLR 论文配对（2021-2023）的录用/拒稿结果 | 录用预测准确率 65.62-90.62%；可比质量检出率（评分高于 -1.0 的配对占比）93.75-100% | Evaluator 选型：主实验剔除了最弱的模型 |
| PaperBench | 覆盖评分叶节点的 SimpleJudge，五种后端模型 | 五篇论文部分复现结果的人工判分叶节点 | 宏平均二分类 F1（0.59-0.84），与每篇成本并列报告 | 为主排行榜选定 judge 后端 |
| HeurekaBench | 以 GPT-4o 为后端的 G-Eval judge | 11 位单细胞专家对 25 条开放题答案打分；另有两个 judge 模型 | 与专家汇总分的 Spearman 0.93 / 0.90、Cohen's κ 0.85；judge 之间 Spearman 0.84 / 0.79 | Judge 选型与 planner 模型排名 |
| [AgentIdeaBench](../works/agentideabench.md) | 结合文献的评审模型 | 人类代表性论文；100 对计算机科学假设的人工判断 | 与人工多数意见一致率 77%；校准对照 | Static/Active 对比 |
| [AgentActionBench](../works/agentactionbench.md) | 自动生成的论文 rubric | 15 篇论文的人工 rubric | 两种 rubric 所得分数的 Pearson 0.93、Spearman 0.88 | 按复现阶段分解；不等于逐项判分准确率 |
| [PTA-IRT](../works/pta-irt.md) | 从子集推算全套成绩的估计器 | 留出 agent 的全套任务结果 | MAE、Kendall tau、Spearman rho | 四折验证与轨迹消融 |
| [QFT-Bench](../works/qft-bench.md) | 判断答案正确性和推导忠实度的 Opus-5 与 GPT-5.6 judge | 三位 QFT 专家审阅 15 个模型的 60 份回答 | 正确性一致率 98% / 92%；忠实度一致率 73% / 67% | Opus-5 用于正确性兜底判分、忠实度统计和错误分类 |
| [AgentProofBench](../works/agentproofbench.md) | DeepSeek Flash/Pro 编写的冻结 Web agent 验收程序，分复用与重建两种；另用新跑的在线判定作对比 | 556 个自然终止状态，以及 Source、Background、Related 三种初始条件下 558 个状态上的参考规则；LLM 审核在 192 个标签中与 191 个一致 | balanced accuracy；完整面板与 decision-replay 的 joint pass；按任务族 bootstrap 的复用减重建 BA | 从相同的保存起点出发交付：面板全对的分配 32/33 正确交付，面板有错的只有 1/11；程序把关不如中性继续 |
| [AlphaIdeaBench](../works/alphaideabench.md) | Gemini 3.7 Flash judge 的四项新颖性评分 | 600 篇 ICLR 2026 / NeurIPS 2025 / ICML 2025 论文的评审意见，由 Gemini 3.7 Flash 转换为 1–5 分 | ±1 分以内的一致率：问题约 94.5–97.4%，方法 95.9–96.8%，场景 80.6–87.5%；GPT-5 mini 重新评分的 Spearman ρ 为 0.81 / 0.83 | harness 与基础模型排名；有效性和可行性没有人工参照 |
| [Into the Unknown](../works/into-the-unknown.md) | GPT-6-Astra agent judge，按作者指定的诚信和方向细则评分（Codex SDK，四次运行，按节点多数） | 每篇原论文作者对三篇盲审后续论文的批评；稳定性对比另用一个 Claude-Opus-5.5 judge | 覆盖率 / 一致率：是否达成方向 100% / 100%，审稿式缺陷 96.97% / 80.34%，质量与影响 89.05% / 68.68%；四次重复中总评相同 86.5% 对 57.7% | 选定 GPT-6-Astra 为全部 135 份提交的默认 judge |

## 还没解决的问题

- 哪些 judge 指标真能预测排名、reward 和部署决策是否可靠？
- Evaluator 的不确定性应如何传递到 leaderboard 和统计比较？
- 没有完整 oracle 时，怎样测 verifier 的覆盖范围与漏判面？
- Pairwise、pointwise、rubric 和确定性 evaluator 各自在什么条件下失效？
- 怎样抵抗 reward hacking、文风偏差、contamination 和针对 evaluator 的自适应优化？

## 相关工作

- [AgentProofBench](../works/agentproofbench.md)
- [AlphaIdeaBench](../works/alphaideabench.md)
- [QFT-Bench](../works/qft-bench.md)
- [Into the Unknown](../works/into-the-unknown.md)
- [AgentIdeaBench](../works/agentideabench.md)
- [PTA-IRT](../works/pta-irt.md)
- [AutoResearchEval](../works/autoresearcheval.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [AgentLens](../works/agentlens.md)
- [AgentActionBench](../works/agentactionbench.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [PSE-Bench](../works/pse-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [HeurekaBench](../works/heurekabench.md)
- [AstroVisBench](../works/astrovisbench.md)
- [AgentRewardBench](../works/agentrewardbench.md)
- [PaperBench](../works/paperbench.md)
- [AI-Researcher](../works/ai-researcher.md)
- [DiscoveryBench](../works/discoverybench.md)
