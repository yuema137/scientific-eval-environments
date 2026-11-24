# OSWorld-Pro (2026)

> [English](../../works/osworld-pro.md) | **简体中文**

> **首次公开：** 2026-09-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.24890)

## Overview

OSWorld 用任务专属脚本检查机器的最终状态来给 computer-use agent 打分，所以一次失败的运行既说明不了 agent 走到了哪一步，也说明不了是哪个动作出了错。OSWorld-Pro 把每个任务拆成一串有先后依赖的 subgoal，再让 LLM judge 逐步标注：agent 这一步在追哪个 subgoal、这个 subgoal 有没有完成。这样一来，任务分数取决于是否完成了所有可行的 subgoal，而逐步的标签能看出进展卡在了哪里、为什么卡住。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — 这是覆盖多种 Linux 应用和发行版的通用桌面 computer-use benchmark，不评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2609.24890>

## Summary

305 个任务中的每一个都被拆成有顺序依赖的 subgoal，共 2,814 个。拆分先由 DeepSeek-V4-Pro 完成，再由标注供应商人工修正；每个 subgoal 都标明它对应哪一个应用。Agent 运行结束后，GPT-5.6-Sol judge 读完整条 trajectory（每张截图上叠加了对应的 pyautogui 动作，另附 agent 的推理和动作描述），给每一步标上目标 subgoal、可行性、是否推进以及是否完成。只有人工标注为可行的 subgoal 全部完成，任务才算解决。这个 judge 用 67,264 条人工标签做了校验：在目标和完成两类标签上与人工高度一致，在可行性和推进两类标签上明显弱一些。

## Tasks

305 个任务分为三类：Diversity（117 个；覆盖较少见的应用，如 Videos、Archive Manager 和 LibreOffice Draw）、Coordination（109 个；每个任务至少涉及四个应用）以及 Robustness（79 个；使用 Ubuntu 以外的 Linux 发行版和桌面环境，如 Fedora、Alpine、AlmaLinux、bspwm、Xfce 和 LXQt）。任务用 ProCUA-SFT 方法生成，其中 Robustness 任务用的是 Kimi-K2.6。目标不清、有安全隐患或 subgoal 之间没有顺序关系的任务被剔除；含不可行 subgoal 的任务沿用 OSWorld 的做法保留下来。每个任务平均有 9.2 个 subgoal（2 到 27 个不等）。

示例（Diversity）：从 KDE 网站安装 Kid3 音频标签编辑器，然后给一个 MP3 文件加上专辑名和发行年份。对应的 subgoal 是：下载 Kid3（Chrome）、安装（Terminal）、打开 MP3（Kid3）、填写专辑名（Kid3）、填写发行年份（Kid3）。

## Domains

跨多种 Linux 应用（浏览器、终端、办公、媒体、文件与压缩工具）以及多个 Linux 发行版和窗口管理器的通用桌面电脑操作。

## Evaluation

- **逐步标签。** Judge 给每一步标出四项：这一步针对哪个 subgoal，这个 subgoal 是否可行，这一步有没有带来推进，以及这个 subgoal 是否完成。只要有至少一步把某个 subgoal 标为完成，这个 subgoal 就算完成。
- **任务分数。** 主指标是「所有人工标注为可行的 subgoal 都完成」的任务所占百分比。任务级的辅助指标是已完成 subgoal 的百分比。以 Kid3 为例，一个 agent 装好了 Kid3、填了专辑名却始终没填年份，就是完成了 5 个 subgoal 中的 4 个，这个任务不算解决。
- **Judge 校验（Macro-F1，judge 对人工）。** 目标 97.0、可行性 61.9、推进 74.7、完成 94.3；subgoal 级 1−MAE 为 94.1，任务级 1−MAE 为 93.0。第二位人工审核者在可行性上得 91.6，在推进上得 94.1。标注者与审核者之间的 Cohen's κ：目标 0.987、可行性 0.847、推进 0.869、完成 0.940。
- **效率。** Table 2 还报告了每个模型的步数、输出 token 数和 token 成本。
- **报告结果。** 共列出 14 个模型。摘要给出 Claude Opus 5 的总体成绩为 75.7%（在 OSWorld 上为 83.4%）；Table 2 则列出 Claude Opus 4.8 Max 总体为 77.7%。列出的开放权重模型中最强的是 Qwen 3.8 Flash Next，得分 55.1%。Minimax M3 在 OSWorld 上得 75.2%，在 OSWorld-Pro 上只有 28.9%。

## Typical Duration

观测到的 trajectory 平均 55.1 步，最长 149 步。论文没有说明每个任务的步数或时间预算。

## Main Contribution

一个基于过程评分的 computer-use benchmark，包含 300 多个任务、2,800 多个 subgoal 和 67,000 多条人工标注，由 LLM judge 在 subgoal 层面打分；同时总结了与 subgoal 无关的动作、点击错误等过程层面的失败模式。

## Key Design Ideas

- 只保留 subgoal 之间有顺序依赖的任务，这样 subgoal 的完成进度就能反映 agent 推进到了哪里。
- 每个 subgoal 只对应一个应用，这样在多应用任务里就能把失败定位到具体应用。
- 保留不可行的 subgoal 并标注可行性，这样 benchmark 也能衡量 agent 会不会停止追求一个做不到的 subgoal。
- 让 judge 一次读完整条 trajectory，并把动作画在截图上，而不是孤立地逐步评判。

## Strengths

- 人工标注规模大（67,264 条标签，报告投入超过 5,000 人时），四类标签的标注者间 κ 都很高。
- 过程标签可以支撑按动作类型的诊断。例如在按动作类型的拆分中，Claude 系列在键盘动作上至少 89.2%、在滚动动作上至少 84.1%，其他模型在这两类上都没到 80%；每完成一个 subgoal 所需的步数从 4.9（GPT-5.6-Sol）到 21.2（Minimax M3）不等。
- Robustness 任务走出了 OSWorld 所用的 Ubuntu 环境。

## Limitations

- Judge 在可行性（Macro-F1 61.9）和推进（74.7）上比在目标和完成上弱；论文认为这是因为这两类标签主观性更强，并指出提高 reasoning effort 可能导致过多地预测为可行。
- 只有 GPT-5.6 系列模型能处理完整 trajectory 的 judge 输入，其他 judge 模型会遇到 payload 或上下文长度错误。
- 设计上排除了 subgoal 之间没有顺序关系的任务。
- Repository note: 摘要（Claude Opus 5，75.7%）和 Table 2（Claude Opus 4.8 Max，77.7%）给出的最佳模型不一致。
- Repository note: arXiv 页面和本卡片所读的论文正文中都没有看到代码或数据的发布链接。TODO(reference)

## Related Works

- [OSWorld](./osworld.md) — OSWorld-Pro 的基础环境；OSWorld-Pro 用 subgoal 层面的 judge 评分取代了它的最终状态检查。
- [OSWorld-Science](./osworld-science.md) — 同样在 OSWorld 上扩展，但方向是科学软件，而不是过程层面的评分。
- [AgentBoard](./agentboard.md) — 同样借助 subgoal 衡量任务成功之下的进展，但用的是自动计算的 progress rate，而不是经人工标签校验过的 LLM judge。
- [AgentProcessBench](./agentprocessbench.md) — 同样给 agent 的单个步骤打标签，但对象是 tool-use trajectory，目的是评估 step verifier。
