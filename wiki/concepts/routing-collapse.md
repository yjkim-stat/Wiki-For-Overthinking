# routing collapse

<!-- auto:begin -->

Routing collapse is the failure of a learned router to spread work across the experts or modes it selects from: instead of specialising, it sends the overwhelming majority of inputs to one of them, so added capacity buys nothing. The archive's two sources use the term at different levels and only one measures it. In the operator-level mixture-of-experts state-space study it is measured directly -- with K = 4 experts and explicit regime boundaries between chaotic, oscillatory and noise segments, the router routes nearly all timesteps to a single expert, this survives annealing the supervised warmup signal to zero, and only transient deviations appear at regime transitions; the consequence is that K = 4 and K = 8 have higher error and higher seed variance than a single expert. The adaptive-reasoning source instead avoids a router altogether, learning a mode token end-to-end inside GRPO, so it treats routing collapse as a hazard of the design rather than something it measures.

- **Kind**: concept
- **Also called**: Routing Collapse, expert collapse, representation collapse
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [adaptive reasoning](adaptive-reasoning.md), [adaptive test-time compute allocation](../methods/adaptive-test-time-compute-allocation.md), [AdaptThink](../methods/adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AutoThink](../methods/autothink.md), [DAPO](../methods/dapo.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Dr. GRPO](../methods/dr-grpo.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [Inverse Scaling](inverse-scaling.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [minervamath](../datasets/minervamath.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning hallucination](reasoning-hallucination.md), [RLVR](../methods/rlvr.md), [Thinkless](../methods/thinkless.md)

## Appears in

- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models](../../archive/papers/2026/arxiv-2608-21840/summary.md) — A controlled synthetic study finding that mixing stable spectral state-space operators through a learned router fails to beat a single-expert baseline on regime-switching time series, with more experts making it worse, routing collapsing to one expert, and apparent MSE gains on chaotic data coming from variance suppression that destroys the attractor.
- [RFS-Guard: Detecting Reasoning Hallucinations via Cross-Phase Routing Focus in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-885/summary.md) — RFS-Guard detects and localizes reasoning hallucinations in LRMs training-free, using a Routing Focus Score (RFS) that measures how strongly cross-step attention between reasoning and answer phases collapses toward semantic-neighbor proximity (rather than task-critical evidence) -- finding this 'routing collapse' is a strong hallucination signal that beats sampling-based, uncertainty-based, and other self-aware baselines while remaining far more inference-efficient.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
