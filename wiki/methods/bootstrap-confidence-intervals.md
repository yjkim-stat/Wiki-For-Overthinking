# bootstrap confidence intervals

<!-- auto:begin -->

Resampling a result many times to put an interval on it, used in both sources as the discipline that keeps a headline honest about how well determined it is. In the Parkinson's screening work the intervals are what make the fused AUROC of 0.802 readable at all -- the interval [0.70, 0.89] on 20 positive cases overlaps both single modalities, and a within-test split-half check is judged to agree precisely because it falls inside that interval, so the bootstrap serves as the yardstick for whether a subgroup difference is a difference. In the test-time-scaling reproducibility work it is part of what a reproducible inference protocol is required to declare. Neither source treats the bootstrap as a subject; what they establish jointly is a norm, that a reported number without an interval on this kind of small evaluation is not interpretable, and that pairing or stratifying the resample -- by problem, by seed, by orientation -- is what makes the interval answer the question actually asked.

- **Kind**: method
- **Also called**: bootstrap CI, paired bootstrap
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BBH](../datasets/bbh.md), [beam search](beam-search.md), [best-of-n](best-of-n.md), [Brumo](../datasets/brumo.md), [budget forcing](budget-forcing.md), [class imbalance](../concepts/class-imbalance.md), [CLIP](../models/clip.md), [CMIMC](../datasets/cmimc.md), [construct validity](../concepts/construct-validity.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1](../models/deepseek-r1.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [gpt-oss-20b](../models/gpt-oss-20b.md), [HMMT](../datasets/hmmt.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Monte Carlo tree search](monte-carlo-tree-search.md), [pass@k](../concepts/pass-k.md), [permutation test](permutation-test.md), [Phi-4-reasoning](../models/phi-4-reasoning.md), [process reward model](../concepts/process-reward-model.md), [Qwen3-30B-A3B-Thinking-2507](../models/qwen3-30b-a3b-thinking-2507.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](self-consistency.md), [shortcut learning](../concepts/shortcut-learning.md), [steering vector](steering-vector.md), [test-time scaling](test-time-scaling.md), [Tree of Thoughts](tree-of-thoughts.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.
- [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-08976/summary.md) — Builds a Parkinson's screen from control data alone using a contrastive activation direction derived from synthetically degraded healthy speech and a nearest-neighbour anomaly score in face-encoder space, and gives a measurable precondition -- positive cosine between the synthetic and real disease directions -- that predicts in advance which modality the steering primitive will work on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
