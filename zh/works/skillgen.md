# SkillGen (2026)

> [English](../../works/skillgen.md) | **简体中文**

> **首次公开：** 2026-05-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.10999)

## Overview

SkillGen 为一个 base agent 写一份可复用的自然语言 skill，并且只有在通过配对测试之后才接受它。把 trajectory 总结成 skill，本身并不能证明这个 skill 有用；平均准确率的提升也可能掩盖 skill 把原本能做对的样例弄坏的情况。SkillGen 把 skill 当作一次干预：每个验证实例都分别在有 skill 和无 skill 的条件下运行，统计修复（baseline 失败、加 skill 后成功）和退化（baseline 成功、加 skill 后失败），据此改进 skill，并且只有在净收益超过阈值时才部署。被接受的 skill 随后用 8 个 base agent 在 11 个 benchmark 的留出划分上测试。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 这是通用的 skill 合成方法，用了 11 个以通用场景为主的 agent benchmark；其中少数与科学相关的 benchmark（ChemLLMBench、PubMedQA、ScienceWorld）只是顺带用作测试平台，并不构成被评估的科学活动。

## Links

- **Paper:** <https://arxiv.org/abs/2605.10999>
- **Code:** <https://github.com/yccm/SkillGen>
- **Venue:** NeurIPS 2026（据官方仓库 README）

## Summary

Base agent 先在归纳子集上运行，把 trajectory 分成成功和失败两组；它在另一个验证子集上的无 skill 结果被缓存下来（skill 训练数据按 70/30 划分）。一个辅助模型（GPT-5.4-Mini）分别承担归纳、生成和验证三个角色：把每个失败与同一任务上最近的成功配对，总结成功模式、失败模式和对比观察，然后写出一个候选 skill，内容包括任务背景、成功模式和避免失败的模式。验证 agent 带着 skill 重跑验证子集，计算净收益 G_m = n₀₁ − n₁₀；修复、退化和仍未解决的失败分别变成下一轮的保留、删除、新增、强调指令。最多八轮之后，按 G_m 保留最好的候选，并且只有在 G_m ≥ max{2, ⌈0.05·m⌉, 1} 时才启用它，否则部署空 skill。验证只覆盖被评估的任务分布，所以被接受的 skill 在偏移后的任务上仍可能退化。

## Tasks

N/A — SkillGen 是 skill 合成方法，不是 benchmark。所用 benchmark 的构建/测试实例数：

- τ-Bench retail 30/30；ALFWorld 分布内 500/150、分布外 500/255；ChemLLMBench property 和 yield 30/30；LiveCodeBench 50/150；MCPBench all-tools 64/40、single-tool 40/16；Mind2Web 100/100；PubMedQA 150/100；ScienceWorld 150/100；SocialMaze FTS 和 UPI 各 60/50。
- 主结果中的 base agent：Gemma-4-26B、Llama-3.1-8B、Mistral-Nemo、Qwen-2.5-7B、Claude-Haiku-4.5、GPT-5.4-Nano、GPT-5.4-Mini、Grok-4-Fast。

## Domains

以通用 agent 环境为主（网页、工具使用、代码、社会推理、文本具身任务）。其中有几个 benchmark 与科学相关：ChemLLMBench（化学性质和反应产率预测）、PubMedQA（生物医学问答）和 ScienceWorld（文本形式的科学实验）。

## Evaluation

