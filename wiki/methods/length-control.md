# length control

<!-- auto:begin -->

Constraining how long a reasoning trace may be, which all three sources find fails when applied at the level of the whole sequence. One replaces trajectory-level control with a signed per-token signal, penalizing tokens that reduce the likelihood of the correct answer, and reports token reductions of 87.1% at 1.5B with accuracy up 2.3%. One sets a different maximum for each query, derived from the solution component of that query's own thinking responses, on the grounds that a uniform limit is wrong for every query. One diagnoses the shared defect directly: a sequence-level efficiency reward implicitly penalizes long but correct trajectories, so the reward is confined to a single mode-selection token instead.

- **Kind**: method
- **Also called**: length budget, length penalty, token budget
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [overthinking](../concepts/overthinking.md), [Pareto frontier](../concepts/pareto-frontier.md), [prompt difficulty](../concepts/prompt-difficulty.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reinforcement learning post-training](reinforcement-learning-post-training.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](../concepts/reward-shaping.md), [supervised fine-tuning](supervised-fine-tuning.md), [token selection](../concepts/token-selection.md), [verification](../concepts/verification.md)

## What we have settled

- **Established** — Control over how long a reasoning model thinks is concentrated in a single special token rather than distributed over the trace, and four sources reach that token from four unrelated directions.
  - Nothing here set out to study the delimiter; each source arrives at it while answering a different question. Mechanism: the pre-allocated reasoning-strength vector steers length by shifting the logits of the end-of-thinking token specifically, with far larger effect there than on the end-of-sequence token or on random tokens. Representation: in deep layers the </think> position progressively aggregates the preceding chain, and during final-answer generation the model attends predominantly to it and only weakly to the intermediate steps. Training: a sequence-level efficiency reward implicitly penalizes long but correct trajectories, and confining that reward to one mode-selection token removes the coupling — after which adjusting that single token's generation probability at inference moves one trained model continuously along the efficiency-performance frontier. Failure mode: on QwQ-32B nearly every competing early-exit baseline fails, and the reason is sporadic invalidation of the end-of-thinking delimiter. The four are independent in method (activation steering, attention analysis, reward placement, baseline failure) and agree on the locus. This matters because the same literature's generation-time signals — token entropy, hidden-state norm, predictive entropy — all read diffuse quantities, while the compression work finds redundancy itself to be diffuse; a distributed signal aimed at a distributed phenomenon is the harder problem, and the delimiter is where the model has already concentrated the decision.

## Appears in

- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.
- [Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2122/summary.md) — Fixes reward hacking in hybrid thinking/non-thinking RL by setting per-query token limits for non-thinking responses derived from the solution part of that query's thinking responses.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — Attributes efficiency-training damage to sequence-level coupling between efficiency and correctness rewards, and decouples them by applying the efficiency reward only to a single mode-selection token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
