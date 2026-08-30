# Skill²-Bench (2026)

> [English](../../works/skill2-bench.md) | **简体中文**

> **首次公开：** 2026-08-05 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.05139)

## Overview

Skill²-Bench 是一个由*跨 skill 长程任务*组成的 benchmark——这类多步问题的相邻步骤需要不同的推理 skill，且后一步依赖前一步的答案——难度由 **skill 熵** 校准——这是一个有向的成对度量，衡量从一个 skill 切换到另一个 skill 有多难。它与 Skill-Entropy RL 一同提出，后者是把同一度量复用为奖励信号的训练方法。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型跨 skill 推理 benchmark；数学、科学与编码题目只是种子素材，会被改写进合成情景以度量 skill 切换，本身并不作为科学或研究任务受评。

## Links

- **Paper:** <https://arxiv.org/abs/2608.05139>
- **Code:** <https://github.com/Gen-Verse/Skill-Entropy-RL>
- **Venue:** arXiv preprint (cs.CL / cs.LG), 2026

## Summary

前沿模型在单 skill benchmark 上往往表现不错，可一旦同一条推理链要在不同 skill 之间腾挪就变得脆弱——比如一段数学推导的结果喂给一个排程步骤，排程结果又指导一个抽取步骤。作者把这类问题形式化为跨 skill 长程任务，并定义 skill 熵 SkE(s_a, s_b)：在固定参考模型下，单 skill 平均准确率与跨 skill 准确率之比，经平滑处理，取值大于 1 意味着这次切换是难的。任务级 skill 熵取任务 skill 序列上两两取值的平均，用来按低、中、高三档难度采样任务。对八个前沿模型与四个开源模型的评估，暴露出一个单领域评测看不见的 skill 切换缺口；随后同一个量被转换成奖励，用于 Skill-Entropy RL。

## Tasks

skill 库含九个领域共 558 个标注 skill——六个可验证领域（数学 186、科学 137、编码 46、逻辑 14、信息抽取 92、规划 34）与三个开放式领域（创意写作 12、上下文检索 12、指令遵循 25）。构建方式是：提示 LLM 为每道种子题标注 3–5 个细粒度 skill，按嵌入对标签聚类，再人工审阅每个簇，使各领域的 skill 粒度大致可比。种子数据集为 OpenR1-Math、MMLU-Pro、LiveCodeBench、ZebraLogicBench 与 Guru-RL-92k、WikiTable 与 WebSRC，以及 NaturalPlan；三个开放式领域的 skill 清单则直接生成。每个任务是一条长度为 L 的问答对序列（L ∈ [2, 10]），相邻步骤来自不同领域：先按目标 skill 熵档位采样一条 skill 序列，每个 skill 抽取一个种子问答对，再由一个 LLM *proposer* 把它们融合成单一连贯的情景，其中每一步都依赖上一步的答案；随后由独立的 *verifier* 依检查清单筛掉不合格的任务。所报告的评估使用一个留出测试集，含 300 个跨 skill 任务，在三个 skill 熵档位与九个领域上保持均衡。

## Domains

九个通用推理领域，其中「科学」取自 MMLU-Pro，「数学」取自 OpenR1-Math。不指派任何规范科学或工程领域：受评目标是 skill 之间切换的难度，领域特定的题目只是经过校准的载体，而非测量的对象。

## Evaluation

每个领域各有自己的打分器 eval_d: (â, a, q) → [0, 1]——例如数学用符号等价、编码用沙箱中的单元测试执行——开放式步骤则由 LLM 评判者（Claude-opus-4.7）依 rubric 在 [0, 1] 上打分。一个任务的得分是其各步得分的平均，而 Skill²-Bench 成绩是模型的平均单步得分。每个模型都以两种模式问询：*单 skill* 模式逐步孤立提问，*跨 skill* 模式则呈现完整的长程任务并要求按顺序作答；两者之差即分离出切换代价。采样在温度 0.7 下进行四次。skill 熵以 Claude-opus-4.7 为固定参考模型一次性算出（Laplace 平滑 α = 0.1），因此难度尺度不随受评模型而变。共评估八个前沿模型（Claude-haiku-4.5、Claude-sonnet-4.5、Claude-opus-4.7、Gemini-3.1-flash、Gemini-3.1-pro、GPT-5.4-mini、O4-mini、GPT-5.5）与四个开源模型（Qwen3-4B、Qwen3-8B、Qwen3-32B、Olmo-3-7B-Think）。

