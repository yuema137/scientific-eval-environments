# SimAgents (2025)

> [English](../../works/simagents.md) | **简体中文**

## Overview

SimAgents 是一个多 agent LLM 系统：它读取宇宙学模拟论文，把论文中的模拟配置参数还原成模拟软件可以直接接受的形式。系统随附一套人工标注的评估数据集，收录 40 余项已发表模拟，并配有对照单 agent 基线的参数级评分协议。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.08958>
- **Code:** <https://github.com/xwzhang98/SimAgents>
- **Demo:** <https://youtu.be/w1zLpm_CaWA>

## Summary

论文的出发点是计算宇宙学中的一个具体瓶颈：复现一项已发表模拟所需的参数散落在密集的正文里，模型不同、格式各异，把它们翻译成可执行的配置既慢又容易出错。SimAgents 把这件事交给一组分工明确、通过结构化讨论协作的 agent——Physics Agent 用领域知识解读论文，Software Agent 依模拟代码用户手册中写明的约束把关，Analysis Code Writer 则在配置确定之后生成可视化与初步分析代码。为检验抽取出的配置是否正确，作者从 arXiv 以及 ApJ、MNRAS 等期刊收集 40 余项模拟，逐一人工标注全部相关的参数/取值对，构成评估数据集，再在人工评分与自动评分两种方式下，把 SimAgents 与 chain-of-thought、exchange-of-thought 两个基线作对比。

## Tasks

40 余项模拟，取自 arXiv 及主流期刊（论文点名 ApJ、MNRAS）上的已发表论文，模拟类型多样。每篇论文都人工标注了与 MP-Gadget 相关的全部参数/取值对：宇宙学参数（Ωm、Ωb、ΩΛ、h、σ8、ns）、初始条件设置（BoxSize、Ngrid、Redshift）以及关键的模型开关。agent 的任务是读论文并给出对应的参数集合，同时满足模拟软件用户手册的约束；随后由第二个模块生成 Python 代码，用于功率谱可视化、三维密度场绘图，以及对模拟输出的初步统计分析。公开仓库以 `golden_standard` 目录的形式提供这批标注，覆盖 IllustrisTNG、Millennium、MTNG、Magneticum、SIMBA 等主要宇宙学模拟项目的已验证参数。本工作只支持 MP-Gadget 这一种模拟代码。

## Domains

天文学。评估目标是宇宙学模拟的配置：标注真值由宇宙学参数（物质、重子与暗能量密度、哈勃参数、σ8、谱指数）和 MP-Gadget 的初始条件设置构成，参考模拟则取自公认的宇宙学结构形成模拟套件。参数所描述的宇宙学模型使物理学成为次级共同领域。

## Evaluation

评分在参数层面进行。抽取出的参数/取值对与人工标注比对，得到真阳性、假阳性与假阴性，据此计算 precision、recall 与 micro-F1；另有一套误差分类，按 Value Error、Type Error、Hallucination 统计每项模拟的平均错误数。两个基线在相同条件下对比：单个 LLM agent 的零样本 chain-of-thought（CoT），以及两个初始化完全相同的 agent 相互讨论的 exchange-of-thought（EoT）。人工评估下（表 1），SimAgents 的 micro-F1 达到 98.67%，precision 97.80%、recall 99.55%，而 CoT 为 93.64/92.46/94.84，EoT 为 94.95/93.87/96.05。误差分类上（表 2），SimAgents 平均每项模拟 0.46 个 Value Error、0.02 个 Type Error、0.30 个 Hallucination，CoT 为 0.97/0.51/0.21，EoT 为 1.21/0.21/0.34。自动评估给 SimAgents 的数字略低：micro-F1 98.13%、precision 97.77%、recall 98.50%。主力骨干模型是 GPT-4；换成 Qwen3-4B 的消融实验则退化到 micro-F1 81.23%，每项模拟 3.05 个 Value Error、2.59 个 Type Error。

