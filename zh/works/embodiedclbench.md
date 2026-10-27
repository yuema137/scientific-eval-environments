# EmbodiedCLBench (2026)

> [English](../../works/embodiedclbench.md) | **简体中文**

> **首次公开：** 2026-10-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.13021)

## Overview

EmbodiedCLBench 测的是：具身 agent 能不能从基础家务任务中学到东西，再把学到的东西重新组合起来，完成没见过的更复杂的任务。agent 先做基础任务，然后面对一个进阶任务，它组合了两到四个基础任务类别里的技能。基准比较三种情况：没有任何经验、把之前的完整轨迹留在上下文里、以及从这些轨迹中提炼出的一份书面技能摘要。进阶任务零样本的成功率是 3–12%，有了任一种经验后是 16–52%；但学习样本超过一个之后，再多也没有带来稳定的提升。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 通用具身家务任务基准；被评测的 agent 在仿真中操作家居物品，不属于科学或研究活动。

## Links

- **Paper:** [EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents](https://arxiv.org/abs/2610.13021)，2026 年预印本（北京大学、北京通用人工智能研究院 BIGAI、香港大学）。
- **Full text:** <https://arxiv.org/html/2610.13021v1>
- **Code:** <https://github.com/PKU-VaLuE-Lab/EmbodiedCLBench>（README 没有注明许可证）
- **Data:** <https://huggingface.co/datasets/PKU-VaLuE-Lab/EmbodiedCLBench>
- **Project:** <https://pku-value-lab.github.io/EmbodiedCLBench-homepage>
- **Venue:** arXiv 预印本（cs.AI，2026）

## Summary

任务来自 TongSim 模拟器闭源版本中的室内家居场景，选闭源版本是因为它支持的动作更多。由于这个版本无法实际用于在线仿真评测，每个任务都被转换成预先构建好的状态转移图：每个节点对应一张第一人称图像和四个候选动作，候选动作分为最优、次优（能执行但绕远）和无效三种。agent 看着当前图像，每一步选一个动作。在步数预算内到达目标节点就算成功；测试时的预算是最短路径加 3 步，学习阶段加 6 步。在 In-Context Learning（ICL）设置下，agent 先完成两个相关的基础任务，并把完整的交互历史留在上下文里。在 Skill Learning 设置下，它做完同样的基础任务后写一份简短的 Markdown 技能摘要，测试时只能看到这份摘要。

## Tasks

共 268 个任务：168 个基础任务，100 个进阶任务。基础任务分六类：Object Manipulation、Spatial Placement、Accessibility Control、Appliance Operation、Activity-Driven Scene Configuration 和 Household State Restoration。一个基础任务由 2 个原子动作组成（最短路径 6 步）；一个进阶任务由 4 个原子动作组成（12 步），取自 2 到 4 个基础任务类别。原子动作是离散的基本操作，比如走到、看向、拿起、放下、打开、关上和开启。一个 LLM（Qwen3.7-Plus）通过三阶段流程生成任务描述和每个状态的动作选项，最短路径用广度优先搜索求出；每个样本要经过三名标注者各自审核图像、描述和选项，三人都通过才保留。

## Domains

具身家居仿真（TongSim），通过在离散的高层动作中做选择来完成任务；不在本仓库的科学/工程领域轴之内，论文也没有评测任何机器人平台或机器人控制。

## Evaluation

- **指标：** Success Rate（SR），即在步数预算内到达目标节点的任务比例。动作选择的比例（最优、次优、无效）另做分析。没有使用 LLM 或 VLM 评审。
- **系统：** Qwen3.8-Flash 和 GPT5.6-Terra，各自放进四个 harness（Hermes、OpenClaw、Codex、Claude Code），共八种配置。
- **结果（Table 1，SR %）：** 基础任务零样本为 42.9–58.9。进阶任务零样本为 3.0–12.0，ICL 下为 16.0–52.0，Skill Learning 下为 22.0–38.0。有经验时的最高分：Codex 搭配 GPT5.6-Terra 在 ICL 下为 52.0；OpenClaw 搭配 Qwen3.8-Flash 在 Skill Learning 下为 38.0。两种设置没有哪一种稳定占优：八种配置里 ICL 领先五种，Skill Learning 领先三种。
- **复杂度（Hermes，Qwen3.8-Flash，3 到 6 个原子动作）：** 零样本 SR 从 28.0% 降到 4.0%；ICL 从 3 个动作时的 72.0% 降到 4 个动作时的 42.0%，6 个动作时为 32.0%，此时 Skill Learning 为 26.0%。
- **学习样本数：** 从 0 个到 1 个学习样本，SR 从 8.0–10.0% 升到 28.0–40.0%；从 1 个到 6 个，没有稳定的上升趋势（Hermes 和 OpenClaw，搭配 Qwen3.8-Flash）。
- **步数预算：** 不给额外步数时，零样本 SR 为 0.0%，ICL 为 15.0%，Skill Learning 为 7.0%。
- **动作选择：** 与零样本相比，有经验时选无效动作的比例下降 13–20%，选次优动作的比例上升 3–8%；Skill Learning 下的变化更小。

## Typical Duration

基础任务的最短路径是 6 步，进阶任务是 12 步，测试时额外给 3 步。论文没有报告 token 数、美元成本和墙钟时间。

## Main Contribution

在具身环境中，把持续学习衡量为从基础任务到其未见组合的迁移，并比较原始轨迹和提炼后的技能摘要哪个更适合承载经验。

## Key Design Ideas

- 用来自多个基础任务类别的原子动作组合出进阶任务，成功就必须重新组合技能，而不是重复某一个技能。
- 固定学习任务，只改变 agent 保留下来的东西（什么都不留、完整轨迹，或者书面技能摘要）。
- 预先算好状态图，并明确标出最优、次优和无效选项，这样成功与否和每一步动作选得好不好都能确定性地打分。

## Strengths

- 同样的八种模型–harness 配置在全部四种设置下都做了评测，可以逐个配置看出经验带来的提升。
- 每个样本都经过三名标注者的独立检查。
- 复杂度、学习样本数和步数预算分别在单独的实验中变化。

## Limitations

- 评测是在预先构建的图上离线进行的，每个状态只有四个候选动作，agent 只能选动作，不能自己生成动作，也走不出这张图。
- 只评测了两个基座模型。
- 论文说 ICL 和 Skill Learning 把进阶任务成功率 "from around 10% to above 30%"；但 Table 1 中 16 个有经验的格子里有五个低于 30%（例如 Hermes 搭配 GPT5.6-Terra 在 ICL 下为 16.0%）。
- Repository note: 论文没有报告重复运行或方差，复杂度和学习样本数实验只用了一到两个 harness。

## Related Works

- [EmbodiedBench](./embodiedbench.md) — 在高层动作和原子动作两个层面评测具身 agent，没有学习阶段。
- [SkillEvolBench](./skillevolbench.md) — 同样比较学到的技能和原始轨迹复用，但任务不是具身任务。
- [PhysRSI-eval](./physrsi-eval.md) — 同样测量从先前尝试中改进的能力，用的是仿真机器人操作上的完整物理轮次。
