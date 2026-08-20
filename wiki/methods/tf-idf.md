# TF-IDF

<!-- auto:begin -->

Term-frequency-inverse-document-frequency features, used in both sources as the surface baseline that a representation-based method has to beat -- and in both cases it turns out to be a much harder baseline than the framing suggests. In the ESG concept-content study, a TF-IDF classifier reaches 0.894 AUC on the Governance pillar, above every configuration of the RFM concept-vector method, and trails the best activation probe by only 2.0 accuracy points there (6.9 and 6.0 on the other two pillars) -- while the surface measures the approach was actually aimed at, a concept-word dictionary and a 25-topic model, sit far below at 0.128 and 0.373 F1. The paper draws the boundary itself: the surface-versus-judgment distinction holds against measures that count concept words, not against a classifier free to learn whatever lexical cues the labels happen to carry. It appears again as a baseline in the monitoring-observability work. The lesson these sources share is that a tuned lexical classifier and a dictionary are not the same kind of baseline, and only the first one tests the claim.

- **Kind**: method
- **Also called**: TF-IDF
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Gemma-4-31B-it](../models/gemma-4-31b-it.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5-mini](../models/gpt-5-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [logistic regression](logistic-regression.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [nested cross-validation](nested-cross-validation.md), [Omni-MATH](../datasets/omni-math.md), [PCA](pca.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [self-correction](../concepts/self-correction.md), [verbosity](../concepts/verbosity.md)

## Appears in

- [How Much Does a Reasoning Summary Reveal? An Observability Ladder for Large Language Models](../../archive/papers/2026/arxiv-2608-02089/summary.md) — Holds one completed reasoning run fixed and varies only what a monitor is allowed to inspect — response, self-summary, full trace, internals — and finds the summary's value nearly vanishes once the monitor already has the prompt, so monitorability is a property of the display and the reader jointly rather than of the text.
- [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](../../archive/papers/2026/arxiv-2608-07208/summary.md) — Compares linear probes against RFM-derived concept vectors for reading how much a sentence concerns a concept out of a frozen LLM's activations, on a human-annotated ESG benchmark, and finds the simpler probe consistently stronger.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
