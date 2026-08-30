# ScienceBoard (2025)

> [English](../../works/scienceboard.md) | **简体中文**

> **首次公开：** 2025-05-26 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.19897)

## Overview

ScienceBoard 是一个计算机使用型 agent benchmark：它把多模态 agent 放进一台运行专业科研软件的真实 Ubuntu 桌面，用 169 个人工整理的工作流任务打分。任务横跨六个科学领域，天文一支由 Celestia 星空模拟软件承担。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2505.19897
- **Code:** https://github.com/OS-Copilot/ScienceBoard
- **Project:** https://qiushisun.github.io/ScienceBoard-Home/
- **Venue:** ICLR 2026

## Summary

ScienceBoard 搭起一个真实、可执行的环境：agent 在其中通过 GUI、命令行或两者混用来操作货真价实的科研桌面软件，同时由一个 HTTP 服务把应用内部状态暴露出来，结果因此可以程序化核验。六个应用对应六个领域——UCSF ChimeraX（生物化学）、KAlgebra（代数）、Lean 4（定理证明）、GRASS GIS（地理信息系统）、Celestia（天文）与 TeXstudio（科技文档）。作者陈述的目的，是检验当前的多模态 agent 能否走完端到端的科研工作流，而不只是回答孤立的问题；报告的结果则是全线偏低。

## Tasks

169 个人工整理的真实任务。按交互方式划分：纯 GUI 38 个（22.5%）、纯 CLI 33 个（19.5%）、GUI+CLI 混合 98 个（58.0%）。按难度划分：简单 53.8%、中等 28.4%、困难 16.6%、开放问题 1.2%（2 个）。任务出自一条标注流水线：标注者先照文档学会每个应用，再筛选候选任务并标注难度，统一措辞，并编写用于初始化虚拟机的配置函数；交叉验证的做法是让每个任务由两名随机选出的标注者各执行一遍。天文（Celestia）环境具体分到多少任务是 `TODO(reference)`：论文与项目页只给出 169 的总数和分领域结果，未公布逐应用的任务数。

## Domains

天文是六个受评领域之一，由 Celestia 星空模拟软件承载。论文描述该环境下的任务需要对真实天象具备时空感知，并报告天文是每一个受评 agent 表现最弱的领域之一。其余五个应用直接决定了共同领域：生物学（UCSF ChimeraX 中的结构与分子工作）、数学（KAlgebra 计算机代数与 Lean 4 定理证明）、地球科学（GRASS GIS 地理空间分析）。TeXstudio 这一科技文档环境不归属任何领域。

## Evaluation

每个任务的打分同时看两处：工作流过程中关键中间输入/输出是否正确，以及虚拟机的最终状态；评估模板支持精确匹配、区间判定与数值容差。任务结果是二元的（成功或失败），头条指标是成功率，分总体与分领域报告。当 agent 发出 `DONE` 或 `FAIL` 信号、或达到预设的尝试上限时，一个 episode 结束。在当前版本中，总体最好的是截图 + 无障碍树观测设定下的 GPT-5，为 24.20%，其后是 Gemini-2.5-Pro 的 16.98% 与 Claude-3.7-Sonnet 的 15.79%；开源骨干模型平均低于 12%。分领域看，生物化学与代数最高（GPT-5 可达 62.07%），GIS 与天文最低。

## Typical Duration

报告的平均值为每任务 9.0 步、124 秒 wall-clock 时间。论文说明 rollout 会在预设的尝试上限处终止，但没有给出这个数字；确切的最大步数预算为 `TODO(reference)`。

## Main Contribution

作者把 ScienceBoard 定位为第一个在专业软件构成的真实、可执行科研工作流中评估多模态自主 agent 的 benchmark——而非在静态问答对上评估——并以此表明，最先进的 agent 目前仍算不上可靠的科研助手。

## Key Design Ideas

- 一台 Ubuntu 虚拟机同时承载六个真实科研应用，每个应用都经过改造，通过 HTTP 暴露内部状态以供程序化核验。
- 双交互通道——GUI 操作与应用自带 CLI——且多数任务刻意要求两者并用。
- 结果核验把中间 I/O 的正确性与虚拟机最终状态结合起来，而不只比对一串最终答案文本。
- 一组观测设定消融（仅截图、无障碍树、截图 + 无障碍树），用以分离感知模态对 agent 成败的贡献。
- 一套标注规程：标注者先经文档培训，每个任务再由两名标注者交叉执行。

## Strengths

- 真实桌面环境中的真实专业软件，做对任务就得真会操作科学家日常使用的工具，而不是就这些工具答题。
- 六个确有差别的领域共处同一套评测框架，跨领域难度因此可在统一协议下直接比较。
- 基于状态而非文本匹配的核验，不受 agent 如何措辞其结果的影响。
- 开放发布：代码采用 MIT 许可，并公开了虚拟机快照，环境因此可复现。

## Limitations

- 逐应用的任务数未公布，天文那一部分究竟多大，无法从论文或项目页核实。
- 成功与否是二元的，没有部分得分；走完长工作流大半的 agent，与一上来就失败的 agent 得分相同。
- 难度分布偏易（53.8%），开放问题只有 2 个，困难一端的提升空间因此很有限。
- Repository note: 每任务平均 9.0 步，说明该环境考的更多是贴近真实的工具操作，而非长程规划；就多小时研究轨迹这层意义而言，它不是长程 benchmark。

## Related Works

- [OSWorld](./osworld.md) — 通用计算机使用环境，ScienceBoard 把它「虚拟机加状态核验」的设计移植到了科研软件上。
- [ScienceAgentBench](./scienceagentbench.md) — 以代码为中心的科学 agent 任务，与 ScienceBoard 的 GUI 加 CLI 桌面设定形成对照。
- [Terminal-Bench Science](./terminal-bench-science.md) — 另一个多领域科学 agent 套件，通过一条领域赛道触及天文。
- [SciVisAgentBench](./scivisagentbench.md) — 评估 agent 驱动科学可视化软件，是与之非常接近的工具操作设定。
