# PhysClosureBench (2026)

> [English](../../works/physclosurebench.md) | **简体中文**

> **首次公开：** 2026-10-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.21767)

## Overview

PhysClosureBench 把两件事分开打分：agent 做出了多少正确的物理，以及它的研究到底有没有回答给定的问题。每道题给出一个研究目标，来自强场物理、阿秒物理或相邻领域，研究怎么做由 agent 自己决定。20 条标准组成的 Atomic Score 给局部步骤计分，比如设定是否正确、是否算出了要求的观测量、机制是否有依据。另有一个研究闭合等级（Research Closure，RC0–RC4），看完整回答所必需的证据和适用范围条件是否都已具备。所以一次尝试可以拿到 9/10，却仍然没有闭合。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** [From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research](https://arxiv.org/abs/2610.21767)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.21767v1>
- **Code:** <https://github.com/uncertainty2019/PhysClosureBench>（MIT 许可证的运行框架和一个示例案例 Case 30；README 说明完整的 50 个案例放在 Hugging Face 数据集 `Tauben/PhysClosureBench`）
- **Venue:** arXiv 预印本（cs.AI，2026）

## Summary

每道题给出科学目标、物理设定、关键参数、必要约束，以及 CPU 和墙钟时间预算，但不规定流程，也不规定验证顺序。agent 在断网的容器里独立工作，自己写数值代码、自己运行，最后提交一份报告，附上推导、执行记录和支撑每条结论的产物。GPT-5.6-Sol 评分器按案例细则分阶段评分。原子标准和闭合要求分别评定，因此 RC 并不是 Atomic Score 上的一条分数线。在 1,050 次尝试中，得分不低于 8/10 的有 229 次，其中 83 次（36.2%）没有达到 RC4。

## Tasks

共 50 道目标明确的研究题，每道都改编自 Physical Review Letters、Physical Review A 等期刊上的一项已发表研究。按方向分：强场原子分子与阿秒物理 24，固体与凝聚态强场物理 12，量子光学与量子光–物质相互作用 8，强场 QED 与相对论动力学 4，物质波与 Kapitza–Dirac 效应 2。一位有超快和强场物理研究经验的领域专家设计并监督了半自动的构建流程，其他专家审查了任务有效性和评分标准。每道题背后的源结果在收录前都经过人工复现，复现的开销用来设定资源上限。以 Case 30（基于 Bray 等人 2018 年的工作）为例：在库仑势和结合能相同的屏蔽势下，电离后的散射如何随激光强度和屏蔽长度改变阿秒钟（attoclock）的角偏移？指令禁止网络搜索、外部 agent 和目标论文的材料。

## Domains

物理：强场与阿秒原子分子物理、强场凝聚态物理、量子光学、强场 QED 与相对论量子动力学，以及物质波衍射。每道题都是计算研究，证据由 agent 用代码自己生成；论文没有提到以实验数据作为任务输入。

## Evaluation

- **Atomic Score（0–10）：** 每个案例 20 条二值标准，每条 0.5 分，分布在表述（F）、输出（O）、识别（I）、机制（M）和验证/适用范围（V）五个维度。全部 1,000 条原子标准中，机制占比最大（369 条，占分值 36.9%）。对某次尝试所走路线不适用的标准记为 N/A，仍保留 0.5 分。
- **研究闭合：** RC4 完全闭合；RC3 主要结论有支撑，但在验证或适用范围上还有实质缺口；RC2 核心证据已有，但核心机制或其他关键要求没有解决；RC1 缺少一项必需的主要输出或分支；RC0 核心科学对象无效或缺失。RC 由哪些不可或缺的要求还没满足来决定。
- **评分：** GPT-5.6-Sol（high）先独立给出初评，再做针对性复核；只有当剩余的实质分歧可能改变分数、RC 或尝试有效性时，才启动裁决。五位受过物理训练的专家复查了 200 条挑选出的标准级判定（有效 192 条），与自动评分一致的占 81.8%；在与闭合相关的标准上，一致率为 75.9%（79 条中 60 条）。
- **模型：** Claude-Opus-5、GPT-5.6-Sol 和 Qwen-3.8-Max 用 xhigh 推理强度；Kimi-K3、DeepSeek-V4.1-Flash、GLM-5.3-Flash 和 Gemini-3.1-Pro 用 high。全部在 OpenCode 1.18.17 中运行，每题独立跑三次，共 1,050 次尝试。
- **结果：** 平均 Atomic Score 为 6.29（Claude-Opus-5）、5.83（GPT-5.6-Sol）、5.17（Kimi-K3），其余模型都在 4.50 或以下，最低 2.85（Gemini-3.1-Pro）。前三名的 RC4 比例分别为 32.7%、22.7% 和 19.3%，Gemini-3.1-Pro 只有 0.7%。DeepSeek-V4.1-Flash 有 10.7% 的尝试达到 RC4，但也有 50.0% 停在 RC0。
- **闭合卡在哪里：** 高分但未达 RC4 的尝试，识别和机制两类标准分别有 16.0% 和 20.8% 没满足；达到 RC4 的尝试对应只有 2.1% 和 3.0%。在整个基准上，适用范围论证的满足率是 86.9%，必需的验证是 59.6%，由风险触发的验证是 47.8%。
- **可重复性：** Claude-Opus-5 在 50.0% 的题上至少一次达到 RC4，三次全部达到的只有 18.0%；GPT-5.6-Sol 为 40.0% 和 10.0%；Kimi-K3 为 40.0% 和 4.0%。

## Typical Duration

各案例的上限从 8 到 96 个 CPU 核、30 到 720 分钟墙钟时间不等。运行到时限的尝试按当时已有的结果评分，不因超时额外扣分。论文没有报告 token 或美元成本。

## Main Contribution

把研究闭合作为单独的结果来评分，标准是各题特有的不可或缺的要求。它与细粒度的 Atomic Score 一起报告，能看出 agent 有多频繁地做完了大部分局部步骤，却没有回答研究问题。

## Key Design Ideas

- 固定问题和有边界的设定，不固定路线：任何有效的证据路径都可以达到 RC4。
- 每个源结果都人工复现一遍，既用来确认可行性，也用来校准 CPU 和墙钟时间预算。
- 分别报告"至少一次达到 RC4"和"三次都达到 RC4"，把能达到闭合与能稳定达到闭合区分开。

## Strengths

- 全部 1,050 次尝试的 Atomic Score 与 RC 联合分布，直接显示两个指标在哪里分道扬镳。
- 人工核查覆盖了全部 50 个案例，并单独报告与闭合相关的标准上的一致率。
- Case 30 的对比追踪了同一道题上的三次运行，分别到达 RC4、RC3 和 RC2。它把误读计算趋势（Gemini-3.1-Pro）和机制有支撑但适用范围没解决（GPT-5.6-Sol）这两种情况区分开。

## Limitations

- 覆盖集中：50 道题里有 24 道属于强场原子分子或阿秒物理。
- 人工与评分器的一致率总体为 81.8%，在与闭合相关的标准上为 75.9%。论文说明，复查的标准是按科学上的重要性挑选的，并不是从所有原子标准中均匀抽样。
- Repository note：所有尝试都由同一个评分模型 GPT-5.6-Sol 打分，而它也是被评测的模型之一。
- Repository note：题目改编自已发表研究。运行时禁止网络搜索和目标论文材料，但论文没有描述针对预训练阶段接触的进一步控制。
- Repository note：N/A 标准保留 0.5 分，所以 Atomic Score 会给不适用的标准计分；论文说明这并不表示相应工作已经完成。

## Related Works

- [PRL-Bench](./prl-bench.md) — 长程物理研究子任务，采用细则评分；论文 Table 1 与之做了对比。
- [CritPt](./critpt.md) — 研究级物理难题，答案可机器验证，而不是开放式研究。
- [PaperBench](./paperbench.md) — 按细则评研究复现；论文认为它没有评估研究闭合。
