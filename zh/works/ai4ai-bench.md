# AI4AI-Bench (2026)

> [English](../../works/ai4ai-bench.md) | **简体中文**

> **首次公开：** 2026-08-20 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.20318)

## Overview

AI4AI-Bench 测的是 coding agent 能不能改进 AI 系统“怎么学”，而不只是围着原方法调这次 run。十个冻结的 research repository 里，agent 最后只交 source-code patch；另一套干净环境再从头执行它，用开发阶段查不到的固定 evaluator 打分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.20318>
- **Project:** <https://lab.einsia.ai/ai4ai/>
- **Code:** <https://github.com/Einsia/AI4AI-Bench>
- **Venue:** arXiv preprint (2026)

## Summary

每个任务给 agent 一套真实 research codebase、起始模型或资产，以及一个便宜的 proxy metric。Agent 用一张 B300 做四小时诊断、改代码、跑小实验，但能进入封闭阶段的只有 source patch；随后系统从干净起点运行修改后的代码，最多十二小时，并在相同条件下与 repository 原方法比较。这样一来，分数对应的是可重放的算法改动，不是 exploration 阶段碰巧留下的好 checkpoint；另一层分析再看 patch 到底只是改了 run 的操作方式，还是碰到了模型的学习机制。

## Tasks

十个 repository 对应十类算法：OpenR1 supervised fine-tuning、RAGEN multi-turn agentic RL、OPD on-policy distillation、BTRM Bradley–Terry reward modeling、DPO preference optimization、DDPO diffusion RL、NPO machine unlearning、DiGress discrete graph diffusion、Model Soup weight averaging，以及 OWL one-shot pruning。前八项从初始化开始训练；weight averaging 和 pruning 只执行一次，但仍受同一 verification 时间上限约束。

## Domains

AI 与 machine-learning research，覆盖 language-model post-training、reinforcement learning、reward modeling、diffusion model、unlearning、graph generation、model merging 和 pruning。

## Evaluation

每项任务保留自己的确定性指标，包括 LiveCodeBench、held-out solve rate、AIME 2024/2025、RewardBench、IFEval、aesthetic score、unlearning balanced score、graph test negative log-likelihood、ImageNet-V2 accuracy 和 WikiText-2 perplexity。一个单调 progress mapping 把它们放到同一尺度：`0` 是没有信息的模型，`0.1` 是在相同预算下重跑 repository 原方法，`1.0` 是该任务的最优值。研究让 29 个 model–harness–effort configuration 跑完十项任务，共 290 个 cell；平均 mapped score 是 0.166，最佳 system 平均 0.250，124 个 cell 还低于原方法 baseline。

为了诊断结果，另一模型读取 263 个可分类 code diff，并分配可以重叠的 change family。其中 141 个 submission 只动训练时长、超参数、checkpoint 选择或 trainable capacity 等 run-side 选择；122 个碰到了 loss、supervision、update rule 或 data。后者平均 0.226，前者平均 0.126。提高 reasoning effort 会把进入 learning side 的比例从 8% 推到 64%，但作者明确说明这不是随机对照，因此不能把两组差值解释成“做算法改动”的因果效果。

## Typical Duration

每项任务先让 agent 在一张 NVIDIA B300 上探索四小时，再从干净起点正式执行最多十二小时；两个不训练的任务只把十二小时当作 verification 上限。

## Main Contribution

把 AI research automation 里的算法设计单独拿出来测：固定 hardware、起始资产、执行预算和 final evaluation，再分别检查 source patch 有没有改进模型，以及它改到了学习流程的哪一层。

## Key Design Ideas

- Exploration 结束后，只允许 source code 进入 formal evaluation。
- 原算法和修改后算法从同一起点运行，hardware、预算、evaluator 和 evaluation asset 全部相同。
- 开发时开放便宜 proxy，但不开放决定最终分数的 metric。
- 用无信息点、原算法和任务最优值，把不同任务的 metric 映射到同一尺度。
- 读取提交的 diff，把运行层面的调参和学习流程本身的改动分开。

## Strengths

- 十项任务覆盖十类算法，不是在一个 post-training recipe 上重复换数据。
- Clean-start replay 把分数落到提交的 source，而不是 exploration checkpoint 或 cache state 上。
- Outcome 和 intervention type 分开报告，能看出一次表面成功的 AI-research run 到底有没有展示算法设计。
- 公开 task environment、evaluator 和 scored submission，方便重放和后续纵向比较。
- 同时报告 exploration cost、reasoning-effort sweep 和 performance。

## Limitations

- 全套只有十项高成本任务，而且都围绕一种 hardware class；算法族覆盖面宽，instance 数量仍小。
- 没有人类专家 baseline；原 repository 算法可以锚定相对提升，但不能说明 human research performance 在哪里。
- Source-patch 的 change family 由语言模型分配，论文没有报告这些标签与人类判断的一致性。
- Proxy/final 分离能阻止 agent 直接查询 final metric，但论文说明部分 proxy 与 final evaluation 来自同一 corpus；它保证的是访问和时间隔离，不是 sample disjointness。
- 公开 repository 支持 self-hosted evaluation，但目前没有 blind evaluation service，因此第三方运行不会自动复现论文里的 evaluator-access 边界。

## Related Works

- [PostTrainBench](./posttrainbench.md) — 开放完整 post-training，包括 data 与 initialization；AI4AI-Bench 则把 training-algorithm design 单独拿出来。
- [RE-Bench](./re-bench.md) — 在时间预算下评估开放式 AI R&D，并提供人类比较，但不隔离 learning-rule 层。
- [Curation-Bench](./curation-bench.md) — 固定 training recipe，把 data-policy improvement 作为 intervention。
- [AutoWorldModel-Bench](./autoworldmodel-bench.md) — 在开放方法空间和 held-out evaluator 下，让 agent 改进 world model。
- [Beyond Final Scores](./beyond-final-scores.md) — 把长时程 improvement 的 outcome 与产生它的 process 和 shortcut 分开。
