# safety alignment

<!-- auto:begin -->

Training a model to refuse or avoid harmful behaviour, which all three sources argue must address the reasoning process rather than the output. Two locate the failure mid-trajectory: one finds models recognize harmful intent and then override that judgement in later steps — named Self-Jailbreak — and intervenes step-wise; the other claims the reasoning structure itself is the cause and alters it with 1K supervised examples. The third shifts from prevention to recovery, adding a token that lets a model reflect and recover mid-generation, reporting harmful completion falling from 13.8% to 4.1%. All three are measured against attacks the authors chose, and the archive holds an attack reaching approaching 100% against reasoning-based defences.

- **Kind**: concept
- **Also called**: harmlessness alignment, safety tuning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [adversarial robustness](adversarial-robustness.md), [alignment tax](alignment-tax.md), [data efficiency](data-efficiency.md), [generalization](generalization.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [jailbreak](jailbreak.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [overthinking](overthinking.md), [post-training](../methods/post-training.md), [reasoning trajectory](reasoning-trajectory.md), [self-correction](self-correction.md), [self-reflection](../methods/self-reflection.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Test-Time Scaling for Safe Text-Guided Image Generation via Intermediate Clean Estimates](../../archive/papers/2026/arxiv-2608-03284/summary.md) — Triggers a safety intervention in image diffusion from the intermediate clean-image estimate rather than from the prompt, and spends optimization only from the first timestep where a violation actually appears — so extra test-time compute is incurred on unsafe inputs and benign latency stays flat as the budget grows.
- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.
- [When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1118/summary.md) — Names Self-Jailbreak, where a model correctly flags a query as harmful and then overrides that judgement during later reasoning steps, and intervenes step-wise rather than over whole trajectories.
- [Self-Reflection Improves Safety of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-678/summary.md) — Adds a Self-Reflection token that lets reasoning models recover from harmful output mid-generation, cutting harmful completion rate from 13.8% to 4.1%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
