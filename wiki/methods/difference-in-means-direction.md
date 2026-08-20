# difference-in-means direction

<!-- auto:begin -->

A direction in activation space computed as the difference between the mean activations of two contrasting sets, usually normalised, and then either added to the residual stream to steer or projected onto to detect. Both sources use it and both make the same point about what limits it, from opposite ends. The text-to-MIDI work builds directions from 25 contrastive prompts per pole and states the constraint plainly: the poles differ lexically as well as in the target attribute, so a direction is only as clean as the contrast behind it -- and its metrics are proxies that are not fully independent of one another. The Parkinson's screening work turns that constraint into something measurable by building its direction from a synthetic degradation of healthy examples rather than from labelled positives, then checking the cosine between that synthetic direction and the real one: +0.37 for the speech encoder, where the detector works at AUROC 0.765, and -0.48 for the face encoder, where an anti-aligned direction scores at chance. Read together the sources say the same thing twice: the contrast pair, not the arithmetic, is the method, and whether the resulting direction points at the intended concept is a question that can be asked directly rather than assumed.

- **Kind**: method
- **Also called**: contrastive activation direction, difference-of-means direction, mean-difference direction
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [CLIP](../models/clip.md), [contrastive activation addition](contrastive-activation-addition.md), [detection versus control](../concepts/detection-versus-control.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [linear separability](../concepts/linear-separability.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [logit lens](logit-lens.md), [permutation test](permutation-test.md), [residual stream](../concepts/residual-stream.md), [selectivity control](../concepts/selectivity-control.md), [shortcut learning](../concepts/shortcut-learning.md), [sparse autoencoder](sparse-autoencoder.md), [steering vector](steering-vector.md), [tuned lens](tuned-lens.md)

## Appears in

- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) — Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