- **循环内部。** 以一个验证实例为例：缓存的无 skill 结果 = 0，加 skill 后结果 = 1 → 计入 n₀₁（修复）。结果从 1 变成 0 的实例计入 n₁₀（退化）。本轮得分为 G_m = n₀₁ − n₁₀；Δ̂ = G_m / m。另外还会跑最多 30 个 baseline 成功样例的保护性检查。
- **留出集。** 每个 benchmark 测试划分上的准确率，以相对同一 base agent 无 skill 时的配对 Δ（百分点）报告。
- **报告结果。** 8 个 base agent 的平均准确率全部上升，从 +3.27 pp（Gemma-4-26B，58.49% → 61.76%）到 +10.08 pp（GPT-5.4-Nano，54.27% → 64.35%）。80 个留出的 benchmark–划分–模型组合中，50 个提升，25 个不变，5 个退化。
- **选择的作用。** 第 8 轮最新的候选平均 Δ = −3.1 pp，而经验证的最佳候选达到 +8.1 pp。
- **迁移。** 在 ALFWorld OOD、ScienceWorld、Mind2Web 和 SocialMaze FTS 上跨模型复用 skill（各 100 个留出实例）：120 个非对角组合中，70% 不为负，42% 超过 +5 pp。
- **Baseline。** Trace2Skill、SkillX、EvoSkill 和 CoEvoSkills，改造成不带工具的单一自然语言 skill，在 ALFWorld IOD/OOD 和 ScienceWorld 上比较；各方法的具体数值只出现在图中（TODO(reference)）。
- **Ablation。** 不做 refinement、不设验证把关、不用失败教训、用 3-shot ICL 代替 skill、用不带脚本的纯文本 skill；论文报告完整系统在 ALFWorld OOD 和 ChemLLMBench yield 的每个数据集–模型组合上都最好（具体数值 TODO(reference)）。

## Typical Duration

构建一个 skill 平均消耗 5.6M token，从 2.2M（ScienceWorld）到 10.2M（τ-Bench）不等，按 GPT-5.4-Mini 的价格约合每个 skill $8.2。每次调用的平均输入，不带 skill 时为 3,589 token，带 skill 时为 4,537 token。没有报告 wall-clock 时间。

## Main Contribution

作者把 skill 看作一次干预，在配对的实例上测量它的效果，这样修好的失败和弄坏的成功都会被算进去。Skill 本身由成功与失败 trajectory 对比合成，之后的改进、选择和把关都靠这种配对测量。

## Key Design Ideas

- 对比式归纳：按 embedding 距离，把每个失败与同一任务上最近的成功配对。
- 在缓存的 baseline 结果上做有无 skill 的配对评估，把修复和退化分开，而不是只报一个准确率。
- Best-of-K 选择加上接受阈值；没过阈值时，干脆不用 skill。
- Refinement 指令由修复集、退化集和未解决失败集生成。
- 由一个固定的辅助模型为所有 base agent 写 skill，base agent 只负责 rollout。

## Strengths

- 最后一轮 refinement（−3.1 pp）与经验证最佳候选（+8.1 pp）之间的差距，直接显示了验证把关的贡献。
- 覆盖 8 个 base agent（包括小型开源模型）和 11 个 benchmark，并明确报告了退化。
- 报告了以 token 和美元计的构建成本。
- 代码公开。

## Limitations

- 被接受的 skill 仍可能过度泛化；例如 Llama-3.1-8B 在 ALFWorld OOD 上从 67.45% 降到 65.10%。
- 验证只覆盖被评估的任务分布；作者建议另加安全评估和人工审查。
- Baseline 被改造成单一自然语言 skill，作者指出这并不能衡量它们原本的多 skill 能力。
- 报告的失败模式包括：交互任务中执行不完整、化学任务中把反应角色对应错，以及代码任务中缺少全局结构。
- Repository note: 本卡片依据 arXiv v1 摘要和 HTML 全文以及官方仓库 README 编写（2026 年 11 月）；只出现在图中的数值记为 TODO(reference)。

## Related Works

- [MIND-Skill](./mind-skill.md) — 同样用执行反馈控制 skill 生成，做法是重建源 trajectory，而不是比较有无 skill 的结果。
- [SkillEvolBench](./skillevolbench.md) — 在固定的部署任务上把各种 skill 条件与无 skill 对照组比较，这正是 SkillGen 用作接受测试的那种对比。
- [SkillLearnBench](./skilllearnbench.md) — 评测 SkillGen 这一类自动 skill 生成方法。
- [SKILL-KD](./skill-kd.md) — 同样在重跑 agent 之后才接受对 skill 的修改，依据的是 teacher 与 student 的 trajectory 对比。
