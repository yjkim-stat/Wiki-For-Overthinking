# counterfactual intervention

<!-- auto:begin -->

Changing one input or internal element while holding everything else fixed, so that a difference in output is attributable to that element. Both sources treat the holding-fixed as the hard part. One injects synthetic reasoning snippets into a trace and measures both whether the model follows them and whether it admits doing so, which turns influence into a known quantity and non-disclosure into a measurable one — over 90% for extreme hints. The other removes a single prompt word while fixing the sampling seed, so that two generated images differ only by that word. The archive's trace-level work faces the same nuisance-variation problem and does not consistently apply an equivalent control.

- **Kind**: method
- **Also called**: controlled ablation, counterfactual, intervention
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [abstention](../concepts/abstention.md), [activation patching](activation-patching.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude-3.7-Sonnet](../models/claude-3-7-sonnet.md), [epistemic verbalization](../concepts/epistemic-verbalization.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [Gemini-3.1-Pro](../models/gemini-3-1-pro.md), [GPT-4.1](../models/gpt-4-1.md), [GPT-4o](../models/gpt-4o.md), [GPT-5.5](../models/gpt-5-5.md), [grounding](../concepts/grounding.md), [GRPO](grpo.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [monitorability](../concepts/monitorability.md), [multi-hop reasoning](../concepts/multi-hop-reasoning.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [process reward](../concepts/process-reward.md), [retrieval-augmented generation](retrieval-augmented-generation.md), [supervised fine-tuning](supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [synthetic data generation](synthetic-data-generation.md), [traceability](../concepts/traceability.md)

## Appears in

- [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](../../archive/papers/2026/arxiv-2608-03292/summary.md) — Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.
- [Reasoning Traces Shape Outputs but Models Won&apos;t Say So](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1986/summary.md) — Injects synthetic reasoning into a model's trace, shows the injection changes the answer, then shows the model refuses to admit it and fabricates an unrelated explanation instead.
- [Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1265/summary.md) — Traces how individual prompt tokens ground into image regions during diffusion denoising, using fixed-seed single-word removal for causal faithfulness and a head-resolved spike score for attribution.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
