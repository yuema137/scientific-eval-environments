# PEOA (2024)

> [English](../../works/peoa.md) | **简体中文**

## Overview

PEOA（Process Engineering Operations Assistant）是一套面向化工与过程工程问题求解的模块化 LLM agent 框架，随框架一同发布的还有两个自建 benchmark 数据集——MathComp 与 ChemProc——以及一套分阶段的工具学习评测协议，用于将该框架与闭源 LLM 对比。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2408.14494
- **Venue:** Accepted for publication by the Association for the Advancement of Artificial Intelligence, Fall Symposium Series

## Summary

PEOA 按「LLM 操作系统」的思路组织：元 agent 统筹一个动作生成器，后者把用户查询拆成子任务，并把每个子任务路由给经指令微调的小规模专家模型。检索在一张带标签属性图上进行——该图由解析学术 PDF 得到，存放于 Neo4j——为图检索增强代码生成（GRACG）循环供给上下文，而这一循环运行在 ReAct 式的迭代求解与错误处理之下。由于该领域此前没有工具集成的解题轨迹，作者用 GPT-4（Omni）作教师模型合成分步轨迹，用来指令微调学生模型。为衡量所得系统，他们构建了两个领域数据集，围绕工具学习的四个阶段并辅以一项人类研究，把该框架与主流闭源模型作了对比。

## Tasks

论文构建了两个自建 benchmark 数据集。MathComp 含 8,500 多个数学建模与数值算法问答对，覆盖微分方程、线性代数、优化等任务。ChemProc 含 7,000 多个化学工程主题的问答对：物料与能量衡算、热力学、传热、反应动力学、流体力学、分离过程与过程控制。两者都编自公开的学术资料，包括从基础到进阶的各类教科书，并按 70% 训练 / 15% 验证 / 15% 测试划分。每个题目都以多步、工具集成的轨迹求解：agent 规划子任务、选择工具、用抽取到的参数调用工具，最后综合出答复。

## Domains

化学工程是核心领域：ChemProc 数据集针对化工与过程工程的核心内容——物料与能量衡算、热力学、传热、反应动力学、流体力学、分离过程与过程控制——论文也把该框架的用途定位为工业化工过程的设计、优化与排障。配套的 MathComp 提供通用的数学建模与数值方法内容（微分方程、线性代数、优化），是为工程计算服务的支撑，而非另一个被单独评估的领域。

## Evaluation

评分沿工具学习的四个阶段展开，而不只看最终答案。任务规划用工具使用意识（Tool Usage Awareness，正确识别出需要外部工具的查询占比）、通过率（成功完成的任务占比）与准确率（生成的计划与标准解一致的占比）。工具选择对照真值工具集，用 Recall@K、NDCG@K 与 COMP@K，其中相关性等级由人工评估者赋分。工具调用看是否符合规定、参数抽取是否正确、错误处理是否得当。答复生成对照参考答复计算 BLEU、ROUGE-L 与 Exact Match。另有一项以用户为中心的评测，对八个由人评判的方面打分——用户满意度、易用性、任务完成度、答复质量、上下文感知、适应性、错误处理与定性反馈——采用 1–5 的 Likert 量表（任务完成度为是/否，定性反馈为 High / Medium-High / Medium）。基线为 GPT-4 Turbo-preview、GPT-4-1106-preview、Claude-3 Opus、Claude-3 Sonnet、Claude-3 Haiku 与 Google Gemini Pro；结果按多次独立运行的集成平均报告。论文给出的结论是：该框架在各评测阶段表现有效，与闭源 LLM 接近，仅存小幅差距。

## Typical Duration

N/A — 论文未报告单任务的 wall-clock、轨迹长度或 token 预算数字。TODO(reference)

## Main Contribution

作者把 PEOA 呈现为一个能自动完成化工与过程工程多步问题求解的框架：它把元 agent 编排器、经指令微调的小规模专家模型、面向检索的属性图知识建模，以及用于领域适配的师生迁移学习管线组合在一起。除框架外，他们还贡献了 MathComp 与 ChemProc 两个 benchmark 数据集和一套分阶段评测协议，并称这补上了更通用的现有数据集所缺的领域知识、计算求解能力与严格评测框架。

## Key Design Ideas

- 元 agent 作为中枢，统筹一个动作生成器与一组经指令微调的小规模专家模型，把复杂查询拆成子任务，再把每个子任务派给对应的专家。
- 知识以 Neo4j 中的带标签属性图建模，节点是自研 PDF 解析管线抽取出的文本、图像、表格与代码，边刻画它们之间的关系；该图同时充当本体与模式。
- 用图检索增强的代码生成（GRACG）替代平铺文本的 RAG，理由是保留图拓扑有助于多跳推理并减少幻觉。
- 师生迁移学习：由 GPT-4（Omni）生成工具集成的解题轨迹作为合成指令微调数据，弥补该领域没有现成轨迹语料的空白。
- 采用迭代求解而非一步规划，使 agent 能依据反馈修正工具输出；DeepSeek-Coder-7B-Instruct 与 DeepSeek-Math-7B-Instruct 用 Hugging Face PEFT 库以 QLoRA 微调。
- 评测按规划、选择、调用、生成四阶段拆分，可以定位轨迹在哪一步断掉，而不是只给一个终点分数。

## Strengths

- 评测是面向轨迹的：四阶段指标族对照标准计划与真值工具集，为中间的规划与工具使用决策打分，而不只看最终答复。
- ChemProc 覆盖化学工程课程的核心广度（衡算、热力学、传递、动力学、分离、过程控制），而非单一子主题。
- 对比覆盖三家厂商的六种闭源模型配置，并按多次独立运行取集成平均。
- 自动指标之外还有八个方面的人类评测，其中刻意注入错误以探测自我纠错能力。

## Limitations

- 论文未提及 MathComp 或 ChemProc 有公开发布，也没有代码仓库；arXiv 页面未列出代码或数据链接。TODO(reference)
- 答复生成质量主要靠对照参考答复的表层重合度指标（BLEU、ROUGE-L、Exact Match）衡量，而这些对工程计算的数值正确性只是很弱的代理。
- Repository note: 同一批数据集既用于指令微调框架，又用于评测框架（70/15/15 划分），因此与闭源基线的对比，实质上是一个领域内微调过的系统对上在其微调分布上零样本作答的模型。
- Repository note: 题目是教科书式的问答对，因此评测覆盖的是过程工程*计算*，而非流程图构建、仿真器在环设计或装置操作决策这类可执行的过程系统任务。
- Repository note: 未报告各数据集内按类别的题量，因此无法判断 ChemProc 中任一化工主题各占多少。

## Related Works

- [T-Eval](./t-eval.md) — 同样把工具使用评测拆成分别评分的子过程，而非一个终点分数。
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — 评估 LLM 求解化学工程热力学问题，与 ChemProc 的主题有重叠。
- [MaScQA](./mascqa.md) — 另一个取自考试/教科书的工程问答数据集，用于探测 LLM 的领域知识。
