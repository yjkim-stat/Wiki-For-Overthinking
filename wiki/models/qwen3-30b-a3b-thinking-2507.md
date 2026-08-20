# Qwen3-30B-A3B-Thinking-2507

<!-- auto:begin -->

A mixture-of-experts reasoning checkpoint with roughly 3B active parameters, and in both sources the strongest single-response configuration in its roster. One uses it as the teacher generating clean reasoning traces for a poisoning curriculum — so it supplies the benign reasoning that a backdoored model is trained to keep emitting. The other reports it as the highest single-response accuracy in a twenty-configuration sweep at 75.56%, and makes it the model on which the sharpest reducer result is measured: selecting by mean token log probability *falls* to 65.83% as the candidate bank grows to eighty, on the same banks where answer plurality rises to 78.33%. Its recurrence is as the strong open baseline whose behaviour under aggregation is worth measuring precisely because its single-sample accuracy is already high.

- **Kind**: model
- **Also called**: Qwen3-30B-A3B-Thinking
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BBH](../datasets/bbh.md), [beam search](../methods/beam-search.md), [BeaverTails](../datasets/beavertails.md), [best-of-n](../methods/best-of-n.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [Brumo](../datasets/brumo.md), [budget forcing](../methods/budget-forcing.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [CMIMC](../datasets/cmimc.md), [construct validity](../concepts/construct-validity.md), [curriculum learning](../methods/curriculum-learning.md), [DeepSeek-R1](deepseek-r1.md), [Gemma-4-12B](gemma-4-12b.md), [GPT-4o](gpt-4o.md), [GPT-4o-mini](gpt-4o-mini.md), [gpt-oss-20b](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [KL regularization](../methods/kl-regularization.md), [linear probe](../methods/linear-probe.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MMLU-Pro](../datasets/mmlu-pro.md), [monitorability](../concepts/monitorability.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [pass@k](../concepts/pass-k.md), [Phi-4-reasoning](phi-4-reasoning.md), [process reward model](../concepts/process-reward-model.md), [Qwen3.5-9B](qwen3-5-9b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time scaling](../concepts/test-time-scaling.md), [Tree of Thoughts](../methods/tree-of-thoughts.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Evading Chain-of-Thought Monitoring Through Model Poisoning](../../archive/papers/2026/arxiv-2608-02820/summary.md) — Shows that supervised fine-tuning can install a triggered backdoor whose visible reasoning stays clean, correct and topically benign while the final answer is attacker-chosen — leaving CoT-only monitors at chance (AUC 0.44-0.55) and recovering detection only when the monitor is shown the answer alongside the trace (0.76-1.00).
- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
