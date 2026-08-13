<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs

- **Authors**: Yuqi Wu, Shengming Zhao, Jie Chen
- **Venue**: cs.AI
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08159>
- **PDF**: <https://arxiv.org/pdf/2608.08159v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large language models (LLMs) are increasingly reported to exhibit human-like neural and cognitive signatures, including concept cells, mental number lines, and cognitive maps. These claims often rely on linear probing and activation steering applied to a single model, yet both methods are highly sensitive to measurement choices. A reported parallel may therefore reflect the model, the measurement procedure, or both. We audit four representative neuroscience-inspired paradigms across 17 models from five families, spanning $0.6$B to $72$B parameters. Our main experiment examines the causal steerability of concept directions. With raw activation units and a fixed layer and coefficient, steerability appears to increase with model scale, resembling an emergent capability. However, this pattern is produced by an uncalibrated pipeline rather than by a claim established in the steering literature. The trend depends jointly on raw units, the readout metric, and the operating point; correcting any one of these removes it. With residual-norm-comparable interventions and held-out operating-point selection, concept steering remains significant at every scale, but shows no significant trend across the Qwen3 series, although the confidence interval does not rule out a moderate positive slope. The remaining results are mixed. A linear geographic world map is consistently decodable in every tested checkpoint up to $72$B. Number magnitude is strongly encoded, but whether individual neurons appear bell-shaped or monotonic depends on the selection criterion. Language-specific structure is localizable, but the direction of the cross-lingual asymmetry reverses under a different attribution method. These results suggest that the main constraint on AI neuroscience is not a lack of phenomena, but a lack of comparable measurements and adequate controls. We release the protocol, stimuli, and code.

---

Record id: `arxiv:2608.08159`
