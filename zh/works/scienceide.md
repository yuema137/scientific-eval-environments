# ScienceIDE (2026)

> [English](../../works/scienceide.md) | **简体中文**

> **首次公开：** 2026-09-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.19134)

## Overview

科学模拟代码大多是公开的，但一个公开仓库还不能直接拿来训练或评测 agent：它没有任务说明，没有隔离好的起始状态，也没有办法判断一次修改在科学上对不对。ScienceIDE 把代码仓库改造成可执行的环境。agent 和领域专家一起把代码拆成模块，每个模块只负责一项科学功能；模块原有的官方测试保留下来作为检查项；再由任务工厂往模块里注入缺陷，或者删掉某段实现。最后由一个私有 verifier 把 agent 算出的数值结果和科学参考值逐一比对。同一个 verifier 有三种用途：在难题子集上给前沿 agent 打分，筛选监督微调用的示范轨迹，以及在强化学习里充当奖励。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** [ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments](https://arxiv.org/abs/2609.19134)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2609.19134v1>
- **Code:** <https://github.com/aitofound/ScienceIDE>
- **Venue:** arXiv 预印本（cs.CL、cs.CY，2026）

## Summary

agent 先把某个固定版本的科学代码编译起来，跑通官方测试和示例，然后提出一套模块划分，交给领域专家审核；模块边界和等价性约定由一位 curator 负责。每个通过审核的模块都会打包成一个可编辑的工作区，附带检查项和私有 verifier。任务工厂分七类（Acceleration、Repair、Discovery、Reproduction、Integration、Calibration、Implementation），负责生成候选任务。一个任务只有同时满足两个条件才会收录：已知正确的解能通过，未修复的起点又还留有提升空间。以修复任务为例，起点是注入了缺陷的代码；agent 改完模块后，verifier 重新运行，得分是这次修改填补了缺陷起点到完全通过之间多大比例的差距。作者说明，目前发布的任务主要是计算物理和地球科学里的修复与实现，不涉及开放式的科学发现。

## Tasks

共 27 个科学代码库、64 个环境、2,812 个生成的任务，其中修复 2,515 个、实现 295 个、加速 2 个。这些环境带有 1,076 个可执行检查，检查对象是数值输出和物理不变量。ScienceIDE-Hard 是从 18 个环境中选出的 85 个任务（修复 52、实现 33）组成的评测子集，论文点名的代码库包括 PLUTO、Athena++、MITgcm、LAPS 和 PHANTOM。各领域的任务数只在一张图里给出。TODO(reference)：各领域任务数。

## Domains

计算物理和地球科学代码，涉及天体物理流体、等离子体物理、海洋与大气模拟，以及粒子模拟。

## Evaluation

- **Verifier：** 完全确定性。输出与私有科学参考值比较，用逐点容差（|c − r| ≤ a + ρ|r|）或不变量检查。论文说明，轨迹审查可以用来诊断失败原因，但任何 judge 都不能推翻确定性检查的结论。
- **修复得分：** r_repair = max(0, (r − f)/(1 − f))，f 是带缺陷起点的原始得分；r_repair = 1 才算严格成功。
- **ScienceIDE-Hard 上的 agent 结果（严格成功率，每题一小时，来自 8 家厂商的 15 个模型）：** Fable 5.1 为 67.1%，Opus 5 为 64.6%，Astra 为 63.1%，Sol 为 55.0%，其余都低于 40%（DeepSeek V4.1 Flash 为 36.0%）。每题成本 Fable 为 7.90 美元，Astra 为 3.56 美元。把时间限制缩到 10 分钟时，Astra 为 49.6%，Fable 只有 25.9%。成功率与运行时长的 Spearman 相关为 −0.22，与输出量的相关为 0.01。
- **失败分析：** 在难题子集上，按任务均衡计算的失败中有 37.3% 是预算耗尽。对 Fable 和 Astra 的轨迹审查发现，大部分失败源于和参考实现的约定不一致。
- **SFT（LoRA，三个 epoch；示范来自 GPT-5.6-sol，经 verifier 过滤；训练片段 4,567 个，来自 564 个任务）：** 留出任务上的平均修复奖励有所提高，比如 4B 模型在 PLUTO-Particles-Dust 上从 0.0000 升到 0.3333，9B 模型在 LAPS 上从 0.3125 升到 0.5000。在公开 benchmark 上，4B 模型的 HumanEvalFix JavaScript 提高 10.98 分，9B 模型的 BBH Word Sorting 从 0.240 升到 0.576。
- **RL（Qwen3.5-4B，30 步，组大小 8；LAPS 修复任务 99 个，MITgcm-biogeo 修复任务 87 个）：** 留出奖励在 LAPS 上从 0.357 升到 0.857，在 MITgcm-biogeo 上从 0.286 升到 0.571。这些留出任务和训练任务来自同一批环境。

## Typical Duration

ScienceIDE-Hard 每题限时一小时。SFT 评测的上下文上限为 8,192 token，回复上限为 2,048 token；RL 设有轮数上限和回复预算，但论文没有给出具体数值。

## Main Contribution

一套把科学代码仓库改造成环境的基础设施：任务由专家审核过的数值 verifier 决定是否收录、如何打分，同一个 verifier 同时用于 agent 评测、示范筛选和 RL 奖励。作者发布了用经过验证的轨迹训练出的 PhAI-IDE-72B、-9B 和 -4B。

## Key Design Ideas

- 按科学功能划分模块；每条官方测试要么保留为检查项，要么写明理由后排除，要么标记为覆盖缺口。
- 收录任务时既要求已知正确的解能通过，也要求未修复的起点有提升空间，已经解决或根本无解的任务都会被剔除。
- 修复得分以带缺陷的起点为基准做归一化，而不是从零算起。
- RL 中，因预算截断的轨迹不参与 loss 计算，但仍计入组内基线。

## Strengths

- 打分完全由确定性检查对照私有科学参考值完成，部分得分有明确的公式。
- 难题子集的结果同时报告了成本、时间预算和成功率，可以看到 10 分钟和一小时两种预算下模型排名会变。
- 失败分析给出了预算耗尽在失败中的具体占比。

## Limitations

- 作者说明，任务主要是计算物理和地球科学里的修复与实现；加速任务只有 2 个，其他工厂类别在任务统计里没有出现。
- 作者指出，同一工厂生成的变体可能共用代码路径，所以任务总数会高估真正独立的覆盖面。
- 难题集只测到一小时预算和两个相互耦合的修改位置。
- 验证只覆盖选定的观测量；作者把外部审计和对抗性的 reward hacking 测试列为尚未完成的工作。
- 作者说明，SFT 的提升只体现在选定的公开 benchmark 上，RL 的提升只体现在训练环境内带提示的任务上，两者都没有证明能迁移到没见过的代码库。
- 作者说明，检索限制不能排除模型在预训练时见过这些公开代码，任务选择也没有证明不受污染。
- Repository note：论文没有说明参与的领域专家人数。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — 同样在容器里用确定性检查给科学计算任务打分。
- [MooseBench](./moosebench.md) — 同样评测 agent 在大型模拟框架代码库里的工作。
- [PostTrainBench](./posttrainbench.md) — 同样把评测结果放进后训练的循环里。
