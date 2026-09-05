# InnovatorBench (2025)

> [English](../../works/innovatorbench.md) | **简体中文**

> **首次公开：** 2025-10-31 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2510.27598)

## Overview

InnovatorBench 把 AI 研究 benchmark 的目标从「复现这个结果」改成了「超过它」。复现类套件给 agent 一篇论文，看它把已发表的数字还原得多接近，这奖励的是忠实度，说明不了 agent 能不能想出更好的方法。InnovatorBench 的做法是：把一篇已发表论文自己的代码库里那部分关键创新连同 commit 历史一起删掉，把剩下的仓库、数据和一份不给操作步骤的任务描述交给 agent，再把评分标定成「照搬原方法大约得 80」。想拿更高分，agent 就必须自己设计点东西。配套环境 ResearchGym 之所以存在，是因为这个目标要求运行动辄几个小时、横跨多台 GPU 机器，agent 得会起后台任务、轮询结果、管理自己的时间预算，而不是一条条发阻塞式命令。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.27598>
- **Code:** <https://github.com/GAIR-NLP/InnovatorBench>
- **Dataset:** <https://huggingface.co/datasets/GAIR/InnovatorBench>
- **Venue:** ICLR 2026 · official listing <https://iclr.cc/virtual/2026/poster/10006754>

## Summary

这项来自上海交通大学、上海创智学院和 GAIR 的工作是一套「benchmark 加平台」：20 个取自 14 篇有影响力论文的 LLM 研究任务，以及承载这些任务的环境 ResearchGym。每个任务提供一个起始工作区，里面有预装好的 conda 环境、数据集与 checkpoint，以及原论文的仓库（多数是 LlamaFactory 或 Verl，关键创新的实现和 git commit 历史都已删除，但仓库照样跑得起来），另外还有一份只讲目标、不讲步骤的任务描述。agent 通过 `eval` 动作提交产物；外部评分服务先检查提交格式，不合格直接返回 0 和一条错误信息，合格则套用任务专属的评分函数，该函数经过标定：baseline 落在 0 附近，标注者复现原论文得到的参考解落在 80 附近。因为评分跑在工作区之外，agent 既够不到参考数据，也改不了打分器。在五个前沿模型驱动同一个轻量 ReAct agent 的实验中，Claude Sonnet 4 以 24.01 的加权平均终分领先，没有任何模型接近参考解。

## Tasks

**20 个任务，取自 14 篇发表于 NeurIPS、ICLR、COLM、EMNLP、ACL 的有影响力论文**，覆盖六个 LLM 研究方向：数据构建、数据过滤、数据增强、损失设计、奖励设计、脚手架构建。具体例子包括：构建医学英语–泰米尔语平行语料并微调 Llama-3.1-8B-Instruct 做翻译；在 Verl 中实现一个 GRPO 变体，既避免 RL 训练中的熵坍缩又把数学推理准确率拉高；在 Verl 中设计奖励函数训练 Qwen2.5-3B 做检索增强推理；以及基于 GPT-4.1 和网页工具搭一个提示驱动的深度研究 agent。

每个任务条目包含七个部分：动机、任务、数据、约束、评估、环境、脚本；此外还配有起始工作区、评估脚本，以及一份由原始研究产物推得、对 agent 隐藏的参考解。约束都是操作层面的：工作时长上限、GPU 配额、输出文件格式。每个任务都备有提示（hint），但不放进工作区：agent 想看就得调 `view_hint` 工具，并为此从终分里扣掉一部分。主实验把这个工具关掉了，消融实验则直接把提示接在任务描述后面给出。

任务构建遵循四条原则：任务能够重做一遍，结果与原论文对得上；结果能在两天内取得显著改进；这组任务能考察 agent 的不同能力；任务使用 Llama-3.1、Qwen2.5、Qwen2.5-VL 这类常见模型。单个任务需要 2 到 36 小时完成。

Repository note：论文的图 6 与表 4 对 20 个任务在数据构建和数据过滤之间的划分说法不一致（图 6 是 3 和 4，逐条列出的表 4 是 4 和 3）。其余四类两处一致：数据增强 5、损失设计 3、脚手架构建 3、奖励设计 2。

## Domains

AI 与机器学习研究。研究对象就是 LLM 研究本身：训练数据的构建、过滤与增强；监督微调和 RL 微调的损失函数设计；面向可验证奖励强化学习的奖励设计；以及 agent 脚手架构建。其中若干任务是多模态的，例如为 Qwen2.5-VL-7B-Instruct 增强科学图文数据，以及在 GPT-4o 上搭建视觉推理工作流。

## Evaluation

