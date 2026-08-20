# permutation test

<!-- auto:begin -->

A non-parametric test that builds its null distribution by relabelling the observed data, used in both sources as the confirmatory step after every other choice has been frozen. One makes it the audit's decision rule: the score, its orientation and the sample size are all fixed on a calibration split before the audit split is opened, and the one-sided two-sample permutation test on that untouched split is what the reported power curves are power *for*. The other uses paired signed-rank and bootstrap variants to compare circuit sites without assuming a parametric form. The reason it recurs here is the same in both: the quantities being tested -- behavioural separability, a patching effect -- have no defensible parametric null, and relabelling supplies one from the data itself.

- **Kind**: method
- **Also called**: permutation test
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap confidence intervals](bootstrap-confidence-intervals.md), [causal intervention](../concepts/causal-intervention.md), [causal tracing](causal-tracing.md), [circuit analysis](circuit-analysis.md), [CLIP](../models/clip.md), [contrastive activation addition](contrastive-activation-addition.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [low-rank weight ablation](low-rank-weight-ablation.md), [membership inference](membership-inference.md), [Pythia-410M](../models/pythia-410m.md), [residual stream](../concepts/residual-stream.md), [self-repair](../concepts/self-repair.md), [shortcut learning](../concepts/shortcut-learning.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [the Pile](../datasets/the-pile.md), [weight-space ablation](weight-space-ablation.md)

## Appears in

- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](../../archive/papers/2026/arxiv-2608-07914/summary.md) — Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) — Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
