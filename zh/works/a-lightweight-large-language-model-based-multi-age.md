# A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis (2025)

> [English](../../works/a-lightweight-large-language-model-based-multi-age.md) | **简体中文**

## Overview

一个含二十道二维建筑框架结构分析题的 benchmark，每题独立运行十次；随之提出的是一套由五个 agent 组成、以 Llama-3.3 70B 驱动的管线，把框架的文字描述转成可执行的 OpenSeesPy 有限元代码。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.05414>
- **Venue:** arXiv preprint (cs.CL), 2025 年 10 月 6 日

## Summary

同一团队此前做的是一维梁，这篇把设定推进到二维框架：作者搭了一个二十题的多跨多层平面框架 benchmark，用它说明通用 LLM 无法为这类框架构造出有效的有限元模型。所提系统把建模任务拆给五个专职 agent——问题分析、几何、代码翻译、模型校验与荷载——全部由轻量的 Llama-3.3 70B Instruct 驱动。其核心设计取舍在于一次两阶段切分：几何推理先用自然语言理清，再输出为结构化的 JSON 拓扑，之后才动手写代码，于是 LLM 做的是受约束的翻译，而不是开放式的代码生成。随后由一个基于工具、确定性执行的模型校验 agent 去重节点与单元、重编号标识，最后才施加荷载。

## Tasks

二十道各不相同的二维框架结构分析题，由竖向柱与水平大梁构成。题集既有从真实建筑抽象而来的拓扑，也有合成生成的：3-2-3 框架（第一跨三层、第二跨两层、第三跨三层）取自巴黎圣母院，3-4-3 框架则改编自卢浮宫的 Mollien 馆。其中五题为三跨框架，十五题为五跨框架；五跨框架各跨的层数在一到五之间独立采样，因而形成不规则的层数轮廓。所有跨度均为 6 m。边界、荷载与材料条件在整个题集中保持一致：底部一律固定支座，每根梁上沿竖直向下施加 10 kN/m 均布荷载，最左跨每层顶部施加一个向右的 50 kN 集中荷载。材料参数固定为 E = 2 × 10¹¹ Pa，柱与大梁的截面面积和惯性矩各不相同，柱为 2 × 10⁻³ m²、1.6 × 10⁻⁵ m⁴，大梁为 6 × 10⁻³ m²、5.4 × 10⁻⁵ m⁴。每道题以结构化的文字描述给出，涵盖几何、边界条件、荷载条件与材料属性。

## Domains

土木与结构工程。受评对象是多跨多层的建筑框架——论文把它们表述为从工业厂房到高层建筑的承重骨架——受评产物则是该框架的有效有限元模型及其轴力、剪力与弯矩响应。benchmark 中有两种拓扑抽象自真实建筑。未指派共同领域；OpenSeesPy 是工具，而非受评目标。

## Evaluation

- 二十道题每题独立运行十次，以计入 LLM 的随机性。准确率即正确生成的代码数占总运行次数的比例。
- **所提多 agent 系统（Llama-3.3 70B Instruct）。** 多数情况下准确率超过 80%。三跨框架在全部试验中都做对。五跨框架的十五道题平均 88%，最低的是 2-4-3-2-5 与 2-3-3-2-5 框架的 70%，以及 2-3-1-4-5 框架的 60%。
- **原始 Llama-3.3 70B Instruct baseline。** 二十道题全军覆没：十次运行无一例外终止于语法错误。错误来源分布为单元定义 61.0%、节点定义 27.5%、支座条件 7.0%、材料属性 4.5%。人工修正语法错误后，还原出的几何暴露出更深层的失败——本该是正交网格，却出现带斜杆的桁架式构形；跨间交点处节点重复；各跨被建成互不相连的独立个体，没有共享节点。
- **Gemini 2.5 Pro。** 平均准确率 37%，各题从 90% 一直分布到 0%。生成的 200 个程序中有 88.5% 能无运行时错误地执行，所以它的失败是几何层面而非语法层面的：漏掉节点、在不相邻的跨之间乱连、多出层数。
- **ChatGPT-4o。** 二十道题、十次试验全部 0%，错误中有 89.0% 出在单元定义，6.5% 在节点定义，2.5% 在荷载施加，2.0% 在支座条件。
- 一项消融把几何 agent 与代码翻译 agent 合成单个一体化 agent、给以相同提示，用以分离「几何推理与代码生成分开做」这一设计的贡献。

