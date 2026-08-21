# Confidence-based early stopping

<!-- auto:begin -->

Stopping a model's sampling or reasoning process once its own confidence signal (e.g. self-distilled calibration, or cross-agent consensus) indicates further compute is unlikely to change the answer, rather than running a fixed budget. CaTS uses a self-distilled confidence signal to adaptively size the sampling budget per query; TUMIX's multi-agent tool-use ensemble stops iterating once its agents' answers converge.

- **Kind**: method
- **Also called**: Confidence-based early stopping, confidence-based early stopping
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Best-of-N](best-of-n.md), [Confidence Calibration](../concepts/confidence-calibration.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Dynasor](dynasor.md), [early stopping](../concepts/early-stopping.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [KV-cache compression](kv-cache-compression.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [Overthinking](../concepts/overthinking.md), [process reward model](process-reward-model.md), [Qwen3-8B](qwen3-8b.md), [R-KV](r-kv.md), [Self-Consistency](self-consistency.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture](../../archive/papers/2026/title-545becf86760af05/summary.md) — An ensemble of parallel agents using different tool-use strategies that iteratively refine and share answers, with a confidence-based rule to stop early and cut inference cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
