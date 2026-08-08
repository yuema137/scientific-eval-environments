# Mathematics

> [English](../../domains/mathematics.md) | **简体中文**

## Scope

数学推理与证明：奥赛与研究数学、形式化数学、以逻辑为基础的演绎。应用数学与统计折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Hard2Verify | 2025 | 为前沿模型对近期开放式奥赛问题（IMO Shortlist、Putnam、EGMO、USAMO）的证明逐步评分。 | 对 80 道 2024 年以后问题的 200 份模型生成解答共 1,860 个专家标注步骤，耗费 500 余小时专家人工。 | 专家二元步骤标签为真值；验证器按步骤级、答案级与首错（ErrorID）的 balanced accuracy 与 F1 计分。 | [→](../works/hard2verify.md) |
| ProcessBench | 2024 | 在逐步数学解答中定位最早出错的步骤，从小学水平（GSM8K）到竞赛与奥赛水平（MATH、OlympiadBench、Omni-MATH）。 | 3,400 个问题–解答对，解答来自 12 个开源生成模型并统一重排为段落级步骤。 | 专家标注的最早错误索引为真值；评判者按错误样本与正确样本上准确率的调和平均 F1 计分。 | [→](../works/processbench.md) |
| PRMBench | 2025 | 在多步数学推理中检测细粒度错误类型——simplicity、soundness、sensitivity 三大类下的九个子类。 | 6,216 个实例、83,456 条步骤级标签（每实例平均 13.4 步），负标签由注入构造。 | 对照注入标签的步骤级二元分类；negative F1 与 PRMScore，附人类标注者基线。 | [→](../works/prmbench.md) |
| Pseudo-Formalization | 2026 | 验证自然语言数学证明——奥赛、Putnam 与已发表研究数学——方法是改写为自包含的前提–结论模块并独立核验。 | 200 份前沿模型证明（经 Hard2Verify），外加 ArxivMathGradingBench：35 篇 arXiv 研究论文、40 处作者自行披露的错误。 | 对照专家标签的步骤级与证明级 precision/recall；在 arXiv 论文上按作者披露的修正做错误位置匹配。 | [→](../works/pseudo-formalization.md) |
| FormalRewardBench | 2026 | 在源自 MiniF2F 的奥赛级代数、数论与组合上，判断偏好正确的 Lean 4 证明而非错误变体。 | 250 个偏好对；错误变体由五种专家整理的错误注入策略生成。 | 真值由 Lean 类型检查器确定；reward model 按 pointwise 与位置一致的 pairwise 准确率计分。 | [→](../works/formalrewardbench.md) |
| MATP | 2025 | 把自然语言演绎推理的每一步自动形式化为一阶逻辑并交由自动定理证明器裁决。 | 10,830 个推理实例（1,083 个案例 × 10 个 LLM），取自 PrOntoQA-OOD、ProofWriter 与 FOLIO 的较难子集。 | 证明器对每一步及其否定给出 True / False / Unknown 判定；有效证明路径的存在性对照真值标签检验。 | [→](../works/matp.md) |
| AIRS-Bench | 2026 | 其四个领域之一的数学中的前沿研究任务，覆盖完整研究生命周期，不提供基线代码。 | 套件共 20 个任务；agent 以 CSV 提交留出测试集上的预测。 | 基于执行、只看结果：任务专属评估脚本计分；SOTA 归一化分数，接近上限处用 'march of nines' 变换。 | [→](../works/airs-bench.md) |
| Terminal-Bench Science | 2026 | 其五大分组中 Mathematical Sciences 分组下的应用数学、形式化数学、运筹学与统计任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Math 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |

## Related Works

- [Hard2Verify](../works/hard2verify.md)
- [ProcessBench](../works/processbench.md)
- [PRMBench](../works/prmbench.md)
- [Pseudo-Formalization](../works/pseudo-formalization.md)
- [FormalRewardBench](../works/formalrewardbench.md)
- [MATP](../works/matp.md)
- [AIRS-Bench](../works/airs-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
