# Mathematics

> [English](../../domains/mathematics.md) | **简体中文** · [← 全部 domains](./README.md)

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
| SciCode | 2024 | 为科学家整理的问题编写科研代码；其 16 个自然科学子领域分属五大主领域，数学是其中之一。 | 80 个主问题分解为 338 个子问题，混合知识回忆、推理与代码合成。 | 对照科学家标注的金标准解与测试用例执行。 | [→](../works/scicode.md) |
| HARDMath | 2024 | 在自动生成的应用数学问题上运用研究生水平的解析近似技术——渐近方法。 | 366 题的 HARDMath-mini 测试集加 40 道应用科学应用题；少样本思维链下的静态解题。 | 对照经数值验证的真值解计算准确率。 | [→](../works/hardmath.md) |
| PDE-Controller | 2025 | 在信号时序逻辑规格下形式化并推理 PDE 支配系统（热方程与波动方程）的控制。 | 人工案例加 200 万合成样本上的自动形式化、推理与程序合成任务。 | 任务指标加所得 PDE 控制的效用增益。 | [→](../works/pde-controller.md) |
| SciVisAgentBench | 2026 | 数学数据的科学可视化与数据分析——其七个应用领域之一——把自然语言意图翻译为可执行可视化操作（如场计算、拓扑任务）。 | 108 个专家精心设计的 SciVis 案例，横跨七个科学领域与 15 类可视化操作，通过 CLI、MCP 服务器与 Python API 在 ParaView、napari 等平台上运行。 | 以结果为中心的多模态管线，结合一个 MLLM judge（报告为 Claude-Opus-4.6；与人类评分 Pearson 0.808）与确定性评估器——图像指标（PSNR、SSIM、LPIPS）、代码检查器，以及基于规则/逐案例的验证器。 | [→](../works/scivisagentbench.md) |
| TCS-Bench | 2026 | 对理论计算机科学成果（FOCS/STOC/SODA）做研究级定理证明；证明生成任务本质上属数学，需要多步形式化风格的数学推理。 | 300 个定理证明任务，每个是一条目标命题加从 FOCS/STOC/SODA 论文（2020–2026）中抽取并组装的上下文；模型产出一份自包含证明。 | 证明由一个自动验证 agent 检查（四次 Gemini 3.1 Flash 调用，四取三多数表决），并对照一个 100 项的人类专家标注集校准，一致率超过 90%。 | [→](../works/tcs-bench.md) |
| VESTA / DAWN | 2026 | 把统计模型拟合当作一个迭代循环：通过作图、假设函数形式、拟合、查看残差再修正，还原生成样本的那个分布，或生成时间序列的那套动力学。 | 400 个实例的 benchmark 中，DAWN 的 300 个领域中立实例——50 个简单与 100 个困难的分布拟合任务（每个 600–1,500 个数据点），以及 50 个简单与 100 个困难的时间序列任务（每个 600 个观测）；三种视觉语言底座。 | 用恰当评分规则而非精确匹配：分布任务用拟合分布与真实分布之间的 Jensen–Shannon 散度，时间序列用留一交叉验证下的期望对数预测密度（ELPD-LOO）。 | [→](../works/vesta-dawn.md) |
| ScienceBoard | 2025 | KAlgebra 中的计算机代数与 Lean 4 中的定理证明——它们是承载各领域的六款专业软件中的两款。 | 单台 Ubuntu 虚拟机中 169 个人工整理的计算机使用任务：38 个纯 GUI、33 个纯 CLI、98 个 GUI+CLI 混合；逐软件任务数未公布。 | 通过支持精确匹配、区间判定与数值容差的模板，程序化检查关键中间输入/输出与虚拟机的最终状态；代数属得分最高的领域之一（GPT-5 最高 62.07%）。 | [→](../works/scienceboard.md) |
| SciVQR | 2026 | 数学中的多模态科学推理，六个顶层计分学科之一，也与物理并列为最难的两个。 | 3,254 道配图的竞赛与考试题目，横跨六个学科、54 个子领域（2,545 道选择题、709 道自由作答；分 easy/medium/hard 三档）；15 个多模态模型零样本受评，并对比用与不用 CoT。各学科的题目数量未公布。 | 按学科报告零样本准确率，另有五维 rubric（忠实性、信息量、冗余、幻觉、步骤缺失）对照专家撰写的解题过程为生成的推理打分。 | [→](../works/scivqr.md) |
| HiSciBench | 2025 | 面向文献的数学工作：对来自 arXiv 的数学论文做解析、翻译、问答与综述生成。 | 8,735 个实例中数学占 1,655 个——200 个通用科学问答、208 个文献 OCR、208 个翻译、821 个单语文献问答、208 个跨语文献问答与 10 个综述选题；数学不贡献数据驱动发现类实例。18 个模型受评。 | 按层级选取指标：问答层用准确率，文献 OCR 用词级准确率，翻译用 BLEU；综述层由 LLM judge 按 1–5 分 rubric 评 Coverage、Structure、Relevance、Synthesis 与 Critical Analysis，另计引文可核验性、元数据准确性、忠实性与时效性。 | [→](../works/hiscibench.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [TCS-Bench](../works/tcs-bench.md)
- [Hard2Verify](../works/hard2verify.md)
- [ProcessBench](../works/processbench.md)
- [PRMBench](../works/prmbench.md)
- [Pseudo-Formalization](../works/pseudo-formalization.md)
- [FormalRewardBench](../works/formalrewardbench.md)
- [MATP](../works/matp.md)
- [AIRS-Bench](../works/airs-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [SciCode](../works/scicode.md)
- [HARDMath](../works/hardmath.md)
- [PDE-Controller](../works/pde-controller.md)
- [VESTA / DAWN](../works/vesta-dawn.md)
- [ScienceBoard](../works/scienceboard.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
