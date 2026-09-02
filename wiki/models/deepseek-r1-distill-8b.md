# DeepSeek-R1-Distill-8B

<!-- auto:begin -->

DeepSeek-R1-Distill-8B is a distilled reasoning-model checkpoint used in 'The Evolution of Thought' as one of the backbones on which RCPD -- an online detector for the paper's Reasoning Completion Point (RCP), the instance-specific point where an LRM's chain-of-thought has semantically converged and further reasoning becomes redundant -- is evaluated. RCPD monitors the rank of the </think> token to catch this point and truncate post-RCP reasoning, cutting tokens up to 44% while preserving or improving accuracy-per-token across four models and three benchmarks.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DEER](../methods/deer.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [MATH500](../datasets/math500.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Reasoning Completion Point (RCP)](../concepts/reasoning-completion-point-rcp.md), [S-GRPO](../methods/s-grpo.md), [semantic path convergence](../concepts/semantic-path-convergence.md), [stepwise truncation protocol](../methods/stepwise-truncation-protocol.md), [thinking-content compensation](../concepts/thinking-content-compensation.md)

## Appears in

- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/local-7c50df663462f26b/summary.md) — Defines an instance-specific Reasoning Completion Point (RCP) as the earliest truncation step at which both content-length stabilization and semantic-distribution convergence hold, and detects it online by monitoring the rank of the </think> token, cutting tokens up to 44% while preserving accuracy across four Qwen3 scales and DeepSeek-R1-Distill-8B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
