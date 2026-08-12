# token selection

<!-- auto:begin -->

Choosing which tokens in a reasoning trace deserve gradient, reward or removal — the archive's central technical dispute, with each source proposing a different criterion and none measuring overlap with the others. The criteria collected here are the teacher's distributional shift when a reference solution is supplied, the signed per-token log-probability gain of the ground-truth answer, the model's own likelihood contribution to the answer and to local coherence, and a teacher's skill-aware decomposition of steps. Elsewhere in the archive the same question is answered by Shannon entropy and by Jensen-Shannon divergence from a reference distribution. One criterion is signed, so it can mark a token as actively harmful rather than merely uninformative; the rest select tokens to weight up.

- **Kind**: concept
- **Also called**: critical token identification, token weighting, token-level credit
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [AIME](../datasets/aime.md), [credit assignment](credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GSM8K](../datasets/gsm8k.md), [length control](../methods/length-control.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [overthinking](overthinking.md), [Pareto frontier](pareto-frontier.md), [preference optimization](../methods/preference-optimization.md), [privileged information](privileged-information.md), [process supervision](process-supervision.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](reasoning-redundancy.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [token-level distillation](../methods/token-level-distillation.md)

## Appears in

- [RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer](../../archive/papers/2026/arxiv-2608-06347/summary.md) — Concentrates privileged self-distillation on reasoning pivots identified by the teacher's distributional shift when an English reference solution is added or removed, for multilingual reasoning transfer.
- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.
- [Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-25/summary.md) — Prunes chain-of-thought segments the model's own likelihood landscape marks as extraneous, then trains on the resulting pruning preference pairs.
- [DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-196/summary.md) — Has a teacher decompose and prune a student's reasoning by mathematical skill, then distills the pruned paths back, on the argument that CoT structure must match student capacity.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
