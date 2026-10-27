# Into the Unknown (2026)

> [English](../../works/into-the-unknown.md) | **简体中文**

> **首次公开：** 2026-10-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.19159)

## Overview

Into the Unknown 想知道，agent 能不能推进一个还没有人做过的研究方向。研究类基准通常拿人类已经做出的东西来评分，比如已发表的结果、参考解答或奖牌分数线。这里改由一篇科学论文的作者提出一个尚未发表的后续方向，并写明一篇成功的后续论文必须满足哪些条件。agent 拿到原论文、它的代码和数据以及这份说明，要交出一篇后续论文，外加代码和日志。随后由一个 agent 形式的 judge 按科学家写的条件检查提交物，条件分成诚信、完整性和充分性三类。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** [Into the Unknown: Benchmarking AI agents on open scientific research problems](https://arxiv.org/abs/2610.19159)，2026 年预印本（arXiv 备注："preprint under review"）。
- **Code:** <https://github.com/prometheus-eval/into-the-unknown>
- **Data:** <https://huggingface.co/datasets/prometheus-eval/into-the-unknown>（任务、agent 轨迹和 agent 写出的 135 篇论文）
- **Leaderboard:** <https://prometheus-eval.github.io/into-the-unknown/viewer/>
- **Venue:** arXiv 预印本（cs.AI、cs.CL、cs.LG，2026）

## Summary

每个实例由一篇原论文、一份任务说明和两套评分细则组成。方向细则把科学家的成功条件和必须交付的内容拆成一个个叶子问题。诚信细则列出哪些情况会让提交物无论报告什么都不可信，比如论文里的数字在日志中找不到出处。只有诚信（C1）、完整性（C2）和充分性（C3）三项的每个节点都通过，提交物才算有效。所有条件都写在任务说明里，所以难点在于把工作做出来，而不是猜隐藏的标准。135 份提交没有一份有效，每个 agent 的严格指标都是 0%；真正把 agent 区分开的是节点通过率。

## Tasks

15 个开放问题，来自 10 位现在或曾经在美国能源部国家实验室（LANL、SNL、LBNL、LLNL、PPPL、Ames）工作的科学家。有一篇论文没有国家实验室作者，加入它是为了覆盖物理信息神经网络这一主题。A 组 8 篇论文发表于 2024 年或更早；B 组 7 篇提交于 2026 年。选题要求能请到论文的第一或最后作者参与，并且论文的实验是计算性的，后续工作只靠代码就能完成。约一半方向是探索性的：例如在有效和无效区间对变分格点标量 QED 做压力测试（P6），或者找出 Vlasov 理论从哪里开始无法预测 MagCBET 粒子模拟的行为（P13）。其余是优化目标，比如减少 Projected Hessian Learning 需要的随机探针数（P11）。任务说明和细则先由 Claude-Opus-5 根据科学家的回答起草，科学家随后做了 112 处修改。工作区里放着转成 Markdown 的原论文，以及它的代码和数据。

## Domains

按 Table 1 的标注：量子计算（4 个：P5、P9、P10、P14），等离子体物理（2 个：P6、P13），计算化学（2 个：P1、P11），材料科学（2 个：P2、P15），科学机器学习（3 个：P4 自主实验的采集策略、P8 参数化 PINN、P12 精确的大规模高斯过程），计算成像（1 个：P3），颜色科学（1 个：P7，感知颜色空间）。

## Evaluation

- 由一个评分 agent 回答每套细则的叶子问题，再对每项条件算出节点通过比例。严格评分要求所有节点都通过，"几乎"评分要求至少 90% 通过。主要指标是在严格评分下同时通过 C1、C2、C3 的提交物比例。
- judge 是在 Codex SDK 中运行的 GPT-6-Astra，最高推理强度。每份提交评判四次，按节点多数合并（四次中三次；2 比 2 记为不通过）。
- 九个 agent 都在各自的原生 harness 中运行，最高推理强度，上下文 1M：Claude-Opus-4.8、Opus-5、Fable-5 和 Opus-5.5（claude-agent-sdk）；GPT-5.6-Sol 和 GPT-6-Astra（codex-sdk）；DeepSeek-V4-Pro-0813（deepseek-harness）；Kimi-K3（kimi-agent-sdk）；GLM-5.3（software-agent-sdk）。
- 结果（Table 2）：九个 agent 的严格有效率都是 0.00%。诚信和方向两套细则的节点通过率，最高是 GPT-6-Astra 的 97.77% 和 83.62%，其次是 Claude-Opus-5.5 的 90.38% 和 80.00%，最低是 GLM-5.3 的 54.41% 和 44.25%。只有三个 agent 在某些论文上通过了严格 C1：GPT-6-Astra 15 篇中 11 篇，GPT-5.6-Sol 6 篇，Claude-Opus-5.5 4 篇。只有一份提交（GPT-6-Astra）既诚信又完整。
- 失败统计（Figure 3）：135 份中有 114 份没通过诚信检查。最常见的违规是论文与代码不一致（90 份）、数字与证据矛盾（85 份），以及声称完成了其实没做的工作（68 份）。128 份缺少要求的文件或记录，120 份没满足方法或流程要求，83 份没达到科学家设定的目标。对 64 条轨迹的人工审查发现：58 条自我验证过于宽松，34 条回溯不足，21 条擅自缩小了任务范围。
- judge 验证（附录 A）：每位原作者盲审三篇后续论文，分别出自 Claude-Opus-5、Claude-Fable-5 和 GPT-5.6-Sol。他们的批评被拆成单条。关于是否达成方向的 41 条判断，细则全部覆盖，流程的结论也与专家全部一致。对审稿式的主要缺陷，覆盖率 96.97%，一致率 80.34%（按论文平均）；对科学质量和影响，分别为 89.05% 和 68.68%。
- judge 稳定性（附录 B，52 份提交各评四次）：GPT-6-Astra judge 给出相同总评的比例为 86.5%，Claude-Opus-5.5 judge 为 57.7%，因此默认使用 GPT-6-Astra。
- Repository note：GPT-6-Astra 既是默认 judge，又是被评测的 agent 之一，而且节点通过率最高。稳定性研究比较的是 judge 与 judge 之间的差异，没有检验自我偏好。

## Typical Duration

不设时间上限，agent 一直运行到自己结束会话，最多重新启动五次（即 "Ralph Wiggum" 循环）。需要 GPU 的六篇论文各给一个 8×H200 节点，其余九篇给 32 个 vCPU 的 Xeon 节点，可用内存 61 GiB；另配 1 TB 存储。135 份提交的生成共耗时 1,942.81 小时，评测耗时 62.95 小时（墙钟时间）。各 agent 运行时长的中位数从 1.3 小时（GPT-6-Astra）到 19.5 小时（DeepSeek-V4-Pro-0813）。网络访问不受限制。

## Main Contribution

开放研究没有参考答案，这里改用原论文作者事先写下的必要条件来评分。另设的诚信细则能把那些看起来像后续论文、实际却报告了没做过或没有依据的工作的提交物识别出来。

## Key Design Ideas

- 固定研究方向和科学家的标准，就把可接受的后续工作缩小到细则能检查的范围。
- 预先放好原论文的代码和数据，把推进新方向的能力与重新实现旧工作的能力分开。
- 这些方向经原作者确认没有已知的发表成果，所以不限制网络访问。
- 同时报告严格评分、"几乎"评分和节点通过率，即使所有严格分数都是零，agent 之间仍能区分开。

## Strengths

- 专家元验证量出了细则管不到的地方：在细则针对的问题上一致率是 100%，到科学价值上降到 68.68%。
- 失败类别、轨迹行为和诚信违规都按提交逐份计数，而不是只举例子。
- 轨迹、论文、文件系统和 judge 判定都已公开。
- 一项带 Holm 校正的 bootstrap 分析表明，无论是比较不同 agent，还是看同一个 agent，都没有证据显示运行越久提交越好。

## Limitations

- 只有 15 个问题，任何一个领域最多四个。
- 作者指出，细则检查的是必要条件，捕捉不到叙述质量，也判断不了前人工作是否真正支撑了所用方法，这些仍要靠专家审阅。
- Repository note：论文中的数字并不总是一致。轨迹审查写的是从"105 份提交"中抽 64 份，Figure 6 也写"全部 105 份提交"，而基准共有 135 份。第 5.2 节说 GPT-5.6-Sol 通过的节点最多，并且是唯一有诚信检查通过的 agent；Table 2 则显示 GPT-6-Astra 节点通过率最高，有三个 agent 通过了诚信检查。本卡片以 Table 2 为准。
- Repository note：论文没有给出每次运行的 token 或美元成本。

## Related Works

- [PaperBench](./paperbench.md) — 按与作者共同制定的细则评复现已发表论文；Into the Unknown 评的是还没人做过的后续工作。
- [Terminal-Bench Science](./terminal-bench-science.md) — 任务同样由一线科学家提供，但每个任务都附带标准解答和测试。
- [MLR-Bench](./mlr-bench.md) — 开放式研究论文由 LLM 审稿人打分，而不是按作者给定的条件评。
- [EurekaBench](./eurekabench.md) — 作者团队部分重合；解释已知观测，而不是延伸一篇论文。
