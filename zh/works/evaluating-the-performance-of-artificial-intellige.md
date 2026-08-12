# Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams (2024)

> [English](../../works/evaluating-the-performance-of-artificial-intellige.md) | **简体中文**

## Overview

一项早期评估研究：把 NCEES 的 Fundamentals of Engineering（FE）与 Principles and Practice of Engineering（PE，结构专业）模拟试题逐题交给 ChatGPT-4 和 Google Bard 作答，对照 NCEES 官方参考解答判分，并报告分主题与总体的等效通过成绩。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://ascelibrary.org/doi/10.1061/PPSCFX.SCENG-1369>
- **Venue:** Practice Periodical on Structural Design and Construction (ASCE), Vol. 29, No. 2 (2024); DOI 10.1061/PPSCFX.SCENG-1369. Preprint: <https://arxiv.org/abs/2303.18149>（"Can AI Chatbots Pass the Fundamentals of Engineering (FE) and Principles and Practice of Engineering (PE) Structural Exams?"）

## Summary

研究要问的是：当时刚出现的聊天机器人，能否通过美国工程执业准入的这两门执照考试。题目取自 NCEES 的 FE（土木）与 PE 结构专业模拟试卷，逐题提交给每个聊天机器人，再对照 NCEES 推荐解答按严格的对/错二分判定。ChatGPT-4 在 FE 上得 70.9%、PE 上 46.2%；Bard 分别为 39.2% 与 41%。作者的结论是：ChatGPT-4 有望通过 FE——该考试的及格线历来被认为在 60–70% 上下——但两个模型离通过 PE 都还很远；论文还分析了错题背后反复出现的失败模式。

## Tasks

每个聊天机器人各答 79 道 FE 题与 39 道 PE 题，均取自 NCEES 的 FE 与 PE 模拟试卷。FE 部分覆盖 FE 土木考试的 18 个板块（数学、概率与统计、计算工具、职业道德与执业实务、工程经济、静力学、动力学、材料力学、材料、流体力学、水力学与水文系统、结构分析、结构设计、岩土工程、交通工程、环境工程、施工、测量），每个板块约五题，其中若干板块更多。PE 部分覆盖结构 PE 考试的 11 个板块（项目策划、施工手段与方法、土力学、结构力学、水力学与水文、线形几何、材料、场地开发、结构分析、结构设计与构造、规范与施工）。由于不少题目带有复杂图形，本研究的覆盖比一次真实考试要稀疏：带图题只有在能被转写成文字时才纳入。这也是测量与环境工程两个板块相对典型 FE 试卷偏少、PE 样本明显小于实际 80 题试卷的原因。出于尊重 NCEES 版权的考虑，论文没有复制原题，只展示了改写并改动数值的示例。上述题量与板块分布取自该研究的 arXiv 预印本版本。

## Domains

土木与结构工程。PE 部分专指结构专业——结构力学、结构分析、结构设计与构造、土力学、规范与施工，回答中会引用 ACI 与 ASCE 的条文。FE 土木部分则更宽，还涉及通用工程基础（数学、概率与统计、计算工具、工程经济、职业道德）以及土木工程中的交通、环境、测量与水力学等分支。

## Evaluation

每次只向聊天机器人提一道题，作者再逐题对照 NCEES 模拟试卷的推荐解答判分。判分为对/错二分，不给部分分，与真实考试的计分方式一致，也不作分数调整；随后按主题板块与总体分别汇总答对与答错的题数。此外还对照 NCEES 的推荐解答，从切题性、准确性与表述清晰度三方面对回答做了定性讨论。已报告结果：FE——ChatGPT-4 70.9%，Bard 39.2%；PE——ChatGPT-4 46.2%，Bard 41%。作者指出：ChatGPT-4 在 FE 上答错的题中有 6 道解题步骤正确，只栽在算术或单位换算上；两个模型的结构设计题全部答错，而职业道德题全部答对；两者都难以区分均布荷载与集中荷载。

## Typical Duration

单轮问答，一次提示一道题，不使用工具，也没有多步轨迹。作者报告两门考试的完整测试过程共耗时 2 小时。

## Main Contribution

一份量化到主题层面的报告，说明第一代通用聊天机器人在土木与结构工程执照考试上的表现，为「以业界公认的专业标准而非临时拼凑的题集来衡量 LLM 能力」立下一个早期参照点。

## Key Design Ideas

- 以 NCEES 官方模拟试卷作为题源，难度、题型与参考解答都来自真实考试的主办机构。
- 按对/错判分，不给部分分也不作分数调整，与实际考试的计分方式一致。
- 一次提示只给一道题，让每道题彼此独立，避免上下文累积。
- 按主题板块而不只是总体报告成绩，结构设计与职业道德之间的反差正是这样暴露出来的。
- 出于版权考虑不公开原题，只发布改写并改动数值的示例。
- 把研究中各板块的题量分布与典型 FE 试卷的分布做比对，作为覆盖度的效度检验。

## Strengths

- 题源来自外部主办的专业标准，难度标定的可信度是自编题集所不具备的。
- 分板块的成绩拆解让失败模式可解读，而不是把表现压缩成一个数字。
- 错误分析把解题步骤上的能力与算术失误区分开，并点出具体的工程概念混淆（均布荷载与集中荷载、挠度公式误用）。
- 同一套流程下既考了通用工程考试（FE），也考了专业考试（PE 结构），形成广度与深度的对照。

## Limitations

- 没有发布任何 benchmark 制品：题目因版权原因未公开，他人无法在同一批题目上重跑这套评估。
- 覆盖只是部分的——FE 110 题中的 79 题、PE 80 题中的 39 题——因为图形密集的题目无法转写；论文也说明这样的抽样并不符合一次真实考试的构成。
- 只评了两个模型，都出自 2023 年初，且各跑一次，因此这些数字是没有方差估计的一次快照。
- 把带图题人工转写成文字改变了任务本身，论文也承认正是这一点导致测量与环境工程板块占比偏低。
- Repository note: 这里的设定是单轮聊天问答，没有工具调用、没有代码执行、没有 agent 轨迹，因此测的是脱离场景的知识与推理，而不是工程任务的执行。
- Repository note: 本卡片引用的题量与分板块分布读自 arXiv 预印本；ASCE 正式版需付费获取，其主要成绩数字与预印本一致，但题量若有修订，无法对照正式版核实。

## Related Works

- [PE Civil Bench](./pe-civil-bench.md) — 后来出现的开放 benchmark，按 NCEES 样式编制土木工程题目，补上了本研究无法提供的可复用性。
- [Civil-Eval](./civil-eval.md) — 把同样的注册考试范式用到中国的土木与交通工程上，公开了题量并给出加权计分方法。
- [StructureClaw](./structureclaw.md) — 把结构工程评估从静态考题挪到可执行、由求解器验证的场景上。
- [MaScQA](./mascqa.md) — 同样是取自考试的静态问答，用于评估 LLM 的领域知识，学科是材料科学。
- [EEE-Bench](./eee-bench.md) — 电气与电子领域的专业工程考试式 benchmark。
