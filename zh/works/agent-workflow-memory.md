# Agent Workflow Memory (2024)

> [English](../../works/agent-workflow-memory.md) | **简体中文**

> **首次公开：** 2024-09-11 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2409.07429)

## Overview

Agent Workflow Memory（AWM）从 web agent 过去的 trajectory 中提取可复用的子流程（称为「workflow」），加进 agent 的 memory，用来指导后续任务。没有它时，web agent 每个任务都从头做起。AWM 增加了一个归纳步骤：由 LM 从已解决的例子中抽象出共同的子流程，把例子里的具体值换成占位符。在线设定下，哪些 trajectory 能进入这一步，由一个基于 LM 的 evaluator 决定：它给 agent 自己在测试时产生的每条 trajectory 打上成功或失败的标签，只有被判为成功的才会变成 workflow。论文在 WebArena 和 Mind2Web 上测量效果，包括跨网站和跨领域的划分。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities

N/A — 这是 workflow memory 方法，评测对象是通用的网页导航（WebArena、Mind2Web），没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2409.07429>
- **Code:** <https://github.com/zorazrw/agent-workflow-memory>
- **Venue:** ICML 2025, PMLR 267:63897–63911 (<https://proceedings.mlr.press/v267/wang25bx.html>)

## Summary

一个 workflow 由一段文字描述和一串步骤组成，每一步包括环境状态描述、agent 的推理和一个可执行的 action。离线设定下，workflow 从带标注的训练样例中一次性归纳出来，所有测试任务共用这份固定的 memory。在线设定下，agent 按顺序处理测试 query；每做完一个任务，由 Pan et al. (2024) 提出的 LM evaluator 给出一个二值成功标签，被判为成功的 trajectory 会转换成 workflow，在下一个 query 之前加入 memory。Workflow 之间可以层层叠加：「按名称查找地点」这个 workflow，会成为后来「获取某地邮编」这个 workflow 里的一个 sub-goal。筛选靠的是模型 evaluator，所以被错误接受的 trajectory 可能变成错误的 workflow，论文也提到了这一点。

## Tasks

N/A — 方法论文，没有提出新的任务集。实验使用 WebArena（812 个任务，覆盖购物、CMS、Reddit、GitLab 和地图网站，另有一个 197 例的跨模板子集）和 Mind2Web（cross-task、cross-website 和 cross-domain 三个测试划分；划分大小 `TODO(reference)`）。摘要把这两个 benchmark 合起来描述为来自 200 多个领域的 1,000 多个任务。

## Domains

通用网页导航（购物、内容管理、论坛、代码托管、地图及其他网站）；没有评估任何规范的科学或工程领域。

## Evaluation

在 WebArena 上，一个任务一直运行到模型预测出 stop action 或达到预设的最大步数，由 WebArena 基于执行的检查器判断是否成功；论文报告成功率和步数。AWM 在线选择 workflow 时用的是 LM evaluator，但报告的分数来自 benchmark 检查器。在 Mind2Web 上，预测按 element accuracy、action F1、step success rate 和 task success rate 计分。

报告的结果：

- **WebArena（GPT-4, gpt-4-0613）：** 总成功率 35.5（Shopping 30.8，CMS 29.1，Reddit 50.9，GitLab 31.8，Maps 43.3），对比 SteP 33.0、BrowserGym 23.5、AutoEval 20.2 和 WebArena baseline 14.9。论文报告相对 BrowserGym 有 51.1% 的相对提升，步数约少 2.0。
- **Mind2Web cross-task（GPT-4）：** 离线 AWM 的 element accuracy 50.6、action F1 57.3、step SR 45.1、SR 4.8；MindAct 的 step SR 为 36.2（相对提升 24.6%）。在线 AWM：50.0 / 56.4 / 43.6 / 4.0。
- **泛化（相对 MindAct 的 step SR 提升）：** 在线 AWM 在 cross-task 上 +7.4，cross-website 上 +3.8，cross-domain 上 +16.9；离线 AWM 在 cross-domain 上 +14.0。

Ablation：基于规则与基于 LM 的归纳（WebArena SR 35.6 对 35.5；Mind2Web cross-task step SR 43.4 对 45.1）；文本与代码形式的 workflow（step SR 45.4 对 45.1；SR 3.6 对 4.8）；把 workflow 作为可调用 action 暴露（AWM-AS：step SR 46.4，agent 在 18.5% 的任务中调用了 workflow action）。

## Typical Duration

WebArena episode 在 stop action 或预设最大步数处结束（具体值 `TODO(reference)`）；Mind2Web 每个任务的步数是固定的。

## Main Contribution

一种从 agent 经验中归纳可复用、可组合 workflow 的方法：既可以离线从训练数据归纳，也可以在线从 agent 自己在测试时产生、经自动 evaluator 过滤的 trajectory 中归纳。

## Key Design Ideas

- 把例子里的具体值抽象成占位符（例如 `{product-name}`），使 workflow 能跨任务使用。
- 粒度定在子任务一级（例如「搜索某个商品」），而不是整个任务的指令。
- 在线设定下，memory 是否更新取决于 LM evaluator 的二值成功判断。
- 后面的 workflow 可以把前面的 workflow 当作 sub-goal 复用。
- 比较了 workflow 的不同表示（文本与代码；自然语言状态描述与过滤后的 HTML），以及作为 context 使用和作为可调用 action 使用两种方式。

## Strengths

- 同时评估了离线归纳和不依赖真实标签的在线归纳（论文）。
- 在 Mind2Web 上测试了跨任务、跨网站和跨领域的泛化（论文）。
- WebArena 分数来自 benchmark 基于执行的检查器，独立于选择 workflow 时用的 evaluator（论文）。

## Limitations

- 论文指出，在线 AWM 依据模型判定的 trajectory 来归纳 workflow，而这些判定并不总是正确。
- Workflow 可能把 agent 推向与当前状态不符的 action，在某些设定下导致 action F1 低于 MindAct（论文）。
- Agent 很少调用 workflow action（18.5% 的任务），而固定的 workflow action 难以应对弹窗之类的页面动态变化（论文）。
- Repository note: 论文没有测量 LM evaluator 的准确率，也没有和使用真实标签的在线归纳做对比。
- 论文正文和表格在个别地方的数值略有出入（例如相对 SteP 的提升有 7.9% 和 7.6% 两个值；AWM-AS 的 SR 有 3.2 和 3.6 两个值）。

## Related Works

- [MACLA](./macla.md) — 同样从 trajectory 中存储可复用的 procedure，但按每个 procedure 的 Bayesian 可靠度来选择，而不是对整条 trajectory 做 evaluator 把关。
- [STAIR](./stair.md) — 把 coding agent 过去的修复抽象成多层 plan，并比较各抽象层级。
- [Trace2Tower](./trace2tower.md) — 利用成功和失败证据，从 trajectory 中归纳三层 skill 层级。
- [SkillEvolBench](./skillevolbench.md) — 评测 agent 能否把 episodic trajectory 蒸馏成可复用的 skill。
