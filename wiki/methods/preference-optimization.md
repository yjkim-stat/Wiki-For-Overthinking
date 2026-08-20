# preference optimization

<!-- auto:begin -->

Training on pairs of preferred and dispreferred outputs rather than on a scalar reward, used by three sources to install a behaviour and by one to question the signal itself. One feeds the model's own self-certainty into the preference objective so confident answers compress and uncertain ones keep deliberating. One builds pairs from model-generated counterfactual reasoning traces to unlearn knowledge from the CoT as well as the answer, iterating to increase divergence from the original model. One forms pairs by pruning non-essential reasoning segments. The fourth undercuts the common source of preference labels, finding LLM-judge preferences track style rather than safety, world knowledge or instruction following.

- **Kind**: method
- **Also called**: DPO, ORPO, preference learning, preference tuning
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [alignment](../concepts/alignment.md), [AlpacaEval](../datasets/alpacaeval.md), [calibration](calibration.md), [chain of thought](chain-of-thought.md), [construct validity](../concepts/construct-validity.md), [DPO](dpo.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [instruction following](../concepts/instruction-following.md), [Llama-3-8B](../models/llama-3-8b.md), [LLM-as-a-judge](llm-as-a-judge.md), [machine unlearning](../concepts/machine-unlearning.md), [memorization](../concepts/memorization.md), [meta-evaluation](../concepts/meta-evaluation.md), [Mistral-7B-v0.3](../models/mistral-7b-v0-3.md), [MMLU](../datasets/mmlu.md), [MT-Bench](../datasets/mt-bench.md), [overthinking](../concepts/overthinking.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning redundancy](../concepts/reasoning-redundancy.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-certainty](self-certainty.md), [self-consistency](self-consistency.md), [supervised fine-tuning](supervised-fine-tuning.md), [token selection](../concepts/token-selection.md)

## Appears in

- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) — Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-industry-152/summary.md) — Feeds a reasoning model's own self-certainty into preference optimization so it compresses confident answers and keeps deliberating on uncertain ones.
- [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-143/summary.md) — Reframes unlearning in reasoning models as an intervention on the CoT itself, having the model generate logically valid counterfactual traces and iteratively preference-tuning toward them.
- [Your Reasoning Model Knows What Counts: Self-Guided Chain-of-Thought Pruning for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-25/summary.md) — Prunes chain-of-thought segments the model's own likelihood landscape marks as extraneous, then trains on the resulting pruning preference pairs.
- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](../../archive/papers/2025/local-503d1e9598036375/summary.md) — Builds a large standardized meta-benchmark and finds that LLM-judge preference scores do not correlate with concrete measures of safety, world knowledge or instruction following, because judges systematically prioritize style over factuality and safety.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
