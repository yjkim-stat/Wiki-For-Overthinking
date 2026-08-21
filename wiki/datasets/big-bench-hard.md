# BIG-Bench Hard

<!-- auto:begin -->

None of the three archived sources describes BIG-Bench Hard; each mentions it only as one evaluation suite among several, alongside their own contributions -- a framework casting test-time scaling as budgeted inference over a prefix tree with 1,948,821 released reasoning traces, ARM's per-task choice among four reasoning formats via Ada-GRPO (about 30% fewer tokens at roughly unchanged accuracy), and a supermartingale-certified router between thinking and non-thinking models. The archive also holds this benchmark under at least three further entries -- 'BBH', 'BBH (Big Bench Hard)' and 'BIG-Bench Hard (BBH)' -- which are the same suite, not distinct ones; 'BBH (Big Bench Hard)' carries the fuller note and is the one to read.

- **Kind**: dataset
- **Also called**: BBH, Big-Bench-Hard
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [BBH (Big Bench Hard)](bbh-big-bench-hard.md), [Chain-of-Draft](../methods/chain-of-draft.md), [CMIMC25](cmimc25.md), [CommonsenseQA](commonsenseqa.md), [Distribution Shift](../concepts/distribution-shift.md), [GPQA](gpqa.md), [Group-Relative Policy Optimization](../concepts/group-relative-policy-optimization.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HMMT 2025](hmmt-2025.md), [MATH](math.md), [MMLU-PRO](mmlu-pro.md), [overthinking](../concepts/overthinking.md), [Risk Control](../concepts/risk-control.md), [Self-Certainty](../methods/self-certainty.md), [StrategyQA](strategyqa.md), [SuperGPQA](supergpqa.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [SVAMP](svamp.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [Anytime Safe PAC Efficient Reasoning](../../archive/papers/2026/title-b525ac9b26640523/summary.md) — Routes queries between a thinking and a non-thinking model with a threshold that is adjusted online by a betting supermartingale, so the accumulated statistical evidence certifies at any stopping time that the accuracy given up stays under a user-specified tolerance.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
