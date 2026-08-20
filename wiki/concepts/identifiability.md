# identifiability

<!-- auto:begin -->

Whether a quantity recovered from a model is determined by the model or by the procedure that recovered it. Both sources treat it as the question mechanistic interpretability has lacked an answer to, and reach it from opposite ends. The theoretical source proves it for one primitive: lifting the forward pass with the Koopman operator gives a spectrum that is coordinate-free, unique up to permutation, invariant under any change of dictionary basis, and recoverable from finite calibration data at the parametric rate with a matching lower bound -- and argues that sparse-autoencoder non-identifiability is therefore structural rather than algorithmic, since the reconstruction-and-sparsity objective does not enforce the required invariance. The empirical source demonstrates the same failure without the theory, sweeping every extraction choice behind a published internal signal and finding no configuration best across benchmarks, models or framings, with the dominant factor family differing between two benchmarks and a mismatched fitting source driving the signal below chance. Together they mark why the question matters practically: a result that is not identifiable is not comparable across papers, since two studies using different recipes are not measuring the same object.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [BigCodeBench](../datasets/bigcodebench.md), [circuit analysis](../methods/circuit-analysis.md), [cross-validation](../methods/cross-validation.md), [detection versus control](detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [distribution shift](distribution-shift.md), [feature absorption](feature-absorption.md), [feature consistency](feature-consistency.md), [Gemma-2-2B](../models/gemma-2-2b.md), [GPT-2 small](../models/gpt-2-small.md), [HumanEval+](../datasets/humaneval.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](interpretability-illusion.md), [layer selection](../methods/layer-selection.md), [linear probe](../methods/linear-probe.md), [logit lens](../methods/logit-lens.md), [MBPP+](../datasets/mbpp.md), [measurement invariance](measurement-invariance.md), [operating point](operating-point.md), [out-of-domain generalization](out-of-domain-generalization.md), [PCA](../methods/pca.md), [pre-registration](../methods/pre-registration.md), [Qwen](../models/qwen.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [residual stream](residual-stream.md), [safety case](safety-case.md), [selection bias](selection-bias.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md)

## Appears in

- [On the Robustness of LLMs' Internal Representation of Code Correctness](../../archive/papers/2026/arxiv-2608-08266/summary.md) — Asks whether a published internal signal for code correctness is a property of the model or of the one extraction recipe used to find it, sweeps every design choice systematically, and finds no configuration is best anywhere -- with the benchmark deciding which choice wins, and a mismatched fitting source able to drive the signal below chance.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
