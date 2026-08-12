# Can Large Language Models Automate the HAZOP Process Without Human Intervention? (2026)

> [English](../../works/can-large-language-models-automate-the-hazop-proce.md) | **简体中文**

## Overview

一项对四个多模态大语言模型在危险与可操作性分析（HAZOP）上的对比评估：每个模型都在统一的提示词下，从同一张管道仪表流程图（P&ID）生成一份完整的 HAZOP 工作表，再对照专家编制的参考工作表打分。论文自陈的贡献是一套评估 LLM 做 HAZOP 的结构化框架，而不是一个 HAZOP 自动化系统。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://doi.org/10.1016/j.ssci.2025.107039
- **Venue:** Safety Science，第 194 卷，文章号 107039（2026）

## Summary

HAZOP 是流程工业中标准的结构化危险辨识方法，论文要问的是：当前的多模态 LLM 能否在无人介入的情况下端到端跑完整个流程，以及所得到的工作表是否足以支撑基于风险的决策。四个模型——GPT-4o、GPT-4o-mini、LLaMA 与 Gemini——各自拿到同一张 P&ID 和同一条标准化提示词，要求产出一份完整的 HAZOP 工作表。生成的工作表再从两个彼此独立的维度与专家参考工作表对照：模型层面的表现（输出相似度与成本），以及 HAZOP 层面的表现（所生成情景的有效性与所提防护措施的多样性）。论文的结论是：LLM 作为辅助工具有用，但无人监督的 LLM HAZOP 输出并不可靠。

## Tasks

一个评估任务，对每个模型各执行一次：在无人介入的前提下，用标准化提示词从同一张 P&ID 生成一份完整的 HAZOP 工作表——篇幅长达数十页。四个多模态 LLM 在完全相同的条件下对比（GPT-4o、GPT-4o-mini、LLaMA、Gemini）。Ground truth 是针对同一张图纸、由专家编制的参考 HAZOP 工作表。整个评估是在单一过程上做的受控模型对比，而不是一套跨多个过程的 benchmark 套件。

## Domains

化学工程——流程工业中的过程安全。受评对象是针对一张管道仪表流程图所做的 HAZOP 分析，涵盖过程偏差、原因、后果与防护措施；这项任务属于过程工程的危险分析，而非化学知识或分子层面的推理。未指派共同领域。

## Evaluation

生成的工作表从两个方面对照专家参考来评估。*模型层面的表现*看两项：一是与参考的相似度，以 F1 报告，四个模型都在 86% 以上；二是计算成本，以每份工作表的美元开销报告（LLaMA 成本效率最高，每份 $0.011）。*HAZOP 层面的表现*则看所生成情景的有效性与所提防护措施的多样性：语义上有效的情景占比在 0.19 到 0.37 之间，防护措施则严重偏向程序性/管理性手段。Gemini 每份工作表产出的情景最多（34.3），每个偏差对应的防护措施也最多（1.79）。把表面相似度与语义有效性拆开，正是这套评分协议的核心：文本上与参考高度重合，和真正有效的情景占比很低，这两件事完全可以同时出现。

## Typical Duration

每份工作表由一条标准化提示词一次生成完成，因此不存在多步轨迹的预算。论文报告的是每份工作表的货币成本（最低 $0.011），而非 wall-clock 时间或 token 预算。逐任务延迟为 `TODO(reference)`，摘要中未予说明。

## Main Contribution

按作者的表述，论文给出了一套评估 LLM 做 HAZOP 的结构化框架——把模型层面的表现（相似度、成本）与 HAZOP 层面的表现（情景有效性、防护措施多样性）分开——并用它回答 LLM 能否在无人介入下自动完成 HAZOP。所报告的答案是不能：那些按相似度指标看很贴近专家参考的工作表，其中语义上有效的情景占比却很低，因此 LLM 被定位为专家主导的 HAZOP 流程中的辅助工具。

## Key Design Ideas

- 固定输入（一张 P&ID、一条标准化提示词），使输出上的差异可归因于模型本身，而非提示词或过程的差异。
- 以专家编制的参考 HAZOP 工作表作 ground truth，而不是自动构造的答案键。
- 评分拆成两条彼此独立的轴——模型层面表现与 HAZOP 层面表现——使与参考的文本吻合无法替代领域有效性。
- 把所生成情景的语义有效性作为与相似度分开的量来测，从而暴露两者之间的落差。
- 把防护措施多样性纳入指标，捕捉模型倾向于给出程序性措施而非工程化保护层的偏好。
- 在质量之外同时报告每份工作表的货币成本，使成本效率成为一个显式的对比维度。

## Strengths

- 四个模型在完全相同的条件下受评，因此所报告的跨模型差异可被解读为模型效应。
- 相似度与有效性的拆分是论文最有信息量的结果：对照参考的 F1 高于 86%，而有效情景占比只有 0.19–0.37，直接说明相似度类指标会高估 HAZOP 能力。
- 评估锚定在来自真实过程安全实践的专家参考工作表上，而不是合成的答案键。
- 报告了每份工作表的成本，这在过程安全的 LLM 研究中很少被量化。
- 发表于经同行评审的过程安全期刊（Safety Science），因此其 HAZOP 方法论经过了领域读者的审读，而不只是 ML 圈的评审。

## Limitations

- 评估只用了一张 P&ID，所以结果刻画的是模型在单个过程上的行为，而非跨一系列单元操作或装置构型的表现。
- 摘要中未描述任何具名、已发布的 benchmark 制品；贡献是一套评估协议加一项对比研究。参考工作表与生成的输出是否公开发布，标记为 `TODO(reference)`。
- Repository note: 一个过程、四个模型的设计，支撑不起关于模型排名的统计性主张；所报告的逐模型差异都是单实例观测。
- Repository note: 情景有效性是一个靠判断得出的量，而摘要既未说明由谁判定，也未给出评分者间一致性。`TODO(reference)`。
- Repository note: 场景是单轮的工作表生成，不是交互式或会用工具的 agent，因此它并不评估诸如查询仿真器或迭代改进设计之类的 agent 行为。

## Related Works

- [PSE-Bench](./pse-bench.md) — 过程系统工程题目 benchmark，其过程设计子集包含 HAZOP 与 LOPA。
- [CeProBench](./ceprobench.md) — 化工过程开发 benchmark，覆盖 PFD 解析与 Aspen Plus 参数优化。
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](./ctrl-alt-recover.md) — 用 LLM agent 在流程装置上做受安全约束的故障恢复。
