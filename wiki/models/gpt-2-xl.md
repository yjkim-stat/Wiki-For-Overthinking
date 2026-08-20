# GPT-2 XL

<!-- auto:begin -->

A GPT-2-family model used in this archive as an interpretability test-bed rather than as a system anyone deploys. Its load-bearing appearance is in the activation-patching best-practices paper, which makes it the setting for factual-recall localization on a purpose-built PairedFacts set of 145 in-distribution prompt pairs, and finds that the clear MLP peak around layer 16 under Gaussian noising is not salient at all under symmetric token replacement, with the noising peak 2x to 5x higher across window sizes regardless of which metric scores it. It is therefore the model on which a widely cited localization result was shown to depend on the corruption method rather than on the model. It also appears among the six models, from GPT-2 to Llama-3.1-405B-Instruct, over which dense trained lenses were attached at every layer and hookpoint.

- **Kind**: model
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [2WikiMultiHopQA](../datasets/2wikimultihopqa.md), [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [ARC-Easy](../datasets/arc-easy.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [GPT-2](gpt-2.md), [GPT-2 small](gpt-2-small.md), [GPT-J 6B](gpt-j-6b.md), [importance sampling](../methods/importance-sampling.md), [indirect object identification](../datasets/indirect-object-identification.md), [KL divergence](../concepts/kl-divergence.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.3-70B](llama-3-3-70b.md), [localization](../concepts/localization.md), [logit lens](../methods/logit-lens.md), [LoRA](../methods/lora.md), [low-rank approximation](../methods/low-rank-approximation.md), [residual stream](../concepts/residual-stream.md), [SciQ](../datasets/sciq.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [the Pile](../datasets/the-pile.md), [tuned lens](../methods/tuned-lens.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
