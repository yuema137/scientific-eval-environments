# A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis (2026)

> [English](../../works/a-large-language-model-empowered-agent-for-reliabl.md) | **简体中文**

## Overview

一个含八道梁结构分析题的 benchmark，配两项定义明确的指标——可靠性（同一题重复运行中输出正确的比例）与鲁棒性（荷载位置与边界条件变化时，可靠性保持稳定的程度）。作者先用它刻画一个裸 LLM，再在同一组题目上刻画一个生成 OpenSeesPy 代码的 agent。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.02938>
- **Venue:** Structure and Infrastructure Engineering (Taylor & Francis)，2026 年 2 月 19 日在线发表，pp. 1–16，<https://doi.org/10.1080/15732479.2026.2630123>

## Summary

结构分析要求精确的数值计算，当今最强的 LLM 在这类任务上究竟有多可靠、多稳健？论文正是为回答这个问题专门搭了一个小 benchmark。作者构造八道静定梁题目，每种题目配置采样 Llama-3.3 70B Instruct 500 次以测可靠性，再把荷载位置扫一遍、重新采样以测鲁棒性。结果显示模型对静力学有定性的把握，定量上却不可信；于是作者把任务从文本生成改写为代码生成，构建一个 agent 输出 OpenSeesPy 代码、执行它，并用 OpsVis 把结果画出来。同一套 benchmark、同样两项指标再用到 agent 上，改造前后的对比因此站在同一基准上。

## Tasks

八道梁结构分析题，每题都要解出一根静定梁的支座反力——包括大小与方向。用到两种典型梁型，跨度同为 10 m：一是简支梁，二是滚动支座设在跨中（5 m）的外伸梁。每种梁型各配四种荷载工况：(I) 10 kN 集中荷载；(II) 作用于 1 m 区段上的 10 kN/m 均布荷载；(III) 10 kN 集中荷载叠加满跨 10 kN/m 均布荷载；(IV) 10 kN 集中荷载叠加 1 m 区段上的 10 kN/m 均布荷载。每道题以一段文本提示给出，说明几何、支座条件、荷载条件与要求输出的量。另有三道扩展梁题——两种支座位置与荷载方向各异的外伸梁配置，加一根带固定支座的悬臂梁——用作留出的泛化任务，提示词组件的消融实验也在这三道题上做。

## Domains

土木与结构工程。受评目标是对承重构件作结构力学判断：通过静力平衡分析求梁的支座反力，扩展任务还要输出弯矩图与剪力图。论文明确把工作放在土木工程范畴内，并把梁分析视为迈向更大结构体系之前的基础一步。未指派共同领域——OpenSeesPy 是手段，而非受评目标。

## Evaluation

- **可靠性** = N_correct / N_total，其中 N_total = 同一题提示独立运行 500 次。提示词的若干写法在预备步骤中先行筛选，测量开始前就固定为表现最好的那一版。
- **鲁棒性** = (1 + CV)⁻¹ = (1 + σ_R / R̄)⁻¹，取值落在 (0, 1] 的归一化分数；把荷载沿梁以 1 m 为间隔从一端移到另一端，对由此得到的一组可靠性值计算，分数越高越稳健。
- **Llama-3.3 70B Instruct 的报告结果。** 简支梁：集中荷载下平均可靠性 87.1%，局部均布荷载下 93.6%；集中荷载与满跨均布荷载或局部均布荷载叠加时，降至 75.8% 与 73.1%。四种简支梁工况的鲁棒性为 0.881、0.952、0.949、0.937。外伸梁则在荷载移入外伸段后急剧劣化：鲁棒性为 0.577、0.691、0.588、0.590，其中集中荷载叠加满跨均布荷载一例的可靠性跌到 10.0% 以下。
- **所提 agent 的报告结果。** 在全部 benchmark 工况上可靠性高于 0.990、鲁棒性高于 0.996；论文结论部分表述为可靠性超过 99.0%、鲁棒性超过 99.6%。三道扩展泛化任务各运行 500 次，可靠性分别为 100%、99.8% 与 99.6%。
- **提示词组件消融**（三道扩展任务上的可靠性；最后一列为鲁棒性）。完整模板：1.000 / 0.998 / 0.996，鲁棒性 0.998。去掉完整示例：0.000 / 0.000 / 0.000。去掉函数用法示例：0.026 / 0.296 / 0.623，鲁棒性 0.513。去掉规定性约束：0.936 / 0.970 / 0.556，鲁棒性 0.781。去掉思维链：1.000 / 0.998 / 0.784，鲁棒性 0.882。

