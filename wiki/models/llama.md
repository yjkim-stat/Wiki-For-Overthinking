# Llama

<!-- auto:begin -->

Meta's open-weight model family, used across the archive as the base on which reasoning behaviour is studied, and named loosely: the sources say 'Llama' both for the pretrained family and for particular checkpoints and their reasoning-distilled variants. It matters here because open weights make internal analysis possible -- the sycophancy work localizes trace sentences with probes and counterfactual rollouts on it, and the position paper fine-tunes members of the family to test whether trace correctness governs answer correctness. Where a claim depends on which member was used, prefer the specific checkpoint over this entry.

- **Kind**: model
- **Also called**: LLaMA, Llama 3.1
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [GPT-OSS](gpt-oss.md), [GRPO](../methods/grpo.md), [linear probe](../methods/linear-probe.md), [localization](../concepts/localization.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [Qwen](qwen.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-20/summary.md) — Locates the sentences in a reasoning trace that commit a model to agreeing with an incorrect user suggestion, using counterfactual rollouts and linear probes.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) — A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
