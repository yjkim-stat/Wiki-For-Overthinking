# NoThinking

<!-- auto:begin -->

In this archive NoThinking appears only as a named comparison method and is never described. ReBalance lists it among nine efficient-reasoning baselines (with CoD, DEER, NoWait, Dynasor-CoT, SEAL, Manifold Steering, FlashThink and TrimR) and ARLCP lists it among its own (with SFT_Shortest, DPO_Shortest, O1-Pruner, TLMRE, AdaptThink and LASER); neither reports its mechanism, and neither gives its scores separately from the baseline set. The one thing the archive does record about the family it is filed with is ReBalance's objection to it: remedies that suppress reflection or cap length make length the control variable and can push a model out of overthinking and into underthinking.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](activation-steering.md), [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Answer Convergence](../concepts/answer-convergence.md), [Budget Forcing](budget-forcing.md), [Chain-of-Draft](chain-of-draft.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DEER](deer.md), [DPO_Shortest](dpo-shortest.md), [Dynasor](dynasor.md), [Early Exit](early-exit.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [Laser](laser.md), [Length Penalty](../concepts/length-penalty.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [NOWAIT](nowait.md), [O1-Pruner](o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [SEAL](seal.md), [SFT_Shortest](sft-shortest.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Early Stopping for Large Reasoning Models via Confidence Dynamics](../../archive/papers/2026/local-204ad034bca12641/summary.md) — CoDE-Stop stops reasoning when either a ramping confidence threshold is crossed or an early-step-weighted 'degeneration score' of accumulated confidence instability exceeds a threshold, targeting both trajectories that are already done and trajectories that are going nowhere, and its evaluation is the archive's first independent head-to-head of RCPD and Answer Convergence under one protocol.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