## Typical Duration

`N/A — the paper reports no per-task wall-clock, token, or cost budget.` 每道题重复十次独立试验。

## Main Contribution

作者把这个 benchmark 与轻量多 agent 系统一并提出，作为 LLM 驱动有限元建模从一维梁迈向二维框架的关键一步——到了框架这一层，空间推理与拓扑一致性成为真正的瓶颈约束——并表明基于开放权重 70B 模型的分解式管线，在该任务上胜过体量大得多的通用模型。

## Key Design Ideas

- benchmark 把真实建筑拓扑与随机采样的层数轮廓混在一起，因而不规则、不对称的框架也在其中，而不只是规整网格。
- 荷载、支座与材料属性在二十道题中完全一致，把几何拓扑单独隔离为受测变量。
- 几何推理经由结构化 JSON 中间表示与代码生成解耦，LLM 不必在同一步里同时理清拓扑和语法。
- 几何 agent 遵循固定的确定性拼装顺序——从左到右逐跨、自下而上逐层——并受四条专家给定的显式规则约束，规则写明每一步各增加多少节点与单元。
- 模型校验 agent 走的是工具路线而非生成路线：由确定性的 Python 函数完成节点去重、单元去重、节点重编号与单元重编号，agent 只负责解读这些函数的纠正动作。
- 失败分析按来源（节点、单元、支座、材料）给出错误分类，而不是一个笼统的准确率数字；并且先人工修好语法错误再可视化还原出的框架，从而把几何问题与语法问题分开看。

## Strengths

- baseline 之间的落差既鲜明又有信息量：两个前沿通用模型只拿到 37% 与 0%，而分解式的 70B 管线在多数题目上超过 80%，这清楚地指明了难点所在。
- 把语法有效性与几何正确性分开、并且两者都测，能抓住「代码跑得很干净、建的却是另一个结构」这种情形。
- benchmark 在实践中确有复用价值：同一团队后续两篇论文都把这套二十题题集直接用作评测平台。
- OpsVis 对几何、荷载分布与内力图的可视化，为「究竟建出了什么模型」留下可供人工核对的痕迹。

## Limitations

- 二十道题规模不大，且荷载、边界与材料条件在所有题目中固定不变，因此只有几何拓扑在变。
- 所有框架都是平面的、弹性的；三维体系、非线性、动力问题与设计决策均未纳入评测。
- 判定正确与否看的是生成的代码及所得模型，而不是把结构响应与一份独立计算的数值参考作比对。
- 当拼装序列很长、条件性规则频繁触发时，系统依然脆弱，在最难的五跨框架上跌至 60%。
- Repository note: 论文未说明代码或数据集的公开情况。
- Repository note: 同一团队的两篇后续论文——一套减少幻觉的多 agent 架构（arXiv 2603.07728）与一个跨 OpenSees/SAP2000/ETABS 平台的变体（arXiv 2604.09866）——都是原样复用这个 benchmark 而非扩展它，因此在这二十道题上报告的增益，是在一个固定且如今已被充分摸透的靶子上累积起来的。

## Related Works

- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — 同一团队的前作，做的是一维梁，指标为可靠性与鲁棒性。
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — 同一团队的后续，扩展到不规则三维框架，正确性判据更严。
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — 另一团队独立提出的 20 题 OpenSeesPy 二维框架 benchmark。
- [StructureClaw](./structureclaw.md) — 同样评估 agent 在 OpenSees 支撑下做结构分析，采用冻结的参考求解器响应与交互式鲁棒性算例。
- [MooseBench](./moosebench.md) — 同样核查生成的仿真工件是否编码了预期的模型，而不止于能跑通。
