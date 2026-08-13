# MMLU-STEM

<!-- auto:begin -->

The science, technology, engineering and mathematics subset of a broad multiple-choice knowledge benchmark, used by both sources as the transfer check in a suite otherwise built from mathematics — the test of whether a method tuned on mathematical reasoning carries to knowledge-heavy multiple choice. Neither studies it. One reports it among the five sets where its latent-thought credit scheme wins at 3B (64.86%) and at 7B (70.10%); the other includes it in a seven-benchmark sweep across three model scales. Its role is negative evidence: a method that improves mathematics while moving this set backwards would be overfitting the training domain, and in both papers it does not.

- **Kind**: dataset
- **Also called**: MMLU-Stem
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME24](aime24.md), [AIME25](aime25.md), [credit assignment](../concepts/credit-assignment.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [latent reasoning](../concepts/latent-reasoning.md), [MATH](math.md), [MATH-500](math-500.md), [MATH500](math500.md), [pass@k](../methods/pass-k.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [REINFORCE](../methods/reinforce.md), [RLVR](../methods/rlvr.md), [soft thinking](../methods/soft-thinking.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning](../../archive/papers/2026/arxiv-2608-01593/summary.md) — Estimates what a continuous latent thought is worth by freezing the context after it and averaging the rewards of several answers sampled from that fixed context, then credits latent positions with the resulting thought-level advantage and answer positions with the ordinary group-relative one.
- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