## Typical Duration

任务在单条推理链上跑 2 到 10 个相互依赖的步骤；未报告逐任务的墙钟时间或 token 预算。成本为 `TODO(reference)`。

## Main Contribution

作者把跨 skill 长程任务形式化，提出 skill 熵作为切换难度的有向成对度量，发布以 skill 熵校准的 Skill²-Bench（覆盖 558 个 skill、九个领域），并证明同一度量可以转成训练奖励（Skill-Entropy RL），且能迁移到未见过的领域。

## Key Design Ideas

- 难度由*转换*定义，而非由表面特征定义：长度相同、skill 集合相同的两个任务，切换难度可能相差悬殊。
- skill 熵是有向的——SkE(s_a, s_b) 与 SkE(s_b, s_a) 在不同的两步组合上计算，取值一般不同。
- 所有 skill 熵都由同一个固定参考模型导出，新模型进来评估时难度尺度不会跟着动。
- 单 skill 与跨 skill 成对问询，把切换代价与单个 skill 上的能力分开。
- proposer–verifier 式构造：由 LLM 把种子题融合成一个带跨步依赖的情景，再由检查清单式 verifier 丢弃不合格的任务。
- 在训练那一半里，skill 标签在推理时显式给出，使奖励可以拿预测的 skill 链去对照 gold 链评分。

## Strengths

- 为 skill 组合提供了定量、与模型无关的难度尺度，而非临时划定的「难/易」二分；并显示准确率随任务级 skill 熵上升近乎单调下降。
- 复用成熟且可验证的种子数据集，配以领域适配的自动打分器，把对 LLM 评判的依赖限制在三个开放式领域内。
- 报告显示：同一个 skill 放进跨 skill 任务里考，比作为单 skill 题目考，准确率大约要掉 4 到 13 个百分点——这正是逐领域排行榜掩盖掉的缺口。
- 发现逐领域的 skill 熵与逐领域的难度基本脱钩——科学是个容易的领域，切换熵却最高——这是关于「组合在哪里失效」的一个不直观的实证结果。
- 指认出一种明确的主导失败模式：到了靠后的步骤，模型会沿用上一步的 skill 与答案形态，而不去切换。

## Limitations

- 任务由 LLM proposer 把种子题融合合成而来，其生态效度取决于 proposer 与 verifier 的检查清单，而非取决于自然发生的多 skill 工作负载。
- skill 标签本身由 LLM 生成再聚类，人工审阅只到簇一级；558 个 skill 之间的粒度因此只是大致齐整。
- 实际操作中，skill 熵是用 skill 到领域的切换来近似的，而非逐个 skill 对计算。
- Repository note: 论文一半是评估贡献、一半是训练贡献；所报告的 Skill-Entropy RL 增益（Qwen3-4B-Instruct 上 34.4% → 68.4%，Qwen3-1.7B 上 14.6% → 40.1%）是在作者自己的 benchmark 上测得的，benchmark 与方法共享同一套设计。
- Repository note: 它评估的是模型的推理链，而不是在环境中行动的 agent——没有工具使用、没有外部状态，也没有从失败步骤中恢复的过程。

## Related Works

- [Skill-Use](./skill-use.md) — 同样把 skill 能力拆成可分离的侧面，但面向的是执行既有 skill，而非在推理 skill 之间切换。
- [T-Eval](./t-eval.md) — 更早的能力子过程分解，在孤立任务上为六个工具使用子过程打分。
- [SkillSV](./skillsv.md) — 把 skill 的内部结构当作分析单元，为其各部分赋予结构感知的价值。
- [AgentBoard](./agentboard.md) — 长程评估并给出逐子目标的进度，是暴露多步链条在哪里断裂的另一条互补路径。
