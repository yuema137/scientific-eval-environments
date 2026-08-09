# LLM4Mat-Bench (2024)

> [English](../../works/llm4mat-bench.md) | **简体中文**

## Overview

LLM4Mat-Bench 评测大语言模型的材料性质预测：约 190 万个晶体结构，取自 10 个数据源、含 45 种性质，以三种文本模态（成分、CIF、晶体文本描述）编码，同时评测生成式对话 LLM 与微调语言模型——结论是任务专用模型仍胜过生成式 LLM。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.00177>
- **Code:** <https://github.com/vertaix/LLM4Mat-Bench>
- **Venue:** NeurIPS 2024 AI4Mat Workshop

## Summary

LLM4Mat-Bench 追问语言模型从晶体的文本编码预测材料性质有多准。它汇集约 190 万个结构，横跨 10 个公开源与 45 种性质，三种输入模态——成分、CIF、晶体文本描述（分别为 4.7M、615.5M、3.1B token）。对比两类模型：零样本与少样本提示的生成式对话 LLM（Llama、Gemma、Mistral），以及对照 CGCNN 基线的微调语言模型（LLM-Prop、MatBERT）。头条对生成式一侧不太乐观——对话 LLM 在分类上近乎随机，而任务专用的微调模型占据主导。

## Tasks

从文本编码的晶体做性质预测：45 种性质的回归与分类（稳定性、带隙是否直接），覆盖约 190 万个结构、三种模态；静态预测，非交互。

## Domains

材料科学——从成分、CIF 与文本描述做晶体性质预测。

## Evaluation

- 回归以 MAD:MAE 比值（越高越好）；分类以 AUC。
- **报告。** 微调的 LLM-Prop 与 MatBERT 领先；生成式对话 LLM 在分类上近乎随机（AUC ≈ 0.5）；任务专用模型占主导。

## Typical Duration

单次预测查询；无交互式设定。

## Main Contribution

对「语言模型在材料性质预测上处于什么位置」的大规模、多模态测量——记录了对生成式 LLM 的提示尚不能与微调的任务专用模型相抗衡。

## Key Design Ideas

- 三种文本模态（成分/CIF/描述）分离出模型能利用哪种编码。
- MAD:MAE 比值使不同量级性质的回归质量可比。
- 把生成式 LLM 与微调基线配对，诚实地框定当前能力差距。

## Strengths

- 规模（190 万结构、45 种性质、10 个源）与模态广度集于一套。
- 生成式与微调的对比对决策直接有用。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、Comments 与官方仓库编写（2026 年 8 月）；该 benchmark 同时评测生成式对话 LLM 与微调编码模型（LLM-Prop/MatBERT），此处因前者而收录。仓库排行榜之外的各模型结果表有待全文校验。

## Related Works

- [MatText](./mattext.md) — 同样是从晶体文本做 LLM 材料性质预测，分析 LLM 与 GNN 的差距。
- [MaScQA](./mascqa.md) — 同样是 LLM 材料评估，考知识问答而非性质回归。
- [MatTools](./mattools.md) — 同样是 LLM 面向材料计算，走工具使用而非直接预测。
