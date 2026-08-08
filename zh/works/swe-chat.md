# SWE-chat (2026)

> [English](../../works/swe-chat.md) | **简体中文**

## Overview

SWE-chat 是一个大规模、持续增长的真实人类–coding agent 交互数据集，采集自真实环境（in the wild）中的开源开发者，把完整的会话转录（prompt、tool call、agent 回复）与行级的人类 vs. agent 代码作者归属配对。它是数据集与观察性分析贡献，而非任务套件式 benchmark。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.20779>
- **Project:** <https://swe-chat.com>
- **Code:** <https://github.com/SALT-NLP/SWE-chat>

## Summary

SWE-chat 从选择加入（opt-in）Entire.io CLI checkpoint logging 的公开 GitHub 仓库采集 coding-agent 会话转录，每个 checkpoint 都关联到一次 commit，并带有行级的人类 vs. agent 代码归属。数据集覆盖五种 coding agent 的会话（Claude Code、OpenCode、Gemini CLI、Cursor、Factory AI Droid；约 85% 来自 Claude Code），并被定位为一个 living dataset——采集流水线持续发现新会话。在原始轨迹之上，论文对真实世界的使用与失败模式给出了实证刻画——编码模式、代码存活、成本效率、安全影响与用户 pushback——并将其框定为超越 curated benchmark 的实证基础。

## Tasks

N/A — 观察性数据集，非人工编写的任务套件。截至撰稿，数据集包含约 6,000 个编码会话，来自 200+ 个公开仓库，含 13,000+ 个 checkpoint、63,000+ 条用户 prompt、355,000+ 次 agent tool call 与 270 万条日志事件（含来自 200 个 extended-thinking 会话的一小批推理轨迹）。

## Domains

开源仓库上的真实软件工程，覆盖多样的编程语言与任务意图——理解已有代码是最常见的具体用户意图（占 prompt 的 19.0%），其后是新建代码（13.4%）、git 操作（13.4%）与调试（13.0%）；全部 agent tool call 中约三分之一是 bash 命令。

## Evaluation

- **没有 agent 排行榜或评分协议**——刻画轨迹而非为 agent 排名。论文在真实轨迹上定义了一套指标：
  - **代码存活率与编码效率**——agent 产出代码中存活进入用户 commit 的比例。总体编码效率为 44.3%（存活率 50.3%）；vibe-coding 会话达到 59.0% / 64.6%。
  - **每行提交代码的成本、token 与时间效率**——vibe-coding 会话每 100 行提交代码消耗中位数 204K token，约为协作会话的 3 倍（每 100 行 $0.13 vs. $0.05；纯人工 $0.07）。
  - **安全影响**——在 commit 前后快照上运行 Semgrep；vibe-coded commit 每 1,000 行提交代码引入 0.76 个漏洞，约为纯人工（0.08）的 9 倍、协作模式（0.14）的 5 倍。
  - **LLM-judge 标注**——会话成功度（0–100；均值 75.7、中位数 82，90% 的会话评分 50+）、用户 persona、prompt 意图与 pushback 类别，均先对照人类专家 gold 标签验证（标注者间一致性为中到高）。
- **主要报告发现：** 编码呈双峰分布——40.8% 的会话为 "vibe coding"（agent 撰写 >99% 的提交代码），22.7% 为纯人工，36.5% 为协作；全部提交代码行的 55.8% 由 agent 撰写；用户在 39% 的轮次后 push back，在 3.3–6.0% 的轮次中打断 agent，而 Claude Code 仅在 1.1–2.6% 的轮次中主动提出澄清问题。

## Typical Duration

多轮会话；大多数 Claude Code 轮次很短——中位轮次不足一分钟，90 分位低于七分钟，但 99.9 分位的轮次时长超过 100 分钟，且在采集期内呈明显上升趋势。

## Main Contribution

首个把真实用户交互与完整 coding-agent tool-call 轨迹、代码 diff 及行级人类 vs. agent 代码作者归属结合起来的大规模数据集——外加对真实环境使用与失败模式的首轮实证刻画，旨在提供超越 curated benchmark 的证据基础。

## Key Design Ideas

- Opt-in 的 git-hook 日志（Entire.io CLI）把每个会话转录绑定到真实 commit，使轨迹指标植根于用户真正保留的内容，而非合成验证器。
- 行级作者归属把每次 commit 中的代码区分为 agent 撰写、人类撰写、agent 自我覆写与人类删除。
- Living-dataset 流水线持续摄入新会话，支持纵向分析（例如三个月观察窗口内 vibe-coding 占比从 20% 翻倍至 40% 以上）。
- LLM-judge 标注量表（会话成功度、persona、意图、pushback）先对照人类专家标签验证，再规模化应用。
- 隐私流水线：基于命名实体识别的 PII 脱敏、凭据清除，研究程序经 IRB 豁免审查。

## Strengths

- 捕获了人类–agent 交互维度——prompting、引导、覆写、弃用——这是指令固定的 curated benchmark 无法建模的。
- 以真实 commit 为结果锚点，给出任何合成 ground truth 都无法提供的有用性信号（代码存活）。
- 跨 agent 覆盖，并按编码模式给出细致的成本、token 与安全核算。
- 作者将其定位为现实性 benchmark、自适应交互设计与在真实轨迹上训练 user simulator 的原材料。

## Limitations

- 作者指出数据人群是某一开源日志工具在公开仓库上的早期采用者——不含专有企业代码库，且相当大比例的数据来自 Entire.io 自己的仓库，结论可能不可泛化。
- 作者指出被放弃的会话往往从未 commit 因而不可见，可能高估会话成功率与 agent 效率；行级归属也会漏掉语义上存活的代码（例如用户在别处重写了 agent 的建议）。
- 作者提醒 LLM 标注并不完美，下游使用前应进一步验证；效率指标只是代理量，未计入用户审阅输出所花的时间。

## Related Works

- [SWE-bench](./swe-bench.md) — Curated GitHub-issue benchmark 范式：其固定、可验证的任务正是 SWE-chat 用真实环境的迭代式使用来对照的对象。
- [AgentProcessBench](./agentprocessbench.md) — 同样在多轮 tool-use 轨迹上提供步骤/轮次级信号，但依靠对精选轨迹的专家标注，而非来自真实用户、以 commit 为锚的日志。
- [Insights Generator](./insights-generator.md) — 语料级轨迹诊断，正以 SWE-chat 提供的这类大规模真实轨迹语料为前提。
