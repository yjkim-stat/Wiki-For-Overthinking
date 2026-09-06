# sparse autoencoders (SAEs)

<!-- auto:begin -->

Sparse autoencoders (SAEs) are a mechanistic-interpretability tool for extracting interpretable features from neural network activations, discussed in a survey organizing mechanistic-interpretability research on large reasoning models, and shown by a compressed-sensing-theoretic analysis to have an inherent encoder-insufficiency limitation for accurate sparse inference, which a decoupled encoder/decoder approach with more expressive inference techniques can substantially improve.

- **Kind**: method
- **Also called**: SAEs, Sparse Autoencoders (SAEs)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Aha Moment](../concepts/aha-moment.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepMath-103K](../datasets/deepmath-103k.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [linear probe](linear-probe.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Reward Hacking](../concepts/reward-hacking.md)

## Appears in

- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/local-34cecfd6f28ba72b/summary.md) — A survey that organizes existing mechanistic-interpretability research on large reasoning models into three areas -- reasoning-oriented training dynamics, reasoning mechanisms, and unintended behaviors (hallucination, CoT unfaithfulness, overthinking, unsafety) -- and proposes directions for future mechanistic work.
- [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](../../archive/papers/2026/local-4c4d1944c8091d55/summary.md) — Trains Top-K sparse autoencoders on the residual stream of DeepSeek-R1-Distill-Qwen-7B to contrast the internal feature dynamics of explicit chain-of-thought (Thinking) against direct answer generation (NoThinking), finding Thinking relies on a sparse, high-intensity, difficulty-invariant feature regime while NoThinking uses a diffuse, difficulty-adaptive one, and that causally suppressing Thinking's dominant features degrades formatting and triggers compensatory, less informative verbosity rather than a clean shortening of the trace.
- [Compute Optimal Inference and Provable Amortisation Gap in Sparse Autoencoders](../../archive/papers/2025/title-67cc50b85e8eb705/summary.md) — Using compressed sensing theory, proves that a sparse autoencoder (SAE) encoder is inherently insufficient for accurate sparse inference even in solvable cases, and shows decoupling encoding from decoding to use more expressive inference techniques yields substantial interpretability gains with minimal extra compute, including on large language models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
