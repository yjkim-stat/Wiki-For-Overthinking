# latent reasoning

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: Latent Reasoning, Latent reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AI2D](../datasets/ai2d.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [COCONUT](coconut.md), [CODI](codi.md), [CoLaR](colar.md), [early exit](early-exit.md), [GRPO](grpo.md), [GSM-Hard](../datasets/gsm-hard.md), [LIBERO-LONG](../datasets/libero-long.md), [MATH-500](../datasets/math-500.md), [MathVista](../datasets/mathvista.md), [MMStar](../datasets/mmstar.md), [recurrent depth](../concepts/recurrent-depth.md), [RLOO](rloo.md), [speculative decoding](speculative-decoding.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [thinking budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [Efficient Reasoning with Hidden Thinking](../../archive/papers/2026/title-725397e20ebf1509/summary.md) — Heima replaces each stage of a multimodal model's textual chain of thought with a single learned 'thinking token' generated in latent space, and trains a separate decoder that can expand those tokens back into readable reasoning.
- [Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models](../../archive/papers/2026/title-e3df9e3ad63924a6/summary.md) — AVA-VLA replaces explicit chain-of-thought in a vision-language-action policy with a sequence of latent reasoning variables trained by RL denoising, and adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success rate.
- [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](../../archive/papers/2025/title-f75fffe554037a34/summary.md) — Introduces a recurrent-depth architecture that scales test-time compute by iterating a latent reasoning block to arbitrary depth instead of generating more chain-of-thought tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
