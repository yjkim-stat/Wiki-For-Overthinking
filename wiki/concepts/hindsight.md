# hindsight

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ALFWorld](../datasets/alfworld.md), [component ablation](../methods/component-ablation.md), [credit assignment](credit-assignment.md), [factorial ablation](../methods/factorial-ablation.md), [forward KL divergence](../methods/forward-kl-divergence.md), [GRPO](../methods/grpo.md), [HMMT 2025](../datasets/hmmt-2025.md), [KL regularization](../methods/kl-regularization.md), [knowledge distillation](../methods/knowledge-distillation.md), [multi-agent pipeline](multi-agent-pipeline.md), [on-policy distillation](../methods/on-policy-distillation.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [outcome reward](outcome-reward.md), [paired bootstrap](../methods/paired-bootstrap.md), [pass@k](pass-k.md), [privileged information](privileged-information.md), [process reward](process-reward.md), [Qwen2.5-3B](../models/qwen2-5-3b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [selectivity control](../methods/selectivity-control.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [teacher-student gap](teacher-student-gap.md), [WebShop](../datasets/webshop.md)

## What we have settled

- **Established** — Removing a signal and scrambling it are different experiments: only the second separates a method that exploits matched correspondence from one that benefits from the signal's marginal properties, and where both are run the scrambled condition is the informative one.
  - Three groups in three settings converged on the same control independently, each preserving a signal's presence and distribution while destroying only which item it corresponds to. In privileged on-policy self-distillation, the teacher is given each student's completed trajectory; the ablation both removes that trajectory and shuffles trajectories across problems, keeping the field populated while breaking its correspondence to the problem and prefix. Shuffling hurts more than removal on both measured quantities — teacher continuation success falls 0.089 against 0.064, and next-token divergence rises 0.110 against 0.067 — so a mismatched trajectory is worse than none, and the benefit is specifically matched hindsight rather than extra context. In agentic hindsight distillation, per-turn allocation multipliers are permuted within a trajectory so each active turn receives another active turn's multiplier: the multiplier values are preserved up to a common rescaling and the eligible-token-weighted mean is restored to one, so supervision magnitude, multiplier distribution and normalisation are all held fixed and only the assignment is broken. The same paper also runs a uniform-multiplier condition, giving the full decomposition — signal absent, signal present but flat, signal present but misassigned, signal present and aligned — and finds flat dense supervision worth 6.4 points on one metric and nothing consistent on three others. In probing, the classical form is a label permutation: shuffling labels and rerunning the entire pipeline 200 times per layer measures what that exact pipeline scores when the labels are meaningless, which is what licenses reading a held-out probe accuracy at all when the feature dimension exceeds the sample count by two orders of magnitude. The three share a structure worth stating generally. An ablation that deletes a component answers whether the component carries information; a permutation that preserves the component and breaks its alignment answers whether the method uses the alignment, which is usually the claim being made. Where a paper reports that per-step supervision, privileged context or a learned allocation helps, the scrambled condition is the one to ask for — and in the two training cases here it changed the reading, since dense-but-unaligned supervision recovered only part of the gain and mismatched context was worse than no context at all.

## Appears in

- [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](../../archive/papers/2026/arxiv-2608-07371/summary.md) — Distributes hindsight supervision across the turns of an agent trajectory by comparing each turn's share of total revision magnitude against its share of eligible tokens, holding the average multiplier at one so the total supervision is fixed and only its allocation changes -- and isolates that allocation with a permutation control that keeps the multiplier values and scrambles which turn receives which.
- [PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](../../archive/papers/2026/arxiv-2608-08726/summary.md) — Gives the teacher in on-policy self-distillation access to each completed student rollout and its verified outcome, adapting it to preserve behaviour on successes and redirect failures toward verified success, while the student keeps a prefix-only interface it can actually deploy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
