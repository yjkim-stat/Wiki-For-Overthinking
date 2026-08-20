# mechanistic interpretability

<!-- auto:begin -->

Explaining a model's behaviour in terms of its internal components, and across 6 sources a field the archive reads with its methodological problems foregrounded. Three appear repeatedly. Comparability: the literature has no convention for corruption methods or evaluation metrics, so results from different papers are frequently not measuring the same thing. Identifiability: where units come from a learned dictionary, different seeds and widths recover different features, so a claim about a feature is partly a claim about a run -- and one source argues the identifiable object and the human-legible object cannot be the same object. Auditability: one source calls for guidelines developed by continuous collaborative reviewing, which is the field-level version of the archive's own practice of asking for nulls and controls. The corpus's positive contributions are tooling and surveys -- a library bringing patching and attention analysis to vision-language models, and a survey organising training, inference and failures for reasoning models.

- **Kind**: concept
- **Also called**: MI, circuit analysis, mech interp
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 6

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [attention pattern](attention-pattern.md), [auditability](auditability.md), [chain of thought](chain-of-thought.md), [circuit analysis](../methods/circuit-analysis.md), [counterfactual intervention](../methods/counterfactual-intervention.md), [emergent behaviour](emergent-behaviour.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [generalization](generalization.md), [identifiability](identifiability.md), [literature survey](../methods/literature-survey.md), [LLaVA-1.5](../models/llava-1-5.md), [localization](localization.md), [meta-evaluation](meta-evaluation.md), [parity](../datasets/parity.md), [Qwen2.5-VL](../models/qwen2-5-vl.md), [Qwen3-VL](../models/qwen3-vl.md), [reproducibility](reproducibility.md), [sample complexity](sample-complexity.md), [training dynamics](training-dynamics.md)

## Appears in

- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-159/summary.md) — A position paper arguing mechanistic interpretability cannot be used in safety-critical settings until its findings are auditable, and proposing continuous collaborative reviewing plus source-based claim tracking.
- [Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-889/summary.md) — A survey organizing mechanistic findings about reasoning models into training dynamics, reasoning mechanisms and unintended behaviours, and arguing the field needs a unified theoretical framework.
- [Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1265/summary.md) — Traces how individual prompt tokens ground into image regions during diffusion denoising, using fixed-seed single-word removal for causal faithfulness and a head-resolved spike score for attribution.
- [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-502/summary.md) — A survey reorganizing mechanistic interpretability from observation into a Locate-Steer-Improve intervention pipeline, categorized by the interpretable object being acted on.
- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) — Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
