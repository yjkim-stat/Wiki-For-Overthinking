# Phi-4-reasoning

<!-- auto:begin -->

A reasoning model trained by curated supervised traces followed by outcome-based reinforcement learning, cited by both sources as a reference point in the open reasoning ecosystem rather than analysed. One names it among the releases that made deliberate reasoning an explicit design target rather than a prompting artifact, in its chronology of how test-time inference and model-side training co-evolved. The other includes its family among the models over which a hidden-state norm signal is validated. Its presence marks one of the two dominant recipes — verified supervised traces plus outcome reinforcement — that this archive's training results are measured against.

- **Kind**: model
- **Also called**: Phi-4-Reasoning, Phi-4-reasoning-plus
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BBH](../datasets/bbh.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [Brumo](../datasets/brumo.md), [budget forcing](../methods/budget-forcing.md), [CMIMC](../datasets/cmimc.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [Gemma-3-4B](gemma-3-4b.md), [GPQA](../datasets/gpqa.md), [gpt-oss-20b](gpt-oss-20b.md), [GSM8K](../datasets/gsm8k.md), [HMMT](../datasets/hmmt.md), [IFEval](../datasets/ifeval.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [overthinking](../concepts/overthinking.md), [pass@k](../concepts/pass-k.md), [process reward model](../methods/process-reward-model.md), [PubMedQA](../datasets/pubmedqa.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-30B-A3B-Thinking-2507](qwen3-30b-a3b-thinking-2507.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3.6-35B-A3B](qwen3-6-35b-a3b.md), [Qwen3-8B](qwen3-8b.md), [reproducibility](../concepts/reproducibility.md), [reward hacking](../concepts/reward-hacking.md), [self-consistency](../methods/self-consistency.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [test-time scaling](../concepts/test-time-scaling.md), [Tree of Thoughts](../methods/tree-of-thoughts.md), [TruthfulQA](../datasets/truthfulqa.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — Formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, separates three structurally different regimes that a single scalar budget conflates, specifies what a reproducible inference protocol must declare, and releases 1.9 million traces — with the empirical section showing a selection score that makes accuracy fall from 75.56% to 65.83% as the candidate bank grows.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
