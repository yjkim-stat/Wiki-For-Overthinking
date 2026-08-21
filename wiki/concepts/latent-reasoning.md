# Latent reasoning

<!-- auto:begin -->

Carrying the intermediate steps of reasoning in continuous hidden states rather than emitting them as chain-of-thought tokens, so that test-time compute is spent on internal iterations instead of on generated text. The archived sources instantiate this in four ways: a recurrent-depth architecture that iterates a latent block to arbitrary depth in place of longer chains; Penelope, which confines the recurrence to a five-layer slice of the decoder and refines a fixed-size boundary memory K times rather than re-running the whole model; Heima, which replaces each stage of a multimodal chain of thought with one learned thinking token and trains a separate decoder to expand those tokens back into readable reasoning; and AVA-VLA, which trains latent reasoning variables in a vision-language-action policy by RL denoising. The recurring open problem across them is not whether to reason latently but how deep to go: AVA-VLA adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success, and SLPO trains a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon, scoring latent transitions with a Gaussian surrogate density from MC-dropout forwards. Because the steps are no longer text, they are not directly inspectable, which is why Heima trains a decoder to recover them.

- **Kind**: concept
- **Also called**: Latent Reasoning, Latent reasoning, latent reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [AI2D](../datasets/ai2d.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Chain-of-Thought Compression](chain-of-thought-compression.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [CoLaR](../methods/colar.md), [Early Exit](../methods/early-exit.md), [GRPO](../methods/grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [LIBERO-Long](../datasets/libero-long.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [MATH500](../datasets/math500.md), [MathVista](../datasets/mathvista.md), [MMStar](../datasets/mmstar.md), [Recurrent Depth](recurrent-depth.md), [RLOO](../methods/rloo.md), [speculative decoding](../methods/speculative-decoding.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [Test-Time Scaling](test-time-scaling.md), [Thinking Budget](thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.
- [Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models](../../archive/papers/2026/title-e3df9e3ad63924a6/summary.md) — AVA-VLA replaces explicit chain-of-thought in a vision-language-action policy with a sequence of latent reasoning variables trained by RL denoising, and adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success rate.
- [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](../../archive/papers/2025/title-f75fffe554037a34/summary.md) — Introduces a recurrent-depth architecture that scales test-time compute by iterating a latent reasoning block to arbitrary depth instead of generating more chain-of-thought tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