## Typical Duration

`N/A — the paper reports no per-task wall-clock, token, or cost budget.` 每种受测配置都采样 500 次，因此报告的统计量靠的是大量重复采样，而不是单条长轨迹。

## Main Contribution

作者把这项工作定位为评估并提升 LLM 在结构工程中可靠性与鲁棒性的第一步：为梁的静力平衡分析构建 benchmark，说明当前最强的开放权重 LLM 虽对结构力学有定性把握，却达不到工程实践所要求的定量可靠性与鲁棒性，并证明把任务改写为面向领域求解器的代码生成，就能补上这一缺口。

## Key Design Ideas

- 重复采样写进了指标本身，而不是事后补一条误差棒：可靠性定义在同一提示的 500 次独立运行之上，测的就是运行之间的不一致。
- 鲁棒性是第二条正交的轴，定义在一次系统性的参数扫描上——荷载以 1 m 为步长沿梁移动——而不是定义在提示词的改写上，因此考的是对工程配置本身的敏感性。
- 鲁棒性分数取「1 加变异系数」的倒数作归一化，把取值限定在 (0, 1]，使不同题目之间可比。
- baseline 与所提 agent 在同样八道题上、用同样两项指标衡量，从而把「文本生成 → 代码生成」这一范式转变单独隔离出来。
- 结构化提示模板拆成五个具名组件（角色设定、思维链、完整示例、函数用法示例、规定性约束），逐一单独消融。
- 生成的 OpenSeesPy 代码自动执行，所得模型由 OpsVis 渲染，给出可供人工核对的轴力图、剪力图与弯矩图。

## Strengths

- 对涉及安全的工程任务而言，「可靠性 + 鲁棒性」这一对指标比单次准确率更为敏锐，而 500 次采样的预算也让报告的曲线足够稳定。
- 荷载位置扫描暴露出一种固定测试集完全看不到的失效模式：荷载落在支承跨内时裸模型表现尚可，一旦移入外伸段便全面崩溃。
- 消融是决定性的，而非装点门面：去掉完整示例后，三道扩展任务的可靠性全部归零，直接指出究竟哪个提示词组件在支撑性能。
- 扩展泛化任务用到的支座类型、支座位置与荷载方向，既不见于 benchmark，也不见于提示示例。

## Limitations

- benchmark 规模很小，且刻意保持初等：八道题、两种梁型、单一跨度，限于静定结构的静力平衡，未触及超静定结构、框架、动力问题与设计问题。
- 作为 baseline 只刻画了 Llama-3.3 70B Instruct 一个模型；没有闭源模型或更大的开放权重模型在该 benchmark 上受测。
- agent 的残余错误只作定性诊断：在悬臂梁自由端幻觉出一个多余的滚动支座；均布荷载与集中荷载叠加时，把均布荷载的作用范围拉长。
- 作者指出，结构越复杂，仅靠文字描述就越难说清，并把视觉语言模型列为后续工作。
- Repository note: 论文未说明代码或数据集的公开情况，因此该 benchmark 只能依据正文中的图与题目描述复现。
- Repository note: 本卡片的全部统计数据均依据 arXiv 预印本（v1，2025 年 6 月 27 日）核验；正式发表的期刊版本无法获取，其中的数字可能在审稿中有所修订。

## Related Works

- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — 同一团队的直接后续工作，把设定从一维梁扩展到二维框架，并配了一个新的 20 题 benchmark。
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — 同一脉络扩展到不规则三维框架，判分依据是数值响应的一致性，而非代码能否执行。
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — 独立的同期工作，同样是基于 OpenSeesPy 的结构分析 benchmark，也测量运行之间的稳定性。
- [StructureClaw](./structureclaw.md) — 同样评估 agent 在 OpenSees 支撑下做结构分析，规模为工作台级，并采用冻结的参考求解器响应。
- [FEABench](./feabench.md) — 同样是语言驱动的有限元工程，走的是 COMSOL 的 API，而非 OpenSeesPy。
