<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning

- **Authors**: Zi-Ao Ma, Xian-Ling Mao, Tian Lan, Chen Xu, Zhijing Wu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.25/>
- **PDF**: <https://aclanthology.org/2026.acl-long.25.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.25
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

SGP-CoT identifies which reasoning units a model can safely drop using only its own intrinsic likelihood signals (counterfactual answer-impact and coherence-impact scores, no external verifier or curated data), then trains the model via preference optimization on self-pruned traces, cutting reasoning length 15-50% across five model families while preserving or improving accuracy -- and shows pruning by a different model consistently degrades accuracy more than self-pruning.

## Problem

Existing efficient-CoT methods (length-aware RL penalties, heuristic truncation, external verifiers or curated compressed data) act as semantically-blind compressors that cannot distinguish which reasoning segments are essential for a given model's own reasoning trajectory versus another model's, so externally-imposed brevity disrupts model-specific reasoning dependencies and degrades accuracy.

## Contributions

- a self-assessment mechanism formalizing CoT traces as sequences of reasoning units and scoring each unit's necessity via two intrinsic counterfactual likelihood signals (answer impact, coherence impact), requiring no external supervision, verifier, or curated data
- SGP-CoT, a fully self-guided pruning-and-preference-optimization framework that consistently preserves or improves accuracy while cutting reasoning length across five model families and four benchmarks
- direct empirical evidence (a pruner-student mismatch experiment and a perplexity probe) that redundancy is model-specific: a model's own pruning signal best preserves its reasoning coherence and downstream accuracy, while pruning by another model (even another LRM or a stronger model like GPT-5) causes measurable accuracy degradation
- ablations isolating the necessity of the coherence-impact buffering mechanism and the preference-optimization training objective, and showing a compact (1.5K-pair) preference dataset is sufficient and preferable to larger ones

## Method

Segments each sampled reasoning trace into semantically coherent 'reasoning units' using data-driven, frequent-first-token line boundaries. For each unit, computes two intrinsic, counterfactual likelihood-based impact scores by comparing the model's own generation likelihoods with and without that unit present: Answer Impact (change in the average log-likelihood of the correct final answer when the unit is removed -- positive means the unit is answer-critical) and Coherence Impact (change in the model's own predicted likelihood of the immediately following unit -- positive means the unit supports fluent local continuation). A conservative pruning strategy keeps any unit above an answer-impact threshold tau_A outright, temporarily buffers units below tau_A but above a coherence threshold tau_C (discarding the buffer only if no subsequent answer-critical unit follows, otherwise retaining the whole buffer), and prunes only units below both thresholds. The resulting pruned-but-correct trace forms a preference pair against the original longer correct trace (pruning-based pairs), combined with sampling-based pairs (a naturally shorter correct response preferred over a longer incorrect one), and the model is trained via DPO with an added SFT loss term to directly optimize for concise, focused reasoning.

## Results

Across five LRMs (DeepSeek-R1-Distill-Qwen-1.5B/7B, DeepSeek-R1-Distill-Llama-8B, OpenMath-Nemotron-1.5B/7B) and four benchmarks (AIME2024, GPQA-Diamond, MATH-500, GSM8K), SGP-CoT consistently maintains or slightly improves Pass@1 accuracy while reducing token count 20-50% on hard benchmarks and 15-30% on easy ones (e.g. GSM8K), and reduces end-to-end wall-clock latency by over 40% on the 1.5B/7B DeepSeek models -- latency reductions exceed raw token reductions, suggesting the method preferentially prunes extra-long, expensive-to-decode responses. Compared to LC-R1 and L1 (length/budget-penalty RL baselines), those methods achieve more aggressive compression but with accuracy drops (e.g. LC-R1 loses 6.4 points on AIME2024 for DS-Qwen-1.5B), while SGP-CoT's more moderate compression consistently preserves or improves accuracy, positioning it as complementary to (not a strict replacement for) aggressive-compression methods when reliability cannot be compromised. A perplexity-probe experiment shows the lowest relative perplexity increase after pruning consistently occurs along the diagonal (a model pruned by itself), confirming self-guided pruning best preserves a model's own reasoning coherence; training a student model (DS-Qwen-7B) with preference pairs constructed by external pruners causes accuracy drops of up to 8.3 points on AIME2024 versus self-pruning at comparable compression rates. Ablations show removing the coherence-guided buffering mechanism ('w/o Retention') preserves accuracy but drastically reduces compression (units are kept too liberally); pruning on answer impact alone ('w/o Delta_C') achieves more aggressive compression (40-53% on hard benchmarks) but causes accuracy drops up to 4 points on AIME2024; rate-matched random pruning at SGP-CoT's compression level causes accuracy drops up to 12 points, confirming the impact-score-guided selection (not just the compression rate) is what preserves accuracy. Increasing the preference-data scale from 1.5K to 10K-30K yields only marginal further compression while larger sets increasingly hurt hard-benchmark accuracy, so the paper adopts a compact 1.5K-pair training set as the default.

