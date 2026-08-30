# CODE2BENCH (2025)

> [English](../../works/code2bench.md) | **简体中文**

> **首次公开：** 2025-08-10 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2508.07180)

## Overview

CODE2BENCH 是动态 benchmark 构造框架。它从近期真实 code repository 中取材，为 Python 和 Java 生成任务，并要求测试达到 100% branch coverage 才能入库。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

N/A — 通用代码生成 benchmark 构造，未直接评估科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2508.07180>
- **Project:** <https://code2bench.github.io/>
- **Venue:** arXiv preprint (2025; revised 2026)

## Summary

CODE2BENCH 同时扩展两件事：从近期 repository 持续刷新任务来源，并用 property-based testing 提高测试严谨度。Scope graph 用于分类依赖，生成的测试必须覆盖全部 branch。CODE2BENCH-2509 含原生 Python 与 Java track，来源涉及 220 个 Python 和 189 个 Java repository，并测试了十个模型。

## Tasks

三个 track：self-contained Python、需要 repository API 的 weakly self-contained Python，以及 self-contained Java。每个实例来自近期 repository function，并配有 property-based tests；各 track 的准确数量见论文 dataset table。

## Domains

软件工程与代码生成。主要贡献是 benchmark construction，因此不加入 domain axis。

## Evaluation

使用达到 100% branch coverage gate 的 property-based tests 计算 Pass@1。Diagnostic fingerprint 区分编译、运行时、逻辑、依赖和 near-pass 失败；SC-Python 中有 6.94% 的提交能通过简单测试，却过不了高严谨度测试。

## Typical Duration

每题生成一次代码，以 Pass@1 评分；论文未给出统一墙钟预算。

## Main Contribution

一套可复现的构造 pipeline，把来源是否新鲜和 verifier 是否严谨作为两个独立的 benchmark validity 要求。

## Key Design Ideas

- 从近期 repository 取材，不依赖固定题库。
- 用 scope graph 区分自包含函数与带依赖函数。
- 生成 property-based tests，并要求完整 branch coverage。
- 发布 failure fingerprint，不只给 aggregate pass rate。

## Strengths

- 动态取材减少对陈旧静态题目的依赖。
- Coverage gate 把 test adequacy 变成明确准入条件。
- Python 与 Java 原生 track 能暴露语言生态差异。

## Limitations

- 近期来源只能降低 contamination 风险，不能证明训练数据中一定没有这些代码。
- Branch coverage 不保证测试在语义上完整。
- 任务是 function-level code generation，不是完整 agent workflow。

## Related Works

- [ResearchCodeBench](./researchcodebench.md)
- [FrontierCode](./frontiercode.md)
