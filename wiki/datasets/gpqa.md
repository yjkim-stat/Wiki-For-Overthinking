# GPQA

<!-- auto:begin -->

A graduate-level science question benchmark, used in the archive as the non-mathematical hard reference alongside competition math. Both sources use it to test whether a method generalizes past math rather than to study the benchmark: one for a training-free hidden-state verifier applied to selection and reranking, the other for selecting RLVR training tokens by the divergence of their logit distribution from a reference. Its presence in the archive is thin — two sources, both incidental — which is itself informative given how dominated the collection is by math benchmarks.

- **Kind**: dataset
- **Also called**: Graduate-Level Google-Proof Q&A
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [activation probing](../methods/activation-probing.md), [AIME 24](aime-24.md), [AIME 25](aime-25.md), [AIME24](aime24.md), [AIME25](aime25.md), [answer stabilization](../concepts/answer-stabilization.md), [best-of-n](../methods/best-of-n.md), [calibration](../methods/calibration.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [MATH-500](math-500.md), [MATH500](math500.md), [MMLU-PRO](mmlu-pro.md), [pass-k](../methods/pass-k.md), [Qwen2.5](../models/qwen2-5.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [QwQ-32B](../models/qwq-32b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [reward hacking](../concepts/reward-hacking.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [token-level entropy](../concepts/token-level-entropy.md), [verification](../concepts/verification.md), [VeRL](../methods/verl.md)

## Appears in

- [Your Reasoning Model is Secretly a Reward Model - Optimization-Free Verification from Experience](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-788/summary.md) — Verifies correctness without training by comparing a reasoning trace's start-to-end hidden-state delta against two class centroids built from labelled experience.
- [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](../../archive/papers/2026/local-2175408b166d313f/summary.md) — Argues that Shannon entropy is the wrong criterion for picking which tokens to train on in RLVR, and selects tokens instead by the Jensen-Shannon divergence of their logit distribution from the group average, updating only the top 10% of these 'unique' tokens.
- [Provable Scaling Laws for the Test-Time Compute of Large Language Models](../../archive/papers/2025/local-e5ae26db2daac1d7/summary.md) — Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
