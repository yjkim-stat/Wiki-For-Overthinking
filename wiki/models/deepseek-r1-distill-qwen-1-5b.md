# DeepSeek-R1-Distill-Qwen-1.5B

<!-- auto:begin -->

A 1.5B Qwen checkpoint distilled from DeepSeek-R1's long chain-of-thought reasoning, used by both sources as the small end of an efficiency study rather than as an object of interest. One reports cutting its average token usage by 87.1% while raising accuracy 2.3%, by penalizing tokens whose marginal utility for the correct answer is negative. The other uses it as a baseline against which per-query non-thinking token budgets cut tokens by around 50% with improved accuracy. That such large reductions come with accuracy gains on this checkpoint is the archive's clearest evidence that distilled reasoning chains carry a substantial fraction of tokens doing no work.

- **Kind**: model
- **Also called**: DeepSeek-R1-Distill-Qwen1.5B, R1-Distill-Qwen-1.5B
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [attention analysis](../methods/attention-analysis.md), [chain-of-thought compression](../methods/chain-of-thought-compression.md), [credit assignment](../concepts/credit-assignment.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DPO](../methods/dpo.md), [generative rewriting](../methods/generative-rewriting.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [length control](../methods/length-control.md), [length penalty](../methods/length-penalty.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [Pareto frontier](../concepts/pareto-frontier.md), [prompt difficulty](../concepts/prompt-difficulty.md), [reasoning distillation](../methods/reasoning-distillation.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning skeleton](../concepts/reasoning-skeleton.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [restructuring level](../concepts/restructuring-level.md), [reward hacking](../concepts/reward-hacking.md), [self-correction](../concepts/self-correction.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [token efficiency](../concepts/token-efficiency.md), [token selection](../concepts/token-selection.md), [TokenSkip](../methods/tokenskip.md), [verification](../concepts/verification.md)

## Appears in

- [Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1386/summary.md) — Defines a token's marginal utility as its log-probability gain for the ground-truth answer, then trains against negative-utility tokens to shorten chains of thought.
- [Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2122/summary.md) — Fixes reward hacking in hybrid thinking/non-thinking RL by setting per-query token limits for non-thinking responses derived from the solution part of that query's thinking responses.
- [CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning](../../archive/papers/2026/local-39eae4c377c77302/summary.md) — Finds that the </think> token aggregates the reasoning chain in deep layers and that attention paid to it from that position ranks which steps matter, then uses that ranking to drive a four-operator compression search — cutting 58% of tokens with accuracy holding.
- [Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs](../../archive/papers/2026/local-d3ff7e5088463145/summary.md) — Turns a linear chain of thought into a dependency DAG, labels each node as advancing the frontier or reviewing it, and prunes review nodes on two graph criteria — too few descendants, or too late in the trace — cutting 42% of tokens while accuracy holds or rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
