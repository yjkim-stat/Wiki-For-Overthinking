# persona conditioning

<!-- auto:begin -->

Instructing a model to answer as a specified character or role, and across 3 sources a manipulation whose internal effect is now partly measured. The mechanistic result: decomposing three speaker settings into sparse-autoencoder features finds roleplay personas retaining an Assistant-associated feature core while differentiating from it across depth, where narrated story characters never acquire that core at all -- so a persona is a modification of the assistant rather than a replacement of it. Its practical uses here are as the structuring device for multi-agent deliberation and as a routing signal for subjective judgement. The archive's related caution is measurement-shaped: one source measures spread across personas without a baseline spread for ordinary prompt variation, so it cannot separate persona-specific worldview from generic prompt sensitivity, and the personas are impersonated by one model rather than drawn from the population whose judgements are the ground truth.

- **Kind**: method
- **Also called**: persona prompting, role prompting
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [ablation](ablation.md), [activation steering](activation-steering.md), [annotation agreement](../concepts/annotation-agreement.md), [best-of-n](best-of-n.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [Claude Haiku 4.5](../models/claude-haiku-4-5.md), [Claude Sonnet 4.6](../models/claude-sonnet-4-6.md), [Cohen's kappa](cohen-s-kappa.md), [consensus](../concepts/consensus.md), [credit assignment](../concepts/credit-assignment.md), [detection versus control](../concepts/detection-versus-control.md), [difficulty conditioning](difficulty-conditioning.md), [Dr. GRPO](dr-grpo.md), [Gemma-3-4B-it](../models/gemma-3-4b-it.md), [GRPO](grpo.md), [GSPO](gspo.md), [human evaluation](human-evaluation.md), [jury aggregation](jury-aggregation.md), [length control](../concepts/length-control.md), [length penalty](length-penalty.md), [LLM-as-a-judge](llm-as-a-judge.md), [majority voting](majority-voting.md), [monosemanticity](../concepts/monosemanticity.md), [multi-agent pipeline](../concepts/multi-agent-pipeline.md), [outcome reward](../concepts/outcome-reward.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [reasoning collapse](../concepts/reasoning-collapse.md), [reward hacking](../concepts/reward-hacking.md), [reward shaping](reward-shaping.md), [RLVR](rlvr.md), [selectivity control](selectivity-control.md), [self-consistency](self-consistency.md), [sparse autoencoder](sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [steering vector](steering-vector.md), [sycophancy](../concepts/sycophancy.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- ["Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-07852/summary.md) — Decomposes three speaker settings -- the default Assistant, an assigned roleplay persona, and a narrated story character -- into sparse-autoencoder features at turn boundaries and pronoun tokens, and finds that roleplay personas retain an Assistant-associated feature core while differentiating from it across depth, where story characters never acquire that core at all.
- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](../../archive/papers/2026/arxiv-2608-08889/summary.md) — Shows on four internal Netflix verification tasks that explicit reasoning usually degrades subjective judgement, that applying RLVR to fix it makes the policy abandon deliberation for short heuristic guessing, and that a length bonus gated on answer correctness is what stops the collapse.
- [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](../../archive/papers/2026/arxiv-2608-11420/summary.md) — Structures multi-agent medical differential diagnosis as rounds of persona-conditioned specialist deliberation, and shows the recall advantage is not reproduced by best-of-n sampling from the same model, concentrates entirely in the cases where monolithic inference fails, and reverses on the easiest quartile.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
