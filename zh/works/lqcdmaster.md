# LQCDMaster (2026)

> [English](../../works/lqcdmaster.md) | **简体中文**

> **首次公开：** 2026-07-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.15001)

## Overview

LQCDMaster 是一个 skill 引导的格点量子色动力学计算 agent，随之发布一个含 70 个任务的格点 QCD 测量代码 benchmark：每一份生成的 PyQUDA 工作流都要与专家手写的参考实现在机器精度上做直接数值比对来验收。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.15001>
- **Code:** <https://github.com/sjtu-sai-agents/LQCD_Master>
- **Venue:** arXiv preprint (hep-lat), 2026

## Summary

格点量子色动力学（LQCD）从第一性原理计算强子可观测量，但要把一个研究动机变成可靠的计算工作流，需要相当深的专业积累。LQCDMaster 把自然语言表述的 LQCD 研究任务转成可执行的 PyQUDA 工作流——测量脚本、作业提交产物、执行日志与数值输出——做法是把 agentic 规划、专家标注的 LQCD skill，以及一个确定性的 Wick 缩并工具（`generate_einsum`）结合起来，用后者约束代码生成中代数上最脆弱的那一环。评测方面的贡献是一个含 70 个任务的 LQCD 计算 benchmark，配专家参考实现与机器精度的验证协议，与代码一同发布。

## Tasks

70 个 LQCD 计算任务：介子与重子的局域二点函数（2PT）20 个、非局域 Wilson 线 2PT 10 个、介子三点函数（3PT）13 个、用顺序源的重子 3PT 15 个，以及 Wilson 圈测量 12 个。每个任务把一份自然语言研究请求，与一份针对同一可观测量、同一系综、同一运动学设定的手写专家参考实现配成一对。agent 所用的专家标注 skill 库含三个 skill：`lqcd-physics-correlator`、`pyquda-tool` 与 `pyquda-gauge`。

## Domains

物理学——格点量子色动力学，一个从第一性原理研究强子结构与谱学的场景（介子、重子、Wilson 圈、光锥分布振幅、轻核与超核谱）。工作流通过 PyQUDA/QUDA 的 GPU 栈执行，并以 SLURM 提交作业，因此这些任务也会考察科学软件与 HPC 工作流工程，但受评目标仍是物理可观测量。

## Evaluation

- **以数值比对验收。** 每份生成的工作流，都与针对同一可观测量、同一系综、同一运动学设定的手写参考实现做直接数值比对来验证。
- **三类结果标签。** *Matched* — 与专家参考在机器精度上一致，|Δ| ≲ 10⁻¹²；*Convention Mismatch* — 只有一处全局符号或相位变换之类的细微差异；*Failure* — 其余任何代数或数值上的不一致。
- **报告结果（GPT-5.4 骨干）。** 63/70 Matched、3 个 Convention Mismatch、4 个 Failure——总体准确率 90.0%；分类别为局域 2pt 20/20（100.0%）、非局域 2pt 8/10（80.0%）、Wilson 圈 12/12（100.0%）、介子 3pt 13/13（100.0%）、重子 3pt 10/15（66.7%）。
- **骨干稳健性（DeepSeek-V4-Pro）。** 56/70 Matched、3 个 Convention Mismatch、11 个 Failure——准确率 80.0%。

## Typical Duration

报告的是实现的 wall-clock 时间，而非 token 预算：专家实现每个可观测量需 1–8 小时，LQCDMaster 需 3.5–10.9 分钟，各可观测量的加速比分别为 17×、30×、54×、38× 与 44×。每任务的 token 数与轮数为 TODO(reference)。

## Main Contribution

一套面向格点 QCD 的 agentic 科学计算系统，配一个已发布、达到研究级难度的 70 任务 benchmark，其判分标准是与专家手写代码的数值精确一致，而非靠 judge 打分或文本匹配。作者还用该系统算出了一个此前未曾计算过的格点量——带对角 Wilson 线的光锥分布振幅——以及质子、氘核、氚核、超子、超氘核与超氚核的谱。

## Key Design Ideas

- 正确性的判据是与专家参考实现在机器精度上一致，从而为一个本无标准答案的领域提供了确定性的验证器。
- 单列一个 *Convention Mismatch* 标签，把全局符号/相位差异与真正的代数错误分开，使物理上等价的工作流不被判为失败。
- 代数上最脆弱的 Wick 缩并那一步交给确定性工具，而不是留给代码生成。
- 专家标注的 skill 无需训练模型，就把通用骨干特化到该领域。
- benchmark 覆盖结构难度不同的可观测量族（2PT、非局域、带顺序源的 3PT、Wilson 圈），正因如此才暴露出重子 3PT 这个短板。

## Strengths

- 确定性的高精度验证，而非 LLM 判定。
- 任务集、生成的脚本、提交脚本与生产输出与 agent 一并发布。
- 结果按可观测量族分别报告，失败集中之处（重子 3PT）因此清晰可见，不会被平均掉。
- 用第二个模型检验骨干稳健性，把架构效应与骨干强弱分开。

## Limitations

- 70 个任务集中在单一子领域内；就 LQCD 而言可观测量覆盖已算广，但作为 agent benchmark 仍偏窄。
- 参考实现出自设计任务的同一个专家组，任务与答案并非独立来源。
- 只报告了两个骨干，与通用编码 agent 的比较也只是补充章节，而非完整的基线扫描。
- Repository note: 论文没有给这套任务集单独的 benchmark 名字；它随系统仓库发布，被称作「the LQCD benchmark with 70 scientific computing tasks」。

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — 同样是领域专用的科学计算 benchmark，最难一档也是端到端的求解器配置与执行。
- [Collider-Bench](./collider-bench.md) — 同样评估 agent 做高能物理分析，对照隐藏的参考数值结果计分。
- [FEABench](./feabench.md) — 同样以「生成的仿真工作流能否经真实求解器复现出正确物理量」来给 agent 打分。
- [CodePDE](./codepde.md) — 同样把数值科学计算表述为由执行来校验的 LLM 代码生成。
