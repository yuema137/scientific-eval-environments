# Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes (2026)

> [English](../../works/frontier-llm-based-agents-can-overcome-the-ontolog.md) | **简体中文**

> **首次公开：** 2026-05-27 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.28965)

## Overview

一项在既有生物策展金标准上做的受控再评估：五个前沿 LLM 各自作为一名「agentic 策展员」在自足的工作区中运行，产出 Entity-Quality 表型标注，并对照与 2018 年原研究相同的金标准、相同的三位受训人类策展员以及相同的 NLP 基线打分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.28965>
- **Code:** <https://github.com/phenoscape/goldstandard>

## Summary

表型标注——把自由文本的表型描述连到本体条目上——是让比较形态学数据得以跨研究整合的那一步，而它长期依赖专家，因此无法规模化。Dahdul et al. (2018) 在七项系统发育研究上构建了一套 Entity-Quality（EQ）标注金标准，并用它比较三位人类策展员与 Semantic CharaParser 这一 NLP 工具，发现机器–人类的一致性远低于人类–人类的一致性。本文用来自 Anthropic 与 OpenAI 的五个前沿托管 LLM 重做这一 benchmark。每个模型都拿到一个自足的工作区，内含源出版物 PDF、人类策展员当年用的同一份标注指南、四个项目本体以及一个校验脚本，评估沿用原研究的语义相似度指标。

## Tasks

评估沿用 Dahdul et al. (2018) 的金标准：从七项脊椎动物形态学的系统发育研究中采样的 203 个性状（463 个性状状态）。为避免工作区调优带来的泄漏，打分只取第 51–203 号性状，共 344 个性状状态。每道任务要求 agent 阅读源出版物，为这些性状状态给出 EQ 标注，标注须锚定在四个 OBO 格式的本体上（UBERON、PATO、BSPO、GO），工作区中另备有一个校验脚本。

## Domains

生物学。具体为比较脊椎动物形态学与进化生物学，标注最终汇入用于跨研究数据整合的表型知识库。论文未主张任何共存领域。

## Evaluation

沿用原研究的四个基于本体的语义相似度指标：SimJ（祖先集合的 Jaccard 相似度）、NIC（共同祖先的归一化信息量）、partial precision（惩罚多余标注）与 partial recall（惩罚遗漏标注）。agent 对照金标准打分，并同时与三位受训生物策展员以及 Semantic CharaParser 比较。受评的五个模型为 Anthropic 的 Opus 4.6、Opus 4.7 与 Sonnet 4.6，以及 OpenAI 的 GPT-5.4 与 GPT-5.4-mini。每个 agent 都落在三位人类策展员彼此之间的变异范围之内；表现最好的几个 agent 明显超过其中两位策展员，但未达到最好的那位人类策展员（WD）；所有 agent 在四项指标上都大幅胜过 Semantic CharaParser，其中 Claude Opus 系列在 SimJ 上约为其两倍。

## Typical Duration

未报告回合、步数或 wall-clock 上限。成本按每个已标注性状报告：Opus 4.6 约 $0.26，Opus 4.7 约 $0.43。

## Main Contribution

在一个未经改动的既有金标准上、用未经改动的指标给出证据：在基于本体的表型策展上，2018 年那项研究记录下的人机差距，前沿 LLM agent 已经补平。这就把策展瓶颈重新框定为一个可解的问题，而不是天然只能依赖专家。

## Key Design Ideas

- 原封不动地复用一个八年前发表的 benchmark 及其指标与人类策展员分数，比较对象因此是一个固定的既有参照点，而不是作者自选的新基线。
- 给 agent 的东西与当年给人类策展员的完全一致——源 PDF、同一份标注指南、项目本体——而不是一个已经预处理好的抽取任务。
- 工作区内的校验脚本让 agent 在提交前先按本体结构自查输出，整套设置因而是 agentic 的，而非单次预测。
- 第 1–50 号性状不计分，因为它们用于打磨工作区，报告的评估因而不掺调优成分。
- 以人类策展员之间的变异作为参照带，于是所问的问题成了「agent 是否落在受训策展员的区间内」，而不是「agent 能否打赢某一个分数」。

## Strengths

- 比较的参照点是固定的既有基准——一个八年前发表的 benchmark，其指标与人类策展员分数都原样沿用——而不是作者自行挑选的基线。
- 以人类策展员间变异作为参照带，使报告的结论（「落在受训策展员的区间内」）具备单一数字比较所没有的可解释性。
- agent 拿到的与人类策展员当年拿到的完全一致：源 PDF、同一份标注指南与项目本体，而非预处理过的抽取任务。
- 第 1–50 号性状不计分，因为它们用于打磨工作区，报告的评估因而不掺调优成分。
- 四个本体感知指标（SimJ、NIC、partial precision、partial recall）按本体结构给部分分，正契合这样一类任务：差之毫厘的标注并不等同于错。

## Limitations

- 该金标准自 2018 年起即公开可得，有可能出现在模型训练数据中；作者明确承认这一污染风险。
- 本地开放权重模型没能完成该任务，因此结论只适用于前沿托管模型。
- 范围限于脊椎动物形态学；能否扩展到其他类群，取决于是否存在足够丰富的解剖学本体。
- 五个模型、七项研究中的 344 个性状状态，评估规模偏小，且论文是一份七页的报告，而非完整发布的 benchmark。
- Repository note: 该工作的贡献是在既有数据集上做的评估研究，而不是新发布的 benchmark 工件——可复用的对象是 agentic 策展员的工作区，以及所链接仓库中的打分流水线。

## Related Works

- [FlyAOC](./flyaoc.md) — 受评任务相同，即面向科学知识库的 agentic 本体策展，但以果蝇遗传学中专门构建的 benchmark 形式发布。
- [BioKGBench](./biokgbench.md) — 生物医学知识图谱上的 agent 任务，打分对象是在既有 KG 中检出错误，而非对照专家策展员做标注。
- [LAB-Bench](./lab-bench.md) — 带人类专家基线的生物学研究能力套件，采用选择题形式而非开放式的本体锚定。
- [CeProBench](./ceprobench.md) — 同样以专家撰写的结构化标注为抽取任务的标准答案，落在化工过程开发领域。
