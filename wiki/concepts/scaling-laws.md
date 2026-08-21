# Scaling Laws

<!-- auto:begin -->

Scaling laws here cover two different senses: the first source's proposed constant-then-cooldown learning-rate schedule is meant to let scaling-law experiments reuse a single training run across many training durations, an experimental-methodology use; the second, on the Inverse Scaling Prize, instead reports 11 tasks on which accuracy gets worse, not better, as parameter count and training compute increase -- the sources disagree in valence rather than definition, one treating scaling as an experimental variable to control for and the other cataloguing where its usual benefit fails.

- **Kind**: concept
- **Also called**: Scaling Laws, scaling laws
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [inverse scaling](inverse-scaling.md)

## Appears in

- [Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations](../../archive/papers/2024/title-5eb9089f909af3c1/summary.md) — Replaces the cosine learning-rate schedule with a constant learning rate followed by a cooldown, so that scaling-law experiments can reuse a single training run across many training durations.
- [Inverse Scaling: When Bigger Isn't Better](../../archive/papers/2025/title-cb7f41c5af287a91/summary.md) — Reports 11 tasks, found via the Inverse Scaling Prize contest, on which language model accuracy declines as model parameter count and training compute increase, and analyzes why.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
