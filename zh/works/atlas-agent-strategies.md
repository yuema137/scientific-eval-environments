# ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning (2026)

> [English](../../works/atlas-agent-strategies.md) | **简体中文**

> **首次公开：** 2026-08-14 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.14352)

## Overview

ATLAS 从 LLM agent 的大量运行记录中学出一个有限状态的行为模型，让分析人员能看出哪些策略通向成功、agent 在哪里打转或失败。Agent 评测通常只报告任务成功率，原始 trace 留给人手工去读。ATLAS 在 trace 和分析人员之间加了一步：由 LLM 把每个 action-observation 对映射成一个抽象符号，再用被动 automata learning 算法把这些符号化 trace 合并成一个 Markov chain，状态上带成功标签，边上带转移概率。论文在一个渗透测试 agent 上做评估：一方面直接查看学到的模型，另一方面把从模型中提取的策略交给更小的执行模型使用。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities

N/A — 这是 trajectory 分析框架，演示场景是一个做 Linux 提权的渗透测试 agent，没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.14352>
- **Code:** <https://doi.org/10.6084/m9.figshare.32841767> （复现包：学到的模型、抽象 trace 和具体 trace、源代码）
- **Venue:** ACM/IEEE MODELS 2026（据 arXiv 备注已录用）；DOI <https://doi.org/10.1145/3822455.3838777>

## Summary

抽象分三个 LLM 阶段完成。第一步，把所有运行中的交互归入 action 类别（可选带一个目标）和两段式的「Value_Target」observation 类别，例如 `DISCOVERY_SUID` 或 `ERROR_NONE`；第二步，把相近的标签归一成一套紧凑的词表；第三步，给每条 trace 里的每次交互分配一个（action 类别，输出类别）对。随后用状态合并算法 Alergia（在 AALpy 中实现）从这些符号化 trace 学出一个带标签的 Markov chain。为了便于解释，再对 chain 做模型变换来缩小它：要么把从初始状态到成功的路径提取成无环图，要么每个状态只保留 top-k 条转移、删去无法到达成功的状态，并把强连通分量折叠起来。作者明确说明，抽象会有意丢掉低层细节。

## Tasks

N/A — 分析框架，没有提出新的任务集。案例研究使用 HackingBuddyGPT 提权 agent，在 12 台有漏洞的 Linux 虚拟机上运行（排除了一个场景），每台机器跑 20 次，每次最多 20 轮。

## Domains

Computer Science（安全方向）：Linux 提权渗透测试。

## Evaluation

ATLAS 从两个方面评估。

- **定性查看模型。** Trace 由 DeepSeek V4 Flash 生成，抽象也由它完成。在其中一个场景里，学到的 chain 显示 agent 先做侦察（`id`、`sudo -l`）；发现用户以后，它要么发出格式错误的命令（一种反复出现的失败模式），要么继续执行 `sudo -l`，后者约有 0.4 的概率在两步内成功。到达 `EXPLOITABLE_SUDO` 之后，agent 有 30% 的情况直接成功，70% 的情况会去执行 `sudo id`，论文认为这一步效率不高。
- **把策略迁移给小模型执行。** DeepSeek V4 Pro 作为知识模型，从学到的 chain 中总结策略；ministral-8b 和 ministral-14b 在五种模式下执行，每种模式按 60 次运行中的成功次数计分：

| Mode | ministral-8b | ministral-14b |
|---|---|---|
| Baseline（不用模型） | 5.0% | 1.7% |
| Common path | 1.7% | 11.7% |
| Minimal | 8.3% | 11.7% |
| Guided | 8.3% | 21.7% |
| Dynamic（随环境一起沿 chain 前进，每次给出一个建议 action，带防重复和死路检测） | 28.3% | 38.3% |

论文还说 ministral-14b 解决了 50% 的 benchmark 任务；它的表格显示 12 台机器中有 6 台被攻破，所以这是按机器统计的数字。模型变换能把一个 41 状态的模型缩成一个小的解释模型。论文讨论了审计这一用途，但没有做评估。

## Typical Duration

每次运行最多 20 轮。Wall-clock 时间和抽象成本为 `TODO(reference)`。

## Main Contribution

一条把 LLM 引导的 trace 抽象和 automata learning 结合起来的 pipeline，用来还原 agent 行为的可解释有限状态模型；论文还演示了这些模型能揭示策略和失败循环，并能用来引导更小的模型。

## Key Design Ideas

- 把每一步抽象成（action 类别，observation 类别）对，这样学到的字母表描述的是行为，而不是原始 shell 字符串。
- 在分配标签之前，先把 LLM 在所有运行上提出的标签统一归一，使所有 trace 共用一套词表。
- 学一个随机模型（用 Alergia 学 Markov chain），让分支概率和带成功标签的状态都能直接看到。
- 对学到的模型做变换（成功路径提取、top-k 剪枝、删除不可达状态、SCC 折叠），生成简短的解释。
- 在运行时把学到的模型当作向导，引导较弱的执行模型（dynamic 模式）。

## Strengths

- 把一组 agent trace 变成一个模型，用分支概率量化某条策略被采用的频率和成功的频率（论文）。
- 迁移实验检验了提取出的策略确实带有可用信息，而不只是读起来清楚（论文）。
- 公开了包含学到的模型、trace 和源代码的复现包（论文）。

## Limitations

- 作者指出，抽象会丢失低层细节，而类别发现需要能力很强的 LLM。
- 能否扩展到长 trajectory、多样或变化的任务以及异构环境，仍未解决（论文）。
- 评估只是渗透测试场景下的概念验证；有用的行为模型需要满足哪些要求，还没有定义（论文）。
- SCC 折叠可能把对成功很关键的步骤吞掉；论文举的例子是 SCC 内部的一次文件读取。
- Repository note: 迁移结果基于每种模式、每个执行模型 60 次运行；最好的模式也只有 38.3%。

## Related Works

- [Insights Generator](./insights-generator.md) — 同样分析大量 agent trace 来找出行为模式，用的是假设检验而不是 automata learning。
- [AgentAtlas](./agentatlas.md) — 用固定的分类体系给 agent 的控制决策分类，而不是从 trace 中学出行为模型。
- [Trace2Tower](./trace2tower.md) — 同样在抽象后的 trace event 上建 transition graph，但目的是归纳可复用的 skill，而不是解释行为。
