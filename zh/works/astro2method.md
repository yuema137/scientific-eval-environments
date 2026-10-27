# Astro2Method (2026)

> [English](../../works/astro2method.md) | **简体中文**

> **首次公开：** 2026-10-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.30282)

## Overview

Astro2Method 检查 LLM 能否为一个天文问题挑出更好的机器学习方法。每道题给出问题设定和两种方法，标准答案是原论文实测效果更好的那一种。基准还进一步检查：检索、agent scaffold，或者原论文自己的流程描述，会不会改变模型的选择。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** [Astro2Method: Benchmarking LLMs on Machine Learning Method Selection in Astronomy](https://arxiv.org/abs/2610.30282)
- **Full text:** <https://arxiv.org/html/2610.30282v1>
- **Dataset:** <https://huggingface.co/datasets/Xingzhongfan/Astro2Method>（500 行 test 划分，CC BY 4.0）
- **Venue:** arXiv 预印本（2026）

## Summary

题目来自已发表天文论文中报告的方法对比。只有差距显著的对比才会保留：论文报告了不确定度时，差距至少要有两个标准差；没有报告时，相对提升至少要达到 10%。难度取决于原作者解释了多少。Easy 题里，作者直接、完整地说明了某种方法为什么更好；Hard 题里只有部分解释。直接提问时，模型在 Easy 题上表现不错，在 Hard 题上却接近随机猜测。检索和推理 scaffold 都没有带来稳定提升。把原论文的流程描述提供给模型（方法名称已遮蔽），Hard 题准确率提高得最多。

## Tasks

500 道二选一题目来自 346 篇论文。这些论文是从 2024-01-01 至 2026-06-30 发表的 1,028 篇天文论文中筛选出来的。其中 Easy 376 题，Hard 124 题。LLM 协助阅读论文、起草题目；每道题都经过人类专家审阅和修改，专家人数没有说明。举一道 Easy 题：根据恒星光变曲线估计表面重力时，加了卷积的 Transformer 和纯卷积网络，哪一个预测误差更低？模型输出 JSON，包含选项 A 或 B，以及一到三句理由。选项与原论文结果一致就算答对。

## Domains

天文学。论文提到的主题包括恒星天体物理（恒星表面重力、极贫金属星、吸积星与原位形成恒星的区分）、星系测光红移，以及一个高能与时域类别，涵盖致密天体、暂现源、引力波和粒子观测。各主题的题目数量只在一张图中给出。

## Evaluation

- 指标是准确率，分别报告 Overall、Easy 和 Hard。随机猜测为 50%，多数类基线为 50.4%。
- 直接提问五个模型：Easy 上 87.50–92.55%，Hard 上 58.87–64.52%，只比随机猜测高 8.9–14.5 个百分点。
- 其中三个模型还在以下设置下测试：基于 1,081 篇 2014–2023 年机器学习天文论文的文本 RAG 和结构化 RAG、不加技能的 agent、ReAct、Self-Ask、CRITIC、来自 Scientific Agent Skills 的三项技能，以及强制联网搜索。
- ReAct、Self-Ask 和 CRITIC 只检索这个历史语料库，Overall 准确率比直接提问低 1.4–6.2 个百分点。
- 强制联网搜索让 Hard 准确率达到 70.97–75.00%。提升主要来自搜索命中了原论文的题目；Hard 题中没有命中原论文的部分，没有一个模型取得正的净提升。
- 加入遮蔽方法名的原论文流程描述后，Hard 准确率比直接提问高 12.1–14.5 个百分点。

## Typical Duration

未报告。agent 设置的上限是：最多六次搜索、每次返回三条结果，Self-Ask 最多六个追问，CRITIC 最多三轮核查。成本不计入评分。

## Main Contribution

一个以文献为依据的基准，把天文中的机器学习方法选择单独拿出来评测，并把原论文完整解释了原因的对比和只部分解释的对比分开。

## Key Design Ideas

- 每道题的答案都是原论文报告、并经过显著性筛选的对比结果。
- 难度取决于原论文对结果解释得是否完整。
- 分别提供相关论文、开放网络和遮蔽后的原论文流程，用来判断模型缺的是实验背景，还是推理能力。

## Strengths

- 对照已发表结果做确定性评分。
- 每道题都经过人工审阅，数据集公开。
- 逐题统计是否接触到原论文，因此联网搜索带来的提升可以追溯到是否找到了答案来源。

## Limitations

- 每题只有两个选项；机器学习与传统方法之间的对比，以及没有方法对比的论文，都被排除在外。
- 作者承认无法排除原论文已进入模型训练数据。论文没有报告人类基线，也没有说明审阅专家人数。
- Repository note: 标签只记录原论文在其自身设定下测得哪种方法更好，不能说明该方法在其他条件下同样占优。

## Related Works

- [AstroMLab 1](./astromlab-1.md) — 基于综述文献构建的天文知识题。
- [AstroAlertBench](./astroalertbench.md) — 对巡天警报做天体物理分类判断。
