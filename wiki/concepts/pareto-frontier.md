# Pareto frontier

<!-- auto:begin -->

The set of achievable accuracy-versus-cost trade-offs where neither can improve without the other worsening, and the standard framing for efficient-reasoning results in the archive. Sources report positions on it — roughly 50% length reduction at roughly 2% accuracy cost in one case, 87.1% token reduction with a 2.3% accuracy gain in another — and one provides continuous traversal at inference from a single trained model by adjusting one token's generation probability. A fourth source challenges the framing itself, characterizing the solution space to argue that sparse paths exist that are simultaneously more accurate and more concise, which would mean the trade-off these papers negotiate is not fundamental.

- **Kind**: concept
- **Also called**: accuracy-cost trade-off, efficiency-accuracy trade-off, pareto front
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [answer stabilization](answer-stabilization.md), [chain of thought](chain-of-thought.md), [credit assignment](credit-assignment.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [foresight](foresight.md), [GRPO](../methods/grpo.md), [length control](../methods/length-control.md), [overthinking](overthinking.md), [reasoning redundancy](reasoning-redundancy.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [reward shaping](../methods/reward-shaping.md), [self-correction](self-correction.md), [test-time compute](test-time-compute.md), [token selection](token-selection.md)

## Appears in

- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.
- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Identifies double-checking after the correct answer is already derived as 'invalid thinking', and trains a GRPO variant with a compress reward that targets exactly that portion.
- [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1149/summary.md) — Reformulates reasoning as a search over thinking strategies, showing sparse reasoning paths exist that are simultaneously more accurate and shorter than standard outputs.
- [ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-165/summary.md) — Attributes efficiency-training damage to sequence-level coupling between efficiency and correctness rewards, and decouples them by applying the efficiency reward only to a single mode-selection token.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
