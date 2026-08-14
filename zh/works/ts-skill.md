# TS-Skill (2026)

> [English](../../works/ts-skill.md) | **简体中文**

## Overview

TS-Skill 是一个受控的时间序列问答 benchmark，把分析能力分解为三种可组合的信号级 skill——时间尺度选择、时间定位、跨区间整合——并给出逐 skill 的能力画像，而不是一个笼统的 TSQA 总分。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.24703>
- **Dataset:** <https://huggingface.co/datasets/Anonymous-Dataset-H/TS-Skill>
- **Venue:** arXiv preprint, May 2026

## Summary

现有时间序列问答 benchmark 按任务类型或高层推理范畴组织，作者认为这使得真正驱动表现的信号级能力无从诊断。TS-Skill 转而定义三种可组合的分析 skill，并让每道题所需的 skill 集合在构造时就是已知的，于是准确率可以按 skill、按 skill 组合分别报告。benchmark 由 **SKEvol** 生成——一条 skill 引导的 agentic 构建流水线，包含领域感知的种子信号生成、skill 受控的题目生成、元数据与代码辅助的答案构建、多阶段的信号锚定校验，以及人在环的策展。对十个模型（涵盖 LLM、VLM、时间序列原生模型与一个工具增强 agent）的评测显示，三种 skill 上的差距既显著又不均衡。

## Tasks

**3,000 道问答题**，覆盖三种 skill 的七种非空组合（从单独的 SK1 一直到 SK1+SK2+SK3）。题目在表述中明确涉及时间戳，锚定在领域上下文条件下生成的合成时间序列上，共涉及 25 个领域类别、517 个变量。三种 skill 是：

- **SK1 — 时间尺度选择：** 判定相关模式在哪个时间粒度上最容易观察到（细粒度的短事件，还是粗粒度的长期趋势）。
- **SK2 — 时间定位：** 找出相关证据所在的时间戳、区间或事件，途径包括显式区间、事件锚定或跨通道识别。
- **SK3 — 跨区间整合：** 把多个彼此分离的时间区域上的证据合起来，做计数、聚合、比较或极值运算。

构建分两个阶段：先由领域上下文引导生成种子信号，并附带元数据与 skill 标注；再做面向特定 skill 的题目生成，由提案 agent 产出，配元数据/代码辅助的答案构建、多阶段校验（基于图、基于规则、基于 LLM）与人工复核。

## Domains

`Repository note:` 不指派任何规范的科学或工程领域。那 25 个领域类别（金融、医疗、能源、交通运输、环境监测、Web 系统等）只是为合成信号的生成提供*上下文条件*，并非扎根真实实测数据的科学任务；受评的能力是对信号的通用时间推理。因此不在领域轴上主张任何归属。

## Evaluation

题目按其所需的 skill 标签分组，模型在每组内计分，输出因此是逐 skill（以及逐 skill 组合）的能力画像。报告三种作答协议：

- **选择题** — 严格字母匹配下的准确率与 macro-F1；无法解析的输出记 0 分。
- **自由作答** — 由 LLM judge（「Judge-Only」）为开放式答案打分。
- **原生形式** — 保留异构答案格式的结构化评分。

共评测七个族的十个模型：闭源文本 LLM 与 VLM（GPT-o3-mini、GPT-4o、Claude Sonnet 4.5）、开源模型（Qwen2.5-14B-Instruct、Qwen3-32B Thinking、DeepSeek-V3、Qwen2.5-VL-7B）、一个时间序列原生模型（ChatTS-14B）、一个针对任务微调的模型（Time-MQA），以及一个工具增强 agent（GPT-5.4，配 ReAct 与趋势检测、峰值查找、开窗、统计等时间序列工具）。

报告的发现：SK3 是最主要的短板——非 agent 模型的得分接近或低于 0.259 的随机基线（ChatTS-14B 0.290、Time-MQA 0.205），而工具增强的 ReAct agent 在单独的 SK3 上达到 0.788，却并未在同时要求定位与规划的组合题上缩小差距。选择题准确率由 Claude Sonnet 4.5 领先，为 0.778。

## Typical Duration

`TODO(reference)` — 所查来源报告了逐题的作答协议，但未给出每题的轨迹长度、wall-clock 时间或 token 预算。工具增强 agent 基线跑的是 ReAct 循环，其步数未见说明。

## Main Contribution

一个受控、带 skill 标签的 TSQA benchmark，表明 skill 级评测能暴露 TSQA 总分所掩盖的时间推理失效——尤其是跨区间整合对非 agentic 模型近乎普遍的失效；同时提出 SKEvol——正是这条 agentic 流水线在大规模生成 skill 受控、答案可验证的题目。

## Key Design Ideas

- 把分解定义在*信号*层面（尺度、位置、整合），而不是按任务类型或高层推理范畴。
- 让 skill 标签成为构造时的属性：题目是为满足指定的 skill 集合而生成的，能力画像因此是设计出来的，而非事后标注的。
- 覆盖全部七种 skill 组合，使组合性的 skill 需求能与单 skill 需求分开。
- 信号是合成的，但受领域上下文约束——这换来了可验证的 ground truth 与可扩展的 skill 标注。
- 入库前经过多阶段校验（基于图、基于规则、基于 LLM）加人在环策展。
- 题干明确带上时间戳，使定位成为真实要求，而不是上下文排序带来的副产品。
- 三种作答协议（选择题、自由作答判分、原生结构化），使结论不绑定在单一评分格式上。

## Strengths

- skill 标签由构造保证而非推断得来，逐 skill 画像因此可信（论文）。
- 在提示式模型之外纳入了工具增强 agent，从而分辨出工具在哪里有用（单独的 SK3）、在哪里没用（组合题）（论文）。
- 报告多种评分协议，降低了排名只是选择题格式副产品的风险（论文）。
- 答案可验证，并配有文档化的多阶段校验流水线与人工复核（论文）。

## Limitations

- 作者声明 TS-Skill 使用的是受控、由领域上下文引导的**合成**时间序列：这让 skill 标注可扩展、答案可验证，但可能无法体现真实部署中的噪声、缺失与分布复杂性。
- 只定义了三种 skill；作者把扩展到真实数据集、更丰富的领域专用任务、多变量设定与更多 skill 列为未来工作。
- `Repository note:` 该 benchmark 本质上是 LLM/VLM 的问答评测——十个基线中只有一个是带工具的 agent——因此它关于 agentic 能力的证据只建立在单一配置上。
- `Repository note:` 所查的数据集链接是一个匿名化的 Hugging Face 仓库，与在审稿件的情形相符；所查来源未给出永久的工件地址。

## Related Works

- [T-Eval](./t-eval.md) — 同样坚持把一项能力分解为分别计分的子过程，应用在工具使用上。
- [Skill-Use](./skill-use.md) — 把 skill 使用拆成若干侧面（触发、遵从、边界），而非信号级的分析 skill。
- [BLADE](./blade.md) — 数据分析评测扎根于真实科学数据集与专家分析，而非受控的合成信号。
- [LongDA](./longda.md) — 在真实调查数据上做文档密集的分析工作流，是 TS-Skill 单题式探针的长时程对应物。
- [DSBench](./dsbench.md) — 更宽泛的数据科学任务评测，但没有逐 skill 的分解。