## Limitations

Impact-score thresholds (tau_A, tau_C) require some tuning, though the paper reports performance is stable across a broad central region and the framework does not require delicate threshold tuning in practice. Scaling preference-data volume beyond ~1.5K pairs increasingly hurts accuracy on hard benchmarks (most clearly AIME2024), so the method is deliberately kept in a small-data regime rather than scaled up, which the paper frames as a design choice for stability and practicality rather than as a limitation to be resolved. The paper does not report results at larger model scales (beyond ~8B) within the excerpted sections.

## Why it matters here

- **overthinking**: Central to the topic: directly challenges the 'redundancy is universal' assumption behind semantically-blind length-penalty or heuristic-truncation methods, arguing and empirically demonstrating that which reasoning steps are essential is model-specific -- the same trace pruned by a different model (even a stronger one) introduces measurable confusion and accuracy loss for the original model. This gives a concrete mechanism (counterfactual likelihood impact, computable with no external verifier) for the broader claim in this archive that current LRMs already 'know' which parts of their own reasoning matter, complementing other archive papers (e.g. attention-head-based or Valid-Thinking-rate approaches) that reach similar conclusions via different signals.

## Entities

- **Concepts**: reasoning unit (semantic segmentation), Answer Impact / Coherence Impact (counterfactual likelihood scores), self-guided vs. externally-imposed pruning, coherence-aware buffered retention
- **Methods**: SGP-CoT (Self-Guided Pruning + DPO), [LC-R1 (baseline)](../../../../wiki/methods/lc-r1-baseline.md), L1-Exact / L1-Max (baseline), [Direct Preference Optimization (DPO)](../../../../wiki/methods/direct-preference-optimization-dpo.md)
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MATH-500](../../../../wiki/datasets/math500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), Mixture-of-Thoughts (science questions, training)

Tags: `overthinking`, `efficient-reasoning`, `self-pruning`, `model-specific-redundancy`, `preference-optimization`

## Abstract

Chain-of-Thought (CoT) reasoning is crucial for the performance of Large Reasoning Models (LRMs) but is often hindered by redundant and distracting segments, which incur excessive inference costs and degrade robustness. Existing approaches try to solve this problem by enforcing brevity through external supervision, such as length-based penalties or heuristic truncation. However, these approaches often degrade performance because they disregard the model’s intrinsic reasoning dependency and thus fail to distinguish between essential and redundant CoT segments. To address this problem, we propose SGP-CoT, a novel Self-Guided Pruning framework that leverages the model’s intrinsic likelihood landscape to identify segments that are extraneous to its specific reasoning pattern. Specifically, SGP-CoT treats the reasoning trajectory as a sequence of semantic units and assesses the necessity of each one via internal likelihood signals, measuring its contribution to the answer and local coherence. Based on this, it selectively removes non-essential segments and then forms high-quality pruning-based preference pairs, enabling the model to learn focused reasoning via self-optimization. Extensive experiments across diverse benchmarks demonstrate that the proposed SGP-CoT significantly reduces output length while maintaining or improving accuracy. These results validate that LRMs intrinsically possess the capability to discern reasoning utility, positioning SGP-CoT as a robust pathway toward scalable inference.

---

Record id: `doi:10.18653/v1/2026.acl-long.25`
