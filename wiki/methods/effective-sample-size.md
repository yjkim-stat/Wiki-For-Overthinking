# effective sample size

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [clip-higher](clip-higher.md), [component ablation](component-ablation.md), [credit assignment](../concepts/credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1](../models/deepseek-r1.md), [degenerate generation](../concepts/degenerate-generation.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration](../concepts/exploration.md), [GRPO](grpo.md), [LiveCodeBench](../datasets/livecodebench.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass@k](../concepts/pass-k.md), [pre-registration](pre-registration.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [reward shaping](../concepts/reward-shaping.md), [selection bias](../concepts/selection-bias.md), [supervised fine-tuning](supervised-fine-tuning.md), [zero-advantage group](../concepts/zero-advantage-group.md)

## Appears in

- [Parameter Exploration for RLVR via Variational Learning](../../archive/papers/2026/arxiv-2608-09805/summary.md) — Explores in weight space rather than token space during RLVR by sampling policies from a variational posterior at rollout time, and introduces a training-time exploration metric -- how often a method produces a correct rollout on a prompt where GRPO produced none -- because entropy and pass@k cannot tell exploration from degeneration.
- [PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR](../../archive/papers/2026/arxiv-2608-11368/summary.md) — Points out that the group-relative policy gradient is a second-order U-statistic over pairs of rollouts rather than a sum of independent per-rollout contributions, and reallocates rollout compute accordingly -- treating prefixes as vertices and pair-gradient terms as edges, then correcting the resulting selection bias by inverse joint-inclusion weighting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
