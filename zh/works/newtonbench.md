# NewtonBench (2025)

> [English](../../works/newtonbench.md) | **简体中文**

## Overview

NewtonBench 是一个通过在模拟物理系统上进行交互式实验来评估 LLM agent 科学定律发现能力的 benchmark。它包含 324 个任务，由对 12 条经典物理定律施加反事实定律偏移（counterfactual law shifts）生成。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.07172>
- **Code:** <https://github.com/HKUST-KnowComp/NewtonBench>
- **Venue:** ICLR 2026

## Summary

NewtonBench 认为现有定律发现 benchmark 面临科学相关性、可扩展性与抗记忆性之间的方法学三难困境，并且把发现过度简化为静态函数拟合。它转而让 agent 通过迭代运行实验来揭示嵌入在模拟模型系统中的定律，共 324 个任务，均由经典物理定律的反事实偏移派生。在 frontier LLM 上的实验揭示出清晰但脆弱的发现能力：GPT-5 的总体 symbolic accuracy 达到 72.9%，但性能随系统复杂度与观测噪声急剧下降，而 code interpreter 可能促使较强模型过早从探索转向利用，反而降低其表现。

## Tasks

共 324 个任务：108 条偏移定律，每条在三种模型系统（Vanilla Equation、Simple System、Complex System）中实例化。偏移定律由 12 条经典定律经表达式树变异——修改运算符或数值常数——策划而来，Easy、Medium、Hard 三个难度层级按累计变异量划分（每级在前一级基础上再施加 1–2 次变异）。在每个任务中，agent 向 `run_experiment` 工具提交输入变量赋值、观察模型输出，并最终以符号表达式形式提交隐藏的目标定律。

## Domains

十二个物理领域，每个对应一条经典定律：牛顿万有引力定律、库仑定律、安培力定律、傅里叶定律、斯涅尔定律、放射性衰变、阻尼谐振动、马吕斯定律、理想气体中的声速、胡克定律、玻色–爱因斯坦分布与热传递。

## Evaluation

- **Symbolic accuracy.** 判定提交表达式与真值定律是否数学等价的二元指标，由 LLM-as-a-judge 协议检查并刻意忽略物理常数取值；论文报告其与人类专家的一致率为 98.3%。
- **RMSLE.** 所发现方程的预测值与真值输出之间的均方根对数误差，以连续的数据保真度分数补充二元判定。
- **Reported.** 在 11 个 LLM、两种配置上以四次运行取平均：Vanilla Agent 配置下 GPT-5 以 72.9% 的 symbolic accuracy 领先，Gemini-2.5-pro 达到 65.0%；加入 code interpreter 后两者分别降至 69.6% 与 62.0%。准确率从 Vanilla Equation 设定到 Complex System 设定急剧下降，而仅 0.0001 的高斯噪声即造成 13–15% 的准确率损失（在 GPT-5-mini 上测得）。

## Typical Duration

多轮交互式发现：agent 反复调用 `run_experiment` 构建自己的观测集，然后再提交定律。论文规定每个任务最多 10 轮实验、每轮至多 20 组输入参数；结果以四次运行的均值报告。

## Main Contribution

一个可扩展、抗记忆的 benchmark，将科学定律发现重构为交互式模型发现，要求 agent 对由反事实偏移物理定律支配的模拟系统进行实验探测。

## Key Design Ideas

- 反事实定律偏移：对表达式树施加变异、修改运算符或数值常数，生成貌似合理、旨在抵御靠背诵已知定律求解的变体。
- 交互式模型发现而非静态函数拟合：agent 通过 `run_experiment` 工具选择实验输入并观察输出，自行构建输入–输出对数据集。
- 三种模型系统设置——Vanilla Equation、Simple System、Complex System——在递增的周边混杂结构中嵌入同一目标定律。
- 两种 agent 配置——Vanilla Agent 与携带 Python 解释器的 Agent with Code Assistance——用以隔离工具访问对发现行为的影响。

## Strengths

- 靠变异生成任务将发现与背诵解耦：即使模型记得教科书定律，也仍须探明偏移后的定律有何不同。
- 变异生成器无需新的专家标注即可扩展任务集，同时让定律保持在科学上合理的形式。
- 难度、系统复杂度、噪声与工具访问相互独立地变化，暴露出论文记录的失败模式：随复杂度退化、对噪声极端敏感、以及工具诱发的满足化（satisficing）。

## Limitations

- Repository note: 评分对象始终是一条由教科书定律变异而来的闭式目标方程，且 LLM 判定的等价检查刻意忽略物理常数取值，因此常数标定不在考核之内。
- Repository note: 噪声鲁棒性结果仅在单一模型（GPT-5-mini）上于四个高斯噪声水平测得，frontier 模型的逐模型鲁棒性画像并未报告。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样评测 LLM agent 的科学发现能力，但其 102 个数据驱动任务取自 44 篇同行评审论文，而非由经典定律的反事实变体生成。
- [Aviary](./aviary.md) — 同样让 language agent 置身交互式科学环境，但它围绕真实生物学研究任务构建训练 gymnasium，而非面向模拟物理系统的评测套件。
