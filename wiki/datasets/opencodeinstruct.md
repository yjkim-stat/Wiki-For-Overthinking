# OpenCodeInstruct

<!-- auto:begin -->

A large instruction-tuning corpus of programming problems, used by both sources as the coding half of a training or calibration mixture rather than as an evaluation set. One draws coding questions from it, in equal proportion with mathematics, to build the calibration set for ternary quantization — the mixture whose composition turns out to decide whether the quantized model scores zero or fifty-eight on mathematics. The other uses it among the corpora its step-level sparse autoencoder is trained over. In both, it is there to keep a method from being tuned on mathematics alone.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [AIME24](aime24.md), [AIME25](aime25.md), [chain of thought](../methods/chain-of-thought.md), [GSM8K](gsm8k.md), [HumanEval+](humaneval.md), [information bottleneck](../concepts/information-bottleneck.md), [linear probing](../methods/linear-probing.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](math-500.md), [MATH500](math500.md), [MBPP+](mbpp.md), [monosemanticity](../concepts/monosemanticity.md), [Omni-MATH](omni-math.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [self-consistency](../methods/self-consistency.md), [self-verification](../concepts/self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](../concepts/superposition.md)

## Appears in

- [Attend to Your Own Thoughts: Breaking the Barrier for Post-Training Quantization of Reasoning LLMs through the Lens of 1.58-Bit Quantization](../../archive/papers/2026/arxiv-2608-01078/summary.md) — Finds that ternary post-training quantization of a reasoning model collapses because the calibration set is web text, and repairs it by calibrating on chain-of-thought traces the target model generates for itself.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
