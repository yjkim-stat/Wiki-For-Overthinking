# catastrophic forgetting

<!-- auto:begin -->

Loss of previously held capability when a model is trained further, which both sources treat as a routine consequence of reasoning post-training rather than an edge case. One measures it: prolonged RLVR degrades foundational skills including perception and faithfulness, and KL regularization does not prevent it because the penalty is computed on the current task. The other locates it in parameter space, reporting that reasoning ability sits in regions of low gradient sensitivity — not in high-magnitude parameters as usually assumed — which would explain why merging and pruning damage reasoning disproportionately. That faithfulness is among the capabilities lost would mean some of the archive's faithfulness findings are a consequence of reasoning training rather than a property of models.

- **Kind**: concept
- **Also called**: capability collapse, capability regression, general-capability forgetting
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [chain of thought faithfulness](chain-of-thought-faithfulness.md), [component ablation](../methods/component-ablation.md), [credit assignment](credit-assignment.md), [GPT-4o](../models/gpt-4o.md), [GRPO](../methods/grpo.md), [KL regularization](../methods/kl-regularization.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [localization](localization.md), [MedCalc-Bench](../datasets/medcalc-bench.md), [model merging](../methods/model-merging.md), [modularity](modularity.md), [o1-mini](../models/o1-mini.md), [outcome reward](outcome-reward.md), [PPO](../methods/ppo.md), [process reward](process-reward.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [REINFORCE](../methods/reinforce.md), [reward shaping](reward-shaping.md), [reward sparsity](reward-sparsity.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](training-dynamics.md)

## Appears in

- [MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning](../../archive/papers/2026/arxiv-2608-08623/summary.md) — Replaces the single tolerance threshold that RLVR uses to score floating-point answers with a hybrid reward pairing a hard clinical-safety constraint against a continuous precision-sensitive term, and adds a reward for stating the computational formula explicitly so an external verifier can check it.
- [ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2201/summary.md) — Merges a reasoning model into a domain-specialized one after finding that reasoning ability resides in low-gradient-sensitivity parameter regions rather than high-magnitude ones.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — Confirms that prolonged RLVR makes models forget foundational skills, and counters it with experience replay whose objective weights adapt online to convergence and instability signals.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
