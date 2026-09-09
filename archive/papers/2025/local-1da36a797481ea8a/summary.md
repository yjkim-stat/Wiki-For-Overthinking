<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mitigating Overthinking in Large Reasoning Models via Manifold Steering

- **Authors**: Yao Huang, Huanran Chen, Shouwei Ruan, Yichi Zhang, Xingxing Wei, Yinpeng Dong
- **Venue**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025)
- **Published**: 2025-01-01
- **Source**: local+virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119969>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

A training-free residual-stream steering method that mitigates overthinking by projecting a difference-in-means 'overthinking direction' onto a low-dimensional PCA manifold of the model's activations before ablating it, removing the accuracy-degrading interference noise that limits naive single-direction steering.

## Problem

Large reasoning models exhibit overthinking -- excessive validation loops and redundant deliberation that inflate inference cost -- and a naive single, difference-in-means steering direction that captures this tendency can be ablated to reduce it, but its effect quickly plateaus and even reverses as intervention strength increases, apparently corrupting the model's other abilities. The open problem is how to isolate a 'purer' overthinking direction that tolerates larger, more effective intervention strength without this degradation.

## Contributions

- Show overthinking can be captured by a single difference-in-means direction in residual-stream activations, extracted by contrasting 'redundant' (long, hesitation-keyword-heavy) versus 'concise' reasoning trajectories.
- Show that naive ablation along this raw direction plateaus and even reverses at higher intervention strength, and attribute this to an orthogonal interference component contaminating the direction.
- Prove theoretically (two theorems) that this interference component has a substantial expected norm and amplifies through the network's layers, disrupting unrelated model capabilities.
- Propose Manifold Steering: project the raw steering direction onto the top-k PCA subspace of the model's activations (a low-dimensional manifold capturing >70% of activation variance) before applying it, removing the interference component.
- Demonstrate up to 71% token reduction while preserving or improving accuracy on GSM8K/MATH500/AMC2023/AIME2024, with cross-domain transfer to LiveCodeBench and GPQA-Diamond without re-deriving the direction.

## Method

Locus: the residual stream at a single selected layer per model (layer 27 for the 1.5B and 7B models, layer 31 for the 8B model, layer 47 for the 14B model), applied to every token position at that layer during decoding. Quantity: a raw difference-in-means direction r = mean(h(x)) over a 'redundant' set minus mean(h(x)) over a 'concise' set, where the two sets are built from 5 sampled responses per question on OpenMathInstruct-2 (redundant: all 5 responses exceed 16k tokens and contain more than 20 hesitation-keyword occurrences such as 'wait'/'alternatively'; concise: all 5 responses are under 1k tokens with none of those keywords; 500 filtered examples retained per set). This raw direction is decomposed into an 'overthinking' component and an orthogonal 'interference' component that the paper shows (via PCA on pooled activations, with the top-10 principal components explaining over 70% of variance) lies largely outside a low-dimensional activation manifold. Manifold Steering projects the raw direction onto that top-k PCA subspace before unit-normalizing it, then ablates the projected component from every activation: h' = h - alpha * r_overthinking * (r_overthinking)^T * h. Fires at every decoding step, at every token position, for the whole generated sequence -- a fixed, content-blind linear intervention (same mechanism as classic activation-steering methods), not conditioned on the current token's content beyond the linear-algebra projection itself. Cost: fully training-free; requires a one-time offline computation of the direction and its low-dimensional manifold from ~20k sampled math questions with 5 rollouts each (500 net samples after IsolationForest outlier filtering) and a PCA decomposition -- no gradient-based optimization or backprop through the model is needed. At inference the paper reports negligible added latency: on DeepSeek-R1-Distill-Qwen-7B/Math500, their method takes 1.05s versus 1.74s for the unsteered original, 39.89s for the Dynasor baseline (external monitoring), and 1.37s for the SEAL baseline (Table 6, Appendix E) -- the method is actually faster than the unsteered baseline because it produces much shorter outputs.

## Results

Table 1: across GSM8K, MATH500, AMC2023 and AIME2024 and four DeepSeek-R1-distilled models (1.5B/7B/8B/14B), Manifold Steering achieves 41%-71% token reduction while maintaining or improving Pass@1, outperforming the Dynasor and SEAL baselines at matched or better accuracy (e.g. R1-7B on GSM8K: vanilla 87.5% Pass@1 / 2735 tokens vs. steered 86.0% / 1143 tokens, a 60% token reduction; R1-14B on AIME2024: vanilla 66.7% / 9986 tokens vs. steered 63.3% / 8132 tokens, a 19% reduction). Token reduction is consistently larger on simpler datasets (GSM8K/MATH500, ~40%) than on harder ones (AMC2023/AIME2024, ~20%), which the paper attributes to complex problems requiring larger genuine token budgets. Cross-domain transfer (direction extracted only from math data) achieves 12%-27% token reduction on LiveCodeBench (code generation) and GPQA-Diamond (disciplinary knowledge) while preserving accuracy (Fig. 3). A cross-task transferability check applies the same projection method to a refusal direction in Qwen2.5-7B-Instruct and achieves a 100% jailbreak success rate on AdvBench versus 74% for a prior single-direction baseline, evidencing generality of the manifold-projection technique beyond overthinking. Latency comparison (Table 6, Appendix E) on R1-7B/Math500: Ours 1.05s vs. Original 1.74s, Dynasor 39.89s, SEAL 1.37s -- the method is faster than the unsteered baseline because of the shorter outputs it produces.

