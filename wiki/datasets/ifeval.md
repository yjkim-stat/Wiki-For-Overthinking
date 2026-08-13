# IFEval

<!-- auto:begin -->

A benchmark of prompts carrying verifiable formatting and constraint instructions, so compliance is checked programmatically rather than judged. Neither source studies it; both use it as the breadth check that a method developed on mathematical reasoning has not damaged instruction following. One includes it among nine benchmarks spanning mathematics, code, instruction following and multi-task knowledge, where a label-free RLVR method stays competitive with a supervised oracle. The other includes it in the twelve-benchmark suite over which a hidden-state norm signal is validated, though its reported comparisons run on the mathematics and knowledge sets rather than this one. Note that the archive also holds this benchmark under the separate name IF-Eval, so a definition written from the sources attached to either name sees only part of the evidence.

- **Kind**: dataset
- **Also called**: IF-Eval, IFEval
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [BBH](bbh.md), [credit assignment](../concepts/credit-assignment.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [entropy collapse](../concepts/entropy-collapse.md), [Gemma-3-4B](../models/gemma-3-4b.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [instruction following](../concepts/instruction-following.md), [KL divergence](../concepts/kl-divergence.md), [LiveCodeBench](livecodebench.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [majority voting](../methods/majority-voting.md), [MATH](math.md), [MATH-500](math-500.md), [MMLU-Pro](mmlu-pro.md), [outcome reward](../concepts/outcome-reward.md), [overthinking](../concepts/overthinking.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-8B](../models/qwen3-8b.md), [reward hacking](../concepts/reward-hacking.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [TruthfulQA](truthfulqa.md)

## Appears in

- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) — Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
