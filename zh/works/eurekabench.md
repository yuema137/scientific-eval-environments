# EurekaBench (2026)

> [English](../../works/eurekabench.md) | **简体中文**

> **首次公开：** 2026-09-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.00492)

## Overview

EurekaBench 要回答的问题是：一个能拟合观测数据的 agent，是否真的找到了数据背后的机制。agent 在科学模拟器里做最多四小时的实验，然后提交一个机制，形式包括文字说明、可执行代码和实验日志。judge 从三方面打分：预测准确度、是否遵守已知的科学约束，以及这个机制能否回答专家写的洞见问题。总分只在所有约束都通过时才计入准确度和洞见得分。一个模型如果为了贴合数据而违反了某条已知约束，总分就是 0。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** [EurekaBench: Measuring Agentic Ability to Discover New Scientific Insights](https://arxiv.org/abs/2610.00492)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.00492v1>
- **Project:** <https://eurekabench.github.io/>
- **Code:** <https://github.com/EurekaBench/EurekaBench>（README 写明首次发布日期为 2026/10/02）
- **Venue:** arXiv 预印本（cs.CL、cs.AI，2026）

## Summary

每道题都从一组初始观测出发，这些观测人类科学家已经部分解释过。agent 拿到一个工作区，里面有任务描述、一个连到环境的命令行接口（比如线虫 C. elegans 模拟器或托卡马克输运代码），有些题还附带训练数据。它要提交 `mechanism.md`、`mechanism.py` 和 `experiments.log`。两个 agent 形式的 judge 可以在环境里补做实验，但不能改动提交的机制。这种设计把拟合数据和解释数据分开：最好的 agent 在预测准确度上离人类参考只差 1.4 分，在洞见上却落后 27.3 分。

## Tasks

共 26 道经专家核验的题目，配有 306 个科学洞见问题。按领域分：神经科学 10、天体物理 7、等离子体物理 3、计算机科学 3、地球物理 2、化学 1。作者先咨询了来自 10 所大学的 15 位有博士学位的科学家，其中 10 位参与了构建。他们经过多轮讨论修订每份任务说明和每条评测标准，并确认每个洞见都有科学价值。洞见问题来自近期的人类研究、源研究中的开放问题，以及专家自己提出的洞见。用到的环境包括 c302（六道线虫题）、TRIBE v2（四道人脑题）、CAMELS 和 DREAMS 模拟套件、TORAX（一道边缘题另加 TokaMaker 和 GPEC）、FEniCSx、由 CAMELS-US 气象强迫驱动的 HBV 模型、在开放权重语言模型上做 LoRA 微调和 TransformerLens 分析，以及 AIMNet2-rxn。每个环境打包成一个 Apptainer 镜像。论文没有给出各领域的洞见问题数量。

## Domains

六个领域：神经科学（线虫神经回路与行为；人脑对视觉和语言输入的响应），天体物理（基于模拟套件的星系、星系环境、引力波、银河系、重子反馈，以及温暗物质并合树和星系族群），等离子体物理（ARC 托卡马克，以及负三角度位形的芯部和边缘场景），计算机科学（三道关于语言模型行为的题：陈述信念偏移、潜意识学习和电路发现），地球物理（冰架流动定律；水文中的流域属性），化学（反应发现）。大多数环境是模拟器；流域题用 CAMELS-US 的真实气象输入驱动模型，再给模拟径流加噪声。

## Evaluation

- **科学约束（SC）：** 每项约束测试记 1 或 0，所有测试都通过，机制才算通过。
- **预测准确度（PA）：** 每条标准在 [0, 1] 内打分，做法是在保留的测试数据上运行 `mechanism.py`。测试数据来自原始研究或针对该任务的模拟器。
- **科学洞见（SI）：** 每个洞见问题记 1 或 0，必须有完整的支撑证据才给分。
- **条件分：** SC 全部通过时，等于（PA 得分 + SI 得分）/（PA 标准数 + SI 标准数），否则为 0。报告的分数是 Claude Opus 4.8 和 GPT 5.6 Sol 两个 agent 形式 judge 各自条件分的平均。
- **人类参考：** 把人类科学家在每道题上已有的进展当作一份人类解答来打分：条件分 63.7%，PA 48.8%，SI 69.7%，SC 失败 0/26。
- **结果（Table 2，条件分 %）：** Claude Code 搭配 Claude Fable 5.1 为 29.8，Opus 5 为 27.3，Opus 4.8 为 18.4；Codex 搭配 GPT 6 Astra 为 28.7，GPT 5.6 Sol 为 19.4；OpenHands 搭配 DeepSeek V4 Flash 为 14.6，Kimi K3 为 12.9。所有模型都用最高推理强度。SC 失败从 10/26（GPT 6 Astra）到 17/26（GPT 5.6 Sol）不等。PA 最高为 47.4%（Fable 5.1 和 GPT 6 Astra），接近人类的 48.8%；SI 最高为 42.4%，而人类是 69.7%。Table 2 还给出每个 agent 的调用次数和美元成本，从 1.24 美元（DeepSeek V4 Flash）到 24.62 美元（GPT 6 Astra）。
- **失败分析：** 专家审阅日志后归纳出四类失败：依赖事先选好的假设；把任务优化当成机制发现；不用实验去消除不确定性；停留在观测层面不再深入。附录列出了十种更细的失败模式，但没有给出每种的数量。有 6.7% 的情况，judge 把实验日志里出现、但提交的机制并不支持的洞见也算了分。Claude Fable 5.1 在只按实验过程计分的洞见上得 22.7%，按机制计分则得 42.4%。
- **引导实验：** 在两道题（神经动力学和 ARC 托卡马克）上用 Claude Fable 5.1 测试。提示里写明科学目标后，SI 贡献分别提高 10.0 和 7.9 分；直接把洞见问题作为优化目标给出，则分别提高 32.5 和 15.8 分。作者认为后一种设置并不自然。
- Repository note：摘要说 agent 在预测准确度上超过人类科学家；但在 Table 2 汇总的 PA 列中，没有一个 agent 超过人类的 48.8%。
- Repository note：论文没有报告两个 judge 之间、或 judge 与专家之间的一致性统计。

## Typical Duration

每次运行一块 H100 GPU，最多 1,000 次迭代、四小时。论文没有说明 Table 2 中的调用次数和成本是按题计算还是总计。

## Main Contribution

把科学约束检查设成总分的门槛，并把机制对洞见问题的回答与预测准确度分开打分。这样，在保留数据上拟合得好，本身并不算一项发现。

## Key Design Ideas

- 三份提交物把因果解释（`mechanism.md`）、可检验的实现（`mechanism.py`）和实验记录（`experiments.log`）分开，judge 因此能检查一个洞见是由机制推出的，还是只出现在日志里。
- 允许网络搜索，但屏蔽每道题背后的原始论文和文献聚合站点。
- judge 本身是 agent，可以在环境里做新实验，而不是只把提交物读一遍。

## Strengths

- 同一张表分别列出 PA、SI 和 SC 失败，可以看出 agent 的 PA 能接近人类，SI 却远远落后。
- 以人类已有进展作参考，每个分数都能和科学家在同一道题上已经确立的结果放在一起比。
- 引导实验直接检验了 SI 偏低的一种解释：agent 漏掉洞见，是不是因为从来没人告诉它目标。

## Limitations

- 作者指出，洞见问题反映的是与专家一起选定的研究方向，评分标准之外的有效发现拿不到 SI 分。
- SI 依赖 judge 的推理。作者指出，judge 可能会接受说得很自信的结论；专家对部分提交物的审阅也表明，一些自动评分偏宽松。
- 作者说明，评测时的网络限制能挡住访问，但不能排除模型在预训练时接触过源研究。
- 覆盖不均衡：神经科学有 10 道题，化学只有 1 道。
- Repository note：论文没有说明每道题跑了几次。

## Related Works

- [HeurekaBench](./heurekabench.md) — 名字相近，也评测科学洞见的产生，但基于真实的单细胞数据分析。
- [DiscoverPhysics](./discoverphysics.md) — 同样让 agent 在模拟世界里做实验，并把提交的解释与预测分开打分。
- [Into the Unknown](./into-the-unknown.md) — 作者团队部分重合；agent 要沿开放方向写后续论文，而不是解释已知的观测。
