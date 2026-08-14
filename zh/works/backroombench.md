# BACKROOMBench (2026)

> [English](../../works/backroombench.md) | **简体中文**

## Overview

BACKROOMBench 是建立在 BACKTRACE 评估框架之上的可验证测试床，用来度量 skill 增强的语言 agent *自述*的 skill 使用，与该 skill 对其答案的因果影响是否一致——后者由*干预实验测得*。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 评估方法学工作；逻辑与数学题目只是度量 skill 溯源的受控载体，任何科学或研究活动本身都不是受评对象。

## Links

- **Paper:** <https://arxiv.org/abs/2607.27484>
- **Venue:** arXiv preprint (cs.AI, cs.MA), 2026

## Summary

评估 skill 增强 agent 时，通常从 agent 可见的推理过程、或它自己的归因陈述来推断它用了哪些 skill；但这些信号说明的是 agent *看起来*用了什么，而非该 skill 是否真的改变了决策。BACKTRACE 用三件事补上这道缺口：为每个带 skill 的作答配一个条件匹配的无 skill 反事实；在 skill 的含义、措辞、身份、内容与指派上施加干预；并且只在答案已经落定之后才向 agent 索取归因。BACKROOMBench 把这套框架落到受控逻辑题与竞赛数学题上，覆盖单 agent 与多 agent 设定以及多个模型家族。作者把由此浮现的现象命名为 *Reasoning Backroom*：自述的 skill 使用与实测的因果依赖之间存在系统性背离。

## Tasks

共 583 个实例：300 道受控的 PrOntoQA 风格逻辑题，283 道自然的 MATH-500 数学题。每道题在七种 skill 条件下各跑一次——无 skill（基线）、正确、改写、误导、换名、换内容、无关——以便把针对 skill 含义、措辞、身份、内容与指派的干预分离开。逻辑子集上评估了十二个模型（Qwen2.5-Instruct 7B/14B/32B、DeepSeek-R1-Distill-Qwen 7B/14B/32B、GPT-4.1 nano/mini、GPT-5 nano/mini、GPT-5.4 nano/mini），其中六个模型的交集延续到数学子集。除单 agent 之外，还评估了多 agent 配置。

## Domains

不指派任何规范科学或工程领域。两个题目来源——PrOntoQA 风格的合成逻辑题与 MATH-500 竞赛题——只是因为便于验证而被选作受控载体，真正度量的是 skill 影响的溯源，而不是数学或逻辑能力。仅凭载体就指派 Mathematics，会让领域轴的口径过宽。

## Evaluation

- **依赖度（R_v）** — 一个指示量，表示 skill 条件 *v* 下的答案是否不同于无 skill 时的答案，即 `1[d_v != d_∅]`。
- **带符号效用（u_v）** — 相对参考答案，这一改变是帮了忙还是帮了倒忙，`1[d_v = d*] - 1[d_∅ = d*]`。
- **归因保真分（AFS）** — 实测依赖与自称使用之间的重合度，按 `2·n11 / (2·n11 + n10 + n01)` 计算。
- **Backroom Gap（Γ_v）** — 自称的依赖与干预实测的依赖之间的不一致率。
- 以这些因果量为参照，对观察型检测手段做元评估：直接的 skill 使用声明、正文中对 skill 的提及、轨迹相似度，以及一个 LLM 评判者。
- **报告。** 有八个模型在基线准确率完美、删除 skill 也毫无依赖的情况下，仍声称自己用了 skill。逻辑子集上，AFS 在各模型–条件组合间从 .01 到 .72 不等；数学子集上没有任何模型–条件组合超过 .43。多 agent 设定中，skill 的影响可以在其来源丢失之后仍经由通信存续，而完全没拿到 skill 的团队照样会说出从未提供过的 skill 与来源，虚假溯源率接近 1.00。

## Typical Duration

TODO(reference) — 论文未报告逐题的墙钟时间或 token 预算。成本随七条件设计而上升，因为每道题都要在每种 skill 条件下各作答一次，外加一个无 skill 反事实。

## Main Contribution

确立了这样一点：自述的 skill 使用并不构成 skill 起了作用的证据；并把 Reasoning Backroom 刻画为一个一般性的 AI 溯源问题——要审计它，靠观察不行，必须靠干预。

## Key Design Ideas

- 每个带 skill 的作答都配一个条件匹配的无 skill 反事实，影响由差值测得，而不是从对话记录里读出来。
- 干预沿五条可分离的轴分解——含义、措辞、身份、内容、指派——从而把行为上的变化追溯到程序性内容，而不是追溯到显示出来的 skill 名称。
- 归因只在答案落定*之后*索取，避免索取归因这件事本身反过来影响决策。
- 观察型检测手段被当作受评对象而非真值，用干预实测出的信号来给它们打分。
- 纳入多 agent 设定，使溯源在通信过程中的丢失，能与它在单个 agent 内部的丢失分开观察。

## Strengths

- 把 skill 评估中经常被混为一谈的两件事分开：agent 提到了某个 skill，和这个 skill 改变了结果。
- 带符号效用把「沉默采纳」（帮了忙却未获承认）与「表演式使用」（获得承认却没帮上忙）区分开，而不是把两者压成一个「用了/没用」的比特。
- 题目来源可验证、参考答案确定，反事实比较因此定义明确。
- 四类检测手段上的负面结果，对基于自我报告与评判者的 skill 使用审计给出了具体的警示。

## Limitations

- 题目载体是刻意收窄的——合成逻辑题与竞赛数学题——因此结论并不直接覆盖长程或需要执行工具的 skill 使用。
- 论文未给出代码或数据集地址；文中提到已发布逐实例记录与运行清单，但未能定位。
- Repository note: 卡片中的数字读自 arXiv 全文（v1，2026 年 7 月）；撰写时未找到同行评议版本。
- Repository note: 七条件设计把每道题的推理成本乘了数倍；要把 BACKTRACE 用到更大或更昂贵的任务套件上，这是一道现实约束。

## Related Works

- [Skill-Use](./skill-use.md) — 同样把 skill 使用当作受测对象，拆成触发 / 遵从 / 边界几个侧面，但不检验 skill 是否真的负有因果责任。
- [SkillTV-Bench](./skilltv-bench.md) — 同样追问 skill 增强执行的旁观者能否看清实际发生了什么，只是站在轨迹评判者一侧。
- [SkillSV](./skillsv.md) — 同样用反事实删除 skill 内容，但目的是为 skill 的内部单元估值，而非审计溯源声明。
- [SkillShapley](./skillshapley.md) — 同样以反事实评估度量 skill 内容的因果贡献，粒度落在 skill 内部的单个步骤。
- [AgentAtlas](./agentatlas.md) — 同样主张 agent 的对话记录所呈现的内容，并不能可靠反映真正驱动其决策的因素。
