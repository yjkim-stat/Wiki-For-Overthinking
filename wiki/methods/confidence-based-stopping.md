# Confidence-Based Stopping

<!-- auto:begin -->

Confidence-based stopping ends reasoning when the model's own confidence in a candidate answer passes a threshold, rather than when a token budget runs out or a fixed number of steps completes. ParallelWorld applies it at the outer loop of an embodied search: an answer agent emits its prediction once confidence exceeds gamma = 0.8 or the exploration budget is exhausted, with no sensitivity analysis reported for that threshold. AVA-VLA applies it inside a vision-language-action policy as a confidence-gated early exit over latent reasoning variables, cutting mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success rate. The two share the shape -- a scalar confidence, a threshold, an exit -- and differ in what the confidence is about: a proposed answer in one case, a latent reasoning state in the other.

- **Kind**: method
- **Also called**: confidence threshold stopping, confidence-based stopping, confidence-gated early exit
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [Early Exit](early-exit.md), [GPT-5.5](../models/gpt-5-5.md), [Information Gain](../concepts/information-gain.md), [Latent reasoning](../concepts/latent-reasoning.md), [LIBERO-Long](../datasets/libero-long.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [ParallelWorld: Test-Time Scaling for Embodied Reasoning](../../archive/papers/2026/arxiv-2608-22971/summary.md) — ParallelWorld is a verifier-guided tree search over simulated future observations for embodied reasoning: from a restorable simulator state it expands several candidate camera and physical actions in parallel, prunes branches with a verifier agent under a branch-width schedule, and answers from the top-ranked root-to-leaf route.
- [Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models](../../archive/papers/2026/title-e3df9e3ad63924a6/summary.md) — AVA-VLA replaces explicit chain-of-thought in a vision-language-action policy with a sequence of latent reasoning variables trained by RL denoising, and adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success rate.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
