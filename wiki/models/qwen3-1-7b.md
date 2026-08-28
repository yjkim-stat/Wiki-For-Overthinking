# Qwen3-1.7B

<!-- auto:begin -->

A small open-weight model used across sources as an efficient-agent backbone: split into two specialized sub-2B agents in a memory-efficient counterspeech-generation framework (per another archived source), and as the model whose per-token generation cost Prefix Sliding's attention-probability motivating analysis is measured on.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [LLaMA-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Phi-4](phi-4.md), [Phi-decoding](../methods/phi-decoding.md), [PRM800K](../datasets/prm800k.md), [Qwen3-0.6B](qwen3-0-6b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [ScienceQA](../datasets/scienceqa.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](../../archive/papers/2026/arxiv-2608-23152/summary.md) — FIRE splits counterspeech generation into two sub-2B Qwen3-1.7B agents -- one that classifies the hate category, names the target group, writes a reasoning trace and triggers a web search for evidence, one that writes the reply -- with specialization coming from a contrastively-trained 22M retrieval encoder over annotated examples rather than from fine-tuning.
- [Prefix Sliding for efficient test-time scaling](../../archive/papers/2026/arxiv-2608-26070/summary.md) — Prefix Sliding discards reasoning tokens outside a prefix (system instructions/prompt) plus a sliding window of the most recent tokens, giving constant per-token generation cost that lets language models reason for arbitrarily long horizons -- 3x faster than full attention without training, and enabling RL rollouts beyond 100,000 tokens with better reward than full-attention training at equal memory.
- [MUR: Momentum Uncertainty guided Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1058/summary.md) — MUR (Momentum Uncertainty guided Reasoning) is a training-free, orthogonal-to-existing-TTS method that recursively aggregates step-level uncertainty into a momentum term (proven to act as a low-pass filter emphasizing recent steps) and selectively applies test-time-scaling compute only to steps whose uncertainty exceeds this momentum by a tunable threshold, cutting thinking-token budgets by over 45% on average while improving accuracy 0.33-3.46% across four benchmarks, three Qwen3 model sizes, and four test-time-scaling backends.
- [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-200/summary.md) — Introduces attention-temperature modulation (softening/sharpening the attention softmax at inference, distinct from decoding-temperature sampling) as a difficulty-adaptive exploration control -- higher attention temperature broadens exploration and helps hard problems, lower temperature curbs overthinking and helps easy ones -- and pairs it with a difficulty-induced weighted-voting aggregation scheme (Thermometer of Thoughts), improving Pass@10 by 6.78-14.20% and aggregation accuracy by 9.74% across seven reasoning benchmarks.
- [ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-536/summary.md) — ReProbe is a lightweight (<10M-parameter) transformer probe trained on a frozen LLM's internal states (hidden states, attention, logits) to predict step-level reasoning correctness, matching or exceeding Process Reward Models up to 810x larger for test-time-scaling verification, at 2.6-25x faster inference, and can be trained fully self-supervised (the model annotating its own reasoning) with no human labels or Monte Carlo rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
