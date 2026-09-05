# AI-Researcher (2025)

> [English](../../works/ai-researcher.md) | **简体中文**

> **首次公开：** 2025-03-04 · **来源：** [官方代码库发布公告](https://github.com/HKUDS/AI-Researcher)

## Overview

AI-Researcher 一次给出两样东西：一个自主研究系统，以及用来衡量它的 benchmark Scientist-Bench。此前那些系统只自动化研究中的某一环，出想法、写实现或者写论文各管一段，也各用各的尺子，谁也说不清一次端到端的运行产出的东西够不够发表水平。Scientist-Bench 换了个思路：它固定的不是指标，而是比较对象。每个任务都锚定一篇由人类研究者写成的真实论文，agent 生成的稿子会与那篇论文放在一起，由 LLM 审稿人按 ICLR 的评审标准做随机换序的两两比较。作者没有默认这个审稿人可信：在用它给 agent 打分之前，先拿 32 组 ICLR 录用/拒稿配对单独验证了它一遍。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.18705>
- **Project:** <https://autoresearcher.github.io>
- **Code:** <https://github.com/HKUDS/AI-Researcher>
- **Venue:** NeurIPS 2025

## Summary

这项来自香港大学的工作把发现任务写成：给定参考论文 *R*（由 LLM 从目标论文 *y* 中挑出的 15–20 篇文献）、研究指令 *I* 和数据集 *D*，产出实现代码 *C* 和技术报告 *p*。Scientist-Bench 用 22 篇 2022 至 2024 年发表的论文构造这些输入，并分成两个难度：Level-1 给出从 *y* 中提取的研究指令，Level-2 把指令抽掉，只留参考文献和数据，方向要 agent 自己想。评分分两段：一个代码审查 agent 检查实现能否运行、是否忠实落实了报告中描述的方法；一个审稿 agent 在随机交换呈现顺序后，用 −3 到 +3 的分数把生成稿与 *y* 做比较。AI-Researcher 系统本身是一条三阶段多 agent 流水线，论文把它当作参考实现放上去评测：用 Claude 系列作 backbone 时，实现完整率 93.8%、正确性 2.65 分（满分 5），而它写出的论文在每一个 evaluator 眼里都低于人类论文，在给出研究指令的 Level-1 上落后 0.53 到 1.70 分。

## Tasks

**22 篇目标论文，22 个 Level-1 任务和 6 个 Level-2 任务。** 论文取自 2022 至 2024 年，收集分两步：先由 LLM 在 16 个研究方向上生成领域关键词，涵盖 Computer Vision、Graph Learning、Recommender Systems、Vector Quantization、Image Processing、Self-Supervised Learning、Contrastive Learning 等；再按每个关键词从 arXiv 取被引最高的论文（每关键词 10 篇），并用引用量相关指标过滤。最终分布为：扩散模型 4 篇、向量量化 6 篇、图神经网络 7 篇、推荐系统 5 篇；另有两篇（图神经网络和推荐系统各一篇）没有进入完整评测。

- **Level-1，指导式创新。** agent 同时拿到参考文献和从目标论文中提取的明确研究指令，考察它能否执行一个既定想法，覆盖全部 22 篇论文。
- **Level-2，自主探索。** 指令被抽掉，只给参考文献和数据集，agent 必须自己找出空白并提出方向。六个任务由五篇分处不同研究领域的标准论文构造，以减少彼此之间的引用重叠。

有两处构建步骤专门用来防止 agent 靠背诵而非推理过关。生成指令时的提示明确要求把技术规格、模型标识、量化结果和架构细节都挡在研究指令之外；在此之上还有一套匿名化协议，把方法名和模型名替换为通用标识，把实现细节从核心概念中抽离，统一数据集命名，并抹去引用与机构标记。

## Domains

AI 与机器学习研究。论文给出的四个子方向分别是 Computer Vision（扩散模型）、Signal Processing（向量量化）、Graph Learning（图神经网络）和 Information Retrieval（推荐系统）。

## Evaluation

- **第一段：技术执行验证。** 一个代码审查 agent 围绕算法正确性、计算效率、是否遵守既定约束做静态分析与运行验证。*完整性* 记录 agent 是否在既定推理预算内产出了可执行代码，判定依据是一个明确的终止协议：agent 发出 `case_resolved` 或 `case_not_resolved`。*正确性* 是 5 分制：Advisor Agent 先写一份详细的分析报告，点出可能存在的问题，Judge Agent 再据此给分；报告里的数值是多次独立判定的均值。
- **第二段：科学贡献评估。** 对生成报告 *p* 和真值论文 *y*，协议计算 `r, J = PaperReview(RandomSwap(p, y); g)`，其中 *g* 是从 ICLR 标准推得的评审准则，涵盖创新性、理论与方法严谨性、实证验证与实验设计质量。比较评分 *r* 取值 −3 到 +3，正值表示生成论文优于人类论文，0 表示相当。协议用两种手段去偏：随机交换两篇论文的呈现顺序，以及让五个 LLM（GPT-4o、o1-mini、o3-mini、Claude-sonnet-3.5、Claude-sonnet-3.7）在 temperature 1 下各对每篇论文做 16 次独立评估。结果汇总为平均评分和 *Comparable(%)*，后者是评分不低于 −1.0 的生成论文占比。
- **审稿人验证。** 审稿 agent 在 32 组论文配对上与人类专家判断对照，配对采自 2021 至 2023 年的 ICLR proceedings，每组一篇录用、一篇拒稿，且内容 TF-IDF 相似度高。衡量口径是录用预测准确率，也就是被录用论文拿到更高评分的配对占比；各 evaluator 落在 65.62% 到 90.62% 之间，五个里有四个不低于 81.25%。Gemini-2.0-flash 最弱，为 65.62%，因此被排除在主实验之外。
- **实测结果。** 用 Claude 系列 backbone 时，系统在全套 benchmark 上完整率 93.8%、平均正确性 2.65 分（满分 5），正确性按领域从 3.22（向量量化）到 2.20（推荐系统）不等。在一个均衡子集上，Claude 系列 backbone 为 87.5% 完整率和 2.75 正确性，4o 系列为 50.0% 和 1.00。Level-1 上，生成论文对照人类论文的平均评分从 −0.53（GPT-4o 评审）到 −1.70（Claude-3.7），Comparable(%) 从 81.82% 降到 13.64%。Level-2 上同一系统的评分反而更高，为 −0.23 到 −1.22，Comparable(%) 为 100.00% 到 50.00%。这是论文最值得注意的发现，因为它意味着给出明确指令并没有帮上忙。

## Typical Duration

论文没有报告。文中既无墙钟时间，也无 token 或费用核算，唯一提到的预算是衡量完整性时所说的「既定推理预算」。实现阶段倒是描述了一种分级投入的做法：原型实现先在极小数据上测试，通常是 1–2 个 epoch 或数据子集，通过初步验证后才推进到全规模实验。

## Main Contribution

Scientist-Bench：作者称之为第一个能对照人类论文、同时在指导式创新与开放式探索两种场景下评估自主研究系统的 benchmark；连同一套两段式评估协议，其中的审稿 agent 用真实会议录用/拒稿结果验证过。

## Key Design Ideas

- 比较对象是人类论文本身而不是一个阈值，分数因此可以直接读作「生成结果离同领域已发表工作还差多远」。
- 两个难度把执行和构思分开：同一篇目标论文既能生成一个给出研究想法的 Level-1 任务，也能生成一个抽掉想法的 Level-2 任务。
- 匿名化做在任务输入上，覆盖方法名、技术细节、数据集名和引用，用来分清 agent 是真的在解决问题，还是在回忆一篇它记住过的论文。
- 交换顺序加上五个 LLM 审稿人在 temperature 1 下独立评审，评审因此是一组意见而不是一次裁决；不同 evaluator 之间的分歧也照实报告，没有被平均掉。
- 审稿人的验证用的是结果已知、且内容相似度高的真实 ICLR 投稿配对，考的是能否分辨接近的论文，而不是分辨明显不同的论文。
- 实现质量拆成完整性和正确性两项，把「代码跑起来了」和「代码实现的确实是所描述的方法」分开。论文自己举的例子是：某次 4o 系列运行声称完成了 Diffusion Transformer，实际产出的却是一个普通的 Vision Transformer。

## Strengths

- evaluator 先验证再使用，验证结果按模型逐个报告，并点名排除了其中最弱的一个。
- 逐个 evaluator 报告的做法把审稿人分歧直接摆了出来：同一批生成论文，五个 judge 在 Level-1 上给出的 Comparable(%) 从 13.64% 到 81.82%，这本身就是不该依赖单一 LLM 审稿人的证据。
- Level-1 与 Level-2 的对照是在同一批目标论文上做的受控比较，作者如实报告了这个反直觉的结果，没有把它抹平。
- 实现完整性与正确性分开统计，读者就不会把高完成率误读成忠实实现。

## Limitations

- 规模偏小：22 篇目标论文、22 个 Level-1 任务和 6 个 Level-2 任务，覆盖四个子方向。
- benchmark 上只评测了作者自己的系统；对比中换的是 backbone LLM 而不是 agent 系统，没有任何外部系统在这些任务上拿过分数。
- 作者自述了三点不足：评估框架没能充分刻画想法本身的质量，也就是新颖性、可行性和影响力；LLM 审稿人偏重呈现方式而不是实质贡献；代码评估也需要走出「能不能跑通」这一层。
- 系统没有专门的外部记忆，依赖 LLM 上下文窗口，长流程中细粒度信息会被压成抽象摘要。
- 论文没有做污染度量。目标论文发表于 2022 至 2024 年，匿名化协议只能从任务输入中抹去标识，无法把这些论文从预训练语料中拿掉。
- Repository note：这篇论文同时贡献了 AI-Researcher 系统和 Scientist-Bench 及其评估协议；本卡片以 benchmark 和协议为主，把系统作为在其上被评测的参考实现来描述。
- Repository note：附录 A.7.2 把审稿人验证描述为判断与 ICLR 最终决定「完全一致」，而附录 A.9 与表 6 给出的录用预测准确率是 65.62% 到 90.62%。此处采用有量化数值的说法。

## Related Works

- [MLR-Bench](./mlr-bench.md) — 同样用经人类专家验证的 LLM 审稿人给全流程 ML 研究打分。
- [PaperBench](./paperbench.md) — 同样对照近期论文给 agent 产出打分，但要求复现已知结果，而不是比较科学价值。
- [MLGym](./mlgym.md) — 同样把 AI 研究系统与衡量它的 benchmark 一并给出，任务同为开放式研究。
