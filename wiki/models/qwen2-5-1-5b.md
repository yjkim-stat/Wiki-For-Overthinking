# Qwen2.5-1.5B

<!-- auto:begin -->

A 1.5B Qwen checkpoint, used by both sources as the small model where a method's effect is largest and most visible. One reports its MATH500 accuracy reaching 58.0% and AMC rising from 25.0% to 32.5% under a verifier-free refine-then-vote scheme that beats verifier-based best-of-N. The other uses it in selecting RLVR training tokens by the divergence of their logit distribution from a reference. Its recurrence at this size is worth noting when reading the results: methods that substitute for weak calibration or weak verification have the most room to help on a small model, and neither source establishes that the gain survives to frontier scale.

- **Kind**: model
- **Also called**: Qwen2.5 1.5B
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [answer stabilization](../concepts/answer-stabilization.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPQA](../datasets/gpqa.md), [greedy decoding](../methods/greedy-decoding.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [majority voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [pass-k](../methods/pass-k.md), [Qwen2.5-0.5B](qwen2-5-0-5b.md), [Qwen2.5-7B](qwen2-5-7b.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
