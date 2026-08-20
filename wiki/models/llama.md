# Llama

<!-- auto:begin -->

The model family that, with Qwen, supplies most of this archive's empirical base -- 4 sources refer to it generically. The entry records the dependency: results measured on one family frequently shrink or reverse on the other, and the archive's better sources include both for that reason. Two family-level observations appear: it is one of the two families in contamination-detection calibration work, and it is used generically in the position paper arguing that reading intermediate tokens as reasoning is unsupported.

- **Kind**: model
- **Also called**: LLaMA, Llama 3.1, Llama family
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [ablation](../methods/ablation.md), [benchmark contamination](../concepts/benchmark-contamination.md), [bootstrap resampling](../methods/bootstrap-resampling.md), [calibration](../concepts/calibration.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [commitment boundary](../concepts/commitment-boundary.md), [decontamination](../methods/decontamination.md), [DeepSeek](deepseek.md), [DeepSeek-R1](deepseek-r1.md), [distribution shift](../concepts/distribution-shift.md), [GPT-5](gpt-5.md), [GPT-OSS](gpt-oss.md), [GRPO](../methods/grpo.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B](llama-3-1-8b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [localization](../concepts/localization.md), [membership inference](../concepts/membership-inference.md), [Monte Carlo tree search](../methods/monte-carlo-tree-search.md), [operating point](../concepts/operating-point.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [post-training](../concepts/post-training.md), [process reward model](../methods/process-reward-model.md), [Qwen](qwen.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [RLVR](../methods/rlvr.md), [ROC analysis](../methods/roc-analysis.md), [self-consistency](../methods/self-consistency.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [sycophancy](../concepts/sycophancy.md), [test-time scaling](../concepts/test-time-scaling.md), [Wasserstein distance](../methods/wasserstein-distance.md)

## Appears in

- [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](../../archive/papers/2026/arxiv-2608-10462/summary.md) — Calibrates feature-based data-contamination detectors against the systematic feature shifts that post-training introduces, by measuring how controlled prompt variants move scores on known non-members and then correcting only the recurring shift directions, with the gains concentrated at the low-false-positive operating point rather than in AUC.
- [INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators](../../archive/papers/2026/arxiv-2608-10492/summary.md) — Fine-tunes student simulators on paired internal-dialogue traces and code edits rather than on actions alone, and measures the result on two axes at once -- how closely generated code matches the distribution of real student submissions, and how well the generated reasoning explains the specific edit that followed.
- [Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-20/summary.md) — Locates the sentences in a reasoning trace that commit a model to agreeing with an incorrect user suggestion, using counterfactual rollouts and linear probes.
- [Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!](../../archive/papers/2026/local-e62f069bc5144f28/summary.md) — A position paper arguing that reading a reasoning model's intermediate tokens as 'reasoning' or 'thinking' is unsupported by the available evidence and actively harmful, and collating experiments in which trace semantics and solution accuracy come apart.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
