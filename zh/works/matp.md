# MATP (2025)

> [English](../../works/matp.md) | **简体中文**

> **首次公开：** 2025-12-29 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2512.23511)

## Overview

MATP（Multi-step Automatic Theorem Proving）是一个评估框架，通过将自然语言推理的每一步翻译为一阶逻辑（First-Order Logic），再交由自动定理证明器裁决，来验证 LLM 生成的推理。它被应用于一个包含 10,830 条推理实例的 benchmark，这些实例由 10 个 LLM 在取自 PrOntoQA-OOD、ProofWriter 和 FOLIO 的任务上产生。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2512.23511>
- **Code:** <https://github.com/zxyhp/MATP>
- **Venue:** ICSE 2026

## Summary

MATP 针对这样一个局限：流畅的语言会掩盖多步 LLM 推理中细微的逻辑错误，而事实核查、self-consistency 和基于规则的验证只能部分地检测出它们。该框架将前提、候选结论以及生成的每一个推理步骤翻译为一个统一的一阶逻辑表示，把公式转换为 TPTP，并应用自动定理证明器既标注每一步，又搜索支撑结论的有效证明路径。在由 10 个 LLM 生成的 10,830 条推理实例上，作者报告 MATP 在推理步骤验证上超过基于 prompting 的 baseline 42 个百分点以上，并且尽管答案准确率相近，reasoning 模型产生的推理链比通用模型更具逻辑一致性。

## Tasks

1,083 个测试用例采样自三个演绎推理数据集——384 个来自 PrOntoQA-OOD、344 个来自 ProofWriter、355 个来自 FOLIO——每个用例提供前提、一个候选结论和一个 ground truth 标签。采样刻意针对更难的子集：PrOntoQA-OOD 的 4-hop 子集、排除 Unknown 标签任务后的 5-hop ProofWriter 测试集，以及限定为 True / False 且丢弃了结论简单重复前提的实例的 FOLIO 训练集用例。随后每个用例由 10 个 LLM——五个通用模型和五个 reasoning 模型——作答，产生 10,830 条包含前提、结论、推理链和预测答案的 benchmark 实例。

## Domains

对自然语言前提集合的演绎逻辑推理，涵盖合成的基于规则的本体（PrOntoQA-OOD、ProofWriter）以及关于人物、地点、数量和事件的人工撰写的真实世界陈述（FOLIO）。

## Evaluation

- **步骤正确性标注。** 对一个推理步骤及其否定分别在前提下调用证明器，将该步骤标注为 True、False 或 Unknown；若二者皆可证明，则说明前提自相矛盾，返回 Error。
- **有效证明路径存在性。** 将那些引入了无法由已纳入步骤推导出的新事实的 True 步骤组装为候选证明路径，若在该路径下评估的结论与 ground truth 标签一致，则该路径有效。
- **细粒度推理链分类。** 六个类别综合了答案正确性、步骤正确性和证明路径有效性——正确答案对应 T1–T4，错误答案对应 F1–F2——而 Error 专门留给耗尽 NL2FOL 重试次数的输入。
- **NL2FOL 翻译质量。** 整体层面的 Execution Rate 和 Execution Accuracy，句子层面的 FOL BLEU 和 Logical Equivalence。
- **报告结果（Table 1）。** 在 10 个目标模型上平均，推理步骤正确性的 macro F1 在 PrOntoQA-OOD 上为 94.26%、在 ProofWriter 上为 91.24%、在 FOLIO 上为 84.42%，而 GPT-4o prompting baseline 分别为 47.79%、49.36% 和 45.17%，DeepSeek-R1 baseline 分别为 61.30%、42.43% 和 37.55%；Execution Accuracy 平均为 99.90%、99.24% 和 70.88%。在一个由 200 个经过变异的 PrOntoQA-OOD 任务构成的独立分类集上，MATP 在 T1–T3 上达到 100%，在 T4 上达到 96%。

## Typical Duration

MATP 每个任务的平均处理时间约为 9 秒，相比之下 GPT-4o prompting baseline 约为 6 秒，DeepSeek-R1 为 96 秒。NL2FOL 翻译对每个输入最多尝试三次生成；论文未给出每个实例单独的 wall-clock 或 token 预算。

## Main Contribution

一个事后评估框架，将前提、结论和每一个推理步骤自动形式化为一阶逻辑以交由自动定理证明器裁决，并配以一套对推理链的六类分类，把真正的演绎推理与信息复述或偶然正确区分开来。

## Key Design Ideas

- 单趟 NL2FOL 翻译，把前提、候选结论和推理步骤转换为一个统一的一阶逻辑表示，在此之前先过滤掉不确定和推测性的陈述。
- 由 Python 脚本完成的确定性一对一 FOL 到 TPTP 转换，之所以采用是因为 TPTP 语法更复杂冗长，直接从自然语言翻译到 TPTP 更容易出错。
- 三值步骤验证，返回 True、False 或 Unknown 而非二元判断，并在证明器遇到执行错误或与 ground truth 标签矛盾时触发重新生成。
- 证明路径构造仅限于那些新增事实的 True 步骤，从而把蕴含结论的推理链与仅仅到达结论的推理链区分开来。

## Strengths

- 由定理证明器进行的符号化裁决，使步骤级判定具有确定性，且不依赖于 judge 模型自身的推理质量。
- 联合考虑答案正确性、步骤正确性和证明路径可靠性，把偶然正确的答案与真正可靠的推导区分开来。
- 在报告验证结果的同时报告翻译质量，使该框架自身最主要的失败模式保持可见，而不是把它折叠进最终得分里。

## Limitations

- Repository note: 验证质量受 NL2FOL 环节的限制，而该环节本身是由 GPT-4o 完成的 LLM 翻译——分析失败率在 PrOntoQA-OOD 上平均为 1.04%、在 ProofWriter 上为 1.22%，但在最接近日常语言的 FOLIO 上升至 31.92%。
- Repository note: 范围局限于对给定前提的演绎推理，归纳和溯因推理不在论文关注范围内，且被评判的 trajectory 是纯文本推理链，而非 tool call 或环境动作的序列。

## Related Works

- [T-Eval](./t-eval.md) — 同样把评估分解到最终任务成败之下，但沿着 tool-use 能力子过程而非相继推理步骤之间的逻辑蕴含关系。
- [TRACE](./trace.md) — 同样对中间 trajectory 质量而非最终答案打分，但通过加权的多维度 rubric，而非证明器给出的可证明 / 可反驳 / 不确定裁决。
- [AgentAtlas](./agentatlas.md) — 同样为每一步打上固定类别体系中的标签，但通过在已有 benchmark 上审计控制决策，而非将每一步对照形式化的前提加以裁决。
