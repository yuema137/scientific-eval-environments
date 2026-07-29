# HeurekaBench (2026)

## Overview

HeurekaBench 是一个用于「造 benchmark」的框架——它生成面向实验数据集的探索性开放研究问题，而本身不是一个固定的 benchmark。每个问题都 grounding 在一篇已发表的科学研究及其代码仓库上，由一条半自动流水线产出，其候选答案须经与该研究已报告的发现比对验证。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.01678>
- **Code:** <https://github.com/mlbio-epfl/HeurekaBench>
- **Venue:** ICLR 2026

## Summary

作者指出，评估 co-scientist 类 agent 需要真实的端到端研究场景，须把数据分析、结果解读与从实验数据中产出新洞见三者贯通，而现有 benchmark 并未提供这样的场景。HeurekaBench 的应对方式是贡献构造流水线而非一份题目清单：由多个 LLM 从研究中抽取候选洞见并生成候选工作流，再与已报告的发现比对验证，通过后才成为题目。该框架在单细胞生物学领域实例化为 sc-HeurekaBench，并用于比较现有的单细胞 agent——其中最强者在开放题正确性上为 5 分制的 2.34 分。

## Tasks

单细胞实例 sc-HeurekaBench 包含 50 道开放题与 50 道选择题，构建自 13 篇论文中的 41 条已验证洞见——其中 9 篇出自 Nature、4 篇出自 Cell。题目分三个阶段产出：insights generation，从科学文献中抽取候选洞见并半自动验证；questions generation，把已验证的洞见改写为问答对；question solving，由 agent 自主设计并执行多步分析，给出基于数据的答案。另有一个精简子集 sc-HeurekaBench-Lite，限定数据集小于 750 MB，含其中 22 道开放题与 18 道选择题，以确保所有参与比较的 agent 都能在同一批任务上跑通。

## Domains

单细胞生物学——作为作者所主张的领域无关构造流水线的一次实例化。

## Evaluation

- **开放题正确性由 LLM judge 评定。** 采用 G-Eval，以 GPT-4o 作为 judge，给出 1 至 5 分的评级。评定时把回答与 ground truth 双方都拆解为原子事实，评级反映二者在完整、部分、缺失三类事实上的重合情况。
- **选择题**以 accuracy 为主指标，同时报告 precision 与 recall。
- **Ground truth 取自已发表的发现。** 流水线产出的候选工作流须与源研究所报告的结果比对验证，而非对照合成目标或标注者自行编写的答案。
- **报告：** 在 sc-HeurekaBench-Lite 上，三个现有单细胞 agent 的开放题正确性（5 分制）分别为 BixBench-Agent 2.34、Biomni 2.31、CellVoyager 2.03。planner 模型的消融给出 Claude-4-Sonnet 2.58 ± 0.05、GPT-OSS-120B 2.08 ± 0.05、Qwen3-235B-thinking 1.85 ± 0.03。作者另报告，加入 critic 模块可使开源 LLM agent 的 ill-formed 回答改善至多 22%，从而缩小与闭源同类的差距。

## Typical Duration

未说明：论文未给出每题的 wall-clock、步数或 token 预算。其记录的唯一资源约束落在数据体量上——Lite 子集限定数据集小于 750 MB，以便所有参与比较的 agent 都能运行。

## Main Contribution

一条用于从已发表研究及其代码仓库构造端到端科学 benchmark 的半自动流水线，其中 ground truth 是与这些研究已报告的发现比对验证而来，而非人工编写。

## Key Design Ideas

- 被贡献的产物是 benchmark 的构造方式；单细胞题集只是该流水线的一次实例化，而非交付物本身。
- Ground truth 锚定在已发表研究已报告的发现上，并与该研究的代码仓库配对，使正确性标准具备外部参照。
- 由多个 LLM 抽取候选洞见并生成候选工作流，再以一道半自动验证环节把关，决定什么才能成为题目。
- 同一批已验证洞见以开放题与选择题两种形式出题，使自由生成与受限选择能在同一来源上被衡量。

## Strengths

- 题目派生自论文及其代码仓库，意味着新研究可直接产出新题而无需人工编写，从结构上而非靠定期重新发布来应对 benchmark 老化。
- 把答案锚定在已发表的发现上，使正确性的参照不依赖于 benchmark 作者自身对「什么是正确答案」的判断。
- 论文把该 benchmark 用于诊断而不只是发布排名——用它比较 planner 模型，并单独隔离出一项 agent 设计选择的影响。

## Limitations

- Repository note: 该流水线是半自动的，依赖多个 LLM 抽取洞见与生成候选工作流，开放题答案又由 LLM judge 评分，因此题目本身及其评分都继承了用于产出它们的模型的可靠性。
- Repository note: 目前只存在单细胞这一个实例——流水线虽被主张为领域无关，但论文并未评估其向其他领域的迁移——且所报告的 agent 比较跑在精简的 Lite 子集上，而非完整的 50 道开放题。

## Related Works

- [NatureBench](./naturebench.md) — 同样把难度锚定在已发表研究上、并对照论文所报告的结果打分，但它蒸馏出的是一份固定任务集，而 HeurekaBench 贡献的是生成这些任务的流水线。
- [ScienceAgentBench](./scienceagentbench.md) — 同样从同行评审论文中提取任务并在发布前加以验证，但其验证由领域专家在人工策展的题集上完成，而非半自动地对照源研究自身的发现。
- [SciAgentArena](./sciagentarena.md) — 同样面向真实研究场景，并报告 agent 在新颖洞见与开放式问题上表现挣扎——而这正是 HeurekaBench 的开放题所要衡量的能力；其任务是直接策展的，而非经由一条构造流水线派生。
