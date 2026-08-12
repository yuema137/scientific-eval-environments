# Large Language Model-Based Multi-Agent Systems for Automated Foundation Design (2026)

> [English](../../works/large-language-model-based-multi-agent-systems-for.md) | **简体中文**

## Overview

一套面向岩土工程地基基础设计的 27 算例评测方案——涵盖浅基础与桩基——配一份四准则评分细则，用来比较九种配置：单体 LLM、顺序式 agentic 工作流，以及一个由路由器驱动的多 agent 系统，它先对送入的设计问题分类，再分派给对应的专家 agent。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)
- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://doi.org/10.1007/s43503-026-00088-8>
- **Preprint:** <https://arxiv.org/abs/2506.13811> — 流传时的标题为「Investigating the Potential of Large Language Model-Based Router Multi-Agent Architectures for Foundation Design Automation: A Task Classification and Expert Selection Study」
- **Venue:** AI in Civil Engineering (Springer)，第 5 卷，2026

## Summary

作者观察到，综述 LLM 在建筑工程中的应用时，几乎找不到有工作把 LLM 用在实务核心的那些基本工程计算上；而已有的岩土研究依赖检索增强的单体 agent，且只在狭窄的浅基础数据集上验证过。他们构建了一条基于路由器的多 agent 工作流：先由双层分类器把桩基问题与浅基础问题分开，再路由到按计算类型划分的专家 agent，其后依次接技术审核 agent 与高级工程师 agent，产出最终的工程报告。为评测它，作者定义了一个覆盖七类地基基础设计问题的 27 算例测试方案、一份四维度评分细则（在计算精度之外还评推理质量、复杂情景处理与输出结构），以及每个算例重复执行三次的规程，用以暴露运行间的波动。九种配置在该方案下比较：四个单体前沿 LLM、在两个不同基座模型上实例化的两种常规顺序式 agentic 工作流，以及同样落在这两个基座模型上的所提路由系统。

## Tasks

27 个不同的测试算例，覆盖岩土工程问题的七个主要类别。浅基础分析贡献 15 个算例，涵盖尺寸设计计算、容许荷载确定、承载力计算与沉降分析。桩基评估贡献 12 个算例，分属四个专门类别：尺寸设计计算、含侧摩阻力与极限承载力的承载力分析、预应力混凝土桩的沉降计算，以及包含荷载分配与弹性沉降行为的群桩分析。算例以简短的专业设计题面提出，给定土层剖面、荷载与安全系数——例如在给定恒载、活载、地基容许承载力与安全系数的条件下，求能承受风致弯矩的基础尺寸 B × L；又如计算一根 15 m 长、截面 0.45 m × 0.45 m、埋置于砂土中的混凝土桩的极限侧摩阻力与容许承载力。结果按准则分列报告：浅基础组为 Finding Dimensions、Allowable Load、Bearing Capacity、Settlement 与 Factor of Safety，桩基组为 Finding Dimensions、Bearing Capacity、Settlement 与 Pile Group。每个算例执行三次，以计入 LLM 的随机性。这些测试算例在论文中有描述，但未作为公开数据集发布。

## Domains

土木与结构工程，属其岩土分支。受评目标是地基基础的设计结果——基础尺寸、极限与容许承载力、瞬时沉降与固结沉降、安全系数、群桩效率与荷载分配——依既有设计方法算得（浅基础用 Terzaghi 承载力理论及其形状与深度系数扩展，桩基用 Vesic 方法计算桩端阻力与侧摩阻力），且全文将其定位为需要专业把关的、涉及安全的土木工程实务。不指派共同领域：土力学只是所设计基础本身的力学，而 LangChain、n8n、OpenRouter 与 SerpAPI 都是工具，不是受评对象。

## Evaluation

- **评分细则。** 四条准则，每条按四级评分——Excellent 2.0、Good 1.0、Needs Improvement 0.5、Poor 0.0。四条准则是：(1) 计算精度，涵盖承载力、边坡稳定与地基设计结果；(2) 思维链推理，即模型是否说明了每一步计算或设计决策的由来、逻辑是否完整；(3) 复杂情景处理，即在非标准边界条件与多因素问题上的鲁棒性；(4) 输出格式的一致与结构化，即输入、计算与最终结果是否以一致的结构呈现。分数按准则以百分制报告，并取平均。
- **协议。** 每个测试算例在相同输入条件下执行三次，以隔离模型随机性。报告的指标包括数值精度、输出格式一致性、计算方法有效性与无效输出的出现频率。
- **架构消融。** 比较三种工作流配置：完整的路由系统；Agentic Workflow I，去掉路由子系统，只剩静态的 Designer → Reviewer → Senior Engineer 顺序管线；以及 Agentic Workflow II，在其上加入迭代精修回路，赋予 Reviewer 驳回或要求修改的权限。
- **浅基础结果（平均得分）。** 所提路由系统配 Grok 3，95.00%；单体 Grok 3，86.25%；所提路由系统配 Gemini 2.5 Pro，82.50%；DeepSeek R1，77.50%；Agentic Workflow II 配 Grok 3，73.75%；Gemini 2.5 Pro-preview 与 Agentic Workflow I 配 Grok 3，71.25%；Agentic Workflow II 配 Gemini 2.5 Pro，72.50%；ChatGPT 4.0-turbo，58.75%；Agentic Workflow I 配 Gemini 2.5 Pro，38.75%。
- **桩基结果（平均得分）。** 所提路由系统配 Grok 3，90.63%；单体 Grok 3，87.50%；所提路由系统配 Gemini 2.5 Pro，84.38%；Gemini 2.5 Pro-preview，81.25%；DeepSeek R1 与 ChatGPT 4.0-turbo，75.00%；Agentic Workflow II 配 Grok 3，62.50%；Agentic Workflow II 配 Gemini 2.5 Pro，56.25%；Agentic Workflow I 配 Gemini 2.5 Pro 与配 Grok 3，均为 51.56%。
- **主要对比。** 路由配置在浅基础上比单体 Grok 3 高 8.75 个百分点，在桩基上高 3.13 个百分点，并以 10.0 至 43.75 个百分点的差距超过常规顺序式工作流。在群桩分析上，它在两个基座模型下都达到 100%，而常规工作流只有 50.00–68.75%。
- 评分细则由谁执行——人类专家评分者还是自动 judge——论文未作说明：`TODO(reference)`。

