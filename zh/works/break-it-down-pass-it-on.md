# Break It Down, Pass It On (2026)

> [English](../../works/break-it-down-pass-it-on.md) | **简体中文**

> **首次公开：** 2026-08-20 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.20274)

## Overview

Break It Down, Pass It On 是一项受控研究，考察 LLM agent 从自己完成的工作中归纳出的 skill，在什么情况下能帮到后续任务。常见做法是每完成一个任务就写一个 skill，并默认复用总是有益的。这项研究则系统地改变两个归纳选择：任务级还是子任务级 skill，文本格式还是 Python 代码格式；每种组合都在同一条任务流上与无 memory 的 baseline 比较。论文还提出一个 skill utility score，只用 skill 描述和任务描述就能算出来，可以作为诊断指标，在跑任何任务之前预判一份 skill memory 会不会有帮助。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities

N/A — 研究的是 skill memory 的归纳粒度，评测用的是通用办公/应用自动化和数据科学问答 benchmark；它评估的是通用 agent memory 的性质，而不是科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.20274>
- **Code:** <https://github.com/Zesearch/skill-transfer-llm-agents>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

任务按顺序组成一条流；每完成一个任务（任务级 agent）或一个子任务（子任务级 agent），agent 就写一个 skill，后面的任务可以按 embedding 相似度检索它。把这些 memory 与无 memory 的运行对比，结果是：任务级 skill 拉低了平均成功率，子任务级 skill 则提高了它；而且文本 skill 比代码 skill 迁移得更好。为了解释这个现象，作者定义了两个量。specificity 衡量一个 skill 与它最近的真实任务之间的距离，比两个随机任务之间的距离近多少；abstractness 衡量它的相似度在各任务之间分布得有多均匀。两者单独都预测不了成功率，但它们的乘积，也就是 utility score，与成功率相关。这个分数用 sentence embedder 计算，不需要运行任务；论文以分箱关系的形式报告它，并不是把它当成校准过的预测器。

## Tasks

N/A — 没有提出新的 benchmark，这项研究复用了三个长程 benchmark：

- **AppWorld** — 417 个任务。
- **OfficeBench** — 300 个任务。
- **KramaBench** — 92 个任务（端到端的数据科学问题，要求针对给定的数据文件写 Python 作答）；少数由 LLM 评判的任务被排除。

共评测 11 个模型：Qwen3-235B-A22B、GPT-OSS-120B、Nemotron-Super-120B、Qwen3-4B/8B/14B/32B、Gemma-3-4B/12B/27B 和 Gemini-3.1-Pro。每个模型都按 2 × 2 设计运行（任务级与子任务级归纳；文本与代码 skill），另加无 memory 的 baseline。

## Domains

通用的办公和应用自动化（AppWorld、OfficeBench）以及数据科学问答（KramaBench）。论文没有把结论限定到某个科学或工程领域。

## Evaluation

- **判分。** AppWorld：官方的基于状态的单元测试，全部通过记 1。OfficeBench：官方检查函数检查文件和应用状态，全部通过记 1。KramaBench：官方的确定性评分器，按答案类型计分（精确答案按容差记 0/1；列表答案用 F1；近似数值答案按相对误差 e 记 1/(1+e)；没有提交记 0）。
- **Skill 诊断。** 设 skill *s* 与 N 条任务指令的余弦相似度为 c_j（all-MiniLM-L6-v2）：specificity(s) = Pr[max_j c_j ≥ cos(t_i, t_k)]，在随机任务对上计算；abstractness(s) = exp H(softmax(c/τ)) / N，τ = 0.1；utility(s) = specificity(s) × abstractness(s)。
- **报告结果（11 个模型平均，成功率 %）。** 任务级：无 memory 22.1，文本 20.9，代码 18.0。子任务级：无 memory 24.8，文本 26.7，代码 25.3。
- **诊断指标的检验。** 按检索到的 skill 的平均 utility 给任务分箱，成功率从 14.0% 升到 24.5%（任务级 agent），从 22.8% 升到 31.0%（子任务级 agent）。论文说，只看 specificity 或只看 abstractness 时，成功率会先升后降；在查阅的正文中没有给出相关系数（TODO(reference)）。
- **成本指标。** 每个任务的 wall-clock 延迟，以及一个 MEM1 风格的「dependency」估计 Σ_c (2p_c + o_c)·o_c / 2，单位为 10⁹ token²。

## Typical Duration

任务级 agent：每个任务 50 步 ReAct。子任务级 agent：最多 15 个子任务，共用 50 步的执行预算（planner 被要求最多拆成 5 个）。每次调用生成上限为 8,192 token。检索最多返回 5 个余弦相似度高于 0.30 的 skill。

## Main Contribution

作者在 11 个模型和三个 benchmark 上表明：skill 按什么粒度、什么格式归纳，决定了 skill memory 相对于无 memory 是有帮助还是有害；他们还提出一个无需运行任务的 utility score（specificity × abstractness），作为 skill memory 的轻量诊断指标。

## Key Design Ideas

- 两个层级使用同一个归纳 prompt，唯一改变的变量是粒度。
- 每个归纳层级都配一个无 memory 的 baseline，所以负迁移会直接表现为差值变成负数，而不只是收益变小。
- 任务按顺序组成流，并在 50 个等宽区间上统计复用密度，追踪写下的 skill 之后什么时候被检索到。
- Utility 只由 skill 和任务描述的 embedding 定义，因此可以在运行任务之前算出来。
- 去重规则：相似度高于 0.85 的文本 skill 合并；近似重复的代码 skill 覆盖或丢弃；加载失败的代码删除。

## Strengths

- 明确报告了负迁移：任务级 skill 在平均值上、在每个 benchmark 上都低于无 memory baseline。
- 模型覆盖面广（11 个模型，从 4B 到前沿规模），判分器都是确定性的。
- 代码和数据公开。

## Limitations

- 只有三个 benchmark；作者指出 computer use 和 agentic coding 场景下可能表现不同。
- Memory 使用固定的归纳和检索规则，skill 不会随时间演化。
- 判分只看最终环境状态。
- 作者提醒，被恶意注入的 skill 可能借同样的复用机制操控 agent。
- Utility score 与成功率的关系只通过分箱成功率展示；没有报告它在新 benchmark 上的预测准确度。
- Repository note: v1 正文说在子任务级文本比代码高 2.9 个点、在任务级高 1.4 个点，而平均表格给出的正好相反（任务级 2.9，子任务级 1.4）；本卡片采用表格数值。
- Repository note: 本卡片依据 arXiv v1 摘要和 HTML 全文以及官方仓库 README 编写（2026 年 11 月）。附录中包含以「an AI Assistant」为对象的 agent system prompt；这些是实验用 prompt，只被当作内容处理。

## Related Works

- [SkillEvolBench](./skillevolbench.md) — 同样发现自我蒸馏出的 skill 可能不如更简单的对照组，它用的对照是复用原始 trajectory，而不是无 memory。
- [SkillLearnBench](./skilllearnbench.md) — 评测从 agent 自身经验生成 skill 的能力，既给任务成功打分，也给 skill 质量打分。
- [Skill Coverage](./skill-coverage.md) — 同样提出一个 skill 级诊断指标，但它从 trajectory 计算，而不是只看描述。
- [SkillLens](./skilllens.md) — 同样关注 skill 按什么粒度复用，在一个四层图上按混合层级调整 skill。
