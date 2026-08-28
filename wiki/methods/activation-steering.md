# activation steering

<!-- auto:begin -->

Controlling how long or how a reasoning model thinks by modifying its internal activations at inference time, rather than by prompting or retraining it. Sources here use it on two objects: a direction in activation space along which overthinking varies, which is projected out or subtracted, and a trajectory through latent states, where the intervention nudges transitions rather than a single vector. The archive now also records the method's ceiling: single-direction steering plateaus and then degrades accuracy as intervention strength rises, which is what motivates the later variants -- sparse, orthogonal edits applied at sentence boundaries and scored by an estimate of a transition's long-horizon utility rather than by one global direction. Reported token savings reach 71% at maintained or improved accuracy, but only for the strength range below that plateau.

- **Kind**: method
- **Also called**: Activation Steering, manifold steering, representation engineering
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [AQuA-RAT](../datasets/aqua-rat.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DEER](deer.md), [DEER (baseline)](deer-baseline.md), [Dynasor](dynasor.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [GSM8K-Hard](../datasets/gsm8k-hard.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](manifold-steering.md), [MATH500](../datasets/math500.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [mechanistic interpretability analysis](mechanistic-interpretability-analysis.md), [NoThinking](nothinking.md), [NOWAIT](nowait.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [QwQ-32B](../models/qwq-32b.md), [SEAL](seal.md), [SEAL (baseline)](seal-baseline.md), [StrategyQA](../datasets/strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [TrimR](trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Activation Steering for Chain-of-Thought Compression](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1828/summary.md) — Shows via t-SNE that verbose and concise chains-of-thought occupy visibly separable regions of a reasoning model's intermediate activation space, then learns a single, KL-trust-region-constrained steering vector (Contrastive Energy-Based Steering, CES) from only 100 verbose-concise CoT pairs by ranking concise traces below verbose ones in length-normalized energy under the steered model -- Activation-Steered Compression (ASC) cuts CoT length up to 69.35% with no accuracy loss across four model scales and multiple benchmarks, achieves 2.7x end-to-end wall-clock speedup, generalizes cross-task with 0.92 cosine similarity between dataset-specific steering vectors, and mitigates a documented 'underthinking' failure mode (excessive backtracking/path-switching without commitment) in QwQ-32B specifically.
- [Base Models Know How to Reason, Thinking Models Learn When](../../archive/papers/2026/title-04d88374347ad37c/summary.md) — By decomposing the base-to-thinking model difference into reasoning mechanisms (steering vectors that induce a behaviour) and reasoning heuristics (a classifier deciding when the behaviour fires), the paper finds that hybrid models recover about 76% of the RL base-to-thinking gap but only about 11% of the SFT-distillation gap, indicating RL mainly teaches when to invoke reasoning behaviours the base model already has.
- [Modeling Hierarchical Thinking in Large Reasoning Models](../../archive/papers/2026/title-7651639ee2f29946/summary.md) — Models a large reasoning model's chain-of-thought as transitions among six latent cognitive states and uses that abstraction to steer generation toward better reasoning policies at inference time, without training.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
