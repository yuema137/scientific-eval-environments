# SCI-AGENT-EXAM (2026)

> [English](../../works/sci-agent-exam.md) | **简体中文**

> **首次公开：** 2026-10-23 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.32441)

## Overview

SCI-AGENT-EXAM 在同一道题上，把科学 agent 运行的代码和它写的报告当作两个独立的评分通道。很多基准只看最终答案，或只看可执行结果。这里 120 道题每一道都要求交出结构化答案、可执行产物和一份书面报告。确定性检查器在隐藏输入上重跑代码，LLM judge 按专家写的细则评报告。两个通道分开报告，就能看出 agent 什么时候为一段没有正确执行的分析写了一份很有说服力的报告，也能看出反过来的情况。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** [SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks](https://arxiv.org/abs/2610.32441)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.32441v1>
- **Code and data（论文给出的地址）：** <https://github.com/SKYLENAGE-AI/Sci-Agent-Exam>
- **Venue:** arXiv 预印本（cs.CL，2026）

## Summary

每道题是一个带版本号的任务包：指令、冻结的离线 Docker 环境、agent 可见的文件、隐藏的参考解答、带权重的程序化检查，以及人工撰写的评分细则。agent 通过统一的 Claude Code harness 在容器里工作。结束后，检查器导入它的代码或读取它的产物，在隐藏数据上重跑计算；judge 则按细则评报告。每道题的分数按任务类型固定的权重把两部分合起来，程序化部分的权重从 Code Generation 的 0.70 到 Literature Synthesis 的 0.20 不等。两个分项分数总是和最终分并列报告。作者还沿每条轨迹对工作区快照重新打分，看质量是什么时候达到的，之后有没有丢掉。

## Tasks

120 道题，分属论文提出的科学工作流任务分类（SWTT）中的七种类型：Literature Synthesis 10、Hypothesis Validation 16、Tool Orchestration 28、Code Generation 20、End-to-End Analysis 25、Error Diagnosis 11、Result Interpretation 10。题目来源包括近期研究论文、科学竞赛和数据集，以及仍在活跃维护的开源项目；只使用允许再分发的许可证。每道题由一位博士水平的专家设计，搭建任务包和参考解答，并在写完解答之后再写细则。参考报告在自己的细则下必须拿到至少 90%。很多题埋了陷阱，比如一个由有泄漏的流程生成的现成看板，或者一个最显眼、却过不了下游物理约束的统计量，只有走完整个流程才能得分。共有 156 位领域专家参与。每道题都要经过一位独立审稿人和一位审核人，两人一致率须达到 85%。举个例子：在 `bioinformatics-end-to-end-analysis-02` 中，agent 要根据挂载的一篇论文和 14 个数据文件，选出一条在四个压力维度上都稳健的宏基因组组装与分箱流程。评分用 20 条细则（权重 70）和 8 项程序化检查（权重 30），其中一项是把所有标识符重新标号后的留出重放。

## Domains

11 个领域（Table 2 的题数）：生物学 15、科学计算 13、物理科学 12、生物信息学 11、化学 11、物理模拟 11、计算机科学 10、数据科学 10、材料科学 10、数学 9、工程 8。论文没有说明"物理科学"和"工程"类的题目具体属于哪门学科。

## Evaluation

- **程序化分数：** 检查函数取值在 [0, 1]，按权重求平均。检查内容包括执行状态、数值是否在声明的容差内、输出格式、必需文件、在允许扰动下是否不变，以及各题特有的约束。缺少某个产物时，依赖它的每项检查都记零分。
- **LLM-judge 分数：** 二值细则条目按权重求平均，涵盖科学正确性、执行与验证、来源依据、表达和完整性。judge 是 GPT-5.6 Sol。它能看到来源摘录和细则，但看不到参考分数；依赖缺失文件的条目在预检阶段直接判为不通过。平均每道题约有 8 项程序化检查和 20 条细则。
- **流程：** 十个模型都在 Claude Code 中以 high 推理强度运行，每道题跑三次。分数先在三次运行间取平均，再对题目做宏平均。Pass@0.95 是最终分不低于 0.95 的运行所占比例。
- **结果（Table 3，最终分 / Pass@0.95）：** GPT-6 Astra 80.9 / 26.0%；Claude Fable 5 67.3 / 9.7%；Claude Opus 5 64.2 / 10.5%；Qwen3.8 Max 62.7；Kimi K3 62.6；GPT-5.6 Sol 59.6；Claude Opus 4.8 57.1；GLM-5.3 55.9；Grok-4.6 52.4；DeepSeek-V4-Pro 50.9 / 1.9%。
- **执行与报告：** judge 分 ≥ 0.5 而程序化分 < 0.5 的题目结果所占比例，从 0.14（GPT-6 Astra）到 0.48（DeepSeek-V4-Pro）。案例分析里，一次 DeepSeek-V4-Pro 运行程序化得 1.00、judge 只给 0.43；一次 Claude Opus 5 运行 judge 给 1.00、程序化只得 0.11。
- **轨迹：** 每次读写文件后的快照都重新打分，用来衡量提前完成、下滑（之前通过的标准后来不通过）、恢复，以及遗憾（到最后仍不通过）。GPT-5.6 Sol 在五个细则维度上的平均下滑率为 27.0%，GPT-6 Astra 为 18.3%。
- **敏感性（50 题子集）：** 把 Claude Code 换成 Codex 后，Kimi K3 和 GLM-5.3 分别下降 15.9 和 20.1 分，GPT-5.6 Sol 则提高 14.3 分。推理强度从 high 调到 max，九个模型的平均分从 61.8 升到 65.1。
- Repository note：摘要称 judge 是"calibrated, expert-validated"。论文描述的校准，是要求每份参考报告在自己的细则下至少得 90%；论文没有报告 judge 与人工评分者之间的一致性统计。

## Typical Duration

在论文所说的"peer subset"上，每次运行的平均成本从 5.13 美元（Claude Opus 4.8）到 57.96 美元（GLM-5.3），运行时间从 22.0 到 56.6 分钟，交互轮数从 30.2 到 102.4（GLM-5.3）。GPT-6 Astra 平均 20.79 美元、22.1 分钟。出题者每道题大约花六小时。

## Main Contribution

在七类工作流任务的每一道题上，都要求交出答案、可执行产物和报告，并把执行正确性和报告质量作为两个分开报告的分数，使任何一方的失败都没法藏在另一方里。

## Key Design Ideas

- 每类任务在评测任何模型之前就固定了权重，决定这类题更看执行还是更看报告。
- 隐藏输入重跑、标识符重新标号和输入扰动，让写死的答案和取巧的解法拿不到分。
- 细则由出题者在写完参考解答后亲自撰写，不由 LLM 生成。

## Strengths

- 分项分数总是和最终分并列，"报告写了、代码没跑对"这类失败因此可以计数。
- 快照重评分在最终状态之外，还记录质量何时达到、之后是否保住。
- harness 和推理强度的敏感性实验表明，单一 harness 下的排名在多大程度上取决于配置。

## Limitations

- 作者指出，研究对象是标准化 agent 设置下的通用基础模型，不包括配有领域工具或记忆的专用 agent。
- 每个领域的题数不多（8 到 15 道），而且有四个领域标签（物理科学、数据科学、科学计算、工程）没有指明具体学科。
- 主排名只用了一个 harness；作者的实验显示，换一个 harness 后有些模型的分数会变动 14 到 20 分。
- Repository note：论文给出的 GitHub 地址在 2026-10-27 访问时返回 HTTP 404，因此无法确认数据和代码是否已发布。
- Repository note：论文说针对不同来源的防污染措施写在附录里，但该附录记录的是来源、许可证和陷阱设计，没有给出截止日期之后取材或泄漏筛查之类的规则。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样在数据驱动的科学任务上靠执行来评生成的程序，但不要求书面报告。
- [Terminal-Bench Science](./terminal-bench-science.md) — 容器化的科学任务，由各题特有的测试检查。
- [ASI-Bench](./asi-bench.md) — 跨 11 个领域的项目级科学任务；论文 Table 1 与之做了对比。
