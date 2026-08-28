# abstention

<!-- auto:begin -->

Abstention -- an LLM's ability to recognize when it should not answer (an ill-posed, ambiguous, or unanswerable query) -- is studied in these sources as a capability degraded by reasoning-style prompting: TRACE INVERSION shows CoT prompting itself lowers abstention accuracy by an average 2.6% versus non-reasoning prompting, and proposes detecting failures via query-reconstruction mismatch; Statistical Early Stopping for Reasoning Models proposes monitoring uncertainty-keyword arrivals within a trace to trigger abstention-driven halting on ill-posed queries, with a finite-sample bound on premature halting for well-posed ones.

- **Kind**: concept
- **Also called**: Abstention
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Conformal Prediction](../methods/conformal-prediction.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [early stopping](early-stopping.md), [GPQA](../datasets/gpqa.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GSM-MC](../datasets/gsm-mc.md), [GSM8K](../datasets/gsm8k.md), [HellaSwag](../datasets/hellaswag.md), [HLE](../datasets/hle.md), [MMLU](../datasets/mmlu.md), [Overthinking](overthinking.md), [Phi-4](../models/phi-4.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Test-Time Compute](test-time-compute.md), [UMWP](../datasets/umwp.md), [Uncertainty Quantification](uncertainty-quantification.md)

## Appears in

- [Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-608/summary.md) — TRACE INVERSION reframes abstention as query misalignment -- a hallucinating model answered a different (reconstructed) question than the one the user actually posed -- and detects this by reconstructing the implied query from a model's own reasoning trace and comparing it to the original via an ensemble of embedding-similarity, LLM-judged, and groundedness-detection metrics, beating five baselines in 33/36 settings across four LLMs and nine abstention datasets, while separately showing that CoT/reasoning-trace prompting itself degrades abstention accuracy by an average 2.6% versus non-reasoning prompting.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
