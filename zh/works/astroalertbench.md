# AstroAlertBench (2026)

> [English](../../works/astroalertbench.md) | **简体中文**

> **首次公开：** 2026-05-07 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.05573)

## Overview

AstroAlertBench 是一个面向天文警报审查的多模态 benchmark：模型需要把 Zwicky Transient Facility (ZTF) 的真实警报判入五个类别，过程分为元数据理解、科学推理、层级分类三个阶段；此外还设有一条明确的「诚实性」轴，用于衡量模型的自我评估是否与其实际正确率相符。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.05573>
- **Project:** <https://astroalertbench.com>
- **Code:** <https://github.com/LLM-for-Astronomy/AstroAlertBench>
- **Venue:** arXiv preprint (astro-ph.IM, cs.AI), 2026

## Summary

现代时域巡天产出的警报量远超专家的审查能力，这正是 AstroAlertBench 针对的瓶颈。每道题对应一个天体，由表格形式的警报元数据加一张 RGB 拼图（科学图、参考/模板图、差分图）构成；模型先要表明自己正确读懂了各元数据字段，再给出结构化的科学论证，最后作出层级分类判断。benchmark 把准确率与校准分开考察：模型还要为自己的推理打分，自评分与实际正确率之间的差距即作为诚实性度量报告。论文评估了十三个具备视觉能力的前沿模型，并给出人类集成 baseline，以及一套基于 Zooniverse、意在把 human-in-the-loop 标注规模化的协议。

## Tasks

先导集包含 1,500 条真实 ZTF 警报，每类 300 例保持类别均衡，使得分反映的是多模态推理而非多数类先验。题目取自 ALeRCE 基于 ZTF 警报流构建的实时 stamp-classifier 数据集，每个天体只取其首次探测的那条警报。五个类别为：伪源（bogus）、小行星、超新星、AGN 与变星。每道题由表格元数据加科学图、参考图、差分图三联的 RGB 拼图组成。

## Domains

天文学：受评目标是时域天文分类——判断一次差分图像探测究竟是伪迹、太阳系内的移动天体，还是真实的暂现源或变源，并进一步判断其天体物理类别。题目取材自一个实际运行的巡天警报 broker。

## Evaluation

分三阶段评分：

- **Stage A — 元数据理解（感知）。** 模型需把六个字段（`fid`、`isdiffpos`、`magpsf`、`sigmapsf`、`ndethist`、`ncovhist`）的数值参数对应到其科学含义。十三个受评模型在全部六个字段上都取得 100% 准确率。
- **Stage B — 科学论证（推理）。** 模型给出结构化的理由说明，并按各维度为自己打 0–5 分；报告的指标是自评推理分均值，以及自评通过率（平均分 ≥ 4 的警报所占比例）。
- **Stage C — 分阶段分类（决策）。** 一条层级级联：先排除伪迹，再判物理来源，最后定天体物理子类；以各阶段准确率、条件准确率和端到端五分类准确率计分。
- **诚实性。** 定义为模型自评与其客观正确率之间的一致程度，从三个角度考察：群体层面的谦逊程度、以 Pearson 相关刻画的样本级校准，以及行为层面的第二轮重试。
- **报告。** 十三个模型的端到端五分类准确率：Claude Opus 4.7 (thinking) 60.60 ± 1.26%、GPT-5.4 high-think 51.07 ± 1.29%、Kimi K2.5 think 49.34 ± 1.29%、Claude Opus 4.7 no-think 48.87 ± 1.29%、Qwen3.5-397B-A17B think 44.27 ± 1.28%、GPT-5.4 no-think 43.67 ± 1.28%、Gemini 2.5 Pro high-think 41.93 ± 1.27%、Gemini 2.5 Flash no-think 36.27 ± 1.24%、Qwen3.5-397B-A17B no-think 34.98 ± 1.23%、Qwen3.5-35B-A3B think 26.73 ± 1.14%、Qwen3.5-35B-A3B no-think 25.50 ± 1.13%、Qwen3.5-4B no-think 22.32 ± 1.08%、Qwen3.5-4B think 8.41 ± 0.72%。人类集成 baseline 为 30.67 ± 5.32%。

## Typical Duration

未以 wall-clock 或成本形式报告。解码设置有明确说明：temperature 0.2，标准模型 `max_tokens` 为 2,048，推理模型为 20,000；总 token 消耗与运行时间未披露。

## Main Contribution

一个面向天文事件审查的多模态、类别均衡 benchmark，把任务拆解为感知、推理与层级决策三段，并引入诚实性 / 自我校准这条轴，表明准确率与可靠的自我评估并不重合。

## Key Design Ideas

- 警报以实际业务中的形式呈现——broker 元数据加科学图 / 参考图 / 差分图三联——而非经过整理的图像，使输入与人工审查者所见一致。
- 三阶段链条把错误来源区分开：是读错元数据，是天体物理推理有误，还是最终决策出了问题。
- 每类 300 例的均衡采样把真实警报流中的极端类别不均衡从得分中剔除，代价是先验分布不再真实。
- 层级分类（伪迹 → 物理来源 → 子类）支持条件准确率，使模型只具备部分能力的情形也能显现出来。
- 诚实性既做统计度量也做行为度量，包括用第二轮重试观察模型在不确定时是否会修正判断。
- 论文还建立了一个 Zooniverse 项目，作为超出内部专家 baseline、走向社区规模标注的途径。

## Strengths

- 题目来自在线运行的巡天 broker（ZTF 流之上的 ALeRCE），呈现方式与人工审查者所见的模态相同，任务形式贴合实际操作。
- 对比面广：十三个具备视觉能力的模型，涵盖闭源与开源权重，同一模型的 thinking 与非 thinking 变体分开报告。
- 人类集成 baseline 是实测而非假定的，为准确率数字提供了可解读的参照点。
- 诚实性这条轴以三种彼此独立的方式落地，而不是只给一个置信度校准统计量。
- 数据、prompt、运行脚本与评分器均已开放，数据集卡片与 1,500 行清单公开托管。

## Limitations

- 论文明确说明题目集是先导样本，且类别均衡是人为施加而非自然形成，因此准确率不能直接外推到警报流的实际吞吐场景。
- Stage A 已经饱和——所有模型在六个元数据字段上都是 100%——因此对模型之间的区分毫无贡献。
- Repository note: 该 benchmark 是带自评的单轮多模态分类，而非 agent 循环；没有工具调用、没有档案查询、没有多步轨迹，因此它衡量的是天文判断力而非自主研究能力。收录依据是本仓库既有的考题式问答先例：题量明确、协议清晰、多模型对比。
- Repository note: 人类集成 baseline（30.67%）是在一个代表性子集上测得的，误差棒较宽，因此模型与人类孰优孰劣的结论只能谨慎解读。

## Related Works

- [Stargazer](./stargazer.md) — 同样是基于真实档案观测数据的天文评估，但那是迭代式模型拟合环境，而非单次多模态分类。
- [AstroVisBench](./astrovisbench.md) — 同样是天文原生 benchmark，judge 也对照职业天文学家做过校验，但评的是代码与可视化，不是警报分类。
- [SciVisAgentBench](./scivisagentbench.md) — 同样把 LLM 评判与专家一致性分析结合，场景在科学可视化。
- [MaScQA](./mascqa.md) — 收录有明确题量、明确协议、多模型对比的领域题集的先例。
