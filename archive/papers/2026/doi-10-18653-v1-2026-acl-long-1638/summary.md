<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SMART: Evaluating LLMs&apos; Mathematical Reasoning via a Human Cognitive Process-Inspired Benchmark

- **Authors**: Yujie Hou, Mei Wang, Yaoyao Zhong, Ting Zhang 0002, Xuetao Ma 0001, Hua Huang 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.1638>
- **DOI**: 10.18653/V1/2026.ACL-LONG.1638
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Decomposes mathematical problem-solving into four cognitive dimensions after Polya and tests each separately, finding wide capability gaps that final-answer accuracy hides.

## Problem

Strong benchmark performance leaves open whether it reflects genuine reasoning or superficial pattern recognition. Existing evaluation focuses either on the final answer or on intermediate steps, reducing mathematical reasoning to a shallow input-output mapping and overlooking that it is inherently multi-stage and multi-dimensional.

## Contributions

- SMART, a benchmark decomposing mathematical problem-solving into Semantic Understanding, Mathematical Reasoning, Arithmetic Computation and Reflection/Refinement
- Dimension-specific tasks that measure each cognitive process separately rather than through final answers
- Evaluation of 22 open- and closed-source LLMs revealing substantial cross-dimensional capability discrepancies
- The All-Pass Score, a metric requiring success across dimensions rather than on average

## Method

SMART, inspired by Polya's problem-solving theory, decomposes mathematical problem-solving into four cognitive dimensions — Semantic Understanding, Mathematical Reasoning, Arithmetic Computation, and Reflection/Refinement — and introduces dimension-specific tasks that measure each corresponding process separately. Measuring dimensions independently is what exposes compensation, where strength in one dimension masks weakness in another under a single aggregate score. A new All-Pass Score metric requires success across dimensions rather than on average.

## Results

Applied to 22 state-of-the-art open- and closed-source LLMs, SMART uncovers substantial discrepancies in capability across the four dimensions and reveals genuine weaknesses in current models, motivating the All-Pass Score.

## Limitations

No numbers in the abstract, so the size of the cross-dimensional discrepancies is unstated and the models are not listed. The four-dimensional decomposition follows a theory of human problem-solving, and whether those dimensions carve model computation at its joints is assumed rather than shown. Dimension-specific tasks may themselves be confounded — a semantic-understanding task still requires reading and producing an answer.

## Why it matters here

- **reasoning-evaluation**: A direct construct-validity contribution: it argues a single math accuracy number aggregates over dimensions that can compensate for one another, and the All-Pass Score is a concrete alternative that refuses to average them. That is the same structural criticism the archive already holds from VAR-MATH, which varies problem instances, but arrives from a different direction — decomposing the task rather than perturbing it — and the two are complementary. It joins three other papers in this drain arguing that reasoning benchmarks measure something other than reasoning, alongside long.826 on perception and findings-acl.460 on code.

## Entities

- **Concepts**: [construct validity](../../../../wiki/concepts/construct-validity.md), [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md), cognitive decomposition, [pattern recognition versus reasoning](../../../../wiki/concepts/pattern-recognition-versus-reasoning.md), aggregate score compensation, [self-correction](../../../../wiki/concepts/self-correction.md)
- **Methods**: SMART, All-Pass Score, dimension-specific evaluation, Polya problem-solving decomposition
- **Datasets**: SMART

Tags: `benchmark`, `construct validity`, `math reasoning`, `cognitive dimensions`, `metric design`

## Abstract

Large Language Models (LLMs) have achieved remarkable performance across a wide range of mathematical benchmarks. However, concerns remain as to whether these successes reflect genuine reasoning or superficial pattern recognition. Existing evaluation methods, which typically focus either on the final answer or on the intermediate reasoning steps, reduce mathematical reasoning to a shallow input–output mapping, overlooking its inherently multi-stage and multi-dimensional cognitive nature. Inspired by Pólya’s problem-solving theory, we propose SMART, a benchmark that decomposes mathematical problem-solving into four cognitive dimensions: S emantic Understanding, M athematical Reasoning, A rithmetic Computation, and R eflection & Refinemen t , and introduces dimension-specific tasks to measure the corresponding cognitive processes of LLMs. We apply SMART to 22 state-of-the-art open-and closed-source LLMs and uncover substantial discrepancies in their capabilities across dimensions. Our findings reveal genuine weaknesses in current models and motivate a new metric, the All-Pass Score, designed to better capture true problem-solving capability. Data is available at https://huggingface.co/datasets/ewdfd/SMART.

---

Record id: `doi:10.18653/v1/2026.acl-long.1638`
