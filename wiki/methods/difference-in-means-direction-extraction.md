# difference-in-means direction extraction

<!-- auto:begin -->

A technique for finding a single direction in a model's residual-stream activations that encodes a target behavior, computed as the mean activation over one contrastive set of examples minus the mean activation over another -- e.g. 'redundant' versus 'concise' reasoning trajectories, or hard-difficulty versus easy-difficulty MATH questions -- taken at a fixed layer and token position. In the manifold-steering source, this raw direction captures overthinking, but ablating it directly only reduces overthinking up to a point: its effect plateaus and then reverses as intervention strength increases, corrupting other model abilities, which motivates projecting it onto a lower-dimensional PCA manifold before applying it. In the reasoning-strength-planning source, the same procedure extracted per layer for MATH difficulty levels yields nearly identical directions across difficulty pairs and layers (cosine similarity ~0.99), with magnitude tracking the number of extra reasoning tokens a question requires, and adding or subtracting the resulting vector causally shortens or lengthens the response by making early or late termination of reasoning more or less likely.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [AdvBench](../datasets/advbench.md), [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-14B](../models/deepseek-r1-distill-qwen-14b.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [Dynasor (baseline)](dynasor-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [QwQ-32B](../models/qwq-32b.md), [SEAL (baseline)](seal-baseline.md)

## Appears in

- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/local-1da36a797481ea8a/summary.md) — A training-free residual-stream steering method that mitigates overthinking by projecting a difference-in-means 'overthinking direction' onto a low-dimensional PCA manifold of the model's activations before ablating it, removing the accuracy-degrading interference noise that limits naive single-direction steering.
- [On Reasoning Strength Planning in Large Reasoning Models](../../archive/papers/2025/local-77b3413236375923/summary.md) — Finds that large reasoning models pre-plan how many reasoning tokens a question will need, encoded as a single pre-allocated direction vector in their activations whose magnitude can be read out to predict reasoning length or added/subtracted to causally control it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
