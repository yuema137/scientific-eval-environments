# AstroVisBench (2025)

> [English](../../works/astrovisbench.md) | **简体中文**

## Overview

AstroVisBench 是面向天文学科学计算与可视化的代码 benchmark：模型要先实现一套天文专属的数据处理工作流，再画出能传达预期科学洞见的图。可视化由一条 VLM-as-a-judge 流水线打分，这条流水线以五位职业天文学家的标注为对照做过校验。

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.20538>
- **Project:** <https://astrovisbench.github.io/>
- **Code:** <https://github.com/SebaJoe/AstroVisBench>
- **Data:** <https://huggingface.co/datasets/sebajoe/AstroVisBench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track

## Summary

AstroVisBench 瞄准的是多数代码 benchmark 会跳过的一步：模型产出的成果究竟有没有传达出正确的科学结果。每个实例都取自真实的天文教程 notebook，并被拆成 setup、processing、visualization 三个阶段；模型拿到 setup 阶段，需要分别写出 processing 代码和 visualization 代码。processing 的产出通过比对内存中的结果变量与真值变量来打分；visualization 的产出则由一个视觉语言 judge 对照参考图，判为 No Error、Minor Error 或 Major Error。对八个当代模型的评测显示，距离「够格当科研助手」还有很大差距：最强的模型也只在少数可视化任务上做到「No Error」。

## Tasks

432 个 processing 任务与 432 个 visualization 任务，取自 110 个 Jupyter notebook。notebook 来自两套精选的天文教程合集——Astro Data Lab 与 Space Telescope Science Institute。作者挑出最后一个单元格产出可视化的 notebook，抽取单元格之间的依赖关系，再把每个实例切成 setup、processing、visualization 三个阶段。

## Domains

天文学：工作流是针对 Astro Data Lab 与 STScI 教程语料中的天文巡天与空间任务数据所做的天文专属数据处理与作图，而正确性判定关心的是图里呈现的科学洞见对不对。次级共同领域是计算机科学 / 软件与系统工程，因为任务形式是在 Python 科学计算环境中生成并执行代码。

## Evaluation

- **processing 阶段。** 先执行生成的代码，再用变量检查分数把其结果变量与真值变量作比对：`VIscore = |V_M ∩ V_G| / |V_G|`，即对真值关键变量的召回率。执行崩溃另行统计为崩溃率。
- **visualization 阶段。** 视觉语言 judge 把生成的图与参考图对比，归入三种错误类别之一：No Error、Minor Error、Major Error。报告的指标包括未崩溃的可视化运行占比、针对可视化数量不对的响应统计的 VisFail 率，以及 CorrectV / MiE / MaE 的分布。
- **judge 校验。** 五位职业天文学家（均持天文学、天体物理或物理学博士学位）标注了 135 组可视化配对（270 张图）。错误类别上的标注者间一致性为 Fleiss' κ = 0.53，在五人共同标注的 30 个任务上两两 Spearman's ρ = 0.69。候选 judge 中，Claude 3.5 Sonnet 与专家标注的相关性最高，ρ = 0.822，因而被选作 judge。
- **报告。** 共评测八个模型——Gemini 2.5 Pro、Claude 3.7 Sonnet、Claude 4.0 Opus、o3-mini、GPT-4o、QwQ、Qwen-2.5、Llama-4 Maverick。Gemini 2.5 Pro 最强：processing 任务上崩溃率 30.8%、VIscore 0.600，visualization 任务上只有 15.7% 为「No Error」，重大错误则占 28.5%。

## Typical Duration

没有以单任务时间或 token 预算的形式报告。论文给出的是运行环境：在两颗 56 核 Intel Xeon MAX 9480 CPU、合计 128 GB 内存上执行，每次模型评测约需 100 GB 存储（约 50 GB 用于执行环境，50 GB 用于 pickle 对象）。生成阶段为 Claude 3.7 Sonnet 设了 1,024 token 上限，864 份响应中只有 10 份触到该上限。

## Main Contribution

首个把天文专属的科学计算与其结果的可视化放在一起评测的 benchmark，并配有一套以 LLM/VLM 为 judge 的可视化正确性评估——该评估以职业天文学家的标注为对照做过校验。

## Key Design Ideas

- 把真实教程 notebook 做三阶段拆解（setup / processing / visualization），既能独立为两种能力打分，又保留了真实的上下文。
- processing 阶段采用变量级打分，检查的是内存中的数据产物，而不是对代码或打印输出做字符串匹配。
- 可视化按科学正确性评判，采用分级错误分类（No Error / Minor / Major），而非像素或结构相似度。
- judge 的选取由与五位天文学家标注面板的实测相关性决定，而不是假定。
- 公开排行榜并发布执行环境，其中包含一份真值缓存，使重跑更省成本。

## Strengths

- 取材于精选的职业天文教程 notebook，工作流因此反映的是真实的档案数据与空间任务数据的使用实践，而非人造练习题。
- 可视化 judge 经过与领域专家的实证校准，一致性统计量是报告出来的，而不是断言出来的。
- 把 processing 与 visualization 分开，隔离出端到端代码 benchmark 会混为一谈的两种失败模式。

## Limitations

- 五位天文学家之间的标注一致性只是中等（Fleiss' κ = 0.53），这限制了可视化指标能有多强的区分力。
- Repository note: `VIscore` 衡量的是对真值变量的召回率，不惩罚多余的虚假变量，因此它也会奖励那些部分正确、同时又产出错误中间结果的工作流。
- Repository note: 该 benchmark 给每个阶段的单次代码生成打分，而不是带工具反馈的迭代 agent 循环，因此它衡量的是工作流的编写能力，而非长时程的自主研究。
- Repository note: 测评框架的存储占用相当可观（每次模型评测约 100 GB），推高了独立复现的成本。

## Related Works

- [SciVisAgentBench](./scivisagentbench.md) — 同样用 LLM judge 加确定性评估器为 agent 的科学可视化打分，但覆盖的是通用 SciVis 领域，而非天文 notebook。
- [Stargazer](./stargazer.md) — 同样是带可执行真值的天文评测，但它是迭代式的模型拟合环境，而非分阶段的代码与作图生成。
- [ScienceAgentBench](./scienceagentbench.md) — 同样跨科学学科、对照专家校验过的参考实现为生成的数据分析程序打分，但没有可视化正确性 judge。
- [SciCode](./scicode.md) — 同样是从研究工作流构建的科学代码生成 benchmark，靠执行而非视觉科学正确性来打分。
