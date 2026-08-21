# LIBERO-LONG

<!-- auto:begin -->

LIBERO-LONG is a long-horizon robot manipulation suite that entered this wiki through vision-language-action papers sharing the topic's 'test-time compute' and 'early exit' vocabulary; the archive files VLA-ATTC as tangential and outside the topic's scope, since it reports only that it cuts the failure rate of the PI0.5 baseline by over 50% on LIBERO-LONG. AVA-VLA gives the one genuine adaptive-depth measurement on it - a confidence-gated early exit cutting mean latent reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms, at 98.1% success on LIBERO-Long and 98.3% across LIBERO overall, against 98.0% with a fixed depth of 5 at 156 ms - but the archive notes that success rates near 98% are close enough to saturation that the benchmark cannot resolve whether adaptive depth helps accuracy. So the reading here is that the extra depth buys nothing measurable and the early exit is a latency optimisation that costs no accuracy, not evidence that stopping at the right point improves answers.

- **Kind**: dataset
- **Also called**: LIBERO-Long
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Early Exit](../methods/early-exit.md), [Latent reasoning](../concepts/latent-reasoning.md)

## Appears in

- [VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](../../archive/papers/2026/title-dc0ea43626fc6cec/summary.md) — Adds an uncertainty-triggered switch to Vision-Language-Action robot control models that shifts from reflexive action execution to a deliberation phase scored by a pairwise action critic.
- [Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models](../../archive/papers/2026/title-e3df9e3ad63924a6/summary.md) — AVA-VLA replaces explicit chain-of-thought in a vision-language-action policy with a sequence of latent reasoning variables trained by RL denoising, and adds a confidence-gated early exit that cuts mean reasoning depth from 5.0 to 2.3 steps and latency from 312 ms to 145 ms at essentially unchanged LIBERO success rate.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
