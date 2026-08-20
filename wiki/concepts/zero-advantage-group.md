# zero-advantage group

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [clip-higher](../methods/clip-higher.md), [component ablation](../methods/component-ablation.md), [credit assignment](credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1](../models/deepseek-r1.md), [degenerate generation](degenerate-generation.md), [effective sample size](effective-sample-size.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration](exploration.md), [GRPO](../methods/grpo.md), [LiveCodeBench](../datasets/livecodebench.md), [matched-budget comparison](matched-budget-comparison.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass@k](pass-k.md), [pre-registration](../methods/pre-registration.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [reward shaping](reward-shaping.md), [selection bias](selection-bias.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Parameter Exploration for RLVR via Variational Learning](../../archive/papers/2026/arxiv-2608-09805/summary.md) — Explores in weight space rather than token space during RLVR by sampling policies from a variational posterior at rollout time, and introduces a training-time exploration metric -- how often a method produces a correct rollout on a prompt where GRPO produced none -- because entropy and pass@k cannot tell exploration from degeneration.
- [PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR](../../archive/papers/2026/arxiv-2608-11368/summary.md) — Points out that the group-relative policy gradient is a second-order U-statistic over pairs of rollouts rather than a sum of independent per-rollout contributions, and reallocates rollout compute accordingly -- treating prefixes as vertices and pair-gradient terms as edges, then correcting the resulting selection bias by inverse joint-inclusion weighting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
