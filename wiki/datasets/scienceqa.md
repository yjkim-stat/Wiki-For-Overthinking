# ScienceQA

<!-- auto:begin -->

ScienceQA is a multimodal science-QA benchmark used in this archive by CoRAP's conformal-prediction uncertainty framework and by vStream, which trains a lightweight linear estimator to predict counterfactual visual-attribution effects from cached attention features, streaming visual grounding at 0.024s per 10 tokens versus 1.9-2.8s for causal baselines.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AI2D](ai2d.md), [GQA](gqa.md), [GSM8K](gsm8k.md), [LLaVA-CoT](../models/llava-cot.md), [MATH](math.md), [MathVerse](mathverse.md), [MathVista](mathvista.md), [OlympiadBench](olympiadbench.md), [Phi-4](../models/phi-4.md), [PRM800K](prm800k.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [StrategyQA](strategyqa.md)

## Appears in

- [Quantifying and Understanding Uncertainty in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1511/summary.md) — CoRAP is a conformal-prediction framework that constructs statistically valid uncertainty sets over reasoning-answer pairs for large reasoning models (guaranteeing a correct answer supported by valid reasoning is covered with a user-specified probability), paired with a Shapley-value-based example-to-step explanation method that provably identifies which training examples and reasoning steps are sufficient to achieve that coverage.
- [ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-536/summary.md) — ReProbe is a lightweight (<10M-parameter) transformer probe trained on a frozen LLM's internal states (hidden states, attention, logits) to predict step-level reasoning correctness, matching or exceeding Process Reward Models up to 810x larger for test-time-scaling verification, at 2.6-25x faster inference, and can be trained fully self-supervised (the model annotating its own reasoning) with no human labels or Monte Carlo rollouts.
- [Real-Time Visual Attribution Streaming in Thinking Model](../../archive/papers/2026/title-503ded235751878b/summary.md) — vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
