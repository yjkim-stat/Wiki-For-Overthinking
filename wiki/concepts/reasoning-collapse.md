# Reasoning Collapse

<!-- auto:begin -->

The failure in which reinforcement learning drives a model's reasoning trace towards nothing rather than towards length - the under-thinking direction, not overthinking. On four subjective verification rubrics with no deterministic verifier, outcome-only RLVR under GRPO drops Qwen2.5-7B's mean completion length from about 300 tokens to about 170 after roughly 70 steps as the policy switches to fast heuristic guessing; TwT reports the same shape for R1-Zero-style RL on machine translation, where traces fall below 100 tokens and degenerate into templates, three of which cover about 73% of Zh->En traces, with or without a KL term. Both read it as evidence that the emergent long reasoning seen in mathematics and code does not transfer to their domains. The fixes differ: the subjective-tasks paper puts length back into the reward as a capped bonus paid only when the answer is correct (L_target = 1000, lambda = 2e-4), reaching 0.851 macro-F1 at about 980 tokens against 0.805 reasoning and 0.748 no-reasoning baselines, while TwT uses no length reward at all and restores length through difficulty-rewritten cold-start data - removing that stage collapses its traces to 62 tokens.

- **Kind**: concept
- **Also called**: Reasoning collapse, reasoning collapse
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink (baseline)](../methods/adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](../methods/deer-baseline.md), [Dr. GRPO](../methods/dr-grpo.md), [Dynasor-CoT (baseline)](../methods/dynasor-cot-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [Length reward](length-reward.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [MATH500](../datasets/math500.md), [O1-Pruner (baseline)](../methods/o1-pruner-baseline.md), [Overthinking](overthinking.md), [Resource-Rational Reasoning](resource-rational-reasoning.md), [Reward Hacking](reward-hacking.md), [underthinking](underthinking.md)

## Appears in

- [Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2607-29287/summary.md) — TwT trains a translation model to spend reasoning tokens in proportion to input difficulty, by cold-starting on 7K difficulty-rewritten CoT traces and then running GRPO with a BLEU+COMET quality reward and an n-gram repetition penalty.
- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — An empirical study of LLM verifiers on four subjective verification tasks from a production recommender platform, showing that explicit reasoning often degrades accuracy and that standard RLVR drives reasoning length to near zero ('reasoning collapse'), plus a conditional length-penalized reward that restores it.
- [PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1545/summary.md) — PACE identifies two distinct failure modes of uniform length-penalty RL for efficient reasoning -- sequence-level over-compression of critical early deduction steps, and group-level indiscriminate compression that ignores query difficulty -- and fixes both with a frozen-policy prefix-rollout anchor (decaying over training) plus a pass-rate-derived, difficulty-scaled length penalty, becoming the only compared method to cut token usage over 45% while simultaneously improving accuracy, and generalizing to code, science and instruction-following domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