- **Kaggle 式提交 + 标定过的分数。** agent 最多可调用 `eval` 四次，用满后系统自动结束任务。每次提交先过格式校验，不合格返回 0 和错误信息；合格提交则在 baseline（约 0）与参考解（约 80）之间做线性插值打分。终分（最后一次提交）与最好分都会报告。
- **一个任务从头走到分数。** 在 GRPO 损失设计任务里，agent 要在 Verl 中实现一个损失变体，既让 RL 训练过程中的熵不坍缩，又提升数学推理准确率。评估脚本读取 agent 的输出，算出一个准确率分和一个熵分，返回 `准确率 × 熵 × 100`；整个评估在可写工作区之外、对照隐藏的参考数据运行，所以靠对齐格式或改写打分器抬不高这个数。
- **实测结果。** 在 ReAct 式 agent 下，Claude Sonnet 4 的加权平均终分 24.01、最好分 24.54，在六个方向中的四个领先；GPT-5 为 12.04 / 12.52，GLM-4.5 为 11.85 / 13.35，Kimi-K2 为 5.35 / 5.45，Qwen3-32b 为 0.00 / 0.00，原因是上下文窗口太小。GPT-5 的例外是脚手架构建，拿到 60.07。所有模型在数据类方向上都比算法类高，作者的解释是：数据任务对小瑕疵有容忍度，而一个不完美的损失或奖励会导致梯度爆炸或系统性错误的策略。
- **提示消融。** 给出真值提示后，损失设计（终分 12.98 → 22.65）和奖励设计（11.56 → 15.06）明显提升，但数据构建、过滤、增强三项反而下降，加权平均从 24.01 掉到 13.88。作者据此判断，数据类任务卡住 agent 的是编码功底，不是缺想法。
- **失败案例分析。** 论文用 trace 片段记录了四类失败：沉不住气（预算还剩 21 小时就把训练任务停掉）、资源管理失当（推理任务还占着 GPU 就启动整卡训练脚本，撞上 CUDA OOM）、库选得不好（一直用 Transformers 而不换 vLLM，因为时间预算这个约束给不出可学习的效率信号），以及模板化推理（自己合成不出真正的思维链后，把一个空洞的模式批量拼接到每条数据上）。

## Typical Duration

每个任务 2 到 36 小时的 agent 工作时间，任务约束里写明了工作时长上限和 GPU 配额。test-time scaling 曲线显示，agent 要跑过 11 小时才达到 InnovatorBench 上的最好成绩，而在 PaperBench 上大约 1.75 小时就到顶，达到饱和所需的时间约为后者的 6.5 倍。每个任务的费用和执行时间也有报告：不给提示时 Claude Sonnet 4 平均每任务 5.13 小时、32.92 美元，给提示时为 4.87 小时、30.86 美元。

## Main Contribution

一个以超越（而非复现）已发表参考解为目标的 benchmark，外加研究环境 ResearchGym。ResearchGym 支撑这类任务所需的长时、多机、异步执行，作者也明确把它定位成可以脱离本 benchmark 复用。

## Key Design Ideas

- 参考解锚定在 80 附近，而不是量表顶端，评分函数因此在原论文之上还留有空间，考的是创新而不是复刻。
- 起始仓库保持原项目可运行，但把论文关键创新的实现和 git commit 历史都删掉了，agent 继承到的是基础设施，既不是答案，也没有能顺藤摸瓜找回答案的线索。
- 评估完全在 agent 的可写工作区之外运行，参考数据隐藏，这堵住了改打分器和凑输出格式这两条常见捷径。
- ResearchGym 提供 42 个原语动作，分为 Command、File、Parse、Web Search、Web Browse 五族，并把动作的执行与选择解耦：绑定到某个 session 的命令会在 agent 继续规划时接着跑，输出稍后用 `get_session_output` 取回。另有一个专门的 `sleep` 动作，免得训练任务还在跑的时候，agent 拿一堆没意义的动作把等待时间填满。
- agent 可以通过 HTTP 同时驱动多台机器或 Docker 容器，每台机器运行一个 HTTP 服务接收并执行终端命令，分布式训练类任务因此才写得出来。
- 快照记录任务说明、agent 的上下文、工作区最终状态和剩余时间预算；系统可以从任意快照恢复，快照还能分叉，实验因此能从不同的点续跑。
- 只有数据构建和数据增强开放网页搜索与浏览；论文说其余任务一律关闭，但没有给出理由。

## Strengths

- 评分完全确定：准确率、F1、BLEU、熵等任务专属指标由外部脚本计算，链路中没有 LLM judge。
- 提示消融是一次受控实验，不只是评论：它把「agent 不知道该做什么」和「agent 做不出它知道的东西」分开，而两者的答案在不同任务方向上并不相同。
- 论文按模型和研究方向报告了墙钟时间与美元开销，并把它们和分数列在一起；与 PaperBench 的 test-time scaling 对比也把时间尺度上的差距量化了出来，而不是空口断言。
- 环境与 benchmark 分开发布，文档也说明了如何扩展，新任务和新评估协议可以在同一套底座上贡献进来。

## Limitations

- 六个方向一共只有 20 个任务，单个方向 2 到 5 个，方向级别的分数因此建立在很少的样本上。
- 没有实测的人类基线。锚点是标注者对原论文的复现实现，不是限时的专家尝试。
- 源论文都已发表，而除了从起始仓库中删掉关键实现和 commit 历史、把参考解藏起来，论文没有说明别的污染控制手段。
- 所有结果都出自同一个轻量 ReAct 式 agent，模型效应与 harness 效应没有分开。
- Repository note：把参考解锚定在 80 附近的标定是逐任务的，论文没有公布各任务的插值常数，因此这些分数在本套件内可跨模型比较，但不能直接理解为参考解性能的百分比。

## Related Works

- [MLRC-Bench](./mlrc-bench.md) — 同样用客观指标给新方法打分，衡量的是基线到顶尖人类之间的差距。
- [MLGym](./mlgym.md) — 同样是 Gym 式环境配开放式 AI 研究 benchmark，但任务更短，也不涉及分布式执行。
- [PaperBench](./paperbench.md) — 面向复现的 benchmark，InnovatorBench 用它作为 test-time scaling 的对照。
- [AI4AI-Bench](./ai4ai-bench.md) — 同样要求 agent 在冻结的研究仓库里、在明确算力预算下重新设计学习算法。
