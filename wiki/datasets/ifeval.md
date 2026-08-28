# IFEval

<!-- auto:begin -->

IFEval is used in these sources as an instruction-following benchmark for evaluating reasoning-efficiency methods' generalization beyond math: PACE reports out-of-domain accuracy and token-reduction gains on it (among GPQA-Diamond and LiveCodeBench-v6) despite training exclusively on math data, and the model-interpolation study and the entropy-in-RLVR paper both use it as one of several out-of-domain/instruction-following evaluation points.

- **Kind**: dataset
- **Also called**: IF-Eval
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink (baseline)](../methods/adaptthink-baseline.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [DAPO-Math-17k (training)](dapo-math-17k-training.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER (baseline)](../methods/deer-baseline.md), [Dynasor-CoT (baseline)](../methods/dynasor-cot-baseline.md), [entropy collapse](../concepts/entropy-collapse.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench-v6](livecodebench-v6.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](math500.md), [Minerva](minerva.md), [O1-Pruner (baseline)](../methods/o1-pruner-baseline.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-4B-Thinking-2507](../models/qwen3-4b-thinking-2507.md), [Reasoning Collapse](../concepts/reasoning-collapse.md)

## Appears in

- [Revisiting Model Interpolation for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-389/summary.md) — Reveals that linear interpolation between an Instruct model's and a Thinking model's weights does not trade off performance and reasoning verbosity smoothly, but follows a predictable three-stage transition (Instruct-dominated -> abrupt thinking-pattern emergence -> converging to Thinking with diminishing/overthinking returns), and shows a strategically chosen interpolation point beats sophisticated model-merging baselines (task arithmetic, TIES) on both efficiency and accuracy.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1266/summary.md) — A systematic study of entropy collapse in GRPO-based RLVR training finds performance can improve without entropy loss (so entropy collapse is not merely a side effect of legitimate learning), identifies clipping thresholds, off-policy update count, and training-data diversity as governing factors, proves theoretically and confirms empirically that positive-advantage tokens are the primary driver of entropy collapse, and proposes Positive-Advantage Reweighting -- dynamically down-weighting positive-advantage-token loss -- to regulate entropy while maintaining performance, though training exclusively on non-positive-advantage tokens actually hurts benchmark scores despite reducing collapse.
- [PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1545/summary.md) — PACE identifies two distinct failure modes of uniform length-penalty RL for efficient reasoning -- sequence-level over-compression of critical early deduction steps, and group-level indiscriminate compression that ignores query difficulty -- and fixes both with a frozen-policy prefix-rollout anchor (decaying over training) plus a pass-rate-derived, difficulty-scaled length penalty, becoming the only compared method to cut token usage over 45% while simultaneously improving accuracy, and generalizing to code, science and instruction-following domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
