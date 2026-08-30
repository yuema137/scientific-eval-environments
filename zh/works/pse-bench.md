# PSE-Bench (2026)

> [English](../../works/pse-bench.md) | **简体中文**

> **首次公开：** 2026-04-04 · **来源：** [官方代码库创建](https://github.com/sombsuk/PSE-Bench)

## Overview

PSE-Bench 是一个含 200 道开放式题目的 benchmark，覆盖过程系统工程的四个核心领域，并配一套多 judge 评测框架：每份答复由五个独立的 LLM judge 对照一份七要素评分细则打分。

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://doi.org/10.1016/j.ceja.2026.101375>
- **Code:** <https://github.com/sombsuk/PSE-Bench>
- **Venue:** Chemical Engineering Journal Advances, Volume 27 (2026), article 101375

## Summary

PSE-Bench 关注的是把大语言模型用作化工过程系统工程的咨询工具——在这类安全攸关的场合，措辞笃定却内容不全的答复是有风险的。benchmark 含 200 道开放式题目，平均分配到过程建模与仿真、过程优化、面向化工过程的机器学习，以及过程设计与系统工程四块。每份模型答复由五个独立 AI judge 组成的集成对照七要素细则打分，用意是抑制单一 judge 的系统性偏差，所得分数再对照人类专家的评判加以核验。五个商业 LLM 以零样本方式接受评测；公开的产物包括带标准答案与评分细则的题集、原始答复、各 judge 的评分明细，以及人类验证数据。

## Tasks

200 道开放式题目，每个领域 50 道，以 `ChemEng_Bench_200_GroundTruth.xlsx` 发布，附标准答案与逐题评分细则。四个领域及其列出的主题为：过程建模与仿真（MOD）——热力学建模、闪蒸计算、反应器建模、动态仿真；过程优化（OPT）——LP/NLP/MILP/MINLP、夹点分析、实时优化、多目标优化；面向化工过程的机器学习（ML）——软测量、故障检测、物理信息神经网络、迁移学习；过程设计与系统工程（DES）——HAZOP、LOPA、过程强化、全厂控制、FEED。题目单轮作答、不使用工具；据官方仓库记录，所有答复于 2026 年 2 月 23 日在零样本条件下采集。

## Domains

化学工程——整个题集通篇是过程系统工程：热力学与反应器建模、闪蒸计算、动态仿真、LP/NLP/MILP/MINLP 过程优化、夹点分析、实时优化、软测量与过程故障检测、HAZOP 与 LOPA 过程安全分析、过程强化、全厂控制以及前端工程设计。未指派共同领域：其中的机器学习子集是把 ML 用于化工过程，而非对机器学习研究本身的贡献。

## Evaluation

- 每份答复由五个独立的 AI judge 对照一份七要素评分细则打分。
- 综合分为 `Overall = 0.15 x ROUGE-1 + 0.15 x ROUGE-L + 0.20 x Cosine + 0.50 x Element%`，分档为 Good（>= 0.50）、Fair（0.35–0.49）与 Poor（< 0.35）。
- 人类专家验证与自动判分并行开展，结果以 `Human_Validation_Final.xlsx` 发布。
- 细则要素覆盖度按 0–7 分计，模型之间的差异用 Friedman 检验，报告为 χ²(4) = 491.4、p < 0.001 的显著结果。
- **报告。** 共评测五个模型：DeepSeek-V3（`deepseek-chat`）、Claude Sonnet 4（`claude-sonnet-4-20250514`）、Gemini 2.5 Flash（`gemini-2.5-flash`）、GPT-4o（`gpt-4o-2024-08-06`）与 Llama 3.3 70B（`llama-3.3-70b-versatile`，经 Groq）。要素覆盖度从 DeepSeek 的 78.1% 递减到 Llama 的 60.8%。各模型的领域难度排序一致，均为 DES > ML > OPT > MOD。三位领域专家重新评阅答案以验证 judge 集成：AI 与人类的一致性为 Spearman rs = 0.416（p < 0.001）、ICC = 0.793，且专家的重评暴露出 AI 在 0–7 分制上系统性偏松 +0.85 分。模型排名在其他计分方案下保持稳定（rs = 1.000），但论文指出，中段模型之间的次序不如整体分层稳固。

## Typical Duration

N/A — 单轮零样本问答，没有 agent 轨迹；benchmark 未报告逐题的 wall-clock 时间或 token 预算。

## Main Contribution

作者把 PSE-Bench 呈现为首个跨过程系统工程各领域评测大语言模型的 benchmark，并为其配上多 judge 评测框架——五 judge 集成意在削弱单个 AI 评判者的系统性偏差。论文给出的结论是：LLM 在程序性的 PSE 任务上能提供帮助，但在建模与优化上仍需专家把关。

## Key Design Ideas

- 四个 PSE 领域各保持 50 道题，使领域之间的分数差异不受样本量差异干扰。
- 采用开放式题目并公开标准答案与逐题评分细则，而非选择题。
- judge 集成：每份答复交由五个独立的 AI judge，而不是单个 LLM judge。
- 综合指标兼顾词面重合（ROUGE-1、ROUGE-L）、嵌入相似度与细则要素覆盖度，其中要素覆盖度占一半权重。
- 设人类专家验证层，用途是核查自动 judge 而非取代它们，并把由此得到的偏松幅度作为显式的校准常数报告出来，而不是含糊带过。
- 用非参数显著性检验（Friedman）加上对其他计分方案的敏感性分析，确认所报排名并非所选权重的产物。
- 题目、标准答案、原始模型答复、各 judge 评分、汇总统计与人类验证数据在 MIT 许可证下全部公开。

## Strengths

- 评测产物端到端公开——题集、标准答案、评分细则、原始答复、各 judge 评分与人类验证数据——所报数字可以重算，而不必全凭信任。
- judge 集成加上显式的人类一致性统计量，正面处理了单一 LLM judge 的可靠性问题，而不是绕开它。
- 模型排名的稳健性对照其他计分方案做了检验（rs = 1.000），把排名结论与具体的权重选择分离开。
- 领域覆盖触及真正的过程工程内容——HAZOP、LOPA、夹点分析、全厂控制、FEED——而非多数化学邻近 LLM benchmark 中占主导的化学知识。

## Limitations

- 单轮、零样本、无工具的问答：没有仿真器、没有代码执行、也没有多步轨迹，因此测的是咨询式知识，而非 agentic 的过程工程能力。
- 综合分把 30% 的权重给了对照参考答案的 ROUGE 重合度，这会奖励与标准答案措辞表层相似的答复。
- 报告的 AI 与人类一致性 rs = 0.416 属中等水平，限制了自动分数单独可承载的置信度；论文也说明，该 benchmark 区分整体性能层级比区分中段的个别模型更可靠。
- AI judge 在 0–7 分制上系统性偏松 +0.85 分，因此若不校正这一偏移，绝对分数会高估模型水平。
- Repository note: 200 道题分摊到四个领域，每个领域只有 50 题，因此按领域得出的结论依据的是小样本。
- Repository note: 官方仓库中的引用信息写的是另一份期刊并标注「Under review」，而正式发表的版本见于 Chemical Engineering Journal Advances 第 27 卷（2026 年）第 101375 号文章。

## Related Works

- [CeProBench](./ceprobench.md) — 本库中另一个化工过程工程 benchmark，但构建为可执行的多任务环境（知识图谱、PFD 解析、Aspen Plus 优化），而非开放式问答。
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — 同样为 LLM 的化学工程解题打分，但用的是人类专家评阅而非 AI judge 集成。
- [Autonomous Action Execution (AAE) Framework](./aae-framework.md) — 同样关注 LLM 在化工过程场景下的可靠性，但走的是对拟议控制动作做确定性校验的路子，而非答案判分。
