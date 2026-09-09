# Activation Patching

<!-- auto:begin -->

A causal-intervention diagnostic that substitutes the activation at a chosen layer and position with one drawn from a different, contrasting run -- e.g. a harmless-prompt activation in place of a harmful-prompt one -- and measures how much of the output (a logit-difference recovery or downstream accuracy) is restored, establishing that a component causally matters rather than merely correlates with the outcome. One source applies it layer-wise as a causal probe over chain-of-thought traces, restoring original activations at only 10-20% of token positions to recover near-full-trace accuracy for content-bearing tokens; it treats this explicitly as diagnostic only, since it requires a full-precision forward pass over the uncompressed trace and is therefore not itself a deployable compression method. The other source uses it, alongside attribution patching, for circuit-level analysis of how different post-training objectives (SFT, reasoning-augmented SFT, ORPO) implement refusal, selecting which layers and attention heads to steer by measuring normalized logit-difference recovery layer by layer.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [difference-in-means direction extraction](difference-in-means-direction-extraction.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MMLU](../datasets/mmlu.md), [Qwen3-8B](../models/qwen3-8b.md), [StrongReject](../datasets/strongreject.md), [Token Entropy](../concepts/token-entropy.md), [WildJailbreak](../datasets/wildjailbreak.md), [XSTest](../datasets/xstest.md), [ZebraLogic](../datasets/zebralogic.md)

## Appears in

- [Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models](../../archive/papers/2026/arxiv-2607-28707/summary.md) — A controlled re-evaluation of entropy-based chain-of-thought compression showing that low- and high-entropy selection never beats random pruning once a random baseline is included, and that the one apparent exception on math benchmarks is caused by numeric tokens rather than by entropy.
- [Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness](../../archive/papers/2026/local-24bb8e465bad18c7/summary.md) — A controlled, cross-paradigm mechanistic comparison of three post-training safety methods (SFT, reasoning-augmented SFT, and ORPO) across three model architectures, showing that training objective -- not just data -- reshapes how and where refusal is computed internally, and that no method studied is simultaneously robust, capability-preserving, and correctable via small steering edits.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
