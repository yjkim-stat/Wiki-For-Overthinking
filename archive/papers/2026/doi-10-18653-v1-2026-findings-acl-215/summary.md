<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization

- **Authors**: Xingjian Diao, Zheyuan Liu 0010, Chunhui Zhang, Weiyi Wu, Keyi Kong, Lin Shi, Kaize Ding, Soroush Vosoughi, Jiang Gui
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.215>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.215
- **Topics**: test-time-scaling, reasoning-training
- **Relevance score**: test-time-scaling 0.50

## In one line

Routes each generation step among a fast path, a perception re-examination path and a self-reflection path, trained on 790k samples of teacher-attributed perception-versus-reasoning failures.

## Problem

Vision-language models overthink, producing verbose responses even for simple queries, costing efficiency and sometimes accuracy. Prior adaptive-reasoning fixes overlook a more basic bottleneck: visual perception failures. The paper argues stable reasoning depends on low-level visual grounding, so reasoning errors often originate in imperfect perception rather than insufficient deliberation — in which case more deliberation cannot help.

## Contributions

- The argument that overthinking work overlooks visual perception failure as the underlying bottleneck
- GPRO, a meta-reasoning controller routing each step among fast, slow-perception and slow-reasoning paths
- Large-scale failure attribution supervision from approximately 790k samples separating perceptual hallucination from reasoning error
- Multi-objective RL training of the controller for accuracy against computational cost under uncertainty
- Improvements in both accuracy and efficiency over recent slow-thinking methods with shorter responses

## Method

Gated Perception-Reasoning Optimization is a meta-reasoning controller that dynamically routes computation at each generation step among three paths: a lightweight fast path, a slow perception path that re-examines visual input, and a slow reasoning path for internal self-reflection. To teach the distinction, large-scale failure attribution supervision is derived from approximately 790k samples, using teacher models to separate perceptual hallucinations from reasoning errors — that attribution is what makes a three-way routing decision learnable rather than a heuristic. The controller is trained with multi-objective RL trading task accuracy against computational cost under uncertainty.

## Results

On five benchmarks, GPRO improves both accuracy and efficiency, outperforming recent slow-thinking methods while generating significantly shorter responses. No numbers are given in the abstract.

## Limitations

No quantitative results, benchmark names or models in the abstract. Failure attribution comes from teacher models, so the supervision inherits the teachers' own confusion between perception and reasoning errors — the labels are estimates of a distinction that is itself contested. 790k samples is a heavy data requirement. Whether re-examining the image actually repairs perception, as opposed to giving another sample of the same process, is not established.

## Why it matters here

- **test-time-scaling**: Adds a dimension the archive's compute-allocation work does not have: what kind of extra computation to spend, not just how much. Every allocation method tracked here chooses between thinking more and thinking less; this one can also choose to look again, on the argument that deliberation cannot repair a perception error. That argument is independently supported in this drain by doi:10.18653/v1/2026.acl-long.826, which attributes roughly 80% of ARC-style failures to perception, and by acl-long.2198, where removing the image improves performance. Three papers converging on perception as the misattributed bottleneck makes the routing design more credible than its unreported numbers would suggest.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [perception bottleneck](../../../../wiki/concepts/perception-bottleneck.md), [adaptive compute allocation](../../../../wiki/concepts/adaptive-compute-allocation.md), meta-reasoning, failure attribution, [test-time compute](../../../../wiki/concepts/test-time-compute.md), [self-correction](../../../../wiki/concepts/self-correction.md), [routing](../../../../wiki/concepts/routing.md)
- **Methods**: GPRO, multi-objective reinforcement learning, teacher-based failure attribution, step-level routing
- **Datasets**: _none recorded_

Tags: `overthinking`, `perception`, `routing`, `multi-objective rl`, `vision-language models`

## Abstract

Large Vision-Language Models (LVLMs) have exhibited strong reasoning capabilities through chain-of-thought mechanisms that generate step-by-step rationales. However, such slow-thinking approaches often lead to overthinking, where models produce excessively verbose responses even for simple queries, resulting in test-time inefficiency and even degraded accuracy. Prior work has attempted to mitigate this issue via adaptive reasoning strategies, but these methods largely overlook a fundamental bottleneck: visual perception failures. We argue that stable reasoning critically depends on low-level visual grounding, and that reasoning errors often originate from imperfect perception rather than insufficient deliberation. To address this limitation, we propose Gated Perception-Reasoning Optimization (GPRO), a meta-reasoning controller that dynamically routes computation among three decision paths at each generation step: a lightweight fast path, a slow perception path for re-examining visual inputs, and a slow reasoning path for internal self-reflection. To learn this distinction, we derive large-scale failure attribution supervision from approximately 790k samples, using teacher models to distinguish perceptual hallucinations from reasoning errors. We then train the controller with multi-objective reinforcement learning to optimize the trade-off between task accuracy and computational cost under uncertainty. Experiments on five benchmarks demonstrate that GPRO substantially improves both accuracy and efficiency, outperforming recent slow-thinking methods while generating significantly shorter responses.

---

Record id: `doi:10.18653/v1/2026.findings-acl.215`
