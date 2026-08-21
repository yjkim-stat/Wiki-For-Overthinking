# MMStar

<!-- auto:begin -->

A general (non-mathematical) multimodal question-answering benchmark that entered this archive through vision-language papers matching the topic's vocabulary rather than its subject. Two of its four sources are marked tangential or out of scope: HiDrop is recorded as a false positive on the phrase 'early exit' — the tokens it drops are image patch embeddings, not reasoning steps, and its 96.5%-of-baseline result at 91.7% token compression across 11 benchmarks is a prefill-side cost, not a decoding-length one — and Mixture-of-Visual-Thoughts reports no token counts or latency at all, only that its RL-trained model splits roughly evenly between text and grounded reasoning modes on MMStar (~51% grounded) where it goes almost entirely one way on the math and grounding sets. The two remaining sources use it as one of a large evaluation panel: Heima evaluates zero-shot on MMStar among six benchmarks and prices its extreme latent compression at roughly 6% of baseline tokens for 3.1 accuracy points on the average, and ARES includes it among ten multimodal benchmarks where ARES-7B averages 55.9 pass@1 against 46.2. No archived source reports an MMStar-specific accuracy-versus-reasoning-length figure.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AI2D](ai2d.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [Ares](../methods/ares.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GPQA](gpqa.md), [GQA](gqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [latent reasoning](../concepts/latent-reasoning.md), [Layer-wise early exit](../methods/layer-wise-early-exit.md), [MATH-500](math-500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU-PRO](mmlu-pro.md), [MMMU](mmmu.md), [overthinking](../concepts/overthinking.md), [POPE](pope.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [Reinforcement Learning with Verifiable Rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [RLVR](../concepts/rlvr.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.
- [HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit](../../archive/papers/2026/title-b2302bb0271de496/summary.md) — HiDrop prunes about 90% of the vision tokens in a multimodal LLM by injecting them only at the layer where visual-text fusion actually begins and then dropping them on a concave schedule with a per-layer early exit, matching baseline accuracy while training 1.72x faster.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
