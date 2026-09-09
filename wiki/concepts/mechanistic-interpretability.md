# mechanistic interpretability

<!-- auto:begin -->

Both archived sources use 'mechanistic interpretability' loosely, as a label for reading and intervening on a model's internal representations rather than for circuit-level reverse engineering, and neither defines it. Manifold Steering works in that register: it finds a single activation-space direction correlated with overthinking, traces the plateau-then-harm behaviour of naive steering to that direction lying on a low-dimensional manifold, and projects the steering vector onto the manifold before applying it at inference, cutting output tokens by up to 71% on DeepSeek-R1 distilled models while maintaining or improving accuracy on mathematical benchmarks (the benchmarks are not named in the material the archive holds). The sparse-autoencoder paper attaches the term to the feature-dictionary line of work instead, and argues via compressed sensing that an SAE's linear-nonlinear encoder provably cannot recover the true sparse code even on solvable instances, so substituting a stronger sparse-inference procedure over the same learned dictionary recovers codes better for small extra compute -- the archive records no number for that gain, nor the interpretability metric claimed to improve. Between the two, the term covers both the analysis of internal representations and the interventions that analysis licenses.

- **Kind**: concept
- **Also called**: Mechanistic Interpretability, mechanistic interpretability
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [Activation Patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [difference-in-means direction extraction](../methods/difference-in-means-direction-extraction.md), [Dynasor (baseline)](../methods/dynasor-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](../methods/manifold-steering.md), [MATH500](../datasets/math500.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [SEAL (baseline)](../methods/seal-baseline.md)

## Appears in

- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/local-1da36a797481ea8a/summary.md) — A training-free residual-stream steering method that mitigates overthinking by projecting a difference-in-means 'overthinking direction' onto a low-dimensional PCA manifold of the model's activations before ablating it, removing the accuracy-degrading interference noise that limits naive single-direction steering.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
