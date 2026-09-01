# PRM800K

<!-- auto:begin -->

PRM800K is a process-reward-model training dataset referenced in SAT (which models reasoning as a Finite-State Machine over four thinking modes navigated by a 30M-parameter distilled Process Reward Model) and ReProbe (a lightweight transformer probe trained on a frozen LLM's internal states to predict step-level reasoning correctness).

- **Kind**: dataset
- **Also called**: PRM800K
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [MATH](math.md), [MATH500](math500.md), [Phi-4](../models/phi-4.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [ScienceQA](scienceqa.md), [StrategyQA](strategyqa.md)

## Appears in

- [SAT: Balancing Reasoning Accuracy and Efficiency with Stepwise Adaptive Thinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2009/summary.md) — SAT models reasoning as a Finite-State Machine over four thinking modes (SLOW, NORMAL, FAST, SKIP), navigated step-by-step during inference by a 30M-parameter distilled Process Reward Model ('Pilot') that scores each step's difficulty and steers generation via in-context control tags, achieving up to 40% token reduction while generally maintaining or improving accuracy across 9 models and 7 benchmarks.
- [ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-536/summary.md) — ReProbe is a lightweight (<10M-parameter) transformer probe trained on a frozen LLM's internal states (hidden states, attention, logits) to predict step-level reasoning correctness, matching or exceeding Process Reward Models up to 810x larger for test-time-scaling verification, at 2.6-25x faster inference, and can be trained fully self-supervised (the model annotating its own reasoning) with no human labels or Monte Carlo rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
