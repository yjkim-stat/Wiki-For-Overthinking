# Chain-of-thought faithfulness

<!-- auto:begin -->

Whether a model's visible reasoning trace is the real support for the answer it gives, which the archive's two sources measure from opposite ends. The KV-cache-compression study looks at the trace as evidence: compression can leave final-answer accuracy intact while the rationale that supposedly justifies the answer becomes invalid or fragile, a divergence the authors name the answer-evidence gap. Risky Business instead measures causal dependence - whether the model acts on what its trace says - using Targeted Reasoning Replacement, a search-and-replace edit of the model's own trace over 77 hand-written HazMart shopkeeper scenarios, and finds the property cuts both ways: models that follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently. So faithfulness here is not one quantity - one source asks whether the trace supports the answer, the other whether the answer follows the trace - and the second source shows it is not simply a property to maximise.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Chain-of-thought monitorability](chain-of-thought-monitorability.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [MMLU](../datasets/mmlu.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](../../archive/papers/2026/arxiv-2608-01631/summary.md) — A diagnostic study showing that KV cache compression for large reasoning models can preserve final-answer accuracy while the visible rationale supporting the answer becomes invalid or fragile, which the authors call the answer-evidence gap.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