## Typical Duration

论文未报告 wall-clock 或 token 预算，而是把交互预算记为 Physics Agent 与 Software Agent 之间结构化讨论的轮数：一到四轮的消融实验表明两轮的 micro-F1 最高，继续增加轮数并不带来提升。

## Main Contribution

一套面向任务分工的多 agent 拆解方案，把已发表的宇宙学模拟描述转化为符合软件规范、可直接执行的配置：其中一个 agent 承担物理推理，另一个 agent 负责落实模拟代码自身的约束。工作同时贡献了人工标注的宇宙学参数抽取评估数据集，并以实测表明这种专门化分工优于单 agent 的 chain-of-thought，也优于对称的双 agent 讨论。

## Key Design Ideas

- 两个抽取 agent 在设计上就不对称：Physics Agent 提供领域解读，Software Agent 提供源自手册的有效性约束——exchange-of-thought 基线隔离出来的正是这一差别。
- 采用多轮结构化通信而非单次通过，轮数当作可调超参处理，实测定为两轮。
- 软件合规性是被计分的属性，而不是事后过滤：Type Error 与 Value Error 分开统计，「物理上说得通、软件上却非法」的输出因此得以显形。
- 幻觉自成一类错误，把凭空杜撰的参数与读错的取值区分开。
- 真值逐篇论文由人工标注而非由模型生成，并随系统一同发布。
- 同一批输出既有人工评分也有自动评分，两者的差距因此是可测的，而不是靠假定。
- 管线并不止于配置，而是继续生成分析代码（功率谱、三维密度场），把「从论文到可运行分析」这条链路闭合。

## Strengths

- 评估数据集人工标注、公开发布，且取自真实的已发表模拟，而非合成。
- 基线是真正的外部对照（chain-of-thought 与 exchange-of-thought），而不只是所提系统的消融。
- 误差分类把单一 F1 会混为一谈的失败模式区分开；即便在幻觉这一项上 SimAgents 并非最优，该数字也照样报告。
- 小骨干模型的消融（Qwen3-4B 对 GPT-4）量化了结果有多少依赖前沿模型、多少来自架构本身。
- 人工评估与自动评估都有报告，且结果高度一致，这支持把自动评分协议当作可复用的打分器。

## Limitations

- 作者说明，受时间所限，只标注了文献中可执行文件的一个版本，更多数据点与可执行版本有待补充。
- 支持范围仅限于少数几个预训练模型，模拟软件也只有 MP-Gadget 一种；作者把扩大软件与模型覆盖列为未来工作。
- Repository note: 评估数据集规模不大——40 余项模拟——且没有单独命名，因此它更像是这套系统的验证集，而不是一个可长期沿用的 benchmark。
- Repository note: 只有参数抽取被计分。分析代码生成模块，以及用抽取出的配置真正跑出的模拟是否正确，都只做了演示而未评估，因此对已发表模拟的端到端复现并未被测量。
- Repository note: 所提系统的 micro-F1 报告值都在 98% 以上，这个数据集上留给后续方法的区分空间已经很小。
- Repository note: 论文没有记录任何发表 venue，公开仓库也没有回指论文的链接。

## Related Works

- [CosmoPaperQA](./cosmopaperqa.md) — 同样评估 LLM 系统从宇宙学论文中抽取科学内容的能力，但以问答而非可执行配置来打分。
- [ReplicationBench](./replicationbench.md) — 天体物理复现任务，同样以「从文字描述还原已发表结果」为目标。
- [HiSciBench](./hiscibench.md) — 含文献抽取与数据驱动发现两个层级，覆盖天文学等多个学科。
- [ScienceAgentBench](./scienceagentbench.md) — 评的是 agent 能否从任务描述产出可运行的科学分析代码。
- [gwBenchmarks](./gwbenchmarks.md) — 另一个天体物理场景，agent 同样必须满足领域软件与精度约束，而不是产出文字。
