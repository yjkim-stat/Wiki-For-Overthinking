# Dynasor

<!-- auto:begin -->

An inference-time reasoning-acceleration method, present in this archive only as a comparison point: both sources cite it in their baseline lists rather than describing it. One of them classes it with SAT as a length-only baseline and notes it was tuned to a comparable level of acceleration rather than compared across its own accuracy-latency curve, which is a caveat about the comparison rather than about the method. Nothing in the archive states how it works.

- **Kind**: method
- **Also called**: Dynasor-CoT
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Answer Convergence](answer-convergence.md), [Concise CoT (CCoT)](concise-cot-ccot.md), [Confidence-based early stopping](confidence-based-early-stopping.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [KV-cache compression](kv-cache-compression.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [process reward model](process-reward-model.md), [Qwen3-8B](../models/qwen3-8b.md), [R-KV](r-kv.md), [SAT](../datasets/sat.md), [SEAL](seal.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](../../archive/papers/2026/arxiv-2608-04771/summary.md) — ReCo uses a 30M process-reward estimator to set, per reasoning step, both the KV-cache retention ratio and generation-side controls (a reflection-token logit penalty and confidence-based early stopping), cutting generated tokens by 37-65% and end-to-end latency by 2.08-2.35x versus full-cache CoT.
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](../../archive/papers/2026/local-8ec022e440eb9021/summary.md) — Proposes PUMA, an inference-time early-exit framework that flags reasoning steps as candidate exits when a contrastively-trained embedding detector finds them semantically redundant with recent context, then confirms the exit is safe via answer-level confidence/consistency verification before stopping.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
