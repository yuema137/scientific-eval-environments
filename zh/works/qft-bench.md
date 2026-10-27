# QFT-Bench (2026)

> [English](../../works/qft-bench.md) | **简体中文**

> **首次公开：** 2026-10-23 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.33134)

## Overview

QFT-Bench 检查语言模型能否完成以单个闭式量为终点的长篇量子场论（QFT）推导。判断对错时先做符号检查；只有符号检查无法判定时，才交给 LLM judge。另有一个 judge 检查：答案对了的回答，展示出来的推导是否真的支撑这个答案。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **论文：** [LLMs Can Tackle High Energy Theoretical Physics, yet Gaps Remain: Part I, Quantum Field Theory](https://arxiv.org/abs/2610.33134)，2026 年预印本。
- **全文：** <https://arxiv.org/html/2610.33134v1>
- **项目主页：** <https://qft-bench.github.io/>
- **数据集：** <https://huggingface.co/datasets/LLMsHEP/QFT-Bench>
- **代码：** <https://github.com/qft-bench/qft-bench>
- **Venue:** arXiv 预印本（hep-ph、cs.CL，2026）

## Summary

作者参考教材和讲义选定主题，再自己编写新题，或改写已有题目，让答案不容易直接查到。用 Sonnet-5 预跑后，作者发现部分题目缺少假设、符号没有定义或约定没有说明，随后在题面中补齐。题面固定了约定和目标量，很多答案因此可以直接由 SymPy 判定。在 39 个模型中，有 12 个准确率超过 95%。忠实度检查则发现，有些回答答案正确，但展示出来的推导并不能推出这个答案。

## Tasks

共 75 道题，作者定位为研究生高难度到研究入门水平，分属八个方向：经典场论（7）、标量场、旋量场与矢量场的量子化（8）、QED（7）、正规化与重整化（6）、非阿贝尔规范理论与 QCD（6）、电弱理论与 Higgs 机制（8）、超对称场论（18）、共形场论（15）。每道题都有闭式参考答案和逐步参考解答。举个例子：一道题要求求出某个 Wess–Zumino 模型的全部经典超对称真空。Sonnet-5 求出的值是对的，但没有放进 box 里，所以被判错。

## Domains

物理，具体是通过 QFT 考察高能理论物理。作者把这项工作称为高能理论物理系列评测的第一部分（Part I）。

## Evaluation

- 最终答案从 `\boxed{}` 中读取。SymPy 评分器先检查它与参考答案是否符号等价。如果检查失败或无法判定，比如因为约定或规范选择不同，就由 Claude Opus-5 对照参考答案和参考解答，给出对或错。没有 box 的回答一律判错。
- 主要指标是 75 道题上的平均准确率。表 4 还单独给出每个模型的符号验证分数，在 33.3% 到 85.3% 之间。
- 39 个模型中，GPT-6.1-Sol 达到 100.0%，最低分为 41.3%。
- 一个 Opus-5 judge 给每份答错的回答标注一个原因：概念错误、计算错误、强先验错误或未遵循指令。三次评估取平均后，得分较低的一半模型中，概念错误占失败的 47.2%；得分前一半模型中占 23.4%，未遵循指令则占 31.5%。
- 一个按 rubric 打分的 Opus-5 judge 把每份回答标为推导不足、忠实或不忠实。不忠实率为 `U_m / C_m`，即答对的回答中被标为不忠实的比例。39 个模型三次运行的平均值为 7.2%；Llama 系列约为 20–40%。
- 三位 QFT 专家审阅了来自 15 个模型的 60 份回答。在正确性上，Opus-5 与专家的一致率为 98%，GPT-5.6 为 92%；在忠实度上分别为 73% 和 67%。

## Typical Duration

生成时 `max_tokens` = 65,536，模型支持时开启 thinking；表 4 的图注把这一设置写作 64k。忠实度 judge 和错误类型 judge 的 token 上限为 32k；论文没有写明正确性 judge 的上限。论文没有报告实际运行时长。

## Main Contribution

一套专门针对 QFT 的推导基准：优先用符号检查判分，并单独衡量正确答案是否得到其展示推导的支撑。

## Key Design Ideas

- 在题面中写明约定和目标量，让大多数等价判断可以用符号方式完成。
- 只有符号检查无法判定的答案才交给 LLM judge。
- 正确性和忠实度分开打分，两个 judge 都与人类专家做了对比。

## Strengths

- 覆盖八个 QFT 方向，其中超对称 18 题、共形场论 15 题。
- 表 4 把每个模型的符号验证分数和最终准确率并列给出。
- 正确性 judge 和忠实度 judge 都报告了与人类专家的一致率。

## Limitations

- 在 60 份回答上，忠实度标签与专家的一致率只有 73%（Opus-5）和 67%（GPT-5.6）。错误类型同样由 judge 标注。
- 答案正确但没有放进 box 也判错；在得分前一半的模型中，未遵循指令是占比最大的失败类型。
- 每道题只有一个二值分数；作者把 accuracy@k 留给后续工作。
- 部分题目改编自已有课程材料，范围也只限于 QFT。
- Repository note：公开数据集包含参考答案和参考解答，后来的模型可能在训练中见到它们。
- Repository note：已有 12 个模型超过 95%，准确率已经很难区分最强的几个模型。

## Related Works

- [TPBench](./tpbench.md) — 评测高能理论与宇宙学中的理论物理问题。
- [CritPt](./critpt.md) — 使用未发表的研究级物理挑战题。
- [PHYSICS](./physics-benchmark.md) — 用自动评分评测大学物理问题。
