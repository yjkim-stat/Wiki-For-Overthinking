# semantic path convergence

<!-- auto:begin -->

Semantic path convergence is the pattern one archived source finds when, at each step of a stepwise truncation sweep, it samples several independent answer continuations, embeds them with the Qwen3 Embedding model and projects them by PCA: early steps scatter widely and the per-step centroid jumps between adjacent steps, then the trajectory enters a stable neighbourhood and stays inside it, with 97.3 percent of post-transition points falling within a 95 percent Mahalanobis confidence ellipse around the convergence centre (94.3 and 96.5 percent on two further instances). Quantitatively the source measures a global convergence residual D_global(k) = KL(Q_k || Q_inf) between the induced content distribution at step k, approximated as a Gaussian in a higher-dimensional PCA space, and a terminal reference estimated from a tail window of late truncation steps; the residual falls sharply and then flattens. The plateau is explicitly non-zero, which the source reads as a dynamic equilibrium inside the basin, that is repetitive oscillation among semantically similar continuations, rather than collapse onto a single solution.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-8B](../models/deepseek-r1-distill-8b.md), [DEER](../methods/deer.md), [entropy collapse](entropy-collapse.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [MATH500](../datasets/math500.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [Reasoning Completion Point (RCP)](reasoning-completion-point-rcp.md), [S-GRPO](../methods/s-grpo.md), [stepwise truncation protocol](../methods/stepwise-truncation-protocol.md), [thinking-content compensation](thinking-content-compensation.md)

## Appears in

- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/local-7c50df663462f26b/summary.md) — Defines an instance-specific Reasoning Completion Point (RCP) as the earliest truncation step at which both content-length stabilization and semantic-distribution convergence hold, and detects it online by monitoring the rank of the </think> token, cutting tokens up to 44% while preserving accuracy across four Qwen3 scales and DeepSeek-R1-Distill-8B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
