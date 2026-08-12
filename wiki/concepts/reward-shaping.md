# reward shaping

<!-- auto:begin -->

Designing the reward's structure — what it attaches to, and when — rather than only its target, which all four sources treat as where efficiency methods succeed or fail. One confines an efficiency reward to a single mode-selection token after diagnosing that a sequence-level efficiency signal implicitly penalizes long but correct trajectories. One pairs a length reward with a compress reward aimed specifically at double-checking that occurs after the answer is already derived. One forces 'None' rollouts so negative samples produce a valid advantage, and penalizes over-refusal on positives. One scales the reward by problem difficulty. The shared lesson is that a reward correct in aggregate can be wrong per token or per group.

- **Kind**: concept
- **Also called**: reward design, reward engineering
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [abstention](abstention.md), [adaptive compute allocation](adaptive-compute-allocation.md), [advantage estimation](advantage-estimation.md), [AIME24](../datasets/aime24.md), [answer stabilization](answer-stabilization.md), [credit assignment](credit-assignment.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hallucination](hallucination.md), [length control](../methods/length-control.md), [majority voting](../methods/majority-voting.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [Pareto frontier](pareto-frontier.md), [prompt difficulty](prompt-difficulty.md), [reasoning redundancy](reasoning-redundancy.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [RLVR](../methods/rlvr.md), [self-correction](self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Identifies double-checking after the correct answer is already derived as 'invalid thinking', and trains a GRPO variant with a compress reward that targets exactly that portion.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — Attributes efficiency-training damage to sequence-level coupling between efficiency and correctness rewards, and decouples them by applying the efficiency reward only to a single mode-selection token.
- [The Overthinker's DIET: Cutting Token Calories with DIfficulty-AwarE Training](../../archive/papers/2025/local-5feb5d3d92da16e0/summary.md) — Trains reasoning models to be concise in proportion to difficulty by modulating the token penalty and the target length per problem, and fixes a distortion that naive reward weighting introduces into group-normalized RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