## Typical Duration

N/A — 未报告任何单算例的轨迹长度、wall-clock 时间或 token 预算。协议层面给出的唯一数量，是每个测试算例三次独立执行。

## Main Contribution

作者提出了他们所称的首个专为地基基础工程设计的路由式多 agent 系统，具备智能任务分类与专家选择能力；与之配套的是一套面向岩土工程 AI 模型的多维评测方法学，在 27 个测试算例上以每例重复执行三次的方式，对计算精度、思维链推理、复杂情景处理与输出结构一致性一并打分。他们主张，在涉及安全的岩土应用中，只看精度指标是一种危险且不完整的评估，因为正确的最终数字也可能出自有缺陷的推理。

## Key Design Ideas

- 双层分类：第一层把桩基问题与浅基础问题分开，因为二者所需的分析方法根本不同；第二层再路由到具体的计算专家（桩长、桩承载力、桩沉降、群桩；或基础尺寸、承载力、沉降、安全系数、容许荷载）。
- 计算方法直接写进每个 agent 的系统提示词，而不靠检索获取，工程师因此可以通过改提示词指定偏好的设计方法或当地设计规范；论文完整复现了浅基础与桩基的系统提示词。
- 有意舍弃 RAG：作者认为检索会把性能绑在文档切分质量上，在工程术语之间存在语义漂移，遇到新型问题时表现下降，且无法区分作废与现行的设计规范。
- 每个专家提示词内含一个 one-shot 的范例解答，并明确要求避免「视情况而定」或「查表确定」这类模糊措辞；若问题条件不足，则应说明还需要哪些数据。
- 一条模仿职业实务的两级质量保证尾链：Technical Reviewer agent 对照设计规范核查计算、给出 1–10 的质量评分并判定 PASS 或 REQUIRES REVISION，随后由 Senior Engineer agent 把最终的工程报告整理成型。
- agent 可使用网络搜索（SerpAPI）获取现行标准，而非依赖固定的知识库。
- 评分细则把推理质量与输出结构同数值精度一道列为一等维度。

## Strengths

- 评测同时覆盖浅基础与深基础，而论文所综述的既有岩土 LLM 研究大多局限于浅基础。
- 评分细则完整公开，四条准则各有明确的等级描述，判分标准因此可供检视。
- 架构做了消融，而不只与单体模型比较：去掉路由与去掉精修回路分别测试，从而把路由的贡献单独隔离出来。
- 每个算例执行三次，正面回应了运行间波动，而不是只报单次成绩。
- 每种配置都报告分准则的结果，暴露出各模型的弱项所在（例如 Grok 3 在 Finding Dimensions 上强，在 Factor of Safety 上弱）。
- 论文明确表示该系统是需要人类持续把关的计算辅助工具，而不是自主设计的替代品。

## Limitations

- 作者表示 27 算例、七个类别的测试集是一项显著局限，只代表职业岩土实务中所遇场景的一小部分。
- 测试算例未作为数据集发布，评测集也未命名，因此结果既无法独立复现，也无法在论文之间比较。
- Repository note: 细则中非精度的那几个维度（推理质量、复杂情景处理、输出结构）属于定性判断，而论文既未报告由谁评分、用了几位评分者，也未给出评分者间一致性。
- Repository note: 路由系统与各基线用同一份细则评分，但路由系统自身的管线里含有一个会给出质量评分、并能触发返工的 Reviewer agent，因此参与比较的各配置在推理期算力上也存在差异，而不只是架构差异；论文未报告任何成本、时延或 token 核算。
- Repository note: 论文给出了重复执行三次以降低方差的动机，却未公布逐次试验的离散度或方差统计，只给了平均分。

## Related Works

- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — 同样以一个小型、专门编制的土木工程题集来测量 LLM agent 的运行间可靠性。
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — 用人工精选的结构分析题集在一个工程框架内比较各 LLM，本文引其为先前工作。
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — 本文所用多 agent 分工在结构分析一侧的对应物。
- [PE Civil Bench](./pe-civil-bench.md) — 土木执业资格考题配上 agent 化的钢筋混凝土设计管线，覆盖同一设计计算问题的结构一侧。
