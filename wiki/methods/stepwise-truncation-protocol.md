# stepwise truncation protocol

<!-- auto:begin -->

The stepwise truncation protocol is the instrument one archived source uses to measure how each reasoning step contributes to the final answer. A thinking trajectory is segmented into sentence-level steps with NLTK, and for each step k the trajectory is cut immediately after s_k and the end-of-thinking delimiter (for example </think>) is force-injected, so the model must produce its answer from the prefix alone: y_k ~ P(y | x, t_{1:k}). Sweeping k yields, per instance, thinking length against induced content length and answer correctness, and the same construction is the substrate for the source's semantic probe, since several continuations can be sampled independently at each truncated prefix. The source frames the injected delimiter as an explicit control signal that terminates the internal thinking process and triggers the transition to content generation, rather than as a naive string cut.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Budget Forcing](budget-forcing.md), [DeepSeek-R1-Distill-8B](../models/deepseek-r1-distill-8b.md), [DEER](deer.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [MATH500](../datasets/math500.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [Reasoning Completion Point (RCP)](../concepts/reasoning-completion-point-rcp.md), [S-GRPO](s-grpo.md), [semantic path convergence](../concepts/semantic-path-convergence.md), [thinking-content compensation](../concepts/thinking-content-compensation.md)

## Appears in

- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/local-7c50df663462f26b/summary.md) — Defines an instance-specific Reasoning Completion Point (RCP) as the earliest truncation step at which both content-length stabilization and semantic-distribution convergence hold, and detects it online by monitoring the rank of the </think> token, cutting tokens up to 44% while preserving accuracy across four Qwen3 scales and DeepSeek-R1-Distill-8B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
