# SKILL-KD (2026)

> [English](../../works/skill-kd.md) | **简体中文**

> **首次公开：** 2026-07-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.28048)

## Overview

SKILL-KD 用来改进一个冻结的、较弱的 student agent：在同一个任务上，对比 student 失败的运行和更强 teacher 的运行，从两者的差异中写出文本 skill patch。只从 student 自己的失败中构建 skill，未必能看出它缺什么；teacher 的成功运行里，关键做法往往没有明说，没法直接照搬。SKILL-KD 把可操作的差异提炼成一个 patch，让 student 带着它重跑这个任务，只有重跑成功才提交 patch，否则最多修改三次；之后由一个整合步骤决定每个被接受的 patch 是新增、合并进已有规则，还是跳过。得到的 skill 文件在五个 benchmark 的留出划分上、两种 student–teacher 设定下测试。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 这是 skill 蒸馏方法，评测用的是通用 agent 任务（搜索问答、电子表格、文档 VQA、ALFWorld），另有一个数学 benchmark 作为测试平台；没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.28048>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

对一个训练任务，一个整合 agent 会拿到冻结 student 的失败 trajectory、teacher 的 trajectory、当前 skill library 和一份编辑历史，然后提出一个包含四个字段（title、content、why、trace）的 patch；agent 只能看到 title 和 content，why 和 trace 只留在供审计用的历史里。Patch 应用后，student 重跑这个任务，由任务 evaluator 给 trajectory 打 [0, 1] 的分；得分为 1 就提交 patch，否则换一个修改后的 patch，最多进行 n = 3 轮自适应修改。始终没能带来成功的 patch 不会写进 library 或历史。随后 Drift-Aware Skill Consolidation 借助指向过去编辑的 trace 链接，把已有规则分为 cover、partial 或 unrelated，并提交 add、modify、delete 或 skip。接受测试只是在同一个训练任务上成功，所以它本身并不能说明 patch 能泛化。

## Tasks

N/A — SKILL-KD 是 skill 蒸馏方法，不是 benchmark。所用 benchmark（训练/验证/测试）：

- SearchQA 400/200/1400；SpreadsheetBench 80/40/280；DocVQA 107/53/374；LiveMath 35/18/124；ALFWorld 39/18/134。没有官方划分的 benchmark 按 2:1:7 的比例划分。
- 第 1 组（同一模型系列）：student 为 Qwen3.5-4B，teacher 为 Qwen3.7-plus。
- 第 2 组（不同模型系列）：student 为 Qwen3.6-35B-A3B，teacher 为 ChatGPT-5.5。

Skill 只从训练划分构建；验证划分只给需要它的 baseline 使用。

## Domains

通用 agent 任务（搜索问答、电子表格操作、文档 VQA、文本具身任务），外加数学解题（LiveMath）。

## Evaluation

- **循环内部。** 以一个训练任务为例：student 失败（得分 < 1）→ 根据 student 与 teacher 的差异提出 patch → student 带着 patch 重跑 → evaluator 得分为 1 → 提交 patch 并交给整合步骤；得分 < 1 → 修改 patch，最多 3 轮。
- **留出集。** 每个 benchmark 测试划分上的原生 hard-success 或 exact-match 分数，来自单次评测。
- **报告结果（五个 benchmark 平均）。** 第 1 组：No Skill 43.5，最强 baseline SkillOpt 63.5，SKILL-KD 66.8。第 2 组：No Skill 57.9，SkillOpt 68.6，SKILL-KD 74.6。其他 baseline：EvoSkill、Trace2Skill、SkillGen。ALFWorld 从 30.6 升到 86.6（第 1 组），从 59.7 升到 96.3（第 2 组）。
- **获取方式 ablation（第 1 组平均）。** 只用 student 60.1（96 条规则），只用 teacher 58.3（80 条规则），批量 59.4（46 条规则），不做自适应修改的成对方式 59.0（85 条规则），SKILL-KD 66.8（38 条规则，3,010 词）。
- **整合 ablation（第 1 组）。** 去掉整合后，SpreadsheetBench 从 24.3 降到 14.6，LiveMath 从 54.8 降到 27.4。
- **自适应轮数（第 1 组，训练集累计成功率）。** n = 0：58.9；n = 1：67.7；n = 2：70.8；n = 3：72.7。

## Typical Duration

TODO(reference) — 没有报告 token 和成本数字。Student 在本地四张 NVIDIA A100 80GB GPU 上运行；teacher 和整合模型通过 API 调用。

## Main Contribution

作者提出把 skill 当作从强 agent 向弱 agent 传递知识的显式载体：在同一任务上对比两个 agent 的 trajectory，通过让 student 重跑来验证每个 patch，并借助带 trace 链接的历史来整合 patch，以限制漂移。

## Key Design Ideas

- 对比式输入：同一任务上 student 的失败和 teacher 的 trajectory。
- 重跑后再提交的把关：只存储能让 student 成功的 patch。
- 审计字段（why、trace）不放进 agent 的 prompt，但在整合时使用。
- Drift-Aware Skill Consolidation 优先更新部分重叠的规则，只有出现新的可复用触发条件时才新增规则。
- 整个 skill 文件直接放进 prompt，而不是检索。

## Strengths

- Ablation 在相同 benchmark 上分开比较了只用 student、只用 teacher、批量、成对几种获取方式，以及整合步骤。
- 有两种 student–teacher 设定：同系列和跨系列。
- 生成的 skill 文件比各 ablation 变体都小（38 条规则），得分却更高。

## Limitations

- 接受测试只是在同一个训练任务上成功；泛化要到事后在留出划分上才能看到。
- 平均有 38.5% 被接受的 patch 来自 teacher 失败的 rollout，所以 teacher 的 trajectory 并不总是正确的参照。
- 每个分数只评测一次，没有报告方差。
- 整个 skill 文件放进 prompt，prompt 长度会随 library 增长。
- Repository note: 论文没有专门的局限性章节，以上几点来自报告的结果。本卡片依据 arXiv 摘要和 v1 HTML 全文编写（2026 年 11 月）；论文已修订到 v4，后续版本的数字可能不同。

## Related Works

- [SkillGen](./skillgen.md) — 同样按重跑结果把关 skill，并作为 baseline 出现；它对比的是 agent 自己的成功和失败，而不是 teacher 的运行。
- [MIND-Skill](./mind-skill.md) — 同样让 agent 只凭 skill 重新执行任务来验证 skill。
- [SkillMisevo-Bench](./skillmisevo-bench.md) — 研究持久化的 skill library 如何积累有害的 procedure，这与 SKILL-KD 的整合步骤要应对的漂移是相关风险。
- [SkillEvolBench](./skillevolbench.md) — 测量写出的 skill 在留出的、偏移后的任务上是否还站得住。