## Limitations

Stated (Sec. 6, Discussion and Limitations): applicability to multi-modal LLMs remains unexplored; interaction with highly specialized tasks such as legal or medical domain-specific reasoning warrants further investigation; the method's sensitivity to intervention strength suggests a need for future work on dynamic steering strategies whose strength adapts to task complexity in real time (i.e. the strength alpha is currently a fixed, hand-tuned per-model hyperparameter, not adaptive). Unstated: the 'redundant' vs 'concise' contrastive dataset used to derive the direction is built from a length-plus-lexical-keyword heuristic (>16k tokens and >20 hesitation-keyword occurrences like 'wait'/'alternatively' vs. <1k tokens and zero such keywords); this operationalizes overthinking as verbosity plus a fixed lexical marker, which risks conflating genuinely necessary long solutions to harder problems with truly redundant deliberation, and the steering direction inherits any bias in that heuristic. The paper also demonstrates (Sec. 5.5) that the same manifold-projection trick, applied to a refusal direction instead of an overthinking direction, raises jailbreak success rate on AdvBench from 74% to 100% versus the prior single-direction baseline — a dual-use finding for a purification technique that the paper reports without extended safety discussion beyond a general call for more safety research.

## Why it matters here

- **overthinking**: Directly targets overthinking mitigation via inference-time residual-stream steering and is a central method for this survey: it shows that naive additive/ablative steering vectors plateau and can backfire at higher strength, motivating a manifold-projection fix that allows larger, safer intervention; it also demonstrates cross-domain transfer of a steering direction derived only from math data, bearing directly on the survey's question of where and how much to intervene mid-generation.

## Entities

- **Concepts**: steering direction, interference noise, low-dimensional activation manifold, difference-in-means, residual stream, [mechanistic interpretability](../../../../wiki/concepts/mechanistic-interpretability.md)
- **Methods**: [Manifold Steering](../../../../wiki/methods/manifold-steering.md), [difference-in-means direction extraction](../../../../wiki/methods/difference-in-means-direction-extraction.md), PCA-based low-dimensional manifold projection, activation ablation/steering, [Dynasor (baseline)](../../../../wiki/methods/dynasor-baseline.md), [SEAL (baseline)](../../../../wiki/methods/seal-baseline.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AMC2023](../../../../wiki/datasets/amc23.md), [AIME2024](../../../../wiki/datasets/aime-2024.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), OpenMathInstruct-2, [AdvBench](../../../../wiki/datasets/advbench.md)

Tags: `activation-steering`, `overthinking`, `manifold-projection`, `mechanistic-interpretability`, `difference-in-means`, `deepseek-r1`, `token-reduction`

## Abstract

Abstract Recent advances in Large Reasoning Models (LRMs) have demonstrated remarkable capabilities in solving complex tasks such as mathematics and coding. However, these models frequently exhibit a phenomenon known as overthinking during inference, characterized by excessive validation loops and redundant deliberation, leading to substantial computational overheads. In this paper, we aim to mitigate overthinking by investigating the underlying mechanisms from the perspective of mechanistic interpretability. We first showcase that the tendency of overthinking can be effectively captured by a single direction in the model's activation space and the issue can be eased by intervening the activations along this direction. However, this efficacy soon reaches a plateau and even deteriorates as the intervention strength increases. We therefore systematically explore the activation space and find that the overthinking phenomenon is actually tied to a low-dimensional manifold, which indicates that the limited effect stems from the noises introduced by the high-dimensional steering direction. Based on this insight, we propose Manifold Steering , a novel approach that elegantly projects the steering direction onto the low-dimensional activation manifold given the theoretical approximation of the interference noise. Extensive experiments on DeepSeek-R1 distilled models validate that our method reduces output tokens by up to 71\% while maintaining and even improving the accuracy on several mathematical benchmarks. Our method also exhibits robust cross-domain transferability, delivering consistent token reduction performance in code generation and knowledge-based QA tasks. Code is available at: https://github.com/Aries-iai/Manifold_Steering.

---

Record id: `local:1da36a797481ea8a`
