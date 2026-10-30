# OSWorld-Science (2026)

> [English](../../works/osworld-science.md) | **简体中文**

> **首次公开：** 2026-09-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.39903)

## Overview

通用的 computer-use benchmark 考的是办公、浏览器和文件管理这类任务，看不出 agent 会不会用科学家真正在用的软件，比如化学结构编辑器、病理切片查看器、CFD 软件包或统计软件。OSWorld-Science 把 OSWorld 的那套设置搬到了这些软件上。agent 读一道科学任务，看着屏幕，在按领域构建的 Ubuntu 镜像里用 pyautogui 代码或命令行操作。一局结束后，任务专属的评测器检查软件状态和 agent 产出的文件，给满分或部分分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** [OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software](https://arxiv.org/abs/2609.39903)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2609.39903v1>
- **Project:** <https://discoailab.github.io/osworld-science-page/>
- **Code:** <https://github.com/DiscoAILab/OSWorld-Science>
- **Data:** <https://huggingface.co/datasets/SciAILab/OSWorld-Science-data>（题目和 Docker 镜像）
- **Venue:** arXiv 预印本（cs.AI，2026）

## Summary

每个任务都在为其领域构建的 Ubuntu 镜像里运行，科学软件已经装好，输入文件也已就位。每一步 agent 拿到当前截图和最近五组“截图加回复”，然后返回一段 pyautogui 代码，或者 `<WAIT>`、`<DONE>`、`<FAIL>` 之一；146 个任务中有 122 个还允许用命令行。一局结束后，只对收集到的软件状态和输出文件打分。以 ASKCOS 里的逆合成任务为例，评测器检查保存下来的结果是否满足任务要求；单一答案的任务做精确匹配，完成的步骤可以拿部分分；仿真任务只要报告的参数误差落在设定范围内就算通过。这个 benchmark 测的是在给定任务上使用现有软件。标题里的“learning”指的是任务从教程出发来设计，并没有实验单独考察 agent 怎样学会一款陌生软件。

## Tasks

共 146 个任务，分布在七个领域：化学 43、物理 31、医学 26、统计 20、生物 18、地理信息 6、语言学 2。任务最多的几款软件是 QuPath 23、ChemDraw 21、ASKCOS 21、SAS/R 20；其余 61 个任务用到 OpenFOAM、ANSYS、EEGLAB、PyMOL 和 MestReNova、QGIS、CIAO 加 DS9、Weasis、3D Slicer、Praat 和一个 PDF 阅读器。任务有两种来源：一是有博士水平知识的领域专家按模板编写，二是从一份基准教程出发、由 AI 辅助生成，再和人一起反复修改。TODO(reference)：专家人数。Repository note：论文的环境部分说有 17 个软件包，结果部分用的是 14 套配置；第 3 节列出的是神经科学，第 4 节列出的却是统计。

## Domains

化学（分子结构绘制、逆合成），物理（在 OpenFOAM 和 ANSYS 里做 CFD 和有限元仿真，在 CIAO/DS9 里分析 X 射线数据），医学（在 QuPath 里分析病理图像，以及放射影像查看器），统计（在 SAS 和 R 里做统计计算），生物（PyMOL 里的结构生物学、MestReNova 里的 NMR、药物协同分析、EEG 分析），地理信息（QGIS）和语言学（Praat）。

## Evaluation

- **打分方式：** 基于执行结果，任务专属的评测器读取一局结束后的软件状态和产出文件；奖励在 [0, 1] 之间，全部要求都满足才得 1。不用 LLM judge，也没有报告人类基线。
- **模型：** 12 个视觉语言模型，使用修改过的 OSWorld PromptAgent harness（Kimi K3 用的是官方自带的设计）。
- **平均任务得分，含部分分（每题成本）：** Claude Fable 5.1 73.7%（6.5 美元）、Claude Opus 5 57.9%（6.7 美元）、GPT-6 Astra 57.4%（7.7 美元）、GPT-5.6 Sol 50.1%（2.79 美元）、GPT-5.6 Terra 31.8%（2.0 美元）、Kimi K3 30.2%（11.7 美元）、Claude Sonnet 5 26.3%（3.6 美元）、GPT-5.6 Luna 22.6%（0.23 美元）。
- **按领域看：** 化学最难（Fable 5.1 约 44%，Opus 5 约 39%）；Fable 5.1 在生物上约 96%。
- **1,530 次公开运行的失败统计：** 402 次（26.3%）拿到满分。去掉 20 次被 harness 终止和 8 次未判定的运行后，没拿满分的 1,100 次里，667 次没有交出可评分的产物，其中 613 次是步数用完；400 次内容错误，33 次产物无效。84 个只有占位内容的产物里，GPT 模型占了 78 个，其中 77 个在化学领域。
- **消融（23 个 QuPath 任务，每格只跑一次）：** Opus 5 的平均分在历史窗口为 1 步时是 35.2，10 步时是 57.0；换任务语言后，Opus 5 的得分在 29.7（中文）到 53.1（日文）之间。经 Bonferroni 校正后，没有一格与默认设置有显著差异。

## Typical Duration

多数任务上限 100 步，每步回复限 16k token，每次回复最多执行 10 个动作。没有报告每题的实际耗时。TODO(reference)：每题耗时。

## Main Contribution

一个建立在真实科学软件上的 computer-use benchmark 和一套可复现的环境，覆盖七个领域；评测器基于执行结果检查软件状态和输出文件，并给部分分。

## Key Design Ideas

- 每个领域有自己的 Docker 镜像，商业和开源科学软件都从固定的初始状态启动。
- 打分只看一局结束后收集到的状态和文件，不看 agent 自己怎么说。
- 任务允许时 agent 可以用命令行，所以测的是能不能把任务做完，而不只是会不会点 GUI。
- 公开的数据带有污染水印，便于事后检测是否被拿去训练。

## Strengths

- 打分基于执行结果，不用 judge，每个任务都定义了部分分。
- 每个模型的得分旁边都列出了每题 API 成本。
- 失败统计覆盖全部公开运行，把步数用完、内容错误和产物无效分开计数。

## Limitations

- 作者承认领域分布不均匀：地理信息只有 6 个任务，语言学只有 2 个。
- 消融只在 QuPath 任务上做，每格只跑一次，校正后没有一项显著。
- 部分软件需要授权，因此有些轨迹没有公开。
- 有几个任务依赖在线服务（SAS OnDemand、SynergyFinder、RCSB API、AlphaFold DB）；论文指出改成本地部署就能去掉这层依赖。
- Repository note：每个模型在每个任务上只跑一次，没有方差估计。

## Related Works

- [OSWorld](./osworld.md) — 本 benchmark 沿用了它的 harness 和设置，并扩展到科学软件。
- [EngiWorld](./engiworld.md) — 同样让 agent 通过 GUI 或 CLI 操作专业软件，并用程序检查产出文件。
- [CADWorld](./cadworld.md) — 同样是 computer-use benchmark，只针对 FreeCAD 这一款科学工程软件。
