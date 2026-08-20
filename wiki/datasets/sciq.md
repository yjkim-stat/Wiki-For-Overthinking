# SciQ

<!-- auto:begin -->

A science question-answering set that appears in three archived papers as a supporting evaluation set, with none of them describing its construction or reporting a headline attributed to it. Two are test-time-scaling papers that use it as the non-mathematical member of an otherwise mathematical suite: the interpretable adaptive-sampling controller is evaluated on GSM8K, MATH and SciQ, and ThinkRetrieve on GSM8K, MATH500, AIME 2025, SciQ and NuminaMath. The third uses it as one of the corpora over which dense trained lenses are fitted and evaluated, alongside the Pile, 2WikiMultiHopQA, ARC-Easy and WikiText-2. Its role in this archive is as a breadth check rather than as a target.

- **Kind**: dataset
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [2WikiMultiHopQA](2wikimultihopqa.md), [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2025](aime-2025.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [budget forcing](../methods/budget-forcing.md), [circuit analysis](../methods/circuit-analysis.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [dense retrieval](../methods/dense-retrieval.md), [detection versus control](../concepts/detection-versus-control.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [GSM8K](gsm8k.md), [importance sampling](../methods/importance-sampling.md), [in-context learning](../concepts/in-context-learning.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [logit lens](../methods/logit-lens.md), [LoRA](../methods/lora.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH](math.md), [MATH500](math500.md), [predictive entropy](../concepts/predictive-entropy.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning drift](../concepts/reasoning-drift.md), [residual stream](../concepts/residual-stream.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [selection signal](../concepts/selection-signal.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [self-reflection](../methods/self-reflection.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [test-time scaling](../methods/test-time-scaling.md), [the Pile](the-pile.md), [tuned lens](../methods/tuned-lens.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [WikiText-2](wikitext-2.md)

## Appears in

- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](../../archive/papers/2026/arxiv-2608-10928/summary.md) — Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
