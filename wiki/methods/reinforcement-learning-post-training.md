# reinforcement learning post-training

<!-- auto:begin -->

Applying RL after pretraining and supervised tuning to shape reasoning, the archive's default recipe and the object of six sources here. Four modify its reward — confining an efficiency reward to a single mode-selection token, adding a compress reward for post-answer redundancy, penalizing negative-utility tokens, setting per-query non-thinking budgets. One forces canonical rollouts so that uniformly-rewarded groups regain the variance the advantage estimate needs. One measures a cost rather than proposing a method, finding instruction adherence degrades under both distilled long-CoT tuning and reasoning-oriented RL, worsening as generation length grows. The sources agree the stage works and disagree about what its reward should be attached to.

- **Kind**: method
- **Also called**: RL fine-tuning, RL post-training, RLHF-style post-training
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 6

**Related**: [abstention](../concepts/abstention.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [advantage estimation](../concepts/advantage-estimation.md), [alignment tax](../concepts/alignment-tax.md), [answer stabilization](../concepts/answer-stabilization.md), [controllability](../concepts/controllability.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GRPO](grpo.md), [hallucination](../concepts/hallucination.md), [instruction following](../concepts/instruction-following.md), [knowledge distillation](knowledge-distillation.md), [length control](../concepts/length-control.md), [overthinking](../concepts/overthinking.md), [Pareto frontier](../concepts/pareto-frontier.md), [prompt difficulty](../concepts/prompt-difficulty.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](reward-shaping.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](supervised-fine-tuning.md), [token selection](../concepts/token-selection.md), [verification](../concepts/verification.md)

## Appears in

- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.
- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Identifies double-checking after the correct answer is already derived as 'invalid thinking', and trains a GRPO variant with a compress reward that targets exactly that portion.
- [Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1878/summary.md) — A benchmark showing that as reasoning capacity grows, instruction adherence falls, and that recovering obedience costs reasoning performance.
- [Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2122/summary.md) — Fixes reward hacking in hybrid thinking/non-thinking RL by setting per-query token limits for non-thinking responses derived from the solution part of that query's thinking responses.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — Attributes efficiency-training damage to sequence-level coupling between efficiency and correctness rewards, and decouples them by applying the efficiency reward only to a single mode-selection token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
