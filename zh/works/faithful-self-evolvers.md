# LLM Agents Are Not Always Faithful Self-Evolvers (2026)

> [English](../../works/faithful-self-evolvers.md) | **简体中文**

> **首次公开：** 2026-01-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2601.22436)

## Overview

Self-evolving agent 会把前面 episode 积累的经验存下来，再塞进后续的 prompt。常见的评估做法是看加入经验后成功率有没有上升，这背后默认了一个前提：agent 的决策真的依赖这些经验。这项研究直接检验这个前提。它在其他条件都不变的情况下扰动或删掉插入的经验，然后看 agent 的表现会不会跟着变。如果把经验清空或换掉以后表现纹丝不动，就说明 agent 其实没在用它。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

N/A — 这是一项诊断研究，检查 self-evolving agent 是否忠实地使用自己的 memory，实验覆盖通用问答、推理、具身和 web 环境；它评估的是 agent 的一种元属性，不涉及科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2601.22436>
- **Code:** <https://github.com/Dreamcatcher0622/Faithfulness>
- **Venue:** ICML 2026

## Summary

作者把 *experience faithfulness* 定义为：agent 的行为是否会因为给它的经验而发生因果上的改变。他们把经验分成两类。一类是 *raw* experience，例如把完整的成功 trajectory 当作示范重复使用；另一类是 *condensed* experience，即从 trajectory 中提炼出来的自然语言 insight、启发式规则或 memory item。针对每一类，作者在四个现有的 self-evolving framework 里做受控干预：保留格式但清空内容、打乱 trajectory 的步骤顺序、换成无关任务的经验、破坏关键组成部分，或者用 filler token 替换 condensed 文本。在测试的各个 backbone 和环境上，扰动 raw experience 会改变表现，而扰动 condensed experience 往往影响很小，即使 condensed experience 是唯一提供的经验也是如此。这项研究诊断的是经验有没有被用上，并没有提出新的 self-evolving 方法。

## Tasks

N/A — 这是诊断研究，不是新 benchmark。干预实验在 9 个现有环境上进行：HotpotQA、FEVER、GPQA-Diamond、MMLU-Pro（engineering）、AIME 2024、Game of 24、ALFWorld、WebArena 和 WebShop。报告的样本量包括 100 道 HotpotQA 题、198 道 GPQA-Diamond 题和 812 个 WebArena 任务；另有一项补充检查分别从 2WikiMultiHopQA 和 Musique 各取 100 个样例。

四个 framework 分别是：ExpeL（离线、单 agent；raw 为成功 trajectory，condensed 为提取出的 insight）、Dynamic Cheatsheet（在线、单 agent）、ReasoningBank（在线、单 agent；condensed memory item 包含标题、描述和内容）以及 G-Memory（在线、多 agent；两种 raw 经验加一种 condensed 经验）。摘要报告的 LLM backbone 数是 13 个，v3 HTML 版第 3.1 节写的是 10 个。点名的 backbone 包括 GPT-4o、GPT-4o-mini、GPT-5.2、Gemini-2.5-Flash、Gemini-3-Pro、Claude-Sonnet-4.6，以及从 1.7B 到 235B-A22B 的 Qwen3 系列模型。

## Domains

多跳问答与事实核查问答、研究生水平的理工科选择题、竞赛数学、算术谜题、具身家务任务（ALFWorld），以及网页导航和购物（WebArena、WebShop）。

## Evaluation

- **干预分组。** Raw experience：Empty、Shuffle、Irrelevant，外加直接移除（"w/o Raw"）。Condensed experience：Empty、Corrupt、Irrelevant、Filler，外加直接移除（"w/o Cond"）。
- **Faithfulness 信号。** 论文没有给出单一的 faithfulness 公式。如果扰动某个经验通道后，agent 的任务分数（按环境分别是成功率或 exact match）发生变化，就认为 agent 对这个通道是 faithful 的。举一条 trace：ExpeL 配 Qwen3-32B 在 2WikiMultiHopQA 上，经验完整时 exact match 为 62，在所有 raw 和 condensed 扰动下都是 63 到 65，所以在这个任务上，插入的经验并没有左右答案。
- **失败分析。** 在 WebArena 上用 ReasoningBank 时，把「不给 condensed experience 能成功、给了反而失败」的案例标成三类：被干扰（distraction）、过度依赖错误先验，以及过早推断。例如 Gemini-2.5-Flash 在 Shopping 上分别占 45.2%、32.3% 和 22.6%。
- **归因分析。** 在 ALFWorld 上用 Qwen3-32B，按 attention head 和层计算 Integrated Gradients，再按 prompt 片段汇总；condensed experience 得到的归因始终很低，靠后的层主要由当前 trajectory 主导。

## Typical Duration

沿用底层环境和 framework 的设置；这项研究本身没有设定 step、时间或 token 预算。TODO(reference)

## Main Contribution

作者给出了第一项关于 self-evolving LLM agent 中 experience faithfulness 的系统研究。因果干预显示，agent 依赖 raw experience，却常常忽略或误读 condensed experience。作者把这种差距归结为三个因素：condensed 内容不够具体、模型内部处理偏向当前上下文，以及有些任务靠预训练知识就已经够用。

## Key Design Ideas

- 把经验通道拆成 raw 和 condensed 两部分，分别独立扰动，这样分数变化可以追溯到某一个通道。
- 用不含内容的对照组区分内容本身的作用和 prompt 结构的作用：Empty 保留格式，Filler 保留长度。
- 在离线与在线、单 agent 与多 agent 的 framework 上重复同一组干预。
- 把行为层面的干预和基于梯度的归因结合起来，定位 condensed experience 在模型内部是在哪里被压低权重的。

## Strengths

- 干预是在四个现有 framework 内部做的，而不是只用一个自定义 agent，所以结论不绑定某一种 memory 设计。
- 研究覆盖推理、具身和 web 环境，backbone 既有闭源模型，也有不同规模的开放权重模型。
- 干预代码已公开。

## Limitations

- 知识密集型任务（HotpotQA、GPQA、MMLU-Pro、FEVER）对任何经验扰动都不太敏感，作者认为这是预训练先验在起作用；在这些任务上，不敏感不能只解读为对 condensed experience 不 faithful。
- Repository note: 论文里 backbone 的数量在摘要（13 个）和第 3.1 节（10 个）之间不一致，而且大部分分条件结果是用图而不是表报告的。
- Repository note: Faithfulness 信号看的是整体任务分数的变化，所以它能发现某个经验通道是否影响结果，但不能说明某一个具体决策有没有参考它。

## Related Works

- [SkillEvolBench](./skillevolbench.md) — 同样检验提炼出的经验是否对 agent 有帮助，但它评的是 agent 能否形成可复用的 skill，而不是给定的经验是否在因果上改变了行为。
- [SkillMisevo-Bench](./skillmisevo-bench.md) — 同样关注 self-improving agent 从过去 episode 中存下了什么，但重点是不安全的内容混进 skill library。
- [SkillLearnBench](./skilllearnbench.md) — 同样评估从经验中得到的 skill，在任务成功之外还给生成的 skill 质量打分。
