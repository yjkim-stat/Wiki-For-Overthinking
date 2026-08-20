<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning

- **Authors**: Zhuohan Xie, Daniil Orel, Rushil Thareja, Dhruv Sahnan, Hachem Madmoun, Fan Zhang 0019, Debopriyo Banerjee, Georgi Nenkov Georgiev, Xueqing Peng, Lingfei Qian, Jimin Huang, Jinyan Su, Aaryamonvikram Singh, Rui Xing 0002, Rania Elbadry, Chen Xu, Haonan Li 0002, Fajri Koto, Ivan Koychev, Tanmoy Chakraborty 0002, Yuxia Wang 0003, Salem Lahlou, Veselin Stoyanov, Sophia Ananiadou, Preslav Nakov
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.662>
- **DOI**: 10.18653/V1/2026.ACL-LONG.662
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## In one line

A financial reasoning benchmark built from parameterized symbolic templates with executable Python, giving machine-verifiable step-level ground truth and contamination-free regeneration.

## Problem

Multi-step symbolic reasoning matters for financial analysis, and existing benchmarks such as FinQA and ConvFinQA emphasize final numerical answers while neglecting the intermediate steps needed for transparency and verification.

## Contributions

- FinChain, the first benchmark for verifiable chain-of-thought evaluation in finance, spanning 58 topics across 12 domains
- Parameterized symbolic templates with executable Python enabling machine-verifiable reasoning and contamination-free scalable generation
- ChainEval, a dynamic alignment measure combining final-answer correctness with step-level reasoning consistency
- Evaluation of 26 leading LLMs, with domain-adapted and math-enhanced models narrowing the gap

## Method

FinChain spans 58 topics across 12 financial domains, each represented by parameterized symbolic templates with executable Python code. Because each instance is generated from a template with executable ground truth, reasoning is fully machine-verifiable and new contamination-free instances can be generated at will — this is what removes both the human-annotation cost and the contamination exposure that fixed benchmarks carry. ChainEval is a dynamic alignment measure scoring final-answer correctness jointly with step-level reasoning consistency.

## Results

Evaluation of 26 leading LLMs shows even frontier models have clear limitations in symbolic financial reasoning, while domain-adapted and math-enhanced fine-tuned models substantially narrow the gap.

## Limitations

No numbers in the abstract and the 26 models are not listed. Template-generated problems are verifiable but constrained to what templates express, so difficulty and diversity are bounded by template design rather than by real financial analysis. The finding that math-enhanced fine-tuning narrows the gap suggests the benchmark measures symbolic manipulation substantially, which may be the intent but limits claims about financial reasoning specifically.

## Why it matters here

- **reasoning-training**: Its construction answers a constraint the archive keeps running into: step-level supervision needs step-level ground truth, and expert annotation is what makes that expensive — findings-acl.28 in this drain could afford it for only 46% of items. Executable symbolic templates produce it for free and regenerate contamination-free instances on demand, which makes FinChain a source of verifiable process supervision rather than only an evaluation. That is directly usable by the process-supervision methods this topic tracks, and it is the same trick the archive's code-reasoning entry (findings-acl.460) gets from the interpreter.
- **test-time-scaling**: Machine-verifiable step-level ground truth makes this a clean testbed for verifier-based test-time methods, since the oracle verifier is available and the gap between a learned verifier and the oracle can be measured directly rather than assumed.

## Entities

- **Concepts**: symbolic reasoning, process evaluation, [benchmark contamination](../../../../wiki/concepts/benchmark-contamination.md), [verification](../../../../wiki/concepts/verification.md), step-level consistency, template generation, [construct validity](../../../../wiki/concepts/construct-validity.md)
- **Methods**: FinChain, ChainEval, parameterized template generation, executable verification
- **Datasets**: FinChain, [FinQA](../../../../wiki/datasets/finqa.md), ConvFinQA

Tags: `benchmark`, `financial reasoning`, `symbolic`, `verifiable`, `contamination-free`

## Abstract

Multi-step symbolic reasoning is essential for robust financial analysis; yet, current benchmarks largely overlook this capability. Existing datasets such as FinQA and ConvFinQA emphasize final numerical answers while neglecting the intermediate reasoning steps required for transparency and verification. To address this gap, we introduce FinChain, the first benchmark specifically designed for verifiable Chain-of-Thought evaluation in finance. FinChain spans 58 topics across 12 financial domains, each represented by parameterized symbolic templates with executable Python code that enable fully machine-verifiable reasoning and scalable, contamination-free data generation.To assess reasoning capacity, we propose ChainEval, a dynamic alignment measure that jointly evaluates both the final-answer correctness and the step-level reasoning consistency. Our evaluation of 26 leading LLMs reveals that even frontier LLMs exhibit clear limitations in symbolic financial reasoning, while domain-adapted and math-enhanced fine-tuned models can substantially narrow this gap.Overall, FinChain exposes persistent weaknesses in multi-step financial reasoning and provides a foundation for developing trustworthy, interpretable, and verifiable financial AI. This project is available at https://github.com/mbzuai-nlp/finchain.git.

---

Record id: `doi:10.18653/v1/2026.acl-long.662`
