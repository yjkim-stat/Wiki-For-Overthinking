# Reasoning Completion Point (RCP)

<!-- auto:begin -->

The Reasoning Completion Point is the earliest step of a large reasoning model's thinking trajectory at which its emerging answer has stopped changing in two independent senses at once: the content the model would produce if forced to stop there has stabilized in length (Delta_content(k) <= eps_c), and the distribution over that induced content has converged toward its terminal form (D_global(k) = KL(Q_k || Q_inf) <= eps_D). Its single archived source uses the point to split a trace into a Pre-RCP active-reasoning stage, where further thinking is typically still needed for the answer to mature, and a Post-RCP converged stage, where additional steps no longer materially alter the induced content and accumulate as redundancy. The point is latent and instance-specific, so no fixed thinking-token budget locates it, and computing it requires sampling several continuations at every truncation step, which makes it obtainable only offline; the source therefore uses it as gold supervision for an online detector rather than applying it directly. It is reported to coincide typically with the first emergence of the final answer in the trace, though the source notes answer emergence itself is an unreliable detection target because answer surface forms vary.

- **Kind**: concept
- **Also called**: RCP
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1-Distill-8B](../models/deepseek-r1-distill-8b.md), [DEER](../methods/deer.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Latent reasoning](latent-reasoning.md), [MATH500](../datasets/math500.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-30B-A3B](../models/qwen3-30b-a3b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [S-GRPO](../methods/s-grpo.md), [semantic path convergence](semantic-path-convergence.md), [stepwise truncation protocol](../methods/stepwise-truncation-protocol.md), [thinking-content compensation](thinking-content-compensation.md)

## Appears in

- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/local-7c50df663462f26b/summary.md) — Defines an instance-specific Reasoning Completion Point (RCP) as the earliest truncation step at which both content-length stabilization and semantic-distribution convergence hold, and detects it online by monitoring the rank of the </think> token, cutting tokens up to 44% while preserving accuracy across four Qwen3 scales and DeepSeek-R1-Distill-8B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
